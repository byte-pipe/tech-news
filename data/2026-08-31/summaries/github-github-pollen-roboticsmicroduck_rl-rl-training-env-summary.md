---
title: GitHub - pollen-robotics/microduck_rl: RL training environments for Microduck (mjlab) · GitHub
url: https://github.com/pollen-robotics/microduck_rl
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-31T02:23:03.915107
---

# GitHub - pollen-robotics/microduck_rl: RL training environments for Microduck (mjlab) · GitHub

# Microduck RL Repository Summary

## Overview
- Provides reinforcement‑learning (RL) training environments for **Microduck**, an ~800 g, ~25 cm tall bipedal robot.  
- Built on **mjlab (MuJoCo Warp)** and uses PPO for policy training.  
- Trained policies run at 50 Hz, are exported to ONNX, and deployed on the physical robot via the `pollen-robotics/microduck` runtime.  

## Key Features
- Complete sim‑to‑real pipeline: BAM actuator physics, domain randomization, backlash simulation, and reward‑design guidelines (see `AGENTS.md`).  
- Supports a variety of tasks (walking, standing, sit‑stand, ground pick, ball kick, rolls, roller‑skating, etc.) on flat, rough, and sloped terrains.  
- Backlash variants for each main task model gear play (±1°) without changing observation or action dimensions.  
- High‑fidelity actuator model (BAM M6) for Dynamixel XL330, including voltage control, back‑EMF, and load‑dependent friction.  

## Quickstart Instructions
1. **Prerequisites**: CUDA‑capable GPU, `uv` package manager.  
2. **Clone**: `git clone https://github.com/pollen-robotics/microduck_rl && cd microduck_rl`.  
3. **Train** (example):  
   ```bash
   uv run train Mjlab-Velocity-Flat-MicroDuck --env.scene.num-envs 4096
   ```  
   – ~1–2 h on a GPU for a usable gait.  
4. **Play** a trained policy:  
   ```bash
   uv run play Mjlab-Velocity-Flat-MicroDuck --wandb-run-path <entity/project/run_id>
   ```  
5. **Export** to ONNX:  
   ```bash
   uv run scripts/export.py Mjlab-Velocity-Flat-MicroDuck --wandb-run-path <...>
   ```  
6. **Run** the exported policy on CPU MuJoCo with keyboard control:  
   ```bash
   uv run scripts/infer_policy.py --walking output.onnx
   ```  
7. **Resume** from checkpoint or use Hugging Face Jobs (`--hf-jobs`) for GPU‑less training.  

## Task Catalogue
- **Walking**: `Mjlab-Velocity-{Flat,Rough}-MicroDuck` (velocity + head‑pose commands).  
- **Walk + Fall Recovery**: `Mjlab-VelStand-{Flat,Rough}-MicroDuck`.  
- **Stand‑up**: `Mjlab-StandUp-{Flat,Rough}-MicroDuck`.  
- **Sit‑Stand**: `Mjlab-SitStand-{Flat,Rough}-MicroDuck`.  
- **Ground Pick**: `Mjlab-GroundPick-{Flat,Rough}-MicroDuck`.  
- **Ball Kick**: `Mjlab-BallKick-Flat-MicroDuck`.  
- **Roulade**: `Mjlab-Roulade-Flat-MicroDuck`.  
- **Roller‑Skating Variants**: velocity tracking, swizzle, crouch, slope, stand‑up, spin, etc.  

All tasks share a 61‑dimensional observation vector (48 proprioceptive values + command slots), enabling runtime hot‑swapping of policies.

## Robot & Actuator Models
- MJCF robot files in `src/mjlab_microduck/robot/microduck/`, exported from Onshape.  
- Variants: `robot_walk.xml`, `robot_allcollisions.xml`, `robot_allcollisions_rollers.xml`, and corresponding backlash versions.  
- Actuator implementation (`src/mjlab_microduck/actuator/friction_dr_bam.py`) models voltage control, back‑EMF, Coulomb/​Stribeck friction, and includes domain randomization of battery voltage, sag, command delay, and friction magnitude.  

## Project Structure Highlights
- `src/mjlab_microduck/robot/` – robot MJCF files and export scripts.  
- `src/mjlab_microduck/actuator/` – actuator physics.  
- `src/mjlab_microduck/tasks/` – task registration, MDP definitions, backlash wrapper, and per‑task config modules.  
- `train_cli.py` – CLI entry point for training (supports Hugging Face Jobs).  
- `hf_jobs.py` – utilities for submitting jobs to Hugging Face.  

## Development & Testing
- Run tests with: `uv run --with pytest pytest tests/`.  
- Tests verify CPU‑only configuration invariance, reward sign conventions, joint‑index mappings, and NaN guards.  

## Additional Resources
- `AGENTS.md` – detailed env‑building workflow and reward‑design rules, useful for AI coding agents.  
- `README.md` – high‑level description and usage examples.  
- `CLAUDE.md` – notes on interactions with Claude (AI assistant).  

---  
This summary captures the repository’s purpose, core components, usage workflow, task set, and architectural details for developers and researchers interested in sim‑to‑real RL for the Microduck robot.