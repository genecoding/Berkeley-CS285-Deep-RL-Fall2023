# Homework 1
* Brief [instruction] and [installation] for [Homework1].
* For detailed execution commands, see [run_hw1.ipynb].

## Note
* Implemented algorithms:
  * [x] Behavior Cloning
  * [x] DAgger (Dataset Aggregation)
* I do 3.2 first, I do grid search on `Ant` and select a set of hyperparameters, apply it to both BC and DA, and run on all four tasks. Although the homework only asks us to choose two of four, I just try all of them.
* Use hyperparameters:
  ```python
  num_agent_train_steps_per_iter = 10000
  train_batch_size = 200
  size = 64
  ```
  `num_agent_train_steps_per_iter = 10000` is a little bit overkill, just for evaluation of all tasks can achieve at least 30% of the performance of the expert. ：P

## Result
* Learning curves
  * Grid search  
    (x-axis: seconds)  
    <img src="results/grid search.png" width="55%" />
  * Behavior Cloning vs. DAgger (including the performance of the agent vs. the expert)  
    (x-axis: iterations)  
    <img src="results/eval.png" width="48%" />
    <img src="results/train.png" width="48%" />
* Evaluation rollouts
  |                  | Behavior Cloning | DAgger            |
  |:-----------------|:----------------:|:-----------------:|
  | Ant              |![bc_ant]         |![da_ant]          |
  | HalfCheetah      |![bc_halfcheetah] |![da_halfcheetah]  |
  | Hopper           |![bc_hopper]      |![da_hopper]       |
  | Walker2d         |![bc_walker2d]    |![da_walker2d]     |



[instruction]: instruction.md
[installation]: installation.md
[Homework1]: https://rail.eecs.berkeley.edu/deeprlcourse/deeprlcourse/static/homeworks/hw1.pdf
[run_hw1.ipynb]: cs285/scripts/run_hw1.ipynb
[bc_ant]: results/bc_ant.gif
[bc_halfcheetah]: results/bc_halfcheetah.gif
[bc_hopper]: results/bc_hopper.gif
[bc_walker2d]: results/bc_walker2d.gif
[da_ant]: results/da_ant.gif
[da_halfcheetah]: results/da_halfcheetah.gif
[da_hopper]: results/da_hopper.gif
[da_walker2d]: results/da_walker2d.gif
