---
title: 'Stop "Vibe Checking" Your AI Agents: How to Build Production Evals in 60 Minutes - DEV Community'
url: https://dev.to/googleai/stop-vibe-checking-your-ai-agents-how-to-build-production-evals-in-60-minutes-2df4
site_name: devto
content_file: devto-stop-vibe-checking-your-ai-agents-how-to-build-pro
fetched_at: '2026-10-06T16:48:03.424430'
original_url: https://dev.to/googleai/stop-vibe-checking-your-ai-agents-how-to-build-production-evals-in-60-minutes-2df4
author: Frank Guan
date: '2026-09-30'
description: How do you currently test your AI agents? If you're like most developers building agentic... Tagged with ai, python, langchain, devops.
tags: '#ai, #python, #langchain, #devops'
---

How do you currently test your AI agents?

If you're like most developers building agentic workflows, you probably rely on the"vibe check": tweak a prompt, run a couple of manual queries, check if the output looks reasonable, and assume it's good to go.

Here's why that breaks down fast:

* Silent Regressions: A teammate submits a PR or tweaks a tool definition, and you have no way to know if performance improved or degraded.
* Cost & Latency Spikes: An agent gets trapped in a multi-turn retry loop, quietly burning thousands of tokens.
* The "Looks Right" Trap: Output can look perfectly well-written while omitting critical parameters or hallucinating key instructions.

In this episode of theAI Agent Clinic, Google Cloud engineer Dani Zamora and Matthew Feroz (Merge) tackle this challenge live:building an end-to-end, framework-agnostic evaluation pipeline in 60 minutes.

Check out the full walkthrough below:

### What We Cover in the Video

1. The Test Subject (DocsHound): Matt brings on DocsHound, an open-source LangGraph agent that scans GitHub issues and PRs to find documentation gaps and open automated PRs.
2. Framework-Agnostic Telemetry (OpenTelemetry + OpenInference): How to standardize multi-turn traces across any agent framework (LangGraph, CrewAI, AutoGen, ADK) with zero vendor lock-in.
3. The 3-Tier Metric Strategy: Why you shouldn't start with 50 metrics, and how to combine:* Managed core metrics: Trajectory quality, tool-calling correctness, and groundedness.
* Custom LLM judges: Rubrics tailored to formatting, code block enforcement, and actionability.
* Deterministic assertions & operational tracking: Syntax checks, latency, token usage, and API cost.
4. The 0.33 Quality Blind Spot: How the automated scorecard caught a 33% documentation quality failure that manual spot-checks completely missed.

### Jump Directly to Key Sections

If you want to skip straight to a specific part of the walkthrough:

* 00:00— Why "vibe checking" fails in production
* 02:11— Introducing DocsHound (LangGraph agent demo)
* 03:40— Standardizing traces with OpenTelemetry & OpenInference
* 05:51— The 60-minute eval challenge begins
* 06:47— Step 1: Mapping agent execution flow with Antigravity
* 11:18— Step 2: Scaffolding the open-source Agent-Eval toolkit
* 17:14— Balancing quality vs. latency vs. token cost
* 18:34— Step 3: Translating quality definitions into custom metrics
* 21:40— Step 4: Inspecting the scorecard & spotting the 0.33 failure
* 24:08— Why automated evals change how you build agents

### Open-Source Repositories & Resources

Follow along with the exact tools used in the video:

* 📺Full Video:Watch on YouTube (25 mins)
* 🛠️Agent-Eval Toolkit:github.com/google-cloud-tech/agent-eval
* 🐶DocsHound Agent Code:github.com/google-cloud-tech/docshound
* 📖Enterprise Agent Platform Docs:g.dev/cloud/agent-evaluation

👉Watch the full video above to see how to set up the eval pipeline step-by-step.If you have questions about instrumenting your own agent framework or setting up custom metrics, drop a comment below!

Enter fullscreen mode

Exit fullscreen mode

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse