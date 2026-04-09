---
title: Zig Builds Are Getting Faster – Mitchell Hashimoto
url: https://mitchellh.com/writing/zig-builds-getting-faster
date: 2025-10-03
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-05T11:13:20.612527
screenshot: hackernews_api-zig-builds-are-getting-faster-mitchell-hashimoto.png
---

# Zig Builds Are Getting Faster – Mitchell Hashimoto

# Overview of Zig Build Improvements

## Introduction

The article discusses the improvements in Zig build times compared to its predecessor release 0.14. The key takeaways are:

* Initial build time: 1 second 702 milliseconds (Zig 0.15) vs. 7 seconds 167 milliseconds (Zig 0.14)
* Complete Ghostty project build time: 32 seconds (Zig 0.15) vs. 41 seconds (Zig 0.14)

## Incremental Build Times

The article highlights the incremental build times of several scenarios:

### 1. Build Script Compilation

* Initial compile time: 7 seconds 167 milliseconds
* Complete build script compilation: +723 milliseconds

### 2. Full Uncached Ghostty Binary Build Time

* Initial build time: 41 seconds
* Complete build script compilation plus additional tasks (e.g., self-hosted x86_64 backend): -9 seconds (-50% reduction)

## Incremental Build Times for Specific Use Cases

The article provides anecdotal evidence of significant improvements in incremental build times:

* Rebuilding a single line of code after updating the core terminal emulation code: 16 seconds
* Rebuilding only a specific library (libghostty-vt) after making one change: +975 milliseconds

## Conclusion

As of version release 0.15, Zig compiler performance has seen significant improvements. The time to build the full Ghostty project and its components has decreased substantially, and incremental build times are expected to approach millisecond levels soon.

Note: This summary is written based on the provided text and may not include any additional information or updates that may have occurred since the article was released.
