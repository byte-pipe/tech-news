---
title: Where Does a Robot Think — On-Device vs Datacenter Inference
url: https://newsletter.semianalysis.com/p/a-brain-too-big-to-carry-on-device
date: 2026-09-15
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-15T07:38:59.127661
---

# Where Does a Robot Think — On-Device vs Datacenter Inference

# Where Does a Robot Think — On‑Device vs Datacenter Inference  

## The Embodiment Problem  
- Robotics flips the LLM workflow: hardware must fit the model, not the other way around.  
- **Time constraint** – robots run real‑time control loops; missing a deadline makes the action obsolete.  
- **Cost constraint** – manufacturers pay for compute on every unit; scaling to millions or billions of robots implies huge upfront CAPEX.  
- Consequently, robot hardware is fixed and models are sized to meet latency and unit‑economics limits.  

## Current Robot Model Sizes  
- Frontier robot models are still in the **billions‑of‑parameters** range (e.g., π0 ≈ 3 B, π0.7 ≈ 5 B, DreamZero ≈ 14 B).  
- Unlike LLMs, size is dictated by data availability, on‑device hardware (Jetson, H100), and latency budgets, not by pure scaling laws.  
- Data is a bottleneck: robot experience is slow and expensive to collect; there is no internet‑scale corpus.  
- Network bandwidth becomes a bottleneck when models outgrow the robot (e.g., DreamZero needs two GB200 GPUs off‑robot).  

## On‑Device vs Off‑Robot Compute  
- A **cascade approach** is expected: some cognition stays onboard, while the planning layer may be offloaded to datacenter GPUs.  
- Off‑robot compute offers:  
  - Freedom from robot’s power and compute limits.  
  - Ability to pool inference across a fleet.  
- Trade‑off: network latency and jitter, especially for high‑frequency loops.  

## Layers of a Robot Model & Frequency Limits  
- **Planning layer** (≈ 5 Hz, ≤ 200 ms per decision) can tolerate a 10‑50 ms round‑trip, making it a candidate for offloading.  
- **Action & servo layers** run at ≥ 100 Hz (≤ 10 ms per step); network round‑trip consumes most of the budget, so these must stay on the robot.  
- Jitter (variable delay) is more problematic than fixed latency; buffering for worst‑case delay hurts performance.  

## Supply‑Chain Reality  
- The semiconductor supply chain is geared toward datacenter silicon (Hopper, Blackwell) rather than robot‑specific chips.  
- Ramp‑up of robot‑focused silicon faces front‑end capacity and DRAM shortages, limiting rapid adoption of higher‑performance on‑device compute.  

## Outlook  
- Model sizes will likely keep growing, but efficiency gains and supply‑chain limits will pull them back.  
- Off‑robot inference is becoming increasingly viable for the planning layer, provided network jitter can be controlled.  
- The field has not converged yet; a mixed architecture combining on‑device real‑time control with datacenter‑based planning appears to be the emerging norm.