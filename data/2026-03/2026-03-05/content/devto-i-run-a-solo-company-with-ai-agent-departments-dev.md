---
title: I Run a Solo Company with AI Agent Departments - DEV Community
url: https://dev.to/setas/i-run-a-solo-company-with-ai-agent-departments-50nf
site_name: devto
content_file: devto-i-run-a-solo-company-with-ai-agent-departments-dev
fetched_at: '2026-03-05T06:00:16.290811'
original_url: https://dev.to/setas/i-run-a-solo-company-with-ai-agent-departments-50nf
author: João Pedro Silva Setas
date: '2026-03-03'
description: I built 8 AI agent departments using GitHub Copilot custom agents — CEO, CFO, COO, Lawyer, Accountant, Marketing, CTO, and an Improver. They share memory, consult each other, and self-improve. Here's how it works. Tagged with agents, ai, automation, startup.
tags: '#agents, #ai, #automation, #startup'
---

TLDR:

* I'm a solo founder running 5 SaaS products with 0 employees
* I built 8 AI agent "departments" using GitHub Copilot custom agents — CEO, CFO, COO, Lawyer, Accountant, Marketing, CTO, and an Improver that upgrades the others
* They share a persistent knowledge graph, consult each other automatically, and self-improve
* Here's how it actually works, with code snippets and honest tradeoffs

## The Premise

I run a solo software company from Braga, Portugal. Five products. Zero employees. Zero funding.

The products:SondMe(radio monitoring),Countermark(bot detection), OpenClawCloud (AI agent hosting), Vertate (verification), and Agent-Inbox. All built with Elixir, Phoenix, and LiveView. All deployed on Fly.io for under €50/month total.

The problem: even a solo founder needs to handle marketing, accounting, legal compliance, operations, financial planning, and tech decisions. Wearing all those hats meant things slipped. Deadlines got missed. Content didn't get posted. IVA filings almost got forgotten.

So I built something weird: a full virtual company where every department is an AI agent.

## The Agent Roster

Each agent is a markdown file in.github/agents/inside my management repo. GitHub Copilot loads the right agent based on which mode I'm working in. Here's the team:

Agent

Role

What It Actually Does

CEO

Strategy & trends

Scans Hacker News and X for market signals. Validates product direction against trends.

CFO

Financial planning

Pricing models, cash flow projections, cost analysis. Checks margins before I commit to anything.

COO

Operations

Runs daily standups. Maintains the sprint board. Orchestrates other agents.

Marketing

Content & growth

Writes all social media content in my voice. Schedules posts. Runs engagement routines.

Accountant

Tax & invoicing

Portuguese IVA rules, IRS simplified regime, invoice requirements. Knows fiscal deadlines cold.

Lawyer

Compliance

GDPR, contracts, Terms of Service. Reviews product claims before Marketing publishes them.

CTO

Architecture

Build-vs-buy decisions, DevOps, stack consistency across all 5 products.

Improver

Meta-agent

Reads past mistakes and upgrades the other agents. Creates new skills. The system evolves itself.

These aren't chatbots. Each agent has domain-specific instructions, access to real tools (MCP servers for X, dev.to, Sentry, scheduling, memory), and the authority to act autonomously.

## How It Works — The Architecture

### Agent Files

Each agent is a.agent.mdfile with structured instructions:

# Marketing Agent — AIFirst

## Core Responsibilities

-
 Content strategy and calendar

-
 Social media posting (via X and dev.to MCP tools)

-
 Community engagement

-
 Launch planning

## Content Voice & Tone

-
 First person singular ("I", never "we")

-
 Technical substance over hype

-
 Show the work — code, configs, real numbers

-
 No: revolutionary, game-changing, leverage, synergy...

## Autonomous Execution

-
 Posts tweets directly via scheduler

-
 Publishes dev.to articles (published: true)

-
 Engagement: likes, replies, follows — every day

Enter fullscreen mode

Exit fullscreen mode

The key insight: these aren't generic "be helpful" prompts. The Marketing agent knows my posting schedule, my voice quirks, which platforms I use, which URLs are blocked on X, and which products to rotate in the content calendar. The Accountant knows Portuguese ENI tax law, IVA quarterly deadlines, and the simplified IRS regime. Real domain expertise encoded in markdown.

### Shared Memory — The Knowledge Graph

This is where it gets interesting. All agents share apersistent knowledge graphvia a Model Context Protocol (MCP) memory server. What one agent learns, every other agent can read.

┌──────────┐ ┌─────────────┐ ┌──────────┐
│ Marketing│───→│ │←───│ CFO │
│ │ │ Knowledge │ │ │
│ CEO │───→│ Graph │←───│Accountant│
│ │ │ │ │ │
│ Lawyer │───→│ (memory.jsonl)│←──│ Improver │
└──────────┘ └─────────────┘ └──────────┘

Enter fullscreen mode

Exit fullscreen mode

Entities have types:product,decision,deadline,client,metric,lesson. Relations use active voice:owns,uses,built-with,depends-on.

Real example of what's stored:

* Strategic decisions and their rationale
* Product status, launch dates, key metrics
* Financial data (pricing decisions, cost benchmarks)
* Legal and compliance decisions
* Lessons learned from launches and incidents

The memory has retention rules too — standups older than 7 days get pruned, but lessons and decisions are permanent. It's the company's institutional memory.

### Inter-Agent Communication

Here's the part that surprised me most. Agentsconsult each other automaticallywhen their work crosses into another domain.

The protocol works like this: each agent has a trigger table. When Marketing writes a product claim, it auto-calls the Lawyer for review. When CFO does pricing, it calls the Accountant to verify tax treatment. When CTO proposes infrastructure changes, it calls CFO to check the cost impact.

CEO ←→ CFO Strategy ↔ Financial viability
CEO ←→ CTO Strategy ↔ Technical feasibility
CFO ←→ Accountant Financial plans ↔ Tax compliance
Marketing ←→ Lawyer Campaigns ↔ Legal compliance
COO → any Orchestrator can call any agent

Enter fullscreen mode

Exit fullscreen mode

The peer review request format looks like this:

## Peer Review Request

**From**
: Marketing

**Call chain**
: COO → Marketing

**Task**
: Draft product launch tweet for Countermark

**What I did**
: Wrote tweet claiming "99% bot detection accuracy"

**What I need from you**
: Is this claim substantiated?

Please respond with:

1.
 ✅ APPROVED

2.
 ⚠️ CONCERNS

3.
 🔴 BLOCKING

Enter fullscreen mode

Exit fullscreen mode

Call-chain tracking prevents infinite loops — each consultation includes who's already been called, and there's a max depth of 3. If CFO calls Accountant, the Accountant can't call CFO back.

### The Daily Standup

Every morning, the COO agent runs a standup that:

1. Checks Sentry for errors across all 5 products
2. Scans the sprint board for overdue tasks
3. Checks if periodic prompts are overdue (weekly review, monthly accounting, quarterly IVA)
4. Reads the knowledge graph for context
5. Delegates tasks to other agents
6. Produces a prioritized day plan

It's not a status meeting — it's an automated orchestration run that delegates work to the right specialist.

### Self-Improvement — The Improver Agent

This is the weirdest (and possibly most valuable) part. There's a meta-agent called the Improver whose job is to:

* Readlessonentities from memory (mistakes and learnings logged by other agents)
* Identify patterns across sessions
* Create new skills (reusable instruction files for specific domains)
* Update other agents' instructions when gaps are found
* Propose new agents when workload patterns suggest one is needed

After every complex task, agents store a lesson:

Entity: lesson:2026-02-10:memory-corruption
Type: lesson
Observations:

 -
 "Agent: CTO"

 -
 "Category: bug"

 -
 "Summary: Concurrent memory writes corrupted JSONL file"

 -
 "Detail: Parallel tool calls to create_entities and create_relations
 caused race condition in the memory server"

 -
 "Action: Added async mutex + atomic writes to local fork"

Enter fullscreen mode

Exit fullscreen mode

The Improver reads these monthly and upgrades the system. The system literally improves itself.

## The Honest Tradeoffs

This isn't a "10x productivity" pitch. Here's what's actually hard:

### Context Windows Are Real

Each agent operates within a context window. Long, complex tasks can exceed it. The solution: agents delegate heavy data-gathering to subagents to keep their own context focused. It works, but it's a constant architectural consideration.

### Agents Hallucinate

The Lawyer catches most compliance hallucinations before they reach production. The inter-agent review protocol exists because of this — multiple agents checking each other's work is the safety net.

### Memory Corruption

We hit this one early. The knowledge graph is stored as a JSONL file. When multiple agents made parallel tool calls (writing entities and relations simultaneously), the file got corrupted — partial writes, duplicate entries, broken JSON lines.

The fix: I forked the upstream MCP memory server and added three things:

1. Async mutex— prevents concurrentsaveGraph()calls
2. Atomic writes— writes to a.tmpfile then renames
3. Auto-repair on load— skips corrupt lines and deduplicates

### It's Not a Replacement for Thinking

The agents are good at executing within their domain. They're bad at knowing when the domain is wrong. Strategic pivots, gut-feel product decisions, "this just doesn't feel right" — that's still me.

## Month 2 Results

After two months of running this system:

* Revenue: €6.09 (one subscriber, from day 2. No ads, no outreach.)
* Infrastructure: ~€42/month (Fly.io across all apps)
* Content output: 84+ tweets, 5 dev.to articles, multiple HN comments
* Time on marketing: less than 1 hour per week (agents handle scheduling, drafting, and engagement)
* Compliance: zero missed deadlines (IVA, IRS, Segurança Social all tracked)

The revenue is barely there. But I ship every week, the system keeps improving, and I'm building in public with a team that costs €0.

## The Code

The entire system lives in a single management repo:

.github/
 agents/
 ceo.agent.md
 cfo.agent.md
 coo.agent.md
 marketing.agent.md
 accountant.agent.md
 lawyer.agent.md
 cto.agent.md
 improver.agent.md
 copilot-instructions.md # Global company identity + protocols
 skills/
 portuguese-tax/SKILL.md
 saas-pricing/SKILL.md
 seguranca-social/SKILL.md
 instructions/
 marketing.instructions.md
 ...
Marketing/
 social-media-sop.md
 social-media-strategy-2026.md
 drafts/
 week-2026-W09.md
 ideas.md
 ...
BOARD.md # Sprint board (COO-maintained)
Setas/
 Atividade.md # Fiscal framework
 INSTRUCTIONS.md # Operational manual

Enter fullscreen mode

Exit fullscreen mode

Thecopilot-instructions.mdfile is loaded into every Copilot interaction. It defines the company identity, agent system, memory protocols, communication rules, and product registry. It's the constitution of the virtual company.

Skills are reusable knowledge modules —portuguese-tax/SKILL.mdcontains complete IVA scenarios, IRS regime rules, invoice requirements, and deadline calendars. The Accountant agent loads this skill automatically when handling tax questions.

## What I'd Do Differently

If I were starting fresh:

1. Start with 3 agents, not 8— COO, Marketing, and Accountant cover 80% of the value. Add specialists when the workload justifies them.
2. Invest in memory early— the knowledge graph is the most valuable part. It compounds over time. I wish I'd been more disciplined about what gets stored from day one.
3. Test agent outputs against each other— the inter-agent review protocol was added after hallucinations caused problems. Build it in from the start.

## Why This Matters

I'm not claiming AI agents replace human teams. They don't. What they do is let a solo founder operate with thestructureof a team — defined roles, communication protocols, institutional memory, and systematic improvement.

The alternative was either hiring people I can't afford or continuing to drop balls. This gives me a middle path: structured execution with human judgment at the critical points.

The system cost: €0 (GitHub Copilot is included in my existing subscription). The time to build: maybe 40 hours total over 2 months. The ongoing maintenance: the Improver handles most of it.

If you're a solo founder drowning in operational overhead, this might be worth trying. Not because AI agents are magic — but because thestructurethey enforce is valuable even when the agents themselves are imperfect.

I'm João, a solo developer from Portugal building SaaS products with Elixir. I write about the real experience of building in public — the numbers, the mistakes, and the weird experiments like this one. Follow me ondev.toorX (@joaosetas).

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
