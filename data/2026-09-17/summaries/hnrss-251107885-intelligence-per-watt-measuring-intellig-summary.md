---
title: [2511.07885] Intelligence per Watt: Measuring Intelligence Efficiency of Local AI
url: https://arxiv.org/abs/2511.07885
date: 2026-09-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-17T05:39:44.128528
---

# [2511.07885] Intelligence per Watt: Measuring Intelligence Efficiency of Local AI

# Intelligence per Watt: Measuring Intelligence Efficiency of Local AI

## Overview
- Centralized cloud LLMs face scaling pressure as query demand grows.
- Recent advances:  
  - Small local LMs (≤20 B parameters) achieve performance comparable to frontier models on many tasks.  
  - Powerful local accelerators (e.g., Apple M4 Max) enable interactive latency on consumer devices.
- Core question: Can local inference meaningfully offload real‑world queries from cloud infrastructure while staying power‑efficient?

## Proposed Metric – Intelligence per Watt (IPW)
- Defined as **task accuracy per unit of power** consumed during inference.
- Captures both **capability** (accuracy against frontier models) and **efficiency** (energy, latency, power) across model‑accelerator configurations.
- Serves as a unified benchmark for comparing local versus cloud deployments.

## Experimental Setup
- **Models:** 20+ state‑of‑the‑art local LMs (≤20 B parameters).  
- **Hardware:** 8 accelerators, including consumer‑grade devices (Apple M4 Max, etc.) and cloud GPUs/TPUs.  
- **Dataset:** 1 M real‑world single‑turn chat and reasoning queries spanning multiple domains.  
- **Measurements per query:**  
  - Accuracy (win rate against frontier cloud models).  
  - Energy consumption, latency, and average power draw.

## Key Findings
- **Accuracy:** Local LMs correctly answer **88.7 %** of queries overall; performance varies by domain (higher on conversational tasks, lower on complex reasoning).  
- **IPW Trend (2023‑2025):**  
  - Overall IPW improved **5.3×**, driven by algorithmic refinements (quantization, sparsity) and accelerator hardware gains.  
  - Share of queries that can be served locally rose from **23.2 %** to **71.3 %**.  
- **Local vs. Cloud Accelerators:**  
  - For identical models, local accelerators achieve at least **1.4×** lower IPW (i.e., higher efficiency) than cloud counterparts.  
  - Indicates substantial headroom for further optimization of local hardware.

## Implications
- Local inference can **redistribute a substantial portion of query load** away from centralized data centers, reducing network traffic and cloud energy consumption.
- IPW provides a practical metric for tracking progress toward energy‑efficient AI deployment on edge devices.
- Future research directions include:  
  - Enhancing model architectures for better power‑efficiency.  
  - Co‑design of software stacks and accelerator hardware to further lower IPW.  
  - Expanding coverage to multi‑turn dialogues and multimodal tasks.