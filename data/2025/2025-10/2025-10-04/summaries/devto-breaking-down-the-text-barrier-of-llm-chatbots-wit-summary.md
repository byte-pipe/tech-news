---
title: Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community
url: https://dev.to/hichamelbsi/breaking-down-the-text-barrier-of-llm-chatbots-with-kendoreact-and-mcp-ui-1ico
date: 2025-09-27
site: devto
model: llama3.2:1b
summarized_at: 2025-10-04T11:17:05.201471
screenshot: devto-breaking-down-the-text-barrier-of-llm-chatbots-wit.png
---

# Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community

Here is a concise and informative summary of the article:

**Building a Powerful LLM Chatbot with Polished UI**

Key Points:

* Built an interactive chatbot using KendoReact components, Supabase as the database backend, and MCP-UI for the glue between the chatbot and UI components.
* The system renders live KendoReact Grids and Cards that can be shown directly in a conversation, powered by real Surpace queries.

**How it Works**

* On the server side: creates an MCP-UI server exposing two tools: `show_grid` to query tables with filters and joins, and returns a KendoReact Grid, as well as `shows_user_details` to fetch a user profile plus task counts.
* On the client side: builds a chatbot UI using KendoReact components and `mcp-ui/client`, which can receive UI Resources from the server.

**Why Not Custom Integration?**

* MCP-UI makes custom integration possible with any host that supports `mcp-ui/client`.

**Demo**

* Provides a demo link to try out the interactive chatbot built with KendoReact, MCP-UI, and Supabase in real-time.

## Technical Overview

* Combines text-only answers limitations of traditional LLMs using Supabase and MCP-UModel Context Protocol UI.
* Renders live data in KendoReact Grids and Cards powered by Surpace queries.
