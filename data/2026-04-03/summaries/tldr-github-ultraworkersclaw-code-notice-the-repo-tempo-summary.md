---
title: GitHub - ultraworkers/claw-code: [Notice] The repo temporarily locked while ownership transfer. in the meantime we maintain on here: https://github.co...
url: https://github.com/instructkr/claw-code
date: 2026-04-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-03T01:02:12.374061
---

# GitHub - ultraworkers/claw-code: [Notice] The repo temporarily locked while ownership transfer. in the meantime we maintain on here: https://github.co...

# Summary of ultraworkers/claw-code repository

## Overview
- Public repository originally hosting leaked Claw Code, now maintained at https://github.com/ultraworkers/claw-code-parity.
- Achieved record growth: fastest repo to reach 50 K stars in 2 hours, now over 100 K stars.
- Focus shifted to a clean‑room Python rewrite and a Rust implementation for a memory‑safe harness runtime.

## Rust Port
- Workspace located in `rust/` with multiple crates:
  - `api-client` – API client with provider abstraction, OAuth, streaming.
  - `runtime` – session state, compaction, MCP orchestration, prompt construction.
  - `tools` – tool manifest definitions and execution framework.
  - `commands` – slash commands, skills discovery, config inspection.
  - `plugins` – plugin model, hook pipeline, bundled plugins.
  - `compat-harness` – compatibility layer for upstream editor integration.
  - `claw-cli` – interactive REPL, markdown rendering, project bootstrap/init flows.
- Build with `cargo build --release`.
- Intended as the definitive, faster version; merge to `main` expected soon.

## Backstory
- On 31 Mar 2026 the original Claw Code source leaked, causing a community frenzy.
- Author ported core features to Python overnight using the `oh‑my‑codex` (OmX) workflow, collaborating with OmX creator @bellman_ych.
- Rust port also driven by OmX and `oh‑my‑opencode` (OmO).

## Media Coverage
- Wall Street Journal article (21 Mar 2026) highlighted the author’s extensive use of Claw Code and its community.
- Notable users: AI startup worker Sigrid Jin, a Belgian cardiologist, and a California lawyer.

## Porting Status
- Primary source tree is now Python‑first (`src/`).
- Tests verify the Python workspace; the snapshot of the leaked code is no longer tracked.
- Python version is not yet a full runtime replacement but covers the main implementation surface.

## Reason for Rewrite
- Legal and ethical concerns about hosting the exposed code.
- Aim to provide an open‑source, clean‑room implementation.

## Repository Layout
- `src/` – Python port (modules, commands, tools, etc.).
- `rust/` – Rust port with multiple crates.
- `tests/` – Python verification suite.
- `assets/omx/` – OmX workflow screenshots.
- Additional docs and markdown files (`README.md`, `CLAW.md`, `PARITY.md`, etc.).

## Python Workspace Overview
- `port_manifest.py` – summarizes workspace structure.
- `models.py` – dataclasses for subsystems and state.
- `commands.py`, `tools.py` – metadata for commands and tools.
- `query_engine.py` – renders a summary from the active workspace.
- `main.py` – CLI entry point for manifest and summary output.

## Quickstart Commands
- `python3 -m src.main summary` – render porting summary.
- `python3 -m src.main manifest` – show workspace manifest.
- `python3 -m src.main subsystems --limit 16` – list current Python modules.
- `python3 -m unittest discover -s tests -v` – run verification tests.
- `python3 -m src.main parity-audit` – audit parity with the local ignored archive.
- `python3 -m src.main commands --limit 10` and `tools --limit 10` – inspect command/tool inventories.

## Current Parity Checkpoint
- Python port mirrors top‑level files, subsystem names, and command/tool inventories closely.
- Still missing many executable runtime slices compared to the original TypeScript system.

## Tooling Used
- Porting and verification driven by Yeachan Heo’s stack: `oh‑my‑codex` (OmX) for scaffolding and `oh‑my‑opencode` (OmO) for implementation acceleration and verification.
