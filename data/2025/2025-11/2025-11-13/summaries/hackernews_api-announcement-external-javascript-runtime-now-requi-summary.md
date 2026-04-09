---
title: [Announcement] External JavaScript runtime now required for full YouTube support · Issue #15012 · yt-dlp/yt-dlp · GitHub
url: https://github.com/yt-dlp/yt-dlp/issues/15012
date: 2025-11-12
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-13T11:13:19.859787
screenshot: hackernews_api-announcement-external-javascript-runtime-now-requi.png
---

# [Announcement] External JavaScript runtime now required for full YouTube support · Issue #15012 · yt-dlp/yt-dlp · GitHub

**yt-dlp Update: External JavaScript Runtime Required**

* **Requiring an external JavaScript runtime**: To support full YouTube download functionality, yt-dlp now requires the use of an external JavaScript runtime.
* **Recommended runtimes**: The following JavaScript runtimes are currently supported:
  1. Deno (recommended for most users)
   - Install via: [Deno](https://deno.com/) and [GitHub releases]
2. Node.js (for security reasons)
3. QuickJS
4. QuickJS-ng
5. Bun

* **Additional requirement**: The yt-dlp-ejs component, which enables the use of an external JavaScript runtime, is now included in all official yt-dlp executables.

* **Support for YouTube**: However, support for full YouTube download functionality is no longer considered "dePRECATED" and relies entirely on the use of an external JavaScript runtime.
