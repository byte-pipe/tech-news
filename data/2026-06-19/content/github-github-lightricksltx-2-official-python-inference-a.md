---
title: 'GitHub - Lightricks/LTX-2: Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model. · GitHub'
url: https://github.com/Lightricks/LTX-2
site_name: github
content_file: github-github-lightricksltx-2-official-python-inference-a
fetched_at: '2026-06-19T01:17:25.623127'
original_url: https://github.com/Lightricks/LTX-2
author: Lightricks
description: Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model. - Lightricks/LTX-2
---

Lightricks

 

/

LTX-2

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.2k
* Star7.4k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

39 Commits
39 Commits
.claude/
skills/
train-model
.claude/
skills/
train-model
 
 
packages
packages
 
 
.clang-format
.clang-format
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
pyproject.toml
pyproject.toml
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

# LTX-2

LTX-2is the first DiT-based audio-video foundation model that contains all core capabilities of modern video generation in one model: synchronized audio and video, high fidelity, multiple performance modes, production-ready outputs, API access, and open access.

ltx-2.mp4

## 🚀 Quick Start

#
 Clone the repository

git clone https://github.com/Lightricks/LTX-2.git

cd
 LTX-2

#
 Set up the environment

uv sync --frozen

source
 .venv/bin/activate

### Required Models

Download the following models from theLTX-2.3 HuggingFace repository:

LTX-2.3 Model Checkpoint(choose and download one of the following)

* ltx-2.3-22b-dev.safetensors-Download
* ltx-2.3-22b-distilled-1.1.safetensors-Download

Spatial Upscaler- Required for current two-stage pipeline implementations in this repository

* ltx-2.3-spatial-upscaler-x2-1.1.safetensors-Download
* ltx-2.3-spatial-upscaler-x1.5-1.0.safetensors-Download

Temporal Upscaler- Supported by the model and will be required for future pipeline implementations

* ltx-2.3-temporal-upscaler-x2-1.0.safetensors-Download

Distilled LoRA- Required for current two-stage pipeline implementations in this repository (except DistilledPipeline, ICLoraPipeline, and LipDubPipeline)

* ltx-2.3-22b-distilled-lora-384-1.1.safetensors-Download

Gemma Text Encoder(download all assets from the repository)

* Gemma 3

LoRAs

* LTX-2.3-22b-IC-LoRA-Union-Control-Download
* LTX-2.3-22b-IC-LoRA-Motion-Track-Control-Download
* LTX-2-19b-IC-LoRA-Detailer-Download
* LTX-2-19b-IC-LoRA-Pose-Control-Download
* LTX-2-19b-LoRA-Camera-Control-Dolly-In-Download
* LTX-2-19b-LoRA-Camera-Control-Dolly-Left-Download
* LTX-2-19b-LoRA-Camera-Control-Dolly-Out-Download
* LTX-2-19b-LoRA-Camera-Control-Dolly-Right-Download
* LTX-2-19b-LoRA-Camera-Control-Jib-Down-Download
* LTX-2-19b-LoRA-Camera-Control-Jib-Up-Download
* LTX-2-19b-LoRA-Camera-Control-Static-Download
* LTX-2.3-22b-IC-LoRA-HDR- HDR IC-LoRA and pre-computed text embeddings forHDRICLoraPipeline
* LTX-2.3-22b-IC-LoRA-LipDub-Download

### Available Pipelines

* TI2VidTwoStagesPipeline- Production-quality text/image-to-video with 2x upsampling (recommended)
* TI2VidTwoStagesHQPipeline- Same two-stage flow as above but uses the res_2s second-order sampler (fewer steps, better quality)
* TI2VidOneStagePipeline- Single-stage generation for quick prototyping
* DistilledPipeline- Fastest inference with 8 predefined sigmas
* ICLoraPipeline- Video-to-video and image-to-video transformations (uses distilled model.)
* KeyframeInterpolationPipeline- Interpolate between keyframe images
* A2VidPipelineTwoStage- Audio-to-video generation conditioned on an input audio file
* RetakePipeline- Regenerate a specific time region of an existing video
* HDRICLoraPipeline- Video-to-video with HDR output (linear float frames via LogC3 inverse decode, suitable for EXR export and tonemapping)
* LipDubPipeline- Lip dubbing, rephrasing, matching speaker identity (distilled model, single IC-LoRA, Two stages).

### ⚡ Optimization Tips

* Use DistilledPipeline- Fastest inference with only 8 predefined sigmas (8 steps stage 1, 4 steps stage 2)
* Enable FP8 quantization- Enables lower memory footprint:--quantization fp8-cast(CLI) orquantization=QuantizationPolicy.fp8_cast()(Python). Fp8-cast should be used with bf16 checkpoints, it shall downcast them on the fly. For Hopper GPUs with TensorRT-LLM, use--quantization fp8-scaled-mmfor FP8 scaled matrix multiplication. Fp8-scaled-mm should be used with fp8 checkpoints.
* Install attention optimizations- On datacenter Blackwell GPUs (B200), install FlashAttention 4 manually:uv pip install 'flash-attn-4==4.0.0b9'(this specific revision is the one we have verified against torch 2.9.1+cu128; newer betas have known issues on consumer Blackwell). On other CUDA GPUs (including Hopper), use xFormers (uv sync --extra xformers).
* Use gradient estimation- Reduce inference steps from 40 to 20-30 while maintaining quality (seepipeline documentation)
* Skip memory cleanup- If you have sufficient VRAM, disable automatic memory cleanup between stages for faster processing
* Choose single-stage pipeline- UseTI2VidOneStagePipelinefor faster generation when high resolution isn't required

## ✍️ Prompting for LTX-2

When writing prompts, focus on detailed, chronological descriptions of actions and scenes. Include specific movements, appearances, camera angles, and environmental details - all in a single flowing paragraph. Start directly with the action, and keep descriptions literal and precise. Think like a cinematographer describing a shot list. Keep within 200 words. For best results, build your prompts using this structure:

* Start with main action in a single sentence
* Add specific details about movements and gestures
* Describe character/object appearances precisely
* Include background and environment details
* Specify camera angles and movements
* Describe lighting and colors
* Note any changes or sudden events

For additional guidance on writing a prompt please refer tohttps://ltx.video/blog/how-to-prompt-for-ltx-2

### Automatic Prompt Enhancement

LTX-2 pipelines support automatic prompt enhancement via anenhance_promptparameter.

## 🔌 ComfyUI Integration

To use our model with ComfyUI, please follow the instructions athttps://github.com/Lightricks/ComfyUI-LTXVideo/.

## 📦 Packages

This repository is organized as a monorepo with three main packages:

* ltx-core- Core model implementation, inference stack, and utilities
* ltx-pipelines- High-level pipeline implementations for text-to-video, image-to-video, and other generation modes
* ltx-trainer- Training and fine-tuning tools for LoRA, full fine-tuning, and IC-LoRA

Each package has its own README and documentation. See theDocumentationsection below.

## 📚 Documentation

Each package includes comprehensive documentation:

* LTX-Core README- Core model implementation, inference stack, and utilities
* LTX-Pipelines README- High-level pipeline implementations and usage guides
* LTX-Trainer README- Training and fine-tuning documentation with detailed guides

## About

Official Python inference and LoRA trainer package for the LTX-2 audio–video generative model.

ltx.io/model/ltx-2

### Topics

 generative-ai

 ltx

 ltx-2

### Resources

 Readme

 

### License

 View license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

7.4k

 stars
 

### Watchers

77

 watching
 

### Forks

1.2k

 forks
 

 Report repository

 

## Releases

No releases published

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Python100.0%