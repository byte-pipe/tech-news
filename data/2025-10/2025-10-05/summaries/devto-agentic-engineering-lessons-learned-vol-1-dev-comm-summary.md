---
title: Agentic Engineering: Lessons Learned Vol. 1 - DEV Community
url: https://dev.to/duske/agentic-engineering-lessons-learned-vol-1-jbj
date: 2025-09-29
site: devto
model: llama3.2:1b
summarized_at: 2025-10-05T11:27:49.413092
screenshot: devto-agentic-engineering-lessons-learned-vol-1-dev-comm.png
---

# Agentic Engineering: Lessons Learned Vol. 1 - DEV Community

**Context Engineering 101**

* Context engineering is a crucial aspect of agentic engineering, as it defines what information an LLM receives to perform tasks.
* In software development, the context is the input that provides necessary information for the model to function correctly.
* The context can be thought of as a composite entity with multiple parts, including instructions (prompt), knowledge, tools, and more.

**Mental Model**

The understanding of the context is essential to designing effective LLMs. We can think of this mental model like a function that takes in the input and generates the output:
```
Context
= Instructions | Knowledge | Tools

agent
(
context
)
-> output
```

**Key Takeaways**

1.  The context determines the outcome, but it's not just the prompt.
*   Instructions (e.g., spec or examples): Provide additional information for the model to understand.
*   Knowledge: Includes documentation and facts/memories that build upon each other.
*   Tools: Regular interactions like reading files, calling external scripts, or using MCP servers.

**Common Pitfalls**

1.  **Context Poisoning**: Repeating an error or hallucination within the context can lead to confusion and errors.

These insights from expert work have been valuable for our team, and we're sharing practical strategies you can use today:

*   Using examples as instructions (especially in language model design)
*   Incorporating documentation into the knowledge base
*   Implementing regular tool interactions or calls

**Additional Read**

For more information, check out Drew Breunig's insightful post on context engineering.

**Validation and Best Practices**

As with any solution, it's essential to validate these strategies for your specific use case. We encourage you to explore resources like the Claude Code community and expert articles before implementing them in your projects. While we have found that these insights are valuable, please keep in mind that results may vary depending on your unique situation.

By mastering a deeper understanding of context engineering, you'll be well-equipped to address its challenges and unlock the full potential of LLMs.
