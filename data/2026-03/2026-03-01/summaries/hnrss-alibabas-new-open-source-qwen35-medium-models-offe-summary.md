---
title: "Alibaba's new open source Qwen3.5-Medium models offer Sonnet 4.5 performance on local computers | VentureBeat"
url: https://venturebeat.com/technology/alibabas-new-open-source-qwen3-5-medium-models-offer-sonnet-4-5-performance
date: 2026-02-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-01T10:16:55.379149
---

# Alibaba's new open source Qwen3.5-Medium models offer Sonnet 4.5 performance on local computers | VentureBeat

# Alibaba's Qwen3.5‑Medium Models: Open‑Source LLMs with Sonnet 4.5‑Level Performance

## Overview
- Alibaba’s Qwen AI team released four new Qwen3.5‑Medium models, three of which are open‑source under Apache 2.0.
- The models support agentic tool calling and can be downloaded from Hugging Face and ModelScope.
- A proprietary fourth model, **Qwen3.5‑Flash**, is available only via Alibaba Cloud Model Studio API but remains competitively priced.

## Released Models
- **Qwen3.5‑35B‑A3B** – flagship, 35 B parameters, 1 M+ token context on 32 GB consumer GPUs.
- **Qwen3.5‑122B‑A10B** – server‑grade version (80 GB VRAM), 1 M+ token context.
- **Qwen3.5‑27B** – optimized for efficiency, >800 K token context.
- **Qwen3.5‑Flash** – hosted API version with default 1 M token context and built‑in tools.

## Technical Highlights
- **Hybrid Architecture (“Delta force”)**
  - Combines Gated Delta Networks with a sparse Mixture‑of‑Experts (MoE) layer.
  - 35 B‑parameter model activates only 3 B parameters per token.
  - MoE uses 256 experts; 8 are routed plus 1 shared expert, reducing inference latency.
- **Near‑Lossless 4‑bit Quantization**
  - Maintains high accuracy after compressing weights and KV cache to 4‑bit, enabling local deployment on consumer GPUs.
- **Thinking Mode**
  - Default internal reasoning chain wrapped in `<think>` tags before producing final answers.

## Performance
- Benchmarks show Qwen3.5‑35B‑A3B surpasses larger predecessors (e.g., Qwen3‑235B) and beats proprietary models:
  - Outperforms OpenAI’s **GPT‑5‑mini** and Anthropic’s **Claude Sonnet 4.5** on knowledge (MMMLU) and visual reasoning (MMMU‑Pro) tests.
- Achieves >1 M token context length with near‑lossless accuracy under 4‑bit weight and KV cache quantization.

## Pricing & API Integration
- **Qwen3.5‑Flash API rates** (per 1 M tokens):
  - Input: $0.10
  - Output: $0.40
  - Cache creation: $0.125
  - Cache read: $0.01
- Tool‑calling add‑ons: Web Search $10 per 1,000 calls; Code Interpreter free (limited time).
- Cost comparison (total per 1 M input + output):
  - Qwen 3 Turbo: $0.25
  - Qwen3.5‑Flash: $0.50 (most affordable among major LLMs)
  - Competitors range from $0.70 (DeepSeek) to $22.00 (Google Gemini 3 Pro > 200K) and $189.00 (OpenAI GPT‑5.2 Pro).

## Implications for Enterprises
- Open‑source models lower the barrier for on‑premise AI deployment, reducing reliance on expensive cloud APIs.
- Large context windows enable local ingestion of massive documents or long‑form video data without privacy concerns.
- Mixture‑of‑Experts architecture offers high performance with modest hardware, supporting cost‑effective, secure, and agile AI integration.
- Early adopters report narrowed performance gaps in agentic scenarios previously dominated by closed‑source, large‑scale models.

## Takeaway
Alibaba’s Qwen3.5‑Medium series delivers frontier‑level context length and competitive benchmark results in an open‑source package, offering a cost‑effective, privacy‑preserving alternative to leading proprietary LLMs for both developers and enterprise decision‑makers.
