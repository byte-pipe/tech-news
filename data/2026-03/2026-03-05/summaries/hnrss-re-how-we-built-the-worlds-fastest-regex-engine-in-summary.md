---
title: "RE#: how we built the world's fastest regex engine in F# | ian erik varatalu"
url: https://iev.ee/blog/resharp-how-we-built-the-fastest-regex-in-fsharp/
date: 2026-03-01
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-03-05T06:03:12.747716
---

# RE#: how we built the world's fastest regex engine in F# | ian erik varatalu

# RE#: How We Built the World’s Fastest Regex Engine in F#

## Brief Overview
- Developed a regex engine in F# that outperforms all existing .NET and industrial engines on extensive benchmarks.
- Supports full Boolean operators: union (`|`), intersection (`&`), complement (`~`), and a form of context‑aware lookarounds, while preserving O(n) search‑time complexity.
- Paper published at POPL 2025; now open‑sourced with an engineering‑focused, conversational write‑up.

## Motivation and Background
- Modern regex engines fall into two camps:
  - **Thompson NFA** (e.g., grep, RE2, Rust regex) – linear‑time guarantees but limited to basic operators.
  - **Backtracking** (majority of existing engines) – richer features (backreferences, lookarounds) but can degrade to exponential time, causing ReDoS vulnerabilities.
- Neither camp historically supports intersection (`&`) or complement (`~`), despite early research (Brzozowski 1964) and later rediscoveries (2009, 2019).
- RE# draws inspiration from SRM and the .NET NonBacktracking engine (2023) but adds true Boolean operators with practical performance.

## Core Technical Idea: Brzozowski Derivatives
- **Derivative** of a regex R with respect to a character c is the regex that matches the remainder after consuming c.
- Matching proceeds by iteratively taking derivatives for each input character and checking if the resulting regex is nullable (accepts the empty string).
- Derivatives naturally extend to intersection and complement because Boolean operators distribute over derivatives, eliminating the need for special handling.
- This approach provides a uniform, simple mechanism for all regular‑language features, including the newly exposed Boolean operators.

## Benefits of Boolean Operators
- **Separation of concerns**: Write small, focused regex fragments for individual properties and combine them with `&` and `~`.
- Improves readability, maintainability, and modularity of patterns.
- Example fragments:
  - `_*` – any string
  - `a_*` – strings starting with `a`
  - `_*a` – strings ending with `a`
  - `~(_*a_*)` – strings that do **not** contain `a`
  - `(_*a_*)&~(_*b_*)` – contains `a` **and** not `b`
- Real‑world use cases:
  - Password filtering by toggling fragments for length, uppercase, digits, symbols.
  - Paragraph extraction using `~(_*\n\n_*)` to exclude double newlines.

## Performance and Correctness
- RE# is the **first general‑purpose regex engine** offering intersection and complement with linear‑time guarantees.
- Benchmarks show it is the **fastest** engine across a large suite of industry‑standard tests.
- Guarantees correct “leftmost‑longest” matches, aligning with PCRE semantics, while avoiding exponential blow‑up.

## Engineering Highlights
- Over a year of experimentation to find a practical combination of derivatives, Boolean operators, and lookarounds with acceptable complexity.
- Initial drafts (arXiv 2023) had poorer lookaround performance; later refinements achieved the current speed.
- Open‑source release includes a web app (https://ieviev.github.io/resharp-webapp/) for visualizing regex composition and matches.

## Takeaway
RE# demonstrates that advanced Boolean regex operators can be integrated into a practical engine without sacrificing performance or safety, offering a more expressive, modular, and reliable tool for developers.
