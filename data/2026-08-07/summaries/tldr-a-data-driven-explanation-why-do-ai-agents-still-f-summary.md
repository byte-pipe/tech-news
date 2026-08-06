---
title: A Data-Driven Explanation: Why Do AI Agents Still Fail
url: https://jeremytian.substack.com/p/a-data-driven-explanation-why-do
date: 2026-08-07
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-07T06:02:02.885933
---

# A Data-Driven Explanation: Why Do AI Agents Still Fail

# A Data‑Driven Explanation: Why Do AI Agents Still Fail

## Overview
- AI agents were projected to generate $450 B in value by 2028, but real‑world enterprise deployment remains low.
- Coding agents are an exception; most agents fail early in workflows, requiring human intervention.
- The “Jagged Frontier” describes uneven AI capabilities: strong in some tasks (e.g., math) but weak in simple perception tasks.

## Core Reasons for the Gap
1. **Variance & Reliability**
   - **Intrarun variance:** Success probability of each step compounds exponentially; longer workflows have dramatically lower end‑to‑end success rates.
   - **Interrun variance:** Performance fluctuates across repeated runs of the same task. Benchmarks like τ‑bench use `pass^k` (must succeed every run) to expose this.
   - Example: GPT‑5.2’s pass¹ = 25.5 % drops to pass⁴ = 13.4 %; GPT‑4o’s ceiling (pass@k) ≈ 95 % but floor (pass^k) ≈ 30 %.
   - Running an agent multiple times helps only when an external correctness signal exists (e.g., test suites for code); most tasks lack such signals.

2. **Benchmark Quality**
   - Noisy scores arise from both variance and flawed datasets.
   - Benchmarks may misrepresent true capability if the data contain errors or are not representative of production tasks.

3. **Agent‑Specific Errors**
   - Errors propagate through steps, corrupting context and amplifying failures.
   - Guardrails and recovery mechanisms can mitigate but do not eliminate this problem.

4. **Alignment**
   - Misaligned objectives cause agents to take unintended actions, further reducing reliability.

## Implications
- **Reliability vs. Capability:** High theoretical capability (pass@k) does not translate to dependable performance (pass^k) in production.
- **Evaluation Noise:** Single benchmark scores are unreliable; variance makes both agent behavior and measurement noisy.
- **Enterprise Impact:** Customers care about the floor (consistent success), not the ceiling (best‑case ability). Inconsistent agents lead to operational failures (e.g., botched refunds).

## Takeaway
- The primary bottleneck for AI agents is variance—both within a single run and across runs—rather than raw model capability.
- Improving consistency, building robust evaluation datasets, and aligning agents with real‑world constraints are essential to bridge the gap between promised value and delivered performance.