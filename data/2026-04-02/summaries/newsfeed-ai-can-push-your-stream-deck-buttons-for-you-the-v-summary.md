---
title: AI can push your Stream Deck buttons for you | The Verge
url: https://www.theverge.com/tech/905021/elgato-stream-deck-mcp-ai-agent-update
date: 2026-04-01
site: newsfeed
model: gpt-oss:120b-cloud
summarized_at: 2026-04-02T01:03:37.318090
---

# AI can push your Stream Deck buttons for you | The Verge

# AI can push your Stream Deck buttons for you

## Overview
- Elgato’s Stream Deck 7.4 update introduces Model Context Protocol (MCP) support.  
- MCP enables AI assistants such as Claude, ChatGPT, and Nvidia G‑Assist to locate and activate Stream Deck actions on the user’s behalf.

## How MCP Works
- Users continue to set up actions in the Stream Deck app exactly as before.  
- Each MCP action includes a description field that AI assistants read to understand what the action does and when to use it.  
- After connecting an AI tool, users can type or speak requests; the AI triggers the matching Stream Deck macro automatically.

## Enabling MCP in the App
- Update to the latest Stream Deck software.  
- Open **Preferences**, go to the **General** tab, and check **Enable MCP Actions**.  
- This creates a dedicated “MCP Actions” profile; any actions placed in this profile become accessible to connected AI tools.

## Required Additional Setup
- Install a Node.js utility and the Elgato MCP Server bridge on the computer to link AI tools with the Stream Deck app.  
- The installation can be finicky for those unfamiliar with MCP integrations, but Elgato provides a detailed step‑by‑step guide.

## Significance
- MCP is being positioned as a universal “USB cable” for artificial intelligence, with backing from companies like Microsoft, Anthropic, Figma, and Canva.  
- The update offers a hands‑free way to trigger any macro commands assigned to physical Stream Deck devices or the digital app.