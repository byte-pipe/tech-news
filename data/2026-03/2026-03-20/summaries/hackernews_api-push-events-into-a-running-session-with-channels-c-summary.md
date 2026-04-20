---
title: Push events into a running session with channels - Claude Code Docs
url: https://code.claude.com/docs/en/channels
date: 2026-03-20
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-03-20T11:25:47.343962
---

# Push events into a running session with channels - Claude Code Docs

## Overview of Push Events into Running Claude Code Session with Channels - Claude Code Docs

To integrate push events into a running Claude Code session with channels, follow these steps:

*   Supported channels are provided for two platforms: Telegram and Discord.
*   Installing and running a channel involves fakechat, a localhost demo available through the quickstart page.
*   Creating a Telegram bot is required to send messages from within Claude Code.

### Installing and Running a Channel

To create a channel, follow these steps:

1.  Open BotFather in Telegram and send `/newbot` with a display name and unique username ending in `bot`.
2.  Provide the token given by BotFather.
3.  Run `plugin install telegram@claude-plugins-official`.

### Configuring Token

To access the channel plugin, run `configure /telegram:configure <token>`.

### Pairing Account from Telegram

1.  Open Telegram and send any message to your bot.
2.  The bot will reply with a pairing code in Claude Code through `--channels`.
3.  To pair your account manually, run `/telegram:access pair <code>`. Then lock down access by enabling the policy allowing only you to send messages from within Claude Code.

### Setup Overview

1.  **Telegram Channel:** Requires fakechat, a localhost demo.
2.  **Discord Channel:** Not supported out-of-the-box with Claude Code v2.1.80 or later and claude.ai login.
3.  To build your own channel, refer to the Channels reference.

## Supported Channels

*   Telegram
*   Discord
