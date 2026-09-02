---
title: GitHub - pacifio/atlas: Source control for agents. Use multiple coding agents, track their changes and query them in one place · GitHub
url: https://github.com/pacifio/atlas
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-03T07:21:49.423547
---

# GitHub - pacifio/atlas: Source control for agents. Use multiple coding agents, track their changes and query them in one place · GitHub

# Atlas – Source control for coding agents

## Why Atlas
- Records both code changes and the reasoning behind them, making everything queryable.  
- Persists on‑device memory of decisions, plans, and changes across sessions.  
- Allows seamless switching between agents without losing context.  
- Stores sessions searchable alongside a real commit graph and file‑level diffs.  
- Uses open formats (markdown, JSON) for notes; only the checkpoint index is stored in SQLite.  
- Built from the ground up for agent‑centric workflows.

## How it works
- Runs agents (Claude Code, Codex, Atlas’s native agent, or any ACP registry agent) as subprocesses or in‑process.  
- Before each prompt, Atlas injects context: source, timestamps, `@`‑mentions, resolved files/folders, notes, skills, papers, and past sessions.  
- Shared memory contains the active plan, decisions, file changes, failures, and architecture notes, readable by all agents.  
- On‑device semantic embeddings and HNSW search match messages to the project’s memory index.  
- Session handoff provides a curated fact pack and the tail of the previous session, even when the new session uses a different agent.  
- All agents follow the same send path; no per‑agent special‑casing is required.

## Checkpoints
- A checkpoint links a commit to the session that produced it, storing prompts, tool calls, and reasoning.  
- Sessions are saved in `.atlas/sessions.db` with secrets scrubbed before writing to disk.  
- Checkpoints survive rebases and amends; you can select a checkpoint and chat with it to retrieve its context.  
- Works fully offline; no account is needed.

## Features

### Agents
- **Multi‑agent sessions** – Claude Code, Codex, and Atlas’s native agent run in parallel; sessions are independent of tabs.  
- **Shared agent memory** – on‑device semantic index (local embeddings, HNSW search) that every agent reads from and writes to.  
- **`@` mentions** – local resolution of files, folders, symbols, branches, commits, notes, skills, papers, and past sessions.  
- **Skills** – `SKILL.md` files scoped globally or per project, enabled per agent by symlinking into the agent’s skills directory.  
- **Packs** – install a GitHub repo of skills, sub‑agents, commands, hooks, rules, and scripts via the `skills.sh` index.  
- **Model chat** – talk to a model directly in its own tab.

## Additional information
- **Local by default** – code, notes, and sessions stay on the machine; optional sign‑in creates an organization for team sync.  
- Community and support are available on Discord (general chat, dev‑build, feature‑requests, bugs).  
- Contribution guidelines, issue tracker, architecture docs, security policy, telemetry details, and build scripts are included in the repository.