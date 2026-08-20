---
title: "Looker's Native MCP Server with Claude Code - DEV Community"
url: https://dev.to/gde/lookers-native-mcp-server-with-claude-code-11j8
date: 2026-08-14
site: devto
model: llama3.2:1b
summarized_at: 2026-08-20T11:26:04.736458
---

# Looker's Native MCP Server with Claude Code - DEV Community

## Looker Native MCP Server Setup

Looker has moved its own MCP (Migrating Cloud Platform) Server to a new endpoint on its core instance. This provides a single, centralized location for managing the MCP Server. Here's a step-by-step guide to set up the Looker Native MCP Server:

### Connecting to the MCP Server

1. The MCP endpoint is available at `https://780eb09e-7dab-4076-9ec1-ecf9d8414630.looker.app/mcp`
2. Run `curl -s -X POST "$LOOKER_MCP_URL" -H 'Content-Type: application/json' -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{"tools":{"listChanged":false},"prompts":{"listChanged":false}}}'

### Configuring the MCP Server

1. Check the Looker Admin Panel: `Users > (your user) Edit Keys`
2. Note the `Base URL`, `Client ID`, and `Client Secret` required to authenticate with the MCP Server.

### Setting Up the Looker CLI

1. Clone the Looker CLI repository: `git clone https://github.com/looker/go-cli.git`
2. Install the Looker CLI: `make cli`

### Getting Started with the MCP Server

1. Launch the MCP Server in fullscreen mode: `looker-cli 0.4.8`
2. Confirm with the MCP Server: `lookup -y`
3. Once the MCP Server is online: `looker-cli 0.4.8 exit`