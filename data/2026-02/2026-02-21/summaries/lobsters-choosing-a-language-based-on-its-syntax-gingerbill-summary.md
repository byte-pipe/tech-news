---
title: Choosing a Language Based on its Syntax? - gingerBill
url: https://www.gingerbill.org/article/2026/02/19/choosing-a-language-based-on-syntax/
date: 2026-02-21
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-21T06:01:49.578884
---

# Choosing a Language Based on its Syntax? - gingerBill

# Choosing a Language Based on its Syntax? - gingerBill

This article discusses the common tendency for programmers to choose a language based on its syntax rather than its underlying semantics. The author argues that syntax is secondary to semantics, and that a language's character is primarily defined by its semantics, not its appearance.

## Key Points:

* **Declaration Syntax Variations:** Languages offer different styles for declaring variables and functions (e.g., type-focused, name-focused, qualifier-focused). These variations primarily affect ergonomics and typing needs, with the core compiler functionality remaining largely the same.
* **Semantics are Fundamental:** The denotational semantics (meaning) of a language are more important than its operational semantics (how it's executed). Many inexperienced programmers fail to recognize this distinction.
* **Semicolons:** The presence or absence of semicolons is a frequent point of contention. The author advocates for making them optional for cleaner and more consistent grammar, citing Odin as an example.
* **First Exposure Bias:** Programmers often develop a preference for the first language they encounter, even if it's not the most semantically suitable choice.
* **Syntax Can Imply Semantics:** While syntax doesn't inherently define semantics, inconsistent or overly complex syntax can hinder readability and understanding. Examples like Perl are mentioned as languages with syntax that can be difficult to parse.
* **Trade-offs in Syntax:** Syntax choices involve trade-offs. For instance, optional semicolons require careful grammar design to ensure clarity, while automatic semicolon insertion (ASI) can lead to unexpected behavior if not implemented carefully.

## Odin as an Example:

The author uses Odin as an example to illustrate how even fundamental syntax choices like optional semicolons can be debated and have significant implications for the language's usability and consistency.
