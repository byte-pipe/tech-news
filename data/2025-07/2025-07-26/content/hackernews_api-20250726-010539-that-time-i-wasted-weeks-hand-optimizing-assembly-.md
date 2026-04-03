---
title: That time I wasted weeks hand optimizing assembly because I benchmarked on random data – Vidar's Blog
url: https://www.vidarholen.net/contents/blog/?p=1160
site_name: hackernews_api
fetched_at: '2025-07-26T01:05:39.669986'
original_url: https://www.vidarholen.net/contents/blog/?p=1160
author: thunderbong
date: '2025-07-21'
description: I wasted weeks hand optimizing assembly because I benchmarked on random data
tags:
- hackernews
- trending
---

Once upon a time I worked in the field of Java Optimizations.

The target system was a distributed data processing platform that ran across hundreds of thousands of machines. At such scales, a 0.5% improvement would easily make up my salary going forward, and 2% was a good result for the half.

That doesn’t mean it was easy. Never have I ever seen such a highly optimized Java codebase. Not before, not since.

Every low hanging fruit had long since been picked clean. For example, there was minimal use ofjava.lang.Stringbecause ain’t nobody got time for a second allocation of achar[]with associated indirection and GC churn.

In other words, we were looking at increasingly heroic optimizations to justify our own existence.

Through careful, large scale profiling, I discovered that data serialization was a small but worthwhile place to focus. In particular, VarInt encoding used enough CPU time to warrant investigation.

If you’re not familiar, a VarInt, or more specifically ULEB128, is a byte efficient way to encode arbitrary integers. You use however many groups of 7 bits you need for your number, and use the 8th bit to specify whether there is another byte coming.

Numbers needing 7-bits or less (< 128) are encoded as0nnnnnn

14-bit (<16384),1nnnnnnn 0nnnnnnn

21bit (<2097152),1nnnnnnn 1nnnnnnn 0nnnnnnn

And so on, in little-endian order.

For a 32bit int, you will need between 1 and 5 bytes. For a 64bit long, you will need between 1 and 10.

They are used in Google Protobuf, Apache/Facebook Thrift, WASM, DWARF, and other formats that want a compact binary representation without sacrificing range.

The interface the system used for this encoding was essentiallyint encodeLong(byte[] buffer, int offset, long data), returning the number of bytes written.

Conventional wisdom is that this is way too small to benefit from native code.

But conventional wisdom is for conventional development.

We were in the early phases of forking the JVM, had recently built the infrastructure to implement custom optimizations, and we were itching to use it.

Engineers don’t exactly need convincing to work on fun assembly puzzles to begin with, but the empire builders in management were additionally competing in a Manifest Destiny style land grab as the company maneuvered to take control of its tech stack from end to end. They were pushing this as hard as anyone to stake their claims.

So off I went to write an ultra optimized VarInt encoder that the JVM JIT could serialize straight into the instruction stream, bypassing the normal overhead associated with JNI.

And I sure did.

My hand coded, branchless, SIMD assembly algorithm performed 4x better than the already highly optimized Java implementation!

(The exact details escape me, but it was some combination of using BMI2 to scatter bits into groups of 7, and some AVX2 comparisons and bit extensions to compute the continuation mask and determine the resulting length.)

This was verified in a benchmark that ran both versions on billions of random numbers, confirming both the huge speedup and the bit-for-bit compatibility of the result.

I spent probably two weeks implementing, testing, integrating, polishing, and landing this change.

Finally I tried to measure the difference in prod.

Nothing.

Measuring ~1% improvements is always a challenge, but even with huge A/B runs, the difference was exactly nothing.

I did some investigations, and eventually found why my benchmarks were so misleading compared to real world performance.

It was because I was using random numbers.

As it turns out, mathematically speaking, most numbers are huge. By an infinite margin. There are dramatically many more 18 digit numbers, than there are 3 digit numbers.

In fact, if you generate random 64bit unsigned longs and try to encode them as ULEB128,

* 50% will need 10 bytes
* ~49.6% will need 9 bytes
* ~0.38% will need 8 bytes
* ~0.003% will need 7 bytes
* …
* ~0.00000000000009% will need 2 bytes
* ~0.0000000000000006% will need 1 byte

Meanwhile, if I look around my real world right now, I see several dozen numbers. Almost all fit into two bytes with room to spare. A “60” watt charger, an old Covid-“19” test, page “1” of “2” of some statement. A few zip codes and reference numbers break the pattern, but overall, real numbers tend to be small.

That’s exactly why people use VarInt in the first place.

The Java version had to do more work the more bytes it had to output. By measuring on random numbers, I was inadvertently doing all my testing against the algorithm’s unrealistic worst case scenario.

When I adjusted my benchmark to primarily generate small numbers, the speedup vanished entirely.

I ended up rolling back the change, and wrote off the time spent as a proof-of-concept for developing and productionizing a custom JIT optimization.

(And I crossed “SIMD” off myprogramming bingo card.)
