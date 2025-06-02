---
date: 2025-06-01
description: 'The venerable master Foo was walking with a novice. Hoping to prompt
  the master into a discussion, the novice said: "Master, I have heard that property-based
  tests are a very good thing - is this...

  '
enhanced_prompting: true
fetched_at: '2025-06-01T01:56:19.664567

  '
local_model: true
model: gemma3:27b
original_url: 'https://blog.snork.dev/posts/a-poor-man-s-types.html

  '
site_name: lobsters
summarization_type: local_high_quality
summarized_at: '2025-06-01T01:58:53.388219'
summary_type: local_high_quality
tags: plt
title: "A poor man\u2019s types"
url: 'https://blog.snork.dev/posts/a-poor-man-s-types.html

  '
---

• Here's a technical summary of the "A poor man’s types" article, formatted as requested:
• **Core Concept: Hierarchy of Confidence:** The article illustrates a hierarchy of program correctness assurance: Tests are a basic level, Types offer a stronger guarantee, and ideally, a robust type system *replaces* the need for extensive testing. This isn’t about dismissing tests, but recognizing types provide *static* guarantees, catching errors at compile time rather than relying on *dynamic* runtime checks.
• **Types as Preconditions & Invariants:** The core insight is that a well-defined type system effectively encodes preconditions and invariants about data. This allows the compiler to *prove* correctness based on the code’s structure and type definitions, reducing reliance on runtime assertions (tests) to verify these properties.
• **Shift in Focus: From Verification to Prevention:** The article advocates a move from a verification-based approach (testing to *find* errors) to a prevention-based approach (types to *prevent* errors). This aligns with principles of defensive programming and aims to build more reliable software through static analysis.
