---
title: Lisette — Rust syntax, Go runtime
url: https://lisette.run/
date: 2026-04-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-06T01:02:30.987744
---

# Lisette — Rust syntax, Go runtime

# Lisette – Rust syntax, Go runtime

## Overview
- Lisette is a small language inspired by Rust that compiles to Go.
- It brings algebraic data types, pattern matching, Hindley‑Milner type inference and immutable‑by‑default semantics to the Go ecosystem.
- Designed for seamless interoperation with existing Go libraries and tooling.

## Core Language Features
- **Algebraic data types & enums** with exhaustive `match` expressions.
- **Pattern matching** for deconstructing values, including guards.
- **Structs and `impl` blocks** for methods (e.g., `Point.distance`).
- **Expression‑oriented syntax** with `if`/`else` as expressions.
- **Lambdas and chaining** using the pipeline operator (`|>`).
- **Interfaces and generics** (`Metric` interface, `max<T: Metric>`).
- **Option and Result** types replace `nil` and unchecked errors.
- **`if let … else`** construct for concise handling of optional values.
- **`defer`** for resource cleanup, mirroring Go’s defer semantics.
- **`try` blocks** for simplified error propagation.

## Safety Guarantees (checked at compile time)
- Non‑exhaustive `match` patterns produce errors.
- `nil` is not a valid value; use `Option<T>` (`None`) instead.
- Unused `Result` values generate warnings; must be handled with `?`, `match`, or explicit discard.
- Private types exposed in public APIs trigger visibility errors.
- Immutable bindings by default; mutable variables require `let mut`.
- Struct literals must include all fields unless defaults are provided.

## Ergonomic Additions for Go Interoperability
- **Pipeline operator** for readable data transformations (e.g., `slugify` example).
- **`try` blocks** to group fallible operations and return a default on error.
- **Concurrency primitives** (`Channel`, `task`, `select`) map to Go goroutines and channels.
- **Serialization attributes** (`#[json(...)]`, `#[tag(...)]`) generate Go struct tags.
- **Panic recovery** returns a `Result` instead of aborting the program.
- **Deferral** (`defer`) integrates with Go’s resource management patterns.

## Tooling Support
- Language Server Protocol (LSP) implementations for:
  - VSCode
  - Neovim
  - Zed

## Example: From Lisette to Go
### Lisette code
```lis
fn classify(opt: Option<int>) -> string {
    match opt {
        Some(x) if x > 0 => "positive",
        Some(x) if x < 0 => "negative",
        Some(_)          => "zero",
        None             => "none",
    }
}
```
### Generated Go code
```go
func classify(opt lisette.Option[int]) string {
    if opt.Tag == lisette.OptionSome {
        x := opt.SomeVal
        if x > 0 {
            return "positive"
        }
        if x < 0 {
            return "negative"
        }
        return "zero"
    }
    return "none"
}
```

## Installation
```bash
cargo install lisette
```
Import Go packages directly in Lisette code using the `import "go:package"` syntax.