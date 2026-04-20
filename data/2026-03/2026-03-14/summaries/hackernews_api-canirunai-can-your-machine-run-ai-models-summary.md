---
title: CanIRun.ai — Can your machine run AI models?
url: https://www.canirun.ai/
date: 2026-03-13
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-14T06:01:33.990686
---

# CanIRun.ai — Can your machine run AI models?

# CanIRun.ai – Can your machine run AI models?

## Overview
- CanIRun.ai is an online tool that evaluates whether a user's hardware (CPU/GPU, VRAM, WebGPU support) can run a wide range of AI models.
- It provides estimates based on browser APIs, showing the required resources for each model and indicating compatibility grades (S/A/B – can run; C/D – tight fit; F – too heavy).

## Key Features
- **Model Catalog**: Includes hundreds of models from major providers (Meta, OpenAI, Alibaba, Google, Microsoft, Mistral AI, DeepSeek, Moonshot AI, etc.) covering chat, code, reasoning, and vision tasks.
- **Resource Metrics**: Displays model size (GB), context length, architecture type (Dense, MoE), active parameter count for MoE models, and supported quantizations (Q2_K, Q3_K_M, …, F16).
- **Filtering & Sorting**: Users can filter by task (chat, code, reasoning, vision), provider, and grade. Sorting options include score, parameter count (ascending/descending), release date, context length, speed, and VRAM requirement.
- **Compatibility Grades**:
  - **S/A/B** – model runs comfortably on the detected hardware.
  - **C/D** – model may run but with limited performance or memory constraints.
  - **F** – model exceeds hardware capabilities.

## Example Models Highlighted
- **Llama 3.1 8B (Meta)** – 4.1 GB, 128K context, dense architecture; good quality/speed balance.
- **Qwen 3.5 9B (Alibaba)** – 4.6 GB, 32K context, multimodal (chat + vision); released 2026‑02.
- **Phi-4 14B (Microsoft)** – 7.2 GB, 16K context, reasoning‑focused.
- **GPT‑OSS 20B (OpenAI)** – 10.8 GB, 128K context, MoE with 3.6 B active parameters.
- **DeepSeek V3.2 (DeepSeek)** – 350.9 GB, 128K context, state‑of‑the‑art MoE with 37 B active parameters.
- **Kimi K2 (Moonshot AI)** – 512.2 GB, 128K context, 1 T‑parameter MoE (32 B active) for strong agentic coding.

## Usage Flow
1. **Detect Hardware**: The site reads browser APIs (e.g., WebGPU) to estimate available VRAM and compute.
2. **View Compatibility**: Models are listed with grades indicating if they will run, fit tightly, or be too heavy.
3. **Adjust Filters**: Users can narrow results by task, provider, or specific model attributes.
4. **Select Model**: Choose a model that fits the hardware and download or run it using the appropriate quantization.

## Purpose
- Helps developers, researchers, and hobbyists quickly determine which open‑weight AI models are feasible on their current machines without manual benchmarking.
- Encourages efficient model selection, especially for edge devices and constrained environments.
