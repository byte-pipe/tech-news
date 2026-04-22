---
title: Agentic coordination, Human delivery - Dont Dos
url: https://dontdos.substack.com/p/what-if-the-robots-came-for-the-org
date: 2026-04-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:45:45.849045
---

# Agentic coordination, Human delivery - Dont Dos

# Agentic coordination, Human delivery – summary

## TL;DR
- The author’s profitable 40‑person B2B SaaS company replaced its nine‑person middle‑management coordination layer with a small team of AI agents (LangGraph, Claude Sonnet, Opus) that generate meeting minutes, roadmaps, acceptance criteria and release notes in Notion.  
- Automating coordination proved extremely cheap and low‑risk; the worst output is a slightly awkward Notion paragraph.  
- Tasks that still require humans are high‑impact, high‑risk activities such as performance reviews, career planning and any work that puts an engineer on a pager.  

## Company shape and original problem
- ~40 employees: 3 senior leaders, ~20 “making” staff (engineers, designers, QA, support), and 9 middle‑layer staff (product managers, engineering managers, design lead, QA lead).  
- The middle layer was hired to absorb strategic chaos from leadership and translate it into clear work items for the delivery teams.  
- Over time, information hand‑offs degraded: a strategic point spoken on Monday became a diluted ticket by Thursday, leading to engineers learning about major deals from support tickets instead of leadership.  

## Diagnosis of the coordination bottleneck
- The organization’s geometry caused “corporate Chinese whispers” – each hand‑off introduced lossy compression, delaying and misaligning execution.  
- The risk of a bad coordinator (misaligned team) is far lower than the risk of a bad engineer (production bug).  
- Treating coordination risk as if it were production risk led to unnecessary paranoia and wasted senior talent on low‑impact tasks.  

## Core insight
- **Coordination work is cheap to automate** because its failure mode is merely a sub‑optimal document.  
- **Shipping code and owning it in production is expensive to automate**; mistakes here have real customer impact, legal exposure, and require on‑call responsibility.  
- The AI industry has focused on the wrong problem by trying to let agents write and ship code directly, rather than using them for coordination.  

## Prototype and implementation
- Built a weekend prototype that ingested Monday leadership meeting transcripts and produced a weekly engineering briefing in Notion.  
- Early outputs were poor; by the fourth iteration the AI‑generated briefings surpassed those written by product managers.  
- After internal validation, the prototype was refined over a month into a production‑grade service running in a Docker container, staffed by a small crew of agents and using Claude Sonnet and Opus for reasoning.  

## Takeaways for founders
- Identify high‑risk, high‑ownership tasks (code shipping, on‑call duties) and keep them human‑centric.  
- Shift expensive middle‑management capacity to AI‑driven coordination: meeting summarisation, ticket generation, roadmap drafting, acceptance‑criteria writing.  
- Expect rapid ROI: the cost of running the agents is comparable to a single coffee or pint, yet it frees senior staff from repetitive, low‑impact work.  

## Outlook
- The author plans to continue expanding the agentic coordination layer while acknowledging that full automation of production ownership remains a distant challenge.