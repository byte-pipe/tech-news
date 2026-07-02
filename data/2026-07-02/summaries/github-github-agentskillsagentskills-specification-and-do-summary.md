---
title: GitHub - agentskills/agentskills: Specification and documentation for Agent Skills · GitHub
url: https://github.com/agentskills/agentskills
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-02T11:57:43.542322
---

# GitHub - agentskills/agentskills: Specification and documentation for Agent Skills · GitHub

**Agent Skills Overview**
=========================

### Introduction

Agent skills are a standardized way to extend AI agent capabilities with specialized knowledge and workflows. They provide a lightweight, open format for packaging procedural knowledge and context into portable, version-controlled folders that agents can load on demand.

### Key Features

* **Reusable instructions**: Agent skills bundle modular code, documentation, templates, and resources.
* **Domain expertise**: Capture specialized knowledge from various domains as reusable instructions and resources.
* **Repeatable workflows**: Build consistent procedures across multiple tasks using agent skills.
* **Cross-product reuse**: Use agent skills across any skill-compatible agents.

### Load and Activate Agent Skills

1.  Discovery: Agents load only the name and description of available skills at startup.
2.  Activation: When a task matches a skill's description, the agent reads the full instruction set into context.
3.  Execution: The agent follows the instructions, optionally executing bundled code or loading referenced files as needed.

### Supported Platforms

*   AI tools and agentic clients from various industries
*   GitHub repository for easy collaboration and sharing

### Getting Started

*   Documentation: Guides and tutorials available for guides, specifications, example skills, and Discord resources.
*   Specification: Details on format, including specification guidelines.
*   Example Skills: Showcase other agents using agent skills to inspire creativity.

By following this guide, developers can now unlock the full potential of AI agents by leveraging the power of agent skills.