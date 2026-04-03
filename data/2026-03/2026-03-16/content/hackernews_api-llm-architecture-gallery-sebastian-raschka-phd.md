---
title: LLM Architecture Gallery | Sebastian Raschka, PhD
url: https://sebastianraschka.com/llm-architecture-gallery/
site_name: hackernews_api
content_file: hackernews_api-llm-architecture-gallery-sebastian-raschka-phd
fetched_at: '2026-03-16T11:23:21.703630'
original_url: https://sebastianraschka.com/llm-architecture-gallery/
author: Sebastian Raschka
date: '2026-03-15'
description: A gallery that collects architecture figures from The Big LLM Architecture Comparison and related articles, with fact sheets and links back to the original sections.
tags:
- hackernews
- trending
---

Last updated: March 15, 2026

This page collects architecture figures and fact sheets fromThe Big LLM Architecture ComparisonandA Dream of Spring for Open-Weight LLMs.
 It focuses on the architecture panels only. Click a figure to enlarge it and use the model title to jump to
 the corresponding article section.

If you spot an inaccurate fact sheet, mislabeled architecture, or broken link, please file an issue here:Architecture Gallery issue tracker.

Upon popular request, you can now also get this as a physical poster viaZazzle.
 The preview there may look a bit low-resolution, but the upload is based on a fresh high-resolution export at
 14570 x 12490 pixels (a 56 MB PNG file with 182 megapixels). I just ordered one myself but please be aware
 that I haven't been able to verify the quality, yet.

### Llama 3 8B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

Reference dense Llama stack used to contrast OLMo 2's normalization and attention choices.

Scale

8B parameters

Date

2024-04-18

Decoder type

Dense

Attention

GQA with RoPE

Key detail

Pre-norm baseline; wider than OLMo 2 at a similar scale.

Related concepts

GQA

### OLMo 2 7B

 View in article
 

 config.json
 

 Tech report
 

Transparent dense model that keeps classic MHA and pushes normalization changes for training stability.

Scale

7B parameters

Date

2024-11-25

Decoder type

Dense

Attention

MHA with QK-Norm

Key detail

Uses inside-residual post-norm instead of the usual pre-norm layout.

Related concepts

QK-Norm

MHA

### DeepSeek V3

 View in article
 

 config.json
 

 Tech report
 

DeepSeek's flagship template kicked off the recent wave of large open MoE models.

Scale

671B total, 37B active

Date

2024-12-26

Decoder type

Sparse MoE

Attention

MLA

Key detail

Uses a dense prefix plus a shared expert to keep a very large model practical at inference.

Related concepts

MLA

MoE

### DeepSeek R1

 View in article
 

 config.json
 

 Tech report
 

Reasoning-tuned DeepSeek model built on the V3 architecture rather than a new base design.

Scale

671B total, 37B active

Date

2025-01-20

Decoder type

Sparse MoE

Attention

MLA

Key detail

Architecture matches DeepSeek V3; the main change is the reasoning-oriented training recipe.

Related concepts

MLA

MoE

### Gemma 3 27B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

Gemma's flagship text stack leans on local attention more aggressively than Gemma 2.

Scale

27B parameters

Date

2025-03-11

Decoder type

Dense

Attention

GQA with QK-Norm and 5:1 sliding-window/global attention

Key detail

Built around a 27B sweet spot with heavier local attention and a large multilingual vocabulary.

Related concepts

QK-Norm

GQA

SWA

### Mistral Small 3.1 24B

 View in article
 

 config.json
 

 Tech report
 

Fast dense 24B model that drops the sliding-window setup used in older Mistral releases.

Scale

24B parameters

Date

2025-03-18

Decoder type

Dense

Attention

Standard GQA

Key detail

Latency-focused design with a smaller KV cache and fewer layers than Gemma 3 27B.

Related concepts

GQA

SWA

### Llama 4 Maverick

 View in article
 

 config.json
 

 Tech report
 

Meta's large MoE follows the DeepSeek V3 playbook but with a more conventional attention stack.

Scale

400B total, 17B active

Date

2025-04-05

Decoder type

Sparse MoE

Attention

GQA

Key detail

Alternates dense and MoE blocks and uses fewer, larger experts than DeepSeek V3.

Related concepts

GQA

MoE

### Qwen3 235B-A22B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

Large sparse Qwen variant that stays very close to DeepSeek V3 while removing the shared expert.

Scale

235B total, 22B active

Date

2025-04-28

Decoder type

Sparse MoE

Attention

GQA with QK-Norm

Key detail

High-capacity MoE design optimized for serving efficiency without a shared expert.

Related concepts

QK-Norm

GQA

MoE

### Qwen3 32B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

Large dense Qwen3 model that serves as the clearest like-for-like comparison for OLMo 3 32B.

Scale

32B parameters

Date

2025-04-28

Decoder type

Dense

Attention

GQA with QK-Norm

Key detail

Reference dense Qwen stack with QK-Norm and 8 KV heads.

Related concepts

QK-Norm

GQA

### Qwen3 4B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

Mid-size dense Qwen3 model used here as a clean baseline against SmolLM3 and Tiny Aya.

Scale

4B parameters

Date

2025-04-28

Decoder type

Dense

Attention

GQA with QK-Norm

Key detail

Compact Qwen3 dense stack with QK-Norm and a 151k vocabulary.

Related concepts

QK-Norm

GQA

### Qwen3 8B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

Dense Qwen3 baseline used here to show how little OLMo 3 changed the overall decoder recipe.

Scale

8B parameters

Date

2025-04-28

Decoder type

Dense

Attention

GQA with QK-Norm

Key detail

Reference Qwen3 dense stack with QK-Norm and 8 KV heads.

Related concepts

QK-Norm

GQA

### SmolLM3 3B

 View in article
 

 config.json
 

 Tech report
 

Compact dense model that experiments with leaving out positional encodings in selected layers.

Scale

3B parameters

Date

2025-06-19

Decoder type

Dense

Attention

GQA with periodic NoPE layers

Key detail

Every fourth layer omits RoPE to test a NoPE-style cadence.

Related concepts

NoPE

GQA

### Kimi K2

 View in article
 

 config.json
 

 Tech report
 

Trillion-parameter Moonshot model that essentially scales the DeepSeek V3 recipe upward.

Scale

1T total, 32B active

Date

2025-07-10

Decoder type

Sparse MoE

Attention

MLA

Key detail

More experts and fewer MLA heads than DeepSeek V3.

Related concepts

MLA

MoE

### GLM-4.5 355B

 View in article
 

 config.json
 

 Tech report
 

Agent-oriented instruction/reasoning hybrid that borrows DeepSeek's dense-prefix MoE layout.

Scale

355B total, 32B active

Date

2025-07-28

Decoder type

Sparse MoE

Attention

GQA with QK-Norm

Key detail

Starts with three dense layers before MoE routing and keeps a shared expert.

Related concepts

QK-Norm

GQA

MoE

### GPT-OSS 120B

 View in article
 

 config.json
 

 Tech report
 

Larger gpt-oss variant keeps the same alternating-attention recipe as the 20B model.

Scale

120B parameters

Date

2025-08-04

Decoder type

Sparse MoE

Attention

GQA with alternating sliding-window and global layers

Key detail

Shared architectural template scaled up for OpenAI's flagship open-weight release.

Related concepts

GQA

SWA

MoE

### GPT-OSS 20B

 View in article
 

 config.json
 

 Tech report
 

OpenAI's smaller open-weight MoE model favors width and alternating local/global attention.

Scale

20B total, 3.6B active

Date

2025-08-04

Decoder type

Sparse MoE

Attention

GQA with alternating sliding-window and global layers

Key detail

Wider and shallower than Qwen3, with attention bias and sink mechanisms.

Related concepts

GQA

SWA

MoE

### Grok 2.5 270B

 View in article
 

 config.json
 

Rare production-model release that shows an older MoE style with fewer, larger experts.

Scale

270B parameters

Date

2025-08-22

Decoder type

Sparse MoE

Attention

GQA

Key detail

Adds an always-on SwiGLU path that effectively behaves like a shared expert.

Related concepts

GQA

MoE

### Qwen3 Next 80B-A3B

 View in article
 

 config.json
 

Efficiency-focused Qwen refresh that swaps standard attention for a DeltaNet-attention hybrid.

Scale

80B total, 3B active

Date

2025-09-09

Decoder type

Sparse hybrid

Attention

3:1 Gated DeltaNet and Gated Attention

Key detail

Adds many more experts, a shared expert, and a native 262k context.

Related concepts

MoE

Gated Attention

Gated DeltaNet

### MiniMax M2 230B

 View in article
 

 config.json
 

MiniMax's flagship returns to full attention and looks like a leaner, sparser cousin of Qwen3.

Scale

230B total, 10B active

Date

2025-10-23

Decoder type

Sparse MoE

Attention

GQA with QK-Norm and partial RoPE

Key detail

Uses per-layer QK-Norm and much sparser MoE routing than Qwen3.

Related concepts

QK-Norm

GQA

MoE

### Kimi Linear 48B-A3B

 View in article
 

 config.json
 

 Tech report
 

Linear-attention hybrid that keeps a transformer backbone but replaces most full-attention layers.

Scale

48B total, 3B active

Date

2025-10-30

Decoder type

Sparse hybrid

Attention

3:1 Kimi Delta Attention and MLA

Key detail

Uses NoPE in MLA layers and channel-wise gating for long-context efficiency.

Related concepts

NoPE

MLA

Gated DeltaNet

### OLMo 3 32B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

Scaled-up OLMo 3 keeps the same block design but moves to grouped-query attention.

Scale

32B parameters

Date

2025-11-20

Decoder type

Dense

Attention

GQA with QK-Norm and 3:1 sliding-window/global attention

Key detail

Keeps post-norm while scaling width and applying YaRN only on global layers.

Related concepts

QK-Norm

GQA

SWA

### OLMo 3 7B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

New transparent Allen AI model that keeps OLMo's post-norm flavor while modernizing context handling.

Scale

7B parameters

Date

2025-11-20

Decoder type

Dense

Attention

MHA with QK-Norm and 3:1 sliding-window/global attention

Key detail

Retains post-norm, keeps MHA, and applies YaRN only on global layers.

Related concepts

QK-Norm

MHA

SWA

### DeepSeek V3.2

 View in article
 

 config.json
 

 Tech report
 

DeepSeek's successor keeps the V3 template but adds sparse attention to cut long-context costs.

Scale

671B total, 37B active

Date

2025-12-01

Decoder type

Sparse MoE

Attention

MLA with DeepSeek Sparse Attention

Key detail

An evolutionary update focused on efficiency rather than a new base layout.

Related concepts

MLA

MoE

DeepSeek Sparse Attention

### Mistral 3 Large

 View in article
 

 params.json
 

Mistral's new flagship effectively adopts the DeepSeek architecture and retunes the expert sizes.

Scale

673B total, 41B active

Date

2025-12-02

Decoder type

Sparse MoE

Attention

MLA

Key detail

Near-clone of DeepSeek V3 with larger experts, fewer routed experts, and multimodal support.

Related concepts

MLA

MoE

### Nemotron 3 Nano 30B-A3B

 View in article
 

 config.json
 

 Tech report
 

NVIDIA's Nano model is the most extreme transformer-state-space hybrid in the gallery.

Scale

30B total, 3B active

Date

2025-12-04

Decoder type

Hybrid MoE

Attention

Mostly Mamba-2 with a few GQA layers

Key detail

Interleaves Mamba-2 and MoE blocks, using attention only sparingly.

Related concepts

GQA

MoE

### Xiaomi MiMo-V2-Flash 309B

 View in article
 

 config.json
 

 Tech report
 

Large MoE model that pushes sliding-window attention harder than most contemporaries.

Scale

309B total, 15B active

Date

2025-12-16

Decoder type

Sparse MoE

Attention

5:1 sliding-window/global attention

Key detail

Uses an unusually small 128-token local window plus multi-token prediction.

Related concepts

SWA

MoE

### GLM-4.7 355B

 View in article
 

 config.json
 

 Tech report
 

Immediate GLM predecessor that stays closer to the older GLM-4.5 style before the MLA shift.

Scale

355B total, 32B active

Date

2025-12-22

Decoder type

Sparse MoE

Attention

GQA with QK-Norm

Key detail

Serves as the pre-MLA, pre-sparse-attention baseline with the same 32B active path as GLM-4.5.

Related concepts

QK-Norm

GQA

MLA

MoE

### Arcee AI Trinity Large 400B

 View in article
 

 config.json
 

 Tech report
 

Arcee's flagship blends several efficiency tricks into a DeepSeek-like coarse MoE design.

Scale

400B total, 13B active

Date

2026-01-27

Decoder type

Sparse MoE

Attention

GQA with gated attention and 3:1 sliding-window/global attention

Key detail

Combines QK-Norm, RoPE+NoPE, sandwich norm, and a coarse-grained MoE.

Related concepts

QK-Norm

NoPE

GQA

SWA

MoE

Gated Attention

### GLM-5 744B

 View in article
 

 config.json
 

 Tech report
 

Huge GLM refresh that adopts both MLA and DeepSeek Sparse Attention for flagship-scale inference.

Scale

744B total, 40B active

Date

2026-02-11

Decoder type

Sparse MoE

Attention

MLA with DeepSeek Sparse Attention

Key detail

Bigger than GLM-4.7, with more experts and fewer layers.

Related concepts

MLA

MoE

DeepSeek Sparse Attention

### Nemotron 3 Super 120B-A12B

 View in article
 

 config.json
 

 Tech report
 

The Super variant scales up Nano and adds both latent experts and native speculative decoding support.

Scale

120B total, 12B active

Date

2026-03-11

Decoder type

Hybrid MoE

Attention

Mostly Mamba-2 with a few GQA layers

Key detail

Adds latent-space MoE and shared-weight MTP for fast inference.

Related concepts

GQA

LatentMoE

MoE

### Step 3.5 Flash 196B

 View in article
 

 config.json
 

 Tech report
 

Throughput-oriented MoE model that stays competitive with much larger DeepSeek-style systems.

Scale

196B total, 11B active

Date

2026-02-01

Decoder type

Sparse MoE

Attention

GQA with 3:1 sliding-window attention

Key detail

Uses MTP-3 during both training and inference for unusually high throughput.

Related concepts

GQA

SWA

MoE

### Nanbeige 4.1 3B

 View in article
 

 config.json
 

 Tech report
 

Small on-device oriented model that stays close to Llama 3.2 while nudging the scaling choices.

Scale

3B parameters

Date

2026-02-10

Decoder type

Dense

Attention

GQA

Key detail

Llama-like stack without tying input embeddings to the output layer.

Related concepts

GQA

### MiniMax M2.5 230B

 View in article
 

 config.json
 

Popular 230B coder that opts for a classic architecture instead of the newer hybrid-attention ideas.

Scale

230B total, 10B active

Date

2026-02-12

Decoder type

Sparse MoE

Attention

GQA with QK-Norm

Key detail

Deliberately avoids sliding-window or linear-attention hybrids while keeping a 10B active path.

Related concepts

QK-Norm

GQA

SWA

MoE

### Tiny Aya 3.35B

 View in article
 

 From scratch
 

 config.json
 

 Tech report
 

Compact multilingual model from Cohere with a rare parallel transformer block.

Scale

3.35B parameters

Date

2026-02-13

Decoder type

Dense

Attention

GQA with 3:1 sliding-window attention

Key detail

Runs attention and the MLP in parallel while mixing RoPE with NoPE.

Related concepts

NoPE

GQA

SWA

### Ling 2.5 1T

 View in article
 

 config.json
 

Trillion-parameter long-context model that swaps DeltaNet for Lightning Attention.

Scale

1T total, 63B active

Date

2026-02-15

Decoder type

Sparse hybrid

Attention

Lightning Attention plus MLA

Key detail

Uses a 7:1 linear-attention/MLA ratio and a much larger 63B active path.

Related concepts

MLA

Gated DeltaNet

### Qwen3.5 397B

 View in article
 

 From scratch
 

 config.json
 

Mainline Qwen refresh that brings the Next-style hybrid attention into the flagship series.

Scale

397B total, 17B active

Date

2026-02-16

Decoder type

Sparse hybrid

Attention

3:1 Gated DeltaNet and Gated Attention

Key detail

Turns the former Qwen3-Next side branch into the new core design with 512 experts and 17B active parameters.

Related concepts

MoE

Gated Attention

Gated DeltaNet

### Sarvam 105B

 View in article
 

 config.json
 

Larger Sarvam variant keeps the sparse MoE layout but switches from GQA to MLA.

Scale

105B total

Date

2026-03-03

Decoder type

Sparse MoE

Attention

MLA with KV LayerNorm and NoPE + RoPE

Key detail

Large vocabulary and strong Indic language support carried into the larger MLA-based sparse MoE variant.

Related concepts

NoPE

GQA

MLA

MoE

### Sarvam 30B

 View in article
 

 config.json
 

Reasoning-oriented Indian-language sparse MoE that keeps GQA at the smaller size.

Scale

30B total

Date

2026-03-03

Decoder type

Sparse MoE

Attention

GQA with QK-Norm

Key detail

Large vocabulary and strong Indic language support paired with a reasoning-focused sparse MoE design.

Related concepts

QK-Norm

GQA

MoE

Source article

## The Big LLM Architecture Comparison

The original comparison article that walks through the architecture figures in context and explains the key
 design choices across dense, MoE, MLA, and hybrid decoder families.

 Read article
 

Source article

## A Dream of Spring for Open-Weight LLMs

Follow-up article covering the additional open-weight architecture releases from early 2026, including the
 newer MiniMax, Qwen, Ling, and Sarvam families.

 Read article
 

 View in article
 

×