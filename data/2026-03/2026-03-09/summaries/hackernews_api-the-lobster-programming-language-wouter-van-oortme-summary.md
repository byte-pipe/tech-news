---
title: The Lobster Programming Language — Wouter van Oortmerssen
url: https://strlen.com/lobster/
date: 2026-03-04
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-09T07:26:06.656772
---

# The Lobster Programming Language — Wouter van Oortmerssen

# The Lobster Programming Language – Summary

## Features
- Statically typed with flow‑sensitive type inference, making code feel as easy as dynamic typing.
- Compile‑time reference counting, lifetime analysis and borrow checking.
- Lightweight blocks and anonymous functions that integrate seamlessly with control structures.
- Built‑in vector operations and unified overloading/dynamic dispatch, supporting specialization.
- Immutable “inline” structs with zero overhead.
- GIL‑less, race‑less distributed memory model for multithreading.
- Python‑style indentation syntax combined with C‑style elements.

## Implementation
- Run programs via a convenient JIT or compile to C++ for higher performance.
- Reference counting with cycle detection; ~95 % of reference‑count ops eliminated at compile time.
- Fully graphical debugger (stack inspection, variable modification).
- Dynamic code loading.
- Performance: order‑of‑magnitude faster than Python, significantly faster than Lua; not yet C‑level speed but improvable.
- Low memory‑allocation overhead, easy deployment (engine/JIT executable + compressed bytecode).
- Extensible with user‑written C++ libraries.

## Portability & Libraries
- Portable engine using OpenGL/SDL/Freetype; runs on Windows, Linux, macOS, iOS, Android and WebAssembly (increasing maturity).
- High‑level OpenGL interface for quick 2D primitives and 3D mesh construction (including marching cubes).
- GLSL shaders usable on OpenGL and OpenGL ES 2 without changes.
- Accurate text rendering via FreeType.
- Uniform input system for mouse and touch.
- Simple sound system supporting .wav and .sfxr files.
- ImGui integration.
- Comes with Lobster libraries for A* pathfinding, game GUIs, etc.

## Examples (Key Takeaways)
- Functions are defined with `def`, blocks use indentation, and anonymous functions are passed directly after calls using `:`.
- No explicit type declarations needed; the compiler infers types and specializes functions per call site (similar to C++ templates).
- `let` (or `var`) introduces new variables; `=` performs assignment.
- `return` exits the nearest enclosing function, and can be directed to any named function, enabling custom exception handling.
- Classes support inheritance; immutable structs (`structor`) are passed by value and work with vector operations.
- Multiple overloads of a function can be defined for different argument types, enabling dynamic dispatch.
