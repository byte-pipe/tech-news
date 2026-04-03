---
title: macOS Tahoe windows have different corner radiuses
url: https://lapcatsoftware.com/articles/2026/3/1.html
site_name: hnrss
content_file: hnrss-macos-tahoe-windows-have-different-corner-radiuses
fetched_at: '2026-03-10T11:15:54.128085'
original_url: https://lapcatsoftware.com/articles/2026/3/1.html
date: '2026-03-06'
description: macOS Tahoe windows have different corner radiuses
tags:
- hackernews
- hnrss
---

# macOS Tahoe windows have different corner radiuses

### March 4 2026

I’m sometimes late to notice new and terrible things about macOS 26 Tahoe, because I use it only for testing, on a secondary Mac. My main Mac remains on Sequoia,as enforced by Little Snitch. I was of course aware that app windows on Tahoe have exaggerated corner radiuses, but I was unaware until now that the window corner radius on Tahoe is not uniform: different windows can have different corner radiuses!

Below is a TextEdit window on Tahoe.

And below is a Calculator window in front of the TextEdit window. Notice the corners of the TextEdit window sticking out!

What accounts for the difference? A toolbar in the window.

In a new Mac app Xcode project, the main window has a less exaggerated corner radius by default, like TextEdit.

When I add a toolbar to the window, the corner radius automatically becomes more exaggerated, like Calculator.

That’s it. Seriously.

Apparently the corner radius also changes on Tahoe for some other window elements, such as a sidebar.

If this isn’t the stupidest user interface “feature” ever invented, I don’t know what is. The Mac used to be famous for consistency; now it’s becoming infamous for inconsistency.

By the way, Tahoe’s UI changes are perplexing not only for Apple users but also for Apple engineers. Here’s a bug fix from the open source WebKit browser engine powering Safari:[macOS] Scroll bars of root scroller may be cutoff due to corner radii of window.