## Bonus Problem
* I try extra mazes which are: `'FlyTrapSmall', 'Tree', 'Spiral11x11', 'FlyTrapBig', 'Galton', 'Maze11x11', 'UMulti', 'Tunnel'`.
* I finetune `IQL` on these mazes and by results divide them into 3 groups, each has a set of hyperparameters. I also run `DQN` for comparison.
* Mazes in the 3rd group are more complex and the randomness is fixed in this homework, so the agent might not perform well at the last evaluation,
  so I train it longer and pick some good evaluations over the training.
* I had also finetuned CQL and AWAC on these mazes, some results look good and some need more finetune; since there are too many hyperparameters and I had already spent too much time on this,
  I decided to stop here.

### Exploration
```python
total_steps = 20000
```
* Exploration (RND) / Last 20000 steps during finetune training of DQN & IQL
  |                     | RND                 | DQN                 | IQL                 |
  |:--------------------|:-------------------:|:-------------------:|:-------------------:|
  | FlyTrapSmall        |![rnd_flytrapsmall]  |![dqn_flytrapsmall]  |![iql_flytrapsmall]  |
  | Tree                |![rnd_tree]          |![dqn_tree]          |![iql_tree]          |
  | Spiral11x11         |![rnd_spiral11x11]   |![dqn_spiral11x11]   |![iql_spiral11x11]   |
  | FlyTrapBig          |![rnd_flytrapbig]    |![dqn_flytrapbig]    |![iql_flytrapbig]    |
  | Galton              |![rnd_galton]        |![dqn_galton]        |![iql_galton]        |
  | Maze11x11           |![rnd_maze11x11]     |![dqn_maze11x11]     |![iql_maze11x11]     |
  | UMulti              |![rnd_umulti]        |![dqn_umulti]        |![iql_umulti]        |
  | Tunnel              |![rnd_tunnel]        |![dqn_tunnel]        |![iql_tunnel]        |

  If training succeeds, a path from the start to the goal would be emerged from trajectories of the agent.
  
### Group1
```python
mazes1 = ['FlyTrapSmall', 'Tree']
```
* Learning curves  
  Offline Training vs. Online Finetuning (including  DQN vs. IQL)  
  <img src="results/veryhard_flytrapsmall.png" width="55%" />
  <img src="results/veryhard_tree.png" width="55%" />
* Evaluation rollouts

### Group2
```python
mazes1 = ['FlyTrapSmall', 'Tree']
```
* Learning curves
* Evaluation rollouts

### Group3
```python
mazes1 = ['FlyTrapSmall', 'Tree']
```
* Learning curves
* Evaluation rollouts



[rnd_flytrapsmall]: exploration_visualization/PointmassVeryHard-FlyTrapSmall-v0_rnd1.0.png
[rnd_tree]: exploration_visualization/PointmassVeryHard-Tree-v0_rnd1.0.png
[rnd_spiral11x11]: exploration_visualization/PointmassVeryHard-Spiral11x11-v0_rnd1.0.png
[rnd_flytrapbig]: exploration_visualization/PointmassVeryHard-FlyTrapBig-v0_rnd1.0.png
[rnd_galton]: exploration_visualization/PointmassVeryHard-Galton-v0_rnd1.0.png
[rnd_maze11x11]: exploration_visualization/PointmassVeryHard-Maze11x11-v0_rnd1.0.png
[rnd_umulti]: exploration_visualization/PointmassVeryHard-UMulti-v0_rnd1.0.png
[rnd_tunnel]: exploration_visualization/PointmassVeryHard-Tunnel-v0_rnd1.0.png

[dqn_flytrapsmall]: exploration_visualization/finetune_PointmassVeryHard-FlyTrapSmall-v0_dqn.png
[dqn_tree]: exploration_visualization/finetune_PointmassVeryHard-Tree-v0_dqn.png
[dqn_spiral11x11]: exploration_visualization/finetune_PointmassVeryHard-Spiral11x11-v0_dqn.png
[dqn_flytrapbig]: exploration_visualization/finetune_PointmassVeryHard-FlyTrapBig-v0_dqn.png
[dqn_galton]: exploration_visualization/finetune_PointmassVeryHard-Galton-v0_dqn.png
[dqn_maze11x11]: exploration_visualization/finetune_PointmassVeryHard-Maze11x11-v0_dqn.png
[dqn_umulti]: exploration_visualization/finetune_PointmassVeryHard-UMulti-v0_dqn.png
[dqn_tunnel]: exploration_visualization/finetune_PointmassVeryHard-Tunnel-v0_dqn.png

[iql_flytrapsmall]: exploration_visualization/finetune_PointmassVeryHard-FlyTrapSmall-v0_iql0.99_temp10.0.png
[iql_tree]: exploration_visualization/finetune_PointmassVeryHard-Tree-v0_iql0.99_temp10.0.png
[iql_spiral11x11]: exploration_visualization/finetune_PointmassVeryHard-Spiral11x11-v0_iql0.99_temp10.0.png
[iql_flytrapbig]: exploration_visualization/finetune_PointmassVeryHard-FlyTrapBig-v0_iql0.99_temp10.0.png
[iql_galton]: exploration_visualization/finetune_PointmassVeryHard-Galton-v0_iql0.99_temp10.0.png
[iql_maze11x11]: exploration_visualization/finetune_PointmassVeryHard-Maze11x11-v0_iql0.99_temp10.0.png
[iql_umulti]: exploration_visualization/finetune_PointmassVeryHard-UMulti-v0_iql0.99_temp10.0.png
[iql_tunnel]: exploration_visualization/finetune_PointmassVeryHard-Tunnel-v0_iql0.99_temp10.0.png


