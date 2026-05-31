---
title: GitHub - nicobailon/pi-subagents: Pi extension for async subagent delegation with truncation, artifacts, and session sharing · GitHub
url: https://github.com/nicobailon/pi-subagents
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-01T04:19:49.408390
---

# GitHub - nicobailon/pi-subagents: Pi extension for async subagent delegation with truncation, artifacts, and session sharing · GitHub

# pi‑subagents – Pi extension for async sub‑agent delegation

## Overview
- Enables Pi to delegate tasks to focused child agents (subagents) for activities such as code review, scouting, implementation, parallel audits, background jobs, etc.  
- Subagents run either in the foreground (streamed in the conversation) or in the background (continue after control returns).  

## Installation & Quick Start
- Install with `pi install npm:pi-subagents`.  
- No configuration needed to begin; simply ask Pi in natural language, e.g., “Use reviewer to review this diff.”  

## Core Concepts
- **Parent session**: the main Pi chat.  
- **Subagent**: a child Pi session with its own job and model (inherits Pi’s default model unless overridden).  
- **Foreground run**: streams results directly in the chat.  
- **Background run**: continues asynchronously; status can be queried later.  

## Built‑in Subagents (plain‑English purpose)
- **scout** – fast local codebase reconnaissance.  
- **researcher** – web/docs research with sources.  
- **planner** – creates concrete implementation plans (read‑only).  
- **worker** – performs implementation, edits files, validates, escalates unapproved decisions.  
- **reviewer** – code review, small fixes, checks against task/plan, tests, edge cases.  
- **context‑builder** – gathers extensive context, produces handoff files.  
- **oracle** – second‑opinion, challenges assumptions, recommends safe next steps.  
- **delegate** – lightweight general delegate behaving like the parent session.  

## Typical Prompts & Workflows
- Get a second opinion: “Ask oracle for a second opinion on my current plan.”  
- Solve a bug: “Use oracle to investigate this bug before we edit.”  
- Review a diff: “Use reviewer to review this diff.”  
- Parallel reviewers: “Run reviewers for correctness, tests, and cleanup.”  
- Implement‑then‑review loop: “Implement this, then review it.”  
- Review until clean: “Run a review loop on this change with a max of 3 rounds.”  
- Scout before planning: “Use scout to inspect the auth flow before planning.”  
- Background execution: “Run this in the background.”  

## Model Overrides
- Override a built‑in agent’s model for a single run:  
  `/run reviewer[model=anthropic/claude-sonnet-4:high] "Review this diff"`  
- Persistent overrides are stored in `~/.pi/agent/settings.json` (user) or `.pi/settings.json` (project) under `subagents.agentOverrides`.  

## Monitoring Subagents
- Foreground runs stream progress; background runs appear as async widgets and send notifications.  
- Query status: `subagent({ action: "status" })` or `subagent({ action: "status", id: "…" })`.  
- List active runs naturally: “Show me the current async runs.”  
- Diagnose configuration: `/subagents-doctor` or “Check whether subagents and intercom are set up correctly.”  

## Recommended Orchestration Pattern
1. Clarify  
2. Planner → Worker → Fresh Reviewers → Worker  

- Use shortcut prompts for repeatable patterns.  
- Child safety boundaries are enforced; child sessions do not inherit bundled `pi-subagents` unless explicitly allowed.