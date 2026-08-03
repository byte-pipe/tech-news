---
title: rust-project-goals/src/2026/move-trait.md at main · rust-lang/rust-project-goals · GitHub
url: https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/move-trait.md
date: 2026-08-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-04T06:01:32.575508
---

# rust-project-goals/src/2026/move-trait.md at main · rust-lang/rust-project-goals · GitHub

# Immobile types and guaranteed destructors

## Overview
- Proposes new auto‑traits (`Move`, `Destruct`, `Forget`) that make a type’s capabilities explicit.
- Allows types to opt out of being moved or forgotten, enabling:
  - Scoped spawn and async drop.
  - Pin‑by‑default semantics without the current `Pin` complexity.
- Mirrors the earlier “Sized hierarchy” work that relaxed the universal‑size assumption.

## Motivation
- **Current assumptions**: all values can be relocated and can be forgotten via `mem::forget` without running destructors.
- **Problems**:
  - *Immobile types*: self‑referential async futures cannot be safely moved; existing `Pin` encodes immovability on *places*, leading to intricate patterns (e.g., Safe Pinned Initialization Problem in the Linux kernel).
  - *Guaranteed destructors*: some resources need deterministic cleanup (e.g., transaction commit/rollback, scoped task handles). Because `mem::forget` is safe, Rust cannot guarantee destructor execution, blocking safe scoped spawn.

## Proposed solution
- Introduce **capability traits** as positive type properties:
  - `unsafe auto trait Move {}` – types **not** implementing `!Move` are immovable for their entire lifetime.
  - `unsafe auto trait Forget {}` – types **not** implementing `!Forget` must have their destructors run; they cannot be forgotten.
  - `Destruct` (implicit in current drop semantics) can be expressed similarly if needed.
- Traits are *type‑level* rather than *place‑level*, simplifying reasoning and implementation.
- Example usage:
  ```rust
  unsafe impl !Forget for ScopedTaskHandle { }
  // The handle’s destructor joins the task; it cannot be forgotten.
  ```

## Work plan (2026‑2027)
### Move trait
| Task | Owner(s) | Notes |
|------|----------|-------|
| Compiler implementation for `Move` | @lcnr, @nia‑e | |
| Write the `Move` RFC | @yoshuawuyts | |
| Test in Linux kernel | @BennoLossin | Real‑world self‑referential structures |
| Verify interaction with `Iterator` | @yoshuawuyts | Ensure generators can desugar to `impl Trait + !Move` |
### Guaranteed destructors
| Task | Owner(s) | Notes |
|------|----------|-------|
| Design exploration for guaranteed destructors | @nikomatsakis | |
| Study trait hierarchy interactions | – | Assess compatibility with existing features |
- **Out of scope for this year**: changes to the `Future` trait, which currently depends on `Pin`. Migration is deferred to a separate project.

## Team requests
- **Language team**: large support; needs a design session to resolve open questions.
- **Types team**: large support; will participate in implementation and review.

## Frequently asked questions
- **Relation to Sized hierarchy**: Both follow the pattern of relaxing a universal assumption via auto‑traits, allowing selective opt‑out.
- **Relation to Pin ergonomics**: This proposal is an alternative to extending `Pin`. It aims to replace `Pin` entirely by making immovability a type property, avoiding duplicate trait definitions and long‑term compatibility concerns.
- **Safe scoped spawn**: Enabled by `!Forget`; the handle’s destructor is guaranteed to run, preventing tasks from outliving their borrowed context.
- **Further reading**: Blog posts titled “Move, Destruct, Leak” discuss the trait hierarchy and design space in more depth.