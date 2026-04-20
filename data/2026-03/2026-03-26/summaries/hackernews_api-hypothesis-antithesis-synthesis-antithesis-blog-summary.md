---
title: Hypothesis, Antithesis, synthesis | Antithesis Blog
url: https://antithesis.com/blog/2026/hegel/
date: 2026-03-25
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-26T01:03:42.886501
---

# Hypothesis, Antithesis, synthesis | Antithesis Blog

# Hypothesis, Antithesis, synthesis – Introducing Hegel

## Introduction
- The author created Hypothesis, later joined Antithesis with Liam DeVoe, leading to a synthesis: the new family of property‑based testing libraries called **Hegel**.
- Hegel aims to bring Hypothesis‑level quality to every programming language and integrate tightly with Antithesis for stronger bug‑finding.
- First release: Hegel for Rust; Go version expected within weeks, with C++, OCaml, and TypeScript libraries in development.

## Hegel for Rust – A Quick Example
- A test annotated with `#[hegel::test(test_cases = 1000)]` generates random strings and feeds them to `Fraction::from_str`.
- The test discovers that `from_str("0/0")` panics instead of returning an error, exposing a bug in the `fraction` crate.

## Why Property‑Based Testing?
- Instead of writing concrete inputs, you specify a property that must hold for a wide range of generated values.
- Example property: a parser should never crash; it must either return a valid result or an error.
- Benefits:
  - Eliminates manual creation of numerous edge‑case inputs.
  - Even simple “doesn’t crash” properties catch surprising bugs in languages like Python and Rust.

## More Advanced Property Examples
- **Decimal round‑trip test**: generate random `Decimal` values, format them in scientific notation, parse back, and assert equality.
  - Revealed a bug in `rust_decimal` where zero is mishandled in scientific notation.
- **Unicode title‑case idempotence**: converting a string to title case twice should be a no‑op.
  - Fails on the character “ß”, which first becomes “SS” and then “Ss”.
- **Structural invariant test (OrdMap vs. BTreeMap)**: compares `get_prev` behavior on large key sets, exposing a size‑dependent bug.

## Classification of Bugs Found by Property‑Based Testing
1. **Forgot about zero** – edge cases involving zero values.
2. **Cursed data types** – subtle issues with specific types (e.g., Unicode).
3. **Complex structural invariants** – mismatches in sophisticated data‑structure behavior.

## Model‑Based Testing
- Build a simple “model” (e.g., a naïve implementation) and use property‑based tests to ensure the real implementation matches the model across many generated scenarios.
- The OrdMap vs. BTreeMap example illustrates this approach.

## What Is Hypothesis?
- The most widely used property‑based testing library, written in Python.
- Its popularity stems from:
  - A rich collection of high‑quality generators.
  - Flexible tools for composing and extending generators.
  - Strong community adoption and integration with testing ecosystems.

## Key Takeaways
- Hegel extends the power of Hypothesis to multiple languages, starting with Rust.
- Property‑based testing simplifies discovery of edge‑case bugs, from trivial crashes to deep structural invariants.
- Combining Hegel with Antithesis’s fuzzing capabilities amplifies bug‑finding effectiveness.
- Starting with existing tests and refactoring them into property‑based form is an effective way to adopt the methodology.
