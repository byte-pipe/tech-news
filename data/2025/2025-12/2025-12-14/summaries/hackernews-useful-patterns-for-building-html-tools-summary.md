---
title: Useful patterns for building HTML tools
url: https://simonwillison.net/2025/Dec/10/html-tools/
date: 2025-12-14
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-14T11:19:58.058661
screenshot: hackernews-useful-patterns-for-building-html-tools.png
---

# Useful patterns for building HTML tools

# Useful Patterns for Building HTML Tools

Simon Willison's Weblog, 10th December 2025

I've been building several HTML tools over the past two years using a combination of HTML, JavaScript, and CSS in a single file. I'm sharing some useful patterns that have helped me speed up development.

## Examples of Useful Tools

1. **SVG Render**: Renders SVG code to downloadable images.
2. **Pypi Changelog**: Generates diffs between different PyPI package releases for easy comparison.
3. **Bluesky Thread**: Provides a nested view of a discussion thread on Bluesky.
4. HTML Tool Collection: Exposes dozens more useful tools, including [views](http://ool.timsweb.org/), [code snippets](http://github.com/simonwillison/tool-samples.json), and more.

## Anatomy of an HTML Tool

The following are the characteristics I've found to be most productive in building HTML tools:

1. **Single file**: Inline JavaScript, CSS, and dependencies in a single HTML file.
2. **No React**: Avoiding the unnecessary build step for complex projects, especially if there's a well-known library that simplifies the process.
3. **Load dependencies from CDN**: Using CDNs like jsdelivr or CDNJS to reduce dependency loads.
4. **Keep it small**: Limiting the number of lines in the codebase to maintain maintainability.

## Prototype with Artifacts or Canvas

When possible, prototype your tool using **Artifacts** or **Canvas**, which provide a more straightforward and efficient way to build complex tools than traditional approaches like React or Redux.

This approach enables you to create prototypes that can be easily deployed, updated, and maintained without unnecessary complexity.
