---
title: GitHub - Tencent/BrowserSkill: Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation a...
url: https://github.com/Tencent/BrowserSkill
date: 2026-08-30
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:02:17.217759
---

# GitHub - Tencent/BrowserSkill: Let AI agents use your real, logged-in browser without interrupting your work. CLI + extension for browser automation a...

# BrowserSkill (Tencent)

## Overview
- Enables AI agents to control a real, logged‑in browser without interrupting the user’s work.  
- Connects agents such as Cursor, Claude Code, Codex, OpenClaw, CodeBuddy, WorkBuddy, Pi, Hermes Agent, DeepSeek Harness, and others to the browser via a CLI and a browser extension.  
- Agents can explicitly borrow a tab, perform tasks, and return it, leaving other windows untouched.

## Advantages
- **Reuse real login state** – agents work with sites you are already signed into, avoiding separate test accounts.  
- **Uninterrupted workflow** – tasks run in a separate visible “Agent Window,” so you can keep using your own browser.  
- **Agent‑agnostic** – any shell‑capable agent can use BrowserSkill through the `bsk` CLI, with no lock‑in to a specific model or framework.  
- **Human‑in‑the‑loop** – when a task hits a captcha, login, or confirmation dialog, the agent can ask you to intervene and then continue.

## Runtime Environment
- **Components**: `bsk` CLI/daemon and BrowserSkill browser extension.  
- **Supported operating systems**: macOS (Apple Silicon & Intel), Linux (x64 & ARM64), Windows x64.  
- **Supported browsers**: Chrome, Microsoft Edge; other Chromium‑based browsers are expected to work; Firefox support is planned.

## Quick Start
### Install via Agent (recommended)
1. Run the one‑line installer referenced in `AGENT_INSTALL.md`; the agent will install the CLI and guide you through loading the extension.  

### Manual Install
1. **Install the CLI**  
   - macOS / Linux:  
     ```sh
     curl -fsSL https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.sh | sh
     ```  
   - Windows PowerShell:  
     ```powershell
     irm https://raw.githubusercontent.com/Tencent/BrowserSkill/main/install.ps1 | iex
     ```  
   - Verify with `bsk --version`.  
2. **Install the browser extension** from the Chrome Web Store or Microsoft Edge Add‑ons (or the Chrome Web Store build for other Chromium browsers).  
3. **Install the skill** into your agent harness:  
   - Run `bsk install-skill`, select the desired harness (Cursor, Claude Code, Codex, OpenClaw, CodeBuddy, WorkBuddy, Pi, Hermes Agent, etc.), and press Enter.  
   - Use `bsk install-skill --list` to view available variants.  
   - For other harnesses, copy `skill/SKILL.md` into the harness’s skills directory manually.

## DeepSeek Harness Plugin
- Distributed as npm package `@wxg-prc-cpg/browser-skill-dsh-plugin`.  
- Provides native `browser_*` tools and a live Web UI overlay for each Agent Window.  
- Install with:  
  ```sh
  dsh plugin --profile web add @wxg-prc-cpg/browser-skill-dsh-plugin
  dsh --profile web
  ```  
- The plugin includes its own copy of the skill, so `bsk install-skill` is not required, but the CLI and browser extension remain prerequisites.

## How It Works
1. The agent issues a shell command to the `bsk` CLI.  
2. The CLI communicates via local IPC with the `bsk` daemon.  
3. The daemon forwards the request over a WebSocket (127.0.0.1) to the BrowserSkill extension.  
4. The extension performs the action in an isolated “Agent Window,” borrowing user tabs only when explicitly requested.

## For Developers
- The repository is a Cargo + pnpm workspace.  
- **crates/bsk-cli** – CLI and daemon implementation.  
- **crates/bsk-protocol** – Shared wire types and JSON schemas.  
- **apps/extension** – Browser extension source.  
- **packages/ui** & **packages/i18n** – Shared UI and internationalization for the extension.  
- **packages/dsh-plugin-browserskill** – DeepSeek Harness plugin.  
- **evals/browser** – Deterministic local pages and agent‑neutral browser capability evaluation.

## License
- MIT License.