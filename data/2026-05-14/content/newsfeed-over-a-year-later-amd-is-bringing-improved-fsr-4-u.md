---
title: Over a year later, AMD is bringing improved FSR 4 upscaling to its older GPUs - Ars Technica
url: https://arstechnica.com/gadgets/2026/05/amd-promises-to-bring-improved-hardware-backed-fsr-4-upscaling-to-older-radeon-gpus/
site_name: newsfeed
content_file: newsfeed-over-a-year-later-amd-is-bringing-improved-fsr-4-u
fetched_at: '2026-05-14T19:35:16.398617'
original_url: https://arstechnica.com/gadgets/2026/05/amd-promises-to-bring-improved-hardware-backed-fsr-4-upscaling-to-older-radeon-gpus/
date: '2026-05-14'
published_date: '2026-05-14T18:55:54+00:00'
description: FSR 4.1 running on RDNA3 or RDNA2 GPUs may take a bigger performance hit.
tags:
- ars-technica
- gaming
- tech
- amd
---

Text
 settings

When AMD announced version 4 of its FidelityFX Super Resolution (FSR) graphics upscaling technology early last year, it came with strings attached: The improved hardware-backed image quality would be available only on Radeon RX 9000-series GPUs based on the RDNA4 architecture, not on any older Radeon GPUs.

To date, AMD has released only a handful of 90-series graphics cards, including theRX 9070 XT, the RX 9070, the 8GB and 16GB versions of theRX 9060 XT, andan RX 9060that’s only available to PC companies rather than end users. That list notably doesn’t include any integrated GPUs, such as those found in AMD-powered thin-and-light laptops or gaming handhelds like the Steam Deck and its imitators.

Over a year later, AMD Computing and Graphics SVP Jack Huynh hasannouncedthat a version of FSR 4 is finally coming to older GPUs. The rollout will begin in July with RDNA3- and 3.5-based GPUs, which include the Radeon RX 7000 series, as well as integrated GPUs like the Radeon 890M and Radeon 8060S.

In “early 2027,” support will also be extended to the RDNA2 architecture, which includes the Radeon RX 6000 series, integrated GPUs like the Radeon 680M, and the Steam Deck’s GPU. This would also open the door to supporting FSR 4 on the PlayStation 5 and Xbox Series X and S, all of which also use RDNA2-based GPUs.

## Performance may take a hit

 Getting hardware-backed FSR running on older Radeon GPUs meant making it work with the INT8 hardware in those chips, rather than the FP8 data format that RDNA4 supports.
 

 Credit:
 AMD
 

 Getting hardware-backed FSR running on older Radeon GPUs meant making it work with the INT8 hardware in those chips, rather than the FP8 data format that RDNA4 supports.

 

 Credit:

 
 AMD

 

Huynh’s short video presentation didn’t get into performance comparisons, but did mention that AMD had to work to get FSR 4’s superior hardware-backed upscaling working on its older graphics architectures. RDNA4 includes AI accelerators that support the FP8 data format in the hardware, and porting FSR 4 to older GPUs meant getting it running on the integer-based INT8 hardware in the RDNA3 and RDNA2-based GPUs.

This may mean that FSR 4.1 running on an RDNA3 or RDNA2-based GPU may come with a larger performance hit relative to RDNA4 cards, or that image quality may differ slightly. Modders havealready worked to get FSR4 working on INT8-supporting GPUs, and the older GPUs reportedly see a 10 to 20 percent performance hit relative to FSR 3.1 running on the same hardware. AMD’s official implementation may or may not improve on these numbers.

Regardless, it’s nice to see AMD doing work to support owners of older GPUs, especially since it continues to sell many products that use the older RDNA3 and RDNA2 architectures. Some of the company’s recent driver releases haveimpliedthat the company was doing less work to support older graphics architectures; the FSR 4.1 announcement should put some of those fears to rest, even though it’s coming later than some owners of those older GPUs might have preferred.

Any games that support FSR 4 should be able to support FSR 4.1 running on Radeon 7000-series cards; users will presumably be able to install a driver update in July that enables the new feature. Games that support the older FSR 3.1 can also be forced to use FSR 4 in the Radeon graphics driver.

AMD’s FSR competes primarily with Nvidia’s Deep Learning Super Sampling (DLSS) upscaling technology, which tends to be more widely supported in games and deliver better results (partly because it has always been hardware-accelerated, something FSR only started doing in version 4). Part of the appeal of previous FSR versions is that they worked on pretty much any reasonably modern GPU hardware, including Intel’s integrated graphics and old GeForce GPUs that didn’t support DLSS. FSR 4.1 still won’t be as widely compatible as older versions were, even with the expanded hardware support.

 Andrew Cunningham
 

Senior Technology Reporter

 Andrew Cunningham
 

Senior Technology Reporter

 Andrew is a Senior Technology Reporter at Ars Technica, with a focus on consumer tech including computer hardware and in-depth reviews of operating systems like Windows and macOS. Andrew lives in Philadelphia and co-hosts a weekly book podcast called 
Overdue
.
 

1. 1.Twin brothers wipe 96 gov't databases minutes after being fired
2. 2.Altman forced to confront claims at OpenAI trial that he's a prolific liar
3. 3.Solar drone with jumbo jet wingspan broke a flight record—then it crashed
4. 4.Desperate Trump taps "Tim Apple," Jensen Huang, Elon Musk to attend Xi summit
5. 5.AI invades Princeton, where 30% of students cheat—but peers won't snitch

Customize