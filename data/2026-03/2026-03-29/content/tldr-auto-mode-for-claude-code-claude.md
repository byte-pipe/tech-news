---
title: Auto mode for Claude Code | Claude
url: https://claude.com/blog/auto-mode
site_name: tldr
content_file: tldr-auto-mode-for-claude-code-claude
fetched_at: '2026-03-29T11:11:18.698589'
original_url: https://claude.com/blog/auto-mode
date: '2026-03-29'
description: Auto mode lets Claude Code make permission decisions with built-in safeguards — fewer interruptions than default, less risk than skipping permissions.
tags:
- tldr
---

# Auto mode for Claude Code

Auto mode provides a safer long-running alternative to--dangerously-skip-permissions.

* CategoryClaude CodeProduct announcements
* ProductClaude Code
* DateMarch 24, 2026
* Reading time5min
* ShareCopy linkhttps://claude.com/blog/auto-mode

Today, we're introducing auto mode, a new permissions mode in Claude Code where Claude makes permission decisions on your behalf, with safeguards monitoring actions before they run. It's available now as a research preview on the Team plan, and coming to the Enterprise plan and API users in the coming days.

## How it works

Claude Code's default permissions are purposefully conservative: every file write and bash command asks for approval. It’s a safe default, but it means you can't kick off a large task and walk away, since Claude will request frequent human approvals along the way. While some developers choose to bypass permission checks with --dangerously-skip-permissions, skipping permissions can result in dangerous and destructive outcomes and should not be used outside of isolated environments.

Auto mode is a middle path that lets you run longer tasks with fewer interruptions while introducing less risk than skipping all permissions. Before each tool call runs, a classifier reviews it tocheck for potentially destructive actionslike mass deleting files, sensitive data exfiltration, or malicious code execution.

Actions that the classifier deems as safe proceed automatically, and risky ones get blocked, redirecting Claude to take a different approach. If Claude insists on taking actions that are continually blocked, it will eventually trigger a permission prompt to the user.

## What to expect

Auto mode reduces risk compared to --dangerously-skip-permissions but doesn't eliminate it entirely, and we continue to recommend using it in isolated environments. The classifier may still allow some risky actions: for example, if user intent is ambiguous, or if Claude doesn't have enough context about your environment to know an action might create additional risk. It may also occasionally block benign actions. We’ll continue to improve the experience over time.

Auto mode may have a small impact on token consumption, cost, and latency for tool calls.

## Getting started

Auto mode is available in Claude Code as a research preview for Claude Team users today, and will roll out to Enterprise and API users in the coming days. It works with both Claude Sonnet 4.6 and Opus 4.6.

* For admins: Auto mode will soon be available for all Claude Code users on Enterprise, Team, and Claude API plans. To disable it for the CLI and VS Code extension, set "disableAutoMode": "disable" in your managed settings. Auto mode is disabled by default on the Claude desktop app, and can be toggled on using Organization Settings -> Claude Code.
* For developers: Run `claude --enable-auto-mode` to enable auto mode, then cycle to it with Shift+Tab. On Desktop and in the VS Code extension, first toggle auto mode on in Settings -> Claude Code, then select it from the permission mode drop-down in a session.

Explore the docsfor more information.

No items found.
Prev
Prev
0
/
5
Next
Next
Get Claude Code

curl -fsSL
 https://claude.ai/install.sh
| bash
Copy command to clipboard
irm
 https://claude.ai/install.ps1
| iex
Copy command to clipboard
Or read the
documentation
Try Claude Code
Try Claude Code
Try Claude Code
Developer docs
Developer docs
Developer docs
eBook

FAQ

No items found.

## Related posts

Explore more product news and best practices for teams building with Claude.

Mar 19, 2026

### Product management on the AI exponential

Claude Code
Product management on the AI exponential
Product management on the AI exponential
Product management on the AI exponential
Product management on the AI exponential
Jan 26, 2026

### Your favorite work tools are now interactive connectors inside Claude

Product announcements
Your favorite work tools are now interactive connectors inside Claude
Your favorite work tools are now interactive connectors inside Claude
Your favorite work tools are now interactive connectors inside Claude
Your favorite work tools are now interactive connectors inside Claude
Mar 23, 2026

### Put Claude to work on your computer

Product announcements
Put Claude to work on your computer
Put Claude to work on your computer
Put Claude to work on your computer
Put Claude to work on your computer
Mar 12, 2026

### Claude now creates interactive charts, diagrams and visualizations

Product announcements
Claude now creates interactive charts, diagrams and visualizations
Claude now creates interactive charts, diagrams and visualizations
Claude now creates interactive charts, diagrams and visualizations
Claude now creates interactive charts, diagrams and visualizations

## Transform how your organization operates with Claude

See pricing
See pricing
See pricing
Contact sales
Contact sales
Contact sales

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Subscribe
Subscribe

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

Thank you! You’re subscribed.
Sorry, there was a problem with your submission, please try again later.
