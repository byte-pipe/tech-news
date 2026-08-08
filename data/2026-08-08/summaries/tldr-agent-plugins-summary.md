---
title: Agent Plugins
url: https://agent-plugins.org/
date: 2026-08-08
site: tldr
model: llama3.2:1b
summarized_at: 2026-08-08T11:31:51.242450
---

# Agent Plugins

## Agent Plugins: A Portable Package Format for Reusable Components

### Introduction

Agent Plugins is an open, vendor-neutral standard for packaging reusable components into portable plugins. Its version 1.0.0 specification defines a shared format for discovering and loading compatible clients across different platforms.

### Main Points:

- **AI Client Plugin Development**: AI client applications have developed their own plugin formats to extend functionality.
- **Interoperability Concerns**: Reusable components must be adaptable between clients without requiring significant alteration on each instance.
- **Portable Package Format**: Agent Plugins provides a standardized interface for plugins with fixed locations and requirements.

## Building an Agent Plugin

*   directory structure: my-plugin/ (manifest), skills/ (Agent Skills file), mcp.json, hooks/
    *   plugin.json identifies the plugin
    *   scripts/ (directory containing script files)
        *   sumSkills.md (script summary)
        *   references/ (directory containing reference information)

## Open Development and Participation

- **Development Process**: Proposals are open for discussion on GitHub; ideas for new features can be implemented with user support.
-   Check the official specification repository to consult relevant documentation.

### Key Benefits:

-   Compatible clients that support portable Agent Plugins format.
-   Easy implementation of a client-based solution using existing skills and MCP server implementations.