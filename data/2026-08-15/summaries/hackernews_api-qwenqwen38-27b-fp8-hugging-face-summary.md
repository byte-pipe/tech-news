---
title: Qwen/Qwen3.8-27B-FP8 · Hugging Face
url: https://huggingface.co/Qwen/Qwen3.8-27B-FP8
date: 2026-08-15
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-15T04:05:54.545381
---

# Qwen/Qwen3.8-27B-FP8 · Hugging Face

# Qwen3.8-27B-FP8 Summary

## Repository & Compatibility
- FP8‑quantized model weights and configuration files in Hugging Face Transformers format.  
- Compatible with Transformers, vLLM, SGLang, TokenSpeed, and other inference frameworks.  
- Quantization method: fine‑grained FP8 with a block size of 128, delivering performance nearly identical to the original model.  
- Managed inference available through the official Qwen Cloud API (future hosted version with 1 M context length and built‑in tools).

## Qwen3.8 Series Overview
- Built on the Qwen3.5 architecture, representing the most capable generation in the Qwen open‑model family to date.  
- Enhances coding, professional work, research, and long‑horizon agentic tasks.  
- Qwen3.8‑27B is a compact, deployment‑friendly dense model that includes native vision‑language capabilities (images and videos) and flexible thinking control for complex multi‑step tasks.

## Highlights
- **Core capabilities** – comprehensive improvements across coding, professional, research, and long‑horizon agentic tasks.  
- **Agent execution** – stronger autonomous planning and better handling of environment feedback, leading to more reliable end‑to‑end task completion.  
- **Downstream compatibility** – broader support for popular harnesses and development tools, simplifying integration.  
- **Flexible thinking control** – thinking mode enabled by default, can be disabled per request; reasoning depth tunable via `reasoning_effort`; historical reasoning context retained via `preserve_thinking`.  
- **Vision‑language understanding** – native support for image and video comprehension, covering STEM diagrams, documents, and hour‑scale videos.

## Model Architecture
- **Type:** Causal Language Model with Vision Encoder  
- **Parameters:** 27 B  
- **Hidden dimension:** 5120  
- **Token embedding:** 248,320 (padded)  
- **Layers:** 64  
- **Hidden layout:** 16 × (3 × (Gated DeltaNet → FFN) → 1 × (Gated Attention → FFN))  
- **Gated DeltaNet:** 48 linear attention heads for V, 16 for QK; head dimension 128  
- **Gated Attention:** 24 attention heads for Q, 4 for KV; head dimension 256; rotary position embedding dimension 64  
- **Feed‑Forward Network:** intermediate dimension 17 408  
- **Multi‑Token Prediction (MTP):** trained with multiple steps  
- **Context length:** native 262 144 tokens, extensible up to 1 000 000 tokens  

## Benchmark Highlights

### Text Performance (selected metrics)
| Benchmark | Qwen3.8‑27B | Note |
|-----------|------------|------|
| Terminal Bench 2.1 (coding) | 73.0 | Highest among listed models |
| SWE‑bench Pro (agentic coding) | 61.7 | Top score |
| NL2Repo‑Bench (repo‑level code generation) | 42.3 | Best available |
| QwenSWEBench (software engineering) | 79.0 | Leading |
| CoWorkBench (long‑horizon office work) | 70.7 | Highest |
| IFBench (instruction following) | 79.5 | Best |
| GPQA Diamond (scientific reasoning) | 89.2 | Near‑top |
| HLE (multidisciplinary reasoning) | 30.8 | Highest |
| LiveCodeBench v6 (competitive coding) | 90.3 | Top |

### Vision‑Language Performance (selected metrics)
| Benchmark | Qwen3.8‑27B | Note |
|-----------|------------|------|
| OSWorld‑Verified (computer use) | 84.3 | Highest |
| WebArena‑Verified (browser use) | 64.8 | Best |
| AndroidWorld (mobile use) | 81.9 | Top |
| RecreationBench (application recreation) | 47.1 | Leading |
| ClawEval‑MM Pass@3 (multimodal tool use) | 57.4 | Best |
| MathVision With CI (visual math) | 94.6 | Top |
| BabyVision With CI (general visual reasoning) | 85.6 | Best |
| CharXiv (RQ) With CI (scientific chart analysis) | 90.2 | Highest |
| OmniDocBench 1.5 (document intelligence) | 91.1 | Leading |
| RealWorldQA (real‑world perception) | 85.9 | Best |
| ERQA (embodied intelligence) | 65.5 | Highest |

## Availability
- FP8 model files and configuration are downloadable from the Hugging Face repository.  
- A hosted version with extended context length and additional production features will be released soon via Qwen Cloud.