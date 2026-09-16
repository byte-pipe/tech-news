---
title: Vectorized and performance-portable Quicksort | Google Open Source Blog
url: https://opensource.googleblog.com/2022/06/Vectorized%20and%20performance%20portable%20Quicksort.html
site_name: hnrss
content_file: hnrss-vectorized-and-performance-portable-quicksort-goog
fetched_at: '2026-09-16T21:54:50.016772'
original_url: https://opensource.googleblog.com/2022/06/Vectorized%20and%20performance%20portable%20Quicksort.html
date: '2026-09-16'
description: We're sharing open source code that can sort arrays of numbers about ten times as fast as the C++ std::sort
tags:
- hackernews
- hnrss
---

### Vectorized and performance-portable Quicksort

#### Thursday, June 2, 2022

Today we're sharing open source code that can sort arrays of numbers about ten times as fast as the C++ 
std::sort
, and outperforms state of the art architecture-specific algorithms, while being portable across all modern CPU architectures. Below we discuss how we achieved this.
First, some background. There is a recent trend towards columnar databases that consecutively store all values from a particular column, as opposed to storing all fields of a record or "row" before those of the next record. This can be faster to filter or sort, which are key building blocks for SQL queries; thus we focus on this data layout.
Given that sorting has been heavily studied, how can we possibly find a 10x speedup? The answer lies in SIMD/vector instructions. These carry out operations on multiple independent elements in a single instruction—for example, operating on 16 float32 at once when using the AVX-512 instruction set, or four on Arm NEON:
If you are already familiar with SIMD, you may have heard of it being used in supercomputers, linear algebra for machine learning applications, video processing, or image codecs such as 
JPEG XL
. But if SIMD operations only involve independent elements, how can we sort them, which involves re-arranging adjacent array elements?
Imagine we have some special way to sort, for instance 256 element arrays. Then, the 
Quicksort algorithm
 for sorting a larger array consists of partitioning it into two sub-arrays: those less than a "pivot" value (ideally the median), and all others; then recursing until a sub-array is at most 256 elements large, and using our special method for sorting those. Partitioning accounts for most of the CPU time, so if we can speed it up using SIMD, we have a fast sort. 
Happily, modern instruction sets (Arm SVE, RISC-V V, x86 AVX-512) include a special instruction suitable for partitioning. Given a separate input of yes/no values (whether an element is less than the pivot), this "compress-store" instruction stores to consecutive memory only the elements whose corresponding input is "yes". We can then logically negate the yes/no values and apply the instruction again to write the elements to the other partition. This strategy has been used in an 
AVX-512-specific Quicksort
. But what about other instruction sets such as AVX2 that don't have compress-store? 
Previous work
 has shown how to emulate this instruction using permute instructions.
We build on these techniques to achieve the first vectorized Quicksort that is portable to six instruction sets across three architectures, and in fact outperforms prior architecture-specific sorts. Our implementation uses 
Highway's
 portable SIMD functions, so we do not have to re-implement about 3,000 lines of C++ for each platform. Highway uses compress-store when available and otherwise the equivalent permute instructions. In contrast to the previous 
state of the art
—which was also specific to 32-bit integers—we support a full range of 16-128 bit inputs.
Despite our single portable implementation, we reach record-setting speeds on both AVX2, AVX-512 (Intel Skylake) and Arm NEON (Apple M1). For one million 32/64/128-bit numbers, our code running on Apple M1 can produce sorted output at rates of 499/471/466 MB/s. On a 3 GHz Skylake with AVX-512, the speeds are 1123/1119/1120 MB/s. Interestingly, AVX-512 is 1.4-1.6 times as fast as AVX2 - a worthwhile speedup for zero additional effort (Highway checks what instructions are available on the CPU and uses the best available ones). When running on AVX2, we measure 798 MB/s, whereas the prior state of the art optimized for AVX2 only manages 699 MB/s. By comparison, the standard library reaches 58/128/117 MB/s on the same CPU, so we have managed a 
9-19x
 speedup depending on the type of numbers.
Previously, sorting has been considered expensive. We are interested to see what new applications and capabilities will be unlocked by being able to sort at 1 GB/s on a single CPU core. The Apache2-licensed 
source code
 is available on Github (feel free to 
open an issue
 if you have any questions or comments) and our 
paper
 offers a detailed explanation and evaluation of the implementation (including the special case for 256 elements).
By Jan Wassenberg – Brain Computer Architecture Research

Labels:

SIMD

 ,
 

Sorting

 
 

 
 

 