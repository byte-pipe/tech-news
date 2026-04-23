---
title: GitHub - huggingface/ml-intern: 🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models · GitHub
url: https://github.com/huggingface/ml-intern
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-04-24T06:02:14.279803
---

# GitHub - huggingface/ml-intern: 🤗 ml-intern: an open-source ML engineer that reads papers, trains models, and ships ML models · GitHub

# ml-intern

## Overview
- Open‑source “ML intern” that autonomously researches, writes, and ships ML code using the Hugging Face ecosystem.  
- Provides deep access to Hugging Face docs, papers, datasets, and cloud compute.

## Quick Start
- Clone the repository and install dependencies:  
  ```bash
  git clone git@github.com:huggingface/ml-intern.git
  cd ml-intern
  uv sync
  uv tool install -e .
  ```
- Run the CLI from any directory with `ml-intern`.
- Create a `.env` file (or export) with the required keys:  
  - `ANTHROPIC_API_KEY` – for Anthropic models (optional).  
  - `HF_TOKEN` – Hugging Face token (prompted on first launch if missing).  
  - `GITHUB_TOKEN` – personal access token for GitHub operations.

## Usage
- Interactive mode (chat session): `ml-intern`  
- Headless mode (single prompt, auto‑approve): `ml-intern "fine‑tune llama on my dataset"`  
- Optional flags:  
  - `--model <model_name>` to select a different LLM.  
  - `--max-iterations <n>` to change the iteration limit.  
  - `--no-stream` to disable token streaming.

## Architecture
- **CLI → submission loop → handlers → agentic loop** (max 300 iterations).  
- Core components:  
  - **ContextManager** – stores message history, performs auto‑compaction, uploads session to Hugging Face.  
  - **ToolRouter** – interfaces with HF docs, repos, datasets, jobs, papers, GitHub code search, sandbox tools, planning, and MCP server tools.  
  - **Doom Loop Detector** – detects repeated tool patterns and injects corrective prompts.  
- Loop flow: LLM call → parse `tool_calls` → approval check → execute via ToolRouter → add results to ContextManager → repeat if needed.

## Agentic Loop Flow
1. User message added to ContextManager.  
2. Iteration loop (up to 300):  
   - Generate LLM response (`litellm.acompletion`).  
   - If `tool_calls` present, add assistant message with calls.  
   - Run doom‑loop check.  
   - For each tool call: request approval if required, execute tool, add output to context.  
   - Continue loop until no tool calls or iteration limit reached.

## Events Emitted
- `processing`, `ready`, `assistant_chunk`, `assistant_message`, `assistant_stream_end`  
- `tool_call`, `tool_output`, `tool_log`, `tool_state_change`  
- `approval_required`, `turn_complete`, `error`, `interrupted`  
- `compacted`, `undo_complete`, `shutdown`

## Extending the Project
- **Add built‑in tools**: modify `agent/core/tools.py` and define new `ToolSpec` entries with name, description, parameters, and async handler.  
- **Add MCP servers**: edit `configs/main_agent_config.json`; environment variables in the config are auto‑substituted from `.env`.

## Repository Statistics
- Stars: 2.9 k  
- Forks: 259  
- Watchers: 20  
- Primary languages: Python (~70 %), TypeScript (~30 %).  

## Resources
- Detailed documentation and installation steps are available in the repository’s README.