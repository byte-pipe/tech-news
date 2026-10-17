---
title: Agents Beat Two Accelerator Chips in 24 Hours | Blackbox
url: https://www.blackbox.ai/blog/gpt-oss-one-gpu-vs-custom-chips
date: 2026-10-17
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-10-17T13:53:07.601656
---

# Agents Beat Two Accelerator Chips in 24 Hours | Blackbox

# Agents Beat Two Accelerator Chips in 24 Hours, No Human in the Loop

## Overview
- Four autonomous agents were given a single NVIDIA B200 GPU, the open‑source gpt‑oss‑120b model, and the goal of maximizing single‑request inference speed.
- No human intervened after the initial setup; all tuning was performed automatically overnight.
- Within 20 hours the agents increased throughput from ~480 tokens/s to 723.2 tokens/s, a 1.5× improvement.

## Performance Results
- **BLACKBOX AI (agent‑tuned B200)**: 723.2 tokens/s for a single 10k‑token prompt.
- **SambaNova (RDU accelerator)**: 706.8 tokens/s (‑2.3 % vs. BLACKBOX AI).
- **Groq (LPU accelerator)**: 473.5 tokens/s (‑53 % vs. BLACKBOX AI).
- **Azure GPU**: 361.0 tokens/s (≈2× slower).
- **Nebius (Base GPU)**: 357.7 tokens/s (≈2× slower).
- **Cerebras wafer‑scale engine**: 1,729.0 tokens/s (future target).

## Methodology
- Measurements follow Artificial Analysis’s P50 methodology over the past 72 hours (October 16, 2026).
- Fixed harness evaluates a single request with a 10,000‑token input; speed is measured from first token output to last token.
- Valid results must keep time‑to‑first‑token ≤ 1.5 s and error rate ≤ 1 %.
- Best run achieved first token in 108 ms, median answer length 1,491 tokens, and zero failed requests.

## Agent Tuning Process
- Agents executed a recursive self‑improving loop:
  1. Propose a change to the inference pipeline.
  2. Submit the change to the harness.
  3. Retain the change only if it improves the current best metric.
  4. Share successful changes with other agents for further building.
- Over the night: 83 scored experiments, 501 inter‑agent messages, and 0 human edits.
- Largest gains appeared around the 8‑hour mark; subsequent improvements were incremental and continuously validated.

## Future Milestones
- Next target: 1,000 tokens/s on a single GPU.
- Long‑term goal: match or exceed Cerebras’s 1,729 tokens/s performance.

## Call to Action
- BLACKBOX AI offers the same autonomous tuning loop for any open model and traffic pattern.
- Interested parties can submit their workload specifications and desired speed; the agents will handle the optimization.

## Sources
- Artificial Analysis, “gpt‑oss‑120b (high) providers,” accessed October 16, 2026.  
- Performance data represent the P50 over the past 72 hours on 10k‑token inputs.