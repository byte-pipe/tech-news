---
title: Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community
url: https://dev.to/hichamelbsi/breaking-down-the-text-barrier-of-llm-chatbots-with-kendoreact-and-mcp-ui-1ico
site_name: devto
fetched_at: '2025-09-30T11:08:58.581452'
original_url: https://dev.to/hichamelbsi/breaking-down-the-text-barrier-of-llm-chatbots-with-kendoreact-and-mcp-ui-1ico
author: ELABBASSI Hicham
date: '2025-09-27'
description: This is a submission for the KendoReact Free Components Challenge. What I Built Large... Tagged with devchallenge, kendoreactchallenge, react, webdev.
tags: '#devchallenge, #kendoreactchallenge, #react, #webdev'
---

This is a submission for theKendoReact Free Components Challenge.

## What I Built

Large Language Model (LLM) chatbots are powerful, but most of them are still limited totext-only answers. When users ask for complex data, the model ends up dumping plain text instead of showing something truly usable.

For this challenge, I built a system that breaks this limitation by combining:

* KendoReact componentsfor polished, interactive UI.
* Supabaseas the database backend.
* MCP-UI (Model Context Protocol UI)as the glue between the chatbot and UI components.

The result is a chatbot that doesn’t just reply with words — it can renderlive KendoReact Grids and Cardsdirectly in the conversation, powered by real Supabase queries.

Here’s how it works:

* On theserver side, I created anMCP-UI serverusing@mcp-ui/server. It exposes two tools:show_grid: queries tables (tasks,projects,users,user_task) with filters and joins, and returns aKendoReact Grid.show_user_details: fetches a user profile plus task counts (todo,in_progress,done), and returns aKendoReact Card.
* show_grid: queries tables (tasks,projects,users,user_task) with filters and joins, and returns aKendoReact Grid.
* show_user_details: fetches a user profile plus task counts (todo,in_progress,done), and returns aKendoReact Card.
* On theclient side, I built a chatbot UI usingKendoReact componentsand@mcp-ui/client. This chatbot can receiveUIResourcemessages from the server and render them inside the conversation.

Why not just build a custom UI directly? BecauseMCP-UI makes the components portable. Any MCP host that supports@mcp-ui/client(likeLibreChat) can consume my server’s interactive Grids and Cards without any custom integration.

I believe this is an early preview of the future of LLM applications. Shopify is already experimenting with “agentic commerce” using similar patterns. With Kendo UI’s battle-tested components and MCP-UI’s portability, we can imagine many more use cases:

* Livestatistics dashboardstied to the ongoing conversation.
* Interactive workflows where one MCP server’s results feed another’s UI.
* Chatbots that don’t just explain data, but let you explore and manipulate it.

## Demo

https://kendo-ai-bot-mcp-ui.vercel.app/Try to display tasks, users or projects and interact with the dynamic KendoReact x MCP-UI components. (e.g. "Show me 10 tasks that are done", "Show me all the tasks assigned to Kyle Ellis", "Show me all tasks from the project student", etc)

⚠️ Heads up: This is running on a temporary Anthropic API key, so if you hammer it too hard the bot might ghost you. I love demos, but I don’t love surprise credit card bills. Please feel free to comment below if the app doesn't work anymore 😅.

⚠️Note:For local setup, I'll provide temporary API keys for Supabase that will be deleted right after ther challenge but an Anthropic api key will be needed.

* 🎥 Video demo of mycustom KendoReact chatbotpowered by MCP-UI.
* 📸 Screenshot of the same MCP-UI server running insideLibreChat, showing that the UI is portable across clients.

📦 Repo:github.com/HichamELBSI/ai-chatbot-with-mcp-ui

## KendoReact Components Used

* Grid, Column, Buttons→ interactive task and project tables.
* Card, CardHeader, CardTitle, CardBody, CardActions, CardImage, CardSubtitle→ user profile cards with avatar and task counts.
* Avatar, SvgIcon, TextArea→ polish for chat messages and inputs.

## Lessons Learned

* MCP-UI is very new, so documentation and patterns are still emerging. But it’s powerful: once you learn theUIResourceflow, you can make any React component portable.
* KendoReactgave me reliable, polished UI components that worked immediately. Without them, I’d have lost most of the hackathon hand-coding tables and cards.
* The “aha!” moment was seeing aKendoReact Grid render inside LibreChatin response to a natural language query. That’s when the pieces clicked together.

🔥“Don’t just tell me the data — show me the data.”

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
