---
title: "Google's Antigravity Bait and Switch | Sid's Blog"
url: https://www.0xsid.com/blog/antigravity-bait-n-switch
date: 2026-05-21
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-22T06:03:29.264894
---

# Google's Antigravity Bait and Switch | Sid's Blog

# Google's Antigravity Bait and Switch | Sid's Blog

## Overview
- Started the day expecting the usual Antigravity IDE workflow.
- Google released a new Codex‑style version at I/O 2026 that auto‑updated my installation.

## Issue Encountered
- The auto‑update replaced the IDE with a single conversational prompt box.
- My daily workflow (plan‑review‑implement loop) was broken; the new chatbot interface is unsuitable for production work.

## Compatibility Problems
- Google offered a legacy installer, but the 2.0 update rewrites default application paths.
- Both the old IDE and the new chatbot cannot coexist; reinstalling the IDE still launches the chatbot.

## Solution: Purge & Reinstall
- Consulted the Antigravity subreddit; many reported the same issue.
- Performed a complete purge of all Antigravity‑related files.
- Reinstalled the standalone IDE after the purge; the clean install restored the original interface.

## Aftermath
- The forced update erased chat history and settings.
- Some configuration could be copied from an old Cursor setup; a folder named `antigravity-backup` may contain the lost data.
- Restoring history is postponed due to lack of time and token budget.

## Opinion on Updates
- Background updates should deliver patches, not replace an entire tool.
- Hijacking a development environment is a major inconvenience and undermines trust.
- Planning to investigate ways to disable auto‑updates to preserve tool stability.