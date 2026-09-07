---
title: GitHub - advaitpaliwal/feynman: The open source AI research agent. · GitHub
url: https://github.com/advaitpaliwal/feynman
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-08T00:32:14.406839
---

# GitHub - advaitpaliwal/feynman: The open source AI research agent. · GitHub

# Feynman – Open‑source AI research agent

## Overview
- An AI‑driven research assistant that can search literature, perform multi‑agent investigations, rank papers, fetch full texts, audit claims, replicate experiments, and host a web‑based science workbench.  
- Repository contains source code, assets, tests, documentation, and a reusable skill library.

## Installation
- **Standalone installer (macOS / Linux)**  
  `curl -fsSL https://feynman.is/install | bash`  
- **Windows PowerShell**  
  `irm https://feynman.is/install.ps1 | iex`  
- Installer downloads the latest tagged release, bundles a pinned Node.js runtime, verifies SHA‑256, and can be pinned to a specific version (e.g., `... | bash -s -- 0.2.35`).  
- **npm package**  
  `npm install -g @advaitpaliwal/feynman` – update with `npm install -g @advaitpaliwal/feynman@latest`.  
- Migration from the old scoped package (`@companion-ai/feynman`) is documented.  
- **Skill‑only installers** add the research skill library to Codex, a repo‑local Claude/agent setup, or an OpenCode project without installing the full terminal app.

## Model configuration
- Supports local models via LM Studio, LiteLLM, Ollama, or vLLM (choose provider during `feynman setup`).  
- Hosted providers authenticated with `feynman model login <provider>`; OpenRouter can use OAuth or an `OPENROUTER_API_KEY` environment variable.

## Core commands
- `feynman "what do we know about scaling laws"` – searches papers/web and returns a cited research brief.  
- `feynman deepresearch "mechanistic interpretability"` – launches parallel agents, synthesis, and verification.  
- `feynman lit "RLHF alternatives"` – produces a literature review with consensus, disagreements, and open questions.  
- `feynman rank "<topic>"` – scores papers to decide reading order; options:  
  - `--expand-citations 2` – adds cited and citing papers to the citation graph.  
  - `--full-text-top 3` – incorporates section‑aware full‑text evidence.  
  - `--critique-top 5` – adds strengths, concerns, and follow‑up questions.  
  - `--synthesize` – writes an auditable model synthesis.  
- `feynman paper 10.7717/peerj.4375 --fetch-full-text` – resolves legal access and downloads the paper text.  
- `feynman serve` – opens the standalone science workbench with projects, chat, notebooks, compute, artifact previews, provenance, settings, and skills.  
- `feynman serve --no-auth` – runs the workbench locally without authentication.  
- `feynman audit 2401.12345` – compares paper claims against the public codebase.  
- `feynman replicate "chain-of-thought improves math"` – plans and runs replication checks after explicit environment selection.  
- `feynman recipe "fine-tune a small model for math reasoning"` – finds ranked, implementable ML training recipes from papers, datasets, docs, and code.

## Workflows (slash commands)
- `feynman rank <topic>` – PaperRank scoring with transparent evidence for citations, methods, reproducibility, and provenance.  
- `feynman paper <id-or-title>` – Resolves access for DOI, arXiv, OpenAlex, PMID, PMCID, or title and optionally fetches full text.  
- Additional commands follow a natural‑language pattern, allowing users to ask questions or invoke specific research actions directly.

## Repository structure (high‑level)
- Directories: `src`, `tests`, `skills`, `prompts`, `papers`, `website`, `workbench-web`, `assets`, `experiments`, etc.  
- Key documentation files: `README.md`, `AGENTS.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `LICENSE`.  
- Metadata, fixtures, and scripts support development and testing.

## Maintenance
- 492 commits, 1 000 forks, 8.9 k stars.  
- Release notes and changelog track updates.  
- Contribution guidelines encourage community involvement.