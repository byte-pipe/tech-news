---
title: Auto-grading decade-old Hacker News discussions with hindsight | karpathy
url: https://karpathy.bearblog.dev/auto-grade-hn/
date: 2025-12-10
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-13T11:09:46.153960
screenshot: hackernews_api-auto-grading-decade-old-hacker-news-discussions-wi.png
---

# Auto-grading decade-old Hacker News discussions with hindsight | karpathy

## Auto-grading decade-old Hacker News discussions with hindsight

yesterday i stumbled upon an old hackernext thread where a user linked to a future version of hnn from exactly 10 years ago (december 2015) [1]. this got me thinking about whether auto-grading our past predictions might actually be possible.

*   **The Future is Looking Bright**: I realized that it might be beneficial to train forward to the future, which could take a significant amount of time and effort.
*   **Security by Obscurity Assumption**: Right now, many people assume that sensitive information will remain secret, but if LLMs are too common, it may become possible to recreate everything in the future.
*   **The Power of hindsight**: It's worth noting that human behavior can be influenced by our current actions and knowledge. If I were to make similar predictions without considering the context now, future results might not reflect reality.

## How I Came Up with This Idea

I decided to start building a Python script, Opus 4.5, that fetches the front page of HN articles from December '25' and analyzes their content using LLMs like ChatGPT 5.1 Thinking.
### **The Project: hn-time-capsule**

This repository on GitHub contains the code for the project. It includes:
*   Downloading HN's front pages of 30 articles
*   Parsing and analyzing article comments using Algolia API
