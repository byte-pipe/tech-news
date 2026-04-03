---
title: Resizing windows on macOS Tahoe – the saga continues – no.heger
url: https://noheger.at/blog/2026/02/12/resizing-windows-on-macos-tahoe-the-saga-continues/
site_name: hackernews_api
content_file: hackernews_api-resizing-windows-on-macos-tahoe-the-saga-continues
fetched_at: '2026-02-13T11:15:48.666049'
original_url: https://noheger.at/blog/2026/02/12/resizing-windows-on-macos-tahoe-the-saga-continues/
author: erickhill
date: '2026-02-12'
description: Resizing windows on macOS Tahoe – the saga continues
tags:
- hackernews
- trending
---

## macOS 26.3, Release Candidate

In the release notes for macOS 26.3 RC, Apple stated that the window-resizing issue I demonstrated inmy recent blog posthad been resolved.

I was happy to read that, but also curious about what had actually changed.

So I wrote a little test app.

It performs a pixel-by-pixel scan in the area around the bottom-right corner of the window, hammering it with simulated mouse clicks to detect exactly where it responds to those clicks (red), where it’s about to resize (green), where it’s about to resize vertically or horizontally only (yellow), and where it doesn’t receive any mouse events at all (blue).

And indeed, the window resize areas now follow the corner radius instead of using square regions:

So that’s definitely better!

But unfortunately, as you can see, the thickness of the yellow area – used for resizing the window only vertically or horizontally – also became thinner. The portion that lies inside the window frame is now only 2 pixels instead of 3.

In total the thickness went down from 7 to 6 pixels, which is a 14% decrease, making it 14% more likely to miss it.

## macOS 26.3, Final Release

When the final version of macOS 26 was released I was curious if Apple might have further refined the implementation. So I performed the scan once again. But to my big surprise, the fix was not only unrefined – it was completely removed! So we are now back to the previous square regions:

And in fact, the release notes have also been updated: the problem went from a “Resolved Issue” to a “Known Issue”.
