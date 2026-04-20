---
title: GitHub - langchain-ai/open-swe: An Open-Source Asynchronous Coding Agent · GitHub
url: https://github.com/langchain-ai/open-swe
date:
site: github
model: llama3.2:1b
summarized_at: 2026-03-18T11:36:28.022009
---

# GitHub - langchain-ai/open-swe: An Open-Source Asynchronous Coding Agent · GitHub

**Open Source Coding Agent Framework Overview**

Open SWE is an open-source coding agent framework that enables internal coding agents to be built on top of existing infrastructure. It combines elements from `Deep Agents` and provides a structured approach for building custom agents, with customizable orchestration, tools, and middleware.

### Key Components:

1. **Agent Harness**: Composed on Deep Agents; allows for upgrade paths while allowing customization.
2. **Sandbox Environment**: Isolated cloud environments, providing full shell access and containing the blast radius of mistakes.
3. **Customization Options**: Supports multiple sandbox providers out of the box (e.g., ModaL, DaytonA) or custom plugins.

### Integration with Existing Frameworks

Open SWE builds upon `LangGraph` and `Deep Agents`, offering similar architectural decisions as the top companies' internal coding agents:

* Composes on Deep Agents framework
* Supports multiple sandbox providers
* Allows for customizable orchestration, tools, and middleware

### Customization Guide

For those interested in modifying Open SWE to suit their organization's requirements:

* Clone the repository in a new directory
* Modify `DEFAULT.md` files as necessary
* Explore and implement additional customization options (e.g., `CUSTOMIZATION.md`)
