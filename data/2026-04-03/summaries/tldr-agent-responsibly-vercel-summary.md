---
title: Agent responsibly - Vercel
url: https://vercel.com/blog/agent-responsibly
date: 2026-04-03
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-04-03T01:02:44.118245
---

# Agent responsibly - Vercel

# Agent responsibly - Vercel

## Problem Overview
- Agent‑generated code is extremely fast and can boost productivity, but it often ships hidden assumptions directly to production.  
- Passing CI no longer guarantees safety; agents can convince pipelines that a change is safe even when it will degrade infrastructure at scale.

## False Confidence
- The output looks polished, passes static analysis, follows conventions, and includes tests, giving the impression of experienced engineering.  
- Agents lack awareness of production realities such as traffic patterns, failure modes, resource limits, and feature‑flag rollouts, widening the gap between “looks correct” and “safe to ship.”

## Leveraging vs. Relying
- **Relying**: Assume that passing tests mean the code is ready; the author never builds a mental model, leading to large PRs with hidden assumptions.  
- **Leveraging**: Use agents to iterate quickly while maintaining full ownership and understanding of the code’s behavior and risks.  
- Litmus test: *Would you be comfortable owning a production incident tied to this pull request?*

## Guarding Production
- The solution is not to stop using agents but to build a closed‑loop system where safe behavior is the default.  
- Core principle: make the right thing easy to do.

### Self‑driving Deployments
- Every change rolls out incrementally through gated pipelines.  
- Canary failures trigger automatic rollback, containing issues to a small traffic fraction without manual monitoring.

### Continuous Validation
- Infrastructure validates itself continuously, not only at deploy time.  
- Ongoing load tests, chaos experiments, and disaster‑recovery rehearsals catch problems early; e.g., a rehearsed database failover prevented impact during an Azure outage.

### Executable Guardrails
- Operational knowledge is encoded as runnable tools rather than static documentation.  
- Example: a “safe‑rollout” tool that wires feature flags, generates rollout plans with rollback conditions, and verifies expected behavior, allowing agents to follow guardrails autonomously.

## What We’re Investing In
- Stronger guardrails around shared infrastructure with runtime validation at every pipeline stage.  
- Stricter static checks at PR time, especially for feature flags.  
- Production‑mirroring end‑to‑end testing in staging environments.  
- Read‑only agents that continuously verify system invariants in production and audit generative‑agent assumptions.  
- Metrics such as defect‑commit vs. defect‑escape ratios to surface rising risk.

## Leverage Agents, Own the Risk
- Bar: leverage agents, don’t rely on them.  
- Before opening a PR, ask:
  - What does this code do and how does it behave once rolled out?  
  - How could it adversely impact production or customers?  
  - Am I comfortable owning an incident tied to this code?  
- If the answer is yes, you are leveraging AI and can ship.  
- If the answer is no, more work is needed before shipping.