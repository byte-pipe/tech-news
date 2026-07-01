---
title: RL Octocopter -- Karolina Dubiel
url: https://karolina.mgdubiel.com/drone/
date: 2026-06-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-01T19:59:17.990636
---

# RL Octocopter -- Karolina Dubiel

# RL Octocopter – Karolina Dubiel

## Overview
- Demonstrates a simulated octocopter policy that survives single, dual, and some triple motor failures.  
- Initial focus was a fast, CPU‑only “sim‑only” policy before moving to full domain‑randomized training.  

## Training attempts timeline
| # | What was tried | Result |
|---|----------------|--------|
| 1 | Baseline PPO with high exploration, always 2 faults; ran overnight | Failed; entropy kept rising, crash at 20 M steps |
| 2 | Lowered exploration, kept always‑2‑faults, no curriculum | Appeared to work, but crashed at 2 M steps; stopped to add single‑motor failures |
| 3 | Added hover → single → dual curriculum | Broke everything; 4 M pure‑hover steps exposed two latent bugs |
| 4 | Operator error: two training processes wrote to the same checkpoint files | Caused corrupted checkpoints |
| 5 | Used residual actions (hover + action) | Commands saturated at ±3, leading to tip‑over in 7 steps |
| 6 | Stripped and re‑added curriculum with low exploration | 0 % success at every checkpoint; crashed at step 7 consistently, indicating a systemic bug |
| 7 | Applied two core fixes (see below) | Successful: hover learned by 0.5 M steps, 100 % survival on hover/single/dual by ~9.5 M steps |

## Core bugs and fixes
1. **Action saturation bug**  
   - PPO gradients were computed on unclipped actions while the environment clipped commands to [0, 1], causing motors to get stuck at the clip edge and produce lopsided tip‑overs.  
   - **Fix:** Apply a tanh squash as a residual around hover throttle, keeping commands within bounds and ensuring an untrained network already hovers. Survival increased from 7 steps to 205 steps.  

2. **Reward shaping bug**  
   - Hover reward (+0.1) was exactly cancelled by altitude penalty (‑0.1), giving no incentive to stay aloft; episodes that hovered then crashed received the same return as immediate crashes.  
   - **Fix:** Increase the survival bonus from 0.1 to 1.0, giving +0.9 per step of hover. PPO then learned to maintain altitude.  

## Results
- Final policy: 43.4 k‑parameter MLP.  
- Learning curve over 20 M steps shows increasing survival and reward across fault classes.  
- Generalizes to unseen triple‑motor failures when physical recovery is possible; even with three adjacent motors disabled, the drone fought for 7.2 s before sinking rather than tumbling.  
- “Uncompensatable‑yaw” cases (two same‑spin motors 90° apart) were actually manageable; policy kept heading drift within ~13°/s.  

## Next steps
- Develop a policy that can transfer from simulation to real hardware (sim‑to‑real).