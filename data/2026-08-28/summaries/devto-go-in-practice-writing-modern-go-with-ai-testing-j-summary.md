---
title: [Go in Practice] Writing Modern Go with AI: Testing JetBrains go-modern-guidelines and Refactoring a 1,039-line main.go - DEV Community
url: https://dev.to/gde/go-in-practice-writing-modern-go-with-ai-testing-jetbrains-go-modern-guidelines-and-refactoring-151o
date: 2026-08-27
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-28T17:07:40.274992
---

# [Go in Practice] Writing Modern Go with AI: Testing JetBrains go-modern-guidelines and Refactoring a 1,039-line main.go - DEV Community

# Summary of “[Go in Practice] Writing Modern Go with AI: Testing JetBrains go-modern-guidelines and Refactoring a 1,039‑line main.go”

## Background
- AI code generators often produce outdated Go because model training data has a cutoff date and exhibits frequency bias toward older patterns.  
- JetBrains go‑modern‑guidelines is a plugin that teaches AI agents the latest Go syntax and idioms.

## What is go‑modern‑guidelines?

### The problem it aims to solve
- **Knowledge cutoff**: Models cannot use standard‑library features added after their training data (e.g., `errors.AsType[T]` introduced in Go 1.26).  
- **Frequency bias**: Even when a model “knows” a newer construct, older forms appear far more often in the data, so the model prefers them (e.g., manual substring search instead of `strings.Contains`).

### How it works
- Provides a CLI with two subcommands:  
  - `list [--go-version <ver> | --file-path <path>]` – returns a version‑specific list of guidelines, newest to oldest.  
  - `explain <id>…` – gives detailed explanations, before/after code examples, and important caveats.  
- `list` adapts to the Go version detected from `go.mod`, `go.work`, or the local toolchain, ensuring only applicable guidelines are suggested.  
- Example guideline (`cmp_or`): shows concise usage, notes that all arguments are evaluated before the call, and provides a before/after transformation.

### Two‑layer information design
- **Layer 1 (list)**: One‑line summaries for all applicable guidelines (~1000 tokens for 45 items).  
- **Layer 2 (explain)**: Detailed info fetched only for the few guidelines relevant to the current code, conserving the AI’s context window.  
- Workflow:  
  1. Run `list` on the target file.  
  2. Identify relevant guidelines.  
  3. Call `explain` for those IDs.  
  4. Apply the suggested changes.  

### Pitfalls
- Do not pipe the raw output of `list` through tools like `head`, `tail`, or `grep`, as this may omit important guidelines.

## Installation
- For Claude Code:  
  ```
  /plugin marketplace add JetBrains/go-modern-guidelines
  /plugin install modern-go-guidelines@goland-claude-marketplace
  ```  
- The plugin auto‑triggers on Go‑related tasks; manual invocation is possible via `/modern-go-guidelines:use-modern-go`.  
- Other agents (Cursor, Junie, Codex) have analogous installation steps; the CLI is cached locally on first run.

## Project case study: a 1,039‑line `main.go`
- The examined repository (`linebot-file`) implements a LINE messaging bot with the following components:  
  - **LINE App** → receives files via webhook.  
  - **Cloud Run** → hosts the webhook endpoint.  
  - **Firestore** → stores user tokens after OAuth2 authorization (`/connect_drive`).  
  - **Google Drive API** → uploads and queries files.  
- The original code contained many outdated patterns (e.g., manual string scanning) that were refactored using the guidelines provided by `go‑modern‑guidelines`.  

---  
*The summary captures the article’s main ideas, the functionality and design of the `go-modern-guidelines` tool, its installation process, and the context of the refactoring case study.*