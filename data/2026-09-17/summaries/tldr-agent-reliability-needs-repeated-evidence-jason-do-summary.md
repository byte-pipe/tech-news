---
title: Agent Reliability Needs Repeated Evidence | Jason Doyle
url: https://jasondoyle.ie/whitepapers/agent-reliability-needs-repeated-evidence
date: 2026-09-17
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-17T05:39:41.203726
---

# Agent Reliability Needs Repeated Evidence | Jason Doyle

# Agent Reliability Needs Repeated Evidence | Jason Doyle

## Executive summary
- An agent can show a high average success score yet be unreliable when the same task is repeated.
- IBM Research’s AppWorld benchmark showed a ReAct agent with GPT‑4.1 achieving **Mean@5 = 77.4 %** but **Pass^5 = 53.0 %**, a 24.4 percentage‑point “consistency gap.”
- Production systems now expect agents to perform multi‑step work (updating records, sending messages, reconciling accounts, etc.) over days or weeks; a single averaged score does not reveal whether a given intent will succeed each time.
- Repeated success is valuable evidence, but reliability also requires outcome quality, robustness, predictability, and safety.
- Simple probability expressions (e.g., \(p^n\)) can be misleading because real agent trajectories involve correlated failures, variable decision risk, and possible recovery.
- Proposed operating model:
  1. Measure a **reliability profile** rather than a single score.
  2. Precisely define the profile’s subject (task class, model version, environment, dependencies, intervention policy, time window).
  3. Report both average outcome yield and strict repeated‑success metrics.
  4. Track consistently wrong outcomes separately.
  5. Stratify results by task structure and operational consequence.
  6. Define an operating boundary where lower and upper confidence bounds meet policy.
  7. Apply deterministic validation, replay, checkpointing, human approval, or refusal outside that boundary.
  8. Use observed SLO misses over time to adjust the amount of autonomous work admitted.
- IBM’s Consistency Analyzer can resample a recorded trajectory, identify “flip‑prone” decisions, and improve Pass^5 (e.g., from 53.0 % to 69.0 % on the same task set). Transferability to other domains must still be validated.
- The paper’s practical contribution: an **agent reliability profile**, an **operating‑boundary record**, and an **intervention checklist** that together turn repeated evaluation into a deployment decision without over‑relying on repeatability alone.

## 1. A success rate answers one question
- **Success rate** tells the fraction of sampled runs that produced an acceptable outcome; it is a useful starting point but insufficient for repeated intents.
- IBM defines three metrics for \(k\) runs:
  - **Pass@k** – at least one of the \(k\) runs succeeds.
  - **Mean@k** – average fraction of successful runs.
  - **Pass^k** – all \(k\) runs succeed (strict repeated‑success condition).
- Example from IBM’s 168‑task AppWorld evaluation (ReAct + GPT‑4.1):
  - Mean@5 = 77.4 %
  - Pass^5 = 53.0 %
  - Consistency gap = 24.4 pp
- For the harder task tier:
  - Mean@5 = 61.9 %
  - Pass^5 = 31.7 %
  - Consistency gap = 30.2 pp
- Mean@k reflects average yield; Pass^k reveals how often an intent can be trusted to succeed repeatedly.
- Neither metric alone predicts the probability of success for a specific future intent because tasks vary in difficulty and latent success probabilities.

## 2. The consistency gap needs careful interpretation
- **Consistency gap(k) = Mean@k – Pass^k** quantifies the drop from average success to strict repeatability.
- **Normalized consistency(k) = Pass^k / Mean@k** adjusts for overall capability; low‑capability systems cannot exhibit large absolute gaps.
- These metrics are informative but do not constitute a full reliability contract.

### 2.1 Pass^k changes with k
- If each run succeeds independently with probability \(p\), then \(Pass^k = p^k\); increasing \(k\) tightens the success criterion without changing the underlying capability.
- Example: \(p = 0.9\) → Pass^3 ≈ 72.9 %, Pass^5 ≈ 59.0 %.
- Reported Pass^k values must always include the corresponding \(k\) and the repeat protocol.
- Comparing observed Pass^5 (53.0 %) to the naïve independent‑run model using the aggregate Mean@5 (0.774) yields \(0.774^5 ≈ 27.8 %\). The higher observed Pass^5 suggests a heterogeneous task population (many always‑pass or always‑fail tasks, fewer borderline cases).

### 2.2 Benchmark aggregation mixes task populations
- Aggregated Mean@k and Pass^k blend easy, medium, and hard tasks, obscuring how reliability varies across sub‑populations.
- Stratifying by task difficulty, structure, and operational impact is essential for meaningful reliability assessment.