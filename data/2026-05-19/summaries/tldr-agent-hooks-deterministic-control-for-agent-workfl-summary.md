---
title: Agent Hooks: Deterministic Control for Agent Workflows
url: https://nader.substack.com/p/agent-hooks-deterministic-control
date: 2026-05-19
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-19T06:02:47.387965
---

# Agent Hooks: Deterministic Control for Agent Workflows

# Agent Hooks: Deterministic Control for Agent Workflows

## Overview
- Hooks attach user‑defined handlers to specific lifecycle events in an agent session.  
- They move policy checks, tests, and runbook steps out of model memory into explicit control points, providing deterministic behavior.  
- Prompts guide the model; hooks enforce rules that must run every time.

## Core Lifecycle Hooks
- **SessionStart** – Load session context such as project conventions, active constraints, environment facts, or relevant runbooks.  
- **UserPromptSubmit** – Inspect the user prompt before the model sees it; add context, route the request, or block known‑bad prompts.  
- **PreToolUse** – Examine a tool call before execution; block, approve, or modify behavior based on policy.  
- **PostToolUse** – Validate after a successful tool call (run tests, formatting, scanning, logging, state capture).  
- **Stop** – Decide whether the agent may finish the current turn.  
- **SessionEnd** – Write final logs, flush metrics, export a summary, or clean up temporary state.

## Operating Model
- **Event → optional matcher/filter → handler → outcome**  
  - *Event*: a lifecycle moment (e.g., `PreToolUse`, `Stop`).  
  - *Matcher/Filter*: optional condition that narrows when the hook runs (e.g., only shell commands).  
  - *Handler*: action performed (shell command, HTTP request, LLM prompt, sub‑agent).  
  - *Outcome*: returned context, decision, log entry, or state update.  
- Hooks make specific checks deterministic while the model remains free to choose plans, edits, and tool calls.

## Why Hooks Are Underutilized
- Teams often add more prompt instructions because they are immediately visible.  
- Hooks require initial setup: selecting an event, writing a script, testing payloads, and defining failure handling.  
- Their benefits are indirect—avoided mistakes, shorter recovery loops, durable logs—rather than visible model output.  
- Good first hooks map to clear “always/never/block/run/verify” policies (protected paths, blocked commands, required tests, audit logging, completion gates).

## Practical Demo
- A small checkout calculator demo illustrates the full hook flow.  
- Hooks applied in the demo:
  - **SessionStart** – Load repo‑specific conventions.  
  - **UserPromptSubmit** – Add extra context when prompts mention checkout, payment, billing, refunds, or invoices.  
  - **PreToolUse** – Block edits to generated files, `.env`, `.git`, sensitive fixtures, and paths outside the repo; block dangerous shell commands.  
  - **PostToolUse** – Run tests after code edits and persist the result.  
  - **Stop** – Prevent the agent from finishing when the last quality gate failed.  
  - **SessionEnd** – Append a final audit record.  
- Walkthrough steps:
  1. Open the demo; SessionStart loads context.  
  2. Submit a prompt about checkout flow; UserPromptSubmit adds relevant context.  
  3. Edit code and run tests; PostToolUse records test outcome.  
  4. Attempt to edit a protected generated file; PreToolUse blocks it.  
  5. Issue a dangerous shell command; PreToolUse blocks it.  
- Commands provided: run unit tests, reset demo state, inspect loaded hooks.

## Takeaway
- Hooks provide deterministic enforcement points that complement prompt instructions.  
- Implementing a core set of lifecycle hooks can dramatically improve safety, auditability, and reliability of agent‑driven workflows.