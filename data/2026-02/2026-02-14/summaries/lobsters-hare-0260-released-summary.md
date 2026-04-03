---
title: Hare 0.26.0 released
url: https://harelang.org/blog/2026-02-13-hare-0.26.0-released/
date: 2026-02-14
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-14T06:03:15.848161
---

# Hare 0.26.0 released

# Hare 0.26.0 Released

Hare 0.26.0, the latest stable release since 0.25.2, was released on February 13, 2026. This release includes new features, bug fixes, and minor improvements. Joe Finney has been formally welcomed as the newest Hare maintainer.

## Release Highlights

*   **Loop values and for..else:** For loops can now be used in expressions to produce a result, either by breaking with a value or using an else branch. This enables more elegant control flow logic.
*   **DragonflyBSD Support:** Hare now officially supports DragonflyBSD, expanding its platform coverage to include Linux and the four common BSD flavors.
*   **Explicit Error Ignoring:** Developers can now assign to `_` to explicitly ignore errors, providing more clarity when error handling is intentionally bypassed.
*   **Padding Structs with _:** The underscore token can be used to define unnamed struct fields for explicit padding, offering a more convenient alternative to the previous `@offset` keyword.
*   **Explicitly Uninitialized Variables:** Variables can now be explicitly initialized to `@undefined`, which is useful in scenarios where a variable needs to be declared before being initialized, such as when passing pointers to functions.

## Download

The following files are available for download:

*   Compiler: harec-0.26.0.tar.gz
*   Standard Library: hare-0.26.0.tar.gz
*   Hare Update: hare-update-0.26.0.0.tar.gz

Hare 0.26.0 is compatible with version 1.2 of qbe.

Hare is a systems programming language designed for simplicity and robustness, featuring a static type system, manual memory management, and a minimal runtime.
