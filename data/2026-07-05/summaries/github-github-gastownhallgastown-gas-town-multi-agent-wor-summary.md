---
title: GitHub - gastownhall/gastown: Gas Town - multi-agent workspace manager · GitHub
url: https://github.com/gastownhall/gastown
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-05T11:34:55.657171
---

# GitHub - gastownhall/gastown: Gas Town - multi-agent workspace manager · GitHub

# Gas Town Workspace Manager

**Overview**

Gas Town is a multi-agent workspace manager that enables persistent work tracking with Claude Code, GitHub Copilot, and other AI agents. It allows for coordinated operation of multiple agents working on different tasks.

## Key Features

* Persistent work state in git-backed hooks
* Built-in mailboxes, identities, and handoffs
* Manually coordinating agent interactions through a single user interface

### Architecture

![Gas Town Architecture](image)

**Agent Management**

* **Rig:** Main workspace for the mayor and associated actors (e.g., Claire Code).
* **Crew1:** Primary actor responsible for implementing tasks within Rig.
* **Hooks:** Persistent storage of working state, connected to git repositories.

### Workflows

* Coordination between agents
* Notification mechanisms for task completion or failures
* Automated data processing using Beads ledger

**Example Use Case**

In a multi-agent workflow, multiple agents such as Claire Code (Claude), GitHub Copilot, and Codex work together on different tasks within the Gas Town workspace. Each agent maintains its own persistent working state in git-backed hooks, allowing for reliable coordination of task completion.

* Mayor (Rig) initiates tasks
* Crew1 (Crew Member) coordinates task execution
* Hooks (Persistent Storage) collect working data from agents

### Conclusion

Gas Town solves challenges with manual agent coordination and provides a scalable solution using persistent work state in git-backed hooks.