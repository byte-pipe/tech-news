---
title: Apple's new desktop computers are designed specifically for local AI development - Ars Technica
url: https://arstechnica.com/apple/2026/08/with-new-mac-studio-and-mac-mini-apple-leans-hard-into-local-ai-inference/
site_name: tldr
content_file: tldr-apples-new-desktop-computers-are-designed-specific
fetched_at: '2026-08-27T06:40:29.581581'
original_url: https://arstechnica.com/apple/2026/08/with-new-mac-studio-and-mac-mini-apple-leans-hard-into-local-ai-inference/
date: '2026-08-27'
published_date: '2026-08-25T13:00:11+00:00'
description: Folks have been daisy-chaining Macs for AI—this refresh keeps that in mind.
tags:
- tldr
---

Text
 settings

The Mac mini and Mac Studio occupy two distinct points in Apple’s lineup of desktops, but lately, they’ve had something in common: They’re popular for local AI inference and software development thanks to the advantages of their unified memory architecture and the fast CPUs and GPUs on their systems-on-a-chip.

Today, Apple announced new iterations of both desktops, along with two new chips: the M6, the first 2nm chip in Apple’s M-series lineup for Macs, and the M5 Ultra, now the most powerful chip in the lineup for most things—especially AI workloads.

There aren’t any major new features for either machine. This is just a specs bump. But based on how Apple is presenting these refreshes, they’re leaning hard into those use cases, which weren’t even a thought when earlier iterations were first engineered.

The devices’ popularity for production inference took off after macOS 26.2 shipped last December. According to Apple’srelease notes, 26.2 enabled “low-latency communication between Thunderbolt 5 hosts for use cases including distributed AI inference using MLX.” Thunderbolt 5 is a very fast wired data connection, and MLX is an open source array framework designed to help machine learning workflows take full advantage of the M-series chips’ unified memory.

Since then, both hobbyists and professional developers and researchers have been essentially daisy-chaining Mac minis or Mac Studios to run inference on local large language models that are much bigger than anything that could run a single mass-market device—providing an alternative to ultra-beefy specialized hardware featuring specialized Nvidia GPUs.

The story here is the chips themselves. The M6 is, as expected, a next-generation SoC (system-on-a-chip) meant for a wide range of consumer applications. It has a 12-core CPU, which includes two of what Apple calls “super cores,” alongside four performance cores and six efficiency cores. It’s the first Apple SoC to use all three core types. There aren’t any verifiable benchmarks to work from yet, but Apple claims it’s up to 40 percent faster at multi-threaded CPU performance compared to the M4 two generations ago.

It also has a 12-core GPU, which is two cores more than its immediate predecessors, and faster unified memory with up to 160GB per second of bandwidth. Memory capacity is limited to 32GB, though.

That’s where the new M5 Ultra—which will be available in the updated Mac Studio—comes in. Its maximum capacity is a whopping 512GB (for the fortunate few who can afford it). In many respects, it’s literally two M5 Maxes running side by side on one SoC, for 36 CPU cores (12 super, 24 performance) and 80 GPU cores. Apple claims it can achieve up to 1.2TB per second in terms of unified memory bandwidth.

Most people would never, ever need that, but that’s what we mean when we say that the AI inference use case is really what Apple is optimizing for here. That kind of memory and bandwidth is of course useful for other things, like gaming and other 3D graphics applications, but local inference is a growing use case, particularly for software developers.

Many developers have been changing their workflows toincorporateAI coding agents more heavily, thanks to powerful frontier large language models and increasingly sophisticated harnesses like Claude Code or Codex, but the cost ofrunning those cloud modelsis steep, and many are questioning whether it will remain practical.

Open-weight models that can be run locally, like some of the latest Qwen and DeepSeek models, can accomplish many of the same tasks but without charging a fortune for tokens, as they’re smaller and driven by the user’s own local energy and compute.

Still, most standard consumer hardware, like an average-spec MacBook Pro, is just far behind enough in terms of the size of models they can run that we’re not fully living in a “just run it all locally on your regular dev workstation” future just yet. That’s why some are tapping these chains of Mac minis or Mac Studios.

As noted, that’s the main story with these refreshes, but in other respects they’re standard upgrades for consumers who aren’t interested in all that. Both have Apple’s N1 chip, which supports Wi-Fi 7 and Bluetooth 6. Apple claims the storage is up to twice as fast, at 15GB/s. And this Mac mini ships with 2.5Gb Ethernet as standard, with the option to upgrade to 10Gb.

The Mac mini with M6 starts at $899 with 16GB of memory, and configurations with M5 Pro start at $1,699, while the Mac Studio with M5 Max starts at $2,499, and the M5 Ultra configurations start at $5,499. They can, of course, get a lot more expensive than that, depending on how you configure them.

Preorders for both start today, and they’re shipping on September 22 (though the 512GB memory config for the Studio won’t ship until late October). Apple also says they’ll ship with macOS 27 Golden Gate, suggesting that the annual OS update may arrive by then for other Mac users, too.

 Samuel Axon
 

Senior Editor

 Samuel Axon
 

Senior Editor

 Samuel Axon is the editorial lead for tech and gaming coverage at Ars Technica. He covers physical and generative AI, large language models, software development, gaming, entertainment, and mixed reality. He has been writing about gaming and technology for nearly two decades at Engadget, PC World, Mashable, Vice, Polygon, Wired, and others. He previously ran a marketing and PR agency in the gaming industry, led editorial for the TV network CBS, and worked on social media marketing strategy for Samsung Mobile at the creative agency SPCSHP. He also is an independent software and game developer for iOS, Windows, and other platforms, and he is a graduate of DePaul University, where he studied interactive media and software development.
 

1. 1.World humanoid robot games show runners breaking records, bursting into flames
2. 2.Apple's new desktop computers are designed specifically for local AI development
3. 3.Google's anti-nausea Motion Assist dots finally rolling out on Android
4. 4.SpaceX intends to invest up to $100 billion in massive Louisiana spaceport
5. 5.The world's busiest spaceport is about to get a lot quieter, at least for now

Customize