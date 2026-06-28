---
title: Fintech Engineering Handbook
url: https://w.pitula.me/fintech-engineering-handbook/
date: 2026-06-27
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-28T18:01:39.896375
---

# Fintech Engineering Handbook

# Fintech Engineering Handbook

## Introduction
- Describes essential software‑engineering patterns for systems where money is the core focus.  
- Can be read wholly for a complete view or in sections to solve specific problems.  
- Intended as a living document; contributions are encouraged.

## Intended Audience
- **New entrants to fintech** – to learn domain concepts and trustworthy money‑system patterns.  
- **Experienced fintech professionals** – as a reference and shared vocabulary for problem solving.  
- **Non‑fintech engineers** – to understand how building for money differs from typical software.

## Core Principles
1. **No invented data** – prevent duplicate or arbitrary balance updates; enforce idempotency, deduplication, and reconciliation.  
2. **No lost data** – persist every monetary event; use full precision, at‑least‑once delivery, event sourcing, audit trails, and immutability.  
3. **No trust** – never assume external providers, internal components, or the world are correct; verify webhooks, cross‑check sources, and fail loudly on broken assumptions.

## Representing Money
### Precision Handling
- Four main approaches:  
  1. **Floating‑point** – fast but prone to unpredictable precision loss; generally unsuitable.  
  2. **Arbitrary precision (e.g., BigDecimal)** – precise control over rounding; good for intermediate calculations like FX or pricing.  
  3. **Minor‑units (integer in smallest unit)** – store amounts as integers (e.g., €12.34 → 1234); works for fiat and crypto (with asset‑specific decimals, may need arbitrary‑width integers).  
  4. **Rational numbers** – eliminates precision loss but slower and harder to convert; requires custom types or libraries.  
- Storage and computation can be decoupled (e.g., integer storage with BigDecimal for calculations).  
- Serialize money as a string (“12.34”) or as an integer in the smallest unit; avoid raw JSON numbers to prevent floating‑point issues.  
- **Principle reinforced:** No lost data – wrong representation silently drops unrecoverable precision.

### Rounding Strategies
- Rounding is unavoidable and must be explicit for divisions, conversions, fees, interest, or precision changes.  
- Business‑driven decisions dictate rounding direction (down‑rounding to avoid overspending, half‑even for statistical fairness, etc.).  
- Preserve full precision as long as possible; round only at persistence or presentation boundaries.  
- Rounding can break sums; may require a dedicated rounding account to reconcile residuals.  
- **Principles reinforced:**  
  - No lost data – track residuals instead of discarding them.  
  - No invented data – rounding must never create money.

### Currency Handling
- Pair amount with currency in a dedicated type (struct/class/record) to avoid mismatches.  
- Disallow arithmetic across different currencies; require explicit conversion with controlled rates.  
- Maintain a validated, controlled list of allowed currency codes; reject arbitrary codes at system boundaries.  
- Fiat codes are unique identifiers; crypto assets need richer identifiers (network, contract address, etc.).  
- Currency metadata (symbol, precision, name) is mainly for display, not core logic.  
- Recognize that pegged, bridged, or wrapped crypto assets are distinct from their underlying assets.  
- **Principles reinforced:** No trust (validate currency) and No invented data (treat distinct assets separately).

### FX Rates
- Rates are directional; EUR/USD ≠ inverse of USD/EUR due to bid/ask spreads.  
- Time relevance:  
  - **Current‑time rate** – for immediate valuation or transaction simulation.  
  - **Value‑date rate** – for tax calculations or value changes on a specific future date.  
- Two rate categories:  
  1. **Transactional rate** – actual rate used in a conversion; derived from original and resulting amounts, not stored directly.  
  2. **Reference rate** – mid‑market or central‑bank rate for valuation and equivalence; not a tradable price.  
- No single canonical rate; rates vary across markets and providers.