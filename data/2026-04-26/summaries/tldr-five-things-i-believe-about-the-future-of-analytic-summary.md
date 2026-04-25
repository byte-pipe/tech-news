---
title: Five things I believe about the future of analytics
url: https://roundup.getdbt.com/p/five-things-i-believe-about-the-future
date: 2026-04-26
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-26T06:02:45.643914
---

# Five things I believe about the future of analytics

# Five things I believe about the future of analytics

## Thing 1: Analysts are going technical  
- Coding agents (e.g., Claude Code) are pulling analysts onto the command line and into IDEs.  
- Analysts can now draft analyses without writing code themselves, gaining huge ROI on time invested.  
- Data consumers (business users) remain in familiar BI tools, creating a bifurcation: technical tooling for everyone except end‑users.

## Thing 2: Data usage will explode  
- The biggest AI disruption is at the “data usage” layer, not just pipelines or platforms.  
- Massive investment has removed infrastructure bottlenecks, but analysis (thinking) remains the limiting factor.  
- Analytic agents promise to eliminate that bottleneck by augmenting human thought.

## Thing 3: Analytic agents are happening now, and moving fast  
- Companies (dbt Labs, Meta, OpenAI, Ramp) have shipped production‑ready analytics agents within months.  
- These agents cover the full workflow: data discovery, SQL generation, notebook publishing, etc.  
- Adoption is rapid because the agents already deliver value.

## Thing 4: Agents consume dramatically more than humans  
- Agents will soon run queries autonomously, generating hypotheses, testing, and concluding without human prompts.  
- Early data (dbt MCP server calls) shows a 50 % month‑over‑month growth since launch.  
- Prediction: agent‑initiated queries will outnumber human‑initiated queries within 12 months and could be 100× higher within 36 months.

## Thing 5: Harnesses are a leverage point  
- A “harness” (the code that feeds information to an LLM) can create up to a 6× performance gap even with the same model.  
- Vertical‑specific harnesses tuned to a domain (e.g., data warehousing, dbt schemas) outperform generic ones.  
- Harness design can be automated, offering a powerful optimization lever for analytics workloads.

## My conclusions  
- **Agents will become the primary consumers of analytic data within a year; infrastructure must be built for that reality.**  
- Analysts will not disappear; their impact grows as they shift from dashboard building to creating and operating agentic analytic systems.  
- Human‑facing analytic assets will still be needed, but they will be authored from technical tools (Claude Code, Cursor) rather than traditional BI interfaces.  
- The data analyst workflow will increasingly resemble that of a front‑end engineer, focusing on UI layers atop data‑driven reasoning engines.  

*3.5 years into the current AI wave and things are truly getting fun. Hope you’re enjoying yourself too :) – Tristan*