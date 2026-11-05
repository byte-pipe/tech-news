---
title: moonshotai/Kimi-K3.1-Pro · Hugging Face
url: https://huggingface.co/moonshotai/Kimi-K3.1-Pro
date: 2026-11-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:25:07.467463
---

# moonshotai/Kimi-K3.1-Pro · Hugging Face

# Kimi K3.1 Pro Overview

## Model Introduction
- Open‑weight, multimodal (text & image) agentic model, first in the K3.1 series.  
- Built on Kimi K3 and further refined with large‑scale joint reinforcement learning across hundreds of downstream domains.  
- 1‑million‑token context window (≈1 MiB) enables long‑context tasks.  
- Notable improvements in coding, 3D creation, financial research, factual accuracy, and general agentic capabilities.

## Architecture & Technical Specs
- **Architecture:** Mixture‑of‑Experts (MoE)  
- **Total parameters:** 2.8 T (104 B activated per token)  
- **Layers:** 93 total, 1 dense layer  
- **Attention:** 69 KDA + 24 Gated DSA (replaces full‑attention Gated MLA for efficient long‑context)  
- **Attention dimensions:** hidden 7168, heads 96, DSA index head 128, top‑K 2048  
- **MoE:** 896 experts, 16 selected per token, 2 shared experts, latent dimension 3584, expert hidden 3072  
- **Vocabulary:** 160 K tokens  
- **Context length:** 1 048 576 tokens  
- **Activation:** SiTU‑GLU  
- **Vision encoder:** MoonViT‑V2 (401 M parameters)  
- **Quantization:** MXFP4 weights / MXFP8 activations (quantization‑aware training)  
- **Modality support:** Text and image  

## Evaluation Highlights
Performance is reported using maximum reasoning effort, temperature = 1.0, top‑p = 0.95 unless noted. Higher scores indicate better results (except where lower is explicitly better).

### Coding Benchmarks
- **Terminal‑Bench 4.0:** 65.7 (top among compared models)  
- **Terminal‑Bench‑Science 0.1:** 38.1 (competitive with Claude Fable 5.1 at 40.0)  
- **SWE Marathon v1.1:** 51.7 (lead over Claude Fable 45.6)  
- **BenchCAD (with tools):** 92.7 (on par with Claude Fable 92.6)  
- **Program Bench:** 31.5 (lower than DeepSeek V4.1 Flash 29.1)  
- **DeepSWE v1.1:** 75.5 (near top, close to DeepSeek 77.0)  
- **Kimi Code Bench 2.0 (internal):** 77.1 (best among listed models)  

### Agentic & Multimodal Benchmarks
- **HLE‑Full (with tools):** 70.0 (highest)  
- **BrowseComp:** 92.1 (near‑top, Claude Fable not reported)  
- **BioMysteryBench:** 80.6 (comparable to Claude Fable 81.6)  
- **CharXiv (RQ) with python:** 93.4 (tied with Claude Opus 93.8)  
- **MMMU‑Pro with python:** 90.0 (close to Claude Opus 89.8)  
- **BabyVision with python:** 95.4 (leading)  
- **ZeroBench (pass@5):** 63.0 (best pass@5 of 39.0)  
- **Agents’ Last Exam (ALL):** 43.2 (higher than DeepSeek 37.7)  
- **Automation Bench‑AA (Elo):** 1846 (top score)  

### Reasoning, Knowledge & Multimodal
- **GPQA‑Diamond:** 94.2 (best)  
- **GPQA‑Diamond (Claude Opus):** 93.9 (close)  
- **HLE‑Diamond:** 39.4 (lower than Claude Fable 55.1)  
- **PerceptionBench:** 68.3 (leading)  

### Cyber‑Security Benchmarks
- **ExploitBench:** 74.7 (competitive with DeepSeek 100)  
- **ExploitGym:** 20.7 (lower than DeepSeek 30.4)  

## Key Takeaways
- Kimi K3.1 Pro combines a massive MoE backbone with efficient gated sparse attention, enabling a 1 M‑token context window while keeping active parameters manageable.  
- Across a broad spectrum of coding, agentic, reasoning, and multimodal tasks, K3.1 Pro often matches or exceeds leading proprietary models such as Claude Fable/Opus, GPT‑6 Astra, and DeepSeek‑V4.1 Flash.  
- The model’s multimodal vision encoder (MoonViT‑V2) and quantization‑aware training support high‑quality image understanding alongside text processing.  
- Internal benchmarks (Kimi Code Bench, Hallucination Bench, etc.) show strong performance, especially in tool‑augmented scenarios.  

---  
*All scores are taken from the original article’s tables and footnotes; where a dash appears, the source did not report a value.*