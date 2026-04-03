---
title: Hare 0.26.0 released
url: https://harelang.org/blog/2026-02-13-hare-0.26.0-released/
site_name: lobsters
content_file: lobsters-hare-0260-released
fetched_at: '2026-02-14T06:00:33.451235'
original_url: https://harelang.org/blog/2026-02-13-hare-0.26.0-released/
date: '2026-02-14'
tags: plt, release
---

## Hare 0.26.0 releasedFebruary 13, 2026
 by Drew DeVault

I am proud to announce the release of Hare 0.26.0 today. 🎉 This is the latest
stable Hare release since last year’s release of Hare 0.25.2. This new release
includes a handful of new features and a modest number of bug fixes and minor
improvements.

We were also pleased to welcome Joe Finney as the latest Hare maintainer during
this release cycle! Joe has been a steadfast contributor and code reviewer for
Hare for some time now and it’s a pleasure to formally invite him to the
maintainer team.

Hare 0.26.0

Release notes

Hare 0.26.0

Download

 compiler:
harec-0.26.0.tar.gz

 standard library:
hare-0.26.0.tar.gz

 hare-update:
hare-update-0.26.0.0.tar.gz

Hare 0.26.0 is compatible with version 1.2 ofqbe.

New here? Hare is a systems programming language designed to be simple and
robust, using a static type system, manual memory management, and a minimal
runtime. You can learn about ithere.

## Release highlights

The big changes in this version of Hare include:

* Loop values and for..else
* DragonflyBSD support
* Explicit syntax for ignoring errors when needed
* Replacing @offset with fields named _ for padding structs
* Support for explicitly uninitialized variables

### Loop values and for..else

Joe Finney designed and implemented another change to for loops in Hare that’s
included in this release: they can now be used in expressions to compute a
result other thanvoid. There are two ways to supply a value to serve as the
result of a for loop: usingbreakwith a value, and adding anelsebranch at
the end of the loop.

Consider the following example, which fetches an item from a list matching a
key:

const

item

=

for

(
let

sample

..

items
)

{


if

(
item
.
key

==

key
)

{


break

item
;


};

}

else

{


fmt
::
errorfln
(
"Warning: item with key {} not found"
,

key
)
!
;


return
;

};

do_work
(
item
);

If the loop ends via break, the value you give to thebreakexpressions is
used as the result. Otherwise, if the loop completes without producing a result,
the else branch is used. In this example, we could have usedyield default_valueor something similar in the else branch to provide a value to
assign to item, but instead we just print an error and return – so the else
branch has the typenever.

There are all sorts of ways to use this construct, and I find myself reaching
for it a lot more often than I thought. Here’s a real-world example from the
scheduler in theHermeskernel:

// Choose an idle CPU, if one is available, or choose at random

const

cpu

=

for

(
let

cpu

&
..

arch
::
cpus
)

{


const

idle

=

atomic
::
casu8
(
&
cpu
.
idle
,

1
,

0
);


if

(
idle
)

{


break

cpu
;


};

}

else

{


const

rand

=

rand
::
u32n
(
&
rng
,

len
(
arch
::
cpus
)
:

u32
);


let

cpu

=

&
arch
::
cpus
[
rand
];


atomic
::
storeu8
(
&
cpu
.
idle
,

0
);


yield

cpu
;

};

This lets you construct more sophisticated logic around loops in Hare with a lot
more elegance than was possible before.

### DragonflyBSD

Thanks to the hard work of Michael Neumann, Hare now supportsDragonflyBSD!
This brings Hare’s platform coverage up to include Linux and the four most
common BSD flavors. Michael is sticking around as the maintainer of the new
subsystem, and we’re looking forward to the new port being tested and put to
good use by Dragonfly users.

### Ignoring errors

Hare makes error handling mandatory, but once in a blue moon you actually do
need to ignore those errors. The old workaround of casting to void to file off
theserial numbererror types from the result of your operation doesn’t work
anymore. Thanks to Sebastian, you can now assign to _ instead:

_

=

os
::
remove
(
"/some/file"
);

This makes the fact that you’re ignoring the error here more explicit. This
does not raise an assertion if an error occurs like!would – it just
proceeds normally.

### Padding structs with _

Another use of the underscore token was added in this release: the ability to
add unnamed struct fields for the purpose of adding explicit padding. Previously
one could use the@offsetkeyword to explicitly define the offset of your
struct fields – but this was quite labor intensive and cumbersome to use, and
required a pretty complicated implementation.

Joe Finney improved the situation for this release, and now one can simply
define nameless fields using _:

export

type

my_struct

=

struct

@packed

{


x
:

u32
,

// offset: 0


_
:

u8
,

// offset: 4


y
:

u64
,

// offset: 5

};

### Explicitly uninitialized variables

Until this release, Hare has required all variables (locals and globals) to be
initialized at the moment they are defined. This is almost always the right
thing to do, but sometimes it is useful or even necessary to declare a variable
without initializing it. If you pass a pointer to a variable into a function
that will initialize it for you, for instance, you might have to initialize it
with a meaningless value in order to fulfill that function’s contract. This gets
worse if the type does not have a default value, such as non-nullable pointer
types, when the object they will ultimately reference does not exist at the
moment of their declaration.

Drew DeVault fixed these issues by allowing one faced with such a scenario to
explicitly “initialize” the variable to@undefined:

let

x
:

my_object

=

@undefined
;

One can also “initialize” the remaining fields of a struct to undefined:

let

x

=

my_object

{


foo

=

1
,


bar

=

2
,


@undefined
...

// remaining fields undefined

};

The programmer is then responsible for ensuring that the variable is not read
from until it is initialized later on. The default behavior remains to require
initializers, since that is almost always the correct way to write your code,
but another escape hatch is available now for use-cases where the programmer
should verify the correctness of the program without the compiler’s help.
