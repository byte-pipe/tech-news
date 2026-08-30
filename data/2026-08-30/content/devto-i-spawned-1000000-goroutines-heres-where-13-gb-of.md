---
title: I Spawned 1000000 Goroutines. Here's Where 13 GB of RAM Went. - DEV Community
url: https://dev.to/nazar-boyko/goroutines-are-cheap-their-stacks-arent-4ena
site_name: devto
content_file: devto-i-spawned-1000000-goroutines-heres-where-13-gb-of
fetched_at: '2026-08-30T21:52:45.707876'
original_url: https://dev.to/nazar-boyko/goroutines-are-cheap-their-stacks-arent-4ena
author: Nazar Boyko
date: '2026-08-27'
description: Ask any Go developer what a goroutine costs and you'll get the same answer with the exact byte count:... Tagged with go, performance, programming, webdev.
tags: '#go, #performance, #programming, #webdev'
---

Stack growth creates hidden OOM risks

Ask any Go developer what a goroutine costs and you'll get the same answer with the exact byte count: 2KB. The FAQ says "a few kilobytes". Conference talks say "you can have a million of them". And I believed it in the same lazy way I believe most numbers I've never checked, right up until I had some free time, a laptop with 68GB of RAM and no better idea than to park a million goroutines and look.

The number held, more or less. A million idle goroutines cost about 2.8GB: 2KB of stack each plus some bookkeeping. Then I changed one thing. Each goroutine called one function that put an 8KB array on its stack before it parked, one call, once. The same million goroutines now cost 13GB. That gap is what this article is about, and honestly the mechanism behind it is more interesting than the number.

## The 2KB Is Real, And It's Only The Stack

The test program is small on purpose. It starts N goroutines that block on a channel and waits until they're all parked. Then it prints the runtime's memory counters and (this part matters later) forces a few garbage collections one at a time and prints the counters after each. Amodeargument decides whether each goroutine touches its stack before parking and by how much.

main.go

package
 
main

import
 
(

 
"fmt"

 
"os"

 
"runtime"

 
"strconv"

 
"sync"

 
"time"

)

func
 
stats
(
label
 
string
)
 
{

 
var
 
m
 
runtime
.
MemStats

 
runtime
.
ReadMemStats
(
&
m
)

 
fmt
.
Printf
(
"%-24s goroutines=%-8d StackInuse=%8.1fMB HeapInuse=%6.1fMB Sys=%8.1fMB
\n
"
,

 
label
,
 
runtime
.
NumGoroutine
(),
 
float64
(
m
.
StackInuse
)
/
1e6
,

 
float64
(
m
.
HeapInuse
)
/
1e6
,
 
float64
(
m
.
Sys
)
/
1e6
)

}

//go:noinline

func
 
sink
(
b
 
[]
byte
)
 
byte
 
{
 
return
 
b
[
0
]
 
+
 
b
[
len
(
b
)
-
1
]
 
}

// A function whose frame holds an 8KB local. The slice goes to a

// noinline sink so the compiler can't drop the array.

//go:noinline

func
 
touch8
()
 
byte
 
{

 
var
 
buf
 
[
8
 
<<
 
10
]
byte

 
buf
[
0
],
 
buf
[
len
(
buf
)
-
1
]
 
=
 
1
,
 
1

 
return
 
sink
(
buf
[
:
])

}

// Same, with a 64KB local.

//go:noinline

func
 
touch64
()
 
byte
 
{

 
var
 
buf
 
[
64
 
<<
 
10
]
byte

 
buf
[
0
],
 
buf
[
len
(
buf
)
-
1
]
 
=
 
1
,
 
1

 
return
 
sink
(
buf
[
:
])

}

func
 
main
()
 
{

 
n
,
 
_
 
:=
 
strconv
.
Atoi
(
os
.
Args
[
1
])

 
mode
 
:=
 
os
.
Args
[
2
]
 
// idle | 8k | 64k

 
var
 
wg
 
sync
.
WaitGroup

 
block
 
:=
 
make
(
chan
 
struct
{})

 
start
 
:=
 
time
.
Now
()

 
for
 
i
 
:=
 
0
;
 
i
 
<
 
n
;
 
i
++
 
{

 
wg
.
Add
(
1
)

 
go
 
func
()
 
{

 
defer
 
wg
.
Done
()

 
switch
 
mode
 
{

 
case
 
"8k"
:

 
touch8
()

 
case
 
"64k"
:

 
touch64
()

 
}

 
<-
block

 
}()

 
}

 
for
 
runtime
.
NumGoroutine
()
 
<
 
n
 
{

 
time
.
Sleep
(
10
 
*
 
time
.
Millisecond
)

 
}

 
fmt
.
Printf
(
"spawned %d (%s) in %v
\n
"
,
 
n
,
 
mode
,
 
time
.
Since
(
start
)
.
Round
(
time
.
Millisecond
))

 
stats
(
"parked, before any GC"
)

 
for
 
i
 
:=
 
1
;
 
i
 
<=
 
6
;
 
i
++
 
{

 
runtime
.
GC
()

 
stats
(
fmt
.
Sprintf
(
"after GC #%d"
,
 
i
))

 
}

 
close
(
block
)

 
wg
.
Wait
()

}

Enter fullscreen mode

Exit fullscreen mode

Two notes on the setup because they change the numbers.StackInuseis the runtime's own count of bytes in stack spans so it's the honest "how much stack memory is out there" figure. And I ran the spawn loop withGOGC=offso the collector wouldn't shrink anything behind my back while I was still creating goroutines. The six explicitruntime.GC()calls afterwards are the only collections that happen. All of it on Go 1.26.4 on an Apple silicon Mac.

A million goroutines that do nothing:

GOGC
=
off ./gor 1000000 idle

# spawned 1000000 (idle) in 290ms

# parked, before any GC goroutines=1000001 StackInuse= 2048.8MB HeapInuse= 724.8MB Sys= 2817.8MB

# after GC #6 goroutines=1000001 StackInuse= 2048.9MB HeapInuse= 639.1MB Sys= 2821.0MB

# maximum resident set size: 2812690432

Enter fullscreen mode

Exit fullscreen mode

2,048.8MB of stacks for 1,000,001 goroutines is 2,048 bytes each, to the byte. That'sstackMin = 2048inruntime/stack.go, the constant everyone is quoting when they say 2KB. There's another 639MB of heap next to it and it's still there after six GCs, so it isn't garbage. It's the runtime'sgstruct for each goroutine plus the closure and the deferred call, about 640 bytes apiece (I checked with a barego park(c)and no closure or defer and got the same 639 bytes, so most of that is thegitself). Total resident memory 2.8GB. Call it 2.8KB per goroutine and the popular number is right within a rounding error.

For scale, an OS thread on Linux reserves whateverulimit -ssays for its stack, 8MB on most systems (the pthread_create man page has the details). That's virtual memory and mostly untouched but a million of them is 8TB of address space and the kernel will say no long before that. So the FAQ's "if goroutines were just threads, system resources would run out at a much smaller number" is true. Fine. The thing the FAQ says in the very next sentence is the one nobody quotes: the run-time "grows (and shrinks) the memory for storing the stack automatically."

## One 8KB Local Turns 2KB Into 16KB

Here's what growing means in practice. Almost every Go function starts with a check: is there enough room left on this goroutine's stack for my frame? If not,runtime.morestackruns. Since Go 1.4 what it does is allocate a new stack of twice the size, copy everything over and fix up every pointer that pointed into the old one. Keith Randall's 2013 design doc for contiguous stacks put it as "using powers of two sizes and just doubling each realloc", and the runtime today literally hasnewsize := oldsize * 2.

Doubling means the sizes go 2KB, 4KB, 8KB, 16KB. A function with an 8KB local can't fit in an 8KB stack (the frame needs room for the return address and the caller's frames and a guard area the runtime keeps at the bottom), so it lands on 16KB. Same 100,000 goroutines, each callingtouch8once before parking:

GOGC
=
off ./gor 100000 8k

# spawned 100000 (8k) in 151ms

# parked, before any GC goroutines=100001 StackInuse= 1461.8MB HeapInuse= 72.2MB Sys= 1555.1MB

# maximum resident set size: 2567208960

Enter fullscreen mode

Exit fullscreen mode

1,461.8MB across 100,001 goroutines is 14.6KB average, so 16KB stacks for nearly all of them (the runtime's per-P stack caches account for the rest, I think). Eight times the idle case for one function call that returned immediately. The 64KB version is the same story one doubling further:

GOGC
=
off ./gor 100000 64k

# spawned 100000 (64k) in 619ms

# parked, before any GC goroutines=100001 StackInuse= 12093.6MB HeapInuse= 72.8MB Sys= 12219.8MB

# maximum resident set size: 11055398912

Enter fullscreen mode

Exit fullscreen mode

Twelve gigabytes of stacks, 128KB each because 64KB plus a frame doesn't fit in 64KB. And the spawn took 619ms instead of 43ms. That's the growth: the runtime works out the size it needs before it allocates (it keeps doubling until the frame fits, then allocates once), so each goroutine paid for one 128KB stack, one copy and one round of pointer adjustment, and the process touched 12GB of fresh memory doing it. CockroachDB ran into the same cost in 2016 with their gRPC handler, back when the growth still happened in steps (more on that below).

None of this is a leak or a bug, it's the design working exactly as documented. The part people skip is that the stack a goroutine ends up with is decided by the deepest thing it ever called, not by what it's doing right now.

## The Stack Comes Back Down By Halves, One GC At A Time, And Stops At 4KB

The FAQ says stacks shrink, and they do, but the rule is more specific than "shrink". It's inshrinkstackinruntime/stack.go: during a garbage collection, if a goroutine is using less than a quarter of its stack the runtime allocates a stack half the size and copies it down. Half, not "whatever it needs", and never below the minimum. Randall's design doc had the same plan in 2013: "at GC time, if a go routine is using at most 1/4 of its stack, free the bottom 1/2 of the stack."

That's why the test forces six collections and prints after each. Here's the 64KB run continued past the first line:

# parked, before any GC goroutines=100001 StackInuse= 12093.6MB

# after GC #1 goroutines=100001 StackInuse= 6554.6MB

# after GC #2 goroutines=100001 StackInuse= 3277.8MB

# after GC #3 goroutines=100001 StackInuse= 1639.4MB

# after GC #4 goroutines=100001 StackInuse= 820.3MB

# after GC #5 goroutines=100001 StackInuse= 410.8MB

# after GC #6 goroutines=100001 StackInuse= 410.8MB

Enter fullscreen mode

Exit fullscreen mode

128KB, 64, 32, 16, 8, 4, and then it stops. 410.8MB across 100,001 goroutines is 4KB each, not 2KB. A parked goroutine that once called something is using a bit more than a quarter of a 4KB stack (its own frame plus thedeferrecord plus the runtime's guard space) so the shrink rule leaves it there. Forever, as far as I can tell, or until the goroutine exits. The 8KB run ends in the same place, 410.6MB, two GCs earlier.

So a goroutine's memory has three numbers, not one. What it starts with (2KB). What it grows to the first time it calls something real (a power of two big enough for the deepest frame). And what it settles at after enough garbage collections have gone by, 4KB for anything that ever grew. In a server where the GC runs every few seconds that middle number is short-lived. In a batch job withGOGC=offor a service with a huge heap where collections are minutes apart it's the number you pay.

There's a catch in "every few seconds" that I glossed over, and@vinhnguyenthanhdncaught it in the comments on dev.to. The collector is triggered by heap allocation. Growing a stack doesn't allocate on the heap, so a service whose heap has gone flat simply stops collecting, and the stacks stay wherever they grew. He reran the 8KB case on Go 1.26.2 with defaultGOGCand no explicitruntime.GC()calls: 100,001 goroutines parked at 770MB of stacks,NumGCstopped at 4, and it was still 770MB after 18 seconds of idling. The one thing that eventually gets you out without help is the forced collection the runtime runs every two minutes when nothing else has triggered one (forcegcperiodinruntime/proc.go), and that's one shrink by half per two minutes, so 128KB to 4KB is about ten minutes of doing nothing.GOMEMLIMITis the real fix: the memory limit counts stacks, so under it the collector keeps running and reachesshrinkstack. In his run the same binary underGOMEMLIMIT=600MiBsettled at 448MB.

One more line from that output that took me a minute:Syswent from 12.2GB before the first GC to 19.4GB after it. Shrinking a stack means allocating a new smaller one and copying, and the old stack spans go back to a free list rather than to the OS, at least not right away. So the process asked the kernel for more memory to use less of it. Resident memory peaked at 11GB. It's the kind of thing that makes a dashboard look wrong for a minute and then look fine, and I'm not sure I'd have believed the graph if I hadn't seen the counters.

## A Million Goroutines That Each Did One Thing Cost 13GB

Put the pieces together at the scale the conference talks like. A million goroutines, each callstouch8once and parks, normalGOGCso the collector runs while they're being created:

./gor 1000000 8k

# spawned 1000000 (8k) in 1.861s

# parked, before any GC goroutines=1000001 StackInuse= 8995.1MB HeapInuse= 658.9MB Sys= 13411.7MB

# after GC #6 goroutines=1000001 StackInuse= 4097.0MB HeapInuse= 639.3MB Sys= 13413.3MB

# maximum resident set size: 13407453184

Enter fullscreen mode

Exit fullscreen mode

13.4GB resident and not 2GB. The collector was shrinking stacks the whole time, that's whyStackInuseis 9GB rather than 16. After six more collections it's down to 4.1GB, the 4KB floor times a million. But the process already holds 13.4GB from the OS and it isn't handing it back in a hurry. WithGOGC=offduring the spawn the same run peaked at 25.5GB and I mention that only because it's the shape of a job that allocates a lot up front and collects rarely.

The idle version of the same million was 2.8GB. Same goroutines and same code with one extra function call in the past of each one, and the process is four and a half times bigger.

## Okay, But What Puts 8KB On A Goroutine's Stack?

That's the fair pushback, becausevar buf [8 << 10]byteisn't what most goroutines look like. Two answers, and the second one surprised me.

The first is that you don't need one big local, you need depth. A handler that calls a router that calls middleware that calls your code that calls a database driver that calls an encoder is a dozen frames, and they add up. The best public number I know of is from CockroachDB: in December 2016 Peter Mattis opened Go issue 18138 because their gRPCServer.Batchentrypoint needed 16 to 32KB of stack, and he wrote that he could "see the stack growing in 4 steps from 2 KB to 32 KB" and that "the stack growth is mildly expensive making it useful to trick the runtime into growing the stack early". They were pre-growing stacks by hand to skip the copies. A plain HTTP handler in a plain service is smaller than that but it isn't 2KB either, obviously.

The second answer is that Go knows this and changed the default. Since Go 1.19 the runtime "will now allocate initial goroutine stacks based on the historic average stack usage of goroutines", the release notes say, "in exchange for at most 2x wasted space on below-average goroutines." The code instack.gorecomputesstartingStackSizeat every GC from the average scanned stack, rounded up to a power of two, and cites issue 18138 as the reason. So in a real server, where most goroutines grow to 8 or 16KB, new goroutines don't start at 2KB anymore. They start at 8 or 16KB. The runtime decided the 2KB number was a bad default for exactly the workloads people quote it about. (GODEBUG=adaptivestackstart=0turns it back off; with a million goroutines that never grow it made no difference in my runs. Which is the point: the average was 2KB.)

There's also a ceiling, since Go 1.2: a single goroutine's stack can grow to 1GB on 64-bit systems before the runtime kills the program, anddebug.SetMaxStackmoves it. That one exists so a runaway recursion fails fast instead of eating the machine.

## What I'd Actually Do

DivideStackInusebyNumGoroutine, that's the metric. Both are cheap to read (runtime/metricshas/memory/classes/heap/stacks:bytesand/sched/goroutines:goroutinesif you'd rather not callReadMemStatsin production, since that one stops the world). If the average is 2 to 4KB your goroutines are the cheap kind and the count is the whole story. If it's 16KB or 32KB the count matters four to sixteen times more than you thought and the thing to look at is what those goroutines call rather than how many there are.

Keep large locals out of goroutines you have a lot of. A[64 << 10]bytescratch buffer in a per-connection goroutine is a 128KB stack per connection until the next few GCs, and a 4KB one after. Put it in async.Poolor on the heap where it's counted and collected on its own schedule and doesn't get copied every time the stack doubles.

And if you reach for a worker pool, be honest about why. It isn't because goroutines are expensive to create (they aren't, 290ms for a million). It's because a bounded number of goroutines means a bounded number of grown stacks, and a grown stack is the part with a real price.

So the 2KB is true, it's just the cost of a goroutine that hasn't done anything yet.

Thanks for reading! English isn't my first language, so I use AI to polish the grammar. Everything else here - the ideas, the code, the opinions - is mine.

Enjoyed this one? Let's stay in touch — I'm onLinkedIn, always happy to chat, swap ideas, or just say hi. 👋

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse