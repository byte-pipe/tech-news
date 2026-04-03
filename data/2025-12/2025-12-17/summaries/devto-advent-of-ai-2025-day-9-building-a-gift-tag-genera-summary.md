---
title: Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes - DEV Community
url: https://dev.to/nickytonline/advent-of-ai-2025-day-9-building-a-gift-tag-generator-with-goose-recipes-3i73
date: 2025-12-12
site: devto
model: llama3.2:1b
summarized_at: 2025-12-17T11:18:30.982601
screenshot: devto-advent-of-ai-2025-day-9-building-a-gift-tag-genera.png
---

# Advent of AI 2025 - Day 9: Building a Gift Tag Generator with Goose Recipes - DEV Community

## Advent of AI 2025 - Day 9: Building a Gesture-Enabled Gift Tag Generator with Goose Recipes

### Quick Solution for Gift Tags

To generate print-ready gift tags with ease, I created a recipe built using Goose, an open-source AI agent. This solution allows users to input the gift details and automatically generates complete HTML files ready to print.

### Key Features of the Solution

* Handles fixed dimensions (3x2, 4x3, or 5x4 inch)
* Supports four different styles: elegant, playful, minimalist, and festive
* Allows multiple languages and QR codes
* Generates AI-generated poems for customization

The most notable feature was overcoming the problem of text overflow when printed. To resolve this issue:

* All content must fit within the specified dimensions without cutting off (overflowing)
* Reduce font size if necessary to fit all content
* Utilize the developer extension to validate that no content is cut off visually in fullscreen mode

The Goose recipe was tested and refined using the following steps:

1. Define a unique ID for each element with defined width, height, class, etc.
2. Generate HTML code based on input data from user preferences, languages, styles, QR codes, poems, and more.

### Benefits of Using the Solution

This solution enables users to create beautifully designed gift tags with ease, allowing them to focus on designing innovative products without excessive time spent debugging layouts or font sizing issues.

**Use Cases**

* Gift tag generation
* Stationery automation
* Digital marketing materials
* Wedding invitations design
* Presentations and business cards
