---
title: AI Engineering Productivity is Anything But Normal | Tomasz Tunguz
url: https://tomtunguz.com/ai-engineering-productivity-anything-but-normal/
site_name: tldr
content_file: tldr-ai-engineering-productivity-is-anything-but-normal
fetched_at: '2026-07-27T19:33:02.826709'
original_url: https://tomtunguz.com/ai-engineering-productivity-anything-but-normal/
author: Tomasz Tunguz
date: '2026-07-27'
description: Per-engineer productivity from AI coding runs from -19% to 8x. The distribution has three tiers, & the gap between them is the operating layer, not the model.
tags:
- tldr
---

In short :AI engineering productivity outcomes cluster in three tiers: a mean of 20-46% from distributing an IDE, a frontier of 2.5-3x from companies building the operating layer around agents (Replit, NVIDIA, Amplitude, Anthropic), & a factory tier at 8x+ where agents operate as first-class organizational units (Nubank with Devin). The gap is not the model but the operating discipline built around it.

We are now in an era where we should expect 3x more from each other.

Over the last six months, one data point has followed another :

* NVIDIA reported a 3x increase in committed code across 30,000 developers with bug rates flat.1
* Amplitude tripled weekly production commits, with an AI agent now a top-three contributor to the codebase.2
* Anthropic measured a 2.5x increase in code written per engineer since adopting Claude Code internally, quality stable.3
* Replit doubled its team & tripled per-engineer output over the same period, with review times, reversions, & incidents all flat.4

The chart above sorts the ecosystem into three unequal tranches, each defined by how much of the model’s power the company captures.5

The first tranche is what most companies experience today. Distribute an AI IDE, change nothing else, & the outcome is modest.

“Engineering leaders went into AI expecting 2-3x productivity gains but are landing closer to 30%.”

— Augment Code6

Faros’s telemetry across 22,000 developers confirms this: engineers completed epics 66% faster, but bugs per developer increased by 54%.7The Google randomized controlled trial put the number at 21%, close to GitHub’s 24%.89This is the default outcome.

The frontier tranche follows. Companies here have built harnesses around the model, orchestrating agents sharing context across GitHub, Linear, & Slack; escalating to engineers for their judgment.

“Every employee gets a manager agent that spawns worker agents in loops. Our internal agent outperformed a seven-figure SaaS tool in security testing and incident triage at one-tenth the cost.”

— Amjad Masad, Replit, “The Self-Driving Company”4

Human PR review time dropped 30%. Complex support handling time dropped 60%. Total code contribution rose 5.8x. This is where the 3x number lives.

The third tranche are the software factories, & here the name is an apt descriptor. They are AI machines that produce software mechanistically. Cognition’s Devin refactors monolithic codebases end-to-end. Factory.ai is deploying software factories at NVIDIA, Adobe, Blackstone, & EY.10

“Nubank achieved an 8x improvement in engineering efficiency & a 20x cost reduction using Devin for large-scale refactoring.”

— Contrary Research, January 202611

Goldman Sachs is piloting Devin alongside 12,000 human developers & publicly estimates agentic AI could deliver 3-4x the rate of prior tools.12

AI engineering productivity gains are here. The initial data shows what to expect: most teams should migrate from 20% productivity gains to a 3x productivity gain & they aren’t normal.

1. Cursor, “How NVIDIA uses Cursor,” February 2026.↩︎
2. Cursor, “Amplitude and Cursor cloud agents,” April 2026.↩︎
3. Boris Cherny, head of Claude Code, on the Big Technology podcast, July 2026.↩︎
4. Amjad Masad, “The Self-Driving Company,” July 16, 2026.↩︎↩︎
5. The distribution above is illustrative, not statistical. Each point is a reported multiplier from a published study, RCT, or company disclosure. It is not drawn from a sampled population, & the curve is a right-skewed log-normal fit to the pattern of reported outcomes, not to raw data. Treat it as a shape argument, not an estimator.↩︎
6. Augment Code on X, 2026.↩︎
7. Faros, “AI Engineering Report 2026”.↩︎
8. Google internal randomized controlled trial, ~100 engineers, 2024. Referenced in DORA reports; roundup atValue Add VC.↩︎
9. GitHub, Microsoft, and Accenture study with a large fintech, ~450 developers, 2024.↩︎
10. Factory.ai, “Factory 2.0: From coding agents to software factories”.↩︎
11. Contrary Research, “Cognition”, January 2026.↩︎
12. CNBC, “Goldman Sachs is piloting its first autonomous coder in major AI milestone for Wall Street,” July 2025.↩︎

### Get the next one in your inbox

The 1-minute read that turns tech data into strategic advantage.Read by 150k+ founders & operators.

Subscribe

GP at Theory Ventures. Former Google PM. Sharing data-driven insights on AI, web3, & venture capital.

Bloomberg•WSJ•Economist