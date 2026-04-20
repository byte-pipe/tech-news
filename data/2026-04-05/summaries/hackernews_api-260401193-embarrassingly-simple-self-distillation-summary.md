---
title: [2604.01193] Embarrassingly Simple Self-Distillation Improves Code Generation
url: https://arxiv.org/abs/2604.01193
date: 2026-04-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-05T01:02:42.693094
---

# [2604.01193] Embarrassingly Simple Self-Distillation Improves Code Generation

# Embarrassingly Simple Self-Distillation Improves Code Generation

## Motivation
- Investigates whether a large language model (LLM) can enhance its code‑generation ability using only its own raw outputs.
- Seeks a method that avoids external verifiers, teacher models, or reinforcement learning.

## Method: Simple Self‑Distillation (SSD)
- Generate candidate solutions from the target model with specific temperature and truncation settings.
- Collect these raw outputs as pseudo‑labels.
- Fine‑tune the same model on the generated samples using standard supervised fine‑tuning.
- No additional supervision, reward modeling, or external feedback loops are required.

## Experimental Results
- Applied SSD to Qwen3‑30B‑Instruct, raising pass@1 on LiveCodeBench v6 from 42.4 % to 55.3 %.
- Gains are most pronounced on harder programming problems.
- Generalizes across model families (Qwen, Llama) and scales (4 B, 8 B, 30 B) for both instruction‑following and “thinking” variants.
- Demonstrates consistent improvements without changing model architecture or inference strategy.

## Analysis of Why SSD Works
- Identifies a precision‑exploration conflict in LLM decoding:
  - High‑precision contexts need concentrated probability mass on correct tokens.
  - Exploratory contexts benefit from diverse token distributions.
- Shows SSD reshapes token distributions in a context‑dependent manner:
  - Suppresses low‑probability “distractor” tails where precision matters.
  - Preserves useful diversity in regions where exploration aids solution discovery.
- Provides empirical evidence that the altered distribution leads to better downstream code correctness.

## Contributions
- Proposes an embarrassingly simple post‑training technique that leverages a model’s own outputs.
- Demonstrates that self‑distillation can be a viable alternative to more complex improvement pipelines for code generation.
- Offers insight into the interplay between decoding precision and exploration, informing future decoding and fine‑tuning strategies.
