# Homework 1
* Brief [instruction] and [installation] for [Homework1].
* For detailed execution commands, see [run_hw1.ipynb].

## Note
* Implemented algorithms:
  * [x] Behavior Cloning
  * [x] DAgger (Dataset Aggregation)
* I do 3.2 first, do grid search on Ant and select a set of hyperparameters and run on all four tasks with BC and DA. Although the homework       only ask us to choose two of four, I just try all of them.
* Use hyperparameters:
  ```python
  num_agent_train_steps_per_iter = 10000
  train_batch_size = 200
  size = 64
  ```
  `num_agent_train_steps_per_iter = 10000` is a little bit overkill, just for evaluation of all tasks can achieve at least 30% of the             performance of the expert. ：P

## Result
* Learning curves
  * Grid search
    (x-axis: second)
    [grid search]
  * Eval of trained agent vs. the expert
    (x-axis: iteration)
    [eval][train]
* Evaluation rollouts



[instruction]: instruction.md
[installation]: installation.md
[Homework1]: https://rail.eecs.berkeley.edu/deeprlcourse/deeprlcourse/static/homeworks/hw1.pdf
[run_hw1.ipynb]: cs285/scripts/run_hw1.ipynb
[grid search]: <results/grid search.png>
[eval]: results/eval.png
[train]: results/train.png
