---
title: What's new about Zen 5 and Arrow Lake? - Page 2 - Agner's CPU blog
url: https://www.agner.org/forum/viewtopic.php?t=287&start=10
site_name: hackernews_api
fetched_at: '2025-07-27T22:07:42.784208'
original_url: https://www.agner.org/forum/viewtopic.php?t=287&start=10
author: matt_d
date: '2025-07-27'
description: Test Results for AMD Zen 5
tags:
- hackernews
- trending
---

## What's new about Zen 5 and Arrow Lake?

News and research about CPU microarchitecture and software optimization

Post Reply


* Print view

Search

Advanced search

			12 posts

* Previous
* 1
* 2

agner


Site Admin

Posts:

88

Joined:
 2019-12-27, 18:56:25

Contact:

Contact agner

Website

### Re: What's new about Zen 5 and Arrow Lake?

* Quote

Postbyagner»2025-05-14, 16:30:11

@jfonseca

You can ignore the error message. I have already got the test results from somebody else. I am currently revising the scripts. I can send the revised scripts to you if you want.

Top

agner


Site Admin

Posts:

88

Joined:
 2019-12-27, 18:56:25

Contact:

Contact agner

Website

### Test results for AMD Zen 5

* Quote

Postbyagner»2025-07-26, 12:43:13

I have now finished testing the Zen 5. Thank you to the people who have helped running test scripts for me.

My test results for the AMD Zen 5 are impressive. It has a lot of features that increase different aspects of the CPU performance to new levels, never seen before.

Most importantly, the instruction fetch rate is increased from 16 to 32 bytes per clock cycle. The 16-bytes fetch rate has been a serious bottleneck in both Intel and AMD processors through many generations. The size of one instruction can be anywhere from 1 to 15 bytes. An AVX512 instruction can be from 6 to 11 bytes. This was a serious bottleneck since the rest of the pipeline could handle four instructions per clock cycle or more in earlier AMD processors as well as Intel processors. Only loops that fit into the micro-op cache could utilize the high throughput.

The Zen 5 can execute up to six instructions per clock cycle (rarely eight). Such a high throughput requires careful considerations from the software programmer to avoid long dependency chains. A dependency chain is a situation where each instruction depends on the result of the preceding instruction so that it is impossible to execute more than one instruction at a time.

The number of execution units is increased over previous models. There are six integer ALUs, four address generation units, three branch units, four vector ALUs, and two vector read/write units. All common instructions have more than one execution unit to choose between so that it will rarely have to wait for a vacant unit. It is possible to do six simple integer instructions per clock cycle. Vector instructions and floating point instructions can execute at a rate of two vector additions, two vector multiplications, and two vector read or write instructions simultaneously per clock cycle. All vector units have full 512 bits capabilities except for memory writes. A 512-bit vector write instruction is executed as two 256-bit writes.

Integer memory operations can execute at a rate of four reads per clock cycle or two reads and two writes. Floating point and vector memory operations can execute at the rate of two reads or writes per clock cycle, except for 512-bit writes.

The performance of branch instructions (if-then-else constructs) is also faster than anything we have seen before. The Zen 5 can execute two predicted taken branches or three predicted not-taken branch instructions per clock cycle. The branch predictor can look two branches ahead and it can decode both sides of a two-way branch simultaneously. Complicated repetitive branch patterns can be predicted after a short learning period.

The latency of integer vector addition has been increased from 1 clock cycle in Zen 4 to 2 clocks in Zen 5, while the latency of floating point addition is reduced from 3 to 2 clocks. Integer vector instructions and floating point vector instructions now have the same latencies.

While the CPU performance in terms of instruction fetch rate, decoding, execution units, memory read/write, and branch throughput is improved to new levels, there are only minor improvements in cache sizes and associativity. This means that CPU throughput is rarely a bottleneck in Zen 5, and the programmer has to focus on optimizing memory access if you want to utilize the high computing power of the Zen 5. The Zen 5 can give a significant performance boost to computation-intensive programs, while programs that are limited mainly by memory and disk access will not benefit much.

Detailed results are reported in my
microarchitecture manual
 and
instruction tables
.

Top

Post Reply


* Print view

Display:
All posts
1 day
7 days
2 weeks
1 month
3 months
6 months
1 year

Sort by:
Author
Post time
Subject

Direction:
Ascending
Descending

			12 posts

* Previous
* 1
* 2

Return to “Agner's CPU blog”

Jump to

* Agner's CPU blog
