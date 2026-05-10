---
title: New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration | Claude
url: https://claude.com/blog/new-in-claude-managed-agents
date: 2026-05-11
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-11T06:04:46.741896
---

# New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration | Claude

# New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

## Build self‑improving agents with dreaming
- Dreaming is a scheduled process that reviews past sessions and memory stores, extracts patterns, and curates memories for agent improvement.  
- Developers can choose automatic memory updates or manual review before changes are applied.  
- It surfaces patterns a single agent cannot see (recurring mistakes, convergent workflows, shared preferences) and restructures memory to stay high‑signal.  
- Particularly useful for long‑running work and multi‑agent orchestration.  
- Available in Managed Agents on the Claude Platform (research preview; request access).

## Deliver better outcomes
- Outcomes let developers define a rubric describing success; a separate grader evaluates output against this rubric in its own context window.  
- If the output fails, the grader pinpoints needed changes and the agent iterates until the rubric is satisfied.  
- Enables agents to self‑correct without human review, useful for detailed, exhaustive, or subjective quality criteria (e.g., brand voice, design guidelines).  
- Internal benchmarks showed up to +10 points improvement on hard tasks, +8.4 % on docx generation, and +10.1 % on pptx generation.  
- Agents can trigger a webhook when an outcome is achieved.

## Handle complex tasks with multiple agents
- Multi‑agent orchestration introduces a lead agent that breaks a job into pieces and delegates to specialist sub‑agents, each with its own model, prompt, and tools.  
- Specialists run in parallel on a shared filesystem, contributing to the lead agent’s context.  
- Persistent events let the lead agent check in mid‑workflow; the Claude Console provides full traceability of actions and reasoning.  

## What teams are building
- **Harvey**: Uses dreaming to retain learnings across legal drafting sessions, achieving ~6× higher completion rates.  
- **Netflix platform team**: Deploys multi‑agent orchestration to analyze massive log batches in parallel, surfacing recurring issues.  
- **Spiral by Every**: Combines orchestration and outcomes for an API/CLI writing agent; lead agent on Haiku delegates drafting to Opus sub‑agents, scoring drafts against editorial rubrics.  
- **Wisedocs**: Implements outcomes to grade document reviews, cutting review time by 50% while maintaining standards.

## Getting started
- Dreaming is in research preview; outcomes, multi‑agent orchestration, and memory are in public beta.  
- Request dreaming access, explore documentation, and deploy agents via the Claude Console.