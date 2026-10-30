---
title: Yes, {} + [] = 0. No, JavaScript Isn’t Broken - DEV Community
url: https://dev.to/sylwia-lask/yes-0-no-javascript-isnt-broken-14ob
date: 2026-10-29
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-30T12:48:17.155523
---

# Yes, {} + [] = 0. No, JavaScript Isn’t Broken - DEV Community

# Yes, {} + [] = 0. No, JavaScript Isn’t Broken

## Introduction
- The article revisits a quirky JavaScript expression (`{} + []`) discovered while waiting at an airport.
- Highlights JavaScript’s long history, backward‑compatibility constraints, and resulting “weirdness.”

## Why `{}` + `[]` evaluates to 0
- At the start of a statement, `{}` is parsed as an **empty block**, not an object literal.
- The `+` that follows is the **unary plus** operator applied to `[]`.
- Unary plus triggers type coercion:
  1. `[]` → `toString()` → `""` (empty string).
  2. `Number("")` → `0`.
- Hence the whole statement becomes `0`.

## How parsing changes the result
- Wrapping the expression in parentheses forces `{}` to be treated as an object:
  ```js
  ({} + []) // "[object Object]"
  ```
- Inside a function call, the same parsing occurs:
  ```js
  console.log({} + []) // "[object Object]"
  ```

## Other related expressions
- `[] + []`  
  - Binary `+` converts both arrays to strings (`"" + ""`) → `""`.
- `[] + {}`  
  - `[]` → `""`, `{}` → `"[object Object]"` → result `"[object Object]"`.
- `{}` + `[]` (when parsed as object + array) also yields `"[object Object]"`.

## Key concepts illustrated
- **Parsing context** determines whether `{}` is a block or an object literal.
- **Unary plus** performs numeric conversion via `Number()`.
- **Type coercion** in JavaScript often leads to surprising but well‑defined results.
- The language’s **weak typing** and **backward compatibility** preserve these quirks.

## Final thoughts
- The behavior is not a bug; it follows JavaScript’s specification.
- Such examples showcase the language’s unique character and the importance of understanding its parsing and coercion rules.
- The author promises future explorations (e.g., `{}` + `{}` = `NaN`).