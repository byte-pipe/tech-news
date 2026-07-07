---
title: GitHub - kyutai-labs/pocket-tts: A TTS that fits in your CPU (and pocket) · GitHub
url: https://github.com/kyutai-labs/pocket-tts
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-07T12:04:44.792965
---

# GitHub - kyutai-labs/pocket-tts: A TTS that fits in your CPU (and pocket) · GitHub

### kyutai-labs/pocket-tts: A TTS that fits in your CPU (and pocket)

#### Key Points:

* **Micro-optimized** TTS application for efficient use of CPUs
* **Runs on:** only CPUs, no GPUs or web APIs required
* **Easy to implement**: use Python API and CLI with minimal installation
* **Multi-language support**: English, French, German, Portuguese, Italian, Spanish

#### Main takeaways:

* Extremely lightweight (100M parameters), suitable for CPU-intensive tasks
* Audio streaming capabilities with low latency (~200ms)
* Faster than real-time implementation on certain hardware
* Compatible with multiple languages and voices
* Can be run directly in web browsers or via CLI (uv installation required)

#### Additional features and instructions:

* **Try it out** without installing anything: visit the website, input text, and select voices to generate speech
* **Manual deployment**: use pip install pocket-tts to install without uv installation; optionally export voice with --voice, choose language with --languagewhen running generate or serve