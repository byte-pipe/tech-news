---
title: AI evals are becoming the new compute bottleneck
url: https://huggingface.co/blog/evaleval/eval-costs-bottleneck
date: 2026-05-01
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-01T03:54:33.878917
---

# AI evals are becoming the new compute bottleneck

# AI evals are becoming the new compute bottleneck

## Overview
- Evaluation costs have risen to the point where they limit who can run modern AI benchmarks.
- The Holistic Agent Leaderboard (HAL) spent ~ $40 K for 21,730 rollouts across 9 models and 9 benchmarks; a single GAIA run on a frontier model can cost $2,829 before caching.
- Exgentic’s $22 K sweep revealed a 33× cost spread on identical tasks, highlighting scaffold choice as a primary cost driver.
- In scientific ML, “The Well” benchmark consumes about 960 H100‑hours for one new architecture and 3,840 H100‑hours for a full four‑baseline sweep.

## Making static LLM benchmarks cheaper
- Early static benchmarks (e.g., HELM) already incurred high API and GPU costs, totaling roughly $100 K across 30 models and 42 scenarios.
- Re‑evaluating thousands of checkpoints (e.g., EleutherAI’s Pythia) can make evaluation costs exceed pre‑training costs for small models.
- Studies showed that a 100×–200× reduction in compute preserves most ranking information, enabling coarse‑to‑fine evaluation pipelines (e.g., Flash‑HELM).
- Aggressive subsampling techniques (tinyBenchmarks, Anchor Points) can cut dataset sizes by 90 % while retaining ranking fidelity for static tasks.

## Agent evals are messier
- Agent benchmarks combine model, scaffold, and token‑budget, causing cost variability of four orders of magnitude across tasks.
- Example: Claude Opus 4.1 charges $15 M input tokens and $75 M output; Gemini 2.0 Flash charges $0.10 and $0.40, a two‑order‑of‑magnitude spread on input alone.
- Higher spend does not guarantee better performance; cost‑to‑accuracy ratios can be 9× or more with only marginal accuracy gains.
- Simple filters (e.g., Ndzomga’s mid‑difficulty filter) achieve 2×–3.5× cost reductions but fall far short of the 100×–200× gains possible for static benchmarks.
- Multi‑turn rollouts introduce variance and long trajectories, making each evaluation item intrinsically expensive.

## Some evals are just training
- Certain benchmarks evaluate models by training them from scratch, turning evaluation into a compute‑heavy training task.
- “The Well” benchmark: 16 scientific datasets (15 TB total); full grid sweep requires 3,840 H100‑hours (~$9,600), with a single new architecture costing ~960 H100‑hours (~$2,400).
- Evaluation compute can exceed training compute by two orders of magnitude, reversing traditional deep‑learning cost assumptions.
- Similar patterns appear in PDEBench and MLE‑Bench, where extensive training loops dominate evaluation budgets.

## Implications and mitigation strategies
- Evaluation has become a primary compute bottleneck, especially for agent and training‑in‑the‑loop benchmarks.
- Cost‑effective practices from static benchmarking (coarse‑to‑fine evaluation, aggressive subsampling) have limited applicability to noisy, scaffold‑sensitive agent tasks.
- Improving scaffold efficiency, standardizing token budgets, and developing reliable low‑cost proxies are critical to curbing the evaluation spend explosion.
- Community‑wide cost tracking (as done by HAL) helps expose cost drivers and guide more economical benchmark design.