---
title: ClojureScript - 1.12.145 Release
url: https://clojurescript.org/news/2026-05-07-release
date: 2026-05-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-09T07:55:30.155446
---

# ClojureScript - 1.12.145 Release

# Code Summary

## Overview
- Imports the global `Promise` class for use in the namespace.  
- Defines an asynchronous function `foo` (marked with `^:async`) that takes a single argument `n`.

## Function Details
- **Awaited values**
  - `x` is assigned the result of `(await (Promise/resolve 10))`, yielding `10`.
  - `y` is computed by awaiting `(Promise/resolve 20)`, then applying `inc` to the resolved value, resulting in `21`.
- **Non‑async helper**
  - `f` is a regular (synchronous) function that returns the constant `20`.
- **Return expression**
  - The function returns the sum of `n`, `x`, `y`, and the result of calling `(f)`, i.e., `(+ n x y (f))`.

## Result
- Calling `(foo n)` produces a promise that resolves to `n + 10 + 21 + 20 = n + 51`.