---
title: What Async Promised and What it Delivered — Causality
url: https://causality.blog/essays/what-async-promised/
date: 2026-04-22
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-27T06:03:35.133901
---

# What Async Promised and What it Delivered — Causality

# What Async Promised and What it Delivered

## Introduction
- OS threads are heavy (memory, creation time, context‑switch cost) leading to the C10K problem: handling many concurrent connections without a thread per connection.
- Solutions arrived in successive “waves,” each fixing the previous wave’s biggest issue while introducing new challenges.
- The article examines the async wave, following earlier discussions of Go channels and Erlang actors.

## Callbacks
- First wave: avoid blocking threads by registering a function (callback) to run when an I/O operation finishes.
- Event‑loop mechanisms (select, poll, epoll, kqueue) let a few threads multiplex thousands of connections.
- Node.js and Nginx demonstrated high‑concurrency performance using this model.
- Problems introduced:
  - Inverted control flow → nested closures (“callback hell”), making code hard to read.
  - Fragmented error handling: each callback needs its own error path; errors cannot naturally propagate up a call stack.
  - No built‑in cancellation: asynchronous operations continue even if their results are no longer needed.

## Promises and Futures
- Second wave: asynchronous operations return a placeholder object (promise/future) representing the eventual result.
- Historical roots in Baker & Hewitt (1977); mainstream adoption driven by C10K pressure in the 2010s.
- Advantages:
  - Composable chains (`promise.then(...).then(...)`) replace nested callbacks.
  - Centralized error handling via a single `.catch()` at the end of a chain.
  - Promises are first‑class values that can be stored, passed, and returned.
- New issues:
  - One‑shot nature: unsuitable for streams or ongoing events; requires separate mechanisms (event emitters, observables).
  - Clunky composition for complex flows (conditional branching, loops) often needs functional‑style combinators like `Promise.all`.
  - Silent failures: unhandled rejections could be swallowed, later turned into warnings or crashes.
  - “Function coloring” problem: callers must know whether a function returns a raw value or a promise, mixing synchronous and asynchronous APIs.

## Async/Await
- Third wave: language syntax (`async`/`await`) that lets developers write asynchronous code that looks sequential.
- Originated in C# (2012); adopted by JavaScript (ES2017), Python (3.5), Rust (1.39), Kotlin, Swift, Dart.
- Benefits:
  - Straight‑line, readable code; natural variable binding.
  - Standard `try/catch` for error handling instead of `.catch()`.
  - Loops and conditional logic work naturally with `await`.
- Rapid industry adoption: major JavaScript frameworks, Python’s asyncio, and Rust’s async runtime all embraced the model as the default for concurrent I/O.

## Emerging Concern: Function Coloring Tax
- The article begins to discuss the cost of the “function coloring” problem introduced by promises and amplified by async/await, where every API consumer must track whether a function returns a plain value or an asynchronous placeholder. (The discussion continues beyond the provided excerpt.)