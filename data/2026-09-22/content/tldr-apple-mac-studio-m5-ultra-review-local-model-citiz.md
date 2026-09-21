---
title: 'Apple Mac Studio (M5 Ultra) review: Local model citizen outpaces DGX Spark and Threadripper | Tom''s Hardware'
url: https://www.tomshardware.com/desktops/mini-pcs/apple-mac-studio-m5-ultra-review
site_name: tldr
content_file: tldr-apple-mac-studio-m5-ultra-review-local-model-citiz
fetched_at: '2026-09-22T08:46:34.656874'
original_url: https://www.tomshardware.com/desktops/mini-pcs/apple-mac-studio-m5-ultra-review
date: '2026-09-22'
published_date: '2026-09-21T13:00:00Z'
description: Taking on the Mac Pro's mantle
tags:
- tldr
---

### Tom's Hardware Verdict

 

 

 

 

The Mac Studio with M5 Ultra is a small powerhouse PC with strong performance, fast memory throughput, and the ability to run AI models locally (if that's your thing).

#### Pros

* +M5 Ultra delivers powerful performance
* +1.2 TB/s memory throughput is excellent for local AI models
* +Small, quiet design
* +Plenty of ports

#### Cons

* -Pricey memory and SSD upgrades
* -Not upgradeable after purchase

Why you can trust Tom's HardwareOur expert reviewers spend hours testing and comparing products and services so you can choose the best for you.Find out more about how we test.

Earlier this year, Applediscontinued the Mac Pro, leaving the Mac Studio as its top-end desktop. With the new M5 Ultra chip, Apple's relatively diminutive system is more than ready to take on the mantle.

While you might not have a ton of PCIe connections and both RAM and storage are set, the Studio offers a ton of ports for accessories, monitors, and peripherals, memory options up to 256GB (with 512GB coming later), and a clean, quiet design.

Starting with an M5 Max at $2,499, the Mac Studio could be poised as a creator system for video editors, photographers, or game designers. At $12,299 as tested with the top-end M5 Ultra, 256GB of unified memory, and 4TB of storage, it effectively becomes an enterprise device, possibly a remote server, that could handle any task with aplomb, including local AI.

Latest Videos From
Tom's Hardware
Watch full video here: 

## Design of the Mac Studio (2026)

Apple hasn't made any changes to the Mac Studio's design. It's a silver, squared-off block that's 7.7 x 7.7 inches on your desk that stands 3.7 inches tall. The aluminum chassis has a shiny Apple logo on the top. The M5 Ultra version we tested weighs 8 pounds, a 2-pound increase over the M5 Max variant. This is largely because the M5 Max version uses a cooler with a thin aluminum stack and a copper heat pipe, while the M5 Ultra uses a heavier copper fin stack and a copper vapor chamber.

Image 1 of 2

(Image credit: Tom's Hardware)

(Image credit: Tom's Hardware)

Image 1 of 2

View Original

Image 2 of 2

View Original

The back of the system is also home to the power button, as well as a bunch of air holes for exhausting heat.

 

(Image credit: Tom's Hardware)

The air comes in through more holes in a small stand built into the bottom of the system. (There's also a Kensington lock slot, though its placement on the bottom necessitates a special adapter.)

 

(Image credit: Tom's Hardware)

## Mac Studio (2026) Specifications

Swipe to scroll horizontally

Processor

 

Apple M5 Ultra (36-core CPU)

 

Graphics

 

80-core GPU (integrated)

 

Memory

 

256GB LPDDR5 unified memory

 

Storage

 

4TB SSD

 

Networking

 

Apple N1, Wi-Fi 7, Bluetooth 6, Thread

 

Front Ports

 

2x Thunderbolt 5 (USB-C), SD card reader (UHS-II)

 

Rear Ports

 

4x Thunderbolt 5 (USB-C), 2x USB-A, HDMI 2.1, 10Gb Ethernet, 3.5 mm headphone jack

 

Power Supply

 

480W maximum continuous power

 

Operating System

 

macOS 27.0 Golden Gate

 

Dimensions (WxDxH)

 

7.7 x 7.7 x 3.7 inches (9.5 x 19.7 x 19.7 mm)

 

Price as Configured

 

$12,299.00

 

## Ports and Upgradeability on the Mac Studio (2026)

On the front, there are two Thunderbolt 5 (USB Type-C) ports along with an SDXC card slot. The rest of the ports are on the rear, including another four Thunderbolt 5 ports, two USB Type-A ports, HDMI 2.1, a 10Gb Ethernet jack, and a 3.5 mm headphone jack.

Stay On the Cutting Edge: Get the Tom's Hardware Newsletter

Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.

Contact me with news and offers from other Future brands
Receive email from us on behalf of our trusted partners or sponsors

There is no upgrading the Mac Studio. The RAM is soldered to the board, so be sure to get what you need when you're first buying the system, and Apple doesn't sell replacement SSDs (Some third parties may sell reverse-engineered NAND, but it will certainly void your warranty, and Apple doesn't support it. You're best off usingexternal storage)

## M5 Ultra

If you pony up for the most expensive Mac Studio configurations, you'll get Apple's most powerful chip. This is the only machine that Apple currently puts that chip inside.

M5 Ultra is Apple's first quad-die chip, connecting a pair of dual-die M5 Max SOCs over its UltraFusion connection. Apple claims that UltraFusion increases bandwidth between the dies to over 4.4 TB/s. Memory bandwidth is up to 1.2TB/s, which lets users store and run huge LLMs entirely on device.

Each of the 80 GPU cores features a neural accelerator, and there's a 32-core neural engine. There's now a media engine with hardware-enabled H.264, HEVC, hardware-accelerated AV1 decode, and four ProRes encode and decode engines.

Cinebench estimates that the M5 Ultra runs single-core at 4.6 GHz and multi-core at 4.3 GHz.

## Productivity Performance on the Mac Studio

The Mac Studio is an absolute workhorse. The system stayed largely quiet (though the fan can make itself known) as it powered through ourbenchmarks. Anything you might want to do on a Mac, you can do on this one.

In fact, while we ran our basic desktop suite on this, we also ran some extra tests, as we don't test many workstations. Instead of pitting this system against other desktops, we pitted it against other workstations to get a better idea of how the M5 Ultra performs. While that's a bit antithetical to the way Apple designs its products (it doesn't sell chips separately; it designs them as part of its computers), it does give us a reference point to the chips powering the Windows and Linux workstations.

 

(Image credit: Tom's Hardware)

On Geekbench 7, the Mac Studio was the clear winner, with the ARM-based chip leading the pack in the bursty workload with a single-core score of 3,770 and a multi-core score of 52,293, despite having fewer cores than the competitors.

 

(Image credit: Tom's Hardware)

The Mac continued its lead on Handbrake, transcoding a 4K video to 1080p in 1 minute and 4 seconds. The next closest, the AMD Ryzen Threadripper 9980X, took 8 seconds longer.

 

(Image credit: Tom's Hardware)

On Blender's benchmark testing CPU-based rendering, the Studio with M5 Ultra fell behind the previous- and current-gen Threadrippers (7980X and 9980X, each with 64-cores), as well as the 56-core Intel Xeon w-3495X.

 

(Image credit: Tom's Hardware)

The Mac Studio with M5 Ultra copied 25GB of files at a rate of 2,983.08 MBps, surpassing the speeds of the M3 Ultra and M4 Max from the last generation.

 

(Image credit: Tom's Hardware)

The Mac Studio was consistent over our 10-run Cinebench 2026 stress test. Its lowest score, 17,825, was actually the first run. When the cooling kicked in, the rest of the results were slightly higher. The sixth run was the highest at 18,069, but it was so similar to the other runs that it's within the margin of error.

During the test, the CPU measured an average of 78.29 degrees Celsius.

## Local AI on the Mac Studio (2026)

The M5 Ultra's GPU cores feature neural accelerators, granting it some extra matrix math horsepower, and Apple has boosted the chip's memory bandwidth to 1.2 TB/s, double that of theM4 Max we previously tested for AI.

The M5 Ultra's prompt processing speeds are even faster than Nvidia's DGX Spark's, and its tokens-per-second throughput is double that of the M4 Max and almost four times higher than the DGX Spark across the board.

 

(Image credit: Tom's Hardware)

Our tests, here using Qwen 3.8-27B-Q4_K_M, a dense model that relies heavily on memory bandwidth, are largely aimed at GPU performance in isolation. But combined with the blazing-fast single- and multi-threaded performance of the 36-core CPU, the Mac Studio with M5 Ultra looks to be ready for anything one might want to do with local or agentic AI workloads — and that's before someone tries to put it into an MLX cluster.

 

(Image credit: Tom's Hardware)

In addition to its raw performance, our M5 Ultra sample's 256GB of memory means you can fit very large, intelligent single models or a range of different models onto a single node. I spent time running models far larger than our tests with Hermes and LM Studio with strong performance. If you are interested in local AI, this will definitely do the job.

## Gaming and Graphics on the Mac Studio (2026)

While the M5 Ultra and its 80-core GPU are more than capable of gaming, the Mac Studio isn't a gaming-first rig. For the price, systems with Nvidia's high-end graphics cards are far more competitive.

To stress the Mac Studio, I booted up InZoi, a life simulator that isn't graphically imposing but is hard on the CPU and memory. I set both the simulation performance and graphics to ultra settings, and set the game to 1080p, but allowed for upscaling with MetalFX's Performance mode, which upscaled from 960 x 540. The game ran between 45 and 65 frames per second, dropping to the lower end in outdoor environments with lots of other characters.

To compare more graphically demanding games, I picked out a few gaming PCs we've tested in the last year and pitted them against each other with the data from theCyberpunk 2077benchmark with the Ray Tracing Ultra preset, which we use for those kinds of rigs.

 

(Image credit: Tom's Hardware)

At 1080p, the Mac Studio ran the game at 66 FPS, falling behind systems like the HP Omen Max 45L and Maingear MG-1 with Nvidia's top-end GeForce RTX 5090. It was much more in line with the Acer Nitro 65, with an RTX 5070. At 4K, the Mac Studio didn't reach playable levels, though the RTX 5090 systems both reached 59 FPS.UsingCyberpunk's "For This Mac" preset set the resolution to 1440p, turned off ray tracing, and mostly stuck to high settings and effects options.

 

(Image credit: Tom's Hardware)

On 3DMark's Steel Nomad graphics test, the Mac Studio still fell far behind the RTX 5090 system, but outperformed the RTX 5070-based Acer desktop.

## Software and Warranty on the Mac Studio (2026)

The Mac Studio comes with macOS 27 Golden Gate. This is a great update over macOS 26 Tahoe, refining the Liquid Glass aesthetic and making it more customizable (I actually kind of like it in this iteration), and yes, thank heavens, consistent window shapes. It also adds the new Siri AI (be sure to get on the waitlist). The new Siri is far superior to the one you're used to.Golden Gate also adds AI throughout apps, including more photo features, including a better Clean up option and spatial reframing, which lets you move a camera after you take a picture (the latter is kind of surreal). Better indexing makes it easier to search messages, emails, and calendar entries, and now you can use natural language to create automations in the Shortcuts app or come up with your own Safari extensions.

There's no bloatware, as usual. Apple's software suite includes Safari, Messages, Photos, Maps, Notes, and Reminders. Its services, including News and Apple TV, also have applications. Pages, Keynote, and Numbers are still in the dock by default, but they're the Creator Studio subscription versions, which require a subscription to get full features, including AI functionality, royalty-free graphics, and additional templates.

People using the Mac Studio as a server running AI models may not need all of those programs. For the first time in a while, I found myself wishing for something akin to macOS Server, but for better remote monitoring. I would also like to see an option for a system of this class to come with pared-down built-in apps, perhaps limiting it to the browser, App Store, Terminal, Activity Monitor, and other essentials and letting system admins decide what else needs or deserves to be there. A video editor might want to use Messages on the side. But you don't need that for a cluster running a huge model.

Apple sells the Mac Studio with a one-year warranty. Further repairs and support can be added as part of AppleCare+ ($6.49 monthly or $64.99 annually), or as part of AppleCare One or AppleCare Family.

## Mac Studio (2026) Configurations

Our Mac Studio review configuration is clearly an enterprise machine. With the top-end M5 Ultra (36-core CPU, 80-core GPU), along with 256GB of RAM (currently the top-end option, with a 512GB configuration coming in late October), and a roomy 4TB SSD, it costs $12,299.00, but that's not stopping anyone: As of this writing, it's backordered between 16 and 18 weeks.

But there are a lot of steps below that. The base model is $2,499 with the M5 Max (18-core CPU, 32-core GPU), 36GB of memory, and 512GB of storage. There are two versions of each: the M5 Max and M5 Ultra. Going from a 32-core GPU to a 40-core GPU on the M5 Max costs $300.

The cheapest M5 Ultra system is $5,499 with a 30-core CPU and 64-core GPU, along with 96GB of memory and 1TB of SSD storage. Bumping up to the M5 Ultra we tested increases the price by $1,300. Moving from 96GB of RAM to 256GB adds $4,000. Bumping up from a 1TB SSD to 2TB is $500, while our 4TB SSD is a $1,500 increase.

The M5 Max configurations have slight port differences on the front of the desktop. The USB-C ports on those are 10Gb/s ports, while on the M5 Ultra, you get Thunderbolt 5 for up to 120Gb/s.

## Bottom Line

At $12,299, the Mac Studio with M5 Ultra is effectively an enterprise computer, capable of difficult workloads like rendering and running AI models that are as close to frontier-grade as you're going to get right now on edge computing.

 

(Image credit: Tom's Hardware)

Much of that price also comes from RAM and storage. Given the fact that you can't really upgrade this computer, businesses and people using this for their job may see the extra cost as an investment. Really, its biggest weakness is in gaming, for professionals who may want to do that on the side. Discrete GPUs still win there.Given the fact that an AMD Ryzen Threadripper 9980X, a 64-core monster that beats this CPU in Blender, is priced around $5,000 on its own before memory, storage, power supplies, or any other components, it may not actually be that crazy in this market, and the Mac Studio can be had in a much smaller case. (For wealthy homelabbers, businesses, and server farms, third-party accessory makers already make rack mounts to fit the Mac Studio; its shape hasn't changed since its last redesign).

For local AI, the M5 Ultra is seriously impressive, though that may still be a niche use case for some. But in a computer that can reach over $12,000, niche is the name of the game.This all makes the M5 Ultra version of the Mac Studio an impressive package and further proof of the power and performance Apple can draw out of its own silicon in concert with its own software.

TOPICS

Andrew E. Freedman

Senior Editor

Andrew E. Freedman is a senior editor at Tom's Hardware focusing on laptops, desktops and gaming. He also keeps up with the latest news. A lover of all things gaming and tech, his previous work has shown up in Tom's Guide, Laptop Mag, Kotaku, PCMag and Complex, among others. Follow him on Threads@FreedmanAEand BlueSky@andrewfreedman.net.You can send him tips on Signal: andrewfreedman.01