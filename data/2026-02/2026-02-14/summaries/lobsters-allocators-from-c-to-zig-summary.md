---
title: Allocators from C to Zig
url: https://antonz.org/allocators/
date: 2026-02-14
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-14T06:01:50.353059
---

# Allocators from C to Zig

# Allocators from C to Zig

This article compares memory allocation approaches in C, Rust, and Zig, highlighting the evolution from a system-provided allocator to more controlled, explicit mechanisms.

## Rust
Rust uses a global memory allocator, though it's currently experimental. The standard library relies on this allocator for types like `Box<T>` and `Vec<T>`. The `GlobalAlloc` trait defines the interface for allocators, requiring implementations to provide `alloc` (allocate memory) and `dealloc` (free memory) methods.  The `Layout` struct specifies the size and alignment requirements of allocated memory.  Rust provides helper functions for creating valid layouts. The system allocator is the default, but this isn't guaranteed.  Direct use of `alloc` and `dealloc` is rare; instead, types like `Box`, `String`, and `Vec` handle allocation and deallocation automatically.  Out-of-memory conditions are handled by returning `null` (as recommended by the system allocator) or by using `handle_alloc_error` to abort the program.

## Zig
Zig takes a more explicit approach to memory management. There's no default global allocator; allocation requires passing an allocator as a parameter to allocation functions. This provides greater control and transparency.

### Allocator Interface
