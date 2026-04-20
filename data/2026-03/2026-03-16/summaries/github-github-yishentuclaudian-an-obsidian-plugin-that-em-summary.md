---
title: GitHub - YishenTu/claudian: An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault · GitHub
url: https://github.com/YishenTu/claudian
date:
site: github
model: llama3.2:1b
summarized_at: 2026-03-16T11:42:28.712911
---

# GitHub - YishenTu/claudian: An Obsidian plugin that embeds Claude Code as an AI collaborator in your vault · GitHub

Here is a concise and informative summary of the article:

**GitHub - YishenTu/claudian**

The article describes the **claude** Obsidian plugin, which embeds Claude Code as an AI collaborator in your vault. This plugin offers various features that make it a powerful tool for creating interactive workflows.

**Key Features:**

* Full agentic capabilities, allowing file read/write, search, and bash commands to be executed within theObsidian vault.
* Context-aware features, including file attachment,mentioning files with@, exclusion of notes by tag, and access to external directories.
* Vision support through analysis of images sent via drag-and-drop or pasted into notes.
* Inline edit capabilities, enabling text edits at the cursor position directly in notes.
* Instruction mode (#) for adding custom instructions from the chat input, along with review/edit functionality.

**Plugin Capabilities:**

* The plugin enables reusability of prompt templates via slash commands, skills, agents, and plugin modules.
* Customizable agents that Claude can invoke, including tool restrictions and model overrides.
* Support for external tools and data sources using Model Context Protocol servers (stdio, SSE, HTTP).
* Advanced features like Haiku, Sonnet, and OPUS models with custom thinking budget fine-tuning.

**Implementation:**

The plugin integrates seamlessly with Claudian plugins installed via the CLI and uses per-vault configuration options. Additionally, an MCP support mechanism is available for external tools and data sources, enabling contextual interactions.

Overall, **claude** offers a robust and customizable setup for creating interactive workflows in Obsidian using Claude Code as an AI collaborator.
