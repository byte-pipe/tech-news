---
title: Helping Valve to Power Up Steam Devices | Igalia
url: https://www.igalia.com/2025/11/helpingvalve.html
site_name: hackernews_api
fetched_at: '2025-11-22T11:06:25.400406'
original_url: https://www.igalia.com/2025/11/helpingvalve.html
author: Igalia
date: '2025-11-21'
published_date: '2025-11-21T12:00:00+00:00'
description: Igalia is an open source consultancy specialised in the development of innovative projects and solutions. Our engineers have expertise in a wide range of technological areas, including browsers and client-side web technologies, graphics pipeline, compilers and virtual machines. We have the most WPE, WebKit, Chromium/Blink and Firefox expertise found in the consulting business, including many reviewers and committers. Igalia designs, develops, customises and optimises GNU/Linux-based solutions for companies across the globe. Our work and contributions are present in many projects such as GStreamer, Mesa 3D, WebKit, Chromium, etc.
tags:
- hackernews
- trending
---

##### "Igalia’s work has opened new possibilities in gaming"

Nov 21, 2025

Last week, Valve stunned the computer gaming world byunveiling three new gaming devices at once: the Steam Frame, a wireless VR headset; the Steam Machine, a gaming console in the vein of a PlayStation or Xbox; and the Steam Controller, a handheld game controller. Successors to the highly successfulValve IndexandSteam Deck, these devices are set to be released in the coming year.

Igalia has long worked with Valve on SteamOS, which will power the Machine and Frame, and is excited to be contributing to these new devices, particularly the Frame. The Frame, unlike the Machine or Deck which have x86 CPUs, runs on an ARM-based CPU.

Under normal circumstances, this would mean that only games compiled to run on ARM chips could be played on the Frame. In order to get around this barrier, a translation layer calledFEXis used to run applications compiled for x86 chips (which are used in nearly all gaming PCs) on ARM chips by translating the x86 machine code into ARM64 machine code.

“If you love video games, like I do, working on FEX with Valve is a dream come true,” saidPaulo Matos, an engineer with Igalia’sCompilers Team. Even so, the challenges can be daunting, because making sure the translation is working often requires manual QA rather than automated testing. “You have to start a game, sometimes the error shows up in the colors or sound, or how the game behaves when you break down the door in the second level. Just debugging this can take a while,” said Matos. “For optimization work I did early last year, I used a game calledPsychonautsto test it. I must have played the first 3 to 4 minutes of the game many, many times for debugging. Looking at my history, Steam tells me I played it for 29 hours, but it was always the first few minutes, nothing else.”

Beyond the CPU, the Qualcomm Adreno 750 GPU used in the Steam Frame introduced its own set of challenges when it came to running desktop games, and other complex workloads, on these devices. Doing so requires a rock-solid Vulkan driver that can ensure correctness, eliminating major rendering bugs, while maintaining high performance. This is a very difficult combination to achieve, and yet that’s exactly what we’ve done for Valve withMesa3DTurnip, a FOSS Vulkan driver for Qualcomm Adreno GPUs.

A sliding comparison of the main menu in the game “Monster Hunter World”, before and after fixing a rendering error

Before we started our work, critical optimizations such as LRZ (which you can learn more about fromour blog post here) or theautotuner(and its subsequentoverhaul) weren’t in place. Even worse, there wasn’t support for the Adreno 700-series GPUs at all, whichwe eventually addedalong with support fortiled rendering.

“We implemented many Vulkan extensions and reviewed numerous others,” saidDanylo Piliaiev, an engineer on theGraphics Team. “Over the years, we ensured that D3D11, D3D12, and OpenGL games rendered correctly through DXVK, vkd3d-proton, and Zink, investigating many rendering issues along the way. We achieved higher correctness than the proprietary driver and, in many cases, Mesa3D Turnip is faster as well.”

We’ve worked with many wonderful people from Valve, Google, and other companies to iterate on the Vulkan driver over the years in order to introduce new features, bug fixes, performance improvements, as well as debugging workflows. Some of those people decided to join Igalia later on, such as our colleague and Graphics Team developerEmma Anholt. “I’ve been working on Mesa for 22 years, and it’s great to have a home now where I can keep doing that work, across hardware projects, where the organization prioritizes the work experience of its developers and empowers them within the organization.”

Valve’s support in all this cannot be understated, either. Their choice to build their devices using open software like Mesa3D Turnip and FEX means they’re committed to working on and supporting improvements and optimizations that become available to anyone who uses the same open-source projects.

“We’ve received a lot of positive feedback about significantly improved performance and fewer rendering glitches from hobbyists who use these projects to run PC games on Android phones as a result of our work,” saidDhruv Mark Collins, another Graphics Team engineer working on Turnip. “And it goes both ways! We’ve caught a couple of nasty bugs because of that widespread testing, which really emphasizes why the FOSS model is beneficial for everyone involved.”

Automatically-measured performance improvement in Turnip since June 2025

An interesting area of graphics driver development is all the compiler work that is involved. Vulkan drivers such as Mesa3D Turnip need to process shader programs sent by the application to the GPU, and these programs govern how pixels in our screens are shaded or colored with geometry, textures, and lights while playing games.Job Noorman, an engineer from our Compilers Team, made significant contributions to the compiler used by Mesa3D Turnip. He also contributed to the Mesa3D NIR shader compiler, a common part that all Mesa drivers use, includingRADV(most popularly used on the Steam Deck) orV3DV(used on Raspberry Pi boards).

As is normal for Igalia, while we focused on delivering results for our customer, we also made our work as widely useful as possible. For example: “While our target throughout our work has been the Snapdragon 8 Gen 3 that’s in the Frame, much of our work extends back through years of Snapdragon hardware, and we regression test it to make sure it stays Vulkan conformant,” said Anholt. This means that Igalia’s work for the Frame has consistently passed Vulkan’s Conformance Test Suite (CTS) of over 2.8 million tests, some of which Igalia is involved in creating.

Our very own Vulkan CTS expertRicardo Garcíasays:

Igalia and other Valve contractors actively participate in several areas inside the Khronos Group, the organization maintaining and developing graphics API standards like Vulkan. We contribute specification fixes and feedback, and we are regularly involved in the development of many new Vulkan extensions. Some of these end up being critical for game developers, like mesh shading. Others ensure a smooth and efficient translation of other APIs like DirectX to Vulkan, or help take advantage of hardware features to ensure applications perform great across multiple platforms, both mobile like the Steam Frame or desktop like the Steam Machine. Having Vulkan CTS coverage for these new extensions is a critical step in the release process, helping make sure the specification is clear and drivers implement it correctly, and Igalia engineers have contributed millions of source code lines and tests since our collaboration with Valve started.

A huge challenge we faced in moving forward with development is ensuring that we didn’t introduce regressions, small innocent-seeming changes can completely break rendering on games in a way that even CTS might not catch. What automated testing could be done was often quite constrained, but Igalians found ways to push through the barriers. “I made a continuous integration test to automatically run single-frame captures of a wide range of games spanning D3D11, D3D9, D3D8, Vulkan, and OpenGL APIs,” said Piliaiev, about the development covered in hisrecent XDC 2025 talk, “ensuring that we don’t have rendering or performance regressions.”

Looking ahead, Igalia’s work for Valve will continue to deliver benefits to the wider Linux Gaming ecosystem. For example, the Steam Frame, as a battery-powered VR headset, needs to deliver high performance within a limited power budget. A way to address this is to create a more efficient task scheduler, which is somethingChangwoo Minof Igalia’sKernel Teamhas been working on. As he says, “I have been developing a customized CPU scheduler for gaming, namedLAVD: Latency-criticality Aware Virtual Deadline scheduler.”

In general terms, a scheduler automatically identifies critical tasks and dynamically boosts their deadlines to improve responsiveness. Most task schedulers don’t take energy consumption into account, but the Rust-based LAVD is different. “LAVD makes scheduling decisions considering each chip’s performance versus energy trade-offs. It measures and predicts the required computing power on the fly, then selects the best set of CPUs to meet that demand with minimal energy consumption,” said Min.

One of our other kernel engineers,Melissa Wen, has been working on AMD kernel display drivers to maintain good color management and HDR support for SteamOS across AMD hardware families, both for the Steam Deck and the Steam Machine. This is especially important with newer display hardware in the Steam Machine, which features some notable differences in color capabilities, aiming for more powerful and efficient color management which necessitated driver work.

…and that’s a wrap! We will continue our efforts toward improving future versions of SteamOS, and with a partner as strongly supportive as Valve, we expect to do more work to make Linux gaming even better. If any of that sounded interesting and you’d like to work with us to tackle tricky problems of your own,please get in touch!
