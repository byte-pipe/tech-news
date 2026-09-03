---
title: Model Catalog - Cerebras Inference
url: https://inference-docs.cerebras.ai/models/overview
site_name: hackernews_api
content_file: hackernews_api-model-catalog-cerebras-inference
fetched_at: '2026-09-04T07:24:53.391988'
original_url: https://inference-docs.cerebras.ai/models/overview
author: altertable
date: '2026-09-04'
description: Browse all models available on Cerebras public endpoints.
tags:
- hackernews
- trending
---

Copy page
Copy MCP Server
View as Markdown
Models on Cerebras public endpoints are available on the free trial and pay-as-you-go tiers, subject to 
rate limits
 and 
pricing
. For additional model families, reserved capacity, higher throughput, and production SLAs, see 
Dedicated Endpoints
.

New here? Follow the 
Quickstart
 to make your first API call. To pick a model by use case, see the 
model selection guide
. Select any model name below for full specs, capabilities, and per-tier limits.

## ​Available Models

Model Name
Model ID
Parameters
Context (free / paid)
Speed (tokens/s)
OpenAI GPT OSS
gpt-oss-120b
120 billion
65k / 131k
~3000
Qwen 3.8 27B
qwen-3.8-27b
27 billion
64k / 128k
~1500

Looking for more models? Many additional model families are available through 
Dedicated Endpoints
.

## ​Model Compression

This section provides transparency about the compression state of each model available on our platform.

We host a variety of open-source models from the community. We do not currently host pruned models on our public endpoints. All models served through our public endpoints are the original, unpruned versions.

While we conduct research on pruning techniques like REAP (Router-weighted Expert Activation Pruning), these pruned models are shared with the research community on Hugging Face but are not available through our shared API. You can read more about REAP in our 
research blog
. 
All of our public models are unpruned.

Cerebras uses selective weight-only quantization only during storage to preserve maximal quality. This means that the weights are stored in partial 16-bit / 8-bit / 4-bit, in-line with industry standards. For quality, sensitive layers are stored at full precision with dequantization on the fly, so operations are done in high precision. The activations, attention, and kv cache remain in full precision and unquantized.

### ​Frequently Asked Questions

Will you change a model's architecture without notice?

No. We are committed to serving the original models for all existing endpoints, without modification. We do not alter model architectures via pruning on our hosted portfolio. If we explore additional compression techniques (like pruning) in the future, these would be offered as separate endpoints with pruning-specific names, ensuring complete transparency and allowing you to choose which version best fits your needs.

Where can I find your REAP pruned models?

Our REAP pruned models are available on Hugging Face for research and experimentation purposes: 
Cerebras REAP Collection
. These models demonstrate our pruning research but are not served through our production API.

What are compression, quantization, and pruning?

Compression
 is an umbrella term for techniques that reduce model size or computational requirements. Common compression techniques include:
* Quantization: Reducing the precision of numbers used to represent model weights (e.g., converting from FP16 to FP8). This reduces memory usage without changing the model’s architecture.
* Pruning: Permanently removing parts of a model, like layers or experts, to reduce model size. This changes the model’s architecture and creates a different model.

Was this page helpful?

Yes
No
⌘
I