---
title: Advanced Mac Substitute
url: https://www.v68k.org/advanced-mac-substitute/
site_name: hnrss
content_file: hnrss-advanced-mac-substitute
fetched_at: '2026-04-12T06:01:14.240304'
original_url: https://www.v68k.org/advanced-mac-substitute/
date: '2026-04-11'
description: Advanced Mac Substitute is an API-level reimplementation of 1980s-era Mac OS
tags:
- hackernews
- hnrss
---

# Advanced Mac Substitute

https://
www.v68k.org
/
advanced-mac-substitute
/

MacPaint
 running in
Advanced Mac Substitute
 (click to see video)

Advanced Mac Substitute

Advanced Mac Substituteis an API-level reimplementation of 1980s-era Mac OS.
It runs 68K Mac applications in an emulatorwithout an Apple ROM or system software.

System’s Twilight
 running in
Advanced Mac Substitute
.

Lode Runner
 running in
Advanced Mac Substitute

The opening of the
prologue
 cinematic from
The Fool’s Errand
 running in
Advanced Mac Substitute

Amazing
 running in
Advanced Mac Substitute
 (point to see the solved maze)

Unlike traditional emulators, Advanced Mac Substitute doesn’t emulate the hardware on which an operating system runs (except for the 680x0 processor), but actually replaces the OS — so it launches directly into an application, without a startup phase.

Welcome
 to
Advanced Mac Substitute
.

(This is an application, not a real loading screen.)

Advanced Mac Substitute is afactored application. Thebackendincludes a 68K emulator and should build and run on any POSIX-like system. Thefrontendis a generic bitmapped terminal abstraction, provided by SDL2 (for various platforms) along with custom implementations for macOS, X11, and Linux framebuffer (fbdev).

Advanced Mac Substitute is capable of running several applications written for the original Macintosh computer. Examples include four games from 1984:Amazing,Solitaire,Missile, andIAGO.

Missile
 running in
Advanced Mac Substitute
 (point to see the next frame)

IAGO
 running in
Advanced Mac Substitute
 (point to see who won)

Currentsupportincludes 1-bit-deep graphics, regions, circles and roundrects, lines, cursors, GrafPorts, text, windows, controls, menus, dialogs, and more.

## Source

Source codefor Advanced Mac Substitute is on GitHub.

If you’re feeling adventurous, you cantry out Advanced Mac Substitutein macOS / OS X, the X Window System, a Linux framebuffer console, or a VNC client.

Nyanochrome Cat
 running in
Advanced Mac Substitute
 (point to animate)

(Older documentationhas moved while revision is under way.)
