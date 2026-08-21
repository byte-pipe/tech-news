---
title: Announcing Rust 1.98.0 | Rust Blog
url: https://blog.rust-lang.org/2026/08/20/Rust-1.98.0/
date: 2026-08-22
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-22T06:01:07.488221
---

# Announcing Rust 1.98.0 | Rust Blog

# Announcing Rust 1.98.0

## Release information
- The stable channel can be updated with `rustup update stable`.
- New users should install rustup from the official website.
- Testers can switch to the beta (`rustup default beta`) or nightly (`rustup default nightly`) channels and report any bugs.

## New stable features

- **Algebraic floating‑point methods**  
  - Added `algebraic_add`, `algebraic_sub`, `algebraic_mul`, `algebraic_div`, and `algebraic_rem` for `f32` and `f64`.  
  - Allow the compiler to reorder operations for better optimization and loop‑vectorization.  
  - Results are non‑deterministic but never cause undefined behavior.

- **Buffered integer formatting**  
  - All primitive integer types now have `format_into(&mut NumBuffer<Self>) -> &str`.  
  - Uses an opaque buffer sized for any value of the type, reducing dynamic dispatch overhead.  
  - Performance comparable to the `itoa` crate, making it a viable standard replacement.

- **Fix for interaction between `ManuallyDrop` and `Box`**  
  - A bug that made moving a dropped `Box` through `ManuallyDrop` undefined behavior was fixed in 1.96.0.  
  - Documentation now guarantees the code is stable and no longer UB.

- **Stabilized APIs**  
  - `str::substr_range`  
  - `[T]::subslice_range`  
  - `core::fmt::NumBuffer`  
  - `<{integer}>::format_into`  
  - `Send/Sync` for `std::process::CommandArgs`  
  - Algebraic floating‑point methods (`{fN}::algebraic_*`)  
  - `NonZero<{integer}>::from_str_radix`  
  - `String::from_utf16le`, `String::from_utf16le_lossy`, `String::from_utf16be`, `String::from_utf16be_lossy`  
  - `[T]::strip_circumfix` and `str::strip_circumfix`  
  - `Atomic<T>::from_mut`, `Atomic<T>::get_mut_slice`, `Atomic<T>::from_mut_slice`  
  - `std::range::legacy`

- **Other changes**  
  - Comprehensive updates to Rust, Cargo, and Clippy are listed in the full changelog.

## Contributors
- A large community of contributors collaborated on Rust 1.98.0.  
- The release team thanks everyone for their effort.