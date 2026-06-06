---
title: Gemma 4 with quantization-aware training
url: https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/
date: 2026-06-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-06T11:52:24.522634
---

# Gemma 4 with quantization-aware training

# Gemma 4 QAT models: Optimizing model compression for mobile and laptop efficiency  

## Overview  
- New checkpoints for the Gemma 4 family are trained with Quantization‑Aware Training (QAT).  
- QAT reduces memory usage and speeds up inference on edge devices and consumer GPUs while keeping model quality.  
- Authors: Olivier Lacombe (Director of Product Management, Google DeepMind) and Omar Sanseviero (Member of Technical Staff, Google DeepMind).  

## Recent Gemma 4 developments  
- Added Multi‑Token Prediction (MTP) to accelerate inference.  
- Released a 12 B model to fill the gap between the E4 B and 26 B MOE models.  

## QAT benefits and formats  
- QAT simulates quantization during training, minimizing quality loss compared with standard Post‑Training Quantization (PTQ).  
- Provides checkpoints for the widely used Q4_0 format and a novel mobile‑specialized quantization format.  
- The mobile format shrinks the Gemma 4 E2 B model’s memory footprint to roughly **1 GB**.  

## Mobile‑optimized quantization schema  
- **Static activations**: scaling parameters are pre‑computed during training, reducing runtime work on mobile chips.  
- **Channel‑wise quantization**: aligns compressed data with the architecture of mobile accelerators for native execution.  
- **Targeted 2‑bit quantization**: token‑generation layers are heavily compressed to 2 bits, while core reasoning layers retain higher precision.  
- **Embedding and KV‑cache optimization**: compresses the vocabulary list and short‑term memory, dramatically lowering active memory usage and enabling longer conversations.  
- A text‑only E2 B model without per‑layer embeddings fits in **under 1 GB** of memory.  

## Memory and storage impact  
- Approximate VRAM requirements are reduced across the family; the E2 B model now loads with ~1 GB, and other variants see proportional savings.  

## Getting started  
- **Weights**: available on Hugging Face for both Q4_0 and mobile formats.  
- **File formats**: GGUF for llama.cpp, compressed tensors for vLLM, and unquantized checkpoints for custom conversion.  
- **Documentation**: guides provided for deployment and best‑practice usage.  
- **Desktop deployment**: supported through llama.cpp, Ollama, and LM Studio.  
- **Edge deployment**: use Google’s lightweight LiteRT‑LM runtime or run directly in the browser with Transformers.js.  
- **Toolchain compatibility**: works with SGLang, vLLM, MLX (Apple Silicon), MTP QAT checkpoints, and fine‑tuning via Hugging Face Transformers and Unsloth.  

## Outlook  
- The team encourages developers to experiment with locally running Gemma 4 models, leveraging the new QAT checkpoints for efficient on‑device AI.