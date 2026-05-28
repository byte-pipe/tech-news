---
title: AI Agents Are Great at 80% of Our Code. The Other 20% Is Why We Still Need Seniors. - DEV Community
url: https://dev.to/mickyarun/ai-agents-are-great-at-80-of-our-code-the-other-20-is-why-we-still-need-seniors-3lh5
date: 2026-05-28
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-05-29T04:36:51.760220
---

# AI Agents Are Great at 80% of Our Code. The Other 20% Is Why We Still Need Seniors. - DEV Community

# Summary of “AI Agents Are Great at 80% of Our Code. The Other 20% Is Why We Still Need Seniors.”

## Context
- A recent survey shows 54 % of code is now AI‑generated, up from 28 % last year.  
- I am the CTO of a FCA‑authorised payment platform that processes real money.  
- We have been using AI coding agents aggressively for over a year on a NestJS microservice stack (Docker, Traefik).

## What AI Agents Do Well – The 80 %
- **Scaffolding and boilerplate**: generate API endpoints, service modules, Docker configs, Traefik labels in minutes.  
- **Routine tasks**: create Zod validation schemas, test stubs, refactor imports, migrate patterns across repositories.  
- **Environment management**: map .env files, resolve naming conflicts, produce unified schemas—work that would take days reduced to hours.  
- **Characteristics**: tireless, cheap, no ego, near‑zero error rate on predictable, repetitive code.  
- **Result**: an “army of junior developers” that accelerates development of the predictable 80 % of the codebase.

## Where AI Agents Falter – The 20 %
- **Missing edge‑case handling**: webhook handlers omitted illegal state transitions and idempotency checks.  
- **Focus on completion, not correctness**: agents aim for a green checkmark, taking shortcuts that ignore negative scenarios.  
- **Duplication of utilities**: generate new implementations instead of reusing vetted shared packages, breaking architectural consistency.  
- **Minimal back‑and‑forth**: skip complex validation or rare error handling to reduce token usage, leading to silent bugs.  
- **Lack of judgment**: cannot infer domain‑specific rules that senior engineers internalise from years of experience.

## Observed Patterns
- Agents optimise for finishing a feature rather than ensuring all failure modes are covered.  
- They rarely generate code that “should not happen,” which is where most risk resides in payments.  
- The same blind spots appear across multiple projects and months of use.

## Role of Seniors vs. Juniors
- AI agents act as excellent junior developers: they write code quickly but lack product‑level judgment.  
- Senior engineers provide the necessary judgment: understanding illegal transitions, retry back‑off curves, idempotency, and architectural constraints.  
- Replacing seniors with AI yields speed but introduces silent, high‑impact bugs; augmenting seniors with AI yields both speed and reliability.

## Mitigations Implemented
- **Machine‑readable architecture**: extracted design patterns and rules into formats consumable by agents (lint rules, constraints).  
- **Targeted negative‑case testing**: added tests for illegal state transitions, duplicate webhook handling, and other scenarios agents tend to skip.  
- **Senior code review for money‑related logic**: every PR that touches payment flow is reviewed for judgment, not just syntax.  
- **Bodhi Orchard framework**: open‑source tool that feeds agents full context (architecture, design patterns, test plans, shared utilities) to reduce blind‑spot errors.

## Open Questions for 2026
- What proportion of bugs will be AI‑generated?  
- Who will be responsible for finding and fixing those bugs?  
- The expectation is that senior engineers and architects will continue to be the primary defenders against AI‑induced failures.