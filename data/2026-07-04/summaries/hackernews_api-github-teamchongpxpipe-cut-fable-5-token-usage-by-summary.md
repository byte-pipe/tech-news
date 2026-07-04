---
title: GitHub - teamchong/pxpipe: cut Fable 5 token usage by rendering text context as images · GitHub
url: https://github.com/teamchong/pxpipe
date: 2026-07-03
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-07-04T11:35:55.880586
---

# GitHub - teamchong/pxpipe: cut Fable 5 token usage by rendering text context as images · GitHub

**Fable Token Optimization with pxpipe**
=====================================

The `pxpipe` project is a local proxy that optimizes Fable 5 token usage by rewrites bulky code sections into compact PNG images before leaving the machine. This results in a significant cost reduction, particularly for servers working with large text datasets.

### Key Points:

*   The system prompt, tool docs, and previous bulk history information are preserved in the image.
*   Real pipeline output is rendered as 100% of the tokens processed, making it a cost-effective option.
*   pxpipe is designed to work with current Fable prices and may not be suitable for all servers or use cases.

### Demo:

The demo uses `Fable AB-Demo.mp4` and compares its token usage against 39 identical images, showcasing how much of the original text content is lost due to rewrites. The output shows that pxpipe can reduce token costs by up to 73.5% on average.

**Comparison Points:**

*   **Token cost**: Reduced or eliminated for servers using Fable 5, resulting in significant savings.
*   **Server requirements**: No major changes needed for servers operating with standard pipelines; only a local proxy is required.
*   **Faster throughput**: Replacements reduce overall token processing time to match real pipeline output.

### Try it (30 seconds):

`npx pxpipe-proxy`

*   Get access to the `pxpipe` proxy server at `http://127.0.0.1:47821`.
*   Point Claude Code's input tokens through the proxy with the requested URL, and the system prompt, tool docs, and previous bulk history will be preserved in the image.

By leveraging pxpipe for Fable 5 token usage optimization, servers can enjoy significant cost savings and improved performance while still maintaining a real pipeline output.