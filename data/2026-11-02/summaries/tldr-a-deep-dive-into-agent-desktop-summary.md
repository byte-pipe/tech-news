---
title: A deep dive into agent-desktop
url: https://flaviocopes.com/agent-desktop
date: 2026-11-02
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-11-02T08:49:49.804730
---

# A deep dive into agent-desktop

# A deep dive into agent-desktop

## What is agent-desktop?
- Command‑line tool from Vercel Labs that lets coding agents interact with native desktop applications.
- Reads the operating system’s accessibility tree (the same structure used by screen readers) and returns JSON objects for each UI element.
- Each JSON object contains a reference (`ref`) that the agent can click, type into, or read.
- Works on macOS, Windows, and Linux; ships native binaries for x64 and ARM64.
- Licensed under Apache‑2.0.

## Relationship to agent-browser
- `agent-browser` is an older sibling that automates browsers via their accessibility tree.
- `agent-desktop` applies the same concept to the whole desktop; reference formats differ (desktop refs include a snapshot ID, e.g., `@s8f3k2p9:e8`).
- Both are CLIs only; they do not contain AI models and do not replace the agent that decides actions.

## How does agent-desktop work?
- **Observation → Action → Re‑observation** loop:
  1. `snapshot` command reads the accessibility tree of a target app and returns refs.
  2. Agent selects a ref and issues an action command (e.g., `click @s8f3k2p9:e8`).
  3. Another `snapshot` verifies the UI state after the action.
- No pixel‑matching is involved; screenshots are optional via a separate command.
- Rules and error handling:
  - Refs are tied to a specific snapshot; UI changes may cause `STALE_REF` or `AMBIGUOUS_TARGET` errors.
  - When multiple windows match, use `--window-id` with the ID provided in the error details.
  - For dense apps, start with a skeleton snapshot (`--skeleton`) then drill down with a root‑based snapshot.
- Execution modes:
  - Default is headless (accessibility API only, no pointer movement or clipboard use).
  - `--headed` flag enables physical input; should be used sparingly.
- Command output is a single JSON envelope; example for a successful click includes fields `version`, `ok`, `command`, and `data`.

## Installation
- **Global npm install (recommended):**  
  `npm install -g agent-desktop`  
  Verify with `agent-desktop version`.
- Alternative package managers: Bun, Yarn, pnpm (use `npx` for non‑global installs).
- Post‑install script replaces a Node launcher with a direct link to the native binary (≈21 ms per call). If scripts are blocked, calls fall back to the slower Node launcher (≈146 ms). Approve scripts via `npm install-scripts approve agent-desktop` or use `--allow-scripts`.
- Manual download: fetch native archive from GitHub Releases, place the helper binary alongside the executable, verify with `gh attestation verify <archive> --repo vercel-labs/agent-desktop`.
- Homebrew and Scoop packages are pending inclusion in default catalogs; check the installed binary path with `command -v agent-desktop` (macOS/Linux) or `Get-Command agent-desktop` (Windows).
- Building from source requires Rust 1.89+, platform‑specific toolchains (Xcode CLI tools on macOS, MSVC on Windows, C linker on Linux). Example:  
  ```
  git clone https://github.com/vercel-labs/agent-desktop
  cd agent-desktop
  cargo build --release -p agent-desktop
  ```

## Platform specifics
- **Linux:** npm install works with a user prefix (`--prefix "$HOME/.local"`). The tool reports OS, architecture, and CLI version in its `version` command output.
- Tested on Ubuntu 24.04.5 LTS (x86_64, glibc 2.39) with XFCE on X11; works with at‑spi2‑core installed.
- Minimum supported Linux environment: Ubuntu 24.04 or newer, GNOME 46, glibc ≥ 2.35.

## Usage example (macOS Finder)
```
agent-desktop snapshot --app Finder -i
agent-desktop click @s8f3k2p9:e8
agent-desktop snapshot --app Finder -i
```
- First snapshot assigns refs, the click uses a ref, the second snapshot confirms the result.

## Key takeaways
- `agent-desktop` provides a programmatic bridge between AI agents and native desktop UI via accessibility APIs.
- It operates entirely through JSON‑based commands, keeping the agent logic separate from the automation layer.
- Installation is straightforward via npm; optional manual download and source builds are supported.
- The tool is still early (v1.0.2 as of 30 Oct 2026) but already functional across major operating systems.