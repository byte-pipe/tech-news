---
title: Elixir v1.20 released: now a gradually typed language - The Elixir programming language
url: https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/
date: 2026-06-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-04T06:56:51.240122
---

# Elixir v1.20 released: now a gradually typed language - The Elixir programming language

# Elixir v1.20 released: now a gradually typed language

## Overview
- Elixir v1.20 introduces a set‑theoretic, gradually typed system that works without requiring explicit type annotations.
- The compiler now performs type inference, detects dead code, and reports **verified bugs** (type violations guaranteed to fail at runtime) with a very low false‑positive rate.
- The implementation excels in the “If T: Benchmark for Type Narrowing”, passing 12 of 13 categories, showing precise type recovery from ordinary code.

## Core Goals of the Type System
- **Soundness**: inferred types accurately reflect program behavior.  
- **Graduality**: the special `dynamic()` type bridges static and dynamic typing; when absent, the system behaves like a static type checker.  
- **Developer friendliness**: types are expressed using unions, intersections, and negations; error messages are clear and concise.

## The `dynamic()` Type
- Unlike the typical `any()` that suppresses all checks, `dynamic()` has **compatibility** and **narrowing** properties.
- **Compatibility**: a typing violation is raised only when the supplied type and the expected type are disjoint (e.g., passing a `dynamic(integer() or binary())` to `Map.fetch!` which expects a map).
- **Narrowing**: as a value flows through the program, its `dynamic()` type is refined based on pattern matches, guards, and field accesses (e.g., a map initially typed `dynamic()` becomes `%{..., a: number(), b: number()}` after accessing `data.a` and `data.b`).
- The system behaves as if every argument were annotated `dynamic()`. Future user‑provided annotations will make the language fully static where `dynamic()` is not used, without extra runtime checks.

## Type Inference in Common Constructs
- **Guards**: unions, intersections, and negations are inferred from `is_*` checks, map‑key presence, and size predicates.
  - Example: `when is_list(x) and is_integer(y)` infers `x :: list()` and `y :: integer()`.
  - Negated map‑key guard (`not is_map_key(x, :foo)`) yields a type `%{..., foo: not_set()}` causing a violation if `x.foo` is accessed.
- **Size checks**: `tuple_size(x) < 3` narrows a tuple to at most two elements; similar checks on lists/maps translate to emptiness information.
- **Pattern matching**: matching on tuples or maps refines component types accordingly.

## Implementation and Support
- Developed through a partnership between CNRS and Remote, with sponsorship from Fresha and Tidewave.
- The current milestone focuses on delivering value without annotation overhead; future work will incorporate user‑supplied type specs and expand static capabilities.