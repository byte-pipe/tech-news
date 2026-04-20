---
title: Introducing Unsloth Studio | Unsloth Documentation
url: https://unsloth.ai/docs/new/studio
site_name: hnrss
content_file: hnrss-introducing-unsloth-studio-unsloth-documentation
fetched_at: '2026-03-18T11:21:12.085512'
original_url: https://unsloth.ai/docs/new/studio
date: '2026-03-17'
description: Run and train AI models locally with Unsloth Studio.
tags:
- hackernews
- hnrss
---

Today, we’re launchingUnsloth Studio(Beta): an open-source, no-code web UI for training, running and exporting open models in one unifiedlocalinterface.

boltQuickstartstarFeaturesgithubGithub

* Run GGUFand safetensor models locally onMac, Windows, Linux.
* Train 500+ models 2x faster with 70% less VRAM (no accuracy loss)
* Run and train text, vision, TTS audio, embedding models
* MacOSandCPUwork forChatGGUF inference. MLX training coming soon.
* No dataset needed.Auto-create datasetsfromPDF, CSV, JSON, DOCX, TXTfiles.
* Export or saveyour model to GGUF, 16-bit safetensor etc.
* Self-healing tool calling/ web search +code execution
* Auto inference parametertuning and edit chat templates.

## hashtag⭐ Features

### hashtagRun models locally

Search and run GGUFand safetensor models withself-healing toolcalling / web search,auto inferenceparameter tuning,code executionand APIs (very soon). Upload images, docs, audio, code files.

Battle models side by side. Powered by llama.cpp + Hugging Face, we supportmulti-GPU inferenceand most models.

### hashtagNo-code training

Upload PDF, CSV, JSONdocs, or YAML configs and start training instantly on NVIDIA. Unsloth’s kernels optimize LoRA, FP8, FFT, PT across 500+ text, vision, TTS/audio and embedding models.

Fine-tune the latest LLMs likeQwen3.5and NVIDIANemotron 3.Multi-GPUworks automatically, with a new version coming.

### hashtagData Recipes

Data Recipestransforms your docs into useable / synthetic datasets via graph-node workflow. Upload unstructured or structured files like PDFs, CSV and JSON. Unsloth Data Recipes, powered by NVIDIADataDesignerarrow-up-right, auto turns documents into your desired formats.

### hashtagObservability

Gaincomplete visibilityinto and control over your training runs. Track training loss, gradient norms, and GPU utilization in real time, and customize to your liking.

You can even view the training progress on other devices like your phone.

### hashtagExport / Save models

Export any model, including your fine-tuned models, to safetensors, or GGUF for use with llama.cpp, vLLM, Ollama, LM Studio, and more.

Stores your training history, so you can revisit runs, export again and experiment.

### hashtagModel Arena

Chat with andcompare 2 differentmodels, such as a base model and a fine-tuned one, to see how their outputs differ.

Just load your first GGUF/model, then the second, and voilà! Inference will firstly load for one model, then the second one.

### hashtagPrivacy first + Secure

Unsloth Studio can be used 100% offline and locally on your computer.

Its token-based authentication, including password and JWT access / refresh flows keeps your data secure and under your control.

circle-exclamation

Please note this is theBETAversion of Unsloth Studio. Expect many improvements, fixes, and new features in the coming days and weeks. One issue we’re actively addressing is precompiled llama.cpp binaries to significantly speed up install times.

## hashtag⚡ Quickstart

Unsloth Studio works on Windows, Linux, WSL and MacOS (chat only currently).

* CPU:Unsloth still works without a GPU, but only forChatinference.
* Training:Works on NVIDIA GPUs: RTX 30, 40, 50, Blackwell, DGX Spark/Station etc.
* Mac:Like CPU - Chat only works for now.MLXtraining coming very soon.
* AMD:Chat works. Train withUnsloth Core. Studio support is coming soon.
* Coming soon:Training support forApple MLX,AMD, andIntel.
* Multi-GPU:Works already, with a major upgrade on the way.

#### hashtagWindows, MacOS, Linux, WSL:

circle-exclamation

First install may take 5-10 minutes. This is normal asllama.cppneeds to compile binaries. We're working on precompiled binaries so next time it won't take so long.

#### hashtagDocker:

Our Docker imagenow works for Studio! We're working on Mac compatibilityunsloth/unsloth. Read ourDocker guide.

#### hashtagPip:

For more details about installation please visit theUnsloth Studio Installsection.You can also view NVIDIA'sVideo Tutorial here.

arrow-down-to-square
Installation
chevron-right

### hashtaggoogleGoogle Colab notebook

We’ve created afree Google Colab notebookarrow-up-rightso you can explore all of Unsloth’s features on Colab’s T4 GPUs. You can train and run most models up to 22B parameters, and switch to a larger GPU for bigger models. Just Click 'Run all' and the UI should pop up after installation.

circle-exclamation

It'll take 30+ mins for llama.cpp to compile on a T4 GPU, thus we recommend using a bigger GPU for faster speeds.

Google Colab
colab.research.google.com
chevron-right

Once installation is complete, scroll toStart Unsloth Studioand clickOpen Unsloth Studioin the white box shown on the left:

circle-exclamation

Sometimes the Studio link may return an error. This happens because Google Colab expects you to stay on the Colab page; if it detects inactivity, it may shut down the GPU session.

## hashtagseedlingWorkflow

Here is a usual workflow of Unsloth Studio to get you started:

1. Launch Studio frominstall instructions.
2. Load a model from local files or a supported integration.
3. Import training data from PDFs, CSVs, or JSONL files, or build a dataset from scratch.
4. Clean, refine, and expand your dataset inData Recipes.
5. Start training with recommended presets or customize the config yourself.
6. Chat with the trained model and compare its outputs against the base model.
7. Save or exportlocally to the stack you already use.

You can read our individual deep dives into each section of Unsloth Studio:

bolt
Get Started
chevron-right
box-isometric
Model Export
chevron-right
hat-chef
Data Recipes
chevron-right
comment-dots
Studio Chat
chevron-right

## hashtagvideoVideo Tutorials

Here is a video tutorial created by NVIDIA to get you started with Studio:

## hashtagcomments-questionFAQ

Does Unsloth collect or store data?We do not collect usage telemetry. We only collect the minimal hardware information required for compatibility, such as GPU type and device (e.g. Mac). Unsloth Studio runs 100% offline and locally.

How do I use an old / exisiting model that I downloaded previously from Hugging Face?Yes, you can use pre-exisiting or old models or GGUFs that you previously downloaded from Hugging Face etc. Read ourinstructions here.

Does Unsloth Studio support OpenAI-compatible APIs?Yes, for our Data Recipes it does. For inference we are working on this and hope to release support for it as soon as this week so stay tuned!

Is Unsloth now licensed under AGPL-3.0?Unsloth uses a dual-licensing model of Apache 2.0 and AGPL-3.0. The core Unsloth package remains licensed underApache 2.0arrow-up-right, while certain optional components, such as the Unsloth Studio UI are licensedAGPL-3.0arrow-up-right.

This structure helps support ongoing Unsloth development while keeping the project open source and enabling the broader ecosystem to continue growing.

Does Studio only support LLMs?No. Studio supports a range of supportedtransformerscompatible model families, including text, multimodal models,text-to-speech, audio,embeddings, and BERT-style models.

Can I use my own training config?Yes. Import a YAML config and Studio will pre-fill the relevant settings.

Do you need to train models to use the UI?No, you can just download any GGUF or model without fine-tuning any model.

#### hashtagFuture of Unsloth

We're working hard to make open-source AI as accessible as possible. Coming next for Unsloth and Unsloth Studio, we're releasing official support for: multi-GPU, Apple Silicon/MLX, AMD, and Intel. Reminder this is the BETA version of Unsloth Studio so expect a lot of announcements and improvements in the coming weeks. We’re also working closely with NVIDIA on multi-GPU support to deliver the best and simplest experience possible.

#### hashtagAcknowledgements

A huge thank you to NVIDIA and Hugging Face for being part of our launch. Also thanks to all of our early beta testers for Unsloth Studio, we truly appreciate your time and feedback. We’d also like to thank llama.cpp, PyTorch and open model labs for providing the infrastructure that made Unsloth Studio possible.

Previous
DPO, ORPO, KTO
chevron-left
Next
Get Started
chevron-right

Last updated25 minutes ago

Was this helpful?
