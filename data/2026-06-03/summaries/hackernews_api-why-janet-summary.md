---
title: Why Janet?
url: https://ianthehenry.com/posts/why-janet/
date: 2026-06-02
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-03T01:52:01.905265
---

# Why Janet?

# Why Janet?

## Janet is simple
- An imperative language with first‑class functions, a single identifier namespace, and lexical block scoping.  
- Core consists of only eight instructions: `do`, `def`, `var`, `set`, `if`, `while`, `break`, `fn`.  
- Macros provide high‑level wrappers for richer control flow.  
- Runtime semantics feel like JavaScript without the “wats”; the whole standard library fits on one page.  
- Can be learned in an afternoon, which is how I first got hooked.

## Janet is distributable
- Programs compile to native executables that statically link the Janet runtime.  
- No need for users to install Janet or any dependencies; the binary runs on its own.  
- Compilation process: Janet → bytecode → C file → system C compiler → native binary.  
- A simple “hello world” binary is under 1 MB (≈784 KB on aarch64 macOS) and includes the runtime, GC, and bytecode compiler, enabling runtime evaluation of Janet code.  
- Ideal for small command‑line tools.

## Janet is unrealistically good at parsing text
- Uses parsing expression grammars (PEGs) instead of regular expressions.  
- PEGs are simpler, more powerful, and deterministic, handling multi‑line text, HTML, JSON, binary formats, and null bytes.  
- Parsers are first‑class, composable, and easy to learn.

## Janet has the best subprocess DSL of any high‑level language
- Third‑party library **sh** provides a shell‑scripting DSL for pipes and redirects directly in Janet, e.g. `($ find . -name *.janet | say)`.  
- The DSL is powerful enough to position Janet as an alternative to both Perl and Bash for many tasks.

## Janet is embeddable
- The Janet runtime is a small C library; embedding requires linking and calling regular C functions.  
- Can be embedded in applications, websites, or static sites with custom DSLs, offering scripting interfaces similar to Lua but with Janet’s features.

## Janet has mutable and immutable collections
- Collections exist in mutable and immutable variants.  
- Immutable collections have value semantics (e.g., `vector[1 2]` equals `(take 2 [1 2 3])`).  
- Mutable collections have reference semantics (e.g., a hash table is only equal to itself).  
- Immutable composite values are built into the standard library, which is uncommon.

## Macros, macros, macros
- Macros are optional but fun; they let you write code that writes code.  
- Requires managing two execution contexts: compile‑time (manipulating ASTs) and run‑time (generated code).  
- Janet’s macros are not hygienic and share the function namespace, but unquoting literal functions enables referentially transparent macros, offering a simple solution to a complex problem.

## Janet lets you pass values from compile‑time to run‑time
- Any Janet value can be serialized to disk implicitly when a program is compiled.  
- Top‑level instructions execute, then a snapshot of the program’s state is written, preserving shared references, mutable values, generator positions, and closures.  
- This enables compile‑time side effects without macros: pre‑compute data, embed assets, generate code from schemas, etc.

## Janet feels good in the hand
- Syntax balances simplicity, uniformity, and variety.  
- Uses pervasive parentheses, with `[]` for lists and `{}` for tables.  
- Mutable literals prefixed with `@` (e.g., `@:"mutable string"`).  
- Anonymous functions: `(fn [x] (+ 1 x))`; shorthand `|` lifts any expression into a function (`|(+ 1 $)`).  
- Supports splats/spreads with `;` (e.g., `(+ ;args)`).  
- String literals can use any number of backticks, avoiding escape sequences and allowing any content.