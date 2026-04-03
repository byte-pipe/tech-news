---
title: DOOM crash after 2.5 years of real-world runtime confirmed on real hardware - LenOwO
url: https://lenowo.org/viewtopic.php?t=31
site_name: hackernews
fetched_at: '2025-09-17T19:06:46.391234'
original_url: https://lenowo.org/viewtopic.php?t=31
author: minki_the_avali
date: '2025-09-17'
published_date: '2025-09-16T23:22:48+02:00'
description: Two and a half years ago, I started my now longest real-world software experiment. I had read an article about how DOOMs engine works and noticed how a variable
---

## DOOM crash after 2.5 years of real-world runtime confirmed on real hardware

A discussion group for the most cursed software ideas out there

Post Reply

* Print view

Search

Advanced search

			1 post
							• Page
1
 of
1



minki


Site Admin

Posts:

15

Joined:
 2024-03-25

Location:
 /bin/bash

Contact:

Contact minki



### DOOM crash after 2.5 years of real-world runtime confirmed on real hardware

* Quote

Postbyminki»2025-09-16

Two and a half years ago, I started my now longest real-world software experiment. I had read an article about how DOOMs engine works and noticed how a variable for tracking the demo kept being incremented even after the next demo started. This variable was compared with a second one storing its previous value. The issue here being, each incrementation would cause the variable to slowly get closer to an overflow, realistically this would never happen in a normal scenario, although it got me curious on just how long it would take until the game would crash due to this.

I did a few calculations, I don't remember the specifics of it sadly as it has been over two years since that point and I sadly did not document it back then (or I did, but on a partition I no longer have access to) but I remember having gotten roughly 2 1/2 years of possible runtime before an overflow. Obviously, I wanted to know if this would actually happen in the real game on real hardware.

So I set up DOOM on a small PDA, powered through a DIY 18650 based UPS which itself was connected to the USB port of my router for a constant 5V supply. I left the system running and mostly forgot about it.

... Until today when I noticed a pop-up appearing on the device, not long ago from posting this to the board. The game had crashed, only hours after the two and a half year mark, proving that the variable did indeed overflow and cause the expected hard crash of the game:

IMG_20250916_224553.jpg (81.99 KiB) Viewed 67652 times

~-~-~
M
S
D
 - Making your old devices useful again since 2022! ~-~-~

Top

Post Reply

* Print view

			1 post
							• Page
1
 of
1

Return to “Software shenanigans”

Jump to

* Cursed Hardware
* Software shenanigans
