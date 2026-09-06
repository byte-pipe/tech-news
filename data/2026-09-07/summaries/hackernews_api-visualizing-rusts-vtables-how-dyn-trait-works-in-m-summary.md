---
title: "Visualizing Rust's Vtables: How dyn Trait Works In Memory"
url: https://sofiabelen.github.io/projects/visualizing-rusts-vtables-how-dyn-trait-works-in-memory/
date: 2026-09-05
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-09-07T08:08:12.528058
---

# Visualizing Rust's Vtables: How dyn Trait Works In Memory

# Visualizing Rust's Vtables: How dyn Trait Works In Memory

## Introduction
- Goal: understand how Rust implements polymorphism and compare it with C++ approaches.  
- Focus on memory layout of static vs. dynamic dispatch, zero‑sized types (ZST), and the `dyn Trait` “fat pointer”.

## C++ Polymorphism Approaches
- **Virtual functions**  
  - Runtime polymorphism via a vtable pointer stored inside each object.  
  - Example: `std::vector<Shape*> shapes = {new Circle(), new Square()};` then `s->draw();`.
- **CRTP (Curiously Recurring Template Pattern)**  
  - Compile‑time polymorphism; no vtables, code is monomorphized per concrete type.  
  - Syntax is verbose; Rust’s generic monomorphization provides a cleaner equivalent.

## Rust Static Dispatch (Generics / Monomorphization)
- Defined by a trait (`Draw`) and generic function `draw_shape<T: Draw>(shape: T)`.
- Compiler generates a separate version of `draw_shape` for each concrete type (`Circle`, `Square`), eliminating runtime cost.
- Comparison with C++ templates:  
  - C++ templates infer constraints (any type with a `draw` method).  
  - Rust requires an explicit trait implementation, making the contract clear.

## Zero‑Sized Types (ZST) in Rust
- Structs without fields (or only ZST fields) have size `0`.  
- Rust guarantees distinct ownership rather than distinct addresses; the borrow checker enforces identity at compile time.
- Taking the address of a ZST:
  - Debug builds allocate a dummy byte for debugger visibility, yielding distinct stack addresses.  
  - Release builds collapse the addresses, showing no guarantee about ZST locations.

## Rust Dynamic Dispatch (`dyn Trait`)
- Function signature changes from generic `T: Draw` to `&dyn Draw`.
- Size difference:
  - `&Circle` → 8 bytes (single pointer).  
  - `&dyn Draw` → 16 bytes (fat pointer: data pointer + vtable pointer).
- The vtable contains pointers to the concrete implementation of each trait method; dispatch occurs at runtime.

## Inspecting the Fat Pointer
- By casting `&dyn Draw` to a raw tuple of two pointers, one can view:
  - The data pointer (address of the concrete value).  
  - The vtable pointer (address of the table containing method addresses).
- Example inspection code shows the two components and confirms that the vtable is shared among all instances of the same concrete type.

## Takeaways
- **Static dispatch** in Rust mirrors C++ CRTP: compile‑time code generation, zero runtime overhead, but requires explicit trait bounds.  
- **Zero‑sized types** break the C++ assumption that every object occupies at least one byte; Rust tracks identity via ownership, not memory addresses.  
- **Dynamic dispatch** uses a fat pointer (`&dyn Trait`) consisting of a data pointer and a vtable pointer, enabling runtime polymorphism similar to C++ virtual functions but with a distinct memory representation.  
- Understanding these mechanisms clarifies why Rust’s approach to polymorphism is fundamentally different from C++ and highlights the language’s safety‑first design.