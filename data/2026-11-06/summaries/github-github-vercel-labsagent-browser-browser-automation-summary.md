---
title: GitHub - vercel-labs/agent-browser: Browser automation CLI for AI agents · GitHub
url: https://github.com/vercel-labs/agent-browser
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:29:30.169351
---

# GitHub - vercel-labs/agent-browser: Browser automation CLI for AI agents · GitHub

# agent-browser – Browser automation CLI for AI agents

## Overview
- Native Rust command‑line tool that lets an AI agent control a browser one command at a time.  
- Takes a snapshot of the page as a compact accessibility tree, assigning refs like `@e1` to interactive elements.  
- The agent acts on refs, reads a new snapshot to verify results, and repeats; the browser stays open between commands.

## Installation
- `npm install -g agent-browser` then `agent-browser install` (downloads Chrome for Testing).  
- Homebrew: `brew install agent-browser && agent-browser install`.  
- Linux: `agent-browser install --with-deps` (adds required system libraries).  
- No install needed: `npx agent-browser open example.com`.

## Quick start
1. `agent-browser open example.com` – open a page.  
2. `agent-browser snapshot -i` – interactive snapshot showing elements with refs.  
3. `agent-browser click @e1` – click an element using its ref.  
4. `agent-browser get url` – read the current URL.  
5. `agent-browser close` – close the session.  

- Re‑snapshot after navigation or DOM changes before using old refs.  
- Supports CSS selectors, text, XPath, and semantic locators (e.g., `agent-browser find role button click --name "Submit"`).  
- Click fails if the target is hidden, disabled, off‑screen, or covered; dismiss the blocker, re‑snapshot, and retry.

## How it works
- Each command is sent to a background daemon that launches a headless Chrome (or other engine) via the Chrome DevTools Protocol (CDP).  
- A separate daemon and browser are created per `--session`.  
- Daemon auto‑closes after one hour of inactivity, persisting state if session persistence is enabled.  
- Supports alternative browsers/engines: Lightpanda, Obscura, Mobile Safari (iOS Simulator), or cloud providers (Browserbase, Browserless, etc.).

## Integration for AI agents
- Skills matching the CLI version can be fetched:
  - `agent-browser skills get core` – core loop, refs, waiting, common workflows.  
  - `agent-browser skills get core --ref commands` – single reference (full command list).  
  - `agent-browser skills get core --full` – full reference + templates.  
  - `agent-browser skills list` – list specialized skills (electron, slack, dogfood, …).  
- Add to an agent harness: `npx skills add vercel-labs/agent-browser`.  
- The installed skill is a thin stub that loads the appropriate core skill, keeping agent instructions in sync with the CLI.  
- For MCP clients, `agent-browser mcp` starts an MCP server over stdio.

## Command categories
- **Navigate & read**: `open`, `back`, `forward`, `reload`, `read`, `snapshot`, `get`, `is`.  
- **Interact**: `click`, `dblclick`, `fill`, `type`, `press`, `keyboard`, `hover`, `focus`, `select`, `check`, `uncheck`, `scroll`, `drag`, `upload`, `mouse`, `find`.  
- **Wait**: `wait`.  
- **Capture**: `screenshot`, `pdf`, `record`, `download`, `diff`.  
- **Page & network state**: `cookies`, `storage`, `network`, `set`, `clipboard`, `eval`, `pushstate`.  
- **Tabs, frames, dialogs**: `tab`, `frame`, `dialog`.  
- **Debug & performance**: `console`, `errors`, `highlight`, `inspect`, `trace`, `profiler`, `vitals`, `react`, `a11y`.  
- **Sessions & auth**: `session`, `state`, `auth`, `profiles`, `confirm`, `deny`.  
- **Agents & integrations**: `skills`, `mcp`, `webmcp`, `flow`, `chat`, `batch`, `plugin`.  
- **Observe**: `stream`, `dashboard`.  
- **Setup**: `install`, `upgrade`, `doctor`, `connect`, `close`.  

Run `agent-browser --help` for the full list and per‑command help.

## Platforms
- Pre‑built native binaries for macOS (ARM64, x64), Linux (ARM64, x64, glibc, musl), and Windows (x64).  
- npm package automatically selects the correct binary for the host OS.

## Development
- Requires Node.js 24+, pnpm 11+, and Rust.  
- Build steps:  
  1. `pnpm install`  
  2. `pnpm build:source` (dashboard + native CLI)  
  3. `pnpm link --global && agent-browser install`  
- Rust checks: `cargo fmt -- --check`, `cargo clippy`, `cargo test`, `cargo test e2e -- --ignored --test-threads=1`.  
- `AGENTS.md` tracks files to update per release, documentation checks, and release process.

## Documentation & Resources
- Main site: **agent-browser.dev** – introduction, guides, reference.  
- Topics: Commands, Configuration, Security (auth vault, allowlists, policies, content boundaries), Vercel Sandbox integration, changelog.

## License
- Apache‑2.0.