---
title: 'John Graham-Cumming''s blog: There''s a ridiculous amount of tech in a disposable vape'
url: https://blog.jgc.org/2026/01/theres-ridiculous-amount-of-tech-in.html
site_name: hackernews_api
fetched_at: '2026-01-15T11:07:21.372152'
original_url: https://blog.jgc.org/2026/01/theres-ridiculous-amount-of-tech-in.html
author: abnercoimbre
date: '2026-01-12'
description: There's a ridiculous amount of tech in a disposable vape
tags:
- hackernews
- trending
---

## 2026-01-08

### There's a ridiculous amount of tech in a disposable vape

So, I'm walking through a park when I see this thing lying on the ground:

It's a disposable vape that someone has discarded because it's empty. Specifically, it's a "Fizzy Max III 60K Rechargeable Disposable Vape" and I was about to take it to a bin to throw away when I noticed it had USB-C. I know nothing about vapes so that was a total WTF moment.

Naturally, I took it home, sanitized it, and plugged it in. Not only did this thing have USB-C and a rechargeable battery, it had a small display showing battery percentage andpoisonvape fluid percentage. It looks kind of cyberpunk.

I ripped the thing apart and discarded the now empty chambers that had contained the fluid. At the bottom there are two circuit boards and a battery. 
The battery is an 800 mAh lipo.
So, wait? This is a disposable device. After 60,000 sucks on the teat you're meant to throw away a battery, display, microprocessor etc. WTF? Turns out that you're meant to recycle it, but it's crazy large amount of technology for nicotine sucking. 

On one side you've got three pairs of pins that are inserted into the chambers containing the vape fluid and are controlled by three transistors on the other PCB. These pins heat the fluid making the vape's vapour. They are activated by the three microphones seen in this picture.

The vape knows you're sucking on the teat in one of six positions by which combination of microphones sense the sucking. This allows it to heat one or two of the chambers providing six flavour combinations.

Three transistors and a small chip that controls charging of the battery. 
Sadly, despite there being some pretty obvious pads connected to the microprocessor (labelled B0081S1) and the fact that those pads are also connected to the USB-C connecter, I have been unable to talk to it via PyOCD or other tools. I was hoping this was a small ARM device that I might be able to hack.

at

January 08, 2026

Email This
BlogThis!
Share to X
Share to Facebook
Share to Pinterest

Labels:

hardware
,

pseudo-randomness

Older Post

Home

Subscribe to:

Post Comments (Atom)
