---
title: Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords
url: https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/
site_name: hackernews_api
content_file: hackernews_api-ubuntu-2604-ends-46-years-of-silent-sudo-passwords
fetched_at: '2026-03-22T11:09:46.851638'
original_url: https://pbxscience.com/ubuntu-26-04-ends-46-years-of-silent-sudo-passwords/
author: Linux
date: '2026-03-21'
published_date: '2026-03-20T05:48:03+00:00'
description: Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords. Starting with the upcoming LTS release, every keystroke at a sudo password prompt will echo an asterisk — a small UX fix that has ignited one of Linux's fiercest debates in years.
tags:
- hackernews
- trending
---

* Facebook
* Twitter

## Ubuntu 26.04 Ends 46 Years of Silent sudo Passwords

* Why Enterprise RAID Rebuilding Succeeds Where Consumer Arrays Fail?
* Linus Torvalds Rejects MMC Subsystem Updates for Linux 7.0: “Complete Garbage”
* The Man Who Maintained Sudo for 30 Years Now Struggles to Fund the Work That Powers Millions of Servers
* How Close Are Quantum Computers to Breaking RSA-2048?
* Why Windows 10 Users Are Flocking to Zorin OS 18 Instead of Linux Mint?
* How to Prevent Ransomware Infection Risks?
* What is the best alternative to Microsoft Office?

Ubuntu 26.04 Breaks 46 Years of sudo Tradition

Ubuntu & Open Source

## Ubuntu 26.04 Ends46 Yearsof Silent sudo Passwords

Starting with the upcoming LTS release, every keystroke at asudopassword prompt
 will echo an asterisk — a small UX fix that has ignited one of Linux’s fiercest debates in years.

LO

Linux Observer Staff

 Published March 19, 2026  ·  6 min read


Ubuntu 26.04

sudo-rs

Rust

For more than four decades, typing a password after asudoprompt
 in a Linux terminal produced nothing visible on screen — no asterisks, no dots, no moving cursor.
 The blank void was intentional: a guard against “shoulder surfing,” the practice of counting
 keystrokes to guess a password’s length. Ubuntu 26.04 LTS, codenamedResolute Raccoonand due on April 23, 2026, changes that.

“Security is theoretically worse since password lengths are exposed to people watching your screen, but this is an infinitesimal benefit far outweighed by the UX issue.”

— sudo-rs upstream commit message, enabling
pwfeedback
 by default

user@ubuntu — bash

# Ubuntu ≤ 25.04 — old behaviour (no feedback)

before
user@ubuntu:~$

sudo apt update

[sudo] password for user:

█ ← cursor blinks; nothing shown

# Ubuntu 26.04 — new behaviour (asterisks per character)

after
user@ubuntu:~$

sudo apt update

[sudo] password for user:

********

← one ✱ per keystroke

## A History Written in Silence

The originalsudoutility
 was created in 1980 by Bob Coggeshall and Cliff Spencer at the State University of New York at Buffalo.
 Its silent password prompt was a deliberate security decision from an era when terminals were shared,
 physical screens were wide-open, and the threat model squarely included people standing behind you counting keystrokes.
 That behaviour survived — untouched — through nearly half a century of Linux distributions.

The tradition began to crack when Linux Mint enabled visual password feedback by default for its own
 sudo configuration, quietly demonstrating that the sky would not fall. Still, mainstream distributions,
 Ubuntu among them, maintained the classic silent prompt.

## Enter sudo-rs: Rust Rewrites the Rules

The catalyst for Ubuntu’s change issudo-rs, a ground-up rewrite of the classic C
 implementation in the Rust programming language. Canonical shipped sudo-rs as the defaultsudoimplementation beginning
 withUbuntu 25.10— a transition that most users never noticed because the command
 name and behaviour were otherwise identical.

Then, roughly two weeks before the Ubuntu 26.04 beta window, the upstream sudo-rs project
 merged a patch to enable thepwfeedbackoption by default. Canonical cherry-picked that patch into Ubuntu 26.04 development builds.
 The legacysudopackage (sometimes labelledsudo-ws) is unaffected; only the sudo-rs path shows asterisks.

1980

Original
sudo
 created at SUNY Buffalo. Silent password input is the default from day one.

Ubuntu 25.10 — October 2025

Canonical replaces the classic C-based sudo with
sudo-rs
 (Rust). Behaviour remains visually unchanged for users.

October 2025

A bug report filed against sudo-rs requests that
pwfeedback
 be enabled by default to “make sane modern UX decisions.”

February 2026

Upstream sudo-rs merges the
pwfeedback
 patch. Canonical cherry-picks it into Ubuntu 26.04 daily builds. Community debate erupts.

April 23, 2026

Ubuntu 26.04 LTS “Resolute Raccoon”
 ships to the public. Password asterisks become the default for millions of users.

## The Security Argument — Both Sides

Critics of the change point to a bug report whose title captures the sentiment perfectly:“sudo-rs echos * for every character typed breaking historical security measures older than I am.”Ubuntu acknowledged the report and marked itWon’t Fix. The upstream sudo-rs
 developers similarly declined to back down.

The developers’ counter-argument rests on two pillars. First, the security benefit of hiding
 password length is negligible in practice — anyone close enough to count asterisks on a screen
 is close enough to hear or watch your keystrokes directly. Second, and more pointedly, most users’sudopassword
 is the same as their login password — one that already appears as visible placeholder dots on the
 graphical login screen. Hiding asterisks in the terminal while showing them at login is, in the
 developers’ estimation, security theatre.

Aspect

Classic sudo (silent)

sudo-rs with pwfeedback

Visual feedback

None

One asterisk per character

Password length exposed

No

Yes (to shoulder snoopers)

Login-screen consistency

Inconsistent — dots shown at GDM

Consistent with graphical prompts

New-user experience

Confusing — appears frozen

Confirms input is registering

SSH session behaviour

Silent

Asterisks shown in SSH sessions too

Revertible?

—

Yes — one sudoers line

## How to Restore the Classic Behaviour

Users and system administrators who prefer the traditional silent prompt can restore it with a
 single configuration change. The setting is toggled via thesudoersfile, which should always be edited through the safevisudocommand to prevent
 syntax errors from locking you out.

### 🔧 Restore Silent Password Input

sudo visudo

Then add the following line to the sudoers file:

Defaults !pwfeedback

Save and close. The change takes effect immediately in new terminal sessions. No reboot required.

## The Broader Picture

The asterisk change is part of a wider modernisation underway in Ubuntu 26.04. The release
 will ship with GNOME 50 running exclusively on Wayland, Linux kernel 7.0, and further adoption of
 Rust-based core utilities — includinguutils/coreutils,
 a Rust reimplementation of the standard Unix command-line tools.
 The switch to sudo-rs is thus one piece of a broader effort to bring memory safety and, apparently,
 modern UX sensibilities to Ubuntu’s fundamental plumbing.

Whether you consider the asterisk change an overdue quality-of-life improvement or a dangerous
 departure from Unix philosophy, one thing is clear: the option to revert remains firmly in your
 hands. The developers have simply decided that the default should favour the many newcomers
 baffled by a blank prompt over the few veterans who cherished it.

Ubuntu 26.04 LTSResolute Raccoonis scheduled for final release on April 23, 2026.

### Windows Software Alternatives in Linux

Windows-Friendly Linux

Office

Email Client

Image Editing

Video Editing

PDF Editing

Project Management

Disk Encryption

Disclaimer of pbxscience.com

Tags:
Debian

Fedora

LInux

Mint

Oracle

Redhat

RHEL

SUSE

Ubuntu


## More Stories



* Games
* Latest News


### PS5 Firmware 12.00 Exploit: What’s Actually Happening?

 5 hours ago



* Latest News
* Linux
* Software


### Why Popular Manjaro Linux Distribution Is Facing a Crisis?

 5 hours ago



* Latest News
* Linux
* Software


### The Linux Desktop Fragmentation Problem and the Slow Road to Unity

 1 day ago
