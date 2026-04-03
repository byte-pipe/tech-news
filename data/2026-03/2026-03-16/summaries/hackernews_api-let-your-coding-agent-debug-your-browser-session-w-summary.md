---
title: Let your Coding Agent debug your browser session with Chrome DevTools MCP | Blog | Chrome for Developers
url: https://developer.chrome.com/blog/chrome-devtools-mcp-debug-your-browser-session
date: 2026-03-15
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-03-16T11:36:27.530546
---

# Let your Coding Agent debug your browser session with Chrome DevTools MCP | Blog | Chrome for Developers

Let's Debug Your Browser Session with Chrome DevTools MCP

* **Stay Organized:** Collections and Categorize Content
---------------------------

* Sebastian Benz, GitHub, Mastodon, Bluesky Alex Rudenko, XGitHub (Published: December 11, 2025)
* Enhancement of Chrome DevTools MCP Server for Coding Agents
* Direct Connection to Active Browser Sessions
* Access to Active Debugging Sessions

**Key Features:**

1. **Re-use an existing browser session**: Automatically access a valid session without authentication.
2. **Access active debugging sessions**: Seamlessly transition between manual and AI-assisted debugging tools.

**How it Works:**

* The remote debugging connection is established automatically on demand by the MCP server.
* When connected, Chrome displays a dialog prompting for user approval before granting remote debugging.
* While an active debugging session exists, "Chrome is being controlled by automated test software" banner appears at top of screen.

**Setup and Usage:**

1. **Enable Remote Debugging**: In Chrome (>=144), enable remote debugging in `chrome://inspect/#remote-debugging` to start using the new capability.
2. **Configure MCP Server**: Set up the MCP server with --autoConnect option to enable auto-connection feature.

### Getting Started:

* Set up remote debugging in Chrome.
* Configure MCP server settings ( --autoConnect)