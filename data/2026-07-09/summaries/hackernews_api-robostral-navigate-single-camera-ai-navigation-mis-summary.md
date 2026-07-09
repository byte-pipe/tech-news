---
title: Robostral Navigate: single-camera AI navigation | Mistral AI
url: https://mistral.ai/news/robostral-navigate/
date: 2026-07-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-09T15:20:22.667005
---

# Robostral Navigate: single-camera AI navigation | Mistral AI

# Robostral Navigate: single-camera AI navigation

## Overview
- An 8 billion‑parameter model that navigates robots using only a single RGB camera and plain‑language instructions.  
- Achieves 76.6 % success on the unseen R2R‑CE benchmark, surpassing the best single‑camera method by 9.7 points and the best multi‑sensor system by 4.5 points.  
- Operates without depth sensors or LiDAR, making it more efficient and easier to deploy.

## Capabilities
- Executes long‑horizon tasks such as “Leave the lobby, walk through the corridor, enter the supply room, and stop to face the second shelf.”  
- Works autonomously in offices, residential and commercial buildings, and outdoor environments.  
- Compatible with wheeled, legged, and flying robots and robust to variations in camera intrinsics and robot size.  

## Technical Highlights
- **Performance**: 79.4 % success on validation‑seen and 76.6 % on validation‑unseen R2R‑CE.  
- **Training data**: ~400 k trajectories collected from 6 k simulated scenes, generated entirely in‑house.  
- **Efficient training**: Prefix‑caching with tree‑based attention masks compresses an episode into a single sequence, cutting token usage by 22× and reducing training time from months to days.  
- **Navigation method**: Predicts image coordinates (pointing) and target orientation; falls back to local‑frame displacements when the target is outside the field of view.  
- **Reinforcement learning**: Applies the CISPO online RL algorithm after supervised training, improving success rate by 3.2 % and mitigating distribution‑shift issues.  

## Future Directions
- Position navigation as a foundational skill for a unified embodied AI agent.  
- Continue scaling simulation, training, and experimentation to push performance further.  

## Hiring
- The team is expanding and seeks research scientists and engineers to advance autonomous navigation across diverse robot platforms.  

*Authors: Théo Cachet, Arjun Majumdar, Srijan Mishra, Thomas Chabal, Chris Bamford, Elliot Chane‑Sane, Benjamin Tibi, Ludovic Ho Fuh, Olivier Duchenne – AI Science Robotics*