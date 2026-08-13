---
title: Agents are coming for data (just slowly) | InfoWorld
url: https://www.infoworld.com/article/4203157/agents-are-coming-for-data-just-slowly.html
date: 2026-08-14
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-14T06:01:12.853191
---

# Agents are coming for data (just slowly) | InfoWorld

# Agents are coming for data (just slowly)

## Overview  
- Agents have appeared in almost every software area except data, mainly because large‑language models have only recently become reliable at generating SQL.  
- Two useful agent categories:  
  1. Agents that perform analytics.  
  2. Agents that manage data‑pipeline plumbing.

## Why data engineering is hard  
- Engineers depend on external systems they cannot control.  
- Schemas change without notice, sources go offline, APIs evolve, and data quality issues (type changes, duplicate keys, missing rows) appear unpredictably.  
- If nothing ever changed, data engineering would be easy, but “the only constant is change.”

## The boring work is where agents thrive  
- **Maintenance automation:**  
  - Agents can read the assumptions embedded in data models (uniqueness, non‑null fields, join relationships) and turn them into tests that verify those assumptions.  
  - When a table is renamed, a column type widens, or a column moves, an agent can often patch the change automatically or at least produce a diagnosis and suggested fix for a human.  
- **Context handling:**  
  - Context is usually handcrafted and drifts over time.  
  - Agents excel at mechanical parts of context (inferring join paths, column value distributions, frequently queried tables, sales‑region lists).  
  - They struggle with business‑logic decisions that are not stored in the warehouse (how to calculate revenue, definition of “customer,” fiscal‑year start).  
  - Their role is to flag when such business rules silently stop being true.

## Automated agent insights remain a fantasy  
- The vision of agents surfacing unsolicited, relevant insights is still a research prototype.  
- High relevance is required; false positives quickly erode user trust.  
- Deterministic alerting systems already suffer from “alarm fatigue,” so agents will face the same tuning challenges until a higher level of intelligence emerges.

## Three concrete steps for data teams  

1. **Lay the groundwork** – Decide how you will manage and expose context before inviting an agent to use it.  
2. **Invest in context validation** – Write a small suite of evaluation tests, automate their execution, and monitor failures; these evals protect the pipeline when an agent makes a mistake.  
3. **Run on suitable infrastructure** – Choose compute that can scale up and down quickly, supports bursty parallel queries, and provides tenant isolation so one curious agent does not throttle others.

## Latency is a bigger deal than it looks  
- Agents generate many queries in rapid succession; the latency of the underlying tools (databases, APIs) becomes the bottleneck, not the LLM response time.  
- A 10 ms engine versus a 100 ms engine makes a 10× difference in total work per minute for an agent that chains queries.  
- Parallelizing agent work speeds it up but also amplifies load; you need enough parallel capacity and isolation.  
- Systems tuned for human‑perceived latency differ from those optimized for agent‑driven throughput.

## Call to action  
- The “agentic wave” is arriving regardless of a team’s readiness.  
- Preparing the stack now—building context, establishing evals, and provisioning scalable infrastructure—gives early adopters a lasting advantage and prevents later scrambling when query volumes surge.

---  

*Jordan Tigani* – Co‑founder and CEO of MotherDuck, former BigQuery architect, ex‑Chief Product Officer at SingleStore, former Microsoft Research engineer. He holds a BA from Harvard and an MS from the University of Washington. When not working, he rows or walks.