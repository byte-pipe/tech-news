---
title: Ornith-1.5: From Self-Scaffolding to Self-Improvement | Ornith Blog
url: https://ornith.ai/ornith_1_5.html
date: 2026-08-19
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-20T07:17:31.791452
---

# Ornith-1.5: From Self-Scaffolding to Self-Improvement | Ornith Blog

# Ornith-1.5: From Self‑Scaffolding to Self‑Improvement

## Overview
- Introduces Ornith‑1.5, an end‑to‑end self‑improvement framework that expands the self‑scaffolding approach of Ornith‑1.0.  
- The model proposes new tasks, builds task‑specific scaffolds, and generates solution rollouts for reinforcement learning, creating a continuous learning loop.  

## Model Scales and Benchmark Performance
- Three scales: 397 Billion MoE, 35 Billion MoE, and 9 Billion dense.  
- **397 B MoE**: 86.1 on Terminal‑Bench 2.1, 56.0 on DeepSWE, matching Claude Opus 4.8 and surpassing open‑source peers (GLM‑5.2, DeepSeek‑V4‑Flash‑0731).  
- **35 B MoE**: Beats Qwen 3.6‑35B on coding and agentic tasks; with only 3 B active parameters per token, outperforms dense Gemma 4‑31B and Muse Glimmer‑30B (e.g., 68.5 vs 43.4 on agentic coding).  
- **9 B dense** (including mobile‑quantized version): Runs on iPhone/Android, achieves 47.0 on Terminal‑Bench 2.1 and 70.6 on SWE‑Bench Verified, matching or exceeding larger models like Gemma 4‑31B and Qwen 3.6‑35B.  

## Self‑Improvement Loop
- **Three training stages per cycle**:  
  1. **Task Generation** – given an environment, high‑level instructions, and past task history, the system proposes increasingly difficult tasks.  
  2. **Scaffold Construction** – creates or refines task‑specific instructions, tools, decomposition, and orchestration.  
  3. **Solution Rollout** – policy produces a rollout conditioned on the task and scaffold.  
- Rewards from rollouts are back‑propagated to all three stages, encouraging better tasks, more effective scaffolds, and higher‑quality solutions.  
- The loop continuously expands the curriculum, adapts problem‑solving strategies, and drives sustained gains across reasoning, coding, and agentic domains.  

## Task Reward Design
- Overall task reward: **R_task = V(q,s) × D(q,s,τ) × N(q)**, combining validity, frontier difficulty, and novelty.  
- **Validity (V)**: Checks that the question and scaffold form a coherent, solvable, and verifiable learning environment; invalid tasks receive zero reward.  
- **Frontier Difficulty (D)**: Uses rollout success rate \(p\) to reward tasks whose success probability is near a target frontier \(p^* = 0.2\); implemented with a Gaussian‑shaped function.  
- **Novelty (N)**: Penalizes similarity to previously generated tasks using a similarity buffer, ensuring diversity without overriding validity or difficulty.  

## Harness and Rollout Rewards (partial)
- Harness reward: **R_harness = C(q,h) × F(h,τ) × H(h)**, where:  
  - **C** measures alignment of the evaluation harness with the task.  
  - **F** assesses fidelity of rewards to true solution quality.  
  - **H** evaluates resistance to reward‑hacking.  

These components together guide Ornith‑1.5 to generate useful curricula, construct reliable evaluation environments, and improve its policy through self‑generated experience.