---
title: jank now has its own custom IR
url: https://jank-lang.org/blog/2026-05-08-optimization/
date: 2026-05-16
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-19T06:02:33.586733
---

# jank now has its own custom IR

# jank now has its own custom IR

## What is an intermediate representation (IR)?
- Compilers use IRs to express programs at a level abstracted from the target CPU instruction set.  
- Benefits include portability across architectures (e.g., x86_64, arm64) and easier implementation of optimizations such as SSA form.  
- IR designers can choose the abstraction level to match language semantics, making the IR more general or language‑specific.  
- Common IRs: JVM bytecode, .NET CIL, GCC GIMPLE, LLVM IR, etc., and some compilers pass through multiple IRs.

## Custom IR rationale
- Historically jank delegated optimization to LLVM, generating C++ or LLVM IR.  
- LLVM IR is low‑level and lacks concepts native to Clojure (vars, transients, persistent data structures, lazy sequences), limiting optimization opportunities.  
- A higher‑level IR that reflects Clojure’s semantics can enable more powerful, language‑aware optimizations.  
- Because jank is not a general VM, the IR can be specialized for jank alone, offering greater optimization potential.  
- No other Clojure dialect has adopted this approach so far.

## Custom IR details
- The IR specification is documented in the jank book; it is stored as C++ data structures but can be rendered to Clojure data for debugging.  
- Example Clojure function `greet` is shown alongside its IR representation, which includes:
  - Lifted vars and constants.  
  - SSA‑based naming (each name assigned once).  
  - Control‑flow graph composed of basic blocks with a single terminating instruction.  
  - Instructions that operate at the level of Clojure semantics (e.g., `var-deref`, `dynamic-call`).  
- Generated C++ code mirrors the IR:
  - Variable names correspond to IR names.  
  - Var dereference becomes a call to `->deref()`.  
  - Dynamic calls become `jank::runtime::dynamic_call`.  
  - This direct mapping is intentional to keep the pipeline transparent.

## Optimizing the IR
- Six weeks were spent designing the IR and reworking C++ code generation to emit from the IR rather than directly from the AST.  
- At present no optimization passes are applied, but the infrastructure is ready.  
- Future work will target benchmarks one by one (starting with recursive Fibonacci), adding IR‑level optimizations until no further gains are possible.  
- Additional technical details are available in videos on the jank TV YouTube channel, which dive into the implementation specifics.

## Interlude / call to action
- The author thanks current sponsors and Clojurists Together, and encourages new sponsorships to support full‑time work on jank.  
- Viewers are invited to subscribe to the jank TV channel for more updates.