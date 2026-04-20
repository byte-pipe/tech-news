---
title: What makes Intel Optane stand out – Tech Central
url: https://blog.zuthof.nl/2023/06/02/what-makes-intel-optane-stand-out/
site_name: hnrss
content_file: hnrss-what-makes-intel-optane-stand-out-tech-central
fetched_at: '2026-03-15T19:14:17.410914'
original_url: https://blog.zuthof.nl/2023/06/02/what-makes-intel-optane-stand-out/
date: '2026-03-15'
description: What makes Intel Optane stand out (2023)
tags:
- hackernews
- hnrss
---

Once in a while new hardware is released that makes a difference. Such a device is the Intel Optane series of high-performance SSD’s for professional use, which was released in late 2017. In this case I’m talking about the IntelOptane P4800XandP5800Xand their consumer counterparts (900Pand905P). All drives are based on the 3D XPoint Technology that Intel co-developed with Micron.

In contrary to regular SSD’s, Optane drives like the P5800X bringsultra low latency, high durability and high performanceto the table. Effectively Optane is a technology that both has aspects of DRAM and regular NAND based Flash. The downsides of Optane are the high cost and relative low capacity. Combined with the high innovation rate of NAND SSD’s andCompute eXpress Link (CXL)around the corner, there was little reason to switch to this pieces of technology for most companies.

Finally, Intel decided to stop the innovation of this technology in July 2022 as part of it’s IDM 2.0 company strategy. In fact, Intel stopped all their flash storage based activities. This does not mean the drives aren’t for sale anymore.

Current Optane based products (in SSD and DIMM form) are still being sold. In the beginning of this year even a newOptane Persistent Memory NV-DIMM series 300 (also called PMEM)was released. This new Optane release was needed for the 4th generation of Intel Scalable CPU’s code nameSapphire Rapidsthat was released in January 2023.

ServeTheHome made a greatvideo about Optane Persistent Memoryif you’re not familiar with it.

## The Gear

As part of the VMware vExpert program, I had the opportunity to test a couple of Intel Optane P4800X drives, which I wanted to get my hands on for quite time, being a (hardware) techie. Many thanks toCorey Romero,Matt Mancini,Simon Toddand theIntel Business and Storage BUfor making this possible.

### Drive specs

Optane P4800X
 (1st Gen)
Optane P5800X
 (2nd Gen)
Capacity
375 GB – 1,5 TB
400 GB – 3,2 TB
Release date
Q3 2017
Q4 2020
PCIe version
PCIe 3.0 (NVMe)
PCIe 4.0 (NVMe)
Sequential Read
2500 MB/s
7200 MB/s
Sequential Write
2200 MB/s
6200 MB/s
Read IOPS (4K)
550.000
1.500.000
Write IOPS (4K)
500.000
1.500.000
Durability (
DWPD
)
30 (Write Intensive)
100 (Write Intensive)

## Optane Advantages

The question arises, what makes Optane drives special compared to NAND based SSD’s. When not familiar with this topic, NAND relates to the type of flash chips used on an SSD. Pretty much all (non Optane) SSD’s are NAND based.

The answer why Optane has advantages over NAND based SSD’s can be explained based on a couple of their qualities.

* Durability
* Data consistency
* Performance (in terms of):LatencyWrite Consistency
* Latency
* Write Consistency

### Durability

In general the durability of an SSD is an important rating, because it shows how many data can be written to the device during the warranty period. In general the cheaper the SSD, the less data can be written.

For examples, when an SSD has only has 3 instead of 5 year of warranty, 40% lesser writes are supported. That’s the easy and cheapest way for manufactures to “raise” the durability.

Compared to NAND based SSD’s, durability is where an Optane drive really shines. So, how does it compares to other professional and consumer drives?

SSD Type
Power-loss Protection
Durability (
DWPD
)
Warranty
QLC based consumer
No
0,1
3y
TLC based consumer
No
0,2 – 0,35
3-5y
TLC based prosumer
Yes
0,3 – 0,35
5y
TLC based professional
(Read Intensive)
Yes
1
5y
TLC based professional
(Mix Use)
Yes
3
5y
MLC / TLC based professional
(Write Intensive)
Yes
10
5y
Optane P4800X
(1st Gen.)
Yes
30
5y
Optane P5800X
(2nd Gen.)
Yes
100
5y

As can be seen in the table above, the Optane is the choice of SSD for high write environments.

For a more detailed explanation of SSD durability, check “Comparing Wear Figures on SSDs” blog byJim Handy(a.k.a. The SSD Guy) to learn more about the numbers that manufacturers throw at you regarding the durability of their drives.

Relevant durability terms are:

* Drive Writes per Day (DWPD)
* Terabytes Written (TBW)
* GB/day

In the end all terms relate to each other, which shows nicely in the diagram below.

Source:
The SSD Guy

### Data consistency

A second aspect that contributes to durability is data consistency. Professional SSD’s (and some consumer ones) have power-loss protection (PLP). PLP is an often overlooked feature of an SSD, that takes care of pending data to be safely stored before the device completely loses power:

PLP protects against:

* Loss of data in the SSD’s cache
* Loss or corruption of the SSD mapping table
* Page corruption when write cycle would be interrupted

PLP can be done in hardware by adding an array of capacitor to the device or in firmware, of which the hardware implementation is preferred. For more info see the link “A Closer Look At SSD Power Loss Protection” from Kingston Memory.

Crucial M500 Consumer drive with hardware PLP.
Source:
TheSSDReview.com

All professional grade SSD’s have I’ve worked with (including Optane) have PLP. Be sure to check your drives for hardware PLP. On the Intel ARK product specification site, hardware PLP for Optane drives translates to the “Enhanced Power Loss Data Protection” feature.

Relevant section of P5800X Spec sheet.

### Performance

Performance of an SSD has 2 important aspects. Latency and Write Consistency.

#### Latency

Latency is where Optane has a clear advantage over NAND SSD’s. Latency is the time the device needs to pull the requested data off it’s flash chips and send it to the CPU for processing.

Let’s compare Optane drives with current Gen professional NAND based ones. It does not make sense to perform the test myself, since the pro’s atStoragereview.comhave already done that.

Optane Read Latency. Source:
Storagereview.com

NAND Read Latency. Source:
Storagereview.com

The tables above shows it all. IOPS wise, Optane is up-to-par with the competition, but the drive shines when it comes down to latency. It’s just astonishing. Being around 25 microsecond (us) per 4K random read for Optane versus 90 to 110 us for NAND based drives. Putting it in perspective, is that every small read on an Optane drive is more than 300% faster. Even up to 1.3 Million IOPS on a single drive.

This means that data reaches the CPU faster, but also lowers the load on the CPU because it simply has to wait shorter.

#### Write Consistency (QoS)

An Optane drives delivers it’s maximum write performance in a consistent way, therefore you could say it’s a form or QoS. That’s not the case for NAND based drives.

A normal NAND based SSD often has DRAM cache or a small part of extra fast flash. This is due to the fact that NAND SSD’s can only writes data to empty 4K pages. Therefore empty pages must be available for optimal write performance.

Due to it’s nature, the erase of a NAND pages takes some time. When most pages are in use or have not been emptied yet (by the garbage collection process), the writes are cached in the DRAM and/or the small of extra fast flash. When that is also filled-up, degradation of write performance occurs for the drive to be able to keep with the garbage collection. In other words, writes are throttled until enough of empty pages are available.

Optane does not work this way since it is byte addressable instead of per 4K page. Secondly data can be overwritten directly on Optane devices. Due to these two characteristics, write are always performed with maximum performance, even under continuous heavy write loads.

## Intended use

Due to the reasons above like low latency, consistent (write) performance, high IOPS and high endurance the Optane drives are especially suited for:

* Ceph (WAL and Caching)
* ZFS (ZIL and SLOG)
* QoS advantageous environments
* High write environments
* High performance databases
* VDI environments
* vSAN Caching

## To conclude

The Intel Optane drives are well suite for many use cases. Especially those that require (consistent) low latency and high IOPS, combined with a high endurance. On the other hand NAND type SSD are still getting better and a lot of development takes place in that space. Secondly the prices for NAND drives are still dropping to an all time low nowadays.

Unfortunately in a couple of years Optane SSD’s will be end of sale, since Intel decided to stop it’s involvement in the memory space. Nonetheless is still available for a couple of year so we still can enjoy it in SSD or NV-DIMM form factor.

By reading this post, I hope you’ve learned about Optane key architectural differences, SSD Endurance, SSD Power Loss Protectection, write consistency and why those qualities matters. Again many thanks toCorey Romero,Matt Mancini,Simon Toddand theIntel Business and Storage BUfor the opportunity.

Cheers, Daniël

## Useful links

ServeTheHome: Optane Persistent Memory (NV-DIMM’s or also called PMEM

ServeTheHome: Compute eXpress Link (CXL)

Western Digital: Understanding SSD Endurance

TheSSDGuy: Comparing Wear Figures on SSDs

Kingston: A Closer Look At SSD Power Loss Protection

Storagereview.com: Intel Optane P5800X Review

Categories:
Homelab
Storage
vSAN


Tags:
homelab
intel
optane
ssd
storage
vSAN
