---
title: 'Two Bits Are Better Than One: making bloom filters 2x more accurate'
url: https://floedb.ai/blog/two-bits-are-better-than-one-making-bloom-filters-2x-more-accurate
site_name: hackernews_api
content_file: hackernews_api-two-bits-are-better-than-one-making-bloom-filters
fetched_at: '2026-02-22T19:11:24.881666'
original_url: https://floedb.ai/blog/two-bits-are-better-than-one-making-bloom-filters-2x-more-accurate
author: matheusalmeida
date: '2026-02-17'
description: Optimisation of bloom filters in Floe using double bit setting with lightweight hashing.
tags:
- hackernews
- trending
---

Engineering
,

C
,

FloeSQL

# Two Bits Are Better Than One: making bloom filters 2x more accurate

 by

Makar

·
Feb 16, 2026 10:00:00 AM

A bloom filter is a probabilistic data structure that potentially can make SQL queries execute orders of magnitudes faster. Today I want to tell you how we use them in Floe, and how we make them produce 2x fewer false results.

## What is a bloom filter?

Feel free to skip this section if you know the answer.

A bloom filter is a probabilistic data structure that answers one question: "Is this element definitely not in the set?" It can give false positives (says yes when the answer is no), but never false negatives (it won't miss elements that are actually there). The main benefit is that a well-designed bloom filter can be really fast - a few CPU cycles per lookup. That's faster than a single function call.

The structure: An array of m bits, all initially set to 0.

Insertion: To add an element, we:

* Hash the element using k different hash functions
* Each hash gives us a position in the bit array
* Set all k bits at those positions to 1

Lookup: To check if an element exists:

* Hash it with the same k hash functions
* Check if ALL k bits are set to 1
* If any bit is 0 → definitely not in the set
* If all bits are 1 → probably in the set

## Why do bloom filters matter?

Here we're discussing bloom filters in the context of database engineering. If you're not familiar with how databases join tables - here's a quick primer: a hash join matches rows from two tables. First, it loads the smaller table into a hash table (that's the build side). Then it scans the larger table row by row, looking up each value in the hash table to find matches (that's the probe side). Most of the work happens on the probe side, because the larger table can have billions of rows.

When processing millions of rows we want to avoid all the extra work that we can. Don't decompress the data you won't use. Don't probe hash tables for keys that don't exist. Discard rows as soon as you can - it's called being efficient (not lazy!)

We use bloom filters at 2 critical places:

1. Storage engine (column store): Before decompressing the columns
2. Hash joins: before probing the hash table during probe phase

## 1. Adaptive Storage Engine filtering

Let's imagine the situation where we want to join two tables where only 1% of 10 billion probe-side rows will be matched. Without filtering we would need to decompress and probe 99% of those rows before discarding them.

What we do instead:

Build phase: At build phase we populate the bloom filter with hashes of build side.

Pushdown: after build phase is complete we push down the bloom filter, which at this point is read-only, to the storage engine.

First-pass filtering: The storage engine decompresses only the columns needed for bloom filtering. It checks each value against the bloom filter, and marks values that definitely do not match the build side.

Adaptive behaviour: Here it gets interesting. We keep the statistics of how many rows we skipped. If we end up discarding almost no rows we don't bother with first-pass filtering and disable it. But we keep checking decompressed rows to re-enable filtering if stats improve.

Rough estimate:

Without bloom filtering:

* Decompress 10 columns × 10B rows
* = 100B column decompression operations
* = time to get another coffee. Or three.

With bloom filtering:

* First pass: Decompress 1 column × 10B rows = 10B operationsbloom rejects 99% → 100M survivors
* bloom rejects 99% → 100M survivors
* Second pass: Decompress 9 columns × 100M rows = 900M operations
* Total: 10.9B operations

That's a huge9x reductionin scan and I/O!

Why do we need to keep the filtering adaptive? Because sometimes bloom doesn't help:

* Join selectivity is high (most rows match anyway)
* Build side is large (bloom fills up, high false positive rate)
* Data is skewed (many duplicates saturate the filter)

## 2. Hash join bloom filter and the micro optimization

For hash joins we use a simpler, almost textbook-style bloom filter: insert values into the bloom filter at build phase, read it at probe phase before probing the hash buckets.

We landed on using a fixed 256KB bloom filter per join as a sweet spot between size and efficiency. Go bigger - waste the memory and overflow L2/L3 cache (cache misses hurt). Go smaller - might as well flip a coin.

Why fixed size? Predictable performance. No dynamic allocation. Compiler can optimize the hell out of it. Lock-free access. The last one is especially critical when we're talking about a concurrent performance-first database engine.

## The Problem: When too many bits tell less

All of the above works well only if the bloom filter is actually useful and doesn't lie too often. If it does - it is useless. In our engine we measure bloom filter performance with a simple threshold for number of bits set. What does that matter? To understand we need to dive deeper into the theory, and understand false positive rate of bloom filter

Why false positives?As we insert more elements (n), more bits get set to 1. Eventually, random elements will have all their k bits set to 1 by pure chance - even though they were never inserted. That's a false positive.

The occupancy problem: As we insert more elements, more bits get set to 1 and the filter gets saturated. For our single-hash (k=1) approach, that means the false positive rate climbs quickly - up to 10% and above - that's way too high!

### Let's Do Some Math (No Really, Stay With Me)

There's a well-known equation for false positive rate:

(1 - e(-kn/m))k

Where:

k = hash functionsm = bitsn = inserted elements.

You could just trust the formula. Or we could derive it in 30 seconds and actually understand why bloom filters break down:

The intuition: Every time we insert an element, we flip some bits from 0 to 1. Eventually, so many bits are set that random elements look like they were inserted - even though they weren't.

The math:

1. Probability a bit stays 0 after one hash: 1 - 1/m
2. After n elements with k hashes: (1 - 1/m)k n
3. As m gets large, (1 - 1/m)m≈ e-1[classic limit]
4. So, probability a bit stays 0: e-k n/m
5. Probability it's set: 1 - e-k n/m
6. False positive = all k bits randomly set: (1 - e-k n/m)k

Plug in our numbers(k=1, n=256K, m=2M): FP = 11.5%

Here is a really nice interactive tool where you can play around with different parameters of bloom filters to see how they scale:Bloom Filter Calculator

## Enough theory. Let's look at the code

Our old implementation:

static inline uint32_t idx32(HashKey32 h, uint32_t mask) { return (h >> 5) & mask; }
static inline uint32_t mask32(HashKey32 h) { return 1u << (h & 31u); }

inline void put(HashKey32 h) {
 const uint32_t m = mask32(h);
 __sync_fetch_and_or(&bits[idx32(h, idx32Mask)], m);
}

inline bool contains(HashKey32 h) const {
 const uint32_t m = mask32(h);
 return (bits[idx32(h, idx32Mask)] & m) != 0;
}

That implementation is simple, and it works. But it is way too simple, let's look for something better:

Goal: find something that's still fast as hell, but lies to us less often.

## Path to solution

We started experimenting with ideas to see how they perform

* Naive approach: Set two bits using two independent hash functions - terrible
* Alternative 1: store two bits in the same cache line - better, but still bad
* Alternative 2: split uint32 into halves. Use lower 16 bits for first bit position, upper 16 bits for 2nd bit position - better, we are getting there

Best solution: two bits, one uint32

Here's the insight: both bits live in the sameuint32variable. We use a single hash value to compute:

1. Which element in the array (16 bits of the hash)
2. Position of first bit within that element (5 bits)
3. Position of second bit within that element (5 more bits)

Leaving us with 6 unused bits.

Why this is beneficial:

1. Single memory access: read singleuint32
2. One atomic operation: set both bits with single atomic OR
3. Simple addressing: bit manipulation is cheap (few cycles), while memory is expensive

There is a minor trade-off: two bits are not truly independent anymore. This slightly increases collision probability. But the performance gain from one memory access crushes the theoretical disadvantage.

## The Results: 2x Better Accuracy, Minimal Cost

The new code is nearly identical in structure - just one extra bit in the mask. We shift and mask by 5 bits becauseuint32_thas 32 bit positions (2^5).

T bitLoc1(T& h) { return (h >> IDX_BITS) & MASK_5BIT; } // first 5-bit offset (0..31)
T bitLoc2(T& h) { return (h >> (IDX_BITS + 5)) & MASK_5BIT; } // next 5-bit offset (another bit)

void put(HashKey32 h) {
 const uint32_t idx = uint32Idx(h);
 const uint32_t mask = (1u << bitLoc1(h)) | (1u << bitLoc2(h));
 __sync_fetch_and_or(mBuf + idx, mask);
}

bool contains(HashKey32 h) const {
 const uint32_t data = mBuf[uint32Idx(h)];
 const uint32_t mask = (1u << bitLoc1(h)) | (1u << bitLoc2(h));
 return (data & mask) == mask;
}

The performance hit?Negligible. From our benchmarking:

* put(): 9.12 → 9.70 cyc/op (+6%)
* contains(): 1.97 → 3.16 cyc/op (+60% in percentage terms, +1.2 cycles in reality)

For context: even the "slower" version executes faster than a function call or branch mis-prediction. We're talking about a nanosecond.

The win?Massive.

* False positive rate: 11.68% → 5.69% (cut in half!)
* On a query scanning a terabyte table, that's avoiding decompression of ~60GB of data

Let me spell it out: we spend one extra nanosecond per row to avoid reading dozens of extra gigabytes.

I'll take that trade every single time.

## Takeaways

Two bits in oneuint32gave us 2x better bloom filter accuracy at essentially zero cost:

* Still one memory operation
* Still one atomic OR
* One more bit shift for creating the mask (but it's very cheap)
* 2.1x lower false positive rate (11.7% → 5.7%)

Adaptive filtering at the storage engine layer saves even more, allowing us to completely avoid decompressing rows that will not be needed. But because the first-pass decompression is still costly, optimizing this code path is not as trivial, so we did not touch it at that time. But when working on Floe, we will definitely use some of this gained knowledge for our smarter pushdowns.

## "Why Not Just Use 3 Bits? Or 4?"

Fair question. Using the same interactive tool:Bloom Filter Calculator

* 1 bit: 100k elements before getting high FP chance
* 2 bits: 253k elements - 2.5x more filter capacity without any real cost
* 3 bits: 306k elements - that's just 20% more capacity. At this point tradeoff becomes questionable
* 4+ bits: 320k elements - less than 5% capacity increase - not even worth it

The beauty of 2 bits: they fit in a singleuint32with minimal collisions.

It is the sweet spot between "too simple" and "too complex"

"But what about Cuckoo filters or XOR filters?"

Great structures! But they require dynamic resizing or more complex addressing. We wanted:

* Fixed size (256KB, done, no allocation)
* Lock-free concurrent writes
* Predictable L2/L3 cache behaviour

Two bits in a fixed bloom filter gave us all three.

## A Teaser: SIMD and Memory Bandwidth

We also wrote a version that checks 8 elements at a time using SIMD instructions. But that is a story for another day.

Author

 Makar


 Makar moved to Estonia from Ukraine in 2019 to study; and have been living and working there ever since. He enjoys coding and experimenting with fast things: memory allocators, hot loop optimizations, and graphics rendering. In his free time he loves to tinker with his home server, play single-player video games, and if Estonian weather allows - spend time in forests, mostly on his bike.
