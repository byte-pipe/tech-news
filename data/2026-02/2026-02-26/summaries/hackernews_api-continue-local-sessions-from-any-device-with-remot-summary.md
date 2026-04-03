---
title: Continue local sessions from any device with Remote Control - Claude Code Docs
url: https://code.claude.com/docs/en/remote-control
date: 2026-02-25
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-26T06:00:53.338978
---

# Continue local sessions from any device with Remote Control - Claude Code Docs

# Remote Control for Claude Code

## Overview
Remote Control is a feature available on Pro and Max Claude Code plans that allows users to connect to a running Claude Code session on their local machine from other devices, such as a phone or another computer via a web browser. It keeps the local Claude Code session running locally, providing access to the user's file system, tools, and project configuration.

## Requirements
To use Remote Control, users need:
* A Claude Code Pro or Max subscription.
* Authentication with runclaude and login to claude.ai.
* Workspace trust established by running runclaude in the project directory.

## Starting a Remote Control Session
A new Remote Control session can be started by running the command `claude remote-control` in the project directory. This command displays a session URL and a QR code in the terminal for connecting from other devices. Existing sessions can be accessed using the `/remotecontrol` (or `/rc`) command, which carries over the current conversation history.

## Connecting from Another Device
Remote Control sessions can be accessed by:
* Opening the session URL in a browser.
* Scanning the QR code displayed in the terminal.
* Finding the session in the Claude.ai/code interface or the Claude app by name.

## Enabling Remote Control for All Sessions
Remote Control can be enabled by setting the "Enable Remote Control for all sessions" option to true in the Claude Code configuration using the `/config` command.

## Connection and Security
Remote Control establishes outbound HTTPS connections only and does not open inbound ports. Communication between the remote client and the local session is secured through TLS, with short-lived, purpose-specific credentials.

## Remote Control vs. Claude Code on the Web
The key difference is that Remote Control runs locally on the user's machine, while Claude Code on the web runs in Anthropic-managed cloud infrastructure. Remote Control is suitable for ongoing local work, while Claude Code on the web is better for starting tasks without local setup or running tasks in parallel.

## Limitations
* Only one remote session can be active at a time per Claude Code session.
* The terminal must remain open for the session to continue.
* Extended network outages (over 10 minutes) may cause the session to time out.

## Related Resources
* Claude Code on the web
* Authentication setup
* CLI reference
* Security overview
* Data usage details
