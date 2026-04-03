---
title: Claude Code On-The-Go - granda
url: https://granda.org/en/2026/01/02/claude-code-on-the-go/
date: 2026-01-05
site: hackernews
model: llama3.2:1b
summarized_at: 2026-01-05T11:25:01.350231
screenshot: hackernews-claude-code-on-the-go-granda.png
---

# Claude Code On-The-Go - granda

# Claude Code Setup and Deployment on iOS and Android

This article discusses the setup and deployment of Claude Code agents, which are cloud-based coding tools developed using mobile development kits (mdks). The setup involves running multiple Claude Code agents in parallel using Termius, an SSH client developed for Termius. The goal is to establish a continuous integration/reintegration (CI/CD) pipeline with minimal infrastructure requirements.

## Key Points:

*   A custom setup using the iOS Shortcut app that contacts the Vultr VM and communicates via Tailscale VPN.
*   Utilizes mosh for seamless connectivity, even between cellular networks.
*   Employes tmux for active session persistence across multiple windows.
*   Implements push notifications from Termius to devices via a hook in the settings.json file.

## Infrastructure:

*   A Vultr instance set up in Silicon Valley with minimal costs (~$7/day).
*   Two scripts handle lifecycle events (start and stop):

    *   `vm-start`: Starts the VM, waits for Tailscale, and connects via mosh.
    *   `vm-stop`: Halt's the VM.

## Mobile Environment:

*   Mobile applications running Termius are handled via SSH.
*   Keychain-based authentication ensures secure access to GitHub auth, where necessary.

## Session Continuity:

*   tmux attaches the terminal session on login and exits when the app is terminated.
*   Multiple windows can be opened by cycling between new terminals using `C-a cfor` and `C-a nto`.

## Push Notifications:

*   A prehook in `.claude/settings.json`: fires a question, extracts the response from Poke's webhook, and posts it to the tool input.

## Trust Model:

*   The setup prioritizes security by running Claude Code in permissive mode.
*   Cost control is achieved through hourly access fees on Vultr with a daily cap set at $7.
