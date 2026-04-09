---
title: 'lsr: ls but with io_uring - rockorager.dev'
url: https://rockorager.dev/log/lsr-ls-but-with-io-uring/
site_name: hackernews_api
fetched_at: '2025-07-20T01:04:50.640326'
original_url: https://rockorager.dev/log/lsr-ls-but-with-io-uring/
author: mpweiher
date: '2025-07-18'
description: 'lsr: ls with io_uring'
tags:
- hackernews
- trending
---

As an excercise in syscall golf, I wrote an implementation ofls(1)which uses my IO library,ourioto perform as much of the IO as possible. What I ended up with is something that is faster than any version or alternative tolsI tested, and also performs anorder of magnitude fewer syscalls. I’m calling itlsr. Let’s start with the benchmarks, then we’ll see how we got there.

## Benchmarks

### Time

Data gathered withhyperfineon a directory ofnplain files.

Program
n=10
n=100
n=1,000
n=10,000
lsr -al
372.6 µs
634.3 µs
2.7 ms
22.1 ms
ls -al
1.4 ms
1.7 ms
4.7 ms
38.0 ms
eza -al
2.9 ms
3.3 ms
6.6 ms
40.2 ms
lsd -al
2.1 ms
3.5 ms
17.0 ms
153.4 ms
uutils ls -al
2.9 ms
3.6 ms
11.3 ms
89.6 ms

### Syscalls

Data gathered withstrace -con a directory ofnplain files. (Lower is better)

Program
n=10
n=100
n=1,000
n=10,000
lsr -al
20
28
105
848
ls -al
405
675
3,377
30,396
eza -al
319
411
1,320
10,364
lsd -al
508
1,408
10,423
100,512
uutils ls -al
445
986
6,397
10,005

## How we got there

Let’s start with howlsrworks. To list directory contents, we basically have 3 stages to the program:

1. Parse args
2. Gather data
3. Print data

All of the IO involved happens in the second step. Wherever possible,lsrutilizes io_uring to pull in the data it needs. To get to that point, it means that we open the target directory with io_uring, if we need local time, user data, or group data, we open (and read) those files with io_uring. We do allstatcalls via io_uring, and as needed we do the equivalent of anlstatvia io_uring. In practice, this means that the number of syscalls we have should be drastically smaller than equivalent programs because we are able to batch thestatsyscall. The results clearly show this…lsrhas at least an order of magnitude fewer syscalls than it’s closest equivalent, beinguutils ls.

We also use the zig stdlib StackFallbackAllocator. This let’slsrallocate memory it needs up front, but fallback to a different allocator when it’s exhausted the fixed allocation. We allocate 1MB up front, which is more than enough for typical usage. This further reduces syscalls by reducing mmap usage.

As a result of working directly with io_uring, we also bypass several libc related pitfalls. Namely, we have no dynamic linking -lshas some considerable overhead in loading libc and related libraries…but it also has the benefit of having locale support.lsrdoes not boast such a feature. Despite being statically linked,lsris still smaller than GNUls: 138.7KB vs 79.3KB when built with ReleaseSmall.

## Anomolies and Thoughts

I have no idea whatlsdis doing. I haven’t read the source code, but from viewing it’sstrace, it is callingclock_gettimearound 5 timesper file. Why? I don’t know. Maybe it’s doing internal timing of steps along the way?

Sorting ends up being a massive part of the workload. I suspect this is whereuutils lsis getting slowed down, since it is doing pretty good on a syscall basis.lsrspends about 30% of it’s runtime sorting, the rest is the IO loop.

This ended up being a pretty fun project to write, and didn’t take too much time either. I am shocked at how much io_uring can be used to reduce syscalls…lsis a pretty basic example but you can only imagine how much of an effect this would have on something like a server.

Also - I’m usingtangled.shfor this project. They have a really cool idea, and I want to see how the PR workflow is so…if you have any bugs or changes, please visit therepo. All you need is an atproto account + app password. I suspect more icons will be needed, feel free to make an issue for icon requests!
