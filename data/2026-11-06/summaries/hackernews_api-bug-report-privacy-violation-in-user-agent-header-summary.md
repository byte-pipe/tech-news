---
title: Bug Report: Privacy violation in User-Agent header · Issue #107757 · anthropics/claude-code · GitHub
url: https://github.com/anthropics/claude-code/issues/107757
date: 2026-11-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-06T12:29:07.564097
---

# Bug Report: Privacy violation in User-Agent header · Issue #107757 · anthropics/claude-code · GitHub

# Bug Report: Privacy violation in User-Agent header

## Description
- The reporter (taylor‑edwards) receives dozens of scam emails daily because Claude Code includes their email address in the `User-Agent` request header during web searches.
- This exposure occurs without permission and is not presented as an opt‑in or opt‑out setting.
- The reporter argues the practice offers no benefit, harms anonymity, and provides a valuable target for scammers.
- As a result, they are migrating to alternative services (Pi with OpenRouter) due to loss of trust in Anthropic’s privacy handling.

## Environment Info
- Platform: darwin (macOS)
- Terminal: tmux
- Claude Code version: 2.1.318
- Feedback ID: f81eb83d-9b95-4788-8773-d3fae8f0cec4

## Reactions
- The issue has received 137 “👍” reactions and 19 “👀” reactions from the community, indicating strong interest and concern.