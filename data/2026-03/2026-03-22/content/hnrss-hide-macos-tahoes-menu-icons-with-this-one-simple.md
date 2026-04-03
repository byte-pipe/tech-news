---
title: Hide macOS Tahoe's Menu Icons With This One Simple Trick - 512 Pixels
url: https://512pixels.net/2026/03/hide-macos-tahoes-menu-icons-with-this-one-simple-trick/
site_name: hnrss
content_file: hnrss-hide-macos-tahoes-menu-icons-with-this-one-simple
fetched_at: '2026-03-22T11:09:51.881754'
original_url: https://512pixels.net/2026/03/hide-macos-tahoes-menu-icons-with-this-one-simple-trick/
author: Stephen Hackett
date: '2026-03-21'
published_date: '2026-03-21T14:58:20+00:00'
description: Hide macOS Tahoe's Menu Icons
tags:
- hackernews
- hnrss
---

Ireallydislike Apple’s choice to clutter macOS Tahoe’s menuswith icons. Itmakes menus hard to scan, and a bunch of the icons Apple has chosenmake no senseand are inconsistent between system applications.

Steve Troughton-Smithis my herofor finding a Terminal command to disable them:

Here’s one for the icons-in-menus haters on macOS Tahoe:

defaults write -g NSMenuEnableActionImages -bool NO

It even preserves the couple of instances you do want icons, like for window zoom/resize.

Your apps will respect this change after relaunching. I ran this a few minutes ago and already appreciate the change. I really think Apple should roll this change back in macOS 27, or offer a proper setting to disable these icons for those of us who find them distracting.