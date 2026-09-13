---
title: Apple iPod engraver
url: https://dunstanorchard.com/apple-ipod-engraver/
site_name: hnrss
content_file: hnrss-apple-ipod-engraver
fetched_at: '2026-09-13T14:50:17.471147'
original_url: https://dunstanorchard.com/apple-ipod-engraver/
date: '2026-09-09'
description: Making the iPod engraver page for Apple’s online store
tags:
- hackernews
- hnrss
---

I spent 2004–2006 working at Apple as a UI engineer for their online store. Part of my job was to prototype concepts that would add some interactive sparkle to the site.

One such project improved the “Personalize your iPod” page, where customers could submit two lines of text to be engraved on the back of the iPod they were ordering.

As originally designed the page offered no interaction beyond a plain form. I added a rotatable iPod, a live “engraved” preview of the customer’s text, and a highlight of any change in shipping times.

I animated the iPod by cycling through a series of JPEGs using JavaScript. The engraving was created usingimagemagick, which took the user’s text and returned an “engraved” image to be overlaid on the rear of the iPod. The shipping highlight was achieved by switching CSS classes to change the background color, in the style of aclassic yellow fade.

There’s an oldworking demoif you’d like to try it yourself.

We obviously have much better ways of doing such things today, but in 2005, with limited browser technology, those solutions seemed a little bit magical.