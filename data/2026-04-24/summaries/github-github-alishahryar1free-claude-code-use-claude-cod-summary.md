---
title: GitHub - Alishahryar1/free-claude-code: Use claude-code for free in the terminal, VSCode extension or via discord like openclaw · GitHub
url: https://github.com/Alishahryar1/free-claude-code
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:01:31.477394
---

# GitHub - Alishahryar1/free-claude-code: Use claude-code for free in the terminal, VSCode extension or via discord like openclaw · GitHub

# Free Claude Code – Summary

## Overview
- A lightweight proxy that enables free use of Claude Code (CLI, VSCode, Discord/Telegram bots) without an Anthropic API key.  
- Routes Anthropic API calls to various back‑ends: NVIDIA NIM, OpenRouter, DeepSeek, LM Studio (local), or llama.cpp (local).  
- Works as a drop‑in replacement by setting two environment variables.

## Key Features
- **Zero Cost**: 40 requests/minute free on NVIDIA NIM; free models on OpenRouter; fully local options via LM Studio or llama.cpp.  
- **Provider Flexibility**: Supports five providers; each Claude model (Opus, Sonnet, Haiku) can be mapped to a different provider.  
- **Thinking Token Support**: Parses `<think>` tags and `reasoning_content` into native Claude thinking blocks.  
- **Tool Call Parsing**: Auto‑parses textual tool calls into structured tool usage.  
- **Request Optimization**: Intercepts trivial API calls locally to save quota and latency.  
- **Smart Rate Limiting**: Rolling‑window throttle, exponential back‑off on 429 responses, optional concurrency cap.  
- **Bots**: Discord/Telegram bots with autonomous coding, session persistence, and live progress.  
- **Subagent Control**: Forces `run_in_background=False` to prevent runaway subagents.  
- **Extensible Architecture**: BaseProvider and MessagingPlatform abstract classes for easy addition of new providers or platforms.

## Quick Start

### Prerequisites
1. Obtain an API key for the chosen provider (or use a fully local provider).  
   - NVIDIA NIM: `build.nvidia.com/settings/api-keys`  
   - OpenRouter: `openrouter.ai/keys`  
   - DeepSeek: `platform.deepseek.com/api_keys`  
   - LM Studio / llama.cpp: no key required.  
2. Install the `uv` tool (`pip install uv`).

### Installation & Configuration
```bash
git clone https://github.com/Alishahryar1/free-claude-code.git
cd free-claude-code
cp .env.example .env
```
- Edit `.env` to select a provider and set model variables (`MODEL_OPUS`, `MODEL_SONNET`, `MODEL_HAIKU`, `MODEL`).  
- Example for NVIDIA NIM:
  ```
  NVIDIA_NIM_API_KEY="nvapi-your-key-here"
  MODEL_OPUS="nvidia_nim/z-ai/glm4.7"
  ENABLE_THINKING=true
  ```

### Optional Authentication
- Set `ANTHROPIC_AUTH_TOKEN` in `.env` to require clients to send the same token via the `ANTHROPIC_AUTH_TOKEN` header.

### Running
1. Start the proxy server:  
   `uv run uvicorn server:app --host 0.0.0.0 --port 8082`  
2. Point Claude Code to the proxy: set `ANTHROPIC_BASE_URL` to `http://localhost:8082` (and optionally `ANTHROPIC_AUTH_TOKEN`).  
   - Bash example:  
     ```bash
     export ANTHROPIC_AUTH_TOKEN=freecc
     export ANTHROPIC_BASE_URL=http://localhost:8082
     claude
     ```

## IDE Integration

### VSCode Extension
1. Start the proxy server.  
2. Add to `settings.json` under `claudeCode.environmentVariables`:
   ```json
   [
     { "name": "ANTHROPIC_BASE_URL", "value": "http://localhost:8082" },
     { "name": "ANTHROPIC_AUTH_TOKEN", "value": "freecc" }
   ]
   ```
3. Reload the extension; authorize if prompted (ignore any credit purchase prompts).

### IntelliJ Extension
1. Edit the IDE’s `installed.json` (Windows) or `acp.json` (Linux/macOS) to include:
   ```json
   "env": {
     "ANTHROPIC_AUTH_TOKEN": "freecc",
     "ANTHROPIC_BASE_URL": "http://localhost:8082"
   }
   ```
2. Restart the IDE after starting the proxy.

## Model Picker (`claude-pick`)
- Interactive selector that lets you choose any model from the active provider at launch time.  
- Installation steps:
  1. Install `fzf` (`brew install fzf` on macOS/Linux).  
  2. Add an alias to your shell rc file:
     ```bash
     alias claude-pick="/absolute/path/to/free-claude-code/claude-pick"
     ```
  3. Reload the shell (`source ~/.zshrc` or `source ~/.bashrc`).  

Now you can run `claude-pick` to pick a model without editing `.env`.