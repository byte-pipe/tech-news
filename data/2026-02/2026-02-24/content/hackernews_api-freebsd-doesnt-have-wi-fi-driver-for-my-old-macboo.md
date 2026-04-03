---
title: FreeBSD doesn't have Wi-Fi driver for my old MacBook. AI built one for me - Vladimir Varankin
url: https://vladimir.varank.in/notes/2026/02/freebsd-brcmfmac/
site_name: hackernews_api
content_file: hackernews_api-freebsd-doesnt-have-wi-fi-driver-for-my-old-macboo
fetched_at: '2026-02-24T11:19:58.341905'
original_url: https://vladimir.varank.in/notes/2026/02/freebsd-brcmfmac/
author: varankinv
date: '2026-02-23'
published_date: '2026-02-23T00:00:00+00:00'
description: FreeBSD doesn't have Wi-Fi driver for my old MacBook, so AI built one for me
tags:
- hackernews
- trending
---

My old 2016 MacBook Pro has been collecting dust in a cabinet for some time now. The laptop suffers from a“flexgate” problem, and I don’t have any practical use for it. For quite some time, I’ve been thinking about repurposing it as a guinea pig, to play with FreeBSD — an OS that I’d aspired to play with for a long while, but had never had a real reason to.

During the recent holiday season, right after FreeBSD 15 release, I’ve finally found time to set the laptop up. Doing that I didn’t plan, or even think, this may turn into a story about AI coding.

## Background

2016 MacBook Pro models use Broadcom BCM4350 Wi-Fi chip. FreeBSD doesn’t have native support for this chip. To have a working Wi-Fi, a typical suggestion on FreeBSD forums, is to run wifibox — a tiny Linux VM, with the PCI Wi-Fi device in pass through, that allows Linux to manage the device through its brcmfmac driver.

Brcmfmac is a Linux driver (ISC licence) for set of FullMAC chips from Broadcom. The driver offloads the processing jobs, like 802.11 frame movement, WPA encryption and decryption, etc, to the firmware, which is running inside the chip. Meanwhile, the driver and the OS do high-level management work (refBroadcom brcmfmac(PCIe) in Linux Wireless documentation).

Say we want to build a native FreeBSD kernel module for the BCM4350 chip. In theory, this separation of jobs between the firmware and the driver sounds perfect. The “management” part of work is what FreeBSD already does for other supported Wi-Fi devices. We need to port some amount of existing “glue code” from specifics of Linux to FreeBSD. If we ignore a lot of details, the problem doesn’t sound too complicated, right?

## Act 1

A level-zero idea, when one hears about “porting a bunch of existing code from A to B”, in 2026 is, of course, to use AI. So that was what I tried.

I cloned the brcmfmac subtree, and asked Claude Code to make it work for FreeBSD. FreeBSD already has drivers that work through LinuxKPI — compatibility layer for running Linux kernel drivers. So I specifically pointed Claude at the iwlwifi driver (a softmac driver for Intel wireless network card), asking “do as they did it”. And, at first, this even looked like this can work — Claude told me so.

https://bsky.app/profile/vladimir.varank.in/post/3mawf7xbdws2r

The module, indeed, compiled, but it didn’t do anything. Because, of course: the VM, where we tested the module, didn’t even have the hardware. After I set the PCI device into the VM, and attempted to load the driver against the chip, the challenges started to pop up immediately. The kernel paniced, and after Claude fixed the panics, it discovered that “module didn’t do anything”. Claude honestly tried to sift through the code, adding more and more#ifdef __FreeBSD__wrappers here and there. It complained about missing features in LinuxKPI. The module kept causing panics, and the agent kept building FreeBSD-specific shims and callbacks, while warning me that this project will be very complicated and messy.

## Act 2

After a number of sessions, the diff, produced by the agent, stared to look significantly larger than what I’d hoped it will be. Even worse, the driver didn’t look even close to be working. This was right around time when Armin Ronacher posted about his experiencebuilding a game from scratch with Claude Opus and PI agent.

Besides the part that working inPi coding agentfeels more productive, than in Claude Code, the video got me thinking that my approach to the task was too straightforward. The code of brcmfmac driver is moderately large. The driver supports several generations of Wi-Fi adaptors, different capabilities, etc. But my immediate task was very narrow: one chip, only PCI, only Wi-Fi client.

Instead of continuing with the code, I spawned a fresh Pi session, and asked the agent to write a detailed specification of how the brcmfmac driver works, with the focus on BCM4350 Wi-Fi chip. I explicitly set the audience for the specification to be readers, who are tasked with implementing the specification in a clean-room environment. I asked the agent to explain how things work “to the bits”. I added some high-level details for how I wanted the specification to be laid out, and let the agent go brrrr.

After a couple of rounds, the agent produced me a “book of 11 chapters”, that honestly looked like a fine specification

% ls --tree spec/
spec
├── 00-overview.md
├── 01-data-structures.md
├── 02-bus-layer.md
├── 03-protocol-layer.md
├── 04-firmware-interface.md
├── 05-event-handling.md
├── 06-cfg80211-operations.md
├── 07-initialization.md
├── 08-data-path.md
├── 09-firmware-commands.md
└── 10-structures-reference.md

Of course, one can’t just trust what AI has written.

To proofread the spec I spawned a clean Pi sessions, and — for fun — asked Codex model, to read the specification, and flag any places, where the text isn’t aligned with the driver’s code (“Source code is the ground truth. The spec needs to be verified, and updated with any missing or wrong details”). The agent followed through and found several places to fix, and also proposed multiple improvements.

Of course, one can’t just trust what AI has written, even if this was in a proofreading session.

To double-proofread the fixes I spawned another clean Pi sessions, asking Opus model to verify if what was proposed was aligned with how it works in the code of the driver.

As a procrastination exercise, I tried this loop with a couple of coding models: Opus 4.5, Opus 4.6, Codex 5.2, Gemini 3 Pro preview. So far my experience was that Gemini hallucinated the most. This was quite sad, given that the model itself isn’t too bad for simple coding tasks, and it is free for a limited use.

Having a written specification should have (in theory) explained how a driver’s code interacts with the firmware.

## Act 3

I started a fresh project, with nothing but the mentioned “spec”, and prompted the Pi agent, that we were building a brand new FreeBSD driver for BCM4350 chip. I pointed the agent to the specification, and asked it to ask me back about any important decisions we must make, and details we must outline, before jumping into “slopping the code”. The agent came back with questions and decision points, like “Will the driver live in the kernels source-tree?”, “Will we write the code in C?”, “Will we rely on LinuxKPI?”, “What are our high-level milestones?”, etc. One influential bit, that turned fairly productive moving forward, was that I asked the agent to document all these decision points in the project’s docs, and to explicitly referenced to these decision docs in the project’s AGENTS.md.

It’s worth saying that, just like in any real project, not all decisions stayed to the end. For example,

Initially I asked the agent to build the driver usinglinuxkpiandlinuxkpi_wlan. My naive thinking was that, given the spec was written after looking at Linux driver’s code, it might be simpler for the agent, than building the on top of the native primitives. After a couple of sessions, it didn’t look like this was the case. I asked the agent to drop LinuxKPI from the code, and to refactor everything. The agent did it in one go, and updated the decision document.

With specification, docs and a plan, the workflow process turned into a “boring routine”. The agent had SSH access to both the build host, and a testing VM, that had been running with the Wi-Fi PCI device passed from the host. It methodically crunched through the backlog of its own milestones, iterating over the code, building and testing the module. Every time a milestone or a portion was finished, I asked the agent to record the progress to the docs. Occasionally, an iteration of the code crashed or hanged the VM. When this happened, before fixing the problem, I asked — in a forked Pi’s session — to summarize, investigate and record the problem for agent’s future-self.

After many low-involved sessions, I got a working FreeBSD kernel module for the BCM4350 Wi-Fi chip. The module supports Wi-Fi network scanning, 2.4GHz/5GHz connectivity, WPA/WPA2 authentication.

https://bsky.app/profile/vladimir.varank.in/post/3mfhnvunnr22d

The source code is in repositorygithub.com/narqo/freebsd-brcmfmac. I didn’t write any piece of code there. There are several known issues, which I will task the agent to resolve, eventually. Meanwhile, I advise against using it for anything beyond a studying exercise.

Anexistentialdiscussion oneHacker News.

Ai
Apple
Arduino
Arm64
Askme
Aws
Berlin
Bookmarks
Brcmfmac
Buildkit
Cgo
Coffee
Continuous Profiling
COVID-19
Design
Docker
Dynamodb
E-Paper
English
Enum
Esp8266
Firefox
Freebsd
Github Actions
Go
Google
Graphql
Homelab
IPv6
K3s
Kubernetes
Linux
Macos
Material Design
MDNS
Music
Ndppd
Neondatabase
Objective-C
Passkeys
Postgresql
Pprof
Profefe
Random
Raspberry Pi
Rust
Travis Ci
Vs Code
Waveshare
Μ-Benchmarks
