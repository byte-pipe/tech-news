---
title: Algolia MCP Supermarket Assistant - DEV Community
url: https://dev.to/campsjos/algolia-mcp-supermarket-assistant-3g9h
site_name: devto
fetched_at: '2025-08-04T04:06:24.077889'
original_url: https://dev.to/campsjos/algolia-mcp-supermarket-assistant-3g9h
author: Josep Camps Miró
date: '2025-07-27'
description: This is a submission for the Algolia MCP Server Challenge What I Built A shopping bot... Tagged with devchallenge, algoliachallenge, webdev, ai.
tags: '#devchallenge, #algoliachallenge, #webdev, #ai'
---

Algolia MCP Server Challenge: Ultimate user Experience

This is a submission for theAlgolia MCP Server Challenge

## What I Built

A shopping bot that gets it. Say "I'm making tacos" and it finds tortillas, beef, cheese automatically. No keyword searching.

Built with Node.js + OpenAI Agents + Algolia MCP. Conversation memory, smart result limiting.

## Demo

Repo:campsjos/algolia-mcp-supermarket

curl
-X
 POST http://localhost:4242/api/chat
-H

"Content-Type: application/json"

\


-d

'{"prompt": "I want to make chocolate cake"}'

Enter fullscreen mode

Exit fullscreen mode

Auto-searches when you mention food/recipes/weather. No explicit commands needed.

OpenAI Agents call the Algolia MCP server automatically when users mention food/recipes/weather.

Key parts:

* Proactive triggers: Recipe → ingredients, weather → appropriate products
* Result extraction: Parse agent_generatedItemsto get Algolia hits
* Smart limiting: 1 result per search if multiple, 4 if single
* Session memory: Conversation context across requests

The integration is seamless - users don't know they're hitting Algolia.

## Key Takeaways

Main challenge:AI is unpredictable. Sometimes "I want pasta" would just give recipes instead of searching for ingredients. Other times it would search for random stuff I didn't expect. Spent days tweaking the system prompt until I found the right balance of being explicit about when to use MCP tools without making responses feel robotic.

What I learned:

* Prompt engineering is crucial- Generic prompts don't work. Had to be very specific about trigger words and search behavior
* Agent state parsing is messy- OpenAI Agents structure responses differently each time. Needed multiple fallback strategies to reliably extract Algolia results
* User experience matters- Raw search results overwhelm people. Smart limiting (1 per search vs 4) made conversations feel natural
* Debugging AI is different- Added comprehensive logging because you can't just console.log your way through unpredictable AI behavior

Development process:Started simple with basic chat, then added MCP integration. Hit the wall with inconsistent AI behavior - sometimes it would search, sometimes not. Realized I needed to treat the AI like a junior developer: give it very clear instructions about what to do and when. The breakthrough was crafting a system prompt that made proactive searching feel natural rather than forced.

Biggest surprise:How seamless MCP servers make tool integration feel once you get the prompting right. The Algolia MCP server just works - all the complexity was in getting the AI to use it consistently.

First time with MCP servers - they make AI tool integration feel natural.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
