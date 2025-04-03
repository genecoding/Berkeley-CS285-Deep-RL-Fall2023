# Homework 2
* Brief [instruction] and [installation] for [Homework2].
* For detailed execution commands, see [run_hw2.ipynb].

## Note
* Implemented algorithms:
  * [x] Policy Gradient (with value function)
  * [x] GAE (Generalized Advantage Estimation)

## Result
* Experiment 1 (CartPole)
  * Learning curves
    * Small Batch vs. Large Batch  
      (x-axis: environment steps)
      <div>
       <img src="results/exp1.png" width="45%" />
       <img src="results/exp1_lb.png" width="45%" />
      </div>
  * Evaluation rollouts  
    (both with rtg & na)
    | small batch      | large batch      |
    |:----------------:|:----------------:|
    |![exp1_rtg_na]    |![exp1_lb_rtg_na] |
* Experiment 2 (HalfCheetah)
  * Learning curves
    * No Baseline vs. Baseline
      <div>
       <img src="results/exp2_baseline eval.png" width="45%" />
       <img src="results/exp2_baseline loss.png" width="45%" />
      </div>
    * Comparison of decreased bgs & blr
  * Evaluation rollouts
* Experiment 3 (LunarLander)
  * Learning curves
  * Evaluation rollouts
* Experiment 4 (InvertedPendulum)
  * Learning curves
  * Evaluation rollouts
* Experiment 5 (Humanoid)
  * Learning curves
  * Evaluation rollouts



[instruction]: instruction.md
[installation]: installation.md
[Homework2]: https://rail.eecs.berkeley.edu/deeprlcourse/deeprlcourse/static/homeworks/hw2.pdf
[run_hw2.ipynb]: cs285/scripts/run_hw2.ipynb
[exp1_rtg_na]: results/exp1_pg_cartpole_rtg_na.gif
[exp1_lb_rtg_na]: results/exp1_pg_cartpole_lb_rtg_na.gif
