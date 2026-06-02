---
title: GitHub - fathah/hermes-desktop: Desktop Companion for Hermes Agent · GitHub
url: https://github.com/fathah/hermes-desktop
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-03T01:54:04.794622
---

# GitHub - fathah/hermes-desktop: Desktop Companion for Hermes Agent · GitHub

# Hermes Desktop – Overview

## Repository Snapshot
- Active development with 601 commits.
- Main languages: English, Simplified Chinese, Japanese.
- Contains source code, docs, tests, build configs, and contribution guidelines.

## Purpose
Hermes Desktop is a native GUI application that simplifies installing, configuring, and interacting with the Hermes Agent — a self‑improving AI assistant capable of tool use, multi‑platform messaging, and closed‑loop learning.

## Installation Highlights
- **Windows**: Unsigned installer; bypass SmartScreen warning. For WSL, grant temporary password‑less sudo to allow Playwright dependency installation.
- **Fedora (RPM)**: `dnf install ./hermes-desktop-<version>.rpm`; use `--nogpgcheck` if signature checking is enforced. Auto‑updates not supported for RPM builds.

## Core Features
- Guided first‑run installation with progress tracking.
- Local or remote backend connectivity (default local at `127.0.0.1:8642`).
- Multi‑provider LLM support (OpenRouter, Anthropic, OpenAI, Gemini, Grok, Nous, Qwen, MiniMax, Hugging Face, Groq, and any OpenAI‑compatible endpoint).
- Streaming chat UI with SSE, markdown rendering, syntax highlighting, and live token‑usage display.
- 22 slash commands for quick actions (e.g., `/new`, `/clear`, `/web`, `/code`, `/usage`).
- Session management with full‑text SQLite search and date‑grouped history.
- Profile switching for isolated Hermes environments.
- 14 built‑in toolsets (web, browser, terminal, file, vision, image generation, TTS, etc.).
- Memory system with editable entries and multiple providers (Honcho, Hindsight, Mem0, etc.).
- Persona editor for customizing the agent’s SOUL.md personality.
- Model management (CRUD) across providers.
- Cron‑style scheduled tasks with 15 delivery targets.
- 16 messaging gateways (Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, iMessage, DingTalk, Feishu/Lark, WeCom, WeChat, Webhooks, Home Assistant).
- Hermes Office (Claw3d) visual 3D interface.
- Backup, import, debug dump, and log viewer in Settings.
- Auto‑updater via electron‑updater.
- Internationalization ready (English locale, community translations welcome).
- Comprehensive test suite using Vitest.

## How It Works
1. Choose local Hermes installation or remote API connection.
2. Local mode: checks `~/.hermes`; if missing, runs official installer (Git, uv, Python 3.11+).
3. Remote mode: prompts for API URL and key, validates connection.
4. Select LLM provider or local endpoint; store configuration in Hermes config files.
5. Launch main workspace; chat requests are sent to the chosen backend using SSE streaming, with real‑time rendering of tool progress and token usage.

## Main Screens
- **Chat**: Streaming conversation with slash commands and token tracking.
- **Sessions**: Browse, search, and resume past chats.
- **Agents**: Manage Hermes profiles.
- **Skills**: Install and manage skill packages.
- **Models**: Configure model settings per provider.
- **Memory**: Edit memory entries and provider settings.
- **Soul**: Edit agent persona.
- **Tools**: Enable/disable individual toolsets.
- **Schedules**: Create cron jobs.
- **Gateway**: Configure messaging integrations.
- **Office**: Set up Claw3d visual interface.
- **Settings**: Provider credentials, backups, logs, theme, network.

## Supported LLM Providers
- OpenRouter (200+ models, recommended)
- Anthropic (Claude)
- OpenAI (GPT)
- Google Gemini
- xAI Grok
- Nous Portal
- QwenAI
- MiniMax (global & China)
- Hugging Face (HF Inference)
- Groq (fast inference)
- Any OpenAI‑compatible local endpoint (LM Studio, Atomic Chat, Ollama, vLLM, llama.cpp)

## Supported Messaging Platforms
Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email (IMAP/SMTP), SMS (Twilio/Vonage), iMessage (BlueBubbles), DingTalk, Feishu/Lark, WeCom, WeChat (iLink Bot), Webhooks, Home Assistant.