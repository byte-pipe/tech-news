---
title: GitHub - handy-computer/transcribe.cpp: ggml speech-to-text inference for 16+ model families · GitHub
url: https://github.com/handy-computer/transcribe.cpp
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-20T12:02:55.014771
---

# GitHub - handy-computer/transcribe.cpp: ggml speech-to-text inference for 16+ model families · GitHub

**handy-computer Transcribe.cpp: GGML speech-to-text inference library**

The easy speech recognition library used for different types of speech models, including those using Metal, Vulkan, and CUDA backends. It supports 16 model families and over 60 variants in various formats.

Key Features:

* Runs diverse speech-to-text model families via `GGUFmodels` on the `ggmlruntime`
* Includes support for multiple backends (Metal, Vulkan, and CUDA)
* Numerically verified and WER-tested against reference implementation
* Supported models include:
  * Parakeet (10 variants: TDT, RNN-T, CTC, TDT+CTC)
  * Canary (canary-1b and canary-v2)
  * Canary-Qwen (canary-qwen-2.5B)
  * Whisper (12 variants with tiny through large-v3-turbo models)
* Other supported models include GigaAM, Moonshine, Qwen3-asr, Cohere Transcribe, SenseVoice, FunASR-Nano, Nemotron Speech Streaming, and Multitalker Parakeet Streaming.