---
title: "GitHub - alibaba/open-code-review: Battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precis..."
url: https://github.com/alibaba/open-code-review
date: 2026-06-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-06T11:51:59.623456
---

# GitHub - alibaba/open-code-review: Battle-tested at Alibaba's scale. Hybrid architecture code review tool: deterministic pipelines + LLM Agent, precis...

# Open Code Review – Alibaba’s AI‑Powered Code Review Tool

## What is Open Code Review?
- An AI‑driven CLI tool that reads Git diffs, sends changed files to a configurable LLM, and produces line‑level structured review comments.  
- Originated as Alibaba Group’s internal AI code review assistant; after two years of production use it has helped tens of thousands of developers and found millions of defects.  
- Open‑sourced for the community; works with any LLM endpoint compatible with OpenAI or Anthropic APIs.

## Why It Was Created
- **Limitations of general‑purpose agents** (e.g., Claude Code):
  - Incomplete coverage on large change sets.
  - Position drift: comments often point to wrong lines or files.
  - Unstable quality due to prompt sensitivity.
- These issues stem from a purely language‑driven architecture that lacks hard constraints.

## Core Design: Deterministic Engineering × Agent Hybrid
### Deterministic Engineering (hard constraints)
- Precise file selection to ensure no important change is missed.  
- Smart bundling of related files (e.g., locale property files) into isolated sub‑agents for stable, concurrent processing.  
- Fine‑grained rule matching per file, using template‑engine‑based rules for predictable behavior.  
- External positioning and reflection modules that improve comment location and content accuracy.

### Agent (dynamic decision‑making)
- Scenario‑tuned prompts that reduce token usage while enhancing effectiveness.  
- Scenario‑tuned toolset derived from large‑scale production data, offering a stable, purpose‑built toolkit for code review.

## How to Use

### Installation
- **NPM (recommended)**: `npm install -g @alibaba-group/open-code-review` (provides global `ocr` command).  
- **Pre‑built binaries**: Download from GitHub Releases for macOS (Apple Silicon, Intel), Linux (x86_64, ARM64), or Windows (x86_64, ARM64) and place in a directory on your `PATH`.  
- **From source**: Clone repo, run `make build`, then copy the binary to `/usr/local/bin/ocr`.

### Quick Start
1. **Configure LLM**  
   - Interactive: `ocr config set llm.url <url>` etc.  
   - Environment variables (highest priority): `OCR_LLM_URL`, `OCR_LLM_TOKEN`, `OCR_LLM_MODEL`, `OCR_USE_ANTHROPIC`.  
   - Config stored at `~/.opencodereview/config.json`.  
   - Supports Claude Code env vars and CC‑Switch proxy settings.

2. **Test connectivity**: `ocr llm test`.

3. **Run review**  
   - Workspace mode (all changes): `ocr review`.  
   - Branch range: `ocr review --from main --to feature-branch`.  
   - Single commit: `ocr review --commit abc123`.

### Integration with Coding Agents
- **Skill installation**: `npx skills add alibaba/open-code-review --skill open-code-review` to let AI coding agents invoke `ocr` as a slash command, classify issues, and optionally apply fixes.  
- **Claude Code plugin**: Install the command plugin (details omitted in snippet) for direct use within Claude Code.

## Repository Overview
- Public repo with 2.8 k stars, 132 forks.  
- Contains source code, examples, plugins, skills, documentation in English and Simplified Chinese.  
- License: Apache‑2.0.