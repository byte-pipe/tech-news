---
title: GitHub - RunanywhereAI/RCLI: Talk to your Mac, query your docs, no cloud required. On-device voice AI + RAG · GitHub
url: https://github.com/RunanywhereAI/rcli
date: 2026-03-10
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-11T13:13:32.964088
---

# GitHub - RunanywhereAI/RCLI: Talk to your Mac, query your docs, no cloud required. On-device voice AI + RAG · GitHub

# RCLI – On‑device Voice AI for macOS

## Overview
- Full STT + LLM + TTS pipeline running natively on Apple Silicon (macOS 13+).  
- No cloud services or API keys required.  
- Provides 38 macOS actions, local RAG over your documents, and sub‑200 ms end‑to‑end latency.  
- Powered by MetalRT, a proprietary GPU inference engine built for Apple Silicon.

## Installation
- **One‑line script**:  
  `curl -fsSL https://raw.githubusercontent.com/RunanywhereAI/RCLI/main/install.sh | bash`
- **Homebrew**:  
  ```bash
  brew tap RunanywhereAI/rcli https://github.com/RunanywhereAI/RCLI.git
  brew install rcli
  rcli setup   # downloads AI models (~1 GB, one‑time)
  ```
- Requires Apple Silicon with M3 or later for MetalRT; M1/M2 fall back to llama.cpp.  
- Troubleshooting for checksum errors includes force‑refreshing the tap, clearing the Homebrew cache, and re‑tapping.

## Quick Start Commands
- `rcli` – launch interactive TUI (push‑to‑talk + text).  
- `rcli listen` – continuous voice mode.  
- `rcli ask "open Safari"` – one‑shot text command.  
- `rcli metalrt` – manage MetalRT engine.  
- `rcli llamacpp` – manage llama.cpp engine.

## Features

### Voice Pipeline
- **VAD** – Silero voice activity detection.  
- **STT** – Zipformer streaming or Whisper/Parakeet offline models.  
- **LLM** – Qwen3 / LFM2 series with KV‑cache continuation and Flash Attention.  
- **TTS** – Double‑buffered sentence‑level synthesis.  
- Tool calling via LLM‑native formats.  
- Multi‑turn memory with sliding‑window conversation history and token‑budget trimming.

### 38 macOS Actions
| Category | Example Actions |
|----------|-----------------|
| Productivity | `create_note`, `create_reminder`, `run_shortcut` |
| Communication | `send_message`, `facetime_call` |
| Media | `play_on_spotify`, `play_apple_music`, `play_pause`, `next_track`, `set_music_volume` |
| System | `open_app`, `quit_app`, `set_volume`, `toggle_dark_mode`, `screenshot`, `lock_screen` |
| Web | `search_web`, `search_youtube`, `open_url`, `open_maps` |

- Actions are routed by the LLM to AppleScript or shell commands.  
- Toggle actions in the TUI; press **X** to clear conversation and reset context.

### Local RAG (Document Q&A)
- Index PDFs, DOCX, and plain‑text files; hybrid vector + BM25 retrieval (~4 ms latency over 5k+ chunks).  
- Commands:  
  - `rcli rag ingest <directory>` – build index.  
  - `rcli ask --rag <index> "<question>"` – query indexed docs.

### Interactive TUI
| Key | Action |
|-----|--------|
| SPACE | Push‑to‑talk |
| M | Browse / download / hot‑swap models |
| A | Browse / enable / disable macOS actions |
| R | Ingest documents for RAG |
| X | Clear conversation / reset context |
| T | Toggle tool‑call trace |
| ESC | Exit |

## MetalRT GPU Engine
- Proprietary inference engine delivering up to **550 tok/s** LLM throughput and sub‑200 ms voice latency.  
- Requires Apple M3 or later (Metal 3.1 features).  
- Falls back to llama.cpp on M1/M2.  
- Install/status: `rcli metalrt install`, `rcli metalrt status`.  
- Supported models: Qwen3 0.6B/4B, Llama 3.2 3B, LFM2.5 1.2B (LLM); Whisper Tiny/Small/Medium (STT); Kokoro 82M with 28 voices (TTS).  
- Proprietary license; contact founder@runanywhere.ai for inquiries.

## Supported Models
- **LLM**: LFM2 1.2B (default), LFM2 350M, LFM2.5 1.2B, LFM2 2.6B, Qwen3 0.6B, Qwen3.5 0.8B/2B/4B, Qwen3 4B.  
- **STT**: Zipformer (streaming), Whisper base.en (default), Parakeet TDT 0.6B (~1.9 % WER).  
- **TTS**: Piper Lessac/Amy, KittenTTS Nano, Matcha LJSpeech, Kokoro English/Multi‑lang.  
- Default install (~1 GB): LFM2 1.2B + Whisper + Piper + Silero VAD + Snowflake embeddings.  
- Management commands: `rcli models`, `rcli upgrade-llm`, `rcli voices`, `rcli cleanup`.

## Building from Source
```bash
git clone https://github.com/RunanywhereAI/RCLI.git
cd RCLI
bash scripts/setup.sh
bash scripts/download_models.sh
mkdir -p build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake --build . -j $(sysctl -n hw.ncpu)
./rcli
```
- CPU‑only build uses llama.cpp + sherpa‑onnx (no MetalRT).  
- Requires CMake 3.15+, Apple Clang (C++17).

## CLI Reference
- `rcli` – interactive TUI.  
- `rcli listen` – continuous voice mode.  
- `rcli ask <text>` – one‑shot command.  
- `rcli actions [name]` – list or detail actions.  
- `rcli rag ingest <dir>` / `rcli rag query <text>` – RAG workflow.  
- `rcli models [llm|stt|tts]` – manage AI models.  
- `rcli voices` – browse / switch TTS voices.  
- `rcli metalrt` / `rcli llamacpp` – engine management.  
- `rcli setup` – download default models.  
- `rcli info` – show engine and model info.  
- Options: `--models <dir>` (default `~/Library/RCLI/models`), `--rag <index>`.

## Benchmarks & Resources
- MetalRT decode throughput vs. llama.cpp and Apple MLX on Apple M3 Max.  
- STT/TTS real‑time factor: MetalRT STT **714×** faster than real‑time.  
- Further reading:  
  - https://www.runanywhere.ai/blog/metalrt-fastest-llm-decode-engine-apple-silicon  
  - https://www.runanywhere.ai/blog/metalrt-speech-fastest-stt-tts-apple-silicon  
  - https://www.runanywhere.ai/blog/fastvoice-on-device-voice-ai-pipeline-apple-silicon