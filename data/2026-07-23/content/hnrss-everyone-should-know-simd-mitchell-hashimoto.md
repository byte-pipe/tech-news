---
title: Everyone Should Know SIMD – Mitchell Hashimoto
url: https://mitchellh.com/writing/everyone-should-know-simd
site_name: hnrss
content_file: hnrss-everyone-should-know-simd-mitchell-hashimoto
fetched_at: '2026-07-23T18:58:40.612467'
original_url: https://mitchellh.com/writing/everyone-should-know-simd
date: '2026-07-22'
published_date: '2026-07-22T00:00:00.000Z'
description: Everyone should know SIMD
tags:
- hackernews
- hnrss
---

# Mitchell Hashimoto

# Everyone Should Know SIMD

July 22, 2026

SIMDhas a reputation for being complex. I've met many very good software engineers
who dismiss it as something too complex to learn or a niche optimization
meant for only the highest-performance software, not useful in everyday
programming.

I think that's wrong. SIMD can be simple to understand1, and common
"process N values at a time" SIMD code to speed up a naive for loop
almost always follows the same general shape. Once you learn the basics,
writing SIMD is just about as easy as a for loop. And when it's not, it's
usually a good sign to skip it for now.

Every developer should know at least that much SIMD.

This post uses Zig for examples but is a general piece that
applies to any programming language. Support for SIMD instructions
varies by programming language and I hope that more programming languages
expose these generic concepts in the future!

I hate that I have to do this for every post now, but I also want
to note this was completely hand-written with no AI assistance.

Table of Contents
* Background: What Is SIMD?
* The Common Shape
* A Real Example
* Step 1: Broadcast Constants
* Step 2: Loop One Vector at a Time
* Step 3: Perform the SIMD Operation
* Step 4: Reduce the Vector Result
* Step 5: Finish with the Scalar Tail
* Recap: The Common Shape
* Why Can't the Compiler Do This?
* Everyone Should Know SIMD

## Background: What Is SIMD?

If you already know what SIMD is, skip this section.

SIMDallows a CPU to operate on multiple values in parallel. For example,
instead of comparing one byte at a time, a CPU can compare
4, 8, or even more bytes with a single instruction.

If you ever see loops like this in your code:

for
 (
byte in bytes
)
 {
 /* ... */
 }

for
 (
character in string
)
 {
 /* ... */
 }

for
 (
value in array
)
 {
 /* ... */
 }

There is an opportunity to use SIMD. SIMD turns those into this:

for
 (
8
 byte chunk in bytes
)
 {
 /* ... */
 }

This results in a localized speedup that directly maps to the parallelism:
you process data 4x, 8x, or even faster.

The only real requirement for this to pay off is that you need to be
regularly processing a large enough number of bytes. If you're doing
these for loops across data that is only ever a handful or dozens of bytes,
it's not worth it. But if this is iterating over hundreds, thousands,
millions of bytes, the payoff will be huge.

That's the basics. Projects such assimdutfandsimdjsontake this to an extreme and use SIMD techniques that can
be difficult to understand. But you do not need to write algorithms like
those to benefit from SIMD. The common case is dramatically simpler.

## The Common Shape

The common "process N values at a time" SIMD code follows the same five steps:

1. Broadcast any constants you need and initialize vector accumulators, if any.
2. Loop over input one vector-width chunk at a time.
3. Perform the comparison or arithmetic across all lanes in parallel.
4. Reduce or store the vector result as needed.
5. Handle the remaining elements with a scalar tail. A scalar tail is just yournormalloop from before vectorizing, but it only processes the remainder
that doesn't fit into a full vector.

As you do this more and more, you'll begin to naturally decompose every
for loop into these five steps and writing SIMD becomes nearly as natural
as writing a scalar loop.

## A Real Example

Let's look at a real example from Ghostty. We'll look at the scalar
implementation, the SIMD implementation, and then map it back to the
common shape above.

I have a slice of decoded codepoints that I want to consume until I see a value
at or below0xF(a C0 control character).2Terminals aremostlyplain characters to be printed, so we try to batch all those together.
So this loop finds the end of the next printable run as quickly as possible.

The scalar loop is one line:

while
 (end 
<
 cps
.
len 
and
 cps[end] 
>
 0xF
) end 
+=
 1
;

It processes one codepoint at a time. It is easy to understand.

Here is the generic vector version with no CPU-specific intrinsics3and no comments. I will explain it in detail later.

if
 (simd
.
lanes
(
u32
)) 
|
lanes
|
 {

 const
 V 
=
 @Vector
(lanes
,
 u32
)
;

 const
 threshold
:
 V 
=
 @splat
(
0xF
)
;

 while
 (end 
+
 lanes 
<=
 cps
.
len) 
:
 (end 
+=
 lanes) {

 const
 values
:
 V 
=
 cps[end
..
][
0
..
lanes]
.
*
;

 const
 greater_than_threshold 
=
 values 
>
 threshold
;

 if
 (
@reduce
(
.
And
,
 greater_than_threshold)) 
continue
;

 const
 mask
:
 std
.
meta
.
Int
(
.
unsigned
,
 lanes) 
=
 @bitCast
(greater_than_threshold)
;

 end 
+=
 @ctz
(
~
mask)
;

 break
;

 }

}

while
 (end 
<
 cps
.
len 
and
 cps[end] 
>
 0xF
) end 
+=
 1
;

12 more lines of code.

This can improve the loop's throughput by up to 4x with ARM NEON (including
Apple Silicon), 8x with AVX2 (most modern x86 CPUs), and 16x with AVX-512
(some Intel CPUs and AMD Zen 4 and newer).

In real-world end-to-end throughput from terminal program to finalized
terminal state on an AVX2 Intel desktop, this was more like a 5x speedup.
You always lose some of the ideal speedup due to the other stuff around the
SIMD code, but... that's still 5x!

Okay, now I understand that those 12 lines are going to look really
alien to someone not familiar with the concepts. So now let's back up
and explain it step by step, mapping it directly to the shape previously
mentioned.

## Step 1: Broadcast Constants

Let's start with the first three lines:

if
 (simd
.
lanes
(
u32
)) 
|
lanes
|
 {

 const
 V 
=
 @Vector
(lanes
,
 u32
)
;

 const
 threshold
:
 V 
=
 @splat
(
0xF
)
;

simd.lanes(u32)is a helper in Ghostty that returns the number ofu32values the target CPU can process at once. These individual values are calledlanes. On ARM this returns 4, AVX2 returns 8, and AVX-512 returns 16. If the
target doesn't have a vector size we want to use, it returnsnulland we skip
all of this code and do zero SIMD work.

@Vector(lanes, u32)creates the vector type. Iflanesis 8, thenVis a
single value containing eightu32values that the CPU can operate on in
parallel. And so on.

Finally, we need to compare every value to0xF. A vector comparison requires
a vector on both sides, so@splat(0xF)copies, orbroadcasts,0xFinto
every lane. The result is a vector that looks like this:

{ 0xF, 0xF, 0xF, 0xF, 0xF, 0xF, 0xF, 0xF }

This is step 1: prepare the vector type and broadcast any constants. Some
algorithms also initialize a vector accumulator here, but this algorithm
doesn't need one.

## Step 2: Loop One Vector at a Time

Next, we loop over one complete vector at a time:

while
 (end 
+
 lanes 
<=
 cps
.
len) 
:
 (end 
+=
 lanes) {

 const
 values
:
 V 
=
 cps[end
..
][
0
..
lanes]
.
*
;

Iflanesis 8, we only enter the loop when at least eight values remain.
Inside the loop, we load those eight values into the vectorvalues. At the
end of every loop,end += lanesmoves forward by eight values instead of one.

The requirement for acompletevector is important. If only five values
remain, we can't load an eight-lane vector. There are various tricks to handle
this, but we do the easy thing and handle them via our scalar tail, which I'll
explain later in step 5.

This is step 2: load and loop over the input one vector-width chunk at a time.
You can see the lane-count speedup here!

## Step 3: Perform the SIMD Operation

Now we perform the comparison:

const
 greater_than_threshold 
=
 values 
>
 threshold
;

Bothvaluesandthresholdare vectors, so this maps to a vector
operation (a literal vector CPU instruction). The one>compares every
lane invaluesto every corresponding lane inthreshold. If there are
eight lanes, this is equivalent to performing the scalar comparisoncps[end] > 0xFeight times, but it does it in one CPU instruction instead.4

The result is another vector with one boolean per lane. Conceptually, it looks
something like this:

values: { 0x41, 0x42, 0x43, 0x0A, 0x44, 0x45, 0x46, 0x47 }

threshold: { 0xF, 0xF, 0xF, 0xF, 0xF, 0xF, 0xF, 0xF }

greater_than_threshold: { true, true, true, false, true, true, true, true }

This is the actual SIMD operation. There is no explicit inner loop. The>operator applies to every lane in parallel.

Comparisons are only one example. This could be addition, multiplication,
minimum, maximum, or any other operation supported by the vector type. The
point is the code still has the same shape.

## Step 4: Reduce the Vector Result

We now have a vector of booleans, but the original loop needs to know the
location of the first value at or below0xF.

First, let's handle the common case where every value is above0xF:

if
 (
@reduce
(
.
And
,
 greater_than_threshold)) 
continue
;

@reduce(.And, ...)combines every boolean usingandand returns a single
boolean. If every lane istrue, wecontinueand process the next
vector. In our example, lane 3 isfalse, so@reducereturnsfalseand we
fall through to find exactly which lane failed.

If any lane isfalse, then we need to find exactly which lane failed:

const
 mask
:
 std
.
meta
.
Int
(
.
unsigned
,
 lanes) 
=
 @bitCast
(greater_than_threshold)
;

end 
+=
 @ctz
(
~
mask)
;

break
;

@bitCastturns the vector of booleans into an integer with one bit per lane.
A1bit means the value was greater than0xFand a0means it wasn't. We
invert the mask so failed comparisons are1, and then@ctzcounts the
number of zero bits before the first failure. That count is the index of the
first failing lane.

We add that index toendand break because we found the control character.

Using the same values from step 3, we can see this transformation per lane:

values: { 0x41, 0x42, 0x43, 0x0A, 0x44, 0x45, 0x46, 0x47 }

greater_than_threshold: { true, true, true, false, true, true, true, true }

mask: { 1, 1, 1, 0, 1, 1, 1, 1 }

~mask: { 0, 0, 0, 1, 0, 0, 0, 0 }

@ctz(~mask)counts three zero bits before the first1, so it returns3.
Adding3toendpoints it at lane 3, which contains0x0A, the first
control character.

This is step 4: reduce the vector result into whatever the original algorithm
needs. This is also the step that varies the most between algorithms. A sum
might reduce a vector accumulator into a single number. A transform might
store the entire vector to an output buffer. Our scan turns the vector into a
bit mask so it can find one specific lane.

## Step 5: Finish with the Scalar Tail

After the vector loop, we run the exact scalar loop we started with:

while
 (end 
<
 cps
.
len 
and
 cps[end] 
>
 0xF
) end 
+=
 1
;

If the input length isn't an exact multiple of the vector width, this processes
the remaining values. For example, an eight-lane vector loop leaves anywhere
from zero to seven values for this loop. This is called thescalar tail.

This loop also handles CPUs wheresimd.lanes(u32)returnsnull. In that
case we skip all of the SIMD code and the scalar loop processes the entire
input. The original implementation remains both the fallback and the tail.

That's step 5. It's just the normal loop.

## Recap: The Common Shape

Let's map the entire implementation back to the five steps:

1. @splat(0xF)broadcasts the comparison value into every lane.
2. Thewhileloop loadslanesvalues at a time.
3. values > thresholdcompares every lane in parallel.
4. @reduce,@bitCast, and@ctzfind the first failed comparison.
5. The original scalar loop handles the remainder and unsupported CPUs.

The details in step 4 initially take some time to understand, but the overall
shape is straightforward. And steps 1, 2, 3, and 5 tend to look nearly
identical across completely different algorithms.

Whenever you see afor (byte in bytes), this is the shape you'll map to.

## Why Can't the Compiler Do This?

Sometimes it can! Compilers canauto-vectorizesimple loops,
particularly regular arithmetic loops without complex control flow. You
should always compile the scalar version with optimizations and see what your
compiler produces before manually writing SIMD.

But compilers are severely limited in what they can auto-vectorize
and are in general very poor at it.
Auto-vectorization has been an active area of compiler research for decades,
andrecent researchstill begins from the
observation that production compilers regularly miss vectorization
opportunities. This isn't a problem I expect to disappear soon.

More importantly, when this loop matters enough for me to care about a 5x
speedup, I want the vectorization to be explicit and predictable. I don't want
an unrelated code change or compiler update to quietly turn it back into a
scalar loop.

## Everyone Should Know SIMD

Every developer should be able to recognize the opportunity and, most
importantly, shouldnot be scared of SIMD. If you see a
hot loop scanning, comparing, counting, or transforming a large amount of
contiguous data, you should be able to imagine processing it a vector-width
chunk at a time.

This post demonstrates that these common cases follow a very regular pattern
that you quickly get used to. And with good language support,
you don't need to know any assembly or CPU-specific quirks to get easy
improvements.

Everyone should know SIMD enough to do this.5

## Footnotes

1. Very impressive projects like simdutf and simdjson use extremely
complex SIMD tricks to achieve their goals. But this isn't
what I'd consider "everyday SIMD."↩
2. C0 controls extend beyond0xF. This is the cutoff Ghostty uses
for this specific code path; ESC and other control-sequence handling
happens elsewhere.↩
3. Generic vectors remove the CPU-specific syntax, not CPU-specific
code generation. Zig still lowers these operations to the instruction
set enabled for the target. Ghostty falls back to scalar code when it
can't choose a supported vector width.↩
4. The comparison itself is one vector operation. Loading the vector,
reducing the result, and locating the failed lane require additional
instructions. The important part is that we're doing multiple
comparisons at once.↩
5. This post was based on aLobsters comment I wrote.↩

July 22, 2026