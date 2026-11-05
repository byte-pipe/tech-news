---
title: Recursive Self-Improvement via AI for Chip Design & Chip Design for AI - Ricursive Intelligence
url: https://www.ricursive.com/ripple
date: 2026-11-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:25:11.590883
---

# Recursive Self-Improvement via AI for Chip Design & Chip Design for AI - Ricursive Intelligence

# Ripple-65B Preview – Summary

## Overview
- Ricursive Intelligence released Ripple-65B Preview, a general‑purpose variant of the proprietary model that drives their AI chip design platform.  
- The model is trained from scratch on 12 trillion tokens and supports up to 1 M context length.  
- It is positioned as a full‑stack AI system that co‑optimizes hardware, software, and model design.

## Performance & Benchmarks
- Achieves U.S. open‑weight state‑of‑the‑art on agentic coding with a TerminalBench 2.1 score of **80.52**.  
- Outperforms larger open‑weight models:  
  - Reflection Beam 501B (80.1)  
  - Meta Muse Spark Open 816B (76.4)  
  - Thinking Machines Inkling 975B (63.8)  
  - NVIDIA Nemotron 3 Ultra 550B (56.4)  
- Dense architecture provides strong reasoning with low‑latency token generation, enabling efficient execution on local devices such as NVIDIA DGX Spark.

## Cost Efficiency
- Total R&D cost: **$32 M**, roughly one‑tenth of the previous open‑weight SOTA cost for agentic coding.  
- Cost includes full development pipeline: pretraining ladder, data mixing, evaluations, debugging, synthetic data generation, post‑training recipes, and final training runs.

## Reinforcement Learning Strategy
- Adopted a compute‑efficient RL pipeline rather than brute‑force scaling.  
- Developed proprietary synthetic data pipelines, quality filtering, and coverage metrics; no external post‑training data purchased.  
- Mixed RL recipe incorporates truncated importance sampling, score centering, and a linear length penalty.  
- Achieved TerminalBench 2.1 score of 80.5 with only **1.4 M rollouts**, about 70× fewer rollouts than the prior SOTA (Reflection Beam).

## Architecture Design
- Built as a modern dense Transformer optimized for NVIDIA hardware; avoided Mixture‑of‑Experts (MoE) complexity.  
- Thin‑and‑deep configuration: **d_model = 5120**, **80 layers**.  
- Over‑provisioned attention heads, increased SWA‑to‑global layer ratio, reduced SWA window size.  
- Added features: FFN activation clipping, gated attention, global NoPE, and value residuals.  
- Maintained solid MFU (~40%) throughout training with simple sharding, no custom kernels, and no quantization.

## Model Laddering & Compute Gains
- Conducted systematic laddering experiments starting from the Olmo 3 ladder.  
- Iterative interventions (v1.0–v1.6) included batch‑size/learning‑rate scaling, architectural scaling, pre+post norm, sigmoid gated attention, global NoPE, LR cooldown, and value residuals.  
- Final ladder incorporated a custom pretraining dataset heavily up‑sampled for code.  
- Resulted in up to **16×** higher compute efficiency on coding tasks at the 4 B scale compared to the Olmo 3 baseline.  
- Efficiency advantage is expected to grow with larger scales.

## Availability
- Model weights are hosted on Hugging Face, Together AI, GMI Cloud, and OpenRouter.  
- Fireworks integration scheduled to go live later the same day.

## Future Directions & Hiring
- Ripple‑65B Preview is intended to close the loop between AI models and the silicon that runs them; an internal variant powers Ricursive’s AI chip design platform.  
- The team acknowledges contributions from open‑source projects (Olmo, Prime Intellect, RadixArk, NVIDIA).  
- Ricursive is actively hiring researchers and engineers to advance full‑stack AI from model to silicon; interested candidates can apply via the company careers page.

## Notes
- U.S. open‑weight competitors reportedly spend up to **$150 M per month** on compute (e.g., Reflection Beam’s 4‑week pre‑ and post‑training schedule).  
- The $32 M figure represents Ricursive’s end‑to‑end cost, including all data and recipe development.