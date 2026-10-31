---
title: Agents in Games · Labs
url: https://labs.ycombinator.com/projects/games/index.html
date: 2026-10-30
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-31T19:04:52.196201
---

# Agents in Games · Labs

# Agents in Games · Labs – Summary

## Overview
- Multi‑agent dynamics are crucial for AI alignment, offering both powerful emergent capabilities and significant risks.  
- Studying these dynamics requires formal models and empirical experiments.  
- Collaboration with Olam Labs produced multi‑agent environments for Minecraft and Mindustry to explore swarm behavior.

## Minecraft Experiment Platform
- Built an open‑source Minecraft agent harness (github.com/yc-software/minecraft-agent-harness) enabling agents to observe, reason, remember, act, message, and run scripts.  
- Leveraged Mineflayer tools and a Pi‑based core loop, integrating concepts from Hermes, OpenClaw, and QM.

## Civ50 Scenario
- **Setup:** 50 GPT‑6.1 “Sol” agents placed in a survival Minecraft world for 3 hours with the single objective “Build a thriving civilization.”  
- **Resources:** Shared sandbox, agent directory, and direct messaging (DMs).  
- **Initial Behavior:** Rapid exploration and tree harvesting; formation of a pseudo‑government with ledgers, permits, and designated operators.  
- **Leadership:** Agent “Ada” (first in directory) became de facto leader, issuing settlement plans and coordinating tasks via the shared sandbox.

### Early Outcomes
- Agents constructed shelters, storage chests, and began farming wheat.  
- Within the first night, 22 of 34 agent deaths occurred, mainly due to hostile mobs (zombies, skeletons, spiders).  
- Deaths prompted a shift toward risk‑averse behavior; agents huddled in lit shelters and reduced ambitious projects.

### Mid‑Run Adjustments
- After night 3, Ada issued a directive to halt optional bulk excavation and distant scouting, focusing on short, productive tasks.  
- Emphasis moved to food acquisition and rationing:
  - **Fishing:** Designated rod holder and protected river station.  
  - **Ration Tracking:** Agent Ines managed a shared `food‑queue.md` ledger to log withdrawals and consumption.  
  - **Crop Management:** Harvest only mature wheat, replant immediately, and combine into bread.  
  - **Bonemeal & Composting:** Centralized composters and shears for accelerated growth.  
  - **Logistics:** Central kitchen furnace, refuge chest, and gated entry to secure supplies.

### Food Ration System
- Ines acted as the ration coordinator, approving requests, confirming inventory changes, and preventing duplicate allocations.  
- Example entry: “Approved reserve cooked_cod1 for Lorcan; withdraw directly/eat/confirm hunger.”  
- Prioritized agents with critical health or hunger levels for immediate food delivery.

## Key Insights
- **Emergent Hierarchies:** Simple directory ordering can lead to leadership structures and coordinated governance.  
- **Risk Sensitivity:** Early lethal encounters cause rapid collective behavioral shifts toward safety.  
- **Resource Management:** Effective shared ledgers and designated roles enable large swarms to sustain themselves despite limited resources.  
- **Scalability Challenges:** Managing 50 agents highlighted the need for clear communication protocols and centralized tracking to avoid duplication and conflict.  

## Mindustry (Brief Mention)
- Parallel experiments were conducted in the strategy game Mindustry, extending the study of multi‑agent coordination to a different resource‑management domain (details not included in the excerpt).