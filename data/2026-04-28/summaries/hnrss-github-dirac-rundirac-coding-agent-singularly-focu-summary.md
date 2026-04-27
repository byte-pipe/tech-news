---
title: GitHub - dirac-run/dirac: Coding Agent singularly focused efficiency and context curation. Reduces API costs by 50-80% vs other agent AND improves the...
url: https://github.com/dirac-run/dirac
date: 2026-04-27
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-28T06:04:51.871390
---

# GitHub - dirac-run/dirac: Coding Agent singularly focused efficiency and context curation. Reduces API costs by 50-80% vs other agent AND improves the...

# Dirac – Accurate & Highly Token Efficient Open Source AI Coding Agent

## Overview
- Open‑source coding agent focused on efficiency and context curation.  
- Reduces API costs by roughly 50‑80 % (average 64.8 % cheaper) while improving code quality and speed.  
- Achieved top score on the Terminal‑Bench‑2 leaderboard (65.2 % with gemini‑3‑flash‑preview).

## Evaluation Results
- Benchmarked on real‑world refactoring tasks across multiple public repositories.  
- Consistently 100 % accuracy on evaluated tasks.  
- Cost per task significantly lower than competing agents (average $0.18 vs $0.49‑$0.87 for others).

## Key Features
- Hash‑Anchored Edits – stable line‑hash targeting for precise modifications.  
- AST‑Native Manipulation – language‑aware edits (TypeScript, Python, C++, etc.) with structural accuracy.  
- Multi‑File Batching – edit many files in a single LLM round‑trip, cutting latency and token usage.  
- High‑Bandwidth Context Curation – keeps only the most relevant information in the prompt.  
- Autonomous Tool Use – file I/O, terminal commands, headless browser, all under an approval‑based workflow.  
- Skills & AGENTS.md – project‑specific instructions and automatic skill import from Claude directories.  
- Native Tool Calling Only – supports models with built‑in tool calling; MCP not supported.

## Installation
- VS Code Extension – install from the VS Code Marketplace.  
- CLI – `npm install -g dirac-cli`.

## Quick‑Start Commands
1. Authenticate: `dirac auth`.  
2. Run a task: `dirac "Analyze the architecture of this project"`.  
3. Optional flags:  
   - `-p` for plan‑mode preview.  
   - `-y` for auto‑approve (YOLO) mode.  
   - Pipe diffs: `git diff | dirac "Review these changes"`.  
   - View history: `dirac history`.

## Configuration
- API keys can be supplied via environment variables (Anthropic, OpenAI, Gemini, etc.) for CI/CD or non‑interactive use.

## License & Acknowledgments
- Licensed under the Apache License 2.0.  
- Forked from the Cline project; thanks to the Cline team and contributors.  
- Developed by Max Trivedi at Dirac Delta Labs.