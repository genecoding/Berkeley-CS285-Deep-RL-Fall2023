# Homework 5
* [Homework5]
* For detailed execution commands, see [run_hw5.ipynb].

## Note
* Implemented algorithms:
  * [x] 
  * [x] 
  * [x] 
  * [x] 
  * [x] 

## Troubleshooting
In `run_hw5_finetune.py`, use normal rewards when updating the agent: remove `* (1 if config.get("use_reward", False) else 0)`. I had tried `use_reward` flag, didn't work...

## Result
### 3 Exploration
* 3.1 Running a Random Policy
  | Easy             | Medium           | Hard             |
  |:----------------:|:----------------:|:----------------:|
  |![random_easy]    |![random_medium]  |![random_hard]    |
* 3.2 Random Network Distillation
### 4 Offline RL
* 4.1 CQL
* 4.2 Policy Constraint Methods: IQL and AWAC
* 4.3 Data Ablations
### 5 Online Fine-Tuning
### Bonus Problem

## Reference



[Homework5]: https://rail.eecs.berkeley.edu/deeprlcourse/deeprlcourse/static/homeworks/hw5.pdf
[run_hw5.ipynb]: run_hw5.ipynb
[random_easy]: exploration_visualization/PointmassEasy-v0_random.png
[random_medium]: exploration_visualization/PointmassMedium-v0_random.png
[random_hard]: exploration_visualization/PointmassHard-v0_random.png
