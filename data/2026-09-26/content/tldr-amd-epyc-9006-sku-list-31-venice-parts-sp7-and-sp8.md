---
title: 'AMD EPYC 9006 SKU List: 31 Venice Parts, SP7 and SP8 Pricing'
url: https://www.storagereview.com/news/amd-posts-the-full-epyc-9006-sku-list-31-venice-parts-from-700-to-14904-across-sp7-and-sp8
site_name: tldr
content_file: tldr-amd-epyc-9006-sku-list-31-venice-parts-sp7-and-sp8
fetched_at: '2026-09-26T21:49:09.049120'
original_url: https://www.storagereview.com/news/amd-posts-the-full-epyc-9006-sku-list-31-venice-parts-from-700-to-14904-across-sp7-and-sp8
date: '2026-09-26'
description: 'AMD''s EPYC 9006 SKU list is live with 1Ku pricing: nine SP7 parts from $8,008 to $14,904 and 22 SP8 parts from $700 to $11,679.'
tags:
- tldr
---

# AMD Posts the Full EPYC 9006 SKU List: 31 Venice Parts From $700 to $14,904 Across SP7 and SP8

by
 
Brian Beeler

on
 
September 26, 2026

Enterprise
  ◇ 
						
Server

AMD has posted the full SKU list for its 6th Gen EPYC 9006 series, the Zen 6 parts it launched asVenice at Advancing AI 2026in July, and all of the processors offer 1Ku pricing guidance. There are 31 parts across the two sockets: nine for SP7, the 16-channel flagship platform, running from a 64-core CPU at $8,008 to the 256-core EPYC 9996 at $14,904, and 22 for SP8, the 8-channel enterprise socket, running from an 8-core EPYC 9016 at $700 to a 128-core EPYC 9746 at $11,679. AMD marks the list as subject to change, and the platform timing from July still stands: SP7 systems in the fourth quarter of this year, SP8 systems in the first half of 2027.

The naming carries over from Turin, so the first digit is the series, the middle digits track relative performance, the last digit is the generation, and the suffix tells you the bin: an F is a high-frequency part with a 5GHz boost, a P is single-socket only, and no suffix means a standard 1P or 2P part. One new label appears in the SP7 list: the EPYC 9G76, which is the host processor AMD builds into everyHelios compute tray, now listed as an orderable part. AMD has also retired TDP as its power label; the product pages use “Default CPU Power,” which AMD defines as the total power consumed across the compute and I/O dies for the stated performance target, with a configurable range beside it.

## SP7: Nine Parts From 64 to 256 Cores

Every SP7 part is a 1P or 2P processor with 16 channels of DDR5, rated at 1,024GB/s per socket with 8,000 MT/s RDIMMs and 1,638GB/s with 12,800 MT/s MRDIMMs, and AMD’s product pages list PCIe 6.0 x96 for the socket. Zen 6c carries core counts above 96; the standard Zen 6 core carries the 5GHz bins, and the 96-core tier is split three ways.

Model

Cores / Threads

Base Clock

Max Boost

L3 Cache

Default CPU Power (Range)

Sockets

1Ku Price

EPYC 9996

256 / 512

2.55 GHz

4.1 GHz

1024MB

600W (400W-600W)

1P / 2P

$14,904

EPYC 9966

192 / 384

2.9 GHz

4 GHz

768MB

600W (400W-600W)

1P / 2P

$14,079

EPYC 9846

168 / 336

2.85 GHz

3.7 GHz

768MB

500W (320W-500W)

1P / 2P

$13,114

EPYC 9756

128 / 256

3.15 GHz

4 GHz

512MB

500W (320W-500W)

1P / 2P

$12,498

EPYC 9G76

96 / 192

3.4 GHz

4.8 GHz

384MB

500W (320W-500W)

1P / 2P

$11,622

EPYC 9686F

96 / 192

3.4 GHz

5 GHz

384MB

500W (400W-600W)

1P / 2P

$11,434

EPYC 9656

96 / 192

3.05 GHz

3.7 GHz

512MB

400W (220W-400W)

1P / 2P

$9,713

EPYC 9586F

64 / 128

3.75 GHz

5 GHz

384MB

500W (400W-600W)

1P / 2P

$9,701

EPYC 9556

64 / 128

2.75 GHz

4.3 GHz

384MB

300W (220W-300W)

1P / 2P

$8,008

 

The 256-core EPYC 9996 sits at $14,904, the same figure AMD used in its July SPECrate comparison against Intel’s 128-core Xeon 6980P at $13,955, and it keeps 4MB of L3 per core with 1,024MB on the package. Each step down the density ladder costs less in total and more per core: the 192-core 9966 is $14,079, the 168-core 9846 is $13,114, and the 128-core 9756 is $12,498, which puts the flagship at $58 per core and the 9756 at $98. Two SKUs from the launch materials are worth noting. The 256-core EPYC 9956 at 400W, which AMD used in its rack-density endnotes in July, is not in the published list, and the 9G76 is, at $11,622 for 96 cores, a 4.8GHz boost, and a 320W to 500W range.

The 96-core tier is where the socket best shows its range. The 9656 is the standard part, at 400W with 512MB of L3 and a 3.7GHz boost for $9,713. The 9686F is the high-frequency host part AMD showcased in July, hitting 5GHz at 500W with a 400W to 600W range for $11,434. The 9G76 lands between them on price, with a 4.8GHz boost, a 320W floor to the F part’s 400W, and the same 384MB of cache. At 64 cores, the 9556 is the least expensive SP7 SKU at $8,008 and 300W, and the 9586F pairs the same core count and 384MB of L3 with a 3.75GHz base and 5GHz boost for $9,701.

## SP8: 22 Parts From 8 to 128 Cores

SP8 is the socket most enterprise buyers will see, and its list is more than twice as long. Every part carries 8 memory channels at 512GB/s with RDIMMs or 819.2GB/s with MRDIMMs, PCIe 6.0 x128, and a power range that starts as low as 130W. Six F parts run to 5GHz, five P parts are single-socket only, and the remaining 11 are standard 1P or 2P processors.

Model

Cores / Threads

Base Clock

Max Boost

L3 Cache

Default CPU Power (Range)

Sockets

1Ku Price

EPYC 9746

128 / 256

2.9 GHz

4 GHz

512MB

400W (200W-400W)

1P / 2P

$11,679

EPYC 9736

128 / 256

2.7 GHz

3.7 GHz

256MB

360W (200W-400W)

1P / 2P

$10,639

EPYC 9736P

128 / 256

2.7 GHz

3.7 GHz

256MB

360W (200W-400W)

1P

$9,989

EPYC 9676F

96 / 192

3.1 GHz

5 GHz

384MB

400W (200W-400W)

1P / 2P

$10,116

EPYC 9646

96 / 192

2.8 GHz

3.7 GHz

256MB

300W (155W-300W)

1P / 2P

$8,904

EPYC 9646P

96 / 192

2.8 GHz

3.7 GHz

256MB

300W (155W-300W)

1P

$8,001

EPYC 9576F

64 / 128

3.55 GHz

5 GHz

384MB

400W (200W-400W)

1P / 2P

$9,431

EPYC 9536

64 / 128

3.25 GHz

4 GHz

256MB

300W (155W-300W)

1P / 2P

$7,837

EPYC 9526

64 / 128

2.75 GHz

3.7 GHz

256MB

220W (130W-220W)

1P / 2P

$7,123

EPYC 9536P

64 / 128

3.25 GHz

4 GHz

256MB

300W (155W-300W)

1P

$6,595

EPYC 9476F

48 / 96

3.65 GHz

5 GHz

192MB

330W (200W-400W)

1P / 2P

$6,695

EPYC 9456

48 / 96

3.2 GHz

3.7 GHz

256MB

265W (155W-300W)

1P / 2P

$5,252

EPYC 9456P

48 / 96

3.2 GHz

3.7 GHz

256MB

265W (155W-300W)

1P

$4,628

EPYC 9376F

32 / 64

3.8 GHz

5 GHz

192MB

285W (200W-400W)

1P / 2P

$4,849

EPYC 9356

32 / 64

3.6 GHz

4.5 GHz

192MB

250W (155W-300W)

1P / 2P

$3,789

EPYC 9336

32 / 64

3.15 GHz

3.7 GHz

128MB

195W (130W-220W)

1P / 2P

$3,320

EPYC 9356P

32 / 64

3.6 GHz

4.5 GHz

192MB

250W (155W-300W)

1P

$2,795

EPYC 9276F

24 / 48

3.8 GHz

5 GHz

96MB

230W (200W-400W)

1P / 2P

$3,512

EPYC 9256

24 / 48

2.85 GHz

4.5 GHz

96MB

190W (130W-220W)

1P / 2P

$2,501

EPYC 9176F

16 / 32

3.9 GHz

5 GHz

192MB

200W (200W-400W)

1P / 2P

$3,787

EPYC 9116

16 / 32

2.85 GHz

4.5 GHz

48MB

160W (130W-220W)

1P / 2P

$1,200

EPYC 9016

8 / 16

3.05 GHz

4.8 GHz

48MB

130W (130W-220W)

1P / 2P

$700

 

The top of the SP8 stack overlaps the bottom of SP7 on core count but undercuts it on price. The 128-core 9746 is $11,679 with 512MB of L3 at 400W, against $12,498 for the 128-core SP7 9756, and the 96-core 9646 is $8,904 at 300W against $9,713 for the SP7 9656; the difference buys the bigger socket’s double memory bandwidth. The 128-core 9736 drops to 256MB of L3 and a 3.7GHz boost for $10,639, and its single-socket twin, the 9736P, is $9,989.

The P discount widens as the parts get smaller. At 128 cores the single-socket version saves 6%, at 96 cores 10%, at 64 cores 16%, at 48 cores 12%, and at 32 cores the 9356P is $2,795 against $3,789 for the 9356, a 26% cut for giving up the second socket. The F parts pay the opposite premium: the 64-core 9576F is $9,431, $1,594 over the standard 9536, for a 5GHz boost, 384MB of L3, and a 400W rating. The most curious part of the list is the 16-core 9176F, which carries 192MB of L3, 12MB per core, at $3,787, the profile of a CPU built for per-core software licensing, where cache per thread matters more than thread count. At the bottom, the 8-core 9016 is $700 at 130W, and the 16-core 9116 is $1,200.

## What Changed Since July

Two details in the published pages update what AMD said in July. AMD’s launch deck listed PCIe Gen 6 as “up to 128 lanes (1P)” for the family; the SP8 slide claimed the full 128, and the SP7 slide gave no lane count at all. The processor pages now put numbers on both sockets: every SP7 part is listed at PCIe 6.0 x96, and all SP8 CPUs at x128.

The second detail is the 400W EPYC 9956, the 256-core CPU AMD used in its rack-density endnotes in July, which has no product page yet; either it arrives later, or the density case now rests on the 600W 9996. AMD’s footnote says the list is subject to change, so that one may resolve before SP7 systems ship. Our earlier coverage of the first Venice platforms fromGiga Computing,ASUS, andSupermicrohas the system side; Giga Computing expects SP7 systems to ship with AMD’s November launch and SP8 systems to follow in March 2027. We’ve also seen plenty of pre-production units from others; Dell, for instance, showed early designs at the AMD event and later at DTW.

### AMD EPYC 9006 Series Product Page

Engage with StorageReview

Newsletter|YouTube| PodcastiTunes/Spotify|Instagram|Twitter|TikTok|RSS Feed

### Brian Beeler

Brian is located in Cincinnati, Ohio and is the chief analyst and President of StorageReview.com.

 

Previous post:NetApp to Acquire PEAK:AIO, Bringing Its Scale-Out pNFS Metadata Work to ONTAP