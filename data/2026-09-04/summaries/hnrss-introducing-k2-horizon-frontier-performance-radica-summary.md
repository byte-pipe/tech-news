---
title: Introducing K2 Horizon: Frontier Performance, Radically Open
url: https://ifm.ai/blog/k2/
date: 2026-09-03
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-04T07:27:00.388023
---

# Introducing K2 Horizon: Frontier Performance, Radically Open

# Introducing K2 Horizon: Frontier Performance, Radically Open

## Overview
- IFM releases a connected fleet of six models: 375B‑A23B, 36B‑A4B, 32B, 7B, 3.7B, and 0.9B.  
- The fleet covers edge to enterprise deployment scenarios and shares a common architecture, vocabulary, training methodology, and tooling.  
- All models and code are released under the Apache 2.0 license; datasets follow their respective licenses (e.g., ODC‑BY).  
- The release includes the full training lifecycle: pre‑training, reasoning, and agentic post‑training checkpoints, data recipes, architecture details, mixture compositions, training code, configurations, logs, evaluation results, and final weights.

## Performance Frontier
- **0.9B, 3.7B, 7B** models achieve state‑of‑the‑art results in their size classes across mathematics, reasoning, coding, and agentic tasks.  
- **36B‑A4B** introduces the Mixture‑of‑Value‑Attention (MoVA) mechanism, delivering exceptional capability per active parameter and outperforming larger models.  
- **32B** (dense) and **375B‑A23B** (sparse MoE) rank among the top models in their respective parameter ranges.  
- Small models show strong AIME 2026 scores (>48) and notable tool‑use and agentic abilities; larger models excel on benchmarks such as SWE‑bench, BrowseComp, and general reasoning suites.

## Fully Open Model Fleet
- First open model family to expose the complete agentic post‑training pipeline.  
- Researchers can study the emergence of reasoning, tool use, planning, and agentic capabilities by reproducing intermediate checkpoints, data recipes, and training logs.  
- Enables adaptation of methods to new tools, environments, and domains rather than treating final weights as a black box.

## Model‑Specific Highlights
- **0.9B**: Designed for highly constrained devices (watches, glasses); supports quantization; excels at focused interactions and lightweight tool use.  
- **3.7B & 7B**: Suitable for phones and on‑device applications; handle more demanding coding and multi‑step workflows.  
- **32B**: Dense model offering a strong balance of capability and local deployability; top dense model below 40 B parameters.  
- **36B‑A4B**: Sparse model activating ~4 B parameters per token; efficiency stems from MoVA and MoE feed‑forward layers.  
- **375B‑A23B**: Sparse MoE with 375 B total parameters, ~23 B active per token; targets enterprise workloads requiring high quality reasoning, software engineering, and long‑horizon agentic tasks.

## Design Philosophy
- Built as a single, connected family rather than a set of unrelated models.  
- Shared core architecture, vocabulary (smaller for 0.9B), training pipeline, evaluation infrastructure, and deployment tooling.  
- Consistency facilitates dynamic routing of work across sizes, comparative studies of capability versus efficiency, and seamless scaling from edge to enterprise.  

## Significance
- Combines competitive, state‑of‑the‑art performance with full transparency of the training process.  
- Provides a foundation for both research (studying capability emergence) and development (reproducing and extending methods).  
- Extends the “fully open” principle introduced in the 2023 LLM360 paper to larger scales and complete lifecycle coverage.