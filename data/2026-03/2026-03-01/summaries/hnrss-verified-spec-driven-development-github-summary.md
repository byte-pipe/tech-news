---
title: Verified Spec-Driven Development · GitHub
url: https://gist.github.com/dollspace-gay/d8d3bc3ecf4188df049d7a4726bb2a00
date: 2026-02-28
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-01T10:16:23.904849
---

# Verified Spec-Driven Development · GitHub

# Verified Spec-Driven Development Summary

## Overview
- VSDD combines Spec‑Driven Development (SDD), Test‑Driven Development (TDD), and Verification‑Driven Development (VDD) into a single AI‑orchestrated workflow.
- Specs define **what** the software must do and serve as the source of truth.
- Tests enforce **how** the specs are satisfied (red → green → refactor).
- An adversarial verification step checks that nothing was missed, forcing the code to meet provable properties.
- AI models handle spec authoring, test generation, code implementation, and verification; the human developer provides strategic direction and final approval.

## Toolchain Roles
- **The Architect** – Human developer; provides vision, domain expertise, and signs off on specs; resolves disputes.
- **The Builder** – AI model (e.g., Claude); writes specifications, generates tests, implements code, and refactors under TDD constraints.
- **The Tracker** – Chainlink; creates a hierarchical issue structure (epics → issues → sub‑issues) linking each spec, test, and implementation to a “bead.”
- **The Adversary** – Hyper‑critical AI reviewer (e.g., Sarcasmotron/Gemini); repeatedly critiques specs, tests, and code to expose ambiguities, missing edge cases, and verification gaps.

## VSDD Pipeline

### Phase 1 – Spec Crystallization
1. **Behavioral Specification**
   - Define a functional contract with preconditions, postconditions, and invariants.
   - Provide precise interface definitions (input, output, error types).
   - List edge cases (null, empty, max size, negative, Unicode, concurrency).
   - State non‑functional requirements (performance, memory, security).

2. **Verification Architecture**
   - Identify provable properties (safety invariants, overflow avoidance, termination, access‑control guarantees).
   - Create a purity boundary map separating deterministic, side‑effect‑free core from effectful shell (I/O, network, DB).
   - Choose appropriate formal verification tools (Kani, CBMC, Dafny, TLA+, etc.) and note their architectural constraints.
   - Draft formal property specifications (proof harnesses, contracts, invariants) alongside the natural‑language spec.

3. **Spec Review Gate**
   - Human architect and the Adversary review the complete spec and verification plan.
   - The Adversary checks for ambiguous language, missing edge cases, hidden assumptions, contradictions, improper purity boundaries, and mismatches with selected verification tools.
   - Iteration continues until no legitimate holes are found.

4. **Chainlink Integration**
   - Each spec item becomes a Chainlink issue; sub‑issues are generated for individual contract clauses, edge cases, and non‑functional requirements, ensuring traceability throughout the pipeline.

*(Subsequent phases (test generation, implementation, adversarial verification, refactoring) follow the same AI‑human gated pattern, but are not detailed in the provided excerpt.)*
