---
title: GitHub - alphaXiv/OpenResearch: Run parallel research agents with any model · GitHub
url: https://github.com/alphaXiv/OpenResearch
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-12T01:23:12.017541
---

# GitHub - alphaXiv/OpenResearch: Run parallel research agents with any model · GitHub

# OpenResearch – Local‑first Workspace for Research Agents

## Overview
- Repository for OpenResearch, a platform that turns Claude Code, Codex, or OpenCode into autonomous research agents.
- Enables literature review, hypothesis generation, experiment execution, and artifact creation.
- Provides a desktop app, CLI, and documentation for macOS, Linux, and Windows (beta).

## Getting Started
- **Desktop app:** download from `openresearch.sh/download`.
- **CLI installation (macOS/Linux):**  
  ```bash
  curl -LsSf https://openresearch.sh/install.sh | sh
  orx up
  ```
- **Windows:** install from the Releases page (requires Git for Windows).
- Open the local dashboard at `http://127.0.0.1:4791`.
- Connect local models (LM Studio, Ollama, etc.) via the “connecting local models” guide.
- Create an account at `openresearch.sh` for email updates and managed compute.

## Core Features
- **Parallel exploration:** each research direction runs in an isolated agent session with its own git worktree.
- **Reproducible experiments:** every run is archived as an immutable git commit within an experiment tree.
- **Evidence in context:** logs, diffs, files, results, and artifacts are linked to the generating work.
- **Agent flexibility:** choose Claude Code, Codex, or OpenCode per session.
- **Compute flexibility:** run locally, on personal infrastructure, or via managed OpenResearch compute.
- **Local ownership:** all projects, conversations, runs, logs, code, and artifacts stay on the user’s machine.

## Autoresearch Loop
- The platform can autonomously:
  1. Propose ideas.
  2. Modify code.
  3. Launch experiments.
  4. Inspect evidence.
  5. Decide the next step.
- Multiple agents can explore different directions simultaneously, with lineage preserved in the experiment tree.

## Run Anywhere
- The same committed source snapshot can be executed:
  - Locally.
  - Over SSH.
  - On Slurm, Kubernetes, Ray, Hugging Face Jobs, Modal, Tinker, or managed OpenResearch compute.
- No need to publish the repository.
- Example remote launch: `orx up --remote user@host`.
- Supports SSH config aliases and custom ports; remote service binds to loopback without application‑level authentication.

## CLI and Agent Integration
- Install the OpenResearch skill for supported coding agents: `orx install-skills`.
- Common commands:
  - `orx projects` – list projects.
  - `orx project view <project-id>` – view a project.
  - `orx runs <project-id>` – list runs.
  - `orx logs <run-id>` – view logs.
  - `orx exp run <experiment-id>` – execute an experiment.
  - `orx discover <keyword> <query>` – discover resources.
  - `orx paper <arxiv-id-or-doi>` – fetch a paper.
  - `orx --help` or `orx <command> --help` – full help.

## Local‑by‑Default Operation
- Runs on `127.0.0.1` with a local SQLite store.
- Creating projects or runs does not publish code.
- An OpenResearch account is only required for organization management and managed compute services.

## Usage Analytics
- Official release builds send optional, coarse usage events tied to a random installation ID.
- No code, prompts, file contents, paths, repository names, tokens, emails, or project identifiers are transmitted.
- Telemetry can be disabled: `orx telemetry off` or `orx <command> --no-telemetry`.
- Source and development builds do not send any analytics.