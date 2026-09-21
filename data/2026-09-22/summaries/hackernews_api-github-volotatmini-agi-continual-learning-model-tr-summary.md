---
title: GitHub - volotat/mini-AGI: Continual learning model trained from scratch on 8GB VRAM laptop with batch-1 stream of data. · GitHub
url: https://github.com/volotat/mini-AGI/
date: 2026-09-21
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-22T08:47:09.502968
---

# GitHub - volotat/mini-AGI: Continual learning model trained from scratch on 8GB VRAM laptop with batch-1 stream of data. · GitHub

# mini-AGI Repository Summary

## Overview
- mini-AGI is a byte‑level continual‑learning language model designed to run on a single GPU with 8 GB VRAM.  
- The model assembles its own architecture during training, stores weights as files on disk, and pages needed parameters onto the GPU, making the parameter count limited only by available disk space.  
- It trains from scratch on a continuous stream of data, avoiding catastrophic forgetting, and can keep learning indefinitely.

## Motivation
- Existing publicly available language models are pre‑trained and frozen; fine‑tuning on personal data quickly leads to forgetting.  
- mini‑AGI aims to provide a truly personal model that can be trained end‑to‑end on consumer hardware and continuously updated with a user’s own data.  
- Three design constraints: fit within 8 GB VRAM, prevent forgetting, and handle any input (256‑byte alphabet, no tokenizer).

## Architecture
- Input bytes pass through two dense prelude blocks, then a recurrent block applied up to 24 times per character.  
- Each recurrent application selects its own top‑8 experts from a shared pool; experts are not tied to specific tasks.  
- **Adaptive depth**: a halting head decides how many recurrent steps each character needs, using a PonderNet‑style weighted halting probability.  
- **Routing**: selection occurs per block‑application, not per character, allowing multiple expert uses at different depths.  
- No explicit tokenization; positions are rotary embeddings without learned parameters, enabling an extendable context window.

## Training and Generation
- The same forward pass is used for both reading (training) and writing (generation).  
- During generation, the model uses greedy decoding (argmax) and produces deterministic output.  
- Writing typically requires slightly more depth per character than reading (≈9.9 rows vs. 8.0 rows in the example).  
- Demonstrated generation continues a story coherently, though with some repetition at the current training stage (≈243 M characters processed).

## Paging Mechanism
- Each expert’s weights and Adam optimizer moments are stored as separate files on disk.  
- Three caching layers manage access:  
  - **Disk**: complete set of experts (bounded by free storage).  
  - **RAM cache**: recently accessed experts, evicted by least‑recently‑used policy.  
  - **VRAM resident set**: the working set required for the current chunk of text.  
- Before processing a chunk, the model predicts which experts will be needed and loads them into VRAM, ensuring efficient use of limited GPU memory.

## Current Status
- The model is a toy‑level experiment; frontier‑level capabilities are not expected.  
- Weights have not been released yet; the training run is still on its first pass through the corpus, projected to take several weeks at the current speed.  
- The repository includes scripts (`train.py`, `serve.py`), configuration (`config.yaml`), and example data directories (`assets`, `corpora`, `minagi`, `runs`).  

## Intended Audience
- Researchers and hobbyists interested in continual learning, low‑resource training, and personal language models.  
- Users with a laptop or PC equipped with at least an 8 GB VRAM GPU who wish to train or continue training their own model on custom data.