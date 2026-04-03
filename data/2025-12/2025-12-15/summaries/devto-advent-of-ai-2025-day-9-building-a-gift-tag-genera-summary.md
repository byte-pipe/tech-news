---
title: Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes - DEV Community
url: https://dev.to/nickytonline/advent-of-ai-2025-day-9-building-a-gift-tag-generator-with-goose-recipes-3i73
date: 2025-12-12
site: devto
model: llama3.2:1b
summarized_at: 2025-12-15T11:19:33.325840
screenshot: devto-advent-of-ai-2025-day-9-building-a-gift-tag-genera.png
---

# Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes - DEV Community

## Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes

### The Advent of AI Challenge: Print-Ready Gift Tags

A new recipe was built by the author using the open source Goose AI agent to generate print-ready gift tags. This implementation allows for customizable designs, flexible sizes (4x3 inch, 5x4 inch, and fixed dimensions), multiple languages, QR codes, and AI-generated poems.

### Key Points:

* The fixed size challenge arose when attempting to generate tags with varying content.
* By setting explicit constraints in the recipe, a solution was found by:
    + Ensuring all content fits within specified dimensions
    + Reducing font sizes if necessary for visual clarity
    + Utilizing the developer extension for validation against edge cases

## Summary of Key Points

- Setting explicit constraints using CSS and developer extensions ensures that all content is visible on print-ready gift tags.
- Flexible size options (4x3 inch, 5x4 inch) can be accommodated with careful font sizing adjustments.
- The Goose recipe adapts to various design styles and languages.
- Integration with external resources such as MCP servers and CLI tools is seamless.
