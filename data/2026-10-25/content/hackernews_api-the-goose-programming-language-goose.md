---
title: The Goose Programming Language · Goose
url: https://aardappel.github.io/goose/
site_name: hackernews_api
content_file: hackernews_api-the-goose-programming-language-goose
fetched_at: '2026-10-25T14:49:12.826486'
original_url: https://aardappel.github.io/goose/
author: bobbydigitales
date: '2026-10-24'
description: The Goose Programming Language
tags:
- hackernews
- trending
---

# The Goose Programming
Language

A memory-safe systems language with no heap allocator, garbage
collector, or lifetime annotations. In this repository's benchmarks,
Goose runs faster than C++ and Rust while using less memory.

Tutorial·Reference·Specification·Packages·Samples·Benchmarks·Standard library

Goose has syntax familiar to C and Rust programmers, butthere is no heap. Every dynamic value lives inline on a
data stack managed by the compiler. Growth advances a pointer, and
memory is freed when its scope ends. The language's type and lifetime
rules make this memory model safe to use.

 

## Why Goose

* Faster than C++ and than safe Rust, while memory
safe.Over sixteen benchmarks Goose runs at 3.3x the speed of
idiomatic C++, 1.16x hand-optimized C++ and 1.12x the best safe Rust, on
1.9x, 1.3x and 1.2x less memory (results). These gains come from Goose's
data layouts and memory model.
* No allocator, no GC, no reference counting, no
destructors.Memory is a handful of data stacks that the
compiler assigns statically. Freeing a million-element structure is one
store, however deeply it nests.
* Growth preserves references.A reference into a
growing array stays valid for as long as the array does. You keep typed
references where C++ mustreserveand safe Rust usesu32indices in the corresponding benchmarks.
* Memory safe with zero annotations.No lifetime
syntax, no aliasing or exclusivity rules, nounsafe. The
compiler infers what every reference is rooted in and rejects references
that could outlive their owners.
* Nested data stays inline.A string, an array of
strings, a record with variable-size fields and an array of those
records are each one contiguous block with no pointer in it. A record
that is 160 bytes and an allocation in C++ is 29 bytes and none in
Goose.
* Enums that cost what they hold.Variable-mode ADTs
give each value its own variant's size rather than the largest one's: 4x
less memory and 2x the speed of a Rustenumon the
benchmark that exercises it.
* Links narrower than pointers.A relative reference
stores a typed, checked link as a 1, 2 or 4-byte offset. Structures
built from them are position independent, so your data structure is
already its file format: saving is a write, loading is a read plus a
verification pass that rejects hostile bytes.
* Everything is built in place, guaranteed.A value
is constructed at its final destination through any depth of calls.items.push(parse(line))writes the parsed record straight
into the array, and returning a growable array by value costs
nothing.
* Returns across multiple calls.return err from loadreturns from a function any number of
frames up, statically checked, with no unwinder, noResulttype and no?on every call.
* Threads that share nothing.A worker is compiled as
a separate program with its own memory, and flat values cross typed
queues as amemcpy. Data races, locks, atomics and memory
orderings do not exist in the language.
* Generics and higher-order functions with no
overhead.An untyped parameter is generic. Function values are
compile-time entities, soxs.filter() { it > 0 }compiles to the loop it looks like and builds its result straight into
its destination.
* Plain C in, plain C out.Goose compiles to one C
file, so it runs wherever a C compiler does and calls C directly throughextern fn. The bundled TinyCC backend compiles and runs a
program in-process, with no build step.

Thetutorialwalks through all of
this by example, thereferencecovers
the whole language topic by topic, thespecificationhas the exact rules, and
thebenchmarkshave the numbers, losses
included.

## Features

This section focuses on what distinguishes Goose. Thetutorialexplains these features in more
detail, and thesamplesshow them in
thirty-one complete programs.

### One memory
model: stacks, and scope exit is the free

A program has the native call stack, static data and N data stacks,
where the compiler works out N. A data stack is a large address-space
reservation with a bump pointer, and there is no other memory. At most
one resizable value is live per stack and it is always on top, so growth
never moves anything and never checks a capacity. All of this is proved
at compile time; the runtime tracks only the bump pointers.

for
 round 
in
 
3
 {

 
var
 scratch
:
 
u8
[
>..
] 
=
 []
;
 
// grow-only: growth is a pointer bump

 
for
 i 
in
 
100000
 { scratch
.
push
((i 
%
 
256
) 
as
!
 
u8
)
;
 }

 
print
(
"round "
,
 round
,
 
": "
,
 scratch
.
len
,
 
" bytes"
)
;

} 
// the free: one store to the stack top

### Nothing moves, so
references survive growth

struct
 
Item
 { id
:
 
i32
,
 weight
:
 
f32
 }

var
 items
:
 
Item
[
>..
] 
=
 []
;

let
 first 
.=
 items
.
push
(
Item
 { 
1
,
 
0.5
 })
;
 
// a reference to element 0

for
 i
:
 
i32
 
in
 
2
..
1000001
 { items
.
push
(
Item
 { i
,
 
0.0
 })
;
 }

first
.
weight 
=
 
99.5
;
 
// still valid, a million pushes later

pushreturns a reference to the new element, so a
program can link elements while building the array. Avector<T>orVec<T>may reallocate
and cannot provide this guarantee. Stable references account for several
benchmark gains.

### Safe references, no
annotations

Every reference and slice has a staticroot: the variable
that bounds its target's lifetime. A reference must not outlive the
variable that owns its target or access that target through an
incompatible type. The compiler infers roots and specializes functions
for them, so no annotations are needed. There are no aliasing or
exclusivity rules. When a lifetime check fails, the error names the
reference's root and its destination:

fn
 
longest
(a
:
 
u8
[
:
]
,
 b
:
 
u8
[
:
]) 
->
 
u8
[
:
] { 
if
 a
.
len
 
>=
 b
.
len
 { a } 
else
 { b } }

var
 outer
:
 
u8
[
>..
] 
=
 []
;

var
 w 
=
 outer[
..
]
;

{

 
var
 inner
:
 
u8
[
>..
] 
=
 []
;

 
format
(inner
,
 
"inner text"
)
;

 w 
=
 
longest
(outer
,
 inner)
;
 
// error: storing a reference rooted at inner,

} 
// which does not outlive the destination (§9.2)

A sliceT[:]lets a function accept a range from any
array kind without copying its elements. For example,splitreturns slices into its input, and a dictionary keyed byu8[:]stores views of strings rather than copies.

### Nested data stays inline

There is no single array type. There is a family that differs only in
what happens to the size, and every member is[metadata][elements...], inline and packed, never a pointer
to an element block:

Spelling

What it is

T[k]

fixed size, known at compile time

T[]
, 
T[varint]

sized at construction, frozen after; a fixed or variable-width
length

T[..k]
, 
T[..]

capacity inline; grows and shrinks within it

T[>..]

grow-only
: the workhorse; references into it stay
valid

T[>..<]

grow-shrink
: stacks, queues, heaps

Strings are justu8arrays:u8[>..]is a
builder,u8[]a finished string stored inline in whatever
holds it,u8[..16]a small string inside a struct,u8[:]a view. A struct may contain variable-size parts, and
they sit inline in declaration order, so a record is a run of bytes with
nothing indirect in it:

struct
 
Item
 { sku
:
 
u8
[
varint
]
,
 qty
:
 
varint
,
 cents
:
 
varint
 }

struct
 
Order
 { id
:
 
varint
,
 customer
:
 
u8
[
varint
]
,
 items
:
 
Item
[
varint
] }

var
 book
:
 
Order
[
>..
] 
=
 []
;

book
.
push
(
Order
 { id
:
 
1001
,
 customer
:
 
"alice"
,

 items
:
 [
Item
 { sku
:
 
"SKU-441"
,
 qty
:
 
2
,
 cents
:
 
1999
 }
,

 
Item
 { sku
:
 
"SKU-7"
,
 qty
:
 
1
,
 cents
:
 
500
 }] })
;

That order is29 bytes and 0 allocations. As C++std::string+std::vector<Item>it is
160 bytes and 1 allocation, and as RustString+Vec<Item>153 bytes and 4. A whole order book is one
array that streams through the cache. The price is that an array of
variable-size elements is sequential: you can iterate it but not index
it (unless you keep a second array of references into it as an
index).

### Enums in two sizes

Algebraic data types are the only dynamic polymorphism: no
inheritance, no vtables. Every ADT can be stored two ways, chosen at the
point of use. Fixed mode (Shape) is a tag plus room for the
largest payload, indexable and overwritable. Variable mode
(Shape..) gives each value exactly its variant's size; the
array becomes sequential and a value never changes variant, and in
exchange you may take referencesintoa payload:

enum
 
Shape
 { 
Circle
 { r
:
 
f64
 }
,
 
Rect
 { w
:
 
f64
,
 h
:
 
f64
 }
,
 
Dot
 }

var
 packed
:
 
Shape
..
[
>..
] 
=
 []
;
 
// 9, 17 and 1 bytes, not 17 each

packed
.
push
(
Shape
.
Circle
 { r
:
 
1.0
 })
;

packed
.
push
(
Shape
.
Rect
 { w
:
 
2.0
,
 h
:
 
3.0
 })
;

packed
.
push
(
Shape
.
Dot
)
;

for
 s 
in
 packed {

 
match
 s { 
Rect
 
&
r 
=>
 { r
.
w 
+=
 
1.0
;
 }
,
 _ 
=>
 {} } 
// edits the payload in place, inside the array

}

Case functionsprovide another way to dispatch on a variant:
define one overload per variant. Calls dispatch on the tag through a
jump table, and the compiler checks that the overloads cover every
variant:

fn
 
area
(s
:
 
Shape
.
Circle
) 
->
 
f64
 { 
3.14159
 
*
 s
.
r 
*
 s
.
r }

fn
 
area
(s
:
 
Shape
.
Rect
) 
->
 
f64
 { s
.
w 
*
 s
.
h }

fn
 
area
(s
:
 
Shape
.
Dot
) 
->
 
f64
 { 
0.0
 }

for
 s 
in
 packed { 
print
(s
,
 
" area "
,
 
area
(s))
;
 }

### Links narrower than pointers

AT&is a machine address: eight bytes, never
dangling. Arelative referenceis the same link stored as a
narrow offset:T&<u32>is measured from the field
itself to a target in the same array, so the structure is position
independent, andT&<u32 in pool>from a named
pool's base, so other arrays can link into the pool.T&<u32>?uses offset 0 as null. Here is a binary
search tree in one grow-only array, with 12-byte nodes:

struct
 
Node
 { key
:
 
i32
,
 left
:
 
Node
&<
u32
>?,
 right
:
 
Node
&<
u32
>?
 } 
// 12 bytes, links included

fn
 
insert
(pool
:
 
Node
[
>..
]
&,
 key
:
 
i32
) {

 
if
 pool
.
len
 
==
 
0
 { pool
.
push
(
Node
 { key
:
 key })
;
 
return
;
 }

 
var
 cur 
.=
 pool[
0
]
;
 
// .= binds a reference; = would copy the node

 
loop
 {

 
if
 key 
==
 cur
.
key { 
return
;
 }

 
let
 next 
=
 
if
 key 
<
 cur
.
key { cur
.
left } 
else
 { cur
.
right }
;

 
if
 next { cur 
.=
 next
;
 
continue
;
 } 
// narrowed by `if`: next is a Node&

 
if
 key 
<
 cur
.
key { cur
.
left 
.=
 pool
.
push
(
Node
 { key
:
 key })
;
 }

 
else
 { cur
.
right 
.=
 pool
.
push
(
Node
 { key
:
 key })
;
 }

 
return
;

 }

}

References are transparent (no*, no->),.=binds or retargets one, andNode?is a nullable reference thatif,guardandassertnarrow. The insert is one
push and one store, and the push cannot invalidatecur.
When lifetimes are not nested, areusablepool pairs a
grow-only array with a hidden freelist:alloc_refreuses a
slot or pushes,freehands one back, and since nothing is
ever actually freed, a stale slot reads adifferent value of the
correct typerather than corrupting memory.

### Your data is already a file
format

var
 image
:
 
u8
[
>..
] 
=
 tree
.
to_bytes
()
;
 
// a framed byte image of the whole array

var
 loaded
,
 ok 
=
 
from_bytes
<
Node
[
>..
]
>
(image)
;
 
// verified before it becomes a value

image[image
.
len
 
-
 
3
] 
=
 
200
;
 
// tamper with a link ...

var
 bad
,
 bok 
=
 
from_bytes
<
Node
[
>..
]
>
(image)
;
 
// ... and it is false and an empty array

The tree's links are self-relative, so it means the same thing
wherever it sits: saving is writing its bytes and loading is reading
them back, with no serializer, no schema and no pointer fixups.from_byteschecks the framing, every tag, every length and
every link before the bytes become a value, so a corrupt or hostile file
is afalse, never a wild reference.

### Built in place, always

The copy-free construction guarantee (spec
§4.3) says a constructed value is always built in its final home,
propagated top-down through calls. A function returning a grow-only
array by value writes its elements straight into the caller's variable,
or into a field of the record being built inside another array, so
out-parameters mostly do not appear.

words
.
push
(
str
(
"word"
,
 i))
;
 
// formatted straight into the new element

let
 evens 
=
 xs
.
filter
() { it 
%
 
2
 
==
 
0
 }
;
 
// built straight into `evens`: no temporary

book
.
push
(
Order
 { id
:
 
1001
,
 customer
:
 
"alice"
,
 items
:
 
parse_items
(
"SKU-441:2:1999;SKU-7:1:500"
) })
;

### Returning errors across
calls

struct
 
User
 { name
:
 
u8
[
..
16
]
,
 age
:
 
i32
 }

fn
 
load
(text
:
 
u8
[
:
]) 
->
 
User
[
>..
]
,
 
u8
[] {

 
var
 users
:
 
User
[
>..
] 
=
 []
;

 
each_split
(text
,
 
'
\n
'
) { users
.
push
(
parse_user
(it))
;
 }
;

 
return
 users
,
 
""
;

}

fn
 
parse_user
(line
:
 
u8
[
:
]) 
->
 
User
 { 
// returns a User: no Result, no error parameter

 
let
 comma 
=
 
find
(line
,
 
","
)
;

 
guard
 comma 
>=
 
0
 
else
 { 
return
 []
,
 
str
(
"expected name,age: "
,
 line) 
from
 load
;
 }

 
let
 age
,
 ok 
=
 
parse_int
(line[comma 
+
 
1
..
])
;

 
guard
 ok 
else
 { 
return
 []
,
 
str
(
"bad age: "
,
 line) 
from
 load
;
 }

 
let
 name 
=
 
trim
(line[
..
comma])
;

 
return
 
User
 { name
:
 name
,
 age
:
 age 
as
 
i32
 }
;

}

return E from freturnsEas the result of
the innermost active call off, however many frames up, and
every function in between keeps its plain signature. It is checked
statically, so every call ofparse_usermust lie inside aloadcall and nothing is uncaught at runtime. It is a
hidden discriminant checked per frame rather than an unwinder, and the
message is built directly whereload's caller wants it. The
parsers in the samples use it for every syntax error.

### Generics and function blocks

fn
 
twice
(x) { x 
+
 x } 
// an untyped parameter is a generic one

fn
 each_pair
<
T
,
 
F
>
(xs
:
 
T
[
:
]) { 
// F is a function value: a compile-time entity

 
for
 i 
in
 
0
..
xs
.
len
 
-
 
1
 { 
F
(xs[i]
,
 xs[i 
+
 
1
])
;
 }

}

fn
 
first_gap
(xs
:
 
i64
[
:
]) 
->
 
i64
 {

 
each_pair
(xs) { a
,
 b 
=>
 
if
 b 
-
 a 
>
 
1
 { 
return
 a
;
 } }
;
 
// returns from first_gap, not each_pair

 
return
 
-
1
;

}

let
 evens 
=
 xs
.
filter
() { it 
%
 
2
 
==
 
0
 }
;

let
 total 
=
 
fold
(xs
,
 
0
) { acc
,
 x 
=>
 acc 
+
 x }
;

sort
(xs) { a
,
 b 
=>
 a 
>
 b }
;

Everything is monomorphized. Type arguments are inferred from
argument types; parameters absent from those types can be supplied
explicitly. Function values are passed as generic parameters: every call
is direct and inlinable, they cannot escape, and there are no closure
objects or function pointers, so a higher-order function compiles to
exactly the loop it looks like. A block mayreturnfrom its
lexically enclosing function, and nested functions see the enclosing
function's locals.

### Threads that share nothing

thread_fn
 
worker
() { 
// a separate program with its own memory

 
loop
 {

 
let
 job 
=
 
qget
<
Job
>
()
;
 
// blocks on the typed queue for Job

 
guard
 job
.
n 
>=
 
0
 
else
 { 
break
;
 } 
// -1 means stop

 
qput
(
Result
 { n
:
 job
.
n
,
 digits
:
 
count_digits
(job
.
n) })
;

 }

}

for
 i 
in
 n { ids
.
push
(
thread_spawn
(worker))
;
 }

There is no shared mutable memory. Athread_fnand
everything it calls is compiled as its own program with its own data
stacks and its own copies of the globals. Values cross through typed
queues, one per type, and must beflat, with no references at
any depth. That is cheap because a flat Goose value is contiguous: a job
or a result carries real data, pixels included, and crossing is amemcpy.

A failed check orabortin a worker started withthread_spawn_containedends only that worker. Its message
goes to whoever waits for it, not to stderr, so a supervisor can log it
and start another:

var
 why
:
 
u8
[
>..
] 
=
 []
;

while
 
!
thread_wait
(
thread_spawn_contained
(serve
,
 attempt)
,
 why) {

 
log
(why)
;
 
// "assert failed (serve.goose:12)"

 why
.
clear
()
;

 attempt
++;

}

The firstthread_wait(id, msg)for a worker takes the
message; a caller that doesn't ask for it loses it.

### Plain C in, plain C out

extern
 
fn
 
hypot
(x
:
 
f64
,
 y
:
 
f64
) 
->
 
f64
;
 
// straight from libm

extern
 
fn
 
crc32_bytes
(s
:
 
const
 
u8
[
:
]) 
->
 
u32
;
 
// a slice crosses as { data, len }

extern
 
fn
 
stats_of
(xs
:
 
i32
[
:
]
,
 out
:
 
Stats
&
)
;
 
// a struct filled through a pointer

Anextern fnbinds a Goose signature to a C symbol. Themathandosmodules use this interface. Only
types with supported C representations may cross the boundary;
unsupported signatures are rejected at the declaration. The compiler
emits one C file for the whole program. The bundled TinyCC backend can
compile and run that C inside the Goose compiler's process.

### Where the speed comes from

Much of the speed comes from the memory model: no heap allocation or
per-object teardown, contiguous data, narrow links, and enums sized for
the variant they contain. Every index is bounds-checked, and the
compiler removes checks it can prove unnecessary. Anasserton a slice length often lets a kernel eliminate its remaining checks and
vectorize.--bce-linesreports the checks that remain.checkfree fnrejects a kernel if any bounds check survives;
index types let graph edges retain validation done during construction.
Benchmark measurements use whole-process wall-clock time, including
teardown.

Geometric mean over 16 benchmarks

vs idiomatic C++

vs hand-optimized C++

vs best safe Rust

speed, MSVC backend

3.51x

1.24x

1.13x

speed, clang backend

3.54x

1.26x

1.19x

peak memory

1.95x less

1.32x less

1.25x less

Thesummaryexplains the gains and
losses;results.mdhas every
measurement, anddesign.mdexplains what
the suite tests.

### What it costs you

* You think about where data lives: who owns this, and how long does
its scope last. Usually the answer is "the function that builds it", and
that is free; when it is not, it is areusablepool.
* Recursive functions cannot keep growable data across a recursive
call; scratch ends before the call, and what outlives it is passed in as
a pool.
* Arrays of variable-size elements iterate but do not index (short of
an index of references kept beside them), a fixed-mode enum cannot be
pointed into, and a variable-mode one cannot be overwritten. You choose
per container.
* No escaping closures, no function pointers, no dynamic dispatch
beyond ADT tags, and whole-program compilation only.
* A slot handed back to areusablepool and still named
reads whatever its next owner put there: a logic bug, never memory
corruption.

Tutorial §18is
the full list.

## Install a release

Prebuilt compilers for Windows (x64), Linux (x64) and macOS (Apple
silicon and Intel) are on thereleases page,
with the graphics, audio, ui and physics packages compiled in. Unpack
one anywhere and put its directory on PATH: the compiler finds the
standard library, TinyCC's runtime and the packages beside itself, and
keeps what it builds under~/.goose(GOOSE_HOME). The archive also holds these docs, the
samples and the VS Code extension.

Running a program in-process (goose file.goose) needs
nothing else on Windows. On Linux it needs the C library's headers
(libc6-dev, orglibc-devel); on macOS, the SDK
of the Xcode command line tools (xcode-select --install).goose buildalso needs a C compiler: Visual Studio 2022 or
later, or clang, on Windows; gcc or clang elsewhere. The Linux compiler
needs glibc 2.35 or later (Ubuntu 22.04, Debian 12), the macOS one macOS
13.3 or later. macOS keeps a downloaded archive's files from running
untilxattr -dr com.apple.quarantineis run on the unpacked
directory.

## Build and run

You need CMake 3.27 or later, a C++20 compiler (MSVC, clang or gcc)
and Python 3 for the test and sample runners. TinyCC, which the
in-process backend is built from, is part of the tree. The graphics,
audio, ui and physics modules are packages in repositories of their own
(goose_gfxandgoose_physics;docs/design/packages.md):-DGOOSE_BUILTIN_LIBS=allfetches them at the pinned tags
(git, at configure time) and compiles them into the compiler, so their
programs run with nothing else installed. Without it the compiler builds
alone, and a program importing one of them has it built into~/.goosethe first time, which needs git, cmake and a C
compiler.

git
 clone https://github.com/aardappel/goose

cd
 goose

cmake
 
-B
 build 
-DCMAKE_BUILD_TYPE
=
Release 
-DGOOSE_BUILTIN_LIBS
=
all

cmake
 
--build
 build 
--config
 Release

GOOSE_BUILTIN_LIBScan also name some of the packages
(physics, orgfx, which carriesaudioanduitoo). On Linux, SDL needs the X11
or Wayland development packages (third_party/SDL/docs/README-linux.md);
without them the build leaves thegfxmodule out and says
what to install.

The runner scripts preferbuild/Release, thenbuild/RelWithDebInfo, thenbuild, thenbuild/Debug. Pass--exeto select a specific
compiler; use an explicit Debug executable when testing with compiler
assertions enabled. The compiler isbuild/goose(build/Release/goose.exewith the Visual Studio generator),
and it finds the standard library in the source tree it was built from.
On Windows 10 version 1903 and later, its embedded manifest selects a
UTF-8 process code page so compiler paths do not depend on the system
locale. Earlier Windows versions retain their legacy code page.
Generated native executables retain their own process settings.

Run a program straight from source, in-process
(goose runsays the same explicitly, andgoose checkonly typechecks):

build/goose
 samples/01_tour.goose

Or build an executable, which lands beside the source
(-oputs it elsewhere). The compiler finds a C compiler on
the machine (goose toolchainsays which: MSVC or clang on
Windows, cc, gcc or clang elsewhere;--ccchooses) and
links the generated C with the runtime and whatever native modules the
program uses, graphics included. Programs that use threads need this
route, since TinyCC cannot place thread-local storage.

build/goose
 build samples/01_tour.goose 
&&
 
samples/01_tour

build/goose
 build samples/27_gfx_cube.goose 
&&
 
samples/27_gfx_cube

--debugturns on the overflow, range and tag checks in
the generated C, each abort naming its source line (and an overflow or a
cast the values involved), and builds the C with debug information;--dry-runprints the commands a build would run, for a
build system of your own;-vprints them as they run.
Intermediates go under~/.goose(GOOSE_HOME),
the runtime object compiled once per C compiler. Useful flags of both
forms:-O0/-O1/-O2set the
inlining level (-O2by default),--bce-linesreports the bounds checks kept per line, and-DGS_DEBUG=1is what--debugdefines. Every resizable value lives on a
data stack of 2 GB of reserved address space, committed as it is used:--stack-reserve 16Gchanges that for a program,--stacksreports how many data stacks the program and each
of its workers can take and the cap that puts onhardware_threads(), and-DGS_STACK_STATS=1makes a program report its actual use as it ends.

A program with C of its own names it in a sidecar beside the source,foo.buildbesidefoo.goose:c_sources = ["impl.c"];, withc_include,c_defines,c_libsand_windows,_linuxor_macosvariants of each for one
platform's part. Both forms build it:goose buildlinks it
in, andgoose runbuilds it into a library the in-process
run loads, so anextern fnreaches it either way. A library
does the same with a sidecar beside its entry (or names the static
library target of its own CMake project,cmake_target = "x";, which the compiler builds through
cmake), and a program takes a library withimport name from "source";in its root file: a directory
("./lib"), or a git repository at a tag or commit
("owner/repo@v1"on GitHub,"host/owner/repo@ref"), fetched into~/.gooseand built there once per C compiler
(docs/design/packages.md).

Underneath,goose -o tour.c tour.goosewrites the C,
which holds the program and the part of the runtime that inlines into
it; the rest of the runtime (the OS layer, data stack reservation,
threads, printing) is one more C file, whichgoose --emit-runtime goose_runtime.cwrites, to be compiled
once and linked with every program
(cc -O2 tour.c goose_runtime.o -o tour -lm -pthread; on
Windowscl /O2 tour.c goose_runtime.obj). Build the runtime
with the compiler and flags the programs use; it takes no-Dof its own, and a program from another version of the
compiler fails to link against it.--standalonewrites a C
file that holds the whole runtime instead, and builds on its own. A
program usingaudio,gfx,physicsoruialso links that module's layer, whichgoose --audio-link msvc|cc,--gfx-link,--physics-linkand--ui-linkname in a
response file
(cc cube.c goose_runtime.o -o cube @$(goose --gfx-link cc),
a ui program's before the gfx one it draws through).goose build --dry-runprints all of this for the program at
hand.

A program usingaudioplays procedural mono/stereo PCM
through SDL3 without opening a graphics window. See theaudio reference.

The test suite and the samples run on Windows, macOS and Linux:

python
 test/run_tests.py

python
 samples/run_samples.py

For editing, theVS Code extensiongives syntax highlighting, the compiler's language server
(goose lsp: errors as you type, hover, go to definition,
completion, rename, symbols) and one-key runs through the JIT:

code
 
--install-extension
 vscode/goose-language.vsix

Other editors can rungoose lspthemselves;editorshas the configuration for Neovim,
Helix and Emacs.

## Documentation

* Documentation index: the map of
everything below, and the root of the documentation site built from
these files (how).
* Tutorial: the friendly
introduction, by example. Read this first.
* Language reference: every feature,
topic by topic, with a compiling example for each: the whole language,
written to be read.
* Language specification: the exact
rules, when you want to know why something did not compile.
* Samples: thirty-one complete
programs in reading order, from a tour of the language to a JSON parser,
a threaded Mandelbrot, a file tree built from two pools, a spinning cube
on the GPU, thousands of boxes raining into a heap and a to-do list in
windows of widgets.
* Standard library: fourteen modules,
all readable Goose understdlib/, includinggfx, graphics on SDL3's GPU API (how
it is built),physics, rigid body physics on Box3D (how
it is built), andui, fonts,text rendering and
game HUDs, windows and widgets on Nuklear, drawn through gfx (how
it is built).
* Building programs and using
packages:goose build, libraries from git repositories
or directories, a program's own C, and how to make a package of your
own.
* Benchmarks: the numbers, with thefull resultsand thedesignbehind them.
* Implementation notes: how the
compiler works, pass by pass, andhow it is
tested.

## Status

Goose is new. What exists today is a whole-program compiler of about
thirty thousand lines of C++, the specification, the standard library,
the samples, and a test suite that CI runs on Windows, macOS and Linux
with an extra sanitizer job. Deliberately out of scope for now: moves
for resizable values, more than one resizable per struct, labeledbreak, namespace privacy, and more OS/library access. Open
items are tracked in thespecification's
Appendix B.

## License

Goose is licensed under theApache License,
Version 2.0.

## Authors

Wouter van Oortmerssen: Language Design, Compiler
Design, Coding standards.homepage,twitter.

Claude Fable: Compiler implementation, Benchmarking,
Sample & Doc writing.

## History & Use of AI

This repo was produced almost entirely with AI, from a human language
design. I had designed Goose several years ago, and had started to
implement it, but running a game startup (which is built on another
programming language of mine,Lobster) there was no time to
finish it. Which was sad, because I knew Goose could do things other
languages can't, and it should exist.

I had not expected AI to help with this until Fable came out. I
thought it might be capable enough to do a good job. I made it
essentially clone the style and structure of my other recent compiler
(Lobster), which is why if you look at the code, it looks rather similar
to that. My initial design had left lots of things unspecified, and lots
of back and forth with Fable made me decide on all of those, and it is
now a better language for it.

It is also an experiment in using AI to implement a new language,
rather than reproduce an existing one.

You may wonder why I had it work in C++, if clearly I could have used
any language, like Rust, or my own Lobster, or.. Goose itself (that may
still happen). With Fable, it was my observation that it is almost
equally capable in any language, and the strong guardrails of Rust or
other languages are not as pressing as they once were. Since the
compiler emits C, you likely already need to have a C/C++ compiler
around, so sticking inside one ecosystem would seem to simplify
deployment and adoption. I've also integrated libtcc and who knows what
other C libraries in the future. And, like I said, to have the compiler
code mimic my existing Lobster compiler seemed fun, at least I can read
it like it is my own.