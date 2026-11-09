---
title: GitHub - synchopate/llama-modchip: 🐋 Run 284B DeepSeek-V4-Flash (<59GiB RAM, 44.4 tok/s pp, 9.1-14.7 tok/s) & 30B MoEs (25-111 tok/s) on a pure 64GB C...
url: https://github.com/synchopate/llama-modchip
date: 2026-11-08
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-11-09T16:01:37.446931
---

# GitHub - synchopate/llama-modchip: 🐋 Run 284B DeepSeek-V4-Flash (<59GiB RAM, 44.4 tok/s pp, 9.1-14.7 tok/s) & 30B MoEs (25-111 tok/s) on a pure 64GB C...

# llama-modchip Overview

## Purpose and Highlights
- Provides ggml/llama.cpp kernel patches, quantization transcoders, and runtime tools for CPU‑first inference of large Mixture‑of‑Experts models (284 B DeepSeek‑V4‑Flash, 30 B MoE) entirely in system RAM.  
- Fits the 284 B model (56.56 GiB) into 64 GB RAM with zero swap; 30 B models run on 16–32 GB RAM.  
- No GPUs required for inference; optional hybrid CPU+GPU mode for higher throughput.  
- Performance: 44.4 tok/s prefill on a 16‑core Zen 5 for the 284 B model; 25–111 tok/s decode for 30 B MoE; KV cache restore in ~13 ms.

## Architecture & Memory Optimizations
- Kernel patches use a 4‑level register tiling (ZMM AVX‑512BW) and multi‑column scheduling, delivering +77 % prefill and +53 % decode speed.  
- Register‑stationary MQA FlashAttention and non‑temporal streaming keep cold expert weights from evicting hot KV cache lines.  
- Self‑speculative drafting with a 1.64 M‑layer L2/L3 drafter (Stockfish‑PVS) and O(1) rollback enables fast context restoration.  
- Quantization schemes:  
  * DeepSeek‑V4‑Flash: IQ1_S (1.5625 bpw) for routed experts, Fractal‑64 (Q2_0) for attention tensors, overall 1.71 bpw.  
  * Nemotron‑3.5‑30B‑A3B variants: Q4_0, MXFP4, Fractal‑64 with 3.75–4.5 bpw.

## Supported Models & Hardware Classes
| Class | RAM | Model | Checkpoint Size | Throughput (0 GPU) |
|------|-----|-------|----------------|--------------------|
| Developer laptop / Mini‑PC | 16–32 GB | Nemotron‑3.5‑30B‑A3B (14.35 GiB) | 3.75 bpw | 25–60 tok/s |
| Desktop / Server | 64 GB | DeepSeek‑V4‑Flash 284 B (56.56 GiB) | 1.71 bpw | 44.4 tok/s prefill, 9.1–14.7 tok/s decode |
| Hybrid CPU+GPU | 32–64 GB + 16 GB GPU | Nemotron‑30B / Qwen3‑30B | 3.75–4.25 bpw | 80.8 tok/s |
| 8‑Channel Workstation (Threadripper) | 128 GB+ | DeepSeek‑284B / Nemotron‑30B | – | 111.6 tok/s (30 B) |

## Quickstart (Linux/macOS)

1. Clone the repository and start the chat interface:  
   ```bash
   git clone https://github.com/synchopate/llama-modchip.git
   cd llama-modchip
   ./modchip chat
   ```

2. Run a pre‑compiled binary with a Hugging Face GGUF checkpoint:  

   *30 B Nemotron‑3.5‑A3B*  
   ```bash
   hf download Synchopate/NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64-CPU-GGUF \
       llama-server-modchip-linux-x86_64 NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64.gguf --local-dir .
   chmod +x llama-server-modchip-linux-x86_64
   ./llama-server-modchip-linux-x86_64 -m NVIDIA-Nemotron-3.5-30B-A3B-Fractal-64.gguf -c 262144 -t 16 --port 8080
   ```

   *284 B DeepSeek‑V4‑Flash*  
   ```bash
   hf download Synchopate/DeepSeek-V4-Flash-0731-Fractal-64GB-CPU-GGUF --local-dir ./dsv4
   chmod +x ./dsv4/llama-server-modchip-linux-x86_64
   ./dsv4/llama-server-modchip-linux-x86_64 -m ./dsv4/DeepSeek-V4-Flash-0731-Fractal-00001-of-00003.gguf -c 32768 -t 16 -fa on --port 8080
   ```

## Windows Usage
- Execute `windows/AVVIA_MODCHIP.bat` or run `./modchip` in Git Bash.  
- The script detects CPU cores, free RAM, and GPU VRAM, downloads appropriate CUDA/Vulkan binaries, computes the CPU‑MoE split, and launches the web UI at `http://127.0.0.1:8080`.

## Modchip Commands
| Command | Description |
|---------|-------------|
| `./modchip chat` | Interactive terminal chat with live token/s, TTFT, and Stockfish‑PVS telemetry |
| `./modchip web` | Dark‑mode web chat UI with live telemetry HUD |
| `./modchip bench` | 30‑second speed test and CPU benchmark scorecard |
| `./modchip claude` | Launch Claude Code CLI (40 tools) with 256K engine and fast restore |
| `./modchip eval` | Run reproducible 100‑point quality, tool‑calling, coding, and needle‑gate tests |
| `./modchip quantize` | Transcode BF16 / Q4_0 / UD‑IQ1_S GGUFs into Fractal‑64 format |

## Documentation
- Detailed architecture, quantization, and performance notes are in `ARCHITECTURE.md`, `FAQ.md`, and the `paper/` directory.  
- Release notes and changelog are available in `RELEASE_NOTES.md`.