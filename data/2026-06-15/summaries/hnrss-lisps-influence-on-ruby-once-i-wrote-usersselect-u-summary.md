---
title: Lisp’s Influence on Ruby. Once I wrote users.select { |u|… | by Ian Johnson | Jun, 2026 | Medium
url: https://blog.tacoda.dev/lisps-influence-on-ruby-6a54f1a7740e
date: 2026-06-11
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-15T06:01:38.375314
---

# Lisp’s Influence on Ruby. Once I wrote users.select { |u|… | by Ian Johnson | Jun, 2026 | Medium

# Lisp’s Influence on Ruby

## Method names with question marks
- Predicate methods end with `?` (e.g., `nil?`, `empty?`, `admin?`) – a convention borrowed from Scheme.  
- The suffix signals a yes‑or‑no answer, no mutation, and makes code read like English.  
- The complementary `!` suffix marks mutating or exception‑raising methods (e.g., `save!`, `compact!`).

## Closures and blocks
- Ruby blocks are closures: they capture surrounding variables (`total` in the example) and can be passed around.  
- Syntax is lighter than Lisp’s parentheses; `do…end` or `{}` replace them.  
- Procs and lambdas (`->(n) { … }`) re‑introduce explicit parentheses, mirroring Lisp’s lambda calculus.

## First‑class functions
- Once closures can be named, functions become values that can be stored, returned, or attached to objects.  
- Ruby’s `Method` and `Proc` classes, plus the `&:method_name` shorthand, enable seamless function composition.  
- This follows Lisp’s core idea that programs are built by composing functions.

## Symbols
- Symbols (`:foo`) are interned identifiers: every occurrence refers to the same object, unlike separate string instances.  
- Originates from Lisp atoms; provides fast equality, hashing, and a clean way to refer to method names (`:save`, `:to_s`).  
- Used heavily in hashes, reflective calls (`send(:save)`), and the `&:foo` shortcut.

## Collection methods
- Enumerable methods (`map`, `select`, `reduce`, `flat_map`, etc.) mirror Lisp’s `mapcar`, `filter`, `reduce`.  
- They operate on whole collections without explicit indices or manual accumulators.  
- Method chaining (`users.select {…}.map(&:email)`) reads like a sentence, a direct inheritance of Lisp’s functional style.

## Lazy enumerators
- Ruby’s `Enumerable#lazy` provides lazy evaluation similar to Lisp’s streams and Scheme’s `delay/force`.  
- Operations are composed without materializing intermediate arrays, enabling efficient handling of large or infinite sequences.  
- Example: an infinite range processed with `lazy.select…map…first(5)` computes only the needed elements.

## Duck typing
- Ruby adopts the “if it walks like a duck…” principle: methods rely on an object’s behavior, not its class.  
- This dynamic, behavior‑focused typing echoes Lisp’s dynamic typing tradition and Smalltalk’s message‑sending model.  
- Example: `def render(thing); thing.to_s; end` works for any object responding to `to_s`.

## Overall perspective
- Matz described Ruby’s design as starting from a simple Lisp, stripping macros and s‑expressions, then adding an object system, blocks, and Smalltalk‑style methods.  
- The features Rubyists love most—predicate naming, closures, first‑class functions, symbols, collection pipelines, laziness, and duck typing—are functional ideas originally forged in Lisp, now dressed in Ruby’s “business‑casual” syntax.