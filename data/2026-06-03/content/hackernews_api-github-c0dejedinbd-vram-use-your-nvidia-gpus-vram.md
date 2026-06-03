---
title: 'GitHub - c0deJedi/nbd-vram: Use your NVIDIA GPU''s VRAM as swap space on Linux. Built for laptops with soldered memory and no upgrade path. If you have an RTX card sitting there with 8GB of VRAM and you''re getting swapped to SSD, this puts that VRAM to work · GitHub'
url: https://github.com/c0dejedi/nbd-vram
site_name: hackernews_api
content_file: hackernews_api-github-c0dejedinbd-vram-use-your-nvidia-gpus-vram
fetched_at: '2026-06-03T12:34:45.134597'
original_url: https://github.com/c0dejedi/nbd-vram
author: tanelpoder
date: '2026-06-02'
description: Use your NVIDIA GPU's VRAM as swap space on Linux. Built for laptops with soldered memory and no upgrade path. If you have an RTX card sitting there with 8GB of VRAM and you're getting swapped to SSD, this puts that VRAM to work - c0deJedi/nbd-vram
tags:
- hackernews
- trending
---

c0deJedi

 

/

nbd-vram

Public

* NotificationsYou must be signed in to change notification settings
* Fork5
* Star266

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

10 Commits
10 Commits
.github
.github
 
 
benchmarks
benchmarks
 
 
systemd
systemd
 
 
udev
udev
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
demo.gif
demo.gif
 
 
install.sh
install.sh
 
 
nbd-vram-connect.sh
nbd-vram-connect.sh
 
 
nbd-vram-disconnect.sh
nbd-vram-disconnect.sh
 
 
nbd-vram-power-check.sh
nbd-vram-power-check.sh
 
 
nbd-vram.c
nbd-vram.c
 
 
nbd-vram.conf
nbd-vram.conf
 
 
test-fill.sh
test-fill.sh
 
 
test-nbd.sh
test-nbd.sh
 
 
uninstall.sh
uninstall.sh
 
 
View all files

## Repository files navigation

# nbd-vram

Use your NVIDIA GPU's VRAM as swap space on Linux.

Built for hybrid graphics laptops with soldered memory and no upgrade path. The display runs off the integrated AMD/ATI GPU. The NVIDIA card sits idle most of the time, its VRAM completely unused. This puts that VRAM to work as high-priority swap.

Tested on: AMD/ATI + RTX 3070 Laptop (GA104M, 16 GB RAM, 8 GB VRAM), driver 580.159.03, kernel 6.17, Pop!_OS. Allocated 7 GB for swap. End result including zram and SSD swap: ~46 GB total addressable memory, tripled from stock. Overflow order: RAM fills, then VRAM absorbs the spill (PCIe), then zram compresses the rest (CPU), then SSD only if everything else is exhausted.

## How it works

A small daemon allocates VRAM via the CUDA driver API, then serves it as a block device using the NBD (Network Block Device) protocol over a Unix socket. The kernel's built-innbddriver connects to it and exposes/dev/nbdX. From there it's a normal swap device.

Data path: kernel swap subsystem - /dev/nbdX - nbd kernel driver - Unix socket - nbd-vram daemon - cuMemcpyHtoD/DtoH - GPU VRAM.

No kernel module to write or maintain. No NVIDIA kernel symbols. Survives kernel and driver updates without rebuilding anything.

## Why not the NVIDIA P2P API?

The "obvious" approach isnvidia_p2p_get_pages_persistent, which pins VRAM pages in BAR1 so the CPU can access them directly viaioremap_wc. Every existing project that tried this route hits the same wall: the NVIDIA driver returnsEINVALon consumer GeForce GPUs. Both the persistent and non-persistent variants, both flag values. It's gated at the RM level for Quadro/datacenter SKUs only, regardless of driver version.

The other approach - directlyioremap_wcthe BAR1 physical address without going through the P2P API - also doesn't work. The GPU's internal page tables only have ~16 MiB of BAR1 mapped (just the display framebuffer). Reads from the rest return zeros.mkswapappears to succeed, thenswaponfails because the swap header isn't actually there.

The NBD approach sidesteps all of this.cuMemcpyHtoDandcuMemcpyDtoHwork on any CUDA GPU without any special permissions.

## Requirements

* NVIDIA GPU with CUDA support (any consumer RTX/GTX card)
* NVIDIA driver withlibcuda.so.1(no CUDA toolkit needed)
* Linux kernel 3.0+ (nbd module, built into most distros)
* nbd-clientpackage
* gcc,make

## Install

git clone https://github.com/c0dejedi/nbd-vram

cd
 nbd-vram
sudo ./install.sh
sudo systemctl start vram-swap-nbd

Verify:

swapon --show

#
 NAME TYPE SIZE USED PRIO

#
 /dev/nbd0 partition 7G 0B 1500

The service is enabled on install, so it comes up automatically on every boot.

## Configuration

Edit/etc/systemd/system/vram-swap-nbd.service:

Environment
=
VRAM_SETUP_SIZE_MB
=7168 
#
 how much VRAM to use

Environment
=
VRAM_SWAP_PRIORITY
=1500 
#
 swap priority (higher = used first)

The daemon tries the requested size first and backs off in 512 MiB steps if the GPU is short on memory - so it will grab as much as it can even if the display compositor is already loaded.VRAM_SETUP_SIZE_MBis the ceiling, not a hard requirement.

After changing, runsudo systemctl daemon-reload && sudo systemctl restart vram-swap-nbd.

## Power management

The installer asks whether to enable power-aware management on first install. If enabled, the service automatically stops when you unplug from AC (or when battery drops below a threshold), and restarts when power is restored. Manualsystemctl stopis always respected and won't be overridden.

To change settings after install, edit/etc/nbd-vram.conf. Changes take effect on the next poll (within 60 seconds) or immediately on the next AC plug/unplug event.

## Smoke test (without installing)

sudo bash test-nbd.sh

Allocates VRAM, connects the NBD device, does a 1 MiB write/readback check, activates swap, then prints teardown instructions.install.shhandles teardown automatically if a test instance is running.

To stress the full partition after the smoke test passes:

sudo bash test-fill.sh

Writes the entire VRAM partition with zeros, verifies a sample read back, then auto-restores swap on exit.

## Performance

Tested on RTX 3070 Laptop (8 GB VRAM), kernel 6.17, Pop!_OS. Compared against NVMe cryptswap (dm-crypt, PCIe 4.0). All benchmarks run with O_DIRECT to bypass page cache.

Three benchmarks are inbenchmarks/. Each runs NVMe first, then starts the VRAM service and runs the same test against the block device. State is restored on exit.

sudo bash benchmarks/bench-throughput.sh 
#
 sequential read/write (dd, 2 GiB, O_DIRECT)

sudo bash benchmarks/bench-iops.sh 
#
 4K random IOPS (fio, libaio, iodepth=32)

sudo bash benchmarks/bench-latency.sh 
#
 per-operation latency (ioping, 20 requests)

fioandiopingare installed automatically if missing.

### Sequential throughput (dd, 2 GiB)

Device

Write

Read

NVMe

2.7 GB/s

2.9 GB/s

VRAM (nbd)

1.1 GB/s

2.3 GB/s

VRAM is slower for large sequential transfers. The bottleneck is the NBD + CUDA userspace round-trip - every block crosses a Unix socket and acuMemcpycall, which adds overhead that NVMe's direct kernel block path doesn't pay. Sequential throughput is not the primary swap workload (the kernel swaps individual 4K pages, not 4 MiB streams) - see the IOPS and latency benchmarks below.

### 4K random IOPS (fio, libaio, iodepth=32)

Device

Read IOPS

Write IOPS

Avg latency

NVMe

45.4k

45.3k

343 us

VRAM (nbd)

28.7k

28.7k

550 us

NVMe wins for sustained random I/O. At iodepth=32, NVMe can have 32 requests genuinely in flight simultaneously; the NBD+CUDA path serialises them through the daemon, so the depth advantage is reduced. The VRAM daemon also adds CPU overhead that the NVMe path does not pay. For continuous high-throughput swap pressure, NVMe is faster.

The picture changes for sporadic access - see the latency benchmark below.

### Per-operation latency (ioping, 4K reads, 1 request/sec)

Device

Min

Avg

Max

NVMe

120 us

9.05 ms

10.1 ms

VRAM (nbd)

134 us

335 us

490 us

VRAM is 27x faster average latency.The NVMe drive is physically capable of ~112 us (visible on the warmup request) but APST (Autonomous Power State Transitions) puts it to sleep between requests. At 1 request per second - the rate of sporadic swap access - it wakes cold almost every time and pays a ~9 ms penalty. VRAM has no power states and responds in 133-490 us consistently.

This is the scenario that matters most in practice. Memory pressure on a laptop is rarely a sustained GB/s flood - it is individual 4K page faults arriving seconds apart. Every one of those faults stalls waiting for the swap device to respond. At 9 ms per fault, NVMe swap is felt. At 335 us, VRAM swap is not.

## Uninstall

sudo bash uninstall.sh

## License

MIT - Sean Lobjoit (c0dejedi)

## About

Use your NVIDIA GPU's VRAM as swap space on Linux. Built for laptops with soldered memory and no upgrade path. If you have an RTX card sitting there with 8GB of VRAM and you're getting swapped to SSD, this puts that VRAM to work

www.seanlobjoit.com

### Topics

 linux

 memory

 gpu

 nbd

 cuda

 nvidia

 swap

 laptop

 vram

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

266

 stars
 

### Watchers

1

 watching
 

### Forks

5

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Shell57.9%
* C41.7%
* Makefile0.4%