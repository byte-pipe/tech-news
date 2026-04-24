---
title: A Hundred Robots Are Running A Bio Lab - by Jolie Gan
url: https://www.corememory.com/p/a-hundred-robots-are-running-a-bio-medra-michelle-lee
date: 2026-04-25
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-25T08:24:12.462413
---

# A Hundred Robots Are Running A Bio Lab - by Jolie Gan

# A Hundred Robots Are Running A Bio Lab – Summary

## Overview
- The article follows a tour of Medra’s new 38,000‑sq‑ft autonomous bio‑lab in San Francisco, where about a hundred robotic arms work continuously.
- A small courier robot shuttles consumables between stations, mimicking a junior scientist’s role.
- Founder and CEO Michelle Lee showcases a robot that can now open and close a glass door, illustrating the system’s growing capabilities.

## Medra’s Platform
- **Physical layer**
  - Every arm and bench carries cameras and nine sensors that monitor actions such as rotor angles, pipette tip depth, and timing.
  - The system records subtle procedural details that human scientists usually keep tacit, creating a permanent knowledge base.
- **AI scientist layer**
  - Software agents analyze results, diagnose problems, propose protocol changes, and rewrite procedures.
  - The AI can operate autonomously or await human approval; a cited case improved antibody binding from 0 % to >70 % by adding a vortex step.
- General‑purpose robot arms (sourced from the same maker as Toyota’s factory robots) are made lab‑ready through Medra’s software, allowing adaptation to existing instruments without new APIs.

## Impact & Results
- Traditional lab automation covers only ~5 % of instruments; Medra aims to raise that to ~75 % by using computer vision and manipulation models.
- One customer’s experiment was completed without any automation engineer, using only a chat interface and a robot arm.
- The platform logs detailed process parameters, turning “intuition” into reproducible data that can be leveraged across customers.

## Company Growth & Challenges
- Medra expanded from a 4,000‑sq‑ft space with a handful of robots to a three‑floor, 38,000‑sq‑ft facility housing a hundred arms.
- Staff grew from 15 (Nov 2023) to 45 employees, with five customers already running experiments in the autonomous lab.
- Customization is a key moat: an AI agent builds a simulation from a JSON protocol description, optimizes layout, and validates virtually before any physical movement.
- Over 85 % of new customer requests involve protocols Medra has never executed before, yet the consistent hardware‑software stack enables rapid reconfiguration.
- Remaining limitation: the system cannot differentiate colorless liquids, so humans still handle box opening and consumable loading.

## Founder Background & Vision
- Michelle Lee grew up in Taiwan, studied chemical engineering, interned at SpaceX, and was slated for a professorship at NYU before AlphaFold 2’s 2021 release shifted her focus to data‑driven biology.
- She recognized that while protein folding benefited from decades of structural data, many biotech problems lack sufficient data; increasing experimental throughput is essential.
- Early attempts (2022‑2024) to sell standardized cell‑culture boxes failed due to diverse lab needs, leading her to redesign hardware and software for flexible reconfiguration.
- Lee’s vision, influenced by her SpaceX experience and belief in rapid infrastructure, sees “Starlink”‑like ubiquitous connectivity as inevitable for the biotech AI era.