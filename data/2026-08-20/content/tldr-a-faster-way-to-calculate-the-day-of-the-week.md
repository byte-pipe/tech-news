---
title: A faster way to calculate the day-of-the-week
url: https://www.benjoffe.com/fast-day-of-week
site_name: tldr
content_file: tldr-a-faster-way-to-calculate-the-day-of-the-week
fetched_at: '2026-08-20T19:30:48.993356'
original_url: https://www.benjoffe.com/fast-day-of-week
author: Ben Joffe
date: '2026-08-20'
description: A range of fast modulus techniques that beat compiler output
tags:
- tldr
---

You need to enable JavaScript to run this app.

# A faster way to calculate theday of the week

## A range of fast modulus techniques that beat compiler output

17 August 2026

Converting aday-count ("rata-die")to theday-of-the-week (“weekday”)sounds like it should be so trivial, that there's almost nothing to say about it. But, as it turns out, when we look under the hood, this is a surprisingly complex problem.

Throughout this article I will present a range ofreally fastfunctions to solve this problem, tuned for different use cases (throughput vs latency, different platforms etc.). Each(full range 32-bit algorithm)outperforms existing solutions, and many have a latency of just a single multiplication plus two cycles. A surprising result is presented: the weekday can be computed in ISO format ([1‥7] instead of [0‥6]), with the exact same instructions, just with tweaked constants (and zero speed penalty).

To give you a taste of the insanity, I'll highlight my favourite function here, this crazy looking 3-instruction sequence (plus a constant load) is accurate over thefull signed 32-bit range(it may not be the lowest latency one, but has the highestthroughputfor x86):

 Unix Weekday [0‥6]
 ISO Weekday [1‥7]
Given: 
input
 
(rd = signed 32-Bit Unix day-count)
; Compute 
weekday [0‥6]
:
1. mov eax, 613566756; Constant Load:u32M= (1 << 32) / 7
2. imul ecx;rd*M(u32a= low bits, i32b= high bits)
3. lea eax, [eax-1828716544+edx*4];u32r=a+ 4 *b+ (Z = 0x93000000)
4. shr eax, 29;weekday=r>> 29

You don't need prior understanding of assembly to follow this blog post.By the end, you will understand why this code above works.

Visualisation of how the function above produces the desired output. The constant on line-3 acts as a rotation angle.

This article is for people interested in low level bit manipulation, optimising high performance date libraries / database engines, compiler authors, and crazy people in general. The techniques used heregeneralisetox % (2^N - 1), and new fast modulus techniques are introduced forother divisorssuch asx % 24andx % 60- applicable to timekeeping.

If you're just here to copy/paste and benchmark code in your library, you can jump to the "Function Explorer" which has all code examples on this page available to copy/paste from C++.

Approx. Relative Speeds of FastestFull Range 32‑BitAlgorithmsAs tested on AMD Ryzen 9 and Apple M4 Pro processors(smaller numbers = faster)Seebenchmark sectionfor specific results.

Others
(double-mod, Rust:rem_euclid, Hinnant)
~1.5-3+×
Neri
(2024)
1×
New Algos
(2026)
~0.3-0.5×

Article Sections:

* Simple Approaches
* Hinnant
* Neri
* The Unreasonably Fast Mul-Add-Shift AlgorithmFast Full Range via 64-Bit Widening
* Fast Full Range via 64-Bit Widening
* Fast Full Range (Variant 1:Shifts)
* Fast Full Range (Variant 2:Two Muls)
* Fast Full Range (Variant 3:High + Low Bits)
* The Function Explorer
* Generalisation
* Closing Thoughts
* Annexure A. Benchmark Results
* Annexure B. Proof of modulus by power-of-2 padding

## Simple ApproachesDeep link

Given:rd=rata-die(day-count, signed 32-Bit int), with epoch1970-01-01= Thursday (4)   —   Then:

Double-mod (languages with signed "%", eg. C/C++)
1. weekday= ((rd%7) + 7 + 4)%7
Languages with special positive-mod (eg. Rust)
1. weekday= (rd + 4)POSMOD7

—   Where:weekday∈[0‥6](0 = Sunday)

This is what I would recommend in most non-library code where maintenance is more important than micro-optimisation.Note that the Rust example overflows for the highest 4 inputs, but assume we don't care about those.

The addition of4(or11 = 7 + 4) is due to the Unix epoch1970-01-01being aThursday. If you number your weekdays differently, or use a different epoch, this might vary.

These "simple approaches" do the job, but they are quite slow, even in the case of Rust with its positive-mod function (rem_euclid), which translated back into C-style pseudocode, looks like the following:

Rust's rem_euclid (compiled pseudocode equivalent) 
View on Godbolt 
1. i32a= (i64(rd+ 4)*-1840700269) >> 32//Note: This pseudocode assumes
2. i32b=rd+ 4 +a//that overflow of signed addition
3. i32c= (b >> 2) + (u32(b) >> 31)//is defined as per Rust
4. i32d=rd-c*7//and two's complement, whereas
5. i32e=d+ 4//for C/C++ it is undefined.
6. u32weekday=e>= 0 ?e: d + 11

A lot more steps than you might have expected, right?

## HinnantDeep link

Howard Hinnant's technique (2014) was adopted by many date libraries (seeoriginal article).

Hinnant's Algorithm (bit-size independent)
Range: INT32_MIN → INT32_MAX − 4
1. weekday=rd>= -4 ? (rd + 4)%7
2. : (rd + 5)%7 + 6

This approach appears designed for simplicity and flexibility. It is the only algorithm from here onwards that does not rely on sign casting or overflow, nor is it bit-width specific. It will be the same logic for 8-bit through to 64-bit.

Hinnant points out in his article that this covers the full signed 32-bit range, except for the highest 4 inputs, which in C/C++ results in undefined behaviour at this extreme (> 5.8M years in the future). In practice, on 2's complement machines, it usually still works for those values, but this is not guaranteed by the compiler.

Although this is not presented asvery fastin the opening bar-chart, it's very fast on Raspberry Pi Zero (and presumably also on older chips).

## NeriDeep link

As usual, Cassio Neri's work is the modern (full range) gold standard. In 2024 Neri published a very clean full-range solution to this problem (seepost):

Cassio Neri: 32-bit version
(Range: Full signed 32-bit)
1. weekday= (u32(rd) + (rd>= 0 ? 4 : 0))%7
Cassio Neri: 64-bit version
(Range: Full signed 64-bit)
1. weekday= (u64(rd) + (rd>= 0 ? 4 : -5))%7

If you want something pretty fast, full-range, and not too low-level, then this is the function for you.

Neri's primary motivation was to overcome the overflow in Hinnant's algorithm. The real trick to avoiding overflow here is the cast from signed to unsigned before doing any work. Interestingly, in the 32-bit version, an addition of zero applies for negative numbers due to the property:2^32 % 7 = 4, and thus the addition of4is already baked-in. Note that if this were not zero (eg. if you don't treat Sunday as0), it would be no slower. To calculate what this 2nd constant should be for different bit-widths, use:- ((3 + 2^BIT_WIDTH) % 7)

Seems like it should be pretty much as fast as possible right?To speed things up, we'll need to look at the assembly. GCC and Clang both emit assembly that computes the following:

Neri, 32-bit (compiled pseudocode equivalent) 
View on Godbolt 
1. u32a=u32(rd) + (rd>= 0 ? 4 : 0)
2. u32b= ((u64)a*613566757) >> 32//≈ a / 7 (rough quotient)
3. u32c= (((a-b) >> 1) +b) >> 2//corrected quotient
4. u32weekday=a-c*7//alternatively: a + c - (c << 3)

Note that line-3 contains four serially dependent operations, just to correct the initial approximation toa / 7. Correction terms like these are required because7is anuncooperative divisor, requiring more than 32-bits in its magic reciprocal multiplier which doesn't fit in a 32-bit register.

There is a faster way, using the "libdivide" technique presented byridiculousfish in 2011. It eliminates the whole correction line by making a saturating-increment to the input and using the round-down multiplier. We could use that, and it measures around 10% faster for me, but there are even faster ways, which we'll first explore by reducing our range requirement...

## The Unreasonably FastMul-Add-ShiftAlgorithmDeep link

It turns out we can calculate the weekday over a restricted-but-useful range with just a multiplication, addition, and a right-shift:

 Unix Weekday [0‥6]
 ISO Weekday [1‥7]
32-bit version (restricted range)
Input range: 
-89,434,796
 to 
89,522,175
Valid dates: 
-242,895-11-06 (Mon: 1)
 to 
247,073-05-23 (Fri: 5)
1. const u32M= (1 << 32) / 7 + 1//613,566,757
2. const u32Z= 0x94920000//2,492,596,224
3. weekday= (u32(rd)*M+Z) >> 29

For a C++ version, see#fn=32unix_narrowin the Function Explorer.

Just three operations. Clearly this is going to run fast, but how on Earth does it work?

Visualisation of how the function to the left produces the desired output. The constant “Z” acts as a rotation angle.

Modulus usually requires many more steps. The reason we can get away with so few operations is due to7being a Mersenne number, i.e. of the form:2N− 1. With such numbers, we can utilise identities like:N % 7 = floor(N * 8 / 7) % 8(seeAnnexure Bfor the proof of this equality).

We then implement* 8 / 7as multiplication by~1.142857...approximated by a single multiplication and right-shift. Usually mul-shifts take the high bits, but we'll take the low bits, ensuring the right-shift is exactly3less than the register-size. The final% 8is then given for free, by virtue of only 3 bits remaining.

By adding the value ofZto the result before the right-shift, we effectively rotate the output values to align with the Unix epoch being a Thursday. A value ofZ = 0x90000000rotates it such that the output values are ISO formatted [1..7], with a balanced input range within exactly±89,478,489(1/24th of 32-bit space). For the Unix format [0..6] variant, I choseZ = 0x94920000, which gives anearly-but-not-perfectly balancedrange, but comes with a minor speed advantage on ARM, by virtue of the low two bytes being zero.

The diagram to the right of the code shows visually how this multiplier strikes the 8 different segments of the circle (top 3 bits), skipping one value each cycle. The arrows "fan out" slightly; this is a representation of how our multiplier is only an approximation of2^29 * 8 / 7. Eventually this fanning out causes an incorrect return value, hence the restricted range.

This algorithm is super fast everywhere, but particularly fast on ARM, where the multiply and addition are fused into a singleMADDassembly operation. Additionally, many operations on ARM allow a fused right-shift, so there's a good chance that downstream code also fuses with the>> 29term.This means in practice that it might compile to effectively a single ARM assembly operation!

An alternative visual guide to the validity of this technique is via the table below, where you can see that the output value111 (7)is skipped each cycle in Unix mode, and the output value000is skipped in ISO mode:

 Unix Weekday [0‥6]
 ISO Weekday [1‥7]
rata_die
Weekday
a = u32(rata_die
* 613566757)
r = u32(
 a + 0x94920000
(2,492,596,224)
r as Binary
r >> 29
Correct?
▲
 Scroll Up 1 Week
↥
 Go to Max Week
5
2
3,067,833,785
1,265,462,713
010
01011011011010110110110111001
2
Pass
4
1
2,454,267,028
651,895,956
001
00110110110110010010010010100
1
Pass
3
0
1,840,700,271
38,329,199
000
00010010010001101101101101111
0
Pass
2
6
1,227,133,514
3,719,729,738
110
11101101101101001001001001010
6
Pass
1
5
613,566,757
3,106,162,981
101
11001001001000100100100100101
5
Pass
0
4
0
2,492,596,224
100
10100100100100000000000000000
4
Pass
-1
3
3,681,400,539
1,879,029,467
011
01111111111111011011011011011
3
Pass
-2
2
3,067,833,782
1,265,462,710
010
01011011011010110110110110110
2
Pass
-3
1
2,454,267,025
651,895,953
001
00110110110110010010010010001
1
Pass
▼
 Scroll Down 1 Week
↧
 Go to Min Week
▲
▼

If your date library only needs to support a range smaller than ±242,000 years, then you can probably just use this technique noted above. An example is the RustJiff date/time librarywhich supports a range of ±10,000 years. Theadoptionof this algorithm yielded a 40% speed-improvement for upstream functions such asnth_weekday_of_month, which previously used Rust'srem_euclidfunction.

The rest of this article will be aimed at achieving similar speed for full range date libraries.

### Fast Full Range via 64-Bit WideningDeep link

The easiest way to extend the range to the full 32-bit input domain is to widen to 64-bit:

 Unix Weekday [0‥6]
 ISO Weekday [1‥7]
64-bit widen version
Input range: Full 32-bit: 
-2
31
 to 
2
31
-1
Valid dates: 
-5,877,641-06-23 (Tue: 2)
 to 
5,881,580-07-11 (Fri: 5)
1. const u64M= 0x2492492493000000//ceil(240/ 7) × 224
2. const u64Z= 0x9400 << 48
3. weekday= (u64(rd)*M +Z) >> 61

For a C++ version, see#fn=32unix_widenin the Function Explorer.

Visualisation of how the function to the left produces the desired output. The constant “Z” acts as a rotation angle.

The64-bit widen versionhas a tweaked multiplier, instead ofceil(264/ 7)I have usedceil(240/ 7) × 224. Again, low bits have been zeroed for more compact ARM assembly: using trial and error to find the minimum number of bytes required.

Notice the arrows in the circle-chart no longer fan-out? That is due to the extra bits of precision afforded by this technique.

TheFunction Explorerhas a variant adjusted for 64-bit inputs(see#fn=64unix_narrow), where the non-rounded multiplier is used for a wider range, covering over one quadrillion years(that ought to be enough for anybody).

### "The Unreasonably Fast" - Prior Work

While researching for this article, I found that I am not the first to recognise this Mersenne number trick. A technique very much like this first appeared inHacker's Delight(§10–20,Remainder by Multiplication and Shifting Right). The book has examples like the following:

Hacker's Delight - Unsigned N mod 7 technique (partial range)
(Accurate over 3.125% of unsigned 32-bit range)
Given: 
x
 Integer 
[0 .. 134,217,734]
  —  Then:
1. u32n=u32(x* 613566756) >> 29//Round-down multiplier
2. x_mod_7=n& (i32(n - 7) >> 31)//Correction to remap 7 to 0

The book uses the round-down multiplier in all cases, rather than the round-up multiplier. Not only does this multiplier give a worse range in many cases (including mod 7), but it necessitates the correction on line-2, which removes a chunk of the speed advantage of this technique.

-- [20 August 2026 - Update] I have been informed that Neri was also familiar with this trick, and implemented correction-free round-up and round-down variants of the Mersenne trick in32-bit (restricted-range)and64-bit.

I am glad I came across this book [Hacker's Delight] though, as I learned the following technique to expand to full-range:

Hacker's Delight - Unsigned N mod 7 technique (full range)
Given: 
x
(unsigned 32-bit integer)
  —  Then:
1. u32n=u32(x* 613566756+ (x>> 1) + (x>> 4)) >> 29
2. x_mod_7=n& (i32(n - 7) >> 31)//Correction to remap 7 to 0

The highlighted correction terms relate to the fractional part of the "ideal" multiplier2^32 / 7 = 613566756.5714...This fractional part is exactly4 / 7. The corrections(x >> 1) + (x >> 4) = 1/2 + 1/16 =0.5625closely approximate the "ideal" shortfall.

We are going to make use of these corrective terms, but instead of using that correction mapping on line-2, we'll continue to use ourZ-rotation.

## Fast Full Range (Variant 1:Shifts)Deep link

Using the correction terms from Hacker's Delight (along with around-downmultiplier) we get the following:

 Unix Weekday [0‥6]
 ISO Weekday [1‥7]
Full range 32-bit version (Variant 1)
Input range: Full 32-bit: 
-2
31
 to 
2
31
-1
Valid dates: 
-5,877,641-06-23 (Tue: 2)
 to 
5,881,580-07-11 (Fri: 5)
1. const u32M= (1 << 32) / 7//613,566,756
2. const u32Z= 0x95000000//2,499,805,184
3. const u32a=u32(rd)*M+Z
4. const u32b= (rd>> 1) + (rd>> 4)
5. weekday= (a+b) >> 29

For a C++ version, see#fn=32unixin the Function Explorer.

Visualisation of how the function to the left produces the desired output. The constant “Z” acts as a rotation angle.

In theory, this can sometimes be as low-latency as a single multiplication plus two cycles. Whether it is in practice will depend on how well the compiler optimises the assembly output (GCC seems best), and the performance characteristics of the target processor.

The key is that unlike with standard division-by-7, the computation of the corrections, such as:b = (rd >> 1) + (rd >> 4)are dependent only on the input value, not on any prior computations. This allowsbto be calculated while the multiplicationrd * Mis underway.

Modern x86 processors aresuperscalar, and can usually perform a shift at the same time as a multiplication. Since multiplications usually take 3 cycles,rd * Mandbare ready at the same time. TheLEAassembly instruction allows adding these two resultsandZin one step (although on some chips this might be two cycles).

This superscalar aspect can be confirmed by observing benchmarks with and without the calculation ofb, which show the same latency results in many cases from my testing. Now, if your date library has a smaller date-range, you might still prefer one of the reduced-range 32-bit algorithms; not because they have reduced latency, but because they can have higherthroughput, meaning your code can be doing something else while the multiplication occurs, such as starting a time-of-day computation etc.

Superscalar x86 Assembly Steps
Step
Computation 1
Computation 2
1
a = rd * M
t
1
 = (rd >> 1)
2
mul-latency
t
2
 = (rd >> 4)
3
mul-latency
b = t
1
 + t
2
4
a + b + Z
 
(LEA instruction)
5
... >> 29

The situation is even better on ARM.Many ARM assembly instructions allow a fused right-shift to occur in the same instruction cycle. This allows the computation ofbto be made in just two-cycles. As such, the processor does not need to have any superscalar features in order to hidebwithin the shadow of the multiplication.

This has been observed on the Raspberry Pi Zero, which again has the same latency whether or notbis included in the function.

Finally, since the algorithm ends with a right-shift, if your subsequent code does something likeaddor subtract the returned value (as is often the case when computing the Nth weekday of a month etc.), then the final shift also gets fused with that subsequent operation.

ARM Optimal Assembly Steps
Step
No parallel steps other than overlapping multiplier
1
a = rd * M + Z
(MADD instruction)
2
t
1
 = (rd >> 1)
mul-latency
3
b = t
1
 + (rd >> 4)
 
(fused shift-add)
mul-latency
4
a + b
5
... >> 29
 
(potentially fused with next operation)

### Medium Range Variant

If therd >> 4term is dropped, leaving onlyrd >> 1, then the function can have slightly higher throughput, and a range of around ±1.46M years. You can find tuned variants of this nature in the Function Explorer. See#fn=32unix_medium.

## Fast Full Range (Variant 2:Two Muls)Deep link

There is a way to get a potentiallyeven fasterresult. We recall that multiplication is slow, but has a high throughput in cases where the multiplications do not depend on each other. By replacing the terms:(rd >> 1) + (rd >> 4)with a hand-rolled division, we get a new fast full-range variant, this timeoptimised forthroughputinstead oflatency.

This function below switches to the round-up multiplier, so instead ofadding4 / 7, we'll aim tosubtract3 / 7.

 Unix Weekday [0‥6]
 ISO Weekday [1‥7]
Full range 32-bit version (Variant 2)
Input range: Full 32-bit: 
-2
31
 to 
2
31
-1
Valid dates: 
-5,877,641-06-23 (Tue: 2)
 to 
5,881,580-07-11 (Fri: 5)
1. const u32M= (1 << 32) / 7 + 1//613,566,757
2. const i32N=i32(M * 4)//-1,840,700,268
3. const u32a=u32(rd)*M+N//Note: Z = N
4. const u32b=u64(rd)*N>> 32//≈ rd * -3 / 7
5. weekday= (a+b) >> 29

For a C++ version, see#fn=32unix_v2in the Function Explorer.Note:i32(M * 4)overflows to give a negative multiplier, resulting in subtraction of3 / 7 *rd.

Visualisation of how the function to the left produces the desired output. The constant “Z” acts as a rotation angle.

Even a simple in-order processor such as the 32-bit ARM chip in Raspberry Pi Zero can overlap these multiplications. We can see how by viewing the steps in the table below. Notice that, although there are two columns in each table, there is never a row with two computations on it?

x86 Optimal Assembly Steps
Step
Computation 1
Computation 2
1
rd * N
2
a = rd * M
mul-latency
3
mul-latency
mul-latency
4
mul-latency
b = ... >> 32
5
a + b + u32(N)
  
("LEA")
6
... >> 29
ARM Optimal Assembly Steps
Step
Computation 1
Computation 2
1
rd * N
2
a = rd * M + u32(N)
 
("MADD")
mul-latency
3
mul-latency
mul-latency
4
mul-latency
-
5
a + (b >> 32)
 
(fused shift-add)
6
... >> 29

### Latency vs Throughput

Notice that the tables above have 6-rows, whereas the algorithm in the previous section(Variant 1)has 5-rows?But conversely, they have one fewer operation overall in each case (X86: 6 → 5; ARM: 5 → 4).This suggests better throughput at the cost of latency, but it depends largely on the target platform and how well the compiler does its job.

### Compiler Performance

* For x86: Unfortunately only GCC takes advantage of the high-throughput 3-component LEA instruction.
* For ARM: Only Clang produces the optimal 4-instruction sequence (plus const loads),andonly if forced to by insertingasm("" : "+r"(a));.

Despite suboptimal compiler assembly, these variants are all still lightning fast, perhaps just 1-2 cycles slower than possible.

Variant 2 - Full Range (GCC x86 Assembly)
1. movsxd rax, edi; Register shuffling
2. imul edi, edi, 613566757
3. imul rax, rax, -1840700268
4. sar rax, 32
5. lea eax, [rdi-1840700268+rax]
6. shr eax, 29
7. ret

View x86 on Godbolt

Variant 2 - Full Range (
Forced
 Clang ARM Assembly)
1. mov w8, #18725; Const load
2. mov w9, #9364; Const load
3. movk w8, #9362, lsl #16; Const load
4. movk w9, #37449, lsl #16; Const load
5. madd w8, w0, w8, w9
6. smull x9, w0, w9
7. add x8, x8, x9, lsr #32
8. lsr w0, w8, #29
9. ret

View ARM on Godbolt

## Fast Full Range (Variant 3:High + Low Bits)Deep link

Finally, we get to the example shown at the start of this article, full-range in three x86 assembly operations:

 Unix Weekday [0‥6]
 ISO Weekday [1‥7]
Given: 
input
 
(rd = signed 32-Bit Unix day-count)
; Compute 
weekday [0‥6]
:
1. mov eax, 613566756; Constant Load:u32M= (1 << 32) / 7
2. imul ecx;rd*M(u32a= low bits, i32b= high bits)
3. lea eax, [eax-1828716544+edx*4];u32r=a+ 4 *b+ (Z = 0x93000000)
4. shr eax, 29;weekday=r>> 29

A C++ implementation of this is available as#fn=32unix_v3in the Function Explorer below.

Recall why we are adding correction terms: due to the multiplier being unable to represent the fractional part of:2^32 / 7 = 613566756.5714...

Visualisation of how the function above produces the desired output. The constant on line-3 acts as a rotation angle.

We have handled this by:

1. using theround-downmultiplier with correction:(rd >> 1) + (rd >> 4) = 1/2 + 1/16 =0.5625≈ 4/7
2. using theround-upmultiplier with a multiplier correction that effectivelysubtracted3/7ths of rd.

An alternative is to revert to theround-downmultiplier, but instead of patching together an approximation ofrd * (4. / 7.), we will find an existing approximation tord / 7and then multiply it by4.

Where can we find such an "existing approximation" toN / 7?Well it's been there all along, it's thehigh 32-bit resultof what we've always been calculating:rd * M:

* Instead of calculatingu32(rd) *M...
* one calculatesw = u64(rd) *M[operation #1]the low result is thena= u32(w)- extracted for "free" in 32-bit x86 by accessing "eax" registerand high result isb=w>> 32- extracted for "free" in 32-bit x86 by accessing "edx" registerthen:r=a+ 4 *b+Z- a single LEA operation*[operation #2]and finally:weekday=r>> 29[operation #3]
* the low result is thena= u32(w)- extracted for "free" in 32-bit x86 by accessing "eax" register
* and high result isb=w>> 32- extracted for "free" in 32-bit x86 by accessing "edx" register
* then:r=a+ 4 *b+Z- a single LEA operation*[operation #2]
* and finally:weekday=r>> 29[operation #3]

*the terma + 4 * b + Zfits the format of a single x86 "LEA" operation. If you haven't seen this operator before, it probably looks like a super-power. It's very specific in what it can handle. It can take two registers, multiply one of them by (1, 2, 4 or 8), and sum them together with another constant. Originally designed to help with memory access patterns, it is available to use and abuse in low level algorithms.

Unfortunately, as before, the compilers I tested don't produce the optimal assembly (View x86 on Godbolt), which is why the introduction presented it in raw assembly, rather than as source code.

## The Function ExplorerDeep link

You have seen many code examples throughout this article, this widget below combines them all in a single "Function Explorer", where you can configure the bit-width, epoch, range and variant. There are a total of 280 hand-tuned permutations, and they are all fully tested.

Input: 
Signed
Unsigned
   
64-bit
32-bit
16-bit
8-bit
Range: 
Full 
(11.8My)
Medium 
(2.9My)
Narrow 
(489Ky)
Variant: 
V1 (2 shifts)
V2 (mul)
V3 (high-bits)
64-Bit Widen
Output: 
[0‥6]
[1‥7]
  
where epoch:
 
−
+
1. // MIT LicenseClick to show
2. //
3. // Copyright (c) 2026 - Ben Joffe <https://www.benjoffe.com/>
4. //
5. // Permission is hereby granted, free of charge, to any person obtaining a copy
6. // of this software and associated documentation files (the "Software"), to deal
7. // in the Software without restriction, including without limitation the rights
8. // to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
9. // copies of the Software, and to permit persons to whom the Software is
10. // furnished to do so, subject to the following conditions:
11. //
12. // The above copyright notice and this permission notice shall be included in
13. // all copies or substantial portions of the Software.
14. //
15. // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
16. // IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
17. // FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
18. // AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
19. // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
20. // OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
21. // SOFTWARE.
23. // Given: rd = rata-die (day-count), Unix epoch 1970-01-01: 4
24. // Compute: Day of week: (rd + 4) POS_MOD 7
25. // Range: Full signed 32-bit
26. // Output: [0..6]
27. // Min Date: -5,877,641-06-23 (Tue: 2)
28. // Max Date: 5,881,580-07-11 (Fri: 5)
29. //OptionalRef:https://www.benjoffe.com/fast-day-of-week#fn=32unix
30. inline uint8_tget_weekday_32unix(int32_trd) {
31. const uint32_tM= (1ull << 32) / 7;//613,566,756
32. const uint32_tZ= 0x95000000;//2,499,805,184
33. const uint32_ta=uint32_t(rd)*M+Z;
34. const uint32_tb= (rd>> 1) + (rd>> 4);
35. returnuint32_t(a+b) >> 29;// top 3 bits
36. }

The chart above visualises how inputs map from an idealised angle around the circle, to 8 segments (representing the top 3-bits of the final computation).It will animate upon form changes.

Testing

All 280 permutations of the above function can be generated into a single file for testing purposes. This is then copy/pasted into the test repo at:https://github.com/benjoffe/fast-world-calendars(the repo already has a copy).Functions of bit-width 8, 16 and 32 are exhaustively tested over the stated range.Functions in the 64-bit range would be prohibitively slow to exhaustively test, so are instead tested in four 1-billion-date chunks: around zero, up to max, down to min, and a random selection.

⬇ Download All Functions
 
⬇ Download Test Commands

## GeneralisationDeep link

The techniques presented in this article generalise to modulus of other Mersenne numbers, i.e. of the form2^N - 1, such asD = 3, 15, 31..., but only so long asD < 2^(BitWidth/2-1). That meansD < 32,768in 32-bit space. That's probably enough for most practical use cases, but for other Mersenne numbers, an alternative option exists.

The function below is that first solution I found to the general day-of-week problem (which builds directly on Neri's):

Full-range 32-bit method 
(First Attempt)
1. u32n=u32(rd) + (rd>= 0 ? 4 : (9 << 28))//New range-compression trick
2. u32q= (u64)n*2454267027 >> 34//Round-up magic: ceil(2^34/7)
3. weekday= (n+q) & 7//New power-of-2 padding trick

There are two tricks here:

Trick #1
1. u32n=u32(rd) + (rd>= 0 ? 4 :(9 << 28))//New range-compression trick
2. u32q= (u64)n*2454267027 >> 34//Round-up magic: ceil(2^34/7)

This is similar to the start ofNeri, but instead of adding0for negative inputs, we are adding a big number:9 × 228or0x90000000. We are also using a round-up magic multiplier to implement correction-free division by 7.

We can use this large addition instead of0, because:

1. This number is equal to4 (mod 7)(the previous value of0can be considered as2^32 = 4 (mod 7))
2. It maps negative numbers in the range of[-231..-1]to a contiguous block of numbers in unsigned 32-bit space:[228.. 9×228-1], meaning there's no wraparound point to worry about.

Why do this? Well, the standard round-up magic for divide-by-7 is only accurate over 80% of the 32-bit input range. This is why the clean version of Neri's algorithm outputs extra assembly to correct the initial estimated quotient for division-by-7, and the reason that a libdivide-style technique was suggested previously as a potential optimisation.

With this new technique,rdhas been mapped to a smaller range than it would otherwise, the overall value ofnis within range of[4..9×228-1]. This range is smaller than 80% of the 32-bit input range, meaning we can use the standard round-up magic number for division. Compilers are not smart enough to recognise the reduced input range, requiring us to hand-roll the division via the custom mul-shift.

So, why9 × 228instead of a smaller number?It is true that we can pick many other choices for this addition, the smallest option would be231+ 2 = 0x80000002.Using that constant would be just as fast on x86, however ARM processors would take two assembly operations to load this constant.9 × 228is a neat number with the lower 16-bits zeroed out, which means it is loaded in only 1 assembly operation for ARM.

Now onto the next step:

Trick #2
1. weekday= (n+q) & 7//New power-of-2 padding trick

This is computing(n + n / 7) % 8instead of the traditionaln - n / 7 * 7, replacing a multiplication with a bit-mask.

I refer to this trick as the"Nundinal Map"(similar to the "Julian Map" introduced in article 1).Nundinalrefers to the ancient Roman 8-day week.Essentially, every time a 7-day week elapses, we pad the numbernwith an additional phantom day.It is not too hard to see thatn / 7will bump 7 to 8, and 14 to 16 etc.Once the number has been mapped to this fake 8-day week, we can extract the true weekday by just inspecting the lowest 3-bits.

It is pretty clear why this would be faster on x86, the alternative usually compiles asn + q - (q << 3), which is 3 cycles instead of 2.It is less obvious why this is faster on ARM, as ARM has a fused multiply-add operation calledMADDwhich can performn + q * -7in one assembly instruction with a 3-cycle latency, but a throughput of just 1 cycle. The reason it's also fast here is because on ARM, this line partly fuses with the previous code's line, which can performn + (w >> 34)(wherewis the prior multiply result)in a single assembly instruction. Thus, this final line is a true single-cycle operation on ARM: just the bit-mask.

I have not seen this particular transformation before.

The mathematical basis for this is:

x
mod
(
2
N
−
1
)
=
(
x
+
⌊
x
2
N
−
1
⌋
)
mod
(
2
N
)

Which is a special case of the following formula, wherec=1andD=2N−1:

x
mod
D
=
(
x
+
c
⌊
x
D
⌋
)
mod
(
D
+
c
)

The proof of this general formula is stated inAnnexure B. - Proof of modulus by power-of-2 padding.

This technique is not just restricted to Mersenne numbers...

### Fast Modulus of Divisors in the form 2N- 2K

The general formula above can be used for numbers of the form2N−2K.

Some interesting use cases in this form include:

* Calculating hours:x % 24 = (x + ((x / 24) << 3)) & 31
* Calculating min/sec:x % 60 = (x + ((x / 60) << 2)) & 63

From my research, these formulas appear novel. They are particularly fast on x86 processors due to theLEAassembly instruction, which can multiply a value by 2, 4 or 8, as well as add another variable, in a single cycle.

Interestingly, even the standard approach ofx - x / 7 * 7is technically a special-case of this general formula wherec=232−7:(x + (x / 7) * (2^32 - 7)) % (2^32). I.e. in 32-bit 2's complement:-7 = 2^32 - 7

## Closing thoughtsDeep link

Why did I bother with all this?Well, if you can't tell by now, I just find this stuff all terribly interesting. The 7-day week is the oldest part of our calendar, and the one with the most truly global reach, surpassing the scope of even the Gregorian calendar. One can imagine that if we undergo civilisational collapse, or if we spread to new planets, the calendar may change, but the 7-day week might not.

The rabbit hole that led to all this was exploring optimisations for cultural calendars, like the Coptic calendar and in particular the Hebrew calendar, which uses the 7-day week more than once in its computation of general dates. Some future blog posts will cover those.

The very next article in this series will be onfast time-of-day, using the "Fast Modulus" techniques above.

If you found this interesting, you shouldfollow me on Xto get notified when I publish more date and algorithm related articles.

Revision history:

* 27 June 2026 - Soft release draft
* 17 August 2026 - First release
* 20 August 2026 - Amendment to"The Unreasonably Fast" - Prior Worksection to note Neri's prior work.
No, not a real artefact...

## Annexure A - Benchmark Results

Exhaustive tests of the ranges asserted in this article can be verified via the testcase code:https://github.com/benjoffe/fast-world-calendars.

The same repository is used for benchmarking, where a large set of random dates are loaded into memory and tested. Latency mode feeds the results into the next computation via bitwise-XOR to ensure no parallel execution:

git clone git@github.com:benjoffe/fast-world-calendars.git
cd fast-world-calendars
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j
./build/bin/weekday_bench
./build/bin/weekday_bench -latency
./build/bin/weekday_bench -batch

The above commands were used with the-repeat=5flag, and for Raspberry Pi Only:-count=256(others are 65536 random dates). Themedianresults were saved to the table below.

The numbers in parenthesis in the table represent the nanoseconds elapsed to process an entire batch, and as with all benchmarks in this series, the relative speed ratios are calculated by first subtracting the "baseline", which removes the overhead of the loop.Smaller numbers = faster.

Note: these benchmarks measurescalar performance. The Narrow, Medium, and V1 variants stick to plain 32-bit math (low bits only) and vectorize cleanly, so in a tight loop over many dates (which gets auto-vectorised) they'd likely pull further ahead than shown here on many platforms. V2 and V3's extra 32-bit-high-half math can add overhead in some SIMD chips.

 Throughput
 Latency
Algorithm:
base-line
naive
rust
Hinnant
Neri
*Narrow
New Medium
*Full 64-Widen
New Full (V1)
New Full (V2)
New Full (V3)
(V3) forced asm
"1st attempt"
MacBook Pro 2024 (MacOS 15.6.1)
Apple M4 Pro
Compiler: Apple clang 17.0.0
-
(14640)
2.78x
(59014)
1.32x
(35634)
2.84x
(59889)
1.00x
(30587)
0.17x
(17388)
0.23x
(18387)
0.18x
(17465)
0.39x
(20788)
0.35x
(20266)
0.25x
(18624)
0.36x
(20331)
0.48x
(22304)
AMD Ryzen 9 9950X3D
Ubuntu 24.04.3 LTS
Compiler: 
GCC
 14.2.0 (x86_64)
-
(5746)
1.84x
(72955)
-
2.92x
(112071)
1.00x
(42185)
0.27x
(15478)
0.42x
(21012)
0.33x
(17870)
0.55x
(25608)
0.59x
(27395)
0.50x
(24010)
0.48x
(23191)
-
AMD Ryzen 9 9950X3D
Ubuntu 24.04.3 LTS
Compiler: 
Clang
 18.1.3 (x86_64)
-
(11556)
2.30x
(90156)
1.72x
(70542)
3.90x
(144980)
1.00x
(45787)
0.23x
(19556)
0.31x
(22334)
0.28x
(21301)
0.47x
(27721)
0.53x
(29548)
0.41x
(25722)
0.41x
(25738)
0.57x
(30965)
MacBook Pro 2016 (MacOS 12.7.6)
Intel Core i7 @ 2.7 GHz
Compiler: Apple clang 14.0.0
-
(23209)
1.84x
(171955)
1.46x
(141247)
3.71x
(323632)
1.00x
(104158)
0.39x
(54856)
0.30x
(47357)
0.39x
(54907)
0.49x
(63104)
0.44x
(58613)
0.85x
(91688)
0.28x
(45984)
0.56x
(68224)
Raspberry Pi Zero
32-Bit ARM
Raspbian GNU/Linux 13 (trixie)
Compiler: GCC 14.2.0 (armv6l)
-
(6222)
1.30x
(59627)
1.03x
(48624)
0.96x
(45630)
1.00x
(47294)
0.75x
(37029)
0.75x
(37016)
0.85x
(41138)
0.70x
(34961)
0.85x
(41140)
0.55x
(28802)
0.56x
(29086)
0.65x
(32954)

* "Narrow" and "Full 64-Widen" first implemented by Neri - x86 benchmarks should be reflective of his approach. The benchmarked variants of these are the versions using the tuned constants for ARM in this article, so will be slightly faster than Neri's on ARM.

## Annexure B. Proof of modulus by power-of-2 paddingDeep link

For any integerx, positive divisorD, and non-negative integerc, where⌊xD⌋denotes floor division:

(1)
x
mod
D
=
(
x
+
c
⌊
x
D
⌋
)
mod
(
D
+
c
)

Proof.WritexmodD=rin terms of quotient and remainder:x=Dq+r,  whereq=⌊xD⌋andr=xmodD:

(2)
x
+
c
⌊
x
D
⌋
=
D
q
+
r
+
c
q
=
(
D
+
c
)
q
+
r

Takingmod(D+c)of both sides:

(3)
(
x
+
c
⌊
x
D
⌋
)
mod
(
D
+
c
)
=
(
(
D
+
c
)
q
+
r
)
mod
(
D
+
c
)

Since(D+c)qis an exact multiple ofD+c, it is eliminated by the modulus, andris not eliminated due tor=xmodD<D<D+c:

(4)
(
x
+
c
⌊
x
D
⌋
)
mod
(
D
+
c
)
=
r
=
x
mod
D
 
 
 
◻

The value ofcis a free parameter. The useful choices are positive values that makeD+ca power of 2, so thatmod(D+c)becomes a free bitwiseAND.

Thec=1case appears in Warren'sHacker's Delight(§10–20,Remainder by Multiplication and Shifting Right), which presents:

x
mod
D
=
⌊
D
+
1
D
⋅
x
⌋
mod
(
D
+
1
)

Warren demonstrates fast approximations of the fixed-point constant(D+1)/Dvia multiply-and-shift as used throughout this article.The direct formx+⌊x/D⌋is not analysed in Hacker's Delight.