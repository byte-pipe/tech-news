---
title: GitHub - Gaurav-Gosain/tuios: A terminal window manager that knows what your agents are doing. Tiling panes, workspaces, sessions that survive restart...
url: https://github.com/Gaurav-Gosain/tuios
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:32.967491
---

# GitHub - Gaurav-Gosain/tuios: A terminal window manager that knows what your agents are doing. Tiling panes, workspaces, sessions that survive restart...

# TUIOS: Terminal UI Operating System

## Overview
- Modern terminal multiplexer and window manager written in Go.
- Vim‑like modal interface with BSP tiling, kitty graphics protocol support, and a command palette.
- Daemon keeps sessions alive, synchronizes across machines, and lets coding agents report state through a unified Inbox.

## Documentation & Learning
- Full documentation hosted at tuios.dev and in the `docs/` folder.
- Interactive WebAssembly tour available at tuios.dev/learn.
- Release notes detail changes for each version (e.g., v0.8.5).

## Quick Links
- Getting Started, Keybindings, BSP Tiling, Layout Modes, Configuration, Hooks, Themes, Glyph Sets, CLI Reference, Tape Scripting, Sessions, Agents, tmux Shim, Control Protocol, Architecture.

## Installation

### Package Managers
- **Homebrew (macOS/Linux)**: `brew install tuios`
- **Homebrew ghostty build (Linux only)**: `brew install gaurav-gosain/tap/tuios-ghostty`
- **Arch Linux (AUR)**: `yay -S tuios-bin`
- **Nix**:  
  - Specific release: `nix run github:Gaurav-Gosain/tuios/v0.8.5#tuios`  
  - Latest main: `nix run github:Gaurav-Gosain/tuios#tuios`  
  - Nixpkgs package: `nix run nixpkgs#tuios`

### Other Methods
- Quick install script: `curl -fsSL https://raw.githubusercontent.com/Gaurav-Gosain/tuios/main/install.sh | bash`
- Go install: `go install github.com/Gaurav-Gosain/tuios/cmd/tuios@latest`
- Docker: `docker run -it --rm ghcr.io/gaurav-gosain/tuios:latest`
- Pre‑built binaries for Linux, macOS, Windows, FreeBSD, OpenBSD available via GitHub Releases.
- Building from source requires Go 1.26.6 or newer.

## Core Features
- **Multiple Terminal Panes**: Create, resize, drag, and organize sessions.
- **9 Workspaces**: Independent isolation with instant switching.
- **Modal Interface**: Vim‑inspired window and terminal modes.
- **Command Palette**: Fuzzy‑searchable action launcher (Ctrl+P).
- **Launcher**: Fuzzy search of `$PATH` and desktop apps (Alt+Space) with kitty graphics icons.
- **Pane Zoom**: Zoom any pane (`z` in WM mode or `Prefix+z`), configurable to fullscreen.
- **Session Rail**: Sidebar showing sessions, terminals, files, git state, and agents.
- **Settings Page**: Adjust options within the app (`Prefix+,`).
- **Pop‑up Floating Panes**: Run commands in temporary panes that close on exit.

## Agent System
- Detects 24 agent CLIs; displays state (working, waiting, done, errored) in pane titles and the rail.
- **Inbox** (`Prefix+i`): Central view of approvals, questions, mail, errors, and completed turns across all sessions and machines.
- **Agent Communication**:  
  - `tuios send-agent-message` for inter‑agent mail.  
  - `tuios ask-agent` to pose a question and wait for a response.
- **Fleets**: Launch a single prompt across multiple agents, each in its own git worktree.
- **Resume**: After daemon restart, the Inbox offers to resume each active agent conversation.
- **Pane Grants**: Define permissions for an agent’s pane (read, write, fan, respond, admin).
- **MCP Server**: Provides read‑only access to the same surface as MCP tools, scoped to the agent’s session unless overridden.
- **tmux Shim**: Runs tools that drive tmux (e.g., Claude Code agent teams) with panes opened as TUIOS panes.
- **Session Stash**: `tuios stash put` stores a file for the session, accessible to other agents.
- **Skill Guides**: `tuios --skill` prints short usage guides for agents; `tuios --skill TOPIC` shows detailed recipes.

## Multi‑Machine Support
- **Hosts**: Add remote machines (`tuios hosts add <name>`) to reach sessions on other devices.
- **Sessions**: Daemon mode allows attaching/detaching sessions across machines; persistent state survives restarts.

## Architecture & Performance
- Built on the Charm stack: Bubble Tea v2 and Lipgloss v2.
- Event‑driven rendering yields near‑zero idle CPU usage.
- Flicker‑free kitty image passthrough.
- Detailed technical design documented in the Architecture section.

## Development
- Repository includes client tests, end‑to‑end tests, examples, integrations, internal packages, skill definitions, and scripts.
- CI/CD handled by Goreleaser and GitHub Actions.
- Contribution guidelines provided in the docs.

## License
- Distributed under the MIT License.