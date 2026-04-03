---
title: Go 1.26 is released - The Go Programming Language
url: https://go.dev/blog/go1.26
date: 2026-02-12
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-12T06:01:32.774331
---

# Go 1.26 is released - The Go Programming Language

# Go 1.26 is released

Go 1.26 has been released, featuring several enhancements across the language, performance, and tools.

## Language Changes
- The built-in `new` function now accepts an expression as its operand, allowing specification of the initial value of the newly created variable.
- Generic types can now refer to themselves in their type parameter lists, simplifying the implementation of complex data structures and interfaces.

## Performance Improvements
- The Green Tea garbage collector, previously experimental, is now enabled by default.
- Baseline Go overhead has been reduced by approximately 30%.
- The compiler can now allocate backing stores for slices on the stack more frequently, improving performance.

## Tool Improvements
- The `go fix` command has been rewritten using the Go analysis framework and includes numerous "modernizers" and analyzers to suggest safe fixes for leveraging newer language features.
- The `inline` analyzer attempts to inline all function calls marked with the `//go:fix inline` directive.

## More Improvements and Changes
- Go 1.26 includes additions to the `crypto/hpk`, `crypto/mlkem/mlkemtest`, and `testing/cryptotest` packages.
- There are report-specific changes and updates to Go Debug settings.
- Several features are experimental and require explicit opt-in:
    - `simd/arch` package provides access to SIMD operations.
    - `runtime/secret` package offers secure erasure of temporary data used in cryptographic operations.
    - `goroutineleak` profile in the `runtime/pprof` package reports leaked goroutines.

## Additional Information
- More details on these experimental features will be covered in future blog posts.
- The complete list of changes and improvements can be found in the Go 1.26 Release Notes.
- The Go team thanks contributors for their efforts in making this release stable and encourages users to report any issues.
