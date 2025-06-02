---
date: 2025-06-01
description: I guess I write stuff.
enhanced_prompting: true
fetched_at: '2025-06-01T01:56:14.979875

  '
local_model: true
model: gemma3:27b
original_url: 'https://blog.pomdtr.me/posts/tweety-v1/

  '
site_name: lobsters
summarization_type: local_high_quality
summarized_at: '2025-06-01T02:03:52.421753'
summary_type: local_high_quality
tags: browsers, web
title: The case for using a web browser as your terminal
url: 'https://blog.pomdtr.me/posts/tweety-v1/

  '
---

• Here's a concise summary of the article, tailored for a technical audience:
• **Web-Based Terminal Emulation:** The article advocates for replacing traditional terminal emulator applications with a web-based approach, leveraging tools like `ttyd` and the author’s project, `tweety`, to run a terminal session directly within a web browser. This aims to consolidate applications and streamline workflow by utilizing the browser as a central hub.
• **URL-Based Command Execution & Security:**  `tweety` extends functionality by mapping URLs to specific commands, enabling execution via the browser's address bar or bookmarks.  Crucially, the author emphasizes security through controlled command whitelisting within the entrypoint script, preventing arbitrary code execution from malicious URLs and advocating for interactive commands over destructive ones.
• **Integration & Automation:** The article details methods for seamless integration with browser features – custom search engines for quick command access, bookmarking for frequently used commands, and automated startup via systemd (Linux) or launchd (macOS) plist files.  It also covers securing the connection with HTTPS and local certificates using a reverse proxy like Caddy.
