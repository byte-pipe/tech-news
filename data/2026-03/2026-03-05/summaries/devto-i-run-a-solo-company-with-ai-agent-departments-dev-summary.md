---
title: I Run a Solo Company with AI Agent Departments - DEV Community
url: https://dev.to/setas/i-run-a-solo-company-with-ai-agent-departments-50nf
date: 2026-03-03
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-03-05T06:02:32.899130
---

# I Run a Solo Company with AI Agent Departments - DEV Community

# I Run a Solo Company with AI Agent Departments

## TL;DR
- Solo founder operating five SaaS products with no employees or external funding.  
- Created eight AI “departments” (CEO, CFO, COO, Marketing, Accountant, Lawyer, CTO, Improver) using GitHub Copilot custom agents.  
- Agents share a persistent knowledge graph, automatically consult each other, and self‑improve over time.  
- Article details the architecture, code snippets, and practical trade‑offs.

## The Premise
- Location: Braga, Portugal.  
- Products: SondMe (radio monitoring), Countermark (bot detection), OpenClawCloud (AI agent hosting), Vertate (verification), Agent‑Inbox.  
- Tech stack: Elixir, Phoenix, LiveView; deployed on Fly.io for under €50/month total.  
- Challenge: a solo founder must still handle marketing, accounting, legal, operations, finance, and technical decisions, leading to missed deadlines and forgotten compliance tasks.  

## Agent Roster
| Agent | Role | Core Functions |
|-------|------|----------------|
| CEO | Strategy & trends | Scans Hacker News and X for market signals; validates product direction. |
| CFO | Financial planning | Builds pricing models, cash‑flow projections, cost analysis; checks margins. |
| COO | Operations | Runs daily stand‑ups, maintains sprint board, orchestrates other agents. |
| Marketing | Content & growth | Writes social media posts in founder’s voice, schedules posts, runs engagement routines. |
| Accountant | Tax & invoicing | Handles Portuguese IVA rules, IRS simplified regime, invoice requirements, fiscal deadlines. |
| Lawyer | Compliance | Reviews GDPR, contracts, Terms of Service, validates product claims. |
| CTO | Architecture | Advises on build‑vs‑buy, DevOps, stack consistency across all products. |
| Improver | Meta‑agent | Analyzes past mistakes, creates new skills, updates other agents, proposes new agents. |

- Each agent is defined in a markdown file inside `.github/agents/`.  
- Agents have domain‑specific instructions, access to real tools (e.g., MCP servers, Sentry, scheduling), and authority to act autonomously.

## How It Works – Architecture

### Agent Files
- Structured markdown (`.agent.md`) containing responsibilities, voice guidelines, and autonomous execution steps.  
- Example: Marketing agent includes posting schedule, tone (“I” not “we”), prohibited buzzwords, and direct integration with X and dev.to via schedulers.

### Shared Memory – Knowledge Graph
- Persistent graph stored in `memory.jsonl` accessed through a Model Context Protocol (MCP) memory server.  
- Entities: product, decision, deadline, client, metric, lesson, etc.  
- Relations expressed with active verbs (e.g., `owns`, `uses`, `built‑with`).  
- Retention rules: routine stand‑up entries older than 7 days are pruned; lessons and strategic decisions are permanent.  
- Provides institutional memory for all agents.

### Inter‑Agent Communication
- Each agent has a trigger table; when its output touches another domain, it automatically calls the relevant agent for peer review.  
- Call‑chain format includes source, task, and required response (APPROVED, CONCERNS, BLOCKING).  
- Loop prevention: call chain tracks already‑called agents and caps depth at three.  

### Daily Stand‑up (COO Agent)
1. Checks Sentry for errors across all products.  
2. Scans sprint board for overdue tasks.  
3. Verifies periodic prompts (weekly review, monthly accounting, quarterly IVA).  
4. Reads knowledge graph for context.  
5. Delegates tasks to specialist agents.  
6. Generates a prioritized day plan.  

### Self‑Improvement – Improver Agent
- Periodically reads `lesson` entities logged by other agents.  
- Detects patterns, creates new instruction files, updates existing agents, and suggests new agents when workload shifts.  
- Example lesson: memory corruption caused by concurrent writes; Improver adds async mutex and atomic write handling.  

## Honest Trade‑offs
- **Context window limits**: agents must keep prompts concise; heavy data gathering is delegated to sub‑agents.  
- **Hallucination risk**: agents can produce inaccurate statements; Lawyer and peer‑review mechanisms act as safety nets.  
- **Memory consistency**: race conditions in the shared graph required mutexes and atomic operations.  
- **Operational overhead**: maintaining trigger tables, prompt engineering, and monitoring agent behavior consumes developer time.  

## Takeaway
- An AI‑driven “virtual company” can automate many founder responsibilities, but it demands careful architecture, robust inter‑agent safeguards, and ongoing maintenance to handle context limits and hallucinations.