---
title: [Announcement] External JavaScript runtime now required for full YouTube support · Issue #15012 · yt-dlp/yt-dlp · GitHub
url: https://github.com/yt-dlp/yt-dlp/issues/15012
date: 2025-11-12
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-14T11:17:49.914606
screenshot: hackernews_api-announcement-external-javascript-runtime-now-requi.png
---

# [Announcement] External JavaScript runtime now required for full YouTube support · Issue #15012 · yt-dlp/yt-dlp · GitHub

Here's a concise and informative summary of the article:

**External JavaScript Runtime Required for Full YouTube Support**

* The latest **yt-dlp** version (2025.11.12) requires an external JavaScript runtime for full support from YouTube.
* Currently supported JavaScript runtimes:
	+ Deno: Strongly recommended, can be installed via GitHub releases or using the `denonote` package.
	+ Node.js (20.x): Required for security reasons and to ensure compatibility with **yt-dlp**.
	+ QuickJS (2023-12-09 and later): Recommended for performance purposes; also supports other runtimes, like Bun.
* Optional extra components:
	+ `yt-dlp-ejs`: Included in all official releases of **yt-dlp**, already included if using the default package or Python installation.

**Important Note:**

* YouTube support without a JavaScript runtime is now considered "deprecated" and format availability may decrease over time.
