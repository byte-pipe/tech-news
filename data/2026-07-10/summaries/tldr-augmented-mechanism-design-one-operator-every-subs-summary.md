---
title: Augmented Mechanism Design: One Operator, Every Substrate - Ethereum Research
url: https://ethresear.ch/t/augmented-mechanism-design-one-operator-every-substrate/25379
date: 2026-07-10
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-07-10T09:10:25.006388
---

# Augmented Mechanism Design: One Operator, Every Substrate - Ethereum Research

# Augmented Mechanism Design: One Operator, Every Substrate

## Claim
- Powerful mechanisms fail not because their core math is wrong, but because actors exploit gaps between the math and the surrounding social context.  
- Traditional response: replace the mechanism (e.g., ban bonding curves, accept MEV).  
- Augmented Mechanism Design (AMD) response: keep the mechanism and add a bounded, mathematically enforced invariant that eliminates the exploit without introducing an admin.

## Operator definition
- For a mechanism **M** with vulnerability **V**, an augmentation **A** produces **M' = A(M)** that preserves M’s core property while reducing V, with limited added complexity.  
- Four invariant flavors (often combined):
  1. **Structural** – makes the bad state unrepresentable (e.g., uniform clearing price, no per‑order price).  
  2. **Economic** – makes the attack unprofitable (e.g., bond + slash).  
  3. **Temporal** – removes speed advantage via time‑locks (commit‑reveal).  
  4. **Verification** – adds cryptographic attestations (commitments, Merkle roots, signatures).

## Substrate 1: Markets (deployed)
- **Augmented Bonding Curves** – add exit tributes and participation‑gated vesting; pump‑and‑dump becomes costly.  
- **Augmented Harberger Taxes** – loyalty multiplier, 72‑hour right of first refusal, superlinear portfolio tax, 20 % displacement premium; turns unilateral seizure into negotiation.  
- **Commit‑Reveal Batch Auctions** – 8 s commit, 2 s reveal, 50 % slash for non‑reveal, XOR‑seeded Fisher‑Yates shuffle; eliminates front‑run, sandwich, and info‑leak attacks.  
- Invariants used: structural (uniform price, XOR seed), temporal (commit/reveal windows), economic (slashes, taxes), compensatory (tributes, displacement premium).

## Substrate 2: Consensus (deployed invariant)
- Problem: stake‑weighted consensus can be captured by a plutocratic majority.  
- AMD fix: **structural anti‑concentration invariant** – finality requires each of two dimensions (capital and contribution) to supply at least half of its own weight before counting (MIN_DIM_BPS = 5000).  
- Result: neither capital nor contribution can finalize blocks alone; capture becomes unrepresentable.  
- Related work: ShapleyDistributor.sol reward attribution with on‑chain non‑additivity router; ongoing hardening against identity‑splitting attacks.

## Substrate 3: AI Systems (deployed harness)
- Problem: large language models are confidently wrong and degrade on long‑horizon tasks.  
- AMD fix: deterministic harness that gates trivial requests, verifies outputs, and routes uncertain cases to stronger tiers.  
- Invariants applied:
  - **Structural** – deterministic gate and schema.  
  - **Verification** – cheap checker and bounded retry loop.  
  - **Temporal/Economic** – budgets control when expensive higher‑tier models are invoked.  
- Evidence: similar patterns appear in Claude Code harness and other model‑wrapping systems.

## Why the name fits and is inevitable
- “Augmented Mechanism Design” precisely describes the cross‑substrate operator: preserve the original mechanism, add math‑enforced invariants, avoid admin trust points.  
- The pattern appears in markets, consensus, and AI, using the same four invariant types each time.  
- Formalization and broader adoption are expected; establishing the term now ties it to concrete deployed work.

## Status discipline
- **Claim:** AMD operator provides substrate‑independent protection via four invariant types.  
- **Status:** Deployed on three substrates (Solidity markets, Noesis consensus layer, Faraday/JARVIS AI harness); ongoing work on reward attribution hardening.