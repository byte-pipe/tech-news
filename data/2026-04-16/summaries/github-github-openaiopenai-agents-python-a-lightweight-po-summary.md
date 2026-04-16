---
title: GitHub - openai/openai-agents-python: A lightweight, powerful framework for multi-agent workflows · GitHub
url: https://github.com/openai/openai-agents-python
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-04-16T12:06:02.397242
---

# GitHub - openai/openai-agents-python: A lightweight, powerful framework for multi-agent workflows · GitHub

**GitHub - openai/openai-agents-python: A Lightweight, Powerful Framework for Multi-Agent Workflows**

### Overview

The OpenAI Agents SDK is a lightweight and powerful framework for building multi-agent workflows. It supports the OpenAI Responses API and several other LLMs.

### Key Features

*   **Agents**: LLMs configured with instructions, tools, guardrails, and handoffs
*   **Sandbox Agents**: Agents preconfigured to work with a container to perform work over long time horizons.
*   **Handoff Systems**: Delegating agents for specific tasks.
*   **Tools**: Providing various tools that let agents take actions (functions, MCP, hosted tools)
*   **Human-in-the-Loop Mechanisms**: Built-in mechanisms for involving humans across agent runs.
*   **Session Management**: Automatic conversation history management across agent runs.
*   **Traces**: Built-in tracking of agent runs to view, debug, and optimize workflows.

### Getting Started

To use the OpenAI Agents SDK, follow these steps:

1.  Set up your Python environment (Python 3.10 or newer).
2.  Install the SDK using pip: `pip install openai-agents`
3.  For voice support with AWS Lambda: Install `openai-agents[voice]`.
4.  For Redis session management with AWS Lambda: Install `openai-agents[redis]`.

### Code

Some examples of code can be found in the SDK's repository, including example code for building and running agents.

### Documentation

You can find more information about the SDK by visiting its documentation page on GitHub.

### Makefile

## Makefiles are included in each supported distribution (.py). They provide detailed build output.


### Code Example
```markdown
## makefile
```

Note: This is a Markdown format list, not a traditional bullet points, with header level 1 being the main title and higher levels being subsidiary titles.