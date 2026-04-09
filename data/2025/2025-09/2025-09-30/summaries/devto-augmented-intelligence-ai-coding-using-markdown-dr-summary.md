---
title: Augmented Intelligence (AI) Coding using Markdown Driven-Development - DEV Community
url: https://dev.to/simbo1905/augmented-intelligence-ai-coding-using-markdown-driven-development-pg5
date: 2025-09-28
site: devto
model: llama3.2:1b
summarized_at: 2025-09-30T11:12:18.473767
screenshot: devto-augmented-intelligence-ai-coding-using-markdown-dr.png
---

# Augmented Intelligence (AI) Coding using Markdown Driven-Development - DEV Community

**Augmented Intelligence (AI) Coding using Markdown Driven Development - DEV Community**

### TL;DR

The article discusses the author's experience with Augmented Intelligence (AI) coding, where they used Readme-Driven Development with Large Language Models (LLMs). The process involves designing feature documentation, exporting a description-only "coding prompt", pasting it into an Agent in YOLO mode, and forcing the agent to work backwards.

**Step 1: Design Feature Documentation**

* Discuss feature goals online using an LLM search engine
* Create user documentation (e.g., README.md or blog post) with an open-ended question to research the feature

### Step 2: Export Description-Only "Coding Prompt"

* Tell the model to create a description-only "coding prompt" with no code
* Output a Markdown feature documentation artefact

**Step 3: Paste to Agent in YOLO Mode**

* Paste the feature documentation and a description-only "coding prompt"
* Restrict git commits and pushes to prevent introducing errors during development
* Request that the agent use GitHub issues, PRs, and branch management best practices

**Step 4: Force Agent to Work Backwards**

* Direct the agent to review and fix bugs with code while working backwards from documentation changes

### Additional Notes

* The author recommends using paid models (Dive AI Desktop) or a mix of free and paid options for better accuracy
* They provide tips on configuring agents, including restricting permissions and creating Todos lists
