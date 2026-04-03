---
title: "Defer available in gcc and clang – Jens Gustedt's Blog"
url: https://gustedt.wordpress.com/2026/02/15/defer-available-in-gcc-and-clang/
date: 2026-02-17
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-17T06:01:46.259898
---

# Defer available in gcc and clang – Jens Gustedt's Blog

# Defer Available in GCC and Clang

This blog post announces the availability of the `defer` feature in GCC and Clang, following a year of development and the completion of its technical specification (TS 25755).

## Key Developments

* **Technical Specification Complete:** The specification for `defer`, edited by Jean Heyd Meniede, is finalized and undergoing ISO publication.
* **Compiler Integration:** Both GCC and Clang communities have integrated the `defer` feature into their C implementations.
* **Clang Availability:** Clang-22 is the first version to include the `defer` feature.
* **GCC Availability:** GCC-9 and later versions offer a workaround for the `defer` feature.

## Benefits of Using `defer`

The `defer` feature allows developers to:

* **Prevent Resource Leaks:** Ensure resources are released even if code paths are exited prematurely.
* **Avoid Deadlock:** Prevent blocked mutexes by guaranteeing cleanup in various scenarios.
* **Reduce Spaghetti Code:** Simplify code by handling cleanup in a more structured manner.

## Implementation and Compatibility

* **Compiler Support:** The provided code snippet offers a workaround for GCC 9 and later, and is expected to be compatible with a wide range of compilation platforms as `defer` doesn't require specific software infrastructure.
* **GCC Fallback:** GCC uses a "nested function" feature for its fallback, which is designed to avoid stack overflow vulnerabilities.
* **Clang Fallback:** Clang's "blocks" extension is not easily adaptable as a drop-in replacement for nested functions due to semantic differences.

## Examples of Use

The post provides examples of how to use `defer` for:

* **Managing Large Arrays:** Ensuring `free` is called even if `malloc` fails.
* **Unlocking Mutexes:** Guaranteeing mutexes are unlocked when exiting critical sections, regardless of the execution path.

## Important Note

The `defer` feature must always be used within curly braces `{}` to ensure the GCC fallback mechanism works correctly.

## Related Standards

The `defer` feature is part of the C11, C17, C23, C2x, C2y, and Modern C standards.
