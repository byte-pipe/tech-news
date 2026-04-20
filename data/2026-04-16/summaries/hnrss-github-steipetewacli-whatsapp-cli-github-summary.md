---
title: GitHub - steipete/wacli: WhatsApp CLI · GitHub
url: https://github.com/steipete/wacli
date: 2026-04-15
site: hnrss
model: llama3.2:1b
summarized_at: 2026-04-16T06:13:29.083858
---

# GitHub - steipete/wacli: WhatsApp CLI · GitHub

**wacli, WhatsApp CLI**
=========================

### Introduction

wacli is a WhatsApp CLI built on top of whatsmewow, focusing on best-effort local sync, fast offline search, and sending messages. It's a third-party tool that doesn't use the official WhatsApp Web protocol.

### Features

* Local sync of message history with continuous capture
* Fast offline search
* Sending messages
* Contact + group management

**Repository Files Navigation**
--------------------------------

This project has various repository files that can be visited for more information:

* `docs`: documentation
* `CHANGELOG.md`: changes to the project over time
* `LICENSE`: license terms and conditions
* `README.md`: user guide and getting started

### Releases

wacli releases are based on specific versions of whatsmewow. Each release includes updates to its core implementation, messages, send functionality, authentication, and more.

### Install / Build

You can install wacli via Homebrew or manually build it locally using `go build`.

### Quick Start

To authenticate with wacli, execute:
```bash
pnpm wacli auth
```
Once authenticated, you can keep syncing to your device. To do so:

```bash
pnpm wacli sync --follow
```

Search messages: `pnpm wacli messages search`
Backfill older messages for a chat (requires the primary device online).
Download media for a message.
Send a message with various options.

Manage contacts and groups by using:
`pnpm wacli groups list`
`pnpm wacli groups rename --jid 123456789@g.us --name`
Before making changes:
`./wacli send file --to 1234567890 --file /tmp/abc123 --filename report.pdf

Prior Art / Credit**

wacli is inspired by the WhatsApp CLI, but it's a separate project. See `CHANGELOG.md` for more information on whatsmewow and how wacli builds upon their work.
```
