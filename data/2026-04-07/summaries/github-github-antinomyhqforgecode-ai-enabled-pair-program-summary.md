---
title: GitHub - antinomyhq/forgecode: AI enabled pair programmer for Claude, GPT, O Series, Grok, Deepseek, Gemini and 300+ models · GitHub
url: https://github.com/antinomyhq/forgecode
date:
site: github
model: llama3.2:1b
summarized_at: 2026-04-07T11:29:11.504014
---

# GitHub - antinomyhq/forgecode: AI enabled pair programmer for Claude, GPT, O Series, Grok, Deepseek, Gemini and 300+ models · GitHub

**Forge Overview**

The `forge` package is a comprehensive coding agent that integrates artificial intelligence (AI) capabilities with various development environments. It offers multiple modes for interacting with the command line interface (CLI), including Interactive Mode, One-Shot CLI Mode, and ZSH Plugin Mode.

**Key Features**

- Comprehensive AI engine for automating tasks
- Integrates with numerous development tools and platforms
- Supports various programming languages and frameworks
- Offers advanced configuration options through `.forge.yaml` files

**How Forge Works**

Forge uses a three-tiered architecture: Interactive Mode (Three Modes), One-Shot CLI Mode, and ZSH Plugin Mode. In Interactive Mode, users can interact with the command line interface using TUI (Text-Based User Interface). For enhanced experience, users can switch to one-shot mode or enable auto-completion.

One-Shot CLI Mode provides a streamlined experience for users who prefer simplicity without extensive configuration. Users can also leverage ZSH Plugin Mode for customized environments tailored to their preferences.

**Key Components**

- `forge.yaml`: Configuration file that manages AI provider credentials
- `.gitattributes`, `.gitignore`, and `.rustfmt.toml` files: File system management scripts
- `AGENTS.md` and `README.md`: Documentation containing key information
- `diesel.toml`, `flake.lock`, `package-lock.json`, `package.json`, `renovate.json`, `rust-analyzer.toml`, `rust-toolchain.toml`, and `vertex.json`: Installation packages

**Installation**

Users can install Forge using the following command: `curl -fsSL https://forgecode.dev/cli | sh`. Alternatively,Forge is available as a ZSH plugin for users familiar with this environment management tool.
