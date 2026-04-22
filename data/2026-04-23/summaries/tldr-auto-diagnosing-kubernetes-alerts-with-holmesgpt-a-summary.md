---
title: Auto-diagnosing Kubernetes alerts with HolmesGPT and CNCF tools | CNCF
url: https://www.cncf.io/blog/2026/04/21/auto-diagnosing-kubernetes-alerts-with-holmesgpt-and-cncf-tools/
date: 2026-04-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-23T09:47:17.212947
---

# Auto-diagnosing Kubernetes alerts with HolmesGPT and CNCF tools | CNCF

# Auto‑diagnosing Kubernetes alerts with HolmesGPT and CNCF tools

## Why we built the pipeline
- STCLab’s two‑person SRE team manages multiple high‑traffic Amazon EKS clusters with full observability (OpenTelemetry → Mimir, Loki, Tempo) and Robusta‑enriched Prometheus alerts.
- Manual triage of each alert took 15–20 minutes (checking pods, querying Prometheus, digging Loki, pulling traces).
- Goal: automate the first investigation pass and post results in the same Slack thread.

## HolmesGPT: letting the LLM decide what to investigate
- Chosen from CNCF Sandbox for its ReAct pattern: LLM reads an alert, selects a tool, processes the result, then decides the next step.
- Investigation path is dynamic, not scripted, adapting to the data available in each namespace.
- Runbooks are stored as markdown with a metadata header (scope, tools, cautions) that HolmesGPT reads early to know which tools to use or skip.

## Making it work with Robusta
- Custom Python playbook (~200 lines) bridges Robusta and HolmesGPT.
- Finds the correct Slack thread after the initial alert, posts investigation results as a reply.
- Deduplicates alerts at the workload level (30‑minute suppression) and maps namespace‑based Slack channels.

## Runbooks changed everything
- Without runbooks the model guessed, called irrelevant tools, and exhausted its step budget.
- Adding exclusion rules (“no Loki, no Tempo, no Istio”) reduced tool calls from ~16 to 2 per investigation.
- Controlled test on a ClickHouse handshake alert:
  - With runbooks: 3–4 tool calls, accurate pattern match.
  - Without runbooks: 20+ steps, unrelated hypotheses.
- Maintained seven runbooks organized by namespace and alert type; they now drive investigation quality more than model upgrades.

## The model journey
- Tested seven models on self‑hosted Spot GPUs (KubeAI) and managed APIs via VPC endpoints.
- Early self‑hosted models (7B, 9B) failed to produce valid tool calls; 14B suffered from evictions and long cold‑starts.
- Managed APIs had compatibility issues; only one model family satisfied all requirements (Korean output, Slack formatting, runbook retrieval, cross‑cluster log correlation).
- Contributed a three‑line upstream fix for pod identity authentication (PR #1850).
- Current hybrid setup: self‑hosted in staging, managed API in production.
- Cost ≈ $0.04 per investigation (~$12 / month); pipeline and runbooks unchanged across backends.

## What actually mattered
- Daily raw alerts ≈ 40 → deduplicated to ≈ 12 unique investigations.
- Engineers read threaded summaries in < 2 minutes vs. 15–20 minutes manual triage.
- ~40 % of investigations resolve automatically (OOMKilled, ImagePullBackOff, known patterns).
- Key lessons:
  - Runbooks provide more impact than model upgrades (score 4.6/5 with runbooks vs. 3.6/5 without).
  - Glue code (the 200‑line playbook) is essential for timing, deduplication, routing, and thread matching.
  - Design pipelines to allow easy model swaps; keep the playbook as the stable core.

## What’s next
- Integrate Inspektor Gadget (CNCF) to feed eBPF‑level network metrics (TCP retransmits, latency) into Prometheus, giving HolmesGPT richer data without changing architecture.

## About STCLab
- Builds high‑performance online traffic‑management software.
- Products: NetFUNNEL (Virtual Waiting Room) and BotManager (bot mitigation) serving millions of concurrent users in 200+ countries.

## Contact
- grace@stclab.com  
- https://stclab.com