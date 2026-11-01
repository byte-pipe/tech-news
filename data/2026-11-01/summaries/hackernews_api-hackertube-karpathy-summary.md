---
title: HackerTube – karpathy
url: https://karpathy.bearblog.dev/hacker-tube/
date: 2026-11-01
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-11-01T18:53:59.158251
---

# HackerTube – karpathy

# HackerTube – Summary

## Overview
- The author was frustrated with YouTube’s low‑quality recommendations and decided to build a better alternative using Opus 5.5.
- The new site, **hackertube.org**, aggregates YouTube videos that have been recommended in Hacker News comments from 2007‑2026.

## Data Collection & Processing
- Opus downloaded all Hacker News comments, filtered out spam, and used Sonnet in a Claude Code workflow to extract recommendations.
- Result: 40 000 relevant comments pointing to 6 454 unique YouTube videos across ~150 topics.

## Features of HackerTube
- Curated, high‑quality content sourced from Hacker News.
- Uses a 50 % thumbnail (instead of the original uploader’s thumbnail) for consistency.
- Provides custom “For You” recommendations without requiring user accounts; state is stored locally in the browser session.
- Includes keyboard shortcuts for navigation.
- Offers an export of the site’s data so users can create their own instances.

## Implementation Process
1. **Tooling**: Used Claude Code (Mac desktop app) with Opus 5.5 set to “Medium effort.”
2. **Manual steps**:
   - Created a Google Cloud API key to fetch YouTube video metadata.
   - Launched a VPS instance.
   - Purchased the domain name.
3. **Automation**: Gave Claude the VPS IP; it handled updating, deploying, securing, hardening, and optimizing the code.
4. **Time investment**: The entire workflow took roughly 2 hours.

## Reflection
- The author no longer writes code manually; instead, they converse with Claude, which performs the engineering tasks.
- The project feels collaborative, with the author overseeing high‑level steps while Claude executes the details.