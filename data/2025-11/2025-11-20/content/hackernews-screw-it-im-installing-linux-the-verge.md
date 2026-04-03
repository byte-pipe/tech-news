---
title: Screw it, I’m installing Linux | The Verge
url: https://www.theverge.com/tech/823337/switching-linux-gaming-desktop-cachyos
site_name: hackernews
fetched_at: '2025-11-20T11:07:27.196506'
original_url: https://www.theverge.com/tech/823337/switching-linux-gaming-desktop-cachyos
author: Nathan Edwards
date: '2025-11-20'
published_date: '2025-11-19T13:00:00+00:00'
description: Windows is getting worse, while gaming on Linux is getting better. I’m gonna move my desktop to CachyOS. Wish me luck.
---

* Tech
* Gaming
* Report

# Screw it, I’m installing Linux

I don’t like where Windows is going. Gaming on Linux has never been more approachable. Time to give it a shot.

I don’t like where Windows is going. Gaming on Linux has never been more approachable. Time to give it a shot.

by


Nathan Edwards
Nov 19, 2025, 1:00 PM UTC
* Link
* Share

If you buy something from a Verge link, Vox Media may earn a commission.See our ethics statement.

Penguin not actual size.

Image: Cath Virginia / The Verge, Linux
Nathan Edwards

is a senior reviews editor who’s been testing tech since 2007. Previously at
Wirecutter
 and
Maximum PC
. Current fixations: keyboards, DIY tech, and the smart home.

This time I’m really going to do it. I am going to put Linux on my gaming PC. Calling it now. 2026 is the year of Linux on the desktop. Or at least on mine.

Linux has been a perfectly viable desktop OS for ages. Butgamingon Linux is now viable, too. Valve’s hard work gettingWindows games to run well on the Linux-based Steam Deckhas lifted all boats. Gaming handhelds that ship with Windowsrun better and have higher frame rates on Bazzite, a Fedora-based distro, than they do with Windows. And after reading about the upcomingSteam MachineandAntonio’s experience running Bazzite on the Framework Desktop, I want to try it.

### Related

* Our first look at the Steam Machine, Valve’s ambitious new game console
* Three years later, the Steam Deck has dominated handheld PC gaming
* Why is Windows 11 so annoying?

To be clear, my desktop works fine on Windows 11. But the general ratio of cool new features to egregious bullshit is low.I do not want to talk to my computer. I do not want to use OneDrive.I’m sure as hell not going to use Recall. I am tired of Windows trying to get me to use Edge, Edge trying to get me to use Bing, andeverything trying to get me to use Copilot. I paid for an Office 365 subscription so I could edit Excel files. Then Office 365 turned into Copilot 365, and I tried to use it to open a Word documentand it didn’t know how.

Meanwhile, Microsoft isending support for Windows 10, including security updates, forcing people to buy new hardware or live with the risks. It’s disabling workarounds that let youset up Windows 11 with a local accountor with older hardware. It’s turning Xboxes into PCs and PCs into upsells for its other businesses. Just this week, the company announced thatit’s putting AI agents in the taskbarto turn Windows into a “canvas for AI.” I do not think Windows is going to be a better operating system in a year, so it feels like a good time to try Linux again.

I’m not normally one to change frogs midstream, but the water sure is getting hot.

Coming soon to a taskbar near you! But not near me.

Image: Microsoft

That’s not to say I know what I’m doing. I’ve used Macs for a decade for work, and I dabbled in Ubuntu 20-something years ago, but otherwise I’ve been a Windows guy since 3.1. At first, that’s because it’s what we had at home, later because that’s where the games were, and finally out of force of habit (and because that’s where the games were). I brought a desktop to college instead of a laptop (so I could play games), and I’ve been building my own PCs for 18 years. I started my journalism career atMaximum PCmagazine, testing gaming PC components.

I try to stay familiar with all the major operating systems because of my job, so in addition to my work MacBook I also have a Chromebook, a ThinkPad, and a collection of older hardware I refuse to get rid of. I can work pretty well in Windows, in macOS, or in ChromeOS.

My experiences with Linux over the past decade, on the other hand, have largely been as a series of extremely optional Tasks:

* Trying to set up Homebridge on a Raspberry Pi. It sort of worked but was stymied by my home network setup, and I eventually replaced it with Home Assistant.
* Setting up aBeepy, a kind of a bootleg Linux handheld with a tiny monochrome screen and a BlackBerry keyboard. This took longer than I wanted, but it worked in the end, and I learned that using a command-line interface with a BlackBerry keyboard on a tiny monochrome screen is my version of hell.
* Running a Linux VM on my Chromebook so I could useObsidian, my preferred note-taking app, which doesn’t have a web interface. This was a pleasant experience and I have no complaints.
* [deep breath] Setting up three different virtual machines using the Windows Subsystem for Linux so I could build keyboard firmware: one for QMK, one for ZMK, and I think the third was because the first QMK one stopped working. All of these were on my old desktop, on which the entire Linux subsystem somehow broke beyond repair.

All of those projects, except the Chromebook one, took longer than expected, and cut into my vanishingly rare discretionary time. That’s also the time I use for gaming, reading, staring into the void, and half-starting organizational projects, so you can see how precious it is to me.

The prospect of instead using that time trying to get my computer back to a baseline level of functionality — that is, as useful as it was before I tried installing Linux — is tempting, but it’s also why I haven’t done it yet.

It’s a good time to try gaming on Linux. Antonio and Sean have beenhaving fun with Bazzite, a Linux distro that mimics SteamOS; my friend and former colleague Will Smith is cohosting aPCWorldpodcast calledDual Boot Diarieswith this exact premise.

Imagine this but Linux.

Photo by Nathan Edwards / The Verge

And what better device to try it on than my personal desktop with anAMD Ryzen 7 9800X3D processorandNvidia GeForce RTX 4070 Super graphics card? I just rebuilt this thing. The Windows install is only like six months old. It’s working about as well as Windows does.

So really, whywouldn’tI blow that up and start over?

Based on listening to two and a half episodes ofDual Boot Diariesand a brief text conversation with Will, I’m going to installCachyOS, an Arch-based distro optimized for gaming on modern hardware, with support for cutting-edge CPUs and GPUs and an allegedly easy setup.

I don’t expect things to go smoothly. I don’treallyknow what I’m doing, and Linux is still a very small percentage of the PC gaming world. As of the most recentSteam Hardware & Software Survey— the best proxy we have for PC gaming hardware info as a whole — just over 3 percent of Steam users are running Linux. Of those, 27 percent are using SteamOS (and therefore a Steam Deck), 10 percent are using Arch, 6 percent are using CachyOS, 4 percent are using Bazzite, and the rest are split over a bunch of distros.

So if anything goes wrong in my install, it’ll be a lot of forum-hopping and Discord searching to figure it all out. But I’ve cleverly arranged it so the stakes are only medium: I have other machines to work on while my desktop is inevitably borked (and to run programs like Adobe Creative Suite), and if I end up spending hours of my discretionary time learning Linux instead of gaming, well, that’s not the worst outcome.

Maybe it’ll all go smoothly and I’ll report back in a few weeks, another prophet of the revolution. Maybe it’ll go terribly and I’ll come crawling back. Only one way to find out.

Follow topics and authors
 from this story to see more like this in your personalized homepage feed and to receive email updates.
* Nathan Edwards
* Analysis
* Gaming
* Linux
* PC Gaming
* Report
* Tech

## Most Popular

Most Popular
1. Screw it, I’m installing Linux
2. Europe is scaling back its landmark privacy and AI laws
3. The Echo Aviation Controller puts a flight simulator in your hands
4. The Apple Watch Series 11 has plunged to a record low price
5. Steam Machine and Steam Frame: your questions answered

## The Verge Daily

A free daily digest of the news that matters most.

Email (required)
Sign Up
By submitting your email, you agree to our

Terms
 and
Privacy Notice
.
This site is protected by reCAPTCHA and the Google

Privacy Policy

and

Terms of Service

apply.
Advertiser Content From

This is the title for the native ad

## More inTech

Google’s new Scholar Labs search uses AI to find relevant studies
The Verge’s 2025 holiday gift guide
I’m out of reasons to recommend Apple’s M1 MacBook Air, even at $600
The best Bluetooth trackers for Apple and Android phones
Future Google TV devices might come with a solar-powered remote
The Verge’s 2025 holiday gift guide for tinkerers
Google’s new Scholar Labs search uses AI to find relevant studies
Elissa Welle
Nov 19
The Verge’s 2025 holiday gift guide
Verge Staff
Nov 19
I’m out of reasons to recommend Apple’s M1 MacBook Air, even at $600
Cameron Faulkner
Nov 19
The best Bluetooth trackers for Apple and Android phones
Victoria Song
Nov 19
Future Google TV devices might come with a solar-powered remote
Andrew Liszewski
Nov 19
The Verge’s 2025 holiday gift guide for tinkerers
Brandon Russell
Nov 19
Advertiser Content From

This is the title for the native ad

## Top Stories

Nov 19
Here’s the Trump executive order that would ban state AI laws
Nov 19
This viral AI pen didn’t help me cheat
Nov 19
AI, my unexpected daily travel companion
Nov 19
Porsche crowns Cayenne Electric ‘most powerful production Porsche of all time’
Nov 19
Europe is scaling back its landmark privacy and AI laws
60 minutes ago
Nvidia has a fix for Windows 11 performance issues.
