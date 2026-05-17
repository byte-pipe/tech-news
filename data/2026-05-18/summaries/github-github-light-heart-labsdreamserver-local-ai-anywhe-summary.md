---
title: GitHub - Light-Heart-Labs/DreamServer: Local AI anywhere, for everyone — LLM inference, chat UI, voice, agents, workflows, RAG, and image generation....
url: https://github.com/Light-Heart-Labs/DreamServer
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-05-18T06:01:22.041105
---

# GitHub - Light-Heart-Labs/DreamServer: Local AI anywhere, for everyone — LLM inference, chat UI, voice, agents, workflows, RAG, and image generation....

# Dream Server Overview

## What is Dream Server?
- A local‑first AI stack that provides LLM inference, chat UI, voice, agents, workflows, RAG, image generation, and privacy tools.
- Runs entirely on user hardware with a single command; cloud or hybrid modes are optional.
- Aims to give users sovereignty over their AI data, costs, and uptime.

## Supported Platforms
- **Linux** (NVIDIA, AMD, Intel Arc) – install and run today. Tested on Ubuntu 24.04/22.04, Debian 12, Fedora 41+, Arch, CachyOS, openSUSE Tumbleweed.
- **Windows** (NVIDIA, AMD) – requires Docker Desktop with WSL2; GPU passthrough for NVIDIA, AMD Strix Halo path documented.
- **macOS** (Apple Silicon, M1+) – requires Docker Desktop; llama‑server runs natively with Metal acceleration, other services in Docker.

## Why Choose Dream Server?
- Eliminates the need for deep technical expertise or extensive CUDA driver debugging.
- One‑click installer detects GPU, selects optimal model, generates credentials, and launches the full stack.
- Immediate chat experience via “bootstrap mode” while the full model downloads in the background.
- All services (chat, agents, voice, workflows, search, RAG, image generation, observability, developer tools) are pre‑wired and ready to use.
- Fully modular: each service is an extension that can be added by dropping a folder and running `dream enable`.

## Installation Quickstart
- **Linux (Docker)**  
  ```bash
  curl -fsSL https://raw.githubusercontent.com/Light-Heart-Labs/DreamServer/main/dream-server/get-dream-server.sh | bash
  # then open http://localhost:3000
  ```
- **Windows (PowerShell)**  
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  git clone https://github.com/Light-Heart-Labs/DreamServer.git
  cd DreamServer
  .\install.ps1
  ```
- **macOS (Apple Silicon)**  
  ```bash
  git clone https://github.com/Light-Heart-Labs/DreamServer.git
  cd DreamServer/dream-server
  ./install.sh
  ```
- Cloud mode available with `./install.sh --cloud` to use OpenAI/Anthropic/Together APIs instead of local inference.
- All ports are configurable via environment variables (see `.env.example`).

## Core Components Included
### Chat & Inference
- Open WebUI – full‑featured chat with history, web search, document upload, 30+ languages.
- llama‑server – high‑performance LLM inference with continuous batching; auto‑selected model per GPU.
- LiteLLM – API gateway supporting local, cloud, and hybrid modes.
- TEI Embeddings – text‑embedding service for RAG and search.

### Voice
- Whisper – speech‑to‑text.
- Kokoro – text‑to‑speech.

### Agents & Automation
- Hermes Agent – local‑first autonomous/browser agent with memory and skills.
- OpenClaw – autonomous AI agent framework.
- n8n – workflow automation with 400+ integrations.
- APE – Agent Policy Engine for auditing tool calls.
- OpenCode – browser‑based AI coding assistant.
- Memory Shepherd – helper for agent memory lifecycle.

### Knowledge & Search
- Qdrant – vector database for retrieval‑augmented generation.
- SearXNG – self‑hosted, no‑tracking web search.
- Perplexica – deep research engine.
- Brave Search – optional paid API integration.

### Creative
- ComfyUI – node‑based image generation.

### Privacy & Operations
- Privacy Shield – PII scrubbing proxy for API calls.
- Dashboard – real‑time GPU metrics, service health, model management.
- Dashboard API – health, setup, status, metrics, and management endpoints.
- Token Spy – monitors token usage for local and proxied LLM traffic.
- Langfuse – optional LLM observability and tracing.

## Hardware Auto‑Detection
- Installer automatically detects GPU type and selects the optimal model (default `MODEL_PROFILE=qwen`), removing the need for manual configuration.