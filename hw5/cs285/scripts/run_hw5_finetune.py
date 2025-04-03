import os
import time
import argparse
import pickle

from cs285.agents import agents as agent_types
from cs285.envs import Pointmass

import gym
import numpy as np
import torch
from cs285.infrastructure import pytorch_util as ptu
import tqdm

from cs285.infrastructure import utils
from cs285.infrastructure.logger import Logger
from cs285.infrastructure.replay_buffer import ReplayBuffer

from scripting_utils import make_logger, make_config
from run_hw5_explore import visualize

MAX_NVIDEO = 2


def run_training_loop(config: dict, logger: Logger, args: argparse.Namespace):
    # set random seeds
    np.random.seed(args.seed)
    torch.manual_seed(args.seed)
    ptu.init_gpu(use_gpu=not args.no_gpu, gpu_id=args.which_gpu)

    # make the gym environment
    env = config["make_env"]()
    epsilon = None
    exploration_schedule = config.get("exploration_schedule", None)
    discrete = isinstance(env.action_space, gym.spaces.Discrete)

    assert discrete, "DQN only supports discrete action spaces"

    agent_cls = agent_types[config["agent"]]
    agent = agent_cls(
        env.observation_space.shape,
        env.action_space.n,
        **config["agent_kwargs"],
    )

    ep_len = env.spec.max_episode_steps or env.max_episode_steps

    # observation = None

    # Replay buffer
    replay_buffer = ReplayBuffer(capacity=config["total_steps"])
    
    ## 1. first loading an offline dataset
    with open(os.path.join(args.dataset_dir, f"{config['dataset_name']}.pkl"), "rb") as f:
        dataset = pickle.load(f)
    replay_buffer.initialize_with_dataset(dataset)
    
    dataset_size = len(dataset)
    print('dataset size:', dataset_size)
    print('buffer size:', replay_buffer.max_size)

    observation = env.reset()

    recent_observations = []

    num_offline_steps = config["offline_steps"]
    # num_online_steps = config["total_steps"] - num_offline_steps

    for step in tqdm.trange(1, config["total_steps"]+1, dynamic_ncols=True):
        # TODO(student): Borrow code from another online training script here. Only run the online training loop after `num_offline_steps` steps.
        ## 3. switching to online learning while keeping all of the data in the dataset to initialize your replay buffer
        if step > num_offline_steps:
            if exploration_schedule is not None:
                # ConstantSchedule is used in this hw, so step makes no difference.
                epsilon = exploration_schedule.value(step)
                action = agent.get_action(observation, epsilon)
            else:
                action = agent.get_action(observation)
                
            next_observation, reward, done, info = env.step(action)
            truncated = info.get("TimeLimit.truncated", False)
            
            replay_buffer.insert(observation=observation,
                                 action=action,
                                 reward=reward,
                                 next_observation=next_observation,
                                 done=done and not truncated)
            recent_observations.append(observation)

            if done:
                observation = env.reset()
                
                logger.log_scalar(info["episode"]["r"], "train_return", step)
                logger.log_scalar(info["episode"]["l"], "train_ep_len", step)
            else:
                observation = next_observation

        ## 2. taking a fixed number of training steps with an offline RL algorithm
        # Main training loop
        batch = replay_buffer.sample(config["batch_size"])

        # Convert to PyTorch tensors
        batch = ptu.from_numpy(batch)

        update_info = agent.update(
            batch["observations"],
            batch["actions"],
            batch["rewards"],  # use normal rewards here!
            batch["next_observations"],
            batch["dones"],
            step,
        )

        # Logging code
        if epsilon is not None:
            update_info["epsilon"] = epsilon

        if step % args.log_interval == 0:
            for k, v in update_info.items():
                logger.log_scalar(v, k, step)
            logger.flush()

        if step % args.eval_interval == 0:
            # Evaluate
            trajectories = utils.sample_n_trajectories(
                env,
                agent,
                args.num_eval_trajectories,
                ep_len,
            )
            returns = [t["episode_statistics"]["r"] for t in trajectories]
            ep_lens = [t["episode_statistics"]["l"] for t in trajectories]

            logger.log_scalar(np.mean(returns), "eval_return", step)
            logger.log_scalar(np.mean(ep_lens), "eval_ep_len", step)

            if len(returns) > 1:
                logger.log_scalar(np.std(returns), "eval/return_std", step)
                logger.log_scalar(np.max(returns), "eval/return_max", step)
                logger.log_scalar(np.min(returns), "eval/return_min", step)
                logger.log_scalar(np.std(ep_lens), "eval/ep_len_std", step)
                logger.log_scalar(np.max(ep_lens), "eval/ep_len_max", step)
                logger.log_scalar(np.min(ep_lens), "eval/ep_len_min", step)

            # log walking trajectories
            env_pointmass: Pointmass = env.unwrapped
            logger.log_figures(
                [env_pointmass.plot_trajectory(trajectory["next_observation"]) for trajectory in trajectories],
                "trajectories",
                step,
                "eval"
            )

        # log exploration trajectories
        if step % args.visualize_interval == 0 and step > num_offline_steps:
            env_pointmass: Pointmass = env.unwrapped
            observations = np.stack(recent_observations)
            recent_observations = []
            logger.log_figure(
                visualize(env_pointmass, agent, observations),
                "exploration_trajectories",
                step,
                "eval",
            )

    # average of the last eval
    print(f"Average eval return: {np.mean(returns)}")

    # Save the final dataset
    # dataset_file = os.path.join(args.dataset_dir, f"{config['dataset_name']}.pkl")
    # with open(dataset_file, "wb") as f:
    #     pickle.dump(replay_buffer, f)
    #     print("Saved dataset to", dataset_file)

    # render last `dataset_size` step exploration
    last_step_idxs = np.arange(replay_buffer.size-dataset_size, replay_buffer.size) % replay_buffer.max_size
    fig = visualize(
        env_pointmass, agent, replay_buffer.observations[last_step_idxs]
    )
    fig.suptitle(f"Last {dataset_size} state coverage")
    filename = os.path.join("exploration_visualization", f"finetune_{config['log_name']}.png")
    fig.savefig(filename)
    print("Saved final heatmap to", filename)
    
    # Render final heatmap
    fig = visualize(
        env_pointmass, agent, replay_buffer.observations[: config["total_steps"]]
    )
    fig.suptitle(f"State coverage")
    filename = os.path.join("exploration_visualization", f"finetune_totalsteps_{config['log_name']}.png")
    fig.savefig(filename)
    print("Saved final heatmap to", filename)


banner = """
======================================================================
Exploration

Generating the dataset for the {env} environment using algorithm {alg}.
The results will be stored in {dataset_dir}.
======================================================================
"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file", "-cfg", type=str, required=True)

    parser.add_argument("--eval_interval", "-ei", type=int, default=10000)
    parser.add_argument("--visualize_interval", "-vi", type=int, default=1000)
    parser.add_argument("--num_eval_trajectories", "-neval", type=int, default=10)

    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--no_gpu", "-ngpu", action="store_true")
    parser.add_argument("--which_gpu", "-gpu_id", default=0)
    parser.add_argument("--log_interval", type=int, default=1)

    parser.add_argument("--use_reward", action="store_true")
    parser.add_argument("--dataset_dir", type=str, required=True)

    parser.add_argument("--env_name", type=str, default="")
    parser.add_argument("--dataset_name", type=str, default="")

    args = parser.parse_args()
    print(args)  # show hyperparameters

    # create directory for logging
    logdir_prefix = "hw5_finetune_"  # keep for autograder

    extra_args = {"env_name": args.env_name,
                  "dataset_name": args.dataset_name}
    config = make_config(args.config_file, extra_args)
    logger = make_logger(logdir_prefix, config)

    os.makedirs(args.dataset_dir, exist_ok=True)
    # print(
    #     banner.format(
    #         env=config["env_name"], alg=config["agent"], dataset_dir=args.dataset_dir
    #     )
    # )

    run_training_loop(config, logger, args)


if __name__ == "__main__":
    main()
