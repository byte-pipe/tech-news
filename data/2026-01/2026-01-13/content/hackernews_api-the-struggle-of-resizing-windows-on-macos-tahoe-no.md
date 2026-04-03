---
title: The struggle of resizing windows on macOS Tahoe – no.heger
url: https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/
site_name: hackernews_api
fetched_at: '2026-01-13T11:07:40.687383'
original_url: https://noheger.at/blog/2026/01/11/the-struggle-of-resizing-windows-on-macos-tahoe/
author: happosai
date: '2026-01-11'
description: The struggle of resizing windows on macOS Tahoe
tags:
- hackernews
- trending
---

A lot has already been said about the absurdly large corner radius of windows on macOS Tahoe. People are calling the way it looks comical, like a child’s toy, or downright insane.

Setting all the aesthetic issues aside – which are to some extent a matter of taste – it also comes at a cost in terms of usability.

Since upgrading to macOS Tahoe, I’ve noticed that quite often my attempts to resize a window are failing.

This never happened to me before in almost 40 years of using computers. So why all of a sudden?

It turns out that my initial click in the window corner instinctively happens in an area where the window doesn’t respond to it. The window expects this click to happen in an area of 19 × 19 pixels, located near the window corner.

If the window had no rounded corners at all, 62% of that area would lieinsidethe window:

But due to the huge corner radius in Tahoe, most of it – about 75% – now liesoutsidethe window:

Living on this planet for quite a few decades, I have learned that it rarely works to grab things if you don’t actually touch them:

So I instinctively try to grab the window corner inside the window, typically somewhere in that green area, near the blue dot:

And I assume that most people would also intuitively expect to be able to grab the corner there. But no, that’s already outside the accepted target area:

So, for example, grabbing it here doesnotwork:

But guess what – grabbing it heredoes:

So in the end, the most reliable way to resize a window in Tahoe is to grab itoutsidethe corner – a gesture that feels unnatural and unintuitive, and is therefore inevitably error-prone.
