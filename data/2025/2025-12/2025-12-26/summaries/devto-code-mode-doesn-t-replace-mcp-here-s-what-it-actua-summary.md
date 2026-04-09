---
title: "Code Mode Doesn't Replace MCP (Here's What It Actually Does) - DEV Community"
url: https://dev.to/blockopensource/code-mode-doesnt-replace-mcp-heres-what-it-actually-does-3hga
date: 2025-12-22
site: devto
model: llama3.2:1b
summarized_at: 2025-12-26T11:09:43.544661
screenshot: devto-code-mode-doesn-t-replace-mcp-here-s-what-it-actua.png
---

# Code Mode Doesn't Replace MCP (Here's What It Actually Does) - DEV Community

## Introduction
The article discusses the challenges of implementing "agentic workflows" with MCP (Model Context Protocol) in today's technology landscape. MCP was introduced to connect agents to everyday apps, but its experience has been imperfect due to the complexity of balancing model power with technical constraints.

## The "Too Many Extensions" Problem
Ingoose, a term used for MCP extensions, refers to multiple tools being added simultaneously, leading to performance degradation, tool calls in unexpected locations, and errors. Experienced users can fall into this trap without realizing it, such as turning on too many tools at once or flooding the agent's context window.

## Making Extensions Dynamic
To address this issue, dynamic extensions were introduced initially but remained hidden from casual users. Code Moderating addresses the problem by limiting extension usage to a specific implementation. The idea is for agents to write JavaScript or TypeScript code that decides which tools to call and how, running a single logic execution instead of constantly inquiring about additional tools.

## Key Points:
- MCP can be clunky due to "tool bloat," where multiple extensions are added without understanding their impact on performance.
- Excessive extensions lead to lag, instability, and errors.
- Dynamic Extensions aim to balance model power with technical constraints.
- Code Moderation solves the problem by limiting extension usage.
- MCP's foundation tools (search_modules, read_module, execute_code) provide a minimalistic approach.

## Main Ideas Retained:
* Implementing MCP has its challenges due to "tool bloat."
* Excessive extensions hinder performance and can be frustrating for users.
* Dynamic Extensions introduce an alternative solution to mitigate these issues.
* Code Moderation provides a framework for managing extensions.
* MCP's foundational tools offer a minimumistic approach.
