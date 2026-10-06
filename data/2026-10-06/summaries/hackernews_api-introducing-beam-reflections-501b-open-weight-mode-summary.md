---
title: Introducing Beam: Reflection’s 501B open-weight model — Reflection
url: https://reflection.ai/blog/introducing-beam
date: 2026-10-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:14.136803
---

# Introducing Beam: Reflection’s 501B open-weight model — Reflection

# Introducing Beam: Reflection’s 501B open‑weight model — Summary

## Overview
- Beam is Reflection’s first open‑weight model, a sparse Mixture‑of‑Experts (MoE) architecture with **501 B total parameters** and **23 B active parameters** per token.  
- Designed for **coding, reasoning, and agentic workloads**.  
- Pretrained on **23.8 trillion high‑quality tokens** from web and proprietary sources.  
- Followed by an extensive **high‑compute reinforcement learning (RL)** phase: >100 M rollouts on 10.5 K NVIDIA GB300 GPUs over 4 weeks.  
- Currently in final red‑team testing; early‑access sign‑up available; weights, technical report, model card, and developer artifacts to be released later this month.

## Model Capability Focus
- Emphasis on **coding** and **agentic performance**.  
- Competitive with larger open models such as **GLM‑5.2** and approaches **Qwen 3.8‑Max** on relevant benchmarks.  
- Main advantage: **higher inference‑time efficiency** compared to raw‑capability leaders like **Kimi K3**.

## Benchmark Performance Highlights
- **Agentic/Coding**: Scores comparable to GLM‑5.2; outperforms many peers on Terminal Bench v2.1 (90.6) and SWE Bench Pro v2‑Hard (77.2).  
- **Reasoning**: Near‑state‑of‑the‑art on AIME 2026 (97.8) and GPQA Diamond (90.5).  
- **Tool Calling / Search**: Strong results on MCP Atlas (78.7) and BrowseComp with context management (77.4).  
- **General Capabilities**: High scores on AA‑LCR (79.3) and IFBench (79.7).  
- Across benchmarks, Beam achieves similar or better scores while using **3–4× less inference compute** than 2 T+ parameter models.

## Inference Efficiency
- Measured in FLOPs per token and token count; Beam shows frontier‑level efficiency on DeepSWE, Humanity’s Last Exam (HLE), and Terminal Bench 2.1.  
- Efficiency calculations consider active parameters per token, excluding prompt prefill and serving overhead, providing an approximate but consistent comparison.

## High‑Compute Reinforcement Learning
- Central scaling axis: **RL science, data, and infrastructure**.  
- Generated **>100 M rollouts** with a maximum context length of **256 K tokens**, using **1.3 B sandbox environments** sourced from **1 M high‑quality coding/agentic/STEM tasks**.  
- Asynchronous policy‑gradient training with novel algorithms to mitigate **policy staleness** and **numerical mismatch**; stable learning observed even with one‑day‑old samples (107 weight versions behind).  
- No performance plateau observed as RL compute increased.

## Learning to Reason Efficiently
- Introduced a **controllable length penalty** rewarding correct solutions while penalizing unnecessary tokens.  
- Early RL phase reduced completion lengths while improving performance; later phase allowed longer reasoning for higher gains.  
- Resulting **Pareto frontier** shows two phases: token‑efficiency contraction followed by performance‑driven expansion.  
- Users can adjust a **reasoning‑effort parameter**: lower settings yield shorter responses, higher settings enable more extensive reasoning for demanding tasks.

## Release and Access
- Final red‑team evaluation underway.  
- Early‑access sign‑up link provided.  
- Full model weights, technical documentation, and developer resources slated for release later this month.