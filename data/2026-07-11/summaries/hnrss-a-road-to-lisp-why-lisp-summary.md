---
title: A road to Lisp: Why Lisp
url: https://scotto.me/blog/2026-07-09-why-lisp/
date: 2026-07-09
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:40:31.175608
---

# A road to Lisp: Why Lisp

# A road to Lisp: Why Lisp

## Introduction
- First encounter with Lisp often feels confusing because of many parentheses, indentation, and unconventional use of `format`.
- Learning Lisp requires mastering packages, symbols, project setup, REPL, conditions, and restarts, as well as a new way of constructing algorithms.
- Although Lisp has a steep learning curve, it offers capabilities unavailable in most other languages, giving programmers greater power and flexibility.
- Paul Graham’s “Blub paradox” explains why programmers accustomed to less powerful languages struggle to appreciate Lisp’s advantages.
- The article aims to highlight several Lisp features that make it worth learning, even if one ultimately uses another language.

## Extensibility
- Lisp is described as “the programmable programming language” because it can be extended from within.
- The macro system is the key to this extensibility; unlike C/Rust/Swift macros, Lisp macros can create new language constructs rather than just eliminating boilerplate.
- Example: a `while` macro is defined using `defmacro`, which expands into a `loop` with `progn` to execute a body repeatedly.
- Using the macro simplifies code compared to writing the underlying `loop` form directly.
- Attempting to implement the same behavior with a regular function (`defun fake-while`) fails because function arguments are evaluated before the function runs, leading to type errors.
- Macros keep their arguments unevaluated, treating them as data (lists), and later expand them into executable code via `macroexpand`.
- This ability to manipulate code as data is what makes Lisp uniquely extensible.

## Lists All the Way Down
- Lisp programs consist of symbolic expressions (s-expressions), which are either atoms (numbers, strings, symbols) or lists of atoms/lists.
- Because both code and data are represented as lists, Lisp exhibits **homoiconicity**: the program’s structure is the same as its primary data structure.
- Example: evaluating `(+ 1 2)` yields `3`, while quoting the same list (`'( + 1 2)`) returns the list itself without evaluation.
- This uniform representation enables powerful metaprogramming techniques, such as macros, and reinforces the language’s flexibility.

## Impact on Programming Mindset
- Working with Lisp forces a shift in thinking: programmers learn to grow the language toward the problem rather than forcing the problem into a fixed language.
- Even if Lisp is not adopted long‑term, the experience broadens one’s perspective on what programming languages can achieve.