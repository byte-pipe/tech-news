---
title: Claude Enterprise consumption guide | Anthropic Help Center
url: https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide
date: 2026-08-24
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-24T07:47:26.478748
---

# Claude Enterprise consumption guide | Anthropic Help Center

# Claude Enterprise consumption guide summary

## Why consumption management matters
- Claude Enterprise pricing is per‑seat and usage‑based; all users share a single consumption pool.  
- Surfaces such as Claude Code and Claude Cowork consume tokens far more quickly than standard chat.  
- Proactive spend limits and user education reduce waste and keep high‑value use cases funded.

## Token intensity across surfaces
- **Core Chat** – low intensity; token use grows with message length and conversation history.  
- **Claude Code** – high intensity; each session adds system prompts, file context, tool calls, and multi‑turn reasoning.  
- **Claude Cowork** – high intensity; agentic workflows and Skills generate many intermediate tokens that may be invisible to users.  
- **Other surfaces** – appear as separate products in Analytics and follow the same org, group, and per‑user limits:  
  - Claude for M365 (Excel, PowerPoint, Word, Outlook add‑ins)  
  - Claude Design (beta) – billed at standard API rates  
  - Claude in Chrome – runs as a Claude Cowork session  
  - Claude Tag (Slack, beta) – bills to the organization balance; DMs bill to the sender’s seat  

**Admin tip:** Include token‑intensity context in onboarding so users of Code or Cowork understand the higher cost.

## Role‑based access controls (RBAC)
- RBAC lets you group users and manage surface access and consumption budgets at the group level, which scales better than per‑user management.

### How to structure groups
- Base groups on job function and usage patterns, not on org hierarchy (e.g., “Engineering” vs. “Sales”).  
- Keep the number of groups low (4‑6 initially; avoid >8‑10).  
- Use groups to gate high‑intensity surfaces: only members of a designated group get Claude Code; others see only Chat and Cowork.  
- Groups can be created manually or synced from an identity provider.  
- Assign group‑level spend caps first, then override for outlier users if needed.

### Group spend management
- Review group consumption weekly during rollout, then monthly.  
- When a group nears its cap, investigate alternatives (e.g., suggest a lower‑cost model) before raising the limit.  
- Appoint a “group owner” or usage reviewer in each department; give them a custom role with Analytics (Can view) and optionally Billing (Can view) permissions.  
- **Governance tip:** Prioritize surface access gating before token‑level limits to avoid unexpected consumption spikes.

## Set spend limits
- Limits can be applied at three levels: organization, group, and individual user.  
- Recommended start: RBAC group‑level limits plus targeted user caps, keeping the org‑wide hard ceiling as a safety net.

### Org‑level spend limits
- Acts as a hard ceiling for all users and surfaces.  
- Hitting this limit disables the entire org, so use it sparingly; rely more on group and user limits for fine‑grained control.

### Group spend limits
- Assign a per‑user monthly spend limit to an entire group; all members inherit the same cap.  
- Precedence rules:  
  1. Individual limits override group limits.  
  2. If a user belongs to multiple groups, the “multi‑group spend limit” setting determines whether the higher or lower limit applies.  
  3. Org‑wide limit remains the ultimate ceiling.  
  4. No limit set anywhere means no cap.  
- Configure via **Organization settings → Usage → By group** (set a dollar amount or “Unlimited”).

### User‑level spend caps
- Set caps for individual accounts to reflect role‑specific needs (e.g., developers vs. marketers).  
- Best practices:  
  - Define consumption tiers (light, standard, power) before rollout.  
  - Start with conservative caps; it’s easier to raise a limit than to roll back an overage.  
  - Adjust caps based on actual usage and user requests.  

**Overall recommendation:** Combine RBAC‑driven group limits, targeted user caps, and occasional org‑level safeguards, while educating users about token intensity and monitoring usage regularly.