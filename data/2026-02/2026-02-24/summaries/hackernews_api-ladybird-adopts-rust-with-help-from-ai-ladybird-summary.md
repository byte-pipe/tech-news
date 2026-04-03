---
title: Ladybird adopts Rust, with help from AI - Ladybird
url: https://ladybird.org/posts/adopting-rust/
date: 2026-02-23
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-24T06:01:42.894090
---

# Ladybird adopts Rust, with help from AI - Ladybird

# Ladybird adopts Rust, with help from AI

* Ladybird is transitioning from C++ to Rust for memory-safe programming, aiming to replace C++ in parts of the codebase.
* Previous attempts with Swift faced challenges with C++ interoperability and limited platform support outside the Apple ecosystem.
* Rust was initially rejected in 2024 due to its incompatibility with Ladybird's 1990s OOP style, but the pragmatic choice has now shifted towards Rust's mature systems programming ecosystem and existing contributor knowledge.
* The initial porting effort focused on LibJS, Ladybird's JavaScript engine, due to its relatively self-contained nature and extensive test coverage.
* AI tools like Claude and Codex were used for the translation, with human direction overseeing the process, including deciding on the order and structure of the Rust code.
* The porting of LibJS resulted in approximately 25,000 lines of Rust code, completed in about two weeks, which would have taken months manually.
* Extensive testing, including verification of byte-for-byte identical output between C++ and Rust pipelines and regression tests, confirms zero regressions in test suites, regression tests, and test262.
* Performance testing also shows no performance regressions on JavaScript benchmarks.
* The initial Rust code prioritizes compatibility with the existing C++ pipeline, intentionally mimicking C++ patterns for bytecode compatibility.
* Future Rust porting will be a gradual, side-track effort managed by the core team, with coordinated efforts to ensure seamless integration with the existing C++ codebase.
* This decision is considered crucial for Ladybird's future, despite potential controversy.
