---
title: Using Claude Code to modernize a 25-year-old kernel driver – Dmitry Brant
url: https://dmitrybrant.com/2025/09/07/using-claude-code-to-modernize-a-25-year-old-kernel-driver
site_name: hackernews_api
fetched_at: '2025-09-08T11:05:58.689164'
original_url: https://dmitrybrant.com/2025/09/07/using-claude-code-to-modernize-a-25-year-old-kernel-driver
author: dmitrybrant
date: '2025-09-07'
description: Using Claude Code to modernize a 25-year-old kernel driver
tags:
- hackernews
- trending
---

As a bit of background, one of my hobbies is helping people recover data from old tape cartridges, such as QIC-80 tapes, which were a rather popular backup medium in the 1990s among individuals, small businesses, BBS operators, and the like. I have a soft spot for tape media; there’s something about the tactile sensation of holding these tapes in my hands that makes the whole process very joyful, even thoughQICtapes are notorious for their many design flaws. With some careful inspection and reconditioning, the data on these tapes is still totally recoverable, even after all these years.

Whenever I receive a QIC-80 tape for recovery, I power up one of my older PC workstations which has the appropriate tape drive attached to it, and boot into a veryold versionof Linux (namely CentOS 3.5), because this is the only way to use theftapedriver, which is the kernel driver necessary for communicating with this tape drive, allowing the user to dump the binary contents of the tape.

You see, the drive that reads these tapes connects to thefloppy controlleron the motherboard. This clever hack was done as a cost-saving measure: instead of having to purchase a separate SCSI adapter (the standard interface for higher-tier tape media), you can just connect this tape drive to your floppy controller, which was already available on most PCs. It can even work alongside your existing floppy drive, on the same ribbon cable! The tradeoff, of course, is that the data rate is limited by the speed of the floppy controller, which was something like 500 Kbps (that’s kilobits, not bytes).

The other downside is that the protocol for communicating with these tape drives through the floppy controller was very messy, nonstandard, and not very well-supported. It was a “hack” in every sense: your motherboard’s BIOS had no knowledge of the tape drive being connected, and it was entirely up to the end-user software to know exactly how to manipulate the hardware I/O ports, timings, interrupts, etc. to trick the floppy controller into sending the appropriate commands to the tape drive.

There were a small number of proprietary tools for MS-DOS and Windows 3.x/9x for dealing with these drives, and only one open-source implementation for Linux, namelyftape. Of course it is possible to use those original DOS/Windows tools to read the tapes, but it’s actually onlyftapethat allows us to read the “raw” binary contents of the tape, regardless of which proprietary software originally wrote it, which is why I prefer it for dumping the contents and worrying afterwards about decoding the proprietary logical formatting, and then extracting the files from it.

The trouble is, theftapedriver hasn’t been supported since roughly the year 2000, and was soon removed from the Linux kernel for this reason. This is why I’ve needed to run a painfully old version of Linux anytime I have to work with one of these drives. It would be great ifftapeworked on a modern distro, with all the benefits and affordances that would provide.

***

So a couple of weeks ago, it occurred to me to make a simple request to Claude Code:

> This repository is a Linux kernel driver that communicates with legacy tape drives connected to the floppy
 controller (FDC) on the motherboard. Unfortunately, this driver hasn't been maintained for a long time, and
 can only compile under kernel version 2.4. I'd like to modernize this driver, allowing it to be built with
 the latest versions of the kernel.

● I'll help you modernize this Linux kernel driver for legacy tape drives. This is a significant task that
 will require updating the code to work with modern kernel APIs and conventions.

And after several iterations of “combobulating” and whatever else Claude claims to do, I suddenly had a kernel driver that was compiling without errors. This is because Claude is able to take the compiler output and feed it back into itself, until the compilation works correctly. There was a laundry list of kernel functions and structures that were understandably deprecated or replaced, in the eternity that elapsed between kernel version 2.4 and version 6.8. Amazingly, Claude found all the outdated bits and replaced them with the correct modern equivalents, requiring just a few manual touch-ups of the code (a bit more on this later).

At this point, however, the kernel driver was still expected to be compiled as part of a full kernel tree, whereas I just wanted it to become a standalone loadable kernel module. OK, no problem:

> Is there a way to compile just this module in-place, instead of copying it into a kernel source tree?

● Yes! You can compile kernel modules out-of-tree without copying them into the kernel source. Let me create
 a proper standalone build system for the ftape driver.

…And it did. Without any further prompting. At the end of this stage, I had a loadable kernel module (.ko) that I could start trying to use with actual live hardware. Unsurprisingly, the module did not yet “work” — it was loading, but something was preventing it from communicating with the tape drive correctly. But I pressed on.

From this point forward, since loading/unloading kernel modules requires sudo, I could no longer let Claude “iterate” on such sensitive operations by itself. Luckily, theftapedriver was already generously sprinkled with logging messages (printk()calls that are printed todmesg), so I loaded the module myself, and iteratively pasted the output ofdmesginto Claude manually, and let Claude compare it to a “known-good” dmesg log that I’d previously saved from a successful tape read. After a few iterations of this, Claude identified the remaining issues preventing the module from communicating with the hardware.

● Perfect! The module has parameters that can be set. The issue is that without configuration, all the base
 addresses default to -1, which gets converted to 0xffff in the config function, causing the detection to fail.
● The "No such device or address" (ENXIO) error occurs because the ftape-internal module is not configured
 with the correct I/O port base address for your floppy controller.
 The issue is in fdc-internal.c:735-737: if fdc->sra == 0xffff, it returns -ENXIO. Since no configuration was
 provided, all values default to -1, which becomes 0xffff....

And at last, I had a kernel module that was able to a) load, b) detect the tape drive, and c) dump the contents of a test tape!

***

Using theftapedriver on a modern kernel, a feat that I thought was hopelessly out of reach, wassuddenly completedover the course of two evenings.

As a giant caveat, I should note that I have a small bit of prior experience working with kernel modules, and a good amount of experience with C in general, so I don’t want to overstate Claude’s success in this scenario. As in, it wasn’tliterallythree prompts to get Claude to poop out a working kernel module, but rather several back-and-forth conversations and, yes, several manual fixups of the code. It wouldabsolutely notbe possible to perform this modernization without a baseline knowledge of the internals of a kernel module.

This led me to crystallize some thoughts on working with such coding agents in our current moment:

#### Open yourself up to a genuine collaboration with these tools.

Interacting with Claude Code felt like an actual collaboration with a fellow engineer. People like to compare it to working with a “junior” engineer, and I think that’s broadly accurate: it will do whatever you tell it to do, it’s eager to please, it’s overconfident, it’s quick to apologize and praise you for being “absolutely right” when you point out a mistake it made, and so on. Because of this, you (the human) are still the one who must provide the guardrails, make product decisions, enforce architectural guidelines, and spot potential problems as early as possible.

#### Be as specific as possible, making sure to use the domain-specific keywords for the task.

I’m not claiming to suddenly be an expert in prompt engineering, but the prompts that I’ve found to be most successful are ones that clearly lay out the verbal scaffolding for a feature, and then describe the gaps in the scaffolding that the LLM should fill in. (For some reason the image that comes to mind is one of those biological stem-cell scaffolds where an artificial human ear will grow.)

#### Develop an intuition for the kinds of tasks that are “well-suited” for an agent to complete.

These agents are not magical, and can’t do literally everything you ask. If you ask it to do something for which it’s not well-suited, you will become frustrated and prematurely reject these tools before you allow them to shine. On this point, it’s useful to learn how LLMs actually work, so that you develop a sense of their strengths andweaknesses.

#### Use these tools as a massive force multiplier of your own skills.

I’m sure that if I really wanted to, I could have done this modernization effort on my own. But that would have required me to learn kernel developmentas it was done 25 years ago. This would have probably taken me several weeks of nonstop poring over documentation that would becompletely useless knowledgetoday. Instead of all that, I spent a couple of days chatting with an agent and having it explain to me all the things it did.

Naturally, I verified and tested the changes it made, and in the process I did end up learning a huge amount of things that will beactually usefulto me in the future, such as modern kernel conventions, some interesting details of x86 architecture, as well as several command line incantations that I’ll be keeping in my arsenal.

#### Use these tools for rapid onboarding onto new frameworks.

I am not a kernel developer by any stretch, but this particular experience ignited a spark that might lead to more kernel-level work, and it turns out that kernel development isn’t nearly as difficult as it might sound. In another unrelated “vibe-coding” session, I built a Flutter app without having used Flutter before. If you’re like me, and your learning style is to learn by doing, these tools can radically accelerate your pace of learning new frameworks, freeing you up to do more high-level architectural thinking.

***

In any case, circling all the way back, I am now happy to say thatftapelives on! Twenty-five years after its last official release, it is once again buildable and usable on modern Linux. I’m still in the process of making some further tweaks and new feature additions, but I have already verified that it works with the floppy-based tape drives inmy collection, as well as parallel-port-based drives which it also supports.

The physical setup looks very similar, but the OS is now Xubuntu 24.04, instead of CentOS 3.5! 🎉Until next time!

Share:
Twitter
Facebook
Pin It
WhatsApp
LinkedIn
Buffer
