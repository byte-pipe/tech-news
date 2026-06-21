---
title: LLMs are complicated now – Ian’s Blog
url: https://ianbarber.blog/2026/06/19/llms-are-complicated-now/
date: 2026-06-20
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-21T11:07:08.743972
---

# LLMs are complicated now – Ian’s Blog

# LLMs are complicated now

## Overview
- In 2022‑2023 Meta’s ML work split into two clear streams: a clean Llama transformer stack and a complex recommendation‑system graph.
- The industry has now made large language models (LLMs) similarly complex.

## Architectural growth
- Modern LLMs employ many attention variants (query grouping, compressed, sparse, linear, sliding‑window, etc.).
- Mixture‑of‑Experts adds selective routing to feed‑forward layers; routing now extends to attention blocks and the residual stream.
- Vision and audio encoders have moved from add‑on modules to fully integrated components.
- Multi‑GPU inference introduces communication operations that create additional boundaries within models.

## Parallel with recommendation systems
- Recommendation systems historically used a simple two‑tower sparse neural net; complexity arose from balancing capability growth with inference efficiency.
- The line between “performance as optimization” and “performance as necessity” has blurred, making baseline performance critical.

## Need for composability
- Swapping one attention variant for another must not cause large performance regressions; a partially fused, optimized version is required to evaluate trade‑offs.
- Research iteration demands flexible, composable designs rather than post‑hoc hand‑fusing or pure generation of kernels.
- A stable baseline is essential for both verification and exploration.

## Kernel development example
- FlexAttention in PyTorch (built on Triton templates) exemplifies composable, verifiable attention kernels with minimal performance impact during experimentation.

## Future directions
- Andrej Karpathy’s move to Anthropic aims to create richer auto‑research loops, emphasizing the importance of reducing architectures to their composable essence alongside agentic methods.