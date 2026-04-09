---
title: An (almost) catastrophic OpenZFS bug and the humans that made it (and Rust is here too) · blog · despair labs
url: https://despairlabs.com/blog/posts/2025-07-10-an-openzfs-bug-and-the-humans-that-made-it/
site_name: lobsters
fetched_at: '2025-07-12T23:06:46.263932'
original_url: https://despairlabs.com/blog/posts/2025-07-10-an-openzfs-bug-and-the-humans-that-made-it/
date: '2025-07-12'
published_date: '2025-07-10T00:00:00+10:00'
tags: c, rust
---

A couple of weeks ago I fixed a nasty bug in this function in OpenZFS:

/*

 * This code converts an asize into the largest psize that can safely be written

 * to an allocation of that size for this vdev.

 *

 * Note that this function will not take into account the effect of gang

 * headers, which also modify the ASIZE of the DVAs. It is purely a reverse of

 * the psize_to_asize function.

 */

static

uint64_t

vdev_raidz_asize_to_psize
(
vdev_t

*
vd,
uint64_t
 asize,
uint64_t
 txg)

{


vdev_raidz_t

*
vdrz
=
 vd
->
vdev_tsd;


uint64_t
 psize;


uint64_t
 ashift
=
 vd
->
vdev_top
->
vdev_ashift;


uint64_t
 cols
=
 vdrz
->
vd_original_width;


uint64_t
 nparity
=
 vdrz
->
vd_nparity;

	cols
=

vdev_raidz_get_logical_width
(vdrz, txg);


ASSERT0
(asize
%
 (
1

<<
 ashift));

	psize
=
 (asize
>>
 ashift);

	psize
-=
 nparity
*

DIV_ROUND_UP
(psize, cols);

	psize
<<=
 ashift;


return
 (asize);

}

Take a moment to find it yourself, if you like. I’ll waffle for moment to push the solution down the page a bit so your eye isn’t immediately drawn to it. Suffice to say, it is both trivial and devastating.

In OpenZFS, any single piece of data we write has three notions of “size”:

* “logical”, the apparent size of the data to the user. This is your file contents, what you see when you runcator something.
* “physical”, the size of the data on disk after transforms like compression and encryption are applied.
* “allocated”, the actual amount of space a virtual device needs to actually store that data, including any metadata overheads, parity data, checksums, and whatever else.

To help the IO pipeline and the allocator, every virtual device driver has functions to convert between physical and allocated size._asize_to_psizereturns the maximum amount of physical data that can fit in the given allocated size, while_psize_to_asizereturns the minimum allocation necessary to contain the given physical size.

This one, obviously, is for theraidzvdev type. It’s a little complicated, because it has to consider parity and changes in the stripe width over time if the vdev has been expanded. The important thing is to not stuff it up - this is core disk allocation stuff, and there are no more checks or safeties to be had. If you return a too-small allocation for the physical data, then we’ll just write past the end of the allocation and silently trample data on disk.

Anyway, that’s enough waffling. Did you find the bug?

diff --git module/zfs/vdev_raidz.c module/zfs/vdev_raidz.c

index a9b12471cb..5941e645e7 100644

--- module/zfs/vdev_raidz.c

+++ module/zfs/vdev_raidz.c

@@ -2260,7 +2260,7 @@ vdev_raidz_asize_to_psize(vdev_t *vd, uint64_t asize, uint64_t txg)

 psize -= nparity * DIV_ROUND_UP(psize, cols);

 psize <<= ashift;

- return (asize);

+ return (psize);

 }

 /*

Yeah, me too. SeePR #17488for more detail.

Now, I made it a bit easy for you by showing you the troublesome function. I actually found it while testing a new feature I’m working on for a client, with some pretty aggressive allocator fragmentation settings in place, and I started getting weird errors, and wondered what I’d broken. It took almost two days to track it down.

Now in a lot of ways, it’s no big deal. Bugs happen, as do near-misses. It had been on the main development branch for a couple of months, but never on a real release.

Still, I’ve been thinking about it a lot, because I’d like to be able to notice this sort of thing ahead of time in the future. As it turns out, there’s not an easy way to catch this one in C. There’s no “cheap” annotation (eg-Wunused) that will notice it. Static analysers do notice thatpsizeis computed but never used, but those tools aren’t usually part of an everyday workflow for C because they tend to be expensive to run and easily find false positives (and we have a lot of them). It’s not impossible to do something, just no “set and forget” option.

With things like this I often think about what I’d do in Rust, which is a language I like ok but don’t get to use very much, and is most of my exposure to “proper” type systems. And I’m sure there’s lots we could do, but at least, we could describe those two types of sizes as being separate distinct things, so they can’t be accidentally swapped:

struct

PhysicalSize
(
u64
);

struct

AllocatedSize
(
u64
);

fn

psize_to_asize
(psize:
PhysicalSize
) ->
AllocatedSize
 {


let
 asize
=
 AllocatedSize(psize.
0

<<

1
);

 asize

}

fn

asize_to_psize
(asize:
AllocatedSize
) ->
PhysicalSize
 {


let
 psize
=
 PhysicalSize(asize.
0

>>

1
);

 asize

}

And then the compiler would deal with it:

error[E0308]:
mismatched
 types


-
->
src
/
main.rs:
11
:
5


|

9

|

fn

asize_to_psize
(asize:
AllocatedSize
) ->
PhysicalSize
 {


|

------------
 expected
`
PhysicalSize
`
 because of
return

type

10

|

let
 psize
=
 PhysicalSize(asize.
0

>>

1
);

11

|
 asize


|

^^^^^
 expected
`
PhysicalSize
`
, found
`
AllocatedSize
`

And this gets me thinking about a thing I have often heard from C programmers pushing back on the use of tools or language features that would improve the quality of their software, along the lines of “competent programmers don’t need these things, they should just get good”.

I am well past the point in my life where I engage with that sort of noise in any good faith, because if your answer to any perceived failing in a person is “just try harder”, you are either woefully inexperienced or a just a dick. But even if we were taking it good faith, what kind of “try harder” or “get better” are we talking about here? Theoriginal changewas written by an extremely competent and experienced C programmer, and reviewed by two others of equal skill. This is not to say that they can’t improve, but rather, these are not the kinds of things that humans can really “get better” at in any meaningful way. We are fuzzy pattern-matching engines, these aren’t the kind bugs we can easily see. And we don’tneedto: we build tools for that!

I also think there’s a bit of a blind spot in the way Rust is sold to C programmers, or at least, in the feeling I get as an old, experienced and competent C programmer reading and listening to people talk about Rust. The sort of “gateway” problem I usually hear is about null pointer dereferences and errors of their kind. Don’t get me wrong; they’re easy to write and can be hard to debug in any sufficiently complex C program. They just aren’t the kind of bugs I worry very much about, because when you hit them, your program tends to crash. Not great, but not silent.

The size conversion bug though? That shitterrifiesme, because if you deploy it and you hit it, you may not know for a while until you start to get weird IO errors, and by then it’s too late - your data isgone. Worrying about that sort of thing literally kept me up at night during my years as a storage admin, and it seems the body never forgets that, because I still lose sleep worrying about introducing bugs that will hurt other people the same way.

So, am I making a point? Not sure. It’s definitely not “abandon C” or “rewrite it in Rust”; those aren’t practical. I guess, mostly, it’s just to remember that we’re all just humans, trying our best, and effort is not much of a predictor of competence, and we’re also really good at building tools, and if they’re available to you you should at least consider if they can help to maximise your strengths and minimise your weaknesses, whatever they may be.

And, maybe, I wish I had lot more time to write Rust. I like it even though it infuriates me, and I would like to work out which parts of my frustration come from lack of experience, and which come from it being a poor fit for some of the tasks I use it for.
