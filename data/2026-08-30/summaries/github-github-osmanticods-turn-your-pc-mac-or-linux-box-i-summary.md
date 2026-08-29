---
title: GitHub - Osmantic/ODS: Turn your PC, Mac, or Linux box into an AI server. LLM inference, chat UI, voice, agents, workflows, RAG, and image generation....
url: https://github.com/Osmantic/ODS
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:03:49.012025
---

# GitHub - Osmantic/ODS: Turn your PC, Mac, or Linux box into an AI server. LLM inference, chat UI, voice, agents, workflows, RAG, and image generation....

# ODS – Osmantic Deployment System Overview

## What is ODS?
- A one‑command installer that turns a PC, Mac, or Linux box into a private AI server.
- Bundles local model inference, chat UI, control dashboard, voice/agents, RAG, image generation, and privacy/observability tools.
- Works without cloud services; cloud or hybrid API modes are optional.

## Key Features
- **Local inference** – runs open‑source models on your own hardware (CPU/GPU).
- **ChatGPT‑style web UI** – Open WebUI accessible via browser.
- **Control dashboard** – manage models, services, GPU status, extensions.
- **Voice, agents, workflows** – automation that can listen, speak, call tools.
- **RAG & search** – connect local documents and private retrieval pipelines.
- **Image generation** – run local image models without external APIs.
- **Privacy & ops** – local storage of prompts, secrets, observability stack.

## Installation
- **Linux/macOS**: `curl -fsSL https://install.osmantic.com/ods.sh | bash`
- **Windows PowerShell**: runs a script that downloads the source ZIP and executes `install.ps1`.
- Prerequisite: Docker (Docker Desktop with WSL2 on Windows).
- Cloud mode (`./install.sh --cloud`) uses OpenAI/Anthropic/Together APIs when no GPU is available.
- Ports are configurable via environment variables (e.g., `WEBUI_PORT=9090`).

## Uninstall
- Linux/macOS: `./ods-uninstall.sh --force`
- Windows: `.\ods.ps1 uninstall --force`

## Runtime Endpoints
- Ollama server: `http://localhost:11434` (Linux Docker) or `http://localhost:8080` (macOS/Windows native) unless overridden.
- Open WebUI: `http://localhost:3000`.

## Target Audience
- Users who want a private AI setup at home, in a lab, or on a workstation.
- Those who prefer not to manually wire together multiple services (Ollama, Open WebUI, n8n, ComfyUI, etc.).

## Platform Support
| Platform | Status |
|----------|--------|
| Linux (NVIDIA, AMD, Intel Arc) | Supported |
| Windows (NVIDIA, AMD) | Supported |
| macOS (Apple Silicon) | Supported |

Tested Linux distributions include Ubuntu 22.04/24.04, Debian 12, Fedora 41+, Rocky Linux 9, Arch, Manjaro, CachyOS, openSUSE Tumbleweed.

## Release Validation
- Operational changes pass a release‑grade gate covering zero‑prereq bootstrap, clean installs, full‑model capabilities, lifecycle recovery, and a “User Green” gate.
- Validation matrix and detailed process are documented in the repository.

## Documentation & Resources
- README, ARCHITECTURE.md, CLAUDE.md, CONTRIBUTING.md, and other docs in the repo root.
- Friendly Guide and audio walkthrough for newcomers.
- Security policy, audit reports, and contributor guidelines are also provided.