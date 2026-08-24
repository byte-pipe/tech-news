---
title: Proofcraft News - 2026
url: https://proofcraft.systems/news-2026/#2026-08-21
date: 2026-08-24
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-25T06:05:42.479303
---

# Proofcraft News - 2026

# Proofcraft News – 2026 Summary

## 21 Aug 2026 – seL4 confidentiality proof on AArch64
- Completed formal proof that seL4 on AArch64 enforces confidentiality, preventing unauthorized information leakage.  
- Builds on earlier functional‑correctness and integrity proofs; supported by NCSC.  
- Guarantees isolation of critical applications from non‑critical ones.

## 24 Jul 2026 – LICS ‘26 paper presentation
- “The Algebra of Iterative Constructions” presented at LICS 2026 (Lisbon).  
- Introduces an algebraic framework for reasoning about fixed‑point constructions, usable in Isabelle/HOL.  
- Result of a spontaneous collaboration between Gerwin Klein (Proofcraft) and Benjamin Kaminski, originating from the 2025 IFIP Working Group meeting.  
- Demonstrates the span of proof engineering from practical kernels to deep theory.

## 29 Jun 2026 – MCS seL4 verified for RISC‑V
- Verified functional correctness of the Mixed‑Criticality Systems (MCS) configuration of seL4 on RISC‑V.  
- First complete functional‑correctness proof for seL4 with MCS; a major step in the verification roadmap.  
- Port to Arm 64‑bit planned under DARPA’s PROVERS program.

## 1 Jun 2026 – Dynamic Domain Scheduler for seL4
- Implemented and proved a semi‑static domain‑scheduling API for seL4 (available in seL4 15.0.0).  
- Allows runtime changes to domain time slices, easing information‑flow enforcement and supporting SDK‑style development (e.g., Microkit).  
- Replaces the previous requirement for a fully static schedule compiled into the kernel.

## 21 May 2026 – June Andronick keynote at CDIS Spring Conference
- June Andronick (Proofcraft CEO) delivered a keynote on formal verification for cybersecurity and joined a panel on Digital Sovereignty at the CDIS spring conference (KTH, Stockholm).

## 28 Apr 2026 – Presentation at Cyberagentur Milestone Research Summit
- Gerwin Klein (Chief Scientist) and Martin Dehnel‑Wild (Kry10) presented the Dyvercon project, extending seL4 proofs to a static multikernel configuration for multi‑core performance.  
- Included a general introduction to formal verification and its real‑world applications.

## 17 Apr 2026 – Proofcraft sponsors seL4 Summit 2026
- Silver sponsor of the 2026 seL4 Summit (Vancouver, 1‑3 Sep).  
- Summit gathers industry, government, and academia around the world’s most assured OS kernel.

## 14 Apr 2026 – Five‑year anniversary of Proofcraft
- Celebrated five years since founding (April 2021).  
- Milestones: seL4 proofs now cover 100 % of supported Arm platforms (DARPA PROVERS); integrity proof for AArch64 completed; confidentiality proof nearing completion with NCSC support.  
- Ongoing large‑scale projects funded by DARPA, Cyberagentur, and NCSC.