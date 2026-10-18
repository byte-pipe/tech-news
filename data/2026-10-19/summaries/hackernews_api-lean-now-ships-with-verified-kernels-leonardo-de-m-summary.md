---
title: Lean Now Ships with Verified Kernels — Leonardo de Moura
url: https://leodemoura.github.io/blog/2026-10-15-lean-now-ships-with-verified-kernels/
date: 2026-10-16
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-19T09:16:52.869322
---

# Lean Now Ships with Verified Kernels — Leonardo de Moura

# Lean Now Ships with Verified Kernels

## Overview
- AI agents have exposed vulnerabilities in Lean’s proof‑checker kernel.
- The team is strengthening the official kernel, adding new kernels, and providing tools to recheck developments with external kernels.
- `lake check` (available from Lean 4.35.0) exports a project and rechecks it with `leanchecker` inside a sandbox; the sandbox can be disabled with `--inadvisably-no-sandbox`.

## New Kernels
- Four additional kernels are shipped: **nanoda**, **lean4lean**, **con‑leche**, and **con‑ron**.
- `lake check --paranoid` runs the development against all kernels, including a hardened‑memory‑allocator variant of the official kernel that aborts on memory corruption.

## con‑leche
- First Lean kernel written in Lean and formally proven consistent (by Claude, supervised by Joachim Breitner at the Lean FRO).
- Consistency means every accepted environment has a set‑theoretic model based on Mario Carneiro’s model of Lean’s type theory.
- The proof is checked by the official kernel and assumes the consistency of the underlying set theory.
- Performance: executes 0.69× the instructions of the official kernel; checks the full Mathlib export in ~100 s on eight threads (see PERF.md).

## con‑ron
- Rust translation of con‑leche generated with AI assistance.
- Verified with **Aeneas**, a tool that proves the Rust implementation refines con‑leche’s algorithm.
- Provides protection against bugs in Lean’s compiler/runtime, as unsoundness would have to appear simultaneously in both the Lean and Rust toolchains.

## Future Plans
- Verification of **lean4lean** expected in the next few months, yielding three verified kernels.
- Lean4lean mirrors the official C++ kernel, strengthening confidence in the reference implementation.
- Ongoing kernel renovation (issue #14977) led by Arthur Adjedjis, with Joachim reviewing changes and ensuring proof integrity.
- Development of simpler kernels to reduce complexity and ease specification validation.
- Improvements to `lake check` usability, user‑hookable kernels, and verification of compiler components.
- Scaling challenges: external kernel checking must handle projects ranging from millions to billions of lines of code; work on binary export formats and incremental checking is underway.

## Call to Action
- Run `lake check --paranoid` on your projects.
- Report any disagreements between kernels to **contact@lean-fro.org**.