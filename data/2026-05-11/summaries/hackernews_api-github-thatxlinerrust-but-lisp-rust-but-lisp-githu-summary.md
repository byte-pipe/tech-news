---
title: GitHub - ThatXliner/rust-but-lisp: Rust but LISP · GitHub
url: https://github.com/ThatXliner/rust-but-lisp
date: 2026-05-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-11T06:04:23.001293
---

# GitHub - ThatXliner/rust-but-lisp: Rust but LISP · GitHub

# Rust but Lisp (rlisp) – Project Summary

## Overview
- rlisp is a weekend project that transposes Rust semantics into Lisp‑style s‑expressions.  
- It is a source‑to‑source compiler: s‑expressions → Rust source (`.rs`) → binary.  
- The tool focuses on syntax transformation; type checking, borrow checking, and optimizations are still performed by `rustc`.  
- Designed for exploration and fun rather than production use; some Rust syntax (e.g., turbofish, lifetime bounds) is still incomplete.

## Installation
- Clone the repository and install with Cargo:
  ```bash
  git clone https://github.com/ThatXliner/rlisp.git
  cd rlisp
  cargo install --path .
  ```

## Usage
- **Compile only**: `rlisp compile file.lisp` → generates `file.rs`.  
- **Build**: `rlisp build file.lisp` → transpiles and compiles with `rustc`.  
- **Run**: `rlisp run file.lisp` → transpiles, compiles, and executes.

## Quick Reference (Lisp ↔ Rust)
- Function definition: `(fn add ((x i32) (y i32)) i32 (+ x y))` → `fn add(x: i32, y: i32) -> i32 { x + y }`
- Variable binding: `(let x i32 42)` → `let x: i32 = 42;`
- Struct: `(struct Point (x f64) (y f64))` → `struct Point { x: f64, y: f64 }`
- Enum: `(enum Option (< T) (Some T) None)` → `enum Option<T> { Some(T), None }`
- Pattern matching: `(match val ((Some x) (handle x)) (None ()))` → `match val { Some(x) => { handle(x) }, None => {} }`
- Control flow, method calls, loops, closures, traits, etc., follow analogous transformations (see README for full table).

## Macros
- rlisp macros are compile‑time s‑expression transformers; no procedural macros, token streams, or external crates required.  
- Special forms:
  - `(quasiquote template)` – returns the template with unquote holes.
  - `(unquote name)` – inserts the value of `name`.
  - `(unquote-splicing name)` – splices a list into the surrounding list.
- Example macro definition:
  ```lisp
  (defmacro when (condition &rest body)
    (quasiquote (if (unquote condition) (do (unquote-splicing body)))))
  ```
- Variadic macros use `&rest` and `unquote-splicing`.

## Loops
- While loop: `(while (> x 0) (println! "{}" x) (-= x 1))`
- Infinite loop: `(loop (println! "tick"))`
- For loop with range: `(for x in 0..10 (println! "{}" x))`
- Destructuring with `enumerate`: `(for (i val) in (. v iter) enumerate ...)`

## Closures
- Untyped closure: `(let add (lambda (x y) (+ x y)))`
- Typed closure with return type: `(let mul (lambda ((x i32) (y i32)) i32 (* x y)))`
- Move closure example using captured variable.

## Modules, Visibility, and Imports
- Visibility modifiers: `pub`, `pub(crate)`, `pub(super)`.  
- Inline module definition with `pub mod utils ...`.  
- External module declaration: `(mod external_lib)`.  
- Import syntax mirrors Rust: `(use std::collections::HashMap)`, `(use std::io::{self, Write, Read})`, `(use std::fmt::Display as Fmt)`.

## Inline Rust
- Raw Rust code can be embedded with `(rust "...")`.  
- The string is emitted verbatim into the generated `.rs` file, with Lisp escape handling.

## Advanced Features
- **Lifetimes**: `(fn longest (< 'a) ((x &'a str) (y &'a str)) (&'a str) ...)`
- **Turbofish**: `(let nums ((:: (. (0..10) collect) Vec<i32>)))`
- **Control flow**: `break`, `continue`, `return` inside loops; `if-let`, `while-let`; type casts with `(as expr Type)`.
- **Unsafe blocks**: `(unsafe (rust "...") (rust "..."))`.

## Motivation
- To experience Rust’s type system and borrow checker without its conventional syntax.  
- Macros become simple compile‑time functions, eliminating the need for procedural macro infrastructure.  
- S‑expressions guarantee balanced parentheses, aiding structural editing.  
- Uniform syntax across expressions, types, patterns, and statements reduces mental overhead.

## License
- Distributed under the MIT License.