---
title: Index, Count, Offset, Size
url: https://tigerbeetle.com/blog/2026-02-16-index-count-offset-size/
site_name: hackernews_api
content_file: hackernews_api-index-count-offset-size
fetched_at: '2026-02-21T19:10:57.507956'
original_url: https://tigerbeetle.com/blog/2026-02-16-index-count-offset-size/
author: matklad
date: '2026-02-18'
description: Insights, updates, and technical deep dives on building a high-performance financial transactions database.
tags:
- hackernews
- trending
---

Wherein we make progress towards solving one of the most vexing
problems of Computer Science — naming things.

I am at a point in my career where the bulk of my bugs are stupid — I
simply fail to type in the code I have in my mind correctly. In
languages with shadowing (like Rust), I will fail to use a shadowed
variable from the outer scope. In languages without shadowing (like
Zig), I will use the wrong version of a variable.

Pests like these are annoying, so I am always on the lookout for
tricks to minimize the probability of bugs. One of the best possible
tricks is of course strong static typing. Types are good at preventing
me from doing stupid things by accident. But types have limitations. The
text of a well-typed program is a two-in-one artifact — a specification
of behavior of a machine (the algorithm), and a proof that the behavior
is not unacceptable. Zero cost abstractions are code without behavior,
just proofs!

The art of skillful typing lies in minimizing verbosity of the proof,
while maximizing the amount of unwanted behaviors ruled out, weighted by
the probability and the cost of misbehavior. But this ratio is not
always favorable — the code can be so proof-heavy that it becomes
impossible to understand what it actuallydoes!

There’s one particular cranny where types don’t seem to usefully
penetrate yet: indexing and associated off-by-one errors.

If you don’t need indexingarithmetic, you can usenewtype
patternto prevent accessing oranges with apple-derived indexes. You
can even go further and bind indexes tospecificarrays, using,
e.g.,Gankra
trick, but I haven’t seen that to be useful in practice.

If, however, youcomputeindexes, you need to be extra
careful to stay in bounds of an array, and need to be mindful that the
maximum valid index is one less than the length of the array. While we
don’t solve this problem perfectly at TigerBeetle, I think we have a
naming convention that helps:

Thanks@marler8997for the illustration idea!

We consistently usecountwhenever we talk about the
number of items, andindexto point to a particular item.
Thepositive
invariantisindex < count. Consistency is the trick
— there are certain valid and invalid ways to combine indexes and counts
in an expression, and, if there’s always an_indexor a_countsuffix in the name, wrong combinations immediately
jump out at you, dear reader, even if you don’t understand the specifics
of the code.

In low-level code you often need to switch between a well-typed
representation[]Tand raw bytes[]u8. To not
confuse the two index spaces, the “count of bytes” is always called asize. By definition,

size
=

@sizeOf
(T)
*
 count;

Andoffsetis the bytewise counterpart ofindex.

We don’t uselengthin our code, as its meaning is
ambiguous. Ruststr::lenis the byte-sizeof
the string, but Python’slen(str)is thecountof Unicode code-points!

Here’s an example of the naming convention in action fromNodePool:

pub

fn
 release(pool
:

*
NodePool
,
 node
:
 Node)
void

{


comptime

assert
(meta
.
Elem(Node)
==

u8
);


comptime

assert
(meta
.
Elem(
@TypeOf
(pool
.
buffer))
==

u8
);


assert
(@intFromPtr(node)
>=
 @intFromPtr(pool
.
buffer
.
ptr));


assert
(

 @intFromPtr(node)
+
 node_size
<=

 @intFromPtr(pool
.
buffer
.
ptr)
+
 pool
.
buffer
.
len

 );


const
 node_offset
=

 @intFromPtr(node)
-
 @intFromPtr(pool
.
buffer
.
ptr);


const
 node_index
=


@divExact
(node_offset
,
 node_size);


assert
(
!
pool
.
free
.
isSet(node_index));

 pool
.
free
.
set(node_index);

}

You can see that thenode_indexcalculation is correct
mechanically, just from the names of the variables.

And here’s anindex/countexample from ourewahimplementation:

pub

fn
 decode(

 source
:
 []
align
(
@alignOf
(Word))
const

u8
,

 target_words
:
 []Word
,

)
usize

{


assert
(source
.
len
%

@sizeOf
(Word)
==

0
);


assert
(disjoint_slices(
u8
,
 Word
,
 source
,
 target_words));


const
 source_words
=
 mem
.
bytesAsSlice(Word
,
 source);


var
 source_index
:

usize

=

0
;


var
 target_index
:

usize

=

0
;


while
 (source_index
<
 source_words
.
len)
{


const
 marker
:

*
const
 Marker
=


@ptrCast
(
&
source_words[source_index]);

 source_index
+=

1
;


@memset
(

 target_words[target_index
..
][
0
..
marker
.
uniform_word_count]
,


if
 (marker
.
uniform_bit
==

1
)
~
@as
(Word
,

0
)
else

0
,

 );

 target_index
+=
 marker
.
uniform_word_count;

 stdx
.
copy_disjoint(


.
exact
,

 Word
,

 target_words[target_index
..
][
0
..
marker
.
literal_word_count]
,

 source_words[source_index
..
][
0
..
marker
.
literal_word_count]
,

 );

 source_index
+=
 marker
.
literal_word_count;

 target_index
+=
 marker
.
literal_word_count;


}


assert
(source_index
==
 source_words
.
len);


assert
(target_index
<=
 target_words
.
len);


return
 target_index;

}

Note well that theindex/countconvention synergizes
with two other TigerStyle shticks. We use “big endian naming”, where
qualifiers are appended as suffixes:

source
source_words
source_index

And we try to make sure that dual names have the same length:

source
target

The code aligns itself, and makes the bugs pop out:

source_index
+=
 marker
.
literal_word_count;

target_index
+=
 marker
.
literal_word_count;

Of course, a simple naming convention by itself won’t make software
significantly better. But grains of sand add up to Dune: there’s no one
trick to get rid of the bugs, but you can layer your defenses to
exponentially decrease the probability of a failure.

Enjoyed this post?Add our RSS feed.
