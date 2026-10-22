---
title: Rust Style Guide | Google Style Guides
url: https://google.github.io/styleguide/rustguide.html
date: 2026-10-21
site: hnrss
model: llama3.2:1b
summarized_at: 2026-10-22T16:18:49.296782
---

# Rust Style Guide | Google Style Guides

## Rust Style Guide (Chrome)

### Background

* The Rust Style Guide is designed to provide a comprehensive set of guidelines for writing clean, efficient, and maintainable Rust code.
* The guide is intended to be followed by all contributors to the Chrome Rust library.

### Scope

* Applies to all Rust code within the Chrome Rust library, including APIs, code organization, and overall coding style.

### Goals

* To create a unified coding style across all Chrome Rust contributors
* To ensure a consistent and high-quality coding experience
* To facilitate collaboration and development efforts

### Public Rust Style Rules

* Follow public Rust style rules throughout the library
* API design should align with public Rust standards
* Code organization should be modular and prioritizing small crates
* For `rust_library` files, use flat file layout
* Favor `rust_library` over other sources
* Avoid non-leaf modules for API design
* Don't implement APIs in non-leaf modules
* Use glob imports for source file organization
* Prefer local scoped trait imports
* Qualify top-level function calls with module names
* Use appropriate import mechanisms
* Code formatting and aesthetics should adhere to Rust standard
* Opt for auto-formatting (but not all time), use correct ownership and borrowing
* Avoid `Rc` and `Arc` unless necessary
* Prefer borrows over deep copies
* Implement known standard library traits
* Prefer named fields over tuples and non-newtype structs
* Traits should be added when necessary, implement known standard library traits instead of custom methods
* Avoid `#[derive]` unless possible
* Prefer generics over `dyn Trait`

### Naming Conventions

* Naming methods, naming lifetimes, naming generic parameters, naming extension traits, naming initialization functions, avoid abbreviations
* Prefer `const` functions for responsible use
* Use `format!` and `write!` for concatenation and substitution

### Documentation

* Respect `# doc hidden` and `# non_exhaustive`
* Use `#[must_use]` on functions, `#[must_use]` on types and functions
* Don't run code before `main()`
* Apply `[non_exhaustive]` to publicly exposed enums and structs with public fields
* Apply `[non_exhaustive]` to publicly exposed structs with public fields and types

### Implementation Concerns

* Prefer pattern matching over check-then-unwrap
* Prefer `expect` over `unwrap`
* Don't omit patterns on non-exhaustive enums when matching
* Use context strings to clarify assertions

### Code Optimization

* Don't call `panic::catch_unwind` (prefer `format!` and `write!`)
* Don't prefer format! and write! over direct iteration when direct iteration is clearer
* Don't use iterator combinator chains when direct iteration is clearer

## Background
The Rust Style Guide is designed to provide a comprehensive set of guidelines for writing clean, efficient, and maintainable Rust code. The guide is intended to be followed by all contributors to the Chrome Rust library.

## Scope
The Rust Style Guide applies to all Rust code within the Chrome Rust library, including APIs, code organization, and overall coding style.

## Goals
The Rust Style Guide aims to create a unified coding style across all Chrome Rust contributors, ensure a consistent and high-quality coding experience, and facilitate collaboration and development efforts.

## Public Rust Style Rules
To follow public Rust style rules throughout the library, api design should align with public Rust standards, code organization should be modular, favoring small crates, use flat file layout for `rust_library` sources, and avoid `Rc` and `Arc` unless necessary.

## Naming Conventions
Avoid using abbreviations when and how document code. Instead, focus on providing accurate and clear documentation. Respect `# doc hidden` and `# non_exhaustive`. Use `#[must_use]` on functions, `#[must_use]` on types and functions, and include context strings to clarify assertions.

## Implementation Concerns
Prefer pattern matching over check-then-unwrap, prefer `expect` over `unwrap`, and avoid omitting patterns on non-exhaustive enums when matching. Use `format!` and `write!` for concatenation and substitution.

## Code Optimization
Prefer direct iteration over iterator combinator chains. Don't call `panic::catch_unwind` and prefer `format!` and `write!` over direct iteration when using direct iteration is clearer.

## Conclusion
The Rust Style Guide aims to provide a comprehensive set of guidelines for writing clean and maintainable Rust code. It aims to ensure a consistent and high-quality coding experience, and facilitate collaboration and development efforts.