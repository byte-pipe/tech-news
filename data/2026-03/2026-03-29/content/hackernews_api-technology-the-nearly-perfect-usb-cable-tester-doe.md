---
title: 'Technology: The (nearly) perfect USB cable tester does exist | Literarily Starved'
url: https://blog.literarily-starved.com/2026/02/technology-the-nearly-perfect-usb-cable-tester-does-exist/
site_name: hackernews_api
content_file: hackernews_api-technology-the-nearly-perfect-usb-cable-tester-doe
fetched_at: '2026-03-29T19:15:57.868409'
original_url: https://blog.literarily-starved.com/2026/02/technology-the-nearly-perfect-usb-cable-tester-does-exist/
author: birdculture
date: '2026-03-25'
published_date: '2026-02-01T12:13:00+02:00'
description: A nearly perfect USB cable tester
tags:
- hackernews
- trending
---

As probably everyone reading this blog, I have a lot of USB cables. I want to sort and categorize them. What the cable can and cannot do is an important factor. But how do I really find out what a cable supports?As I found out during this quest, your cable may successfully lie to your PC.

### Previous attempts

I always thought: The perfect USB cable tester doesn’t exist. Unitl now I used a cable tester that used LEDs that show the status of a USB cable.

This came with one major annoyance: every time I had to retrieve the manual what that specific pattern implies.

At least for USB C cables I thought I had found a very clever way to determine what speed was supported:

* I used it to connect a device that supported 20gbps (e.g. a SSD)
* Then I looked up whatsystem_profiler SPUSBDataTypeon macOS told me about the connection speed.

At that point I discovered: my cables keep lying to my PC. The cable tester showed that a speed above USB 2.0 was physically impossible, but macOS still was happily reporting to have that disk connected with 10gbps. Some tests reading/writing that disk confirmed that “something is rotten in the state ofDenmarkUSB.”

### The Treedix USB Cable Tester with 2.4" Color Screen

Then one day I stumbled over theTreedix USB Cable Tester with 2.4" Color Screen. It pressed all my buttons: wide range of supported plug types, clear and easy to parse information and a real deep dive what your cable says it does.

Power supply is either a AAA battery or through an external USB C cable on a dedicated port. I guess that port also allows to update the system although all hints on that were just some posts on Reddit.

What kind of cables can it check?

* Side A: USB-A or USB-C
* Side B: USB-C, Mini, Micro, Micro-B

The device has a mode button with which you can cycle through different modes:

* Data and Power modes:
* Connected lanes:
* Resistance values:
* Cable eMarker

This is pretty easy to understand… or so it seemed.

### My experience

Then I started rating my cables. One of the cables that I expected to be rated quite high showed a contradictory output:

Data and Power modes are USB 2.0 and PD 3.0:

The connected lanes match to that output:

But the eMarker tells a completely different story: 20gbps and USB4 Gen2

When I look at what my PC tells me when I connect it with an SSD through that cable: it shows what the eMarker says, despite missing the required SuperSpeed lanes.The cable lies to your PC and the PC believes it.As it turned out, that is not an exception. I found three cables that showed a similar behavior. Every single one of them was a USB C to USB C cable.At this point, the cable was no longer a passive piece of copper, but a rather unreliable narrator.

Identifying those cables already paid for the USB cable tester. I had a lot less “high quality” cables than I previously believed.

I developed based on the result a marking standard for my cables and a method to sort them. But that is a story for another post.

The only downside of the USB cable tester is that I would love to support more plugs on the B side: USB-A (for my Frankencables) and USB B (which everyone but seems to think extinct).

Overall I am very, very happy with this USB cable tester and can only recommend it. It costs about 45 US$.

You can comment on this post in the thread onMastodon.