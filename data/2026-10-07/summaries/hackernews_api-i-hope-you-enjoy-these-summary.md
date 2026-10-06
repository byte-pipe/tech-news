---
title: I hope you enjoy these
url: https://www.vivienhenz.com/common-lisp
date: 2026-10-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-07T06:01:13.063977
---

# I hope you enjoy these

# Why Common Lisp Is Now the Best Programming Language

## Core Claim
- The author argues that Common Lisp is the best language today, especially when paired with large language models (LLMs) that generate code.

## Feedback Loop Advantage
- LLMs produce code instantly, making the time to verify correctness the new bottleneck.
- Common Lisp’s image‑based environment eliminates separate read, compile, and runtime phases, allowing functions to be redefined instantly without restarting the program.
- Errors invoke an interactive debugger instead of crashing, enabling an LLM to inspect the stack and variables, fix the issue, and resume execution.

## Language Features that Aid LLM‑Driven Development
- Code and data share the same list structure, enabling programs to manipulate their own code.
- Macros are functions that transform code into new code, allowing developers to extend the language with domain‑specific constructs.
- By building a domain‑specific language (DSL) on top of Lisp, companies can embed their design opinions directly into the product, making user‑driven customization safer and more coherent.

## Economic and Practical Benefits
- Lisp programs tend to be far more concise; the author’s Lisp applications are 6–7 times shorter than comparable Python versions.
- Shorter code reduces token usage for LLMs, lowering development costs and keeping more of the program within the model’s context window, which improves the quality of LLM suggestions.
- The ANSI Common Lisp standard has been stable since 1994, so user‑written extensions remain compatible over time.

## Ecosystem Considerations
- While Quicklisp offers far fewer packages than npm, the author views this as an advantage: reliance on fewer third‑party libraries reduces supply‑chain risk.
- LLMs can generate missing functionality or port existing libraries, mitigating the smaller ecosystem.

## Talent and Adoption
- Concern about the scarcity of Lisp engineers is downplayed; hiring adaptable, fast learners and training them in Common Lisp is presented as a viable strategy.

## Conclusion
- For rapid, LLM‑assisted development, concise code, stable language semantics, and powerful macro facilities, the author recommends choosing Common Lisp for new projects.