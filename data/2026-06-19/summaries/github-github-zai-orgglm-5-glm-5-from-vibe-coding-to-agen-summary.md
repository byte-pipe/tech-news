---
title: GitHub - zai-org/GLM-5: GLM-5: From Vibe Coding to Agentic Engineering · GitHub
url: https://github.com/zai-org/GLM-5
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:19:57.000222
---

# GitHub - zai-org/GLM-5: GLM-5: From Vibe Coding to Agentic Engineering · GitHub

# GLM-5 Repository Overview

## Introduction
- GLM-5 series targets complex systems engineering and long‑horizon agentic tasks.
- Three main model versions:
  - **GLM‑5** – baseline model scaling to 744B parameters (40B active) with DeepSeek Sparse Attention.
  - **GLM‑5.1** – next‑generation flagship for agentic engineering; stronger coding, better long‑term reasoning, handles ambiguous problems and iterates over hundreds of rounds.
  - **GLM‑5.2** – latest flagship with 1 M‑token context, advanced coding effort levels, and architectural improvements (IndexShare, enhanced MTP layer).

## Key Capabilities
- **Long‑context processing**: GLM‑5.2 supports a stable 1 M‑token context.
- **Coding performance**: GLM‑5.2 leads open‑source benchmarks (e.g., Terminal‑Bench 2.1 score 81.0, SWE‑bench Pro 62.1).
- **Agentic efficiency**: GLM‑5.1 sustains productivity over thousands of tool calls and long sessions.
- **Resource‑efficient architecture**: IndexShare reduces per‑token FLOPs by 2.9× at 1 M context; speculative decoding acceptance length increased up to 20 %.
- **Training infrastructure**: “slime” asynchronous RL system improves fine‑grained post‑training throughput.

## Benchmark Highlights
- GLM‑5 outperforms GLM‑4.7 on CC‑Bench‑V2 across frontend, backend, and long‑horizon tasks.
- On Vending Bench 2 (one‑year simulated business), GLM‑5 ranks #1 among open‑source models with a final balance of $4,432, close to Claude Opus 4.5.

## Model Downloads
| Model | Platform | Size | Precision |
|-------|----------|------|-----------|
| GLM‑5.2 | Hugging Face, ModelScope | 744B‑A40B | BF16 |
| GLM‑5.2‑FP8 | Hugging Face, ModelScope | 744B‑A40B | FP8 |
| GLM‑5.1 | Hugging Face, ModelScope | 744B‑A40B | BF16 |
| GLM‑5.1‑FP8 | Hugging Face, ModelScope | 744B‑A40B | FP8 |
| GLM‑5 | Hugging Face, ModelScope | 744B‑A40B | BF16 |
| GLM‑5‑FP8 | Hugging Face, ModelScope | 744B‑A40B | FP8 |

## Local Deployment
- Supported frameworks: SGLang (≥v0.5.13.post1), vLLM (≥v0.23.0), Transformers (≥v0.5.12), KTransformers (≥v0.5.12).
- Ascend NPU deployment via vLLM‑Ascend, xLLM, SGLang.
- Reasoning effort control: `reasoning_effort="max"` (default) or `"high"`; disable thinking with `enable_thinking=false`.

## Citation
If used in research, cite the technical report:

```
@misc{glm5team2026glm5vibecodingagentic,
  title = {GLM-5: from Vibe Coding to Agentic Engineering},
  author = {GLM-5-Team and ... (full author list in repository)},
  year = {2026}
}
```