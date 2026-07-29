---
title: Discovering cryptographic weaknesses with Claude \ Anthropic
url: https://www.anthropic.com/research/discovering-cryptographic-weaknesses
date: 2026-07-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-29T12:29:20.829675
---

# Discovering cryptographic weaknesses with Claude \ Anthropic

# Discovering cryptographic weaknesses with Claude

## Summary
- Researchers used Claude Mythos Preview to find new attacks on two cryptographic algorithms:
  - An improved key‑recovery attack on the post‑quantum signature scheme **HAWK**, cutting its effective key size roughly in half.
  - A faster attack on a round‑reduced version of **AES**, speeding up previous attacks by 200–800×.
- Both attacks target mathematical weaknesses in the algorithms themselves, not implementation bugs.
- The findings do not affect deployed systems: HAWK is only a candidate scheme and the AES attack applies to a weakened variant.
- The work demonstrates that frontier AI models can autonomously assist cryptanalysis, prompting the creation of **CryptanalysisBench** for broader evaluation.
- Responsible disclosure was followed, with coordination with NIST, the HAWK authors, and academic partners.

## Introduction
- Claude Mythos Preview had previously shown the ability to locate implementation bugs in cryptographic libraries.
- The new research shows the model can also discover **mathematical flaws** in the underlying algorithms.
- Cryptographic algorithms protect everyday online activities (digital signatures, encrypted traffic); flaws could endanger billions of users if exploited in production.

## Improved key‑recovery attack on HAWK
- **HAWK** is a third‑round NIST candidate for post‑quantum digital signatures, based on the Lattice Isomorphism Problem.
- Mythos identified a previously unknown **non‑trivial automorphism** in the lattice, enabling a faster enumeration attack.
- The attack reduces the effective security level by a factor of two, meaning key sizes would need to be doubled to retain the same security margin.
- Development timeline: ~60 hours of work with limited human guidance; cost ≈ $100 k in API usage.
- Process involved:
  - Extensive literature review.
  - Mathematical reasoning and computational experiments using Python and Sage.
  - An end‑to‑end verification pipeline built by the model to confirm correctness.

## Faster attack on round‑reduced AES
- AES is the most widely used symmetric cipher; researchers study weakened versions to gauge robustness.
- Mythos discovered a method that eliminates one of the attacker’s guess steps, accelerating the best known attacks by 200–800×.
- The attack applies only to a **reduced‑round** variant and does not compromise the full AES specification.
- This result was generated fully autonomously after a scaffold was provided by a human researcher; cost also ≈ $100 k in API usage.

## CryptanalysisBench
- To enable the community to evaluate LLM cryptanalytic abilities, Anthropic partnered with ETH Zurich, Tel Aviv University, and University of Haifa.
- The benchmark bundles a variety of ciphers and provides a standardized testing framework for future AI‑driven cryptanalysis research.

## Responsible disclosure and collaboration
- Findings were vetted with academic experts and shared in advance with U.S. government and industry partners.
- The HAWK attack was disclosed to its authors in June and coordinated with the public NIST mailing list at the time of publication.
- All work adhered to responsible disclosure practices throughout the research cycle.

## Implications
- While the attacks have no immediate practical impact, they illustrate that advanced AI models can accelerate cryptographic research and stress‑testing.
- The ability to uncover algorithmic weaknesses may influence future design, evaluation, and standardization processes for post‑quantum and classical cryptography.