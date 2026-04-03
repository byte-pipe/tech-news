---
title: [Announcement] Upcoming new requirements for YouTube downloads · Issue #14404 · yt-dlp/yt-dlp · GitHub
url: https://github.com/yt-dlp/yt-dlp/issues/14404
date: 2025-09-24
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-09-25T00:49:52.364492
screenshot: hackernews_api-announcement-upcoming-new-requirements-for-youtube.png
---

# [Announcement] Upcoming new requirements for YouTube downloads · Issue #14404 · yt-dlp/yt-dlp · GitHub

Here is a concise and informative summary of the article:

**Upcoming Requirements for YouTube Downloads**

* Starting September 23, 2025, yt-dlp will require Deno or another supported JavaScript runtime to function properly.
* Existing users will need to install Deno or ensure their existing setup can handle deno installations.
* The changes are primarily aimed at supporting more robust and modern JavaScript environments on YouTube.

**What's Changing?**

* YouTube has recently made significant changes to its backend, making the existing built-in JavaScript interpreter insufficient for downloading content.
* yt-dlp will need to leverage a newer, supported JavaScript runtime to continue functioning as intended.

**Action Items:**

* Deno support users: Install and upgrade yt-dlp with or without deno's optional dependency group (pip install -U "yt-dlp[default]") or run with additional flags for npm dependencies.
* Other users with third-party package installations: Check the repository to determine the best course of action, as this may vary depending on the package manager.
