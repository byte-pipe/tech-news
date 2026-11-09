---
title: GitHub - homeassistant-ai/ha-mcp: Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants. · GitHub
url: https://github.com/homeassistant-ai/ha-mcp
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-10T04:42:34.878265
---

# GitHub - homeassistant-ai/ha-mcp: Configure and automate Home Assistant with Claude, ChatGPT, and other AI assistants. · GitHub

# HA‑MCP – Manage Home Assistant with AI

## Overview
- HA‑MCP enables configuration and automation of Home Assistant through AI assistants such as Claude, ChatGPT, and others.  
- The project provides multiple ways to run a server that mediates between Home Assistant and AI clients.  
- It is compatible with all Home Assistant installation types (OS, Supervised, Container, Core).

## Installation options
- **HA‑MCP integration (recommended)** – installed via HACS or the built‑in Marketplace (Home Assistant 2026.11+). Runs an in‑process server with full feature parity.  
- **Home Assistant app / add‑on** – suitable for OS and Supervised installations; no access token required.  
- **Docker / PyPI / uvx (stdio)** – runs the server outside Home Assistant; useful for Container/Core setups or separate hosts.  
- **Manual custom component** – copy `custom_components/ha_mcp_tools` into the Home Assistant `custom_components` directory.

> Only one install method should be active for a given client; mixing methods can cause connection hangs.

## Quick start – HA‑MCP integration
1. Install the integration via HACS (Home Assistant 2026.8–2026.10) or Marketplace (2026.11+).  
2. Restart Home Assistant.  
3. Create a dedicated administrator account or generate a long‑lived access token.  
4. Add the integration: *Settings → Devices & Services → Add Integration → HA‑MCP Server*.  
5. Provide the token or account credentials, choose remote (webhook) and/or local network access, and submit.  
6. Copy the generated connect URL from the integration’s configuration screen.  
7. Paste the URL into your AI client to start using HA‑MCP.

- Remote access uses a Home Assistant webhook URL (`https://<ha-domain>/api/webhook/<id>`).  
- Local network access is available at `http://<ha-ip>:9584/private_<random>`.  
- An admin‑only HA‑MCP panel appears in the Home Assistant sidebar for managing tools, feature flags, backups, and themes.  
- Optional authentication can be switched to `ha_autht` to require a Home Assistant sign‑in instead of the secret URL.

## Home Assistant app (add‑on) installation
1. Add the repository `https://github.com/homeassistant-ai/ha-mcp` in *Settings → Apps → Repositories* (if not auto‑detected).  
2. Install **Home Assistant MCP Server** from the Apps store and start it.  
3. Retrieve the unique MCP URL from the logs tab.  
4. Connect your AI client to this URL; no additional token configuration is needed.

## Other install methods
- **Docker (HTTP mode)**: run `ghcr.io/homeassistant-ai/ha-mcp` with the Home Assistant URL and a long‑lived token.  
- **PyPI / uvx**: install the package and launch the server in stdio mode.  
- Each method provides a setup wizard that generates client‑specific configuration.

## Key features
- Full control of Home Assistant via natural‑language prompts.  
- Supports multiple AI back‑ends (Claude, Gemini, ChatGPT, etc.).  
- File and YAML editing tools are optional and disabled by default.  
- Remote webhook access works through Nabu Casa or any reverse proxy.  
- Theme and backup management through the HA‑MCP sidebar panel.  

## Repository layout (high‑level)
- `custom_components/ha_mcp_tools` – core integration code.  
- `ha_mcp` – server implementation.  
- `docs`, `templates`, `tests` – documentation, UI templates, and test suite.  
- Configuration files (`Dockerfile`, `docker‑compose.yml`, `pyproject.toml`, etc.) for various deployment methods.  
- Markdown files (`README.md`, `AGENTS.md`, `CHANGELOG.md`, etc.) provide detailed usage instructions.