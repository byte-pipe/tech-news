---
title: OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI
url: https://simonwillison.net/2025/Dec/12/openai-skills/
date: 2025-12-13
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-13T11:11:50.113343
screenshot: hackernews-openai-are-quietly-adopting-skills-now-available-i.png
---

# OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI

## OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI

OpenAI has been quietly implementing a skills mechanism that allows other platforms to adopt and leverage AI models like ChatGPT. This mechanism, which is built on top of the Anthropic Skills repository, enables developers to create skills that can be interacted with using various tools.

## Overview of Skills in OpenAI's Codex CLI Tool

The open-source Codex CLI tool has recently been updated to include experimental support for skills, allowing users to explore and utilize AI models like ChatGPT within their platforms. Skills folders are created by simply prompting a command like `Create a zip file of /home/oai/skills`, resulting in access to the necessary resources.

## Implementation Details in OpenAI's Codex CLI Tool

Skills implementation is achieved using an approach that converts documents, spreadsheets, and PDFs into rendered per-page PNGs before passing them through AI models. This minimizes information loss in PDFs and documents.

Anthropic has also implemented similar skills technology in their official Skills repository. Using this open-source framework, users can create compatible skills for use within their platforms.

## Adoption of Skills by OpenAI's ChatGPT

ChatGPT, a conversational AI model developed by OpenAI, now supports the Anthropic Skills mechanism. Users can engage with the chatbot using new "Home" or `/oai/skills` folders, which are accessed via a simple prompt: `Create a zip file of /home/oai/skills`. This has enabled users to explore the contents of these folders.

## Conclusion and Implications

OpenAI's adoption of skills technology demonstrates their commitment to empowering developers and end-users with AI capabilities. Whether used within Codex CLI tools or Anthropic's official Skills repository, this enhanced skill structure provides new possibilities for exploration, creation, and interaction.
