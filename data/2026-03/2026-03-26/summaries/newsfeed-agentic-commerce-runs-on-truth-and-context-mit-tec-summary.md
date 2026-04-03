---
title: Agentic commerce runs on truth and context | MIT Technology Review
url: https://www.technologyreview.com/2026/03/25/1134516/agentic-commerce-runs-on-truth-and-context/
date: 2026-03-25
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-03-26T01:02:28.749407
---

# Agentic commerce runs on truth and context | MIT Technology Review

# Agentic commerce runs on truth and context – Summary

## The shift to agentic AI
- Agents move from merely assisting (providing links) to executing full transactions (e.g., booking a trip, handling payment) on behalf of users.  
- Speed is no longer limited to payment processing; the entire pre‑payment workflow (discovery, comparison, decision, authorization) must operate at machine speed.  
- Trust, not speed, becomes the critical constraint when decisions are automated.

## Role of master data management (MDM)
- MDM acts as the exchange layer that records who an agent represents, its permissions, and accountability when value moves.  
- Clear identity, authority, and accountability prevent market failures that stem from ambiguous ownership.

## New participant: the agent
- Commerce now involves three first‑class entities: buyer, merchant, and the agent acting for the buyer.  
- Key questions enterprises must answer:
  - How to uniquely identify the individual across channels and devices?  
  - How to define the agent’s permissions and limits?  
  - How to verify the correct merchant or supplier?  
  - Who bears liability if an agent’s action diverges from user intent?  
- Agents need deterministic signals; guessing leads to broken trust or unnecessary human confirmation.

## Why “good enough” data fails at machine speed
- Traditional tolerance for duplicate records, incomplete attributes, or delayed reconciliation is insufficient when agents act autonomously.  
- Predictable failure modes:
  - **Product truth** – inconsistent catalogs cause arbitrary or wrong selections.  
  - **Payee truth** – expanded payment methods require real‑time, accurate payee identification.  
  - **Identity truth** – multiple personal and work contexts must be distinguished to avoid blocking legitimate activity or approving risky actions.

## Context intelligence: the missing layer
- Beyond model capabilities (planning, reasoning), a real‑time system of authoritative context is required to answer:
  - Is this the right person?  
  - Is this the right agent with appropriate permissions?  
  - Is this the right merchant/payee?  
  - What constraints (budget, policy, risk, loyalty) apply now?  
- Design principles:
  1. Entity truth must be deterministic; probabilistic LLM outputs are unsuitable for financial decisions.  
  2. Context must travel at interaction speed and be portable across the value chain, pre‑resolved and packaged for lightweight execution.  
- Emerging approaches (e.g., tokenization, verifiable intent) encode credentials, agent identities, permissions, and user intent as cryptographically secure artifacts for instant verification.

## Recommended actions for leaders (next 12‑24 months)
1. Treat agents as governed identities—define onboarding, authentication, permissioning, monitoring, and retirement processes.  
2. Prioritize entity resolution where errors are most costly (payees, suppliers, personal vs. work identities, high‑volume product categories).  
3. Build a reusable context service accessible to all workflows and agents, avoiding duplicated identity reconstruction.  
4. Pre‑compute and compress signals upstream so runtime decisioning remains fast and predictable.  
5. Expand autonomy gradually, guided by governance frameworks, human‑in‑the‑loop safeguards for high‑risk actions, and measured accuracy metrics.

## Industry impact
- Agentic AI will extend beyond shopping carts to procurement, travel, claims, customer service, and finance operations.  
- Organizations that provide agents with clean identity, precise entity truth, and reliable context will compress decision cycles and eliminate manual steps.  
- Success hinges on treating entity truth and context as core infrastructure, not as after‑the‑fact data‑cleanup projects; trust becomes an architectural decision embedded in identity, context, and control.