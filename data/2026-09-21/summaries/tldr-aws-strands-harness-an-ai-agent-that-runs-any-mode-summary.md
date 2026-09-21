---
title: AWS Strands Harness: An AI Agent That Runs Any Model
url: https://thelettertwo.com/2026/09/21/aws-strands-harness
date: 2026-09-21
site: tldr
model: llama3.2:1b
summarized_at: 2026-09-21T16:57:06.762286
---

# AWS Strands Harness: An AI Agent That Runs Any Model

**Strands Harness Overview**
==========================

Amazon Web Services (AWS) has launched Strands Harness, a new tool for developers that enables developers to run and manage complex tasks with ease. Unlike other solutions, Strands Harness is designed to be more cost-effective and lightweight, with a focus on providing a complete set of features for open-source and on-machine use.

**Key Features and Capabilities**
-------------------------------

* Runs on a variety of reasoning models, including Amazon Bedrock, Anthropic, OpenAI, and Google
* Supports the Agent Skills format, similar to Anthropic's implementation
* Long-term memory across runs, allowing for context switching and improved performance
* Built-in helper agent for managing subtasks, tracks work against a checklist, and maintains a context window
* Offloads bulky tool results to files and caches reused portions of each request

**Cost and Performance**
------------------------

* AWS claims Strands Harness costs 26% less when using the same model as OpenAI's Code and Codex
* Outperforms these models in token efficiency, but outperforms a harness outperforms Strands Harness in token efficiency
* Scores higher on Terminal-Bench 2.1 evaluation

**Manager Interface and Integration**
-------------------------------------

* Outlines the decision-making process for choosing which agent to run and tuning the system prompt
* Evaluates whether the choice of agent improves performance or only consumes more tokens

**Conclusion**
==========

Strands Harness is a powerful tool that empowers developers to create complex tasks with ease, while being more cost-effective and lightweight compared to other solutions. By providing a complete set of features and a user-friendly interface, Strands Harness opens up new opportunities for developers to build and deploy powerful AI agents for various use cases.