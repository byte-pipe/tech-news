---
title: Anthropic launches advisor tool for Claude API users
url: https://www.testingcatalog.com/anthropic-launches-advisor-tool-for-claude-platform-api-users/
site_name: tldr
content_file: tldr-anthropic-launches-advisor-tool-for-claude-api-use
fetched_at: '2026-04-12T06:00:26.715275'
original_url: https://www.testingcatalog.com/anthropic-launches-advisor-tool-for-claude-platform-api-users/
date: '2026-04-12'
published_date: '2026-04-09T21:52:48.000Z'
description: Anthropic launches the advisor tool for Claude, enabling developers to pair Opus with efficient models to boost AI agent reasoning at lower cost.
tags:
- tldr
---

Anthropic has unveiled the advisor tool on the Claude Platform, providing developers with the ability to use Opus as an advisor alongside Sonnet or Haiku as executors. This strategy allows agents to access advanced reasoning capabilities while maintaining operational costs at the level of the more efficient executor models. The advisor tool is now available publicly through the Claude Platform API and can be activated with a simple configuration in the Messages API request. The primary audience includes developers and organizations building AI agents that require both cost management and high-level reasoning.

We're bringing the advisor strategy to the Claude Platform.Pair Opus as an advisor with Sonnet or Haiku as an executor, and get near Opus-level intelligence in your agents at a fraction of the cost.pic.twitter.com/fRkegyMs5t

— Claude (@claudeai) 
April 9, 2026

The advisor tool works by allowing Sonnet or Haiku to handle tasks independently. When these executors encounter complex decision points, they call upon Opus for guidance. Opus reviews the shared context and returns a plan or corrective feedback, after which the executor resumes its task. This approach contrasts with traditional systems where a large model orchestrates and delegates tasks to smaller agents. Instead, the advisor tool allows the executor to escalate only when necessary, keeping most operations at a lower cost. Technical evaluations show improvements in benchmarks such as SWE-bench Multilingual, BrowseComp, and Terminal-Bench 2.0. For example, Haiku with an Opus advisor more than doubled its standalone benchmark score while costing significantly less than running Sonnet alone.

Anthropic, the company behind Claude, focuses on developing advanced AI systems that prioritize reliability and efficiency. This release underscores the company’s commitment to helping developers deploy intelligent agents at scale without incurring the high costs typically associated with frontier-level models.

Source

### RelatedArticles

## OpenAI develops unified Codex app and new Scratchpad feature

11 Apr 2026

·

2 min read

 

 

## Notion tests Computer to expand capabilities of its AI offering

10 Apr 2026

·

2 min read

 

 

## Google prepares broader rollout of Skills for Gemini and AI Studio

10 Apr 2026

·

2 min read

 

 

## Anthropic develops managed 24/7 Agent for Claude mobile apps too

10 Apr 2026

·

1 min read

 

 

## Perplexity launches Personal Finance powered by Plaid

9 Apr 2026

·

2 min read

 

 

## Anthropic launches Claude Cowork in General Availability

9 Apr 2026

·

1 min read