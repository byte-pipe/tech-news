---
title: Emacs Internal #02: Data First — Deconstructing Lisp_Object in C | The Cloudlet
url: https://thecloudlet.github.io/blog/project/emacs-02/
date: 2026-03-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-09T07:26:14.140808
---

# Emacs Internal #02: Data First — Deconstructing Lisp_Object in C | The Cloudlet

# Emacs Internal #02: Data First — Deconstructing Lisp_Object in C

## Overview
- The article continues a series on GNU Emacs internals, focusing on system‑design aspects rather than historical background.
- It emphasizes a “data‑first” approach to understanding source code, especially the core Emacs type `Lisp_Object`.

## Mathematical and Compiler Foundations
- Computation is framed as data transformed by operations (e.g., arithmetic, matrix multiplication, convolution).
- This abstraction maps to the Von Neumann model: bits in memory are fetched into registers and operated on by lowered IRs until they become native instructions.
- Modern compilers (LLVM, MLIR) embody this principle by optimizing sequences of operations across heterogeneous hardware.

## Code as Data and Data as Code
- The article reiterates that both data and instructions are just bit patterns in memory; the CPU interprets bits as code only when the program counter points to them.
- Lisp machines were still von Neumann architectures; they merely bundled a Lisp OS, compiler, and some hardware accelerators.

## Preference for Data‑Centric Reading
- The author prefers to start from data structures (e.g., private members of a C++ class) because they are self‑descriptive.
- Understanding the data model makes the surrounding operations appear as transformations, aligning with functional and data‑oriented programming mindsets.

## Lisp_Object: The Universal C Type
### Tagged Pointer Layout
- `Lisp_Object` is a 64‑bit word used to represent any Emacs Lisp value in C.
- Heap‑allocated objects are 8‑byte aligned, leaving the lowest three bits free; Emacs stores a 3‑bit type tag in these bits.
- Immediate integers (fixnums) use the upper 62 bits for the value, with the tag occupying the low bits.

### Tag Enumeration
- The `enum Lisp_Type` defines tags such as `Lisp_Symbol (0b000)`, `Lisp_Int0 (0b010)`, `Lisp_Int1 (0b110)`, `Lisp_String (0b100)`, etc.
- The same two low bits for `Lisp_Int0` and `Lisp_Int1` allow a doubled range for fixnums:
  - 3‑bit tag → 61‑bit value range (‑2⁶⁰ … 2⁶⁰‑1)
  - 2‑bit tag for fixnums → 62‑bit value range (‑2⁶¹ … 2⁶¹‑1)

### Operation Conventions
- Macros and inline functions follow a naming scheme:
  - `X` prefix – eXtract the underlying value or pointer after masking off the tag.
  - `P` suffix – Predicate that checks the type, returning a boolean.
  - `CHECK_` prefix – Assert the type, signaling a Lisp error on mismatch.
- Example pattern:

```c
if (FIXNUMP (obj)) {
    EMACS_INT n = XFIXNUM (obj);
}
```

- Extraction macros (`XSTRING`, `XCONS`, `XFIXNUM`, etc.) mask the tag bits (using `XUNTAG`) and cast to the appropriate C struct or integer type.

## Takeaways
- Emacs implements a compact, tag‑embedded representation (`Lisp_Object`) to avoid extra metadata structures and improve cache locality.
- Understanding this data layout clarifies how Emacs Lisp values are manipulated in the C runtime.
- The “data first” perspective aligns with functional and data‑oriented programming, offering a clearer mental model for navigating Emacs’s source code.
