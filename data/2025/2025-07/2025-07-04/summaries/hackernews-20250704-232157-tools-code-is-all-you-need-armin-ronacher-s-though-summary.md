---
title: "Tools: Code Is All You Need | Armin Ronacher's Thoughts and Writings"
url: https://lucumr.pocoo.org/2025/7/3/tools/
date: 2025-07-04
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-04T23:21:57.645992
---

# Tools: Code Is All You Need | Armin Ronacher's Thoughts and Writings

**Analysis**

The article by Armin Ronacher discusses the challenges and limitations of Model Context Protocol (MCP), an AI tool designed to help developers generate code automatically. Ronacher highlights two main flaws in MCP:

1. **Inference over composition**: MCP struggles with context input, instead using inference to compose the generated code.
2. **High contextual consumption**: MCP consumes significant upfront input and requires even more context than writing and running code.

Ronacher also expresses surprise that his stance on MCP is a criticism and acknowledges the limitations of the tool in certain scenarios. He notes that MCP might not be suitable for general code generation due to its reliance on inference, but rather for end-user applications like automating domain-specific tasks in financial companies.

**Market Indicators**

There are no specific market indicators mentioned in the article. However, it's essential to note that Ronacher is an independent developer and does not have direct access to user adoption, revenue, or growth metrics.

**Technical Feasibility**

Ronacher mentions several technical challenges:

1. **Complexity**: MCP requires a layer of filtering to ensure correct tool invocation.
2. **Required skills**: Writing a custom shell script for specific tasks can be difficult, especially for non-technical users.
3. **Time investment**: Building and maintaining an integration with other tools (if needed) requires significant effort.

**Business Viability Signals**

Ronacher concludes that MCP is not suitable for all workflows and individuals:

1. **Domain-specific tasks without code generation**: Even in these cases, code generation is often the better choice due to its ability to compose.
2. **Non-technical users**: MCP might be challenging or impractical for non-technical users who need a simple, automated solution.

**Actionable Insights**

Based on this analysis:

1. Consider replacing MCP with A Shell Script for specific tasks that don't require code generation.
2. Develop custom tools and integrations to meet the needs of domain-specific applications where code generation is more suitable.
3. Consider alternative solutions when working as a non-technical user or in niche environments where manual coding skills are not feasible.

By understanding Ronacher's thoughts on MCP, developers can identify potential workflow scenarios where A Shell Script could be used effectively, making it an actionable insight for building profitable solo developer businesses.
