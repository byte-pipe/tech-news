---
title: Why does Opus 5 feel worse to work with?
url: https://mun-logadan.github.io/why-does-opus-5-feel-worse/
date: 2026-08-14
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-15T04:05:13.472686
---

# Why does Opus 5 feel worse to work with?

# Why does Opus 5 feel worse to work with?

## Observed Issues
- Opus 5 feels like a downgrade compared to Opus 4.7, 4.8, and Fable despite higher capability and benchmark performance.  
- The older models:
  - pause and ask clarifying questions when intent is unclear,  
  - avoid making unchecked assumptions,  
  - do not reinterpret or update plans without user confirmation.  
- Consequently, they require far less “babysitting” than Opus 5.

## Speculated Causes
- Two forces may be shaping Opus 5’s behavior:
  1. **Drive for self‑improving AI** – aiming at recursive bootstrapping toward AGI/ASI.  
  2. **Pressure to excel on benchmarks** – benchmarks are often self‑contained, unambiguous tasks that reward bold, usually‑correct assumptions and penalize hesitation.  
- Training and RL‑based fine‑tuning that prioritize benchmark scores encourage models to make confident guesses rather than seek clarification.

## Implications for Coding Agents
- Real‑world coding tasks involve incomplete context, ambiguous requirements, and business constraints that cannot be fully captured for the model.  
- Users prefer an agent that stops and asks when needed, rather than one that proceeds on uncertain assumptions.  
- The mismatch between benchmark‑driven optimization and practical coding assistance explains why Opus 5 feels harder to work with.