---
title: "GitHub - michael-denyer/pstack-claude: Claude Code, Codex, Pi, OpenCode, Gemini, and Prime Agent versions of Poteto's pstack. Rigorous agent workflows..."
url: https://github.com/michael-denyer/pstack-claude
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-10-05T12:21:22.594995
---

# GitHub - michael-denyer/pstack-claude: Claude Code, Codex, Pi, OpenCode, Gemini, and Prime Agent versions of Poteto's pstack. Rigorous agent workflows...

# Summary of pstack‑claude Repository

## Overview
- pstack‑claude is a port of Lauren Tan’s **pstack** skill stack for Claude Code, Codex, Pi, OpenCode, Gemini, and Prime Agent.
- Provides opinionated Cursor skill workflows that improve agent outcomes and support named policy forks via `tools/forks.json`.
- Includes additional plugins for formal verification (TLA+ model checking and Lean proofs).

## Installation
- **Claude Code**:  
  `/plugin marketplace add michael-denyer/pstack-claude`  
  `/plugin install pstack@pstack-claude`
- **Codex**:  
  `codex plugin marketplace add michael-denyer/pstack-claude`  
  `codex plugin add pstack@pstack-claude`
- **Pi**:  
  `pi install git:github.com/michael-denyer/pstack-claude`
- Supports Prime Agent, OpenCode, Gemini CLI, and skills‑only installs (see shared installation docs).

## Getting Started
- Activate `poteto-mode` to invoke the appropriate workflow for a given task.
- Example workflow: reproduces a bug, runs `showandwhy` for investigation, delegates fix, reruns failing case, and provides evidence of success.
- Additional playbooks cover planning, refactoring, performance, investigations, prototypes, PR maintenance, shipping, and long‑term projects.

## Core Features
- **Skills and slash commands** for concise interaction.
- **Runtime setup** with configurable model defaults and reasoning effort per role (e.g., `arena runners: opus @xhigh`).
- **Routing instruction** installed automatically on Claude Code, Codex, and Pi.
- **No server or telemetry**: all data stays local; scripts run on the user’s machine; GitHub CLI used for PR tools.

## Contribution Guidelines
- Contributions welcome: bug reports, documentation fixes, runtime improvements.
- Follow checks and file placement described in `CONTRIBUTING.md`.
- Report security issues privately as outlined in `SECURITY.md`.

## Licensing
- MIT‑licensed (© 2026 Michael Denyer) with original pstack © 2026 Lauren Tan and imported cursor‑team‑kit skills © 2026 Cursor.
- See `LICENSE-cursor-team-kit` and `NOTICE.md` for full details.