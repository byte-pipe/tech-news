---
title: Announcing Rust 1.95.0 | Rust Blog
url: https://blog.rust-lang.org/2026/04/16/Rust-1.95.0/
date: 2026-04-18
site: tldr
model: llama3.2:1b
summarized_at: 2026-04-18T11:42:54.779429
---

# Announcing Rust 1.95.0 | Rust Blog

**Rust 1.95 Stable Release**

The Rust team is pleased to announce the release of Rust 1.95, a stable version of the programming language.

**Key Changes and Features:**

- **cfg_select! Macro:** A new feature in `cfg_select!` macro that allows for more flexible and concise conditional compilation.
- **if-let Guards in Matches:** Support has been added to match expressions with if let guards, allowing for conditionals based on pattern matching.
- **Stabilized APIs:** Previous stabilized APIs have been implemented or updated.

**Changes and Improvements:**

- **Changes to `if` Guards:** Improved performance by not considering patterns matched in `if let` guardians as part of the exhaustiveness evaluation, similar to pattern guards.
- **New API Stability Indicator:** A new way to check for stability using the `MaybeUninit[T; N]` type.

**What Users Need to Know:**

- To upgrade or maintain Rust 1.95, you can use `$ rustup update stable <version>`.
- For detailed release notes and more information on new features, visit our website.
- Testing of future releases is encouraged by participating in the beta channel (newest local testing setup) or nightly channel (most recently tested version).

**How Users Can Help:**

- Report any bugs you discover in tests.
- Consider updating for the latest stable release via the default beta channel (beta1.95.0).
