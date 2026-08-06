---
title: Prime Agent: A self-improving RLM agent
url: https://www.primeintellect.ai/blog/prime-agent
date: 2026-08-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-07T06:01:40.052443
---

# Prime Agent: A self-improving RLM agent

# Prime Agent: A self-improving RLM agent

## Overview
- Launches a self‑improving coding harness built on two abstractions: Recursive Language Model (RLM) and Continual Harness.  
- Aims to move beyond static, hand‑engineered tool‑calling schemas by letting the model manipulate its own context, prompts, skills, memory, and sub‑agents dynamically.  
- Targets use cases such as a general coding assistant, long‑horizon autonomous evaluation, and research collaboration.  
- Fully open‑source; installable via a single curl‑pipe‑sh command.

## Core Abstractions
- **Recursive Language Model (RLM)**
  - Treats context as a mutable variable.
  - Enables sub‑agent delegation as function calls inside a persistent REPL.
  - Provides programmatic access to history, tools, and variables, allowing arbitrarily long sessions without losing past information.
- **Continual Harness**
  - Represents the harness’s state (prompts, skills, memory, sub‑agents) as CRUD‑able resources.
  - Allows the agent to create, read, update, and delete these resources during its trajectory.
  - Supports orchestration across sub‑agents and across separate Prime Agent sessions via agent‑to‑agent communication.

## Architecture
- **Persistent IPython Kernel**
  - Serves as the sole tool; all other harness features are exposed as kernel functions.
- **Background Daemon**
  - Owns all live agent sessions over a local socket.
  - Enables attach/detach without stopping the underlying agent loop.
  - Recovers crashed workers from JSONL session logs and kernel snapshots.
- **Agents View (TUI)**
  - Accessible via left‑arrow on an empty prompt.
  - Lists running, idle, and inactive sessions; allows immediate interaction, steering, and command queuing.
  - Provides recursive navigation into sub‑agents, with automatic memory unloading after 30 minutes of inactivity.
- **Session & Context Management**
  - Append‑only JSONL files store full session history, supporting branching, forking, and cloning.
  - Compaction runs automatically when context thresholds are hit or manually via `compact.run()`.
  - Asynchronous garbage‑collector agent cleans the REPL state to prevent memory bloat.

## Programmatic Tool‑Calling (PTC) with RLM
- `rlm()` is an asynchronous function that spawns a full sub‑agent session (model, kernel, history) and returns a handle immediately.
- Sub‑agents communicate back to the parent via `agent_message.send(...)`.
- Enables parallel fan‑out patterns:
  - Example: launch `auth-expert` and `http-expert` sub‑agents simultaneously, then steer them mid‑flight with targeted messages.
- Future model generations are expected to rely more on such direct programmatic control rather than static prompts.

## Orchestration & Multi‑Agent Communication
- The daemon mediates Agent‑to‑Agent (A2A) messaging, allowing any Prime Agent session to message any other session using the same mechanism as persistent sub‑agents.
- Facilitates coordination of sub‑agent swarms, sharing of resources, and cross‑session collaboration.

## Installation
```bash
curl -fsSL https://app.primeintellect.ai/prime-agent/install.sh | sh
```