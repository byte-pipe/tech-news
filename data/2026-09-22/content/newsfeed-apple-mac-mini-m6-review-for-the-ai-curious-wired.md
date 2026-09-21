---
title: 'Apple Mac Mini (M6) Review: For the AI Curious | WIRED'
url: https://www.wired.com/review/apple-mac-mini-m6/
site_name: newsfeed
content_file: newsfeed-apple-mac-mini-m6-review-for-the-ai-curious-wired
fetched_at: '2026-09-22T08:46:47.688272'
original_url: https://www.wired.com/review/apple-mac-mini-m6/
author: Luke Larsen
date: '2026-09-21'
description: Apple has refreshed the Mac Mini with a brand-new chip, the M6. And this time, it’s more focused on AI than ever.
tags:
- wired
- gear
- gear / products
- gear / reviews
---

$899
 at Apple
Save Story
Save this story
Save Story
Save this story
Rating:

9/10

Open rating explainer
Information
WIRED
Unprecedented power in a tiny box. Impressive gaming for what it is. Big gains in some AI performance. Good port selection with support for dual 5K monitors.
TIRED
More expensive starting point. No SD card slot. 16 GB isn't enough for agentic AI.

The Mac Minihas gone through a Peter Parker-esque transformation this year. Just six months ago, it was a meek, unassuming little Mac starter kit, content to fulfill the role of being Apple's smallest and most affordable Mac. It was so easy to overlook that Apple even skipped its M5 refresh last year.

But at the beginning of 2026, the world was flooded with agentic AI frameworks like Claude Cowork,OpenClaw, and Perplexity Computer. Suddenly, the Mac Mini became a hot commodity for running AI models. Before long, it was completely sold out and hard to find for most of the year. EvenApple was caught off guard.

And now, it's back. Powered by the M6 chip and a newfound sense of importance, the Mac Mini is owning its heroic identity—and crushing the competition.

## An Old Friend

The M6 Mac Mini isn't designed to be flashy. It's meant to blend into your desk's workspace, maybe even hidden behind your monitor or in a closet. That's not necessarily because it's ugly or poorly made, though. The chassis was redesigned for the2024 M4 release, adopting a boxier look and overall smaller form factor. It fits in your hand, with a footprint of just 5 x 5 inches. It's tiny and well crafted. Everything is inside, including the power supply—no huge power brick to have to find a spot for.

Photograph: Luke Larsen

Ports remain the same. Two forward-facingUSB-C 3 ports(up to 10 gigabytes per second), as well as a headphone jack and a power indicator light. On the back, there are three Thunderbolt 4 ports, HDMI 2.1, an Ethernet jack, and the power adapter port. Using the available USB-C ports and HDMI on the back, you canconnect up to two 5K 120-Hz external displays(such as the Studio Display XDR or BenQ 5K MA270S) or three 4K displays.

One controversial design is that the power button is still hidden underneath the back left corner of the computer. If you know where it is, just tilt the Mac Mini to the side and reach your finger back—easy. If you don't know (or keep forgetting, as I do), it means having to flip the thing over entirely, with all your cables attached. It remains a silly design decision in my view, but it's nowhere near as egregious as theMagic Mouseit pairs with (sold separately), which still infamously charges from the bottom. But I digress.

I still wish it had an SD card slot (forward-facing, like theMac Studio) though. Plenty of photographers and videographers would be well suited for the Mac Mini, and yet they'll need to buy an additional dock or adapter. And yes, some color options, like the iMac, would be nice. But from the outside, it's the same well-built, compact mini PC it's always been. It's the performance under the hood where you'll need to dig in to see the extra value in this latest generation.

## AI Gains

Right off the bat, I was eager to test a couple of new components in the M6 Mac Mini. First, there are the advances in the M6 chip itself. This is our first glimpse of the next generation of Apple Silicon, and the first built on a 2-nm process node. It represents a significant step up in transistor count on the die—46 billion in this case. That's around a 35 percent increase in transistor density, which translates to higher efficiency and more performance. In theory.

The M6 Mac Mini also adds two more CPU cores than the M4 model, for a total of 12. That's a 21 percent increase in single-thread performance and a 36 percent improvement in a multi-threaded run. Those numbers sound impressive, but compared to theM5 in the MacBook Air, they're not as substantial. It's only around 10 percent faster than the M5 Pro chip in the MacBook Pro in single-threaded performance (and unsurprisingly, much further behind in multi-threaded). Those two extra CPU cores, though, do prop up the multi-threaded performance, even compared to the base M5 chip. It's hard to do apples-to-apples comparisons to only a laptop.

Like previous Mac Minis, it has a fan inside. And when you get to work on something heavy, you'll definitely hear it start to make some noise. It's not terrible, but if you're coming from a MacBook, you'll definitely notice. That active cooling ensures you get stronger performance from that M6 chip than you would in a MacBook Air (though I won't be able to do a side-by-side comparison until the M6 MacBook Air comes out, presumably in 2027).

Photograph: Luke Larsen

Apple skipped the M5 generation for the Mac Mini, so this is the first time the Mac Mini gets the Neural Accelerators built into each GPU core. That means improved local AI inferencing, which brings me to the second thing I really wanted to try out. Despite the base model only having 16 GB of RAM, it took an average of 1 minute and 40 seconds to generate a 20-step image in Draw Things using the Flux.2 model on the M6 Mac Mini. This is a 9-billion-parameter AI model being run completely locally, without going to the cloud. My16-inch M4 Pro MacBook Prowith 48 GB of RAM was faster, however, generating this same image 20 seconds faster. Still, I was really impressed by the M6, and I chalk it up to the beefed-up GPU.

The M6 chip also includes a “dual” Neural Engine. Apple hasn't talked extensively about how exactly this works, but claims that it delivers twice the “peak compute” to speed up on-device AI workflows and that these frameworks can automatically access and use both Neural Engines at the same time. This will enhance all kinds of in-app features that creatives may appreciate, such as detecting edits in raw footage in Final Cut Pro. This can be done relatively seamlessly. It doesn't necessarily apply to running models on-device as a replacement for ChatGPT or Gemini. I tested out the same 70-billion-parameter Llama 2 model in LM Studio that I tested on previous Macs, but the application couldn't load it, saying it required 32 GB of memory to run well. I tried to load it anyway, which did, indeed, cause my system to freeze immediately.

Smaller models, however, run just fine on the M6 Mac Mini. I tried both a 16-billion-parameter Llama 3.2 model and a 9-billion Qwen3.5 model in LM Studio, and was really impressed by the speed. It's nowhere near as fast or as useful as acloud-based frontier model, but it's responsive enough to feel conversational. Just for fun, I also attempted a very basic agentic workflow in LM Bionic, giving it access to 15 local text files and asking for a detailed report using Qwen3.5, a 9-billion-parameter model. This proved to be a bit much. After a half-hour of running, the M6 Mac Mini still couldn't complete the task, while the M4 Pro MacBook Pro with 48 GB of RAM finished in 9 minutes and 43 seconds. Lack of memory is clearly the bottleneck here. No amount of Neural Engines can get around that.

Photograph: Luke Larsen

Beyond AI performance, though, I was also curious how the Mac Mini M6 functioned for gaming and content creation. The GPU performance really is impressive. It has 26 percent faster gaming inCyberpunk 2077than the M5 MacBook Pro, achieving a very playable 53 frames per second. With some light upscaling, I was able to get 82 frames per second. That's within a percent or two of Intel's latest X7 Panther Lake chip as tested in theDell XPS 14, a high-end laptop that costs well over $2,000. It certainly makes me excited about the gaming prowess of the next series of MacBooks.

Most Pro or Max chips from Apple in the past few years will surpass the GPU performance of the M6 Mac Mini. I have an M4 Pro MacBook Pro, and I was curious how the graphics stacked up. It was 15 percent faster in the 3DMark Steel Nomad Light gaming benchmark, which isn't as big a lead as I thought. While the M6 Mac Mini is far from a gaming PC, there's enough here to dabble—even in heavier games. This is especially significant since manyentry-level gaming laptopswith even an RTX 5050 cost at least $1,200 these days.

## Pricing Is Marketing

All that might have you wondering if the Mac Mini is right for you. It's not the AI powerhouse that some people desire, nor is it a super-affordable mini PC for your home office. It's somewhere in between.

Let's start with the latter group. You don't need to be AI-eager to get a lot of value out of the M6 Mac Mini—even at this price. If you want to run a workstation with multiple 4K or 5K monitors and need stellar performance that won't dip when you're multitasking and running complex software, the M6 Mac Mini is a home run. Most people will likely stick with a MacBook for the flexibility of working on the go, but the Mac Mini is more compact, more powerful, and much cheaper. And if you want to dabble in video editing, gaming, or local AI, the M6 Mac Mini has just enough performance to let you dip your toe in the water and be satisfied with the results.

And for those interested in running some at-home AI workflows, the Mac Mini with the M6 chip is a good starting place, especially if you upgrade to the 32-GB model for $1,299. That's a reasonable price for that much memory these days. To configure a MacBook Air with that much memory, for example, it would cost $1,699. Of course, you can also upgrade to the new M5 Pro Mac Mini, which is what you need if you want access to 48 GB or 64 GB of memory. The M5 Pro also has three more GPU cores and two more CPU cores than the M6.

Despite the price increase, the Mac Mini M6 isstilla good deal. It's theMac desktopthat most people should buy. Brand-new Windows- or Linux-based mini PCs start at hundreds of dollars more and lack some of the AI capabilities of the Mac Mini M6. Oftentimes, they're also larger. The upcomingNvidia RTX Spark mini PCscertainly look promising and may be the only serious challenger in the works, throwing tons of memory and GPU horsepower at AI workflows and games. But for now, those are more aimed at the higher-end M5 Pro Mac Mini and Mac Studio demographic. A 16-GB RTX Spark base configuration for less-demanding users may come in the future, but for now, the M6 Mac Mini rules the roost at this price.

$899
 at Apple

## Comments

Back to top
Join the discussion

## Comments

Back to top
Triangle
Luke Larsen
 is a product writer and reviewer at WIRED, covering laptops, PCs, Macs, monitors, and the wider PC peripheral ecosystem. He’s been reporting on tech for over a decade, previously at Digital Trends as the senior editor in computing, where he spent seven years leading the publication’s daily coverage. ... 
Read More
Product Writer & Reviewer

Topics
Shopping
Mac
Desktops
Computers
apple
Reviews
review
artificial intelligence