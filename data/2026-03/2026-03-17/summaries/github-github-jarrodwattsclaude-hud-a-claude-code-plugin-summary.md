---
title: "GitHub - jarrodwatts/claude-hud: A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress · G..."
url: https://github.com/jarrodwatts/claude-hud
date:
site: github
model: llama3.2:1b
summarized_at: 2026-03-17T11:23:09.967249
---

# GitHub - jarrodwatts/claude-hud: A Claude Code plugin that shows what's happening - context usage, active tools, running agents, and todo progress · G...

**GitHub - jarrodwatts/claude-hud: A Claude Code plugin that shows what's happening**

The GitHub repository of the "claude-hud" plugin is a custom Claude Code tool that provides detailed insight into the session using various features such as context usage, active tools, running agents, and todo progress. The following key points summarize the main ideas and features:

**Installation and Setup**

1. Fork the repository to install the plugin in your Claude Code instance.
2. Run `plugin marketplace add jarrodwatts/claude-hud` to add the plugin to your instance.
3. Configure the statusline using `/claude-hud:setup`.

**Features**

* **Project Path**: Know which project you're in (configurable directory levels)
* **Context Health**: Understand how full your context window is
* **Tool Activity**: Watch Claude read, edit, and search files as it happens
* **Agent Tracking**: See subagents running and their tasks
* **Todo Progress**: Track task completion in real-time

**Appearance**

The plugin displays key information in a bar on the left or right side of the screen, which provides context about the session:

*   **Context Health**: Green (25%) for full context window or yellow (45%) when too dense
*   **Tools Activity**: Display tools being used (e.g., `auth.ts`), reading files, and running subagents
