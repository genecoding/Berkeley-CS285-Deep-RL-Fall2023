# Homework 3
* [Homework3].
* For detailed execution commands, see [run_hw3_dqn.ipynb] and [run_hw3_sac.ipynb].

# Note
* Implemented algorithms:
  * [x] Q Learning
  * [x] Double Q Learning
  * [x] SAC (Soft Actor Critic)

# Troubleshooting
Fix two bugs in `MemoryEfficientReplayBuffer`.

# Result
* 2.4 Basic Q-Learning
  * Debug your DQN implementation on CartPole-v1.
  * Run DQN on CartPole-v1, but change the learning rate to 0.05.
    * Learning curves  
      (x-axis: environment steps)
      <div>
       <img src="results/dqn_cartpole eval.png" width="32%" />
       <img src="results/dqn_cartpole qvalue.png" width="32%" />
       <img src="results/dqn_cartpole critic loss.png" width="32%" />
      </div>
  * Run DQN with three different seeds on LunarLander-v2.
    * Learning curves
      <div>
       <img src="results/dqn_lunarlander.png" width="55%" />
      </div>
      Q-Learning might be unstable.
    * Evaluation rollouts
      | s1               | s2               | s3                |
      |:----------------:|:----------------:|:-----------------:|
      |![lunarlander_s1] |![lunarlander_s2] |![lunarlander_s3]  |
* 2.5 Double Q-Learning
  * Run three more seeds of the lunar lander problem.
    * Learning curves
      <div>
       <img src="results/dqn_lunarlander_doubleq.png" width="55%" />
      </div>
      Double Q-Learning shows more stablility.
    * Evaluation rollouts
      | s1               | s2               | s3                |
      |:----------------:|:----------------:|:-----------------:|
      |![doubleq_lunarlander_s1] |![doubleq_lunarlander_s2] |![doubleq_lunarlander_s3]  |
  * Run your DQN implementation on the MsPacman-v0 problem.
    * Learning curves
      * Train Return vs. 
      <div>
       <img src="results/dqn_mspacman eval return.png" width="48%" />
       <img src="results/dqn_mspacman train return.png" width="48%" />
      </div>
    * Evaluation rollouts
* 2.6 Experimenting with Hyperparameters  
  I choose `Space Invaders` and run with `learining rate = 1e-3, 5e-3, 1e-4, 5e-4`.
* 3.1.1 Bootstrapping
* 3.1.2 Entropy Bonus and Soft Actor-Critic
* 3.1.3 Actor with REINFORCE
* 3.1.4 Actor with REPARAMETRIZE
* 3.1.5 Stabilizing Target Values




[Homework3]: https://rail.eecs.berkeley.edu/deeprlcourse/deeprlcourse/static/homeworks/hw3.pdf
[run_hw3_dqn.ipynb]: run_hw3_dqn.ipynb
[run_hw3_sac.ipynb]: run_hw3_sac.ipynb
[lunarlander_s1]: results/dqn_lunarlander_s1.gif
[lunarlander_s2]: results/dqn_lunarlander_s2.gif
[lunarlander_s3]: results/dqn_lunarlander_s3.gif
[doubleq_lunarlander_s1]: results/doubleq_lunarlander_s1.gif
[doubleq_lunarlander_s2]: results/doubleq_lunarlander_s2.gif
[doubleq_lunarlander_s3]: results/doubleq_lunarlander_s3.gif
