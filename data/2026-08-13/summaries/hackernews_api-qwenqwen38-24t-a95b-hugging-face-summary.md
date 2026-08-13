---
title: Qwen/Qwen3.8-2.4T-A95B · Hugging Face
url: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B
date: 2026-08-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-13T11:44:10.657105
---

# Qwen/Qwen3.8-2.4T-A95B · Hugging Face

# Qwen3.8-2.4T-A95B Overview

## Model Description
- Open‑source causal language model released in Hugging Face Transformers format.  
- Compatible with vLLM, SGLang, TokenSpeed, and other inference stacks.  
- Managed inference available via the official Qwen Cloud API.  
- Serves as the foundation for **Qwen3.8‑Max**, which adds vision input, non‑thinking mode, 1 M default context, and built‑in tools.

## Key Highlights
- **Enhanced capabilities** across coding, professional work, research, and long‑horizon agentic tasks.  
- **Improved autonomous planning** and better handling of environment feedback for reliable end‑to‑end task completion.  
- **Broad downstream compatibility** with popular harnesses and development tools.  
- **Flexible reasoning control**: `reasoning_effort` adjusts depth; `preserve_thinking` retains reasoning context from prior messages.  

## Architecture & Specifications
- **Model type**: Causal Language Model (pre‑training + post‑training).  
- **Parameter count**: 2.4 T total, 95 B activated.  
- **Hidden dimension**: 8 192.  
- **Token embedding size**: 248 320 (padded).  
- **Layers**: 92, organized as 23 blocks of mixed Gated DeltaNet and Gated Attention, each followed by Mixture‑of‑Experts (MoE).  
- **Gated DeltaNet**: 128 linear attention heads for V, 16 heads for QK, head dimension 128.  
- **Gated Attention**: 64 Q heads, 4 KV heads, head dimension 256.  
- **Rotary position embedding**: dimension 64.  
- **Mixture‑of‑Experts**: 512 experts, 10 routed + 1 shared active per token, intermediate dimension 2 048.  
- **Multi‑Token Prediction (MTP)**: trained with multiple steps.  
- **Context length**: native 262 144 tokens, extensible up to ~1 010 000 tokens.

## Benchmark Highlights
| Category | Representative Scores (higher = better) |
|----------|-------------------------------------------|
| **Coding Agent** | Terminal Bench 2.1: 86.6 (Qwen3.8‑Max) – top among listed models. |
| **Software Engineering** | SWE‑bench Pro: 67.7; DeepSWE 1.1: 56.6; QwenSWEBench: 80.7. |
| **General Agent** | CoWorkBench: 74.8; WorkSpaceBench: 67.7; SkillsBench: 70.2. |
| **Tool Use** | Automation‑Bench (Pass@1): 27.3; Toolathlon Verified (Pass@1): 72.5. |
| **General Knowledge** | GPQA Diamond: 92.6; IFBench: 82.8; $OneMillion‑Bench (expert): 52.5. |
| **Domain‑specific** | PLawBench: 73.2; PRBench‑Legal: 57.6; PRBench‑Finance: 58.3. |
| **Long‑Context** | MRCR v2 256K (8‑needle): 92.9; LongBench v2: 66.3. |

*Notes*: Scores are drawn from a mix of in‑house and public benchmarks; “--” indicates missing data. Detailed evaluation settings are provided in the original release notes.

## Availability
- Model weights and configuration files are hosted on Hugging Face under the repository **Qwen/Qwen3.8-2.4T-A95B**.  
- For scalable, managed inference, use the **Qwen Cloud** service.  

---  
*The Qwen3.8 series represents the most capable open‑model generation in the Qwen family to date, delivering notable improvements in multi‑step reasoning, tool integration, and long‑context handling.*