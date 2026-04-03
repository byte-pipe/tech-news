---
title: Allocating on the Stack - The Go Programming Language
url: https://go.dev/blog/allocation-optimizations
date: 2026-02-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-02-28T12:14:24.911302
---

# Allocating on the Stack - The Go Programming Language

# Allocating on the Stack - The Go Programming Language

## Introduction
- Recent Go releases focus on reducing heap allocations because they incur significant runtime and GC overhead.
- Stack allocations are cheaper, automatically reclaimed with the stack frame, and improve cache locality.

## Stack allocation of constant‑sized slices
- Example `process` builds a slice by repeatedly appending tasks from a channel.
- Without a pre‑allocated backing store, `append` repeatedly allocates larger slices (1, 2, 4, 8 …), causing allocator work and garbage.
- Pre‑allocating with `make([]task, 0, 10)` removes most reallocations.
- The compiler can detect the constant capacity (10) and allocate the backing store on the stack, eliminating heap allocations entirely when the slice does not escape.

## Stack allocation of variable‑sized slices
- Allowing the caller to supply a length guess (`process3`) makes the capacity non‑constant.
- In Go 1.24 the compiler cannot place such a backing store on the stack, so it falls back to a heap allocation (still only one allocation).
- Go 1.25 introduces a transformation: for small capacities (up to a 32‑byte internal buffer) the compiler allocates the backing store on the stack automatically, keeping the allocation count at zero when the guess fits.
- A manual workaround (`process4`) uses a constant‑size `make` for small guesses and a variable one for larger guesses, but the compiler now handles this automatically.

## Stack allocation of append‑allocated slices
- Go 1.26 extends the optimization to slices built entirely with `append`.
- The compiler speculatively creates a small stack‑backed buffer (e.g., capacity 4) at the first `append`.
- Subsequent appends use this buffer without heap allocation until it fills; then a heap allocation occurs for further growth.
- This eliminates the early‑stage allocations of sizes 1, 2, 4 and their associated garbage, benefitting programs with small slices.

## Stack allocation of append‑allocated escaping slices
- When a slice escapes (e.g., returned from a function), its final backing store must reside on the heap because the stack frame disappears.
- However, intermediate slices created during the building process can still be allocated on the stack, reducing temporary heap traffic even for escaping results.

*Upgrade to the latest Go release to take advantage of these stack allocation improvements and achieve faster, more memory‑efficient programs.*
