---
title: "Stop \"Vibe Checking\" Your AI Agents: How to Build Production Evals in 60 Minutes - DEV Community"
url: https://dev.to/googleai/stop-vibe-checking-your-ai-agents-how-to-build-production-evals-in-60-minutes-2df4
date: 2026-09-30
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-06T16:49:00.804793
---

# Stop "Vibe Checking" Your AI Agents: How to Build Production Evals in 60 Minutes - DEV Community

# Stop "Vibe Checking" Your AI Agents: How to Build Production Evals in 60 Minutes

## Problem Overview
- Many developers test agents by manually tweaking prompts, running a few queries, and judging output by appearance (“vibe check”).
- This approach fails in production because:
  - Silent regressions go unnoticed when code changes or tool definitions are updated.
  - Cost and latency spikes can occur when agents enter retry loops, burning thousands of tokens.
  - Outputs may look well‑written while omitting critical parameters or hallucinating instructions.

## Video Walkthrough Highlights
- Google Cloud engineer Dani Zamora and Matthew Feroz (Merge) build a framework‑agnostic evaluation pipeline in 60 minutes.
- **Test subject:** DocsHound, an open‑source LangGraph agent that scans GitHub issues/PRs for documentation gaps and opens automated PRs.
- **Telemetry:** Use OpenTelemetry + OpenInference to standardize multi‑turn traces across any agent framework (LangGraph, CrewAI, AutoGen, ADK) without vendor lock‑in.
- **Metric strategy:** Combine managed core metrics, custom LLM judges, and deterministic assertions for a balanced evaluation.
- **Blind spot discovery:** Automated scorecard identified a 33 % documentation quality failure that manual spot‑checks missed.

## 3‑Tier Metric Strategy
- **Managed core metrics**
  - Trajectory quality
  - Tool‑calling correctness
  - Groundedness
- **Custom LLM judges**
  - Rubrics for formatting, code‑block enforcement, and actionability
- **Deterministic assertions & operational tracking**
  - Syntax checks
  - Latency measurements
  - Token usage
  - API cost monitoring

## Key Sections (timestamps)
- 00:00 – Why “vibe checking” fails in production
- 02:11 – Introducing DocsHound (LangGraph demo)
- 03:40 – Standardizing traces with OpenTelemetry & OpenInference
- 05:51 – The 60‑minute eval challenge begins
- 06:47 – Step 1: Mapping agent execution flow with Antigravity
- 11:18 – Step 2: Scaffolding the open‑source Agent‑Eval toolkit
- 17:14 – Balancing quality vs. latency vs. token cost
- 18:34 – Step 3: Translating quality definitions into custom metrics
- 21:40 – Step 4: Inspecting the scorecard & spotting the 0.33 failure
- 24:08 – Why automated evals change how you build agents

## Open‑Source Repositories & Resources
- Full video (YouTube, 25 min)
- Agent‑Eval Toolkit: `github.com/google-cloud-tech/agent-eval`
- DocsHound agent code: `github.com/google-cloud-tech/docshound`
- Enterprise Agent Platform documentation: `g.dev/cloud/agent-evaluation`

## Takeaways
- Relying on manual “vibe checks” is unsafe for production‑grade agents.
- A lightweight, framework‑agnostic eval pipeline can be assembled in an hour.
- Combining core metrics, LLM judges, and deterministic checks provides comprehensive visibility into agent performance, cost, and reliability.