---
title: Advent of AI 2025 - Day 17: Building a Wishlist App with Goose and MCP-UI - DEV Community
url: https://dev.to/nickytonline/advent-of-ai-2025-day-17-building-a-wishlist-app-with-goose-and-mcp-ui-330l
date: 2025-12-27
site: devto
model: llama3.2:1b
summarized_at: 2025-12-29T11:11:45.830113
screenshot: devto-advent-of-ai-2025-day-17-building-a-wishlist-app-w.png
---

# Advent of AI 2025 - Day 17: Building a Wishlist App with Goose and MCP-UI - DEV Community

**Advent of AI Day 17: Wishlist MCP App**
=====================================================

### A Magical MCP-UI Application for Wish Management

For the 17th day of the Advent of AI challenge, I built a Winter Wishlist app using MCP-UI. This application allows users to create and manage their wishes in a visually appealing interface.

#### Key Features

*   **Make Wishes**: Allow users to input wishes with categories (toy/experience/kindness/magic) and priorities (dream wish/hopeful wish/small wish).
*   **Wishgrid Interface**: Display all created wishes in a beautifully formatted grid, making it easy to browse and manage.
*   **Grant and Release Wishes**: Permit users to grant their wishes when they come true, and release them as needed.

#### Implementation

The implementation stores wishes in memory based on MCP session ID. To ensure data persistency and make the application more robust, I utilized the following solutions:

*   Designed for maximum flexibility: I used MCP-UI's extensibility features to access any LLM (Large Language Model) directly from the user interface.
*   Adapts to workflow: goose's customizability capabilities allowed me to tailor the experience based on individual needs.
*   Multi-model configuration: This approach optimizes performance and cost by integrating with MCP servers.
