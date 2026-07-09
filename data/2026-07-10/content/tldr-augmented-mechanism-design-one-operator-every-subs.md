---
title: 'Augmented Mechanism Design: One Operator, Every Substrate - Ethereum Research'
url: https://ethresear.ch/t/augmented-mechanism-design-one-operator-every-substrate/25379
site_name: tldr
content_file: tldr-augmented-mechanism-design-one-operator-every-subs
fetched_at: '2026-07-10T09:09:44.747377'
original_url: https://ethresear.ch/t/augmented-mechanism-design-one-operator-every-substrate/25379
date: '2026-07-10'
published_date: '2026-07-06T17:28:49+00:00'
description: 'Augmented Mechanism Design: One Operator, Every Substrate Positioning note, 2026-07-06. Builds on the formal paper “Augmented Mechanism Design: Protective Extensions for Pure Economic Mechanisms” (~/JARVIS/papers/augment&hellip;'
tags:
- tldr
---

# Augmented Mechanism Design: One Operator, Every Substrate

WGlynn

 July 6, 2026, 5:28pm
 

1

# Augmented Mechanism Design: One Operator, Every Substrate

Positioning note, 2026-07-06. Builds on the formal paper “Augmented Mechanism Design: Protective Extensions for Pure Economic Mechanisms” (~/JARVIS/papers/augmented-mechanism-design.md), which carries the math and the DeFi case studies. This note makes the larger claim the paper implies but does not state: the operator is substrate-independent, and it is now deployed across three of them.

## The claim

A powerful mechanism almost never fails because its core principle is wrong. It fails because a sophisticated actor exploits the gap between the mechanism’s mathematics and its social context. The usual response is replacement: the bonding curve enables pump-and-dump, so ban bonding curves; continuous trading enables MEV, so accept MEV as a cost of doing business.

Augmented Mechanism Design is the other response. Keep the mechanism. Add a bounded, math-enforced invariant that rules out the exploit by construction. Never add an admin, because an admin is a new trust point, which is a new capture surface, which is the failure you started with wearing a badge.

Written as an operator: for a mechanismMwith a known vulnerabilityV, there is an augmentationAsuch thatM' = A(M)preserves the core property ofMwhile shrinkingV, at bounded added complexity. The augmentation comes in four flavors, and real designs compose two to four of them:

* Structural: the bad state is unrepresentable. A uniform clearing price cannot be gamed per-order because there is no per-order price.
* Economic: breaking it is possible but unprofitable. A bond plus a slash makes the attack cost more than it pays.
* Temporal: a time-lock removes the speed advantage. Commit now, reveal later, and front-running has nothing to read.
* Verification: a cryptographic attestation makes the claim checkable. A commitment, a Merkle root, a signature.

The paper proves this across three market mechanisms. The point of this note is that the same operator, the same four invariant types, keep reappearing at layers of the stack that have nothing to do with DeFi. That recurrence is the thesis. It is also why the name is the right one.

## Substrate 1: markets (deployed)

This is the paper’s home ground. Three pure mechanisms, each augmented, each shipped as Solidity.

* Augmented Bonding Curves.The conservation law is untouched. Exit tributes and participation-gated vesting are added around it, so the curve still prices deterministically but pump-and-dump loses money and early capital binds to contribution.BondingCurveLauncher.sol.
* Augmented Harberger Taxes.Self-assessment still governs both tax and acquisition, so assets still flow to their highest-valued users. A loyalty multiplier, a 72-hour right of first refusal, a superlinear portfolio tax, and a 20 percent displacement premium turn a unilateral seizure into a negotiation and make hoarding irrational.VibeNames.sol.
* Commit-Reveal Batch Auctions.Orders execute at an efficient price, now a uniform clearing price over a batch. An 8-second commit, a 2-second reveal, a 50 percent slash on non-reveal, and a Fisher-Yates shuffle seeded by the XOR of every revealed secret remove the entire front-run, sandwich, and information-leak class.CommitRevealAuction.sol,DeterministicShuffle.sol.

The augmentation types in play: structural (uniform price, XOR seed), temporal (commit and reveal windows, grace period), economic (slash, portfolio tax), compensatory (displacement premium, tributes to the commons). None of the three mechanisms was replaced. Each was armored.

## Substrate 2: consensus (deployed invariant)

Consensus is not a market, but the same failure and the same fix apply. A stake-weighted consensus lets capital finalize blocks. The exploit is plutocratic capture: enough capital finalizes alone, and contribution has no say.

The replacement answer would be to bolt on a committee or a foundation veto, which is an admin, which is capture with extra steps. The augmentation answer is a structural anti-concentration invariant. In the Noesis node, finality is a weighted mix of a capital dimension and a contribution dimension, and each dimension must independently supply at least half of its own weight before it counts. The constant isMIN_DIM_BPS = 5000(node/src/runtime.rs:596): neither axis can finalize on its own, so capital cannot finalize without contribution’s consent and contribution cannot finalize without capital’s. It is a per-dimension floor, not a cap, and it makes capture unrepresentable rather than merely punished.

That is the Harberger anti-concentration move ported off the market and onto the consensus layer: preserve the mechanism, add one structural invariant, refuse the admin. The same paper’sShapleyDistributor.solreward attribution ships alongside it, with an on-chain non-additivity router (ShapleyAttributionHook.sol, committed on public master) that takes an additive fast path when contributions are separable and escalates to exact Shapley when they are not. Hardening the reward weighting so the fairness floor cannot be farmed by identity-splitting is active work as of this writing, honestly still in flight rather than shipped.

## Substrate 3: AI systems (deployed harness)

A large language model is a powerful mechanism with a well-known vulnerability: it is confidently wrong in ways that are hard to catch, and it degrades on long-horizon tasks. The replacement answer is to wait for a bigger model. The augmentation answer is to keep the model and wrap it in deterministic structure that it cannot corrupt.

That is exactly what a harness is. A deterministic gate resolves the trivial requests so the model never touches them and can never get them wrong. A cheap structural verifier checks the model’s output and drives a bounded retry with the exact error. A confidence probe, self-consistency across samples, decides when the model does not know and routes those cases to a stronger tier. The moat is the delegation layer, and the base model is a swappable commodity behind it. This is the Faraday local-model harness and the wider JARVIS substrate, and it is the four invariant types again: structural (the gate, the schema), verification (the checker), with temporal and economic budgets governing when the expensive tier fires.

The strongest evidence that this is a real pattern and not a private preference is that the people who build the model converged on it independently. The Claude Code harness is, in effect, a while-loop that asks the model, runs a tool, and repeats, with the overwhelming majority of the system being deterministic scaffolding and a thin slice touching the model. That is augment-don’t-replace, shipped by the lab whose model it wraps. When the mechanism’s own authors armor it the same way you do, the operator is not a metaphor.

## Why the name is right, and why it is inevitable

A term earns adoption when it names something real and useful. “Augmented Mechanism Design” names a real cross-substrate operator: preserve the mechanism, add a bounded math-enforced invariant, refuse the admin. It shows up in markets, in consensus, and in AI systems, with the same four invariant types each time. Because it is real and useful, someone will eventually formalize and name it. That is not a risk to hedge, it is a schedule to beat.

The only thing in our control is what a search for the term resolves to. It can resolve to a bare dictionary definition that anyone could have written, or it can resolve to a body of deployed work that already uses the term consistently across three substrates. The move is to weld the name to the receipts at the point of coinage, which is what this note and the paper it extends are for. Lab adoption of the phrase would be a multiplier on top. It is not the plan, because it is not ours to decide.

## Status discipline

Claim

Status

AMD operator and four invariant types

formalized (paper)

ABC / AHT / CRBA augmentations

built (deployed or deployment-ready Solidity)

Shapley attribution + non-additivity router

built (on public master)

Scale-invariant, sybil-neutral reward weighting

in flight (landing now, not yet shipped)

Consensus anti-concentration floor (
MIN_DIM_BPS = 5000
)

built (live constant, verified in source)

AI harness (gate + verifier + escalation)

built (Faraday local harness; JARVIS substrate)

Claude Code convergence on the same shape

observed (external validation)

Cross-substrate universality as a formal result

open (this note argues it; it is not proven)

Never rounded up. The universality claim is a design argument backed by three deployed instances, not a theorem. The formal operator, its compositional properties, and the market case studies live in the paper.