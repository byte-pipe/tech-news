---
title: RISC-V is sloooow – Marcin Juszkiewicz
url: https://marcin.juszkiewicz.com.pl/2026/03/10/risc-v-is-sloooow/
site_name: hnrss
content_file: hnrss-risc-v-is-sloooow-marcin-juszkiewicz
fetched_at: '2026-03-12T03:14:06.220296'
original_url: https://marcin.juszkiewicz.com.pl/2026/03/10/risc-v-is-sloooow/
date: '2026-03-10'
description: 143 vs 36 minutes is far too big difference
tags:
- hackernews
- hnrss
---

About 3 months agoI started working withRISC-V port of Fedora
Linux.
Many things happened during that time.

### Triaging

I went throughthe FedoraRISC-V trackerentries, triaged most of them (at the moment 17 entries left inNEW) and tried
to handle whatever possible.

### Fedora packaging

My usual way of working involves fetching sources of a Fedora package (fedpkg
clone -a) and then building it (fedpkg mockbuild -r fedora-43-riscv64). After
some time, I check did it built and if not then I go through build logs to find
out why.

Effect? At the moment,86 pull requests sent for Fedora packages.
From heavy packages like the “llvm15” to simple ones like the “iyfct” (some
simple game). At the moment most of them were merged, and most of these got
built for the Fedora 43. Then we can build them as well as we follow
‘f43-updates’ tag on the Fedora koji.

### Slowness

Work on packages brings the hard, sometimes controversial, topic: speed. Or
rather lack of it.

You see, theRISC-V hardware at the moment is slow. Which results in terrible
build times — look at details of the binutils 2.45.1-4.fc43 package I took from
koji (FedoraandRISC-V Fedora):

Architecture

Cores

Memory

Build time

aarch64

12

46 
GB

36 minutes

i686

8

29 
GB

25 minutes

ppc64le

10

37 
GB

46 minutes

riscv64

8

16 
GB

143 minutes

s390x

3

45 
GB

37 minutes

x86_64

8

29 
GB

29 minutes

That was StarFive VisionFive 2 board, while it has other strengths (such as
upstreamed drivers), it is not the fastest available one. I asked around and one
of porters did a built on Milk-V Megrez — it took 58 minutes.

Also worth mentioning is that the current build ofRISC-V Fedora port is done
with disabledLTO. To cut on memory usage and build times.

RISC-V builders have four or eight cores with 8, 16 or 32GBofRAM(depending
on a board). And those cores are usually compared to Arm Cortex-A55 ones. The
lowest cpu cores in today’s Arm chips.

The UltraRISCUR-DP1000SoC, present on the Milk-V Titan motherboard should
improve situation a bit (and can have 64GBram). Similar with SpacemiT K3-based
systems (but only 32GBram). Both will be an improvement, but not the final solution.

### Hardware needs for Fedora inclusion

We need hardware capable of building above “binutils” package below one hour.
WithLTOenabled system-wide etc. to be on par with the other architectures.
This is the speed-related requirement.

There is no point of going for inclusion with slow builders as this will make
package maintainers complain. You see, in Fedora build results are released into
repositories only when all architectures finish. And we had maintainers
complaining about lack of speed of AArch64 builders in the past. Some developers
may start excludingRISC-V architecture from their packages to not have to wait.

And any future builders need to be rackable and manageable like any other boring
server (put in a rack, connect cables, install, do not touch any more). Because
no one will go into a data centre to manually reboot anSBC-based builder.

Without systems fulfilling both requirements, we can not even plan for theRISC-V 64-bit architecture to became one of official, primary architectures in
Fedora Linux.

### I still useQEMUfor local testing

Such long build times make my use ofQEMUuseful.My AArch64 desktophas 80
cores, so with the use ofQEMUuserspace riscv64 emulation, I can build the
“llvm15” package in about 4 hours. Compare that to 10.5 hours on a Banana PiBPI-F3 builder (it may be quicker on a P550 one).

btop shows 80 cores being busy

AndLLVMpackages make real use of both available cores and memory. I am
wondering how fast would it go on 192/384 cores of Ampere One-based system.

Still, I usedQEMUfor local builds/testing only. Fedora, like several other
distributions, does native builds only.

### Future plans

We plan to start building Fedora Linux 44. If things go well, we will use the
same kernel image on all of our builders (the current ones use a mix of kernel
versions).LTOwill still be disabled.

When it comes to lack of speed… There are plans to bring new, faster builders.
And probably assign some heavier packages to them.

development

fedora

qemu

risc-v

virtualization

### Comments?

If you want to comment, head over tomy post on Mastodon.

* Books I read in 2025 »