---
title: Hylo | Hylo
url: https://hylo-lang.org/
date: 2026-02-12
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-12T06:03:45.363270
---

# Hylo | Hylo

# Hylo
A Systems Programming Language Focused on Value Semantics and Generic Programming

## Join the Hylo Community
Connect with developers and contributors via Slack and GitHub Discussions.

## Achievements
Hylo has made progress in several key areas:

**MV S & Theory:**
- Extended Swift's subscripts with inout projections.
- Implemented method bundles for structured concurrency.
- Achieved safe and faster double linked list representation using value semantics.

**Compiler:**
- Compilation using LLVM is underway.
- Developed novel techniques for compiling generics with coherence.
- Implemented caching and serialization of the compiler's program state.
- Ongoing research in C interoperability.

**Standard Library:**
- Documentation of fundamental traits and data structures is available.
- Implemented positionless collection algorithms.
- Developed rs-stl, a Rust port of C++ STL algorithms for enhanced generic programming.

**Developer Experience:**
- Provides a VSCode extension with syntax highlighting and code execution.
- Includes a documentation compiler.
- A language server prototype is in development.

**Compiler DevOps:**
- Offers development container support for easy setup.
- Supports SPM/CMake, Ninja/Xcode, Windows/Linux/macOS.
- Includes a test generation compiler plugin.
- Provides pre-built Hylo development toolchain Docker images.
- The compiler is written in Swift 6.2.

## Research Around Hylo
Several research papers have been published on Hylo, covering topics such as:
- Ownership of doubly-linked list contents.
- High-fidelity C interoperability.
- Debugging Hylo.
- The state of coherence in type classes.
- Type checking with rewriting rules.
- The potential harms of use site checking.
- Method bundles.
- Borrow checking in Hylo.
- The Val object model.
- Generics and value semantics.
- Implementation strategies for mutable value semantics.
- A vision for memory safety.
- Native implementation of mutable value semantics.
- A formal definition of Swift's value semantics.

Interested in research collaboration? Contact the authors to learn about topics or suggest new ones.

## Talks
Hylo has been presented at various conferences:
- **ConcConcurrency Hylomorphism** by Lucian Radu Teoedorescu (ACCU, 2024-07) - Keynote.
- **Hylo: The Safe Systems and Generic-programming Language Built on Value Semantics** by Dave Abrahams (C++ on Sea, 2024-07).
- **HyloDoc: A Documentation Compiler for Hylo** by Ambrus Tóth (C++ on Sea, 2024-06).
- **Borrow checking Hylo** by Dimi Racordon (IWACO, 2023-05).
- **ConcConcurrency Approaches: Past, Present, and Future** by Lucian Radu Teoedorescu (ACCU, 2023-04).
- **Val: A Safe Language to Interoperate with C++** by Dimi Racordon (CppCon, 2022-09).
- **Value Semantics: Safety, Independence, Projection, & Future of Programming** by Dave Abrahams (CppCon, 2022-09) - Keynote.
- **An Object Model for Safety and Efficiency by Definition** by Dave Abrahams (CppNorth, 2022-07) - Keynote.
- **A Future of Value Semantics and Generic Programming Part 1 & 2** by Dave Abrahams & Dimi Racordon (C++Now, 2022-05).
- **Structured Concurrency** by Lucian Radu Teoedorescu (ACCU, 2022-04).

## Podcasts
Hylo has been discussed on the following podcasts:
- **Sean Parent on Hylo! (Part 2)** (ADSP #138, 2023-07-14).
- **Sean Parent on Hylo (vs Rust)!** (ADSP #137, 2023-07-07).
- **Val and Mutable Value Semantics** (CppCast #352, 2023-01-20) by Dimi Racordon.

## Working Examples
Despite being in early stages, working examples demonstrate Hylo's capabilities:

- **Subscripts - A Safe Projection Mechanism:** Demonstrates safe projection using inout.
- **Sink Methods - Capability for Deinitialization:** Illustrates the use of sink methods for controlled shutdown of resources.
- **CustomMove:** Shows a custom movable type with witness tracking.

More examples can be found in the compiler test suite.
