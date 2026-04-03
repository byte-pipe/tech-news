---
title: The Emperor Has No Clothes: How to Code Claude Code in 200 Lines of Code - Mihail Eric
url: https://www.mihaileric.com/The-Emperor-Has-No-Clothes/
date: 2026-01-08
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-01-10T11:14:22.308944
screenshot: hackernews_api-the-emperor-has-no-clothes-how-to-code-claude-code.png
---

# The Emperor Has No Clothes: How to Code Claude Code in 200 Lines of Code - Mihail Eric

Here is a concise and informative summary of the article text:

## Overview
The article discusses how to build a functional coding agent from scratch using 200 lines of code in Python. It highlights that this approach relies on a conversation between a powerful Large Language Model (LLM) and the user's input.

### The Mental Model
The article explains that a coding agent works as follows:

1. The user sends a message to the LLM.
2. The LLM responds with a structured call to an additional tool.
3. The user's program executes this local tool call.
4. The result is sent back to the LLM.

### Three Essential Tools
To build a functional coding agent, three essential tools are needed:

1. A file system interface: allows the LLM to read files and interact with the user's project directory.
2. A list of available file interfaces: enables the LLM to navigate tasks such as browsing directories or executing commands.
3. An editing tool: provides the necessary APIs for modifying code.

### Implementation
The article details one implementation method using OpenAI Anthropic and its API client. The code includes utility functions for resolving absolute paths, making sure they are absolute, and implementing the three tools mentioned above.

## Key Takeaways

* A coding agent relies on a conversation between a LLM and the user's input.
* Three key tools are needed: file system interface, list of available file interfaces, and editing tool.
* OpenAI Anthropic is a relevant API client for this implementation.

Overall, the article provides guidance on how to build simple coding agents using 200 lines of code in Python.
