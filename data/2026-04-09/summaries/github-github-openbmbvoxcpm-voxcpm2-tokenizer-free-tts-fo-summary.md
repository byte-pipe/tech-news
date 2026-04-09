---
title: GitHub - OpenBMB/VoxCPM: VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning · GitHub
url: https://github.com/OpenBMB/VoxCPM
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-04-09T11:26:24.255262
---

# GitHub - OpenBMB/VoxCPM: VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning · GitHub

**VoxCPM2: Next-Generation Text-to-Speech**

* **Tokenizer-Free Architecture**: Directly generates continuous speech representations without discrete tokenization, leading to highly natural and expressive synthesis.
* **Multi-Language Support**: Synthesize text in 30 languages with no language tag required.
* **Voice Design**: Create a brand-new voice from a natural-language description alone (gender, age, tone, emotion, pace ...) without reference audio.
* **Controllable Cloning**: Clone any voice from a short reference clip, guided by style options to preserve timbre and nuance.
* **High-Quality Audio Output**: Accepts 16kHz reference audio and produces studio-quality audio via AudioVAE V2's asymmetric encode/decode design.

**Key Features**

* Supports 30 languages
* Has the ability to synthesize directly without language tag input
* Allows for voice design and control via natural-language descriptions of gender, age, tone, emotion, pace ...
* Enables controllable cloning and high-quality audio output

**Technical Specifications**

* Designed on a MiniCPM-4 backbone
* Supports 16kHz reference audio through super-resolution enabled by AudioVAE V2
* Offers highly scalable architecture with support for real-time streaming