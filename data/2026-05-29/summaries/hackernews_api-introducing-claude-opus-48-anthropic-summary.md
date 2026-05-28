---
title: Introducing Claude Opus 4.8 \ Anthropic
url: https://www.anthropic.com/news/claude-opus-4-8
date: 2026-05-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:38:39.893491
---

# Introducing Claude Opus 4.8 \ Anthropic

# Introducing Claude Opus 4.8

## Overview
- Upgrade from Opus 4.7 with better benchmark performance; price unchanged.  
- New features:
  - **Effort control** lets users set how much reasoning effort Claude applies.  
  - **Dynamic workflows** in Claude Code enable very large‑scale problems with parallel sub‑agents.  
  - **Fast mode** runs 2.5× faster and is three times cheaper than previous fast modes.

## Capabilities
- Comparative table (coding, agentic skills, reasoning, knowledge‑work) shows Opus 4.8 surpasses its predecessor and other models.  
- Full details are in the Claude Opus 4.8 System Card.

## Collaboration Feedback (early testers)
- More reliable judgment: asks right questions, catches its own mistakes, pushes back on unsound plans.  
- Only model to complete every case on the Super‑Agent benchmark, matching GPT‑5.5 on cost.  
- Exceeds prior Opus models on CursorBench; tool‑calling uses fewer steps for the same intelligence.  
- Highest score on the Legal Agent Benchmark, breaking the 10 % overall pass threshold.  
- Faster, easier to collaborate with, better at maintaining context and style over long sessions.  
- Strongest computer‑use and browser‑agent performance (84 % on Online‑Mind2Web).  
- Cleaner tool usage; fixes comment‑verbosity and tool‑calling issues seen in Opus 4.7.  
- Higher‑quality analysis: richer, more information‑dense outputs, proactive issue flagging.  
- Improved consistency and reasoning in CoCounsel Legal workflows.  
- Enables step‑change agentic reasoning in Databricks’ Genie, with multimodal PDF/diagram handling at 61 % lower token cost.  
- Better citation precision and token efficiency for dense financial‑document workflows in Hebbia.

## Honesty & Alignment
- Greater honesty: flags uncertainties, makes fewer unsupported claims; ~4× less likely to let flawed code pass unnoticed.  
- Alignment assessment shows new highs in prosocial traits (supporting user autonomy, acting in user’s best interest).  
- Misaligned behavior rates are substantially lower than Opus 4.7 and comparable to Claude Mythos Preview.  
- Full assessment and safety tests are documented in the System Card.

## Additional Launches
- **Dynamic workflows** (research preview) allow Claude to plan, run hundreds of parallel sub‑agents, verify outputs, and report back—e.g., codebase‑scale migrations across hundreds of thousands of lines.  
- **Effort control** (available on all plans) lets users choose higher effort for deeper reasoning or lower effort for faster, token‑conserving responses.  
- **Messages API** now accepts system entries within the messages array, enabling mid‑task instruction updates without breaking the prompt cache.

## Note on Effort Settings
- Default is “high effort,” judged to give the best quality‑experience balance; token usage matches Opus 4.7’s default but with better performance.  
- Options for “extra” (xhigh) or “max” increase token spend for tougher or long‑running asynchronous workflows; “extra” is recommended for difficult tasks.