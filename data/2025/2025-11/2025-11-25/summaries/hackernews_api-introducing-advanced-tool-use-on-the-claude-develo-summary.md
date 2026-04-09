---
title: Introducing advanced tool use on the Claude Developer Platform \ Anthropic
url: https://www.anthropic.com/engineering/advanced-tool-use
date: 2025-11-24
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-25T11:16:38.087540
screenshot: hackernews_api-introducing-advanced-tool-use-on-the-claude-develo.png
---

# Introducing advanced tool use on the Claude Developer Platform \ Anthropic

# Introduction to Advanced Tool Use on the Claude Developer Platform

## Enhancing AI Agent Capabilities with Tool Discovery and Execution

The goal of AI agents is to work seamlessly across hundreds or thousands of tools, allowing them to access a wide range of functionalities without requiring extensive knowledge of individual tool libraries. To achieve this, Claude's developers have introduced three new beta features: Tool Search Tool, Programmatic Tool Calling, and Tool Use Examples.

## Tool Search Tool

### Improving Context Modulation

The current approach involves using context windows to limit the number of tools that can be accessed at once. However, tool definitions often provide significant context, resulting in a large number of tokens consumed for every request. With Tool Search Tool, Claude can now dynamically discover and access thousands of tools without the need for exhaustive keyword searching or schema definition lookup.

## Programmatic Tool Calling

### Simplifying Code Execution with Inference Passes

While Python code can be used to invoke tools, making use of it in a fully context-aware environment still poses significant challenges. To address this issue, Claude now supports invoking tools using programmatic methods, reducing the impact on the model's context window. This enables agents to perform complex tasks without accumulating unnecessary context.

## Tool Use Examples

### Establishing Common Ground for Effective Use

The new features provided by Tool Search Tool and Programmatic Tool Calling facilitate the discovery of correct tool usage patterns through JSON schema definitions or examples rather than relying solely on schema definition. Additionally, they introduce universal standards for demonstrating how to use given tools in code, ensuring a consistent approach across different tasks.

## Real-World Benefits

Internal testing has shown that these new features can effectively build things beyond what was previously possible with conventional tool usage patterns. An example of this is Claude being used to read and modify large spreadsheets using Programmatic Tool Calling without overloading the model's context window, as demonstrated by the results for building programs.

## Key Takeaways:

* Advanced tool use on the Claude Developer Platform offers improved efficiency and flexibility in managing hundreds or thousands of tools.
* New features facilitate dynamic discovery of tools and invocation through code execution with reduced impact on context windows.
* Tool Use Examples provide a standard approach to demonstrating correct tool usage patterns, enhancing model training.
