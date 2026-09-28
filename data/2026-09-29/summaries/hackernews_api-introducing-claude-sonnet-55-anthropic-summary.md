---
title: Introducing Claude Sonnet 5.5 \ Anthropic
url: https://www.anthropic.com/claude-sonnet-5-5
date: 2026-09-29
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-29T07:31:34.035376
---

# Introducing Claude Sonnet 5.5 \ Anthropic

# Introducing Claude Sonnet 5.5

## Overview
- Second model in the Claude 5.5 family, positioned as a faster, lower‑cost complement to Claude Opus 5.5.  
- Targets well‑scoped everyday tasks such as bug fixing, document creation, slide and spreadsheet generation, and design work.  
- Claude Haiku 5.5, aimed at high‑volume, cost‑sensitive use cases, will be added to the family soon.

## Key Improvements over Sonnet 5
- **Performance**: Scores 70.6 % on Terminal‑Bench 4.0 (vs. 10.3 % for Sonnet 5) and is within two points of Opus 5.5 on GDPval‑AA. First Sonnet model to excel at long‑horizon tasks and image understanding.  
- **Collaboration**: Generates clearer prose, making it a better partner for teamwork; speed enables rapid iteration on simpler tasks.  
- **Cost**: Same listed rates ($2 M input tokens, $10 M output tokens, $0.20 M cache reads) but typically uses far fewer tokens, delivering up to 30 % lower cost per task.  
- **Speed**: Produces outputs more than 30 % faster, the quickest Sonnet model to date.  
- **Alignment & Safety**: Matches or exceeds Sonnet 5 on alignment metrics; includes cybersecurity safeguards comparable to Opus 5.5 and retains existing biology safeguards.

## Benchmark Highlights
- **Agentic Coding (Terminal‑Bench 4.0)**: 70.6 % score, far surpassing Sonnet 5 and approaching Opus 5.5.  
- **FrontierCode & CursorBench**: At high effort, Sonnet 5.5 matches GPT‑6 Sol’s best scores while costing roughly one‑fifteenth to one‑fifth as much per task.  
- **Knowledge Work (GDPval‑AA, AA‑Briefcase)**: Scores within a few points of Opus 5.5; at medium effort beats Sonnet 5’s best score for about one‑ninth the cost.  
- **Visual Chart Recognition (Chartography)**: 61.6 % without tools, outperforming Sonnet 5’s 15.6 %.

## Coding Performance
- Shows a dramatic jump in coding ability; high‑effort FrontierCode score is 10 points higher than Sonnet 5 with far lower token usage.  
- Efficient tool‑call batching reduces steps and cost.  
- Early testers note rapid codebase comprehension and snappy responses even on multi‑hour, large‑scale tasks.

## Customer Feedback
- **Epic Games (COO Daniel Vogel)**: Model met high‑tier quality standards on system design audits and data‑flow reviews, handling tens of thousands of lines of code quickly.  
- **Every (Designer Tyler Nishida)**: Fast, steerable in iterative workflows, and inherits natural‑writing upgrades from Opus 5.5.  
- **Additional users**: Report better judgment, fewer unnecessary web searches, and significant token savings, prompting migration of simple and moderate reviews to Sonnet 5.5.

## Future Outlook
- Claude Haiku 5.5 will join the Claude 5.5 family in the coming weeks, extending the lineup for high‑volume, cost‑sensitive applications.