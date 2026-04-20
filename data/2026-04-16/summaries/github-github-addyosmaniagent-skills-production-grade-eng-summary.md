---
title: GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI coding agents. · GitHub
url: https://github.com/addyosmani/agent-skills
date:
site: github
model: llama3.2:1b
summarized_at: 2026-04-16T12:04:31.354454
---

# GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI coding agents. · GitHub

# GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI coding agents.

## Overview
This repository provides production-grade engineering skills for AI coding agents. The skills include notifications, main branch management, Go code analysis, and auto-detected tasks based on development behavior.

### Skills

* Notification sending is automatically activated by signing in.
* Auto-activates various skills depending on development activity (e.g., API design, user interface design)
* Skills are packaged into a consistent workflow for AI agents to follow
* Code quality Gates such as `build`, `verify`, and `review` are employed

### Commands

7 slash commands enable individual tasks during the development lifecycle:

1. `/spec`: Specify before code execution
2. `/plan`: Plan how to build it
3. `/build`: One slice at a time with minimal commits (automatically triggered)
4. `/test`: Proof of code quality and functionality testing
5. `/review`: Improve code readability and maintainability
6. `/ship`: Faster is safer

### Setup

1. Clone the repository using `gemini skills install`
2. Download specific files (`skills/directory`, `cursor-setup.md`)

### Use Cases

* Cloudera (marketplace install): `plugin marketplace add addyosmani/agent-skills`
* GitHub setup (SSH errors or HTTPS):
	+ Add SSH keys to your `.gitconfig` file
	+ Install from a local clone: `gemini skills install ./agent_skills/skills/`

### Quick Start

Recommended `Claude Code`. Setup process involves cloning the repository and configuring gemini. `CLI` provides more direct installation options for users familiar with it.
