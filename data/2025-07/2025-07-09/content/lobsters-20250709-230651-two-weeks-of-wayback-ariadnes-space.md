---
title: Two weeks of wayback · Ariadne's Space
url: https://ariadne.space/2025/07/07/two-weeks-of-wayback.html
site_name: lobsters
fetched_at: '2025-07-09T23:06:51.508204'
original_url: https://ariadne.space/2025/07/07/two-weeks-of-wayback.html
date: '2025-07-09'
published_date: '2025-07-07T21:28:10-07:00'
tags: linux
---

# Two weeks of wayback

Jul 7, 2025

· 3 min read

A poorly kept secret is that the X11 graphics stack is under-maintained as resources shift towards the maintenance of Wayland’s graphics stack instead. To some extent, technical steering committees in major distributions have been watching this situation develop for the past few years with increasing concern, as limited maintenance becomes a security risk: bugs accumulate and already burdened distribution security teams have to carry the security maintenance load in an absence of new releases.

In Alpine, we have been discussing the sunset of the standalone X.org server implementation for several years for these reasons to come up with a strategy that allows us to keep supporting X11-based desktop environments in a world without the X.org server. Recently, a group of neofascist reactionaries announced a fork of the X.org server which, amongst other things,has introduced new security bugs into the X server they forked from X.org, which brought Alpine to a new crossroads in the general discussion we’ve been having about X11. While Alpine has rejected this fork on the grounds that collaborating with neofascist reactionaries is fundamentally incompatible with our values, the overarching problem of X11 under-maintenance still persists, and is unlikely to change any time soon, leading us to begin directly looking for a solution.

## Enter Wayback: just enough Wayland to make Xwayland work

For the past year or so, the main idea circulating around the Alpine community to solve the X11 maintenance problem has been the creation of a stub Wayland compositor that can sit in front of Xwayland and act as a full X server. Given the timing and desire to put the X11 maintenance issue to bed entirely, I decided to write a quick and dirty proof of concept over a weekend, sharing it on Mastodon and BlueSky:

Since then, a lot has happened: we have been slowly putting the foundational pieces together to build a replacement X stack around Xwayland, and enough is now there for people with simple setups to use wayback as their daily X11 implementation, as long as they don’t mind bugs.

## Towards the first Wayback release

There’s a lot still left to do before we can confidently say that Wayback is ready for distributions to switch to. This work is across the stack: Wayback still needs to expose surfaces that Xwayland can use, Xwayland needs to implement a few new features such as cursor warping and some X extensions inside Xwayland itself need to be properly plumbed (such as Xinerama being able to make use of the Wayland output layout data).

Longer term goals aside, we are at most a few weeks away from the first alpha-quality release of Wayback. The main focus of this release is to get to a point where enough is working that users with basic setups and requirements can be reasonably served by Wayback in place of the X.org server, to allow for further testing. It’s already to a point where I am daily driving it:

Of course, while the first release is coming soon, the project remains in an experimental state, and the first release will itself be experimental, but we’re making real progress towards a sustainable solution for the X11 problem. Come join us in IRC (irc.libera.chat #wayback) or Matrix (#wayback:catircservices.org)! Unlike other projects, we are focused on building real solutions rather than fascism.
