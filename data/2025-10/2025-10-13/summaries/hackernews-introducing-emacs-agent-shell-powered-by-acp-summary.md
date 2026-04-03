---
title: Introducing Emacs agent-shell (powered by ACP)
url: https://xenodium.com/introducing-agent-shell
date: 2025-10-13
site: hackernews
model: llama3.2:1b
summarized_at: 2025-10-13T11:23:51.035595
screenshot: hackernews-introducing-emacs-agent-shell-powered-by-acp.png
---

# Introducing Emacs agent-shell (powered by ACP)

# Emacs Agent Shell (powered by ACP) Overview
-----------------------------------------------------------------

Introduction

The Emacs agent-shell is a native Emacs shell powered by Agent Client Protocol (ACP). This feature allows users to access LLMs and AI systems without requiring specific tools or infrastructure.

## Key Features

* **Agent-Agnostic**: Users can switch between different agents easily, regardless of the chosen protocol.
* **Multi-Protocol Support**: The agent-shell supports Gemini CLI and Claude Code protocols, providing options for various AI systems.

## Setup and Configuration
--------------------------------

### Gemini CLI Agent Shell

*   Configures a Gemini CLI agent shell with:
    *   A new session
    *   A comint-mode connection
    *   Specific Emacs environment variables to support the Gemini API key
*   Interactively starts an agent using `acp-make-client` and provides prompt for authentication and command invocation

### Claude Code Agent Shell

*   Configures a Claude Code agent shell with:
    *   A new session
    *   A comint-mode connection
    *   Specific Emacs environment variables to support the Anthropic API key
*   Interactively starts an agent using `acp-make-client` and provides prompt for authentication and command invocation

### Additional Setup

*   Requires an existing client library (e.g., acp.el) to be set up with ACP.
*   Users can use other agents by modifying the corresponding configuration function (`agent-shell-start-gemini-agent/agent-shell-start-claude-code-agent`).

## Benefits and Next Steps
---------------------------

As this initial version completes, users who are interested in playing around with agents should start providing feedback on the ease of integration, scalability, and potential issues with different agent setups. Contributing fixes or new configurations will help further develop and expand the functionality for users.

The following information is already known: There are still many AI systems to explore that support Emacs.
You're encouraged to propose and contribute projects, including models, protocols, or applications utilizing the agent-shell tool for other languages, frameworks, and platforms
