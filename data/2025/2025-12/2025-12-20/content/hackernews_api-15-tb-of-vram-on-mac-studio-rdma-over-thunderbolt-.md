---
title: 1.5 TB of VRAM on Mac Studio - RDMA over Thunderbolt 5 | Jeff Geerling
url: https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5
site_name: hackernews_api
fetched_at: '2025-12-20T11:06:43.354438'
original_url: https://www.jeffgeerling.com/blog/2025/15-tb-vram-on-mac-studio-rdma-over-thunderbolt-5
author: rbanffy
date: '2025-12-18'
description: 1.5 TB of VRAM on Mac Studio – RDMA over Thunderbolt 5
tags:
- hackernews
- trending
---

# 1.5 TB of VRAM on Mac Studio - RDMA over Thunderbolt 5

Apple gave me access to this Mac Studio cluster to test RDMA over Thunderbolt, anew feature in macOS 26.2. The easiest way to test it is withExo 1.0, an open source private AI clustering tool. RDMA lets the Macs all act like they have one giant pool of RAM, which speeds up things like massive AI models.

The stack of Macs I tested, with 1.5 TB of unified memory, costs just shy of $40,000, and if you're wondering, no I cannot justify spending that much money for this. Apple loaned the Mac Studios for testing. I also have to thank DeskPi for sending over the 4-post mini rack containing the cluster.

The last time I remember hearing anything interesting about Apple and HPC (High Performance Computing), was back in the early 2000s, when they still made theXserve.

They had a proprietary clustering solution called Xgrid... thatlanded with a thud. A few universities built some clusters, but it never really caught on, and now Xserve is a distant memory.

I'm not sure if its by accident or Apple's playing the long game, but the M3 Ultra Mac Studio hit a sweet spot for running local AI models. And with RDMA supportlowering memory access latency from 300μs down to < 50μs, clustering now adds to the performance, especially running huge models.

They also hold their own for creative apps and at least small-scale scientific computing, all while running under 250 watts and almost whisper-quiet.

The two Macs on the bottom have512 GBof unified memory and 32 CPU cores, and cost $11,699 each. The two on top, with half the RAM, are $8,099 each1.

They're not cheap.

But with Nvidia releasing theirDGX Sparkand AMD with theirAI Max+ 395systems, both of which have afourththe memory (128 GB maximum), I thought I'd put this cluster through its paces.

## Video

This blog post is the reformatted text version of my latest YouTube video, which you can watch below.

## A Mini Mac Rack

In a stroke of perfect timing, DeskPi sent over a new 4-post mini rack called theTL1the day before these Macs showed up.

I kicked offProject MINI RACKearlier this year, but the idea is you can have the benefits of rackmount gear, but in a form factor that'll fit on your desk, or tucked away in a corner.

Right now, I haven't seen any solutions for mounting Mac Studios in 10" racks besidesthis 3D printable enclosure, so I just put them on some 10" rack shelves.

The most annoying thing about rackinganynon-Pro Macs is the power button. On a Mac Studio it's located in the back left, on a rounded surface, which means rackmount solutions need to have a way to get to it.

The open sides on the mini rack allow me to reach in and press the power button, but I still have to hold onto the Mac Studio while doing so, to prevent it from sliding out the front!

Itisnice to have the front ports on the Studio to plug in a keyboard and monitor:

For power, I'm glad Apple uses an internal power supply. Too many 'small' PCs are small only because they punt the power supply into a giant brick outside the case. Not so, here, but youdohave to deal with Apple's non-C13 power cables (which means it's harder to find cables in the perfect length to reduce cabling to be managed).

The DGX Spark does better than Apple on networking. They have these big rectangle QSFP ports (pictured above). The plugs hold in better, while still being easy to plug in and pull out.

The Mac Studios have 10 Gbps Ethernet, but the high speed networking (something like 50-60 Gbps real-world throughput) on the Macs comes courtesy of Thunderbolt. Even withpremium Apple cablescosting $70 each, I don't feel like the mess of plugs would hold up for long in many environments.

There's tech calledThunderLok-A, which adds a little screw to each cable to hold it in, but I wasn't about to drill out and tap the loaner Mac Studios, to see if I could make them work.

Also, AFAICT, Thunderbolt 5 switches don't exist, so you can't plug in multiple Macs to one central switch—you have to plug every Mac into every other Mac, which adds to the cabling mess. Right now, you can only cross-connect up to four Macs, but I think that may not be a hard limit for the current Mac Studio (Apple said all five TB5 ports are RDMA-enabled).

The bigger question is: do you need a full cluster of Mac Studios at all? Because just one is already a beast, matchingfourmaxed-out DGX Sparks or AI Max+ 395 systems. Managing clusters can be painful.

## M3 Ultra Mac Studio - Baseline

To inform that decision, I ran some baseline benchmarks, and postedallmy results (much more than I highlight in this blog post) to mysbc-reviewsproject.

I'll compare the M3 Ultra Mac Studio to a:

* Dell Pro Max with GB10 (similar to the Nvidia DGX Spark, but with better thermals)
* Framework Desktop Mainboard (with AMD's AI Max+ 395 chip)

First, Geekbench. The M3 Ultra, running two-generations-old CPU cores, beats the other two in both single and multi-core performance (and even more handily in Geekbench 5, which is more suitable for CPUs with many cores).

Switching over to a double-precision FP64 test, my classictop500 HPL benchmark, the M3 Ultra is the first small desktop I've tested that breaks 1 Tflop FP64. It's almost double Nvidia's GB10, and the AMD AI Max chip is left in the dust.

Efficiency on the CPU is also great, though that's been the story with Apple since the A-series, with all their chips. And related to that, idle power draw on here is less than 10 watts:

I mean, I've seenSBC'sidle over 10 watts, much less something that could be considered a personal supercomputer.

Regarding AI Inference, the M3 Ultra stands out, both for small and large models:

Of course, thetrulymassive models (like DeepSeek R1 or Kimi K2 Thinking) won't even run on a single node of the other two systems.

But thisisa $10,000 system. You expect more when you pay more.

But consider this: a single M3 Ultra Mac Studio has more horsepower than myentireFramework Desktop cluster, usinghalfthe power. I also compared it to a tiny 2-node cluster of Dell Pro Max with GB10 systems, and a single M3 Ultra still comes ahead in performance and efficiency, with double the memory.

## Mini Stack, Maxi Mac

But with four Macs, how's clustering and remote management?

The biggest hurdle formeis macOS itself. I automateeverything I canon my Macs. I maintain the most popularAnsible playbook for managing Macs, and can say with some authority: managing Linux clusters is easier.

Every cluster has hurdles, but there are a bunch of small struggles when managing a cluster of Macs without additional tooling like MDM. For example: did you know there's no way to run a system upgrade (like to 26.2) via SSH? Youhaveto click buttons in the UI.

Instead of plugging a KVM into each Mac remotely, I used Screen Sharing (built into macOS) to connect to each Mac and complete certain operations via the GUI.

## HPL and Llama.cpp

With everything set up, I tested HPL over 2.5 Gigabit Ethernet, and llama.cpp over that and Thunderbolt 5.

For HPL, I got 1.3 Teraflops with a single M3 Ultra. With all four put together, I got 3.7, which is less than a 3x speedup. But keep in mind, the top two Studios only have half the RAM of the bottom two, so a 3x speedup is probably around what I'd expect.

I tried running HPL through Thunderbolt (not using RDMA, just TCP), but after a minute or so, both Macs I had configured in a cluster would crash and reboot. I looked into usingApple's MLX wrapper formpirun, but I couldn't get that done in time for this post.

Next I tested llama.cpp running AI models over 2.5 gigabit Ethernet versus Thunderbolt 5:

Thunderbolt definitely wins for latency, even if you're not using RDMA.

All my llama.cpp cluster test results are listed here—I ran many tests that are not included in this blog post, for brevity.

## Enabling RDMA

Exo 1.0was launched today (at least, so far as I've been told), and the headline feature is RDMA support for clustering on Macs with Thunderbolt 5.

ToenableRDMA, though, you have to boot into recovery mode and run a command:

1. Shut down the Mac Studio
2. Hold down the power button for 10 seconds (you'll see a boot menu appear)
3. Go into Options, then when the UI appears, open Terminal from the Utilities menu
4. Type inrdma_ctl enable, and press enter
5. Reboot the Mac Studio

Once that was done, I ran a bunch of HUGE models, including Kimi K2 Thinking, which at 600+ GB, is too big to run on a single Mac.

I can run models like that across multiple Macs using both llama.cpp and Exo, but the latter is so far the only one to support RDMA. Llama.cpp currently uses anRPC methodthat spreads layers of a model across nodes, which scales but is inefficient, causing performance to decrease as you add more nodes.

This benchmark of Qwen3 235B illustrates that well:

Exo speedsupas you add more nodes, hitting 32 tokens per second on the full cluster. That's definitely fast enough for vibe coding, if that's your thing, but it's not mine.

So I moved on to testing DeepSeek V3.1, a 671 billion parameter model:

I was a little surprised to see llama.cpp get a little speedup. Maybe the network overhead isn't so bad running on two nodes? I'm not sure.

Let's move to the biggest model I've personally run on anything, Kimi K2 Thinking:

This is a 1trillionparameter model, though there's only 32 billion 'active' at any given time—that's what the A is for in the A32B there.

But we're still getting around 30 tokens per second.

Working with some of these huge models, I can see how AI has some use, especially if it's under my own local control. But it'll be a long time before I put much trust in what I get out of it—I treat it like I do Wikipedia. Maybe good for a jumping-off point, but don'teverlet AI replace your ability to think critically!

But this post isn't about the merits of AI, it's about a Mac Studio Cluster, RDMA, and Exo.

They performed great...whenthey performed.

## Stability Issues

First a caveat: I was working withprereleasesoftware while testing. A lot of bugs were worked out in the course of testing.

But it was obvious RDMA over Thunderbolt is new. When it works, it works great. When it doesn't... well, let's just say I was glad I had Ansible set up so I could shut down and reboot the whole cluster quickly.

I also mentioned HPL crashing when I ran it over Thunderbolt. Even if I do get that working, I've only seen clusters of 4 Macs with RDMA (as of late 2025). Apple says all five Thunderbolt 5 ports are enabled for RDMA, though, so maybe more Macs could be added?

Besides that, I still have some underlying trust issues with Exo, since the developerswent AWOL for a while.

Theyarekeeping true to their open source roots, releasing Exo 1.0 under the Apache 2.0 license, but I wish they didn't have to hole up and develop it in secrecy; that's probably a side effect of working so closely with Apple.

I mean, it's their right, but as someone who maybe developstoomuch in the open, I dislike layers of secrecy around any open source project.

Iamexcited to see where it goes next. They teasedputting a DGX Spark in front of a Mac Studio clusterto speed up prompt processing... maybe they'll get support re-added for Raspberry Pi's, too? Who knows.

## Unanswered Questions / Topics to Explore Further

But I'm left with more questions:

* Where's the M5 Ultra? If Apple released one, it would bea lot fasterfor machine learning.
* Could Apple revive the Mac Pro to give me all the PCIe bandwidth I desire for faster clustering, without being held back by Thunderbolt?
* Could Macs getSMB Direct? Network file shares would behave as if attached directly to the Mac, which'd be amazing for video editing or other latency-sensitive, high-bandwidth applications.

Finally, what about other software?Llama.cppand other apps could get a speed boost with RDMA support, too.

## Conclusion

UnlikemostAI-related hardware, I'm kinda okay with Apple hyping this up. When the AI bubble goes bust, Mac Studios are still fast, silent, and capable workstations for creative work (I use an M4 Max at my desk!).

But it's not all rainbows and sunshine in Apple-land. Besides being more of a headache to manage Mac clusters, Thunderbolt 5 holds these things back from their true potential. QSFP would be better, but itwouldmake the machine less relevant for people who 'just want a computer'.

Maybe as a consolation prize, they could replace the Ethernet jack and one or two Thunderbolt ports on the back with QSFP? That way we could use network switches, and cluster more than four of these things at a time...

1. As configured. Apple put in 8 TB of SSD storage on the 512GB models, and 4TB on the 256GB models.↩︎

## Further reading

* I clustered four Framework Mainboards to test huge LLMs
* I regret building this $3000 Pi AI cluster
* LLMs accelerated with eGPU on a Raspberry Pi 5

apple

mac

mac studio

rdma

hpc

arm

thunderbolt

exo

networking

video

youtube

* Add new comment


## Comments

Thank you for the great post, Jeff. Has there been any indication they'll backport support for RDMA over TB to the older models?

It seems rather strange that Exo disappeared for a few months and has now come out with a totally new rewrite of the project (in some kind of backroom deal with Apple) that exclusively supports only the newest generation of Apple Silicon computers (M3/M4) while the older ones (M1/M2) are apparently left in the dust wrt RDMA.

I'm not trying to blow smoke or complain; there are a lot of people who took Alex Cheema, Awni Hannun, and Georgi Gerganov at their word when they pointed out that the M2 series is really great for inference. Georgi himself has an M2 Ultra 192GB; is he going to quietly trade it in for an M3 Ultra and eat a $7,000 loss because... Apple doesn't feel like issuing a microcode patch that enables RDMA on the M2? It all feels so fake.

It almost feels like this is a big marketing stunt by Apple to get the home computing hobbyist community to spend a few more $B on new Apple Silicon.

And of course, in the time between MLX/Exo coming out and the present, we completely lost all the main developers of Asahi Linux.

* Reply

I don't know anything that's happened behind closed doors, but I have seen many times when an AI startup that does something interesting/promising get gobbled up and just kinda disappear from the face of the planet.

At least this time Exo re-surfaced! I'm more interested in the HPC aspects, than LLM to be honest. It'd be neat to build a true beowulf cluster with RDMA of a Mac, an Nvidia node, an AMD server, etc. and see what kind of fun I could have :)

* Reply

Hey Andrej,What's your reasoning for saying M1/M2 is not supported, is the requirement TB5 specifically (in which case some of the M4 and M5 machines are not supported as well)? Didn't really find any source and I was hoping I can mix and match whatever M1 Max with M1 Pro and M4 and M3 Ultra to my liking, so to speak. If that's not the case then… it's disappointing.

Cheers

* Reply

Have you tried with thunderbolt 5 hosts with thunderbolt 4 hosts? I wanted to try this clustering for local LLM.

* Reply

I've been emailing with Deskpi about the TL1, do you know if it is able to fit 10"x10" rack like this one?https://www.printables.com/model/1176409-10-x10-minirack-now-with-micro…The rails looks slightly oddly shaped but it seems like it should work.Makes it way cheaper when getting a MOBO for your rack if you can fit a microATX instead of mini

It would make my current setup MUCH less janky

* Reply

No only up to like 8.75" I think... 220mm?

* Reply

did you know there's no way to run a system upgrade (like to 26.2) via SSH? You have to click buttons in the UI.

/usr/sbin/softwareupdatecan't do this? I don't have any pending updates to test with, but it looks like--install --os-only --restartshould suffice.

* Reply

A few people mentioned this — I had tried with the 26.0 update and it didn't seem to work. I may try again once 26.3 is out (I could maybe test on a beta...).

* Reply

I remember the Xserve days and VFX render clusters. But these days software update cli is deprecated as Apple pushes us all to MDM (DDM for software updates) but other ways to update existing for enterprise admins like Graham Pugh’s erase-install on github which leverages Nindi Gill’s mist-cli. A lot of crafty Mac Admins

* Reply

Just setting-up RDMA across 2 x M3 Ultra Studios (1024GB RAM)I got tons of models on local drive - most > 700GB - I don't want to download them again from Huggingface.

Is there a way to get EXO to use local model directory?

I have seen some comments -

from GitHub repo ...

How to use the downloaded local model #190

- but its all a bit cryptic

Since you have a "working system" - have you tried to see what is the "fix" (if at all) to use locally stored model?

I appreciate that the supported models / tokenises are baked into EXO at the moment - I am using same models - but they are LOCALY stored.

Any feedback / testing would be most welcome by those of us who have access to the expensive compute (the M3 Ultras)

Thanks

* Reply

Hi, thank you for the great article!I have a question: is it possible to measure the actual throughput of Thunderbolt 5 in RDMA mode?Specifically, can we monitor what the real transfer rate is when using RDMA over Thunderbolt 5, and if so, what tools or methods do you recommend to observe that actual throughput?

* Reply

Great work Jeff! I'm wondering what version of HPL are you using? It's a bit peculiar to see you didn't have results for HPL over RDMA -- would OpenMPI need to add support for this RDMA transport?Cheers, Pengcheng

* Reply

Jeff, great work as always, and thank you for your Ansible contributions; I use them nearly every day. Came here to comment that I feel your pain w.r.t. provisioning macOS hardware. One thing that has helped *tremendously* is using Claude Computer Use to automate the parts that cannot otherwise be automated through programmatic means, in particular OS reinstallations and the granting of sensitive permissions, e.g. screen recording and camera. Together w/ Ansible and MDM, it enables me to wipe and reprovision a mac end-to-end w/o any human intervention. Just thought I'd mention it here as it's genuinely useful in this scenario.

* Reply

Great blog post/video as always! Thank you :)

There is another open source clustering sofware available athttps://github.com/GradientHQ/parallaxWondering what differences between exo and that one. Also it looks like exo is not providing an OpenAI-compatible API, is it?

* Reply

Supposedly they are, but I have not tested it.

* Reply

The OpenAI-compatible API, is baked into the EXO software - just set-up the endpoints in your client (openWEBUI) and use the local EXO IP with port 8000 - it works well!

* Reply

What if you use thunderbolds for ethernet on AMD 385maxIt should be much faster

* Reply

So far I've only been able to get 9-10 Gbps on the 40 Gbps TB4 ports on the Max+ 395 boards from Framework. Still working on it though...

* Reply
