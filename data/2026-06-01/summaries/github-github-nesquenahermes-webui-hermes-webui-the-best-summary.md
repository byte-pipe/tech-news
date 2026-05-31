---
title: GitHub - nesquena/hermes-webui: Hermes WebUI: The best way to use Hermes Agent from the web or from your phone! · GitHub
url: https://github.com/nesquena/hermes-webui
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:19:22.375747
---

# GitHub - nesquena/hermes-webui: Hermes WebUI: The best way to use Hermes Agent from the web or from your phone! · GitHub

# Hermes WebUI Overview

## Repository Structure
- Main directories: `.github/workflows`, `api`, `docs`, `scripts`, `static`, `tests`
- Key files: `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `Dockerfile`, `server.py`, `bootstrap.py`, `ctl.sh`, `start.sh`
- Configuration examples: `.env.example`, `.env.docker.example`
- Documentation files: `AGENTS.md`, `ARCHITECTURE.md`, `DESIGN.md`, `ROADMAP.md`, `THEMES.md`

## What is Hermes WebUI?
- Lightweight, dark‑themed web interface for the Hermes Agent.
- Provides full parity with the CLI: any terminal command can be performed via the UI.
- Built with only Python and vanilla JavaScript; no build step, framework, or bundler.
- Layout:
  - Left sidebar: sessions and navigation.
  - Center panel: chat interaction.
  - Right panel: workspace file browser with inline preview.
  - Footer (composer): model, profile, workspace controls, token‑usage ring.
- Features:
  - Light mode with full profile support.
  - Password‑protected settings.
  - Workspace browsing, session projects, tags, and tool call cards.
  - Secure access via SSH tunnel; single command to start and tunnel.

## Why Choose Hermes?
- **Persistent memory**: retains user profile, notes, and reusable skills across sessions.
- **Self‑hosted scheduling**: cron‑like jobs run offline, delivering results to many messaging platforms.
- **Multi‑platform reach**: works in terminal, 10+ messaging apps (Telegram, Discord, Slack, Signal, email, etc.).
- **Self‑improving skills**: automatically writes and saves new skills from experience.
- **Provider‑agnostic**: supports OpenAI, Anthropic, Google, DeepSeek, OpenRouter, and others.
- **Agent orchestration**: can spawn Claude Code or Codex for heavy coding tasks and integrate results.
- **Self‑hosted**: all data, memory, and compute stay on your hardware.

### Comparison with Competitors
| Feature | Hermes | OpenClaw | Claude Code | Codex CLI | OpenCode |
|---|---|---|---|---|---|
| Persistent memory (auto) | ✅ | ✅ | Partial | Partial | Partial |
| Self‑hosted scheduling | ✅ | ✅ | ❌ | ❌ | ❌ |
| Messaging app access (15+ platforms) | ✅ | ✅ | Partial | ❌ | ✅ |
| Web UI (self‑hosted) | ✅ | ✅ | ❌ | ❌ | ✅ |
| Self‑improving skills | ✅ | ✅ (marketplace) | ❌ | ❌ | ❌ |
| Python/ML ecosystem | ✅ | ✅ | ❌ | ❌ | ❌ |
| Provider‑agnostic | ✅ | ✅ | ❌ (Claude only) | ✅ | ✅ |
| Open source (MIT) | ✅ | ✅ | ✅ | ✅ | ✅ |

- Closest competitor: **OpenClaw** – both are always‑on, self‑hosted agents with memory and scheduling. Hermes differs by auto‑saving skills, higher stability, and native Python integration.

## Quick Start Guide
1. Clone and bootstrap:
   ```bash
   git clone https://github.com/nesquena/hermes-webui.git hermes-webui
   cd hermes-webui
   python3 bootstrap.py
   ```
2. Or use the provided launcher:
   ```bash
   ./start.sh
   ```
3. Daemon control via `ctl.sh`:
   - `./ctl.sh start` – runs in background, PID stored at `~/.hermes/webui.pid`.
   - `./ctl.sh status` – shows PID, uptime, host/port, log path.
   - `./ctl.sh logs --lines 100` – tail log file.
   - `./ctl.sh restart` / `./ctl.sh stop` – manage lifecycle.
   - Supports environment overrides, e.g., `HERMES_WEBUI_HOST=0.0.0.0 ./ctl.sh start`.

## Optional Session Recall Prefill
- WebUI can attach **ephemeral prefill messages** to new browser sessions, useful when external note sources (Joplin, Obsidian, Notion, etc.) provide durable context.
- Prefill can be a compact router‑style hint rather than a full note dump.
- Configuration options:
  - Static JSON file: `prefill_messages_file` or `HERMES_PREFILL_MESSAGES_FILE`.
  - Dynamic script hook:
    ```yaml
    webui_prefill_messages_script:
      - python3
      - /path/to/notes_recall.py
    webui_prefill_messages_script_timeout: 5
    ```
    Or via env vars:
    ```bash
    HERMES_WEBUI_PREFILL_MESSAGES_SCRIPT="python3 /path/to/notes_recall.py"
    HERMES_WEBUI_PREFILL_MESSAGES_SCRIPT_TIMEOUT=5
    ./ctl.sh restart
    ```
- Script output can be:
  - OpenAI‑style JSON message list.
  - JSON object with a `messages` list.
  - Plain text (wrapped as a single user prefill message).
  - System‑role messages for guidance.
- Output limited to 256 KiB; final context bounded by `webui_prefill_context_max_chars` or `HERMES_…` settings.