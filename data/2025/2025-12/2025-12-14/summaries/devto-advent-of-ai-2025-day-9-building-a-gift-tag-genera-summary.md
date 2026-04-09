---
title: Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes - DEV Community
url: https://dev.to/nickytonline/advent-of-ai-2025-day-9-building-a-gift-tag-generator-with-goose-recipes-3i73
date: 2025-12-12
site: devto
model: llama3.2:1b
summarized_at: 2025-12-14T11:22:01.778010
screenshot: devto-advent-of-ai-2025-day-9-building-a-gift-tag-genera.png
---

# Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes - DEV Community

## Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes
===============================================================

The article discusses an experiment involving building a gift tag generator using the Goose open source AI agent. Here are the key points:

*   The creator leverages Goose, an accessible and extensible AI engine that can automate various engineering tasks.
*   Goose supports complex development workflows from scratch, including writing code, executing it, debugging failures, and orchestrating workflows without human intervention.
*   The author describes Goose as a "local, extensible, open source AI agent" capable of automating tasks with precision and flexibility. The agent integrates smoothly with MCP servers for seamless workflow execution.

## Building the Gift Tag Generator Recipe
------------------------------------------

The article highlights four different styles (elegant, playful, minimalist, festive) that can be customized using a Goose recipe:

*   **Elegant**: Four distinct styles to choose from.
*   **Playful**: Supports multiple languages and AI-generated poems.
*   **Minimalist**: No font sizes or text sizes are allowed.
*   **Festive**: Reduces font sizes and uses the developer extension to ensure content is visible.

## Key Benefits of Using Goose
------------------------------

The author highlights several benefits of using Goose:

*   High efficiency: Goose automates tasks, saving development time.
*   Flexibility: Supports various LLMs for seamless integration with MCP servers.
*   Customization: Allows choosing from four predefined styles and modifying them as needed.

## Code Example (Goose Recipe)
---------------------------

The full recipe is provided on GitHub. However, the article includes a simplified example that demonstrates how to use Goose to generate print-ready gift tags:

```goose
title "Gift Tag"

input {
  kind = "text"
}

body {
  text: select style, html, font-size
}

style {
  body-style() {
    -content-truncate-on-content-overflow;
    padding-bottom: auto;
  }
}
```

## Key Takeaways and Limitations
-------------------------------

The article mentions several key points:

*   Goose is an accessible AI engine that can automate engineering tasks.
*   It supports complex development workflows from scratch, including code execution and debugging improvements.
*   The author cautions that customizing styles requires additional HTML elements.

However, it also highlights potential limitations:

*   Requires technical expertise to implement custom styles.
*   May not work correctly for older browsers or those with specific rendering issues.
