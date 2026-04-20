---
title: I-DLM: Introspective Diffusion Language Models
url: https://introspective-diffusion.github.io/
date: 2026-04-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-15T06:04:00.678792
---

# I-DLM: Introspective Diffusion Language Models

# I-DLM: Introspective Diffusion Language Models

## Motivation
- Diffusion language models (DLMs) promise parallel token generation, potentially removing the sequential bottleneck of autoregressive (AR) decoding.
- In practice DLMs have lagged behind AR models in generation quality.
- The authors identify a lack of *introspective consistency*: AR models generate tokens that agree with their own predictions, while DLMs often produce tokens that do not align with later verification steps.
- Three bottlenecks in existing DLMs are highlighted:
  1. Low introspective consistency (SDAR score 0.699 vs. I‑DLM 0.984).
  2. High compute overhead (TiDAR ≈ 7.8× vs. I‑DLM ≈ 2.5×).
  3. Mismatch with existing serving infrastructure (SDAR slope = 84 vs. I‑DLM slope = 549).

## Method
- **Introspective‑Consistency Training**
  - Convert a pretrained AR model to a diffusion model using causal attention, a logit‑shift trick, and an all‑masked training objective.
- **Introspective Strided Decoding (ISD)**
  - Generate N tokens per forward pass while simultaneously verifying previously generated tokens using a p/q acceptance criterion.
  - The acceptance step guarantees that the output distribution matches that of the underlying AR model.
- **AR‑Compatible Serving**
  - Strict causal attention allows I‑DLM to be deployed as a drop‑in replacement in existing AR serving stacks such as SGLang, without custom infrastructure.

## Results
- **Quality**
  - I‑DLM‑8B matches the quality of same‑scale AR models and surpasses prior DLMs on 15 benchmarks.
  - Notable gains include +26 points on AIME‑24 and +15 points on LiveCodeBench‑v6 compared to LLaDA‑2.1‑mini (16 B) while using half the parameters.
- **Throughput**
  - Achieves 2.9–4.1× higher throughput than LLaDA‑2.1‑mini at high concurrency (batch size = 64).
  - With gated LoRA, ISD provides bit‑for‑bit lossless acceleration; the LoRA overhead factor α ≈ 1.12 matches empirical measurements.
- **Efficiency**
  - Compute efficiency exceeds that of AR decoding (efficiency ≈ 1.22 for N = 4, acceptance p = 0.9), meaning parallel decoding can reduce total FLOPs.
  - Acceptance probability compounds geometrically across positions, ensuring most tokens are accepted early in the stride.

## Resources
- Open‑source code, model checkpoints, and detailed documentation are provided.
- Installation steps include cloning the repository and running the provided install script.
- Quick‑start instructions cover launching a SGLang server and generating text via a REST API.
- Training recipe describes converting a pretrained AR model, data requirements, and curriculum for stride sizes.
- Inference guide explains the ISD algorithm, configuration files, and the gated LoRA technique for lossless output.
- Additional sections cover serving integration, benchmark reproduction, and a model zoo.
