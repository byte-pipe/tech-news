---
title: Model Catalog - Cerebras Inference
url: https://inference-docs.cerebras.ai/models/overview
date: 2026-09-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-04T07:25:39.459521
---

# Model Catalog - Cerebras Inference

# Model Catalog - Cerebras Inference Summary

## Overview
- Public endpoints provide access to models on free trial and pay‑as‑you‑go tiers, subject to rate limits and pricing.  
- For reserved capacity, higher throughput, and production SLAs, use **Dedicated Endpoints**.  
- New users should follow the Quickstart guide for their first API call; the model selection guide helps choose a model by use case.  

## Available Models
- **OpenAI GPT OSS**  
  - Model ID: `gpt-oss-120b`  
  - Parameters: 120 billion  
  - Context windows: 65k (free) / 131k (paid)  
  - Speed: ~3000 tokens/s  
- **Qwen 3.8 27B**  
  - Model ID: `qwen-3.8-27b`  
  - Parameters: 27 billion  
  - Context windows: 64k (free) / 128k (paid)  
  - Speed: ~1500 tokens/s  
- Additional model families are available through Dedicated Endpoints.  

## Model Compression
- All models served on public endpoints are the original, unpruned versions.  
- Pruned models (e.g., REAP) are shared on Hugging Face for research but are **not** available via the public API.  
- Storage uses selective weight‑only quantization (partial 16‑bit / 8‑bit / 4‑bit) to keep maximal quality:  
  - Sensitive layers stored at full precision and de‑quantized on the fly.  
  - Activations, attention, and KV cache remain in full precision and unquantized.  

## Frequently Asked Questions
- **Will model architecture change without notice?**  
  - No. Existing endpoints will continue serving the original models unchanged. Future compression techniques will be offered as separate, clearly named endpoints.  
- **Where are REAP pruned models located?**  
  - On Hugging Face under the *Cerebras REAP Collection*.  
- **What is the difference between compression, quantization, and pruning?**  
  - *Compression*: General term for reducing model size or compute requirements.  
  - *Quantization*: Lowers numeric precision of weights (e.g., FP16 → FP8) without altering architecture.  
  - *Pruning*: Removes parts of the model (layers, experts), changing its architecture.  

## Feedback
- Users can indicate whether the page was helpful with “Yes” or “No”.