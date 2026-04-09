---
title: Sync Primitives are Functionally Complete | protty
url: http://kprotty.me/2025/07/31/sync-primitives-are-functionally-complete.html
site_name: lobsters
fetched_at: '2025-08-01T23:06:50.641873'
original_url: http://kprotty.me/2025/07/31/sync-primitives-are-functionally-complete.html
date: '2025-08-01'
published_date: '2025-07-31T00:00:00+00:00'
description: 'You can use any thread synchronization primitive to build any other one. Here’s how:'
tags: api
---

You can use any thread synchronization primitive to build any other one. Here’s how:

### Reducing into Event

First, the primitive needs to support blocking the caller until some condition occurs. With it, you can then create anewprimitive called anEvent. This is simply a type where one thread callsevent.wait()which suspends its caller until another thread callsevent.set(). Think of it as waiting for a bool to become true.

For example, here’s how to do it with POSIX threading primitives: With aMutexandCondvarit’s pretty straight forward; Wrap a bool in the mutex, usingcond.wait()to wait until it’s set and callingcond.signal()when setting it. If there’sonlyaMutexavailable, locking it prematurely turns it into aSemaphorewhere a subsequentlock()isevent.wait()andunlock()isevent.set().RwLockis effectively aMutexhere to the same effect.

For a more practical example, here’s how to build it from OS threading primitives: Most systems provide aFutexAPI, wherewait(&atomic_int, value)blocks until the atomic no longer matches the value andwake(&atomic_int, N)unblocks N threads waiting on the atomic (after its value has presumably been updated). Some OS like Windows and NetBSD instead provide Events directly, withNtWaitForAlertByThreadId/NtAlerThreadByThreadIdandlwp_park/lwp_unparkrespectively.

For a threading primitive where theset()caller must block until a matchingwait()(e.g.NtKeyedEventsor Rust’sBarrier), it can be made non-blocking by introducing an atomic bool in front; Bothwait()andset()atomic swap the bool to true. Ifwait()seesFalse, set() is yet to arrive so it blocks on the primitive. Ifset()seesTrue, wait() is/will-be blocking so it unblocks the primitive.

### Expanding from Event

Now with anEvent, it can be used to make any other sync primitive. Let’s start with a Mutex:

Pseudo-code for a simplistic, Event based Mutex

type

Node
:


next
:

?*
Node


event
:

Event

type

Mutex
(
state
:

Atomic
(
usize
)

=

0
):


lock
():


s

=

state
.load
(
Relaxed
)


loop
:


while

s

&

1

==

0
:


s

=

state
.cas
(
s
,

s

|

1
,

Acquire
,

Relaxed
)

orelse

return


node

=

Node
{

next
:

?*
Node
(
s

&

~
1
),

event
:

Event
{}

}


s

=

state
.cas
(
s
,

usize
(
&
node
)

|

1
,

Release
,

Relaxed
)

orelse
:


node
.event
.wait
()


s

=

state
.load
(
Relaxed
)


continue



unlock
():


s

=

state
.cas
(
1
,

0
,

Release
,

Acquire
)

orelse

return


loop
:


node

=

*
Node
(
s

&

~
1
)


s

=

state
.cas
(
s
,

usize
(
node
.next
),

Release
,

Acquire
)

orelse
:


node
.event
.set
()


return

If curious how this works, check out my previous post onBuilding a Tiny Mutex. With just anEvent(+ optionally aMutex), aFutexAPI can be builtusing similar tricks. FromFutex, all other primitives can be made (as seen on linuxglibc&musl). Here’s some examples:

Pseudo-code for simplistic, Futex based POSIX primitives

type

Mutex
(
state
:

Atomic
(
u32
)):


lock
():


_

=

state
.cas
(
0
,

1
,

Acquire
,

Relaxed
)

orelse

return


while

state
.swap
(
2
,

Acquire
)

!=

0
:


Futex
.wait
(
&
state
,

2
)


unlock
():


if

state
.swap
(
0
,

Release
)

==

2
:


Futex
.wake
(
&
state
,

1
)

type

Condvar
(
state
:

Atomic
(
u32
)):


wait
(
mutex
):


s

=

state
.load
(
Relaxed
)


mutex
.unlock
()


Futex
.wait
(
&
state
,

s
)


mutex
.lock
()


signal
():

_wake
(
1
)


broadcast
():

_wake
(
max
(
u32
))


_wake
(
n
):


_

=

state
.fetchAdd
(
1
,

Release
)


Futex
.wake
(
&
state
,

n
)

It’s all pretty neat, but does it make sense to do this in practice? Yes.

Golang implements all its blocking using anEventwithin each goroutine, wherewait()isgoparkandset()isgoready. AFutex-styleimplementation(exposed as a semaphore) is then written using said goroutineEvent, and the other sync primitives then use that semaphore API.

Also, a while back I wrote a Rust crate calledµSyncwhich implements all Rust standard library (stdlib) sync primitives using anEventbased onstd::thread::park(). However, unlike Golang, this skips having an intermediaryFutexand instead builds each directly on top ofEvent. The benchmarks showed it matching or outperforming those in the stdlib at the time, and some of the strategies wounded upcontributed upstream(thanks joboet!).

So with one you can always make the others. The more interesting question is whether that’s a good idea..

I think so, at least.
