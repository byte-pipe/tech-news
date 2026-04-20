---
title: Surelock
url: https://notes.brooklynzelenka.com/Blog/Surelock
date: 2026-04-08
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-04-12T06:04:10.499639
---

# Surelock

# Surelock

## TL;DR
- Deadlocks arise when the four Coffman conditions hold simultaneously.
- Surelock eliminates the **circular‑wait** condition using two complementary mechanisms.
- **LockSet** acquires same‑level locks atomically in a deterministic order.
- **Level<N>** acquires cross‑level locks incrementally with compile‑time ordering enforcement.
- The public API is entirely safe; unsafe code is confined to the internal raw mutex implementation.
- Works with `no_std`, has zero runtime dependencies.

## Why Careful Coding Isn’t Enough
- Manual caution does not scale; deadlocks can appear under unforeseen request patterns.
- Rust’s borrow checker prevents data races, but it does not guarantee deadlock‑freedom.
- Coffman’s four conditions (mutual exclusion, hold‑and‑wait, no preemption, circular wait) show that breaking **circular wait** is sufficient to avoid deadlocks.
- Mutual exclusion is required, preemption introduces other bugs, leaving hold‑and‑wait and circular wait as targets.
- Surelock aims to provide ergonomic, compile‑time guarantees without sacrificing usability.

## Core Metaphor: The MutexKey
- A **MutexKey** is a linear, move‑only token representing the current lock state.
- Calling `.lock()` consumes the key and returns a new key together with the guard; the new key records which locks have been taken.
- Attempting to acquire a lock out of order or to “go backwards” fails to compile.
- The key enables atomic acquisition of multiple mutexes and supports incremental acquisition across levels.

## Prior Art
| Library | Contribution | Limitations |
|---------|--------------|-------------|
| **happylock** | Introduced capability token + sorted multi‑lock acquisition. | Requires acquiring *all* locks at once; uses address‑based sorting needing unsafe tricks for stability. |
| **lock_tree** | Compile‑time lock ordering via `LockAfter` trait. | Cannot express same‑level multi‑lock; uses a DAG ordering rather than a strict total order. |

Surelock builds on happylock’s token idea and lock_tree’s compile‑time ordering, while adding same‑level multi‑lock support, per‑instance level assignment, and a total order for simplicity.

## Dual Mechanism Design
| Mechanism | When Used | Acquisition Style | Enforcement |
|-----------|-----------|--------------------|-------------|
| **LockSet** | Multiple locks at the *same* level | Atomic (all‑or‑nothing) | Runtime sort by stable `LockId` |
| **Level<N>** | Locks at *different* levels | Incremental | Compile‑time trait bounds |

The two mechanisms are mutually exclusive and together cover common locking patterns.

## Same‑Level Locks: `LockSet`
- Each `Mutex` receives a unique, monotonically increasing `LockId` from a global atomic counter at creation.
- `LockSet::new` takes a collection of references, sorts them by `LockId`, and stores the ordered list.
- When two threads request the same set of locks in opposite orders, both see the same deterministic order, preventing cycles.
- Example (simplified):

```rust
let alice = Mutex::new("alice");
let bob   = Mutex::new("bob");

// Order of arguments does not matter
let set = LockSet::new((&alice, &bob));

key.scope(|key| {
    let (a, b) = set.lock(key);
    // both locked, deadlock impossible
});
```

## Cross‑Level Locks: `Level<N>`
- Levels are represented by distinct types (`Level<0>`, `Level<1>`, …).
- A lock belonging to a higher level can only be acquired after all lower‑level locks have been taken, enforced by trait bounds on the `MutexKey`.
- This provides **incremental** acquisition while preserving a strict total order at compile time.
- Example (simplified):

```rust
let low  = Mutex::<Level<0>>::new(...);
let high = Mutex::<Level<1>>::new(...);

key.scope(|key| {
    let (low_guard, key) = low.lock(key);   // acquire level 0
    let (high_guard, _)   = high.lock(key); // acquire level 1
});
```

## Safety Guarantees
- If the program compiles, deadlock cannot occur.
- No `Result`/`Option` or runtime panic is needed on the lock path.
- All unsafe code is isolated inside the low‑level mutex implementation; the public API is 100 % safe.

## Current Status
- Pre‑release; core design is stable but may have rough edges.
- Contributions and feedback are welcomed.
