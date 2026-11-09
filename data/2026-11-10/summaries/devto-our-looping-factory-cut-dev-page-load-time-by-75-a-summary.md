---
title: Our Looping Factory Cut DEV Page Load Time by 75% and Counting - DEV Community
url: https://dev.to/dailycontext/our-looping-factory-cut-dev-page-load-time-by-75-and-counting-1hnf
date: 2026-11-09
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-11-10T04:42:24.593464
---

# Our Looping Factory Cut DEV Page Load Time by 75% and Counting - DEV Community

# Our Looping Factory Cut DEV Page Load Time by 75% and Counting

## Context and Motivation
- A month ago the average Rails request on DEV took ~70 ms, with P99 often > 1 s.  
- The team needed massive, systematic performance gains but struggled to prioritize them amid other work.  
- The goal was to separate routine maintenance from creative, high‑impact projects by building an autonomous “software factory.”

## Performance Gains
- Average request time dropped from 70 ms to 16 ms across ~300 k daily sampled requests.  
- Database time fell from 39 ms to < 12 ms.  
- View rendering reduced from 12 ms to 2.6 ms.  
- Redis latency went from 7 ms to 1.3 ms.  
- Over the last 30 days, 475 pull requests were merged into Forem, including 351 from autonomous loops.

## Automation Approach
- Created a persistent self‑hosted OpenHands hub (Oct 19) to run closed‑loop systems.  
- Built autonomous loops on top of OpenHands and the Agent Client Protocol (ACP) to handle PR creation, testing, and merging without human “clipboard” intervention.  
- Designed feedback loops that ingest live telemetry (ClickHouse spans, read‑only Postgres gateway) so each PR must justify its impact against real traffic.

## Loop Configurations and Evolution
1. **Model routing** – Started with Claude Opus 5.5, then added OpenAI Codex‑ACP and Google Gemini 4 Argon via a three‑provider router with round‑robin selection and 8‑hour cooldowns.  
2. **Git isolation** – Moved from shared checkouts to detached‑HEAD worktrees with self‑healing lock cleanup and a PID 1 init (tini) to avoid git and process collisions.  
3. **Specialized loops** – Split work into orthogonal loops running on 10‑minute daytime ticks:  
   - *perf‑loop*: ActiveRecord, Redis, view partial optimizations.  
   - *rust‑loop*: Port hot Ruby paths to native gems, verified by 1 000‑input differential specs.  
   - *test‑loop*: Parse 30 RSpec shards to trim FactoryBot churn and slow specs.  
   - *error‑loop* and *deps‑loop*: Filter out timeouts, ambiguous bugs, and noisy patches.  
   - *github‑pr‑reviewer & merge loop*: A second‑lens model audits blast radius and auto‑merges low‑risk PRs after CI passes.

## Results and Impact
- 444 PRs merged by autonomous loops: 172 performance, 93 test‑suite speedups, 32 Rust rewrites, 29 dependency upgrades, 20 production error fixes, 5 issue‑to‑PR conversions.  
- Remaining 93 bespoke PRs were driven directly by the author, focusing on high‑leverage work such as home‑feed redesign, JavaScript delivery modernization (‑71 % app.js, ‑55 % base.js), L1 local Redis cache, and new observability extensions.  
- The system eliminated intermittent slowdowns, handled traffic peaks smoothly, and freed the author’s time for deeper engineering tasks.

## Takeaways
- Autonomous loops can turn routine performance maintenance into a self‑sustaining pipeline, allowing engineers to focus on creative, high‑impact work.  
- Real‑time telemetry integration is crucial for loops to produce traffic‑aware, justified changes.  
- A modular, garden‑metaphor approach—strong contracts at the edges and isolated “beds” for specific tasks—keeps the codebase healthy while enabling continuous churn.  

---  
The described software factory demonstrates how AI‑driven automation, when properly looped and guarded, can deliver dramatic latency reductions and reshape the balance between maintenance and innovation.