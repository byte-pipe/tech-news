---
title: Anthropic launches advisor tool for Claude API users
url: https://www.testingcatalog.com/anthropic-launches-advisor-tool-for-claude-platform-api-users/
date: 2026-04-12
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-12T06:02:08.750160
---

# Anthropic launches advisor tool for Claude API users

# Anthropic launches advisor tool for Claude API users

## Overview
- Anthropic introduced an **advisor tool** on the Claude Platform that lets developers use Opus as an advisor together with Sonnet or Haiku as executors.
- The tool is publicly available via the Claude Platform API and can be enabled with a simple configuration in a Messages API request.
- Target audience: developers and organizations building AI agents that need high‑level reasoning while controlling costs.

## How the advisor tool works
- Executors (Sonnet or Haiku) handle routine tasks independently.
- When an executor reaches a complex decision point, it calls Opus for guidance.
- Opus reviews the shared context, returns a plan or corrective feedback, and the executor resumes execution.
- Unlike traditional pipelines where a large model orchestrates smaller agents, escalation to Opus occurs only when necessary, keeping most operations on the cheaper executor models.

## Benefits and performance
- Provides near‑Opus‑level intelligence at a fraction of the cost of running Opus continuously.
- Technical evaluations show notable improvements on benchmarks:
  - SWE‑bench Multilingual
  - BrowseComp
  - Terminal‑Bench 2.0
- Example: Haiku with an Opus advisor more than doubled its standalone benchmark score while costing less than running Sonnet alone.

## Company context
- Anthropic, the creator of Claude, emphasizes reliability and efficiency in its AI systems.
- The release reflects Anthropic’s commitment to enabling scalable, cost‑effective intelligent agents without the high expense of frontier‑level models.

## Related articles
- OpenAI develops unified Codex app and new Scratchpad feature (11 Apr 2026)
- Notion tests Computer to expand capabilities of its AI offering (10 Apr 2026)
- Google prepares broader rollout of Skills for Gemini and AI Studio (10 Apr 2026)
- Anthropic develops managed 24/7 Agent for Claude mobile apps too (10 Apr 2026)
- Perplexity launches Personal Finance powered by Plaid (9 Apr 2026)
- Anthropic launches Claude Cowork in General Availability (9 Apr 2026)
