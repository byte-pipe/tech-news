---
title: How I Do Content Engineering with Claude Code
url: https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/
date: 2026-05-05
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-05-05T00:53:54.681522
---

# How I Do Content Engineering with Claude Code

# How I Do Content Engineering with Claude Code

## Background
- Ryan Law, Director of Content Marketing at Ahrefs, has 13 years of experience across writing, strategy, leadership, and agency work.  
- He previously built an AI‑assisted content pipeline using ChatGPT and custom GPTs that cut creation time from days to a few hours but still required heavy manual work.  

## New Process Overview
- Uses Claude Code together with 23 custom “skill files” that are chained to produce publish‑ready drafts in 6–12 minutes.  
- Implemented on ~15 new articles and ~30 updates so far.  
- Claims that AI content quality has reached a level where it can automate major parts of the workflow without loss of quality, and even improve research.  

## Important Caveats
- **Experience matters** – the system works because it encodes Ryan’s 13 years of editorial knowledge; newcomers without that background will not see the same results.  
- **Topic selection still matters** – the workflow is designed for informational SEO pieces on topics Ryan understands and that Ahrefs has previously covered.  
- **No plan to mass‑scale** – the goal is to maintain an evergreen library on core topics, not to produce tens of thousands of articles.  

## Core Steps of the Workflow
### 1. Mimic human workflows by chaining editorial skills
- 23 skill files correspond to stages such as keyword research, gap analysis, outlining, drafting, etc.  
- Each file contains a markdown guide for Claude, examples, and output formatting.  
- A master skill (`blog-pipeline`) orchestrates the sequence, allowing full automation from keyword idea to draft.  

### 2. Output every step for iteration and troubleshooting
- Each stage writes its result to a markdown file (e.g., outlines, research primers).  
- Ryan can inspect, edit, and restart from any stage that meets quality criteria, making debugging straightforward.  

### 3. Create test cases for recursive self‑improvement
- Uses Anthropic’s `skill‑creator` to generate test outputs with and without custom guidance.  
- The LLM reviews results and suggests refinements, keeping skill files concise and effective.  

### 4. Give LLMs great data from great sources
- Claude accesses Ahrefs MCP for real keyword metrics, SERP overviews, and common questions.  
- Additional data sources include competitor content, trusted news/research, and Ahrefs product documentation.  
- Mandating concrete data sources prevents the model from producing vague, “bloviated” content.  

### 5. Front‑load human direction
- Small amounts of expert input at the start of the process (e.g., clear brief, target intent) are far more impactful than extensive later editing.  

## Additional Resources
- YouTube walkthrough of the current AI content process.  
- Ahrefs podcast episode demonstrating the system to CMO Tim Soulo.  
- Links to Ahrefs MCP use‑case guide and API information for integrating SEO data into other tools.