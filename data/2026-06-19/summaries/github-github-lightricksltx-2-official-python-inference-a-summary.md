---
title: GitHub - Lightricks/LTX-2: Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model. · GitHub
url: https://github.com/Lightricks/LTX-2
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:19:45.112375
---

# GitHub - Lightricks/LTX-2: Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model. · GitHub

# LTX-2 Repository Overview

## Description
- First DiT‑based audio‑video foundation model offering synchronized audio/video, high fidelity, multiple performance modes, production‑ready outputs, API access, and open access.

## Quick Start
- Clone the repository and set up the environment with `uv sync --frozen` followed by `source .venv/bin/activate`.
- Download required model checkpoints, upscalers, LoRAs, and the Gemma text encoder from the LTX‑2.3 HuggingFace repository.

## Required Models
- LTX‑2.3 model checkpoint (choose either `ltx-2.3-22b-dev.safetensors` or `ltx-2.3-22b-distilled-1.1.safetensors`).
- Spatial upscaler (x2 or x1.5 version).
- Temporal upscaler (future pipeline support).
- Distilled LoRA (except for DistilledPipeline, ICLoraPipeline, and LipDubPipeline).
- Gemma 3 text encoder (download all assets).
- Various LoRAs for control, motion, pose, camera movements, HDR, LipDub, etc.

## Available Pipelines
- TI2VidTwoStagesPipeline – production‑quality text/image‑to‑video with 2× upsampling (recommended).
- TI2VidTwoStagesHQPipeline – two‑stage flow using a higher‑order sampler for better quality.
- TI2VidOneStagePipeline – single‑stage generation for rapid prototyping.
- DistilledPipeline – fastest inference with 8 predefined sigmas.
- ICLoraPipeline – video‑to‑video and image‑to‑video transformations using the distilled model.
- KeyframeInterpolationPipeline – interpolate between keyframe images.
- A2VidPipelineTwoStage – audio‑to‑video generation conditioned on an input audio file.
- RetakePipeline – regenerate a specific time region of an existing video.
- HDRICLoraPipeline – video‑to‑video with HDR output (linear float frames suitable for EXR export).
- LipDubPipeline – lip dubbing, rephrasing, and speaker identity matching (distilled model, single IC‑LoRA, two stages).

## Optimization Tips
- Use DistilledPipeline for the fastest inference.
- Enable FP8 quantization (`--quantization fp8-cast` in CLI or `QuantizationPolicy.fp8_cast()` in Python) to reduce memory usage.
- Install attention optimizations:
  - FlashAttention 4 for Blackwell GPUs (`uv pip install 'flash-attn-4==4.0.0b9'`).
  - xFormers for other CUDA GPUs (`uv sync --extra xformers`).
- Apply gradient estimation to cut inference steps from 40 to 20‑30 while keeping quality.
- Disable automatic memory cleanup between stages if VRAM is sufficient.
- Choose a single‑stage pipeline when high resolution is not required.

## Prompting Guidelines
- Write a detailed, chronological single‑paragraph prompt describing actions, movements, appearances, background, camera work, lighting, and any sudden events.
- Keep the prompt under 200 words.
- Structure: main action → specific movements/gestures → precise appearances → environment details → camera angles/movements → lighting and colors → changes or events.
- Automatic prompt enhancement is available via the `enhance_prompt` parameter.

## ComfyUI Integration
- Follow the integration instructions at `https://github.com/Lightricks/ComfyUI-LTXVideo/`.

## Repository Structure
- Monorepo organized into three main packages:
  - `ltx-core` – core model implementation, inference stack, and utilities.
  - `ltx-pipelines` – high‑level pipeline implementations for various generation modes.
  - `ltx-trainer` – training and fine‑tuning tools for LoRA, full fine‑tuning, and IC‑LoRA.
- Each package contains its own README and detailed documentation.

## Documentation
- Separate READMEs for Core, Pipelines, and Trainer provide comprehensive usage guides.

## Repository Statistics
- Stars: 7.4 k
- Forks: 1.2 k
- Primary language: Python (100 %)