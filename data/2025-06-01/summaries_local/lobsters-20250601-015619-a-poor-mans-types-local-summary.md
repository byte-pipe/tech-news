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
summarized_at: '2025-06-01T23:49:22.414098'
summary_type: local_high_quality
tags: plt
title: "A poor man\u2019s types"
url: 'https://blog.snork.dev/posts/a-poor-man-s-types.html

  '
---

• Here's a technical summary of the article "A poor man’s types", formatted as requested:
• **Core Concept: Hierarchy of Verification Techniques:** The article presents a hierarchy of program verification methods, positioning tests as a weaker form of type systems, and type systems as a weaker form of more robust formal verification. This implies that strong static typing provides *more* assurance than relying solely on runtime tests.
• **Types as Implicit Specifications:** The core insight is that type systems act as implicit specifications of program behavior. By enforcing constraints at compile time, types *prevent* certain classes of errors that tests can only *detect* after the program is running. This shifts error detection from runtime to compile time, improving reliability.
• **Trade-offs & Practical Implications:** The "poor man's" framing highlights a trade-off. Tests are easier to implement initially, but offer weaker guarantees. Types require more upfront investment in defining and maintaining, but provide stronger, static guarantees about program correctness. This impacts design choices, especially in safety-critical or high-reliability systems.
