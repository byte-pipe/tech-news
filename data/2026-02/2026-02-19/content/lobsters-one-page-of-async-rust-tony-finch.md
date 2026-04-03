---
title: One page of async Rust – Tony Finch
url: https://dotat.at/@/2026-02-16-async.html
site_name: lobsters
content_file: lobsters-one-page-of-async-rust-tony-finch
fetched_at: '2026-02-19T06:00:37.389703'
original_url: https://dotat.at/@/2026-02-16-async.html
date: '2026-02-19'
tags: rust
---

I’m writing a simulation, or rather, I’m procrastinating, and this
blog post is the result of me going off on a side-track from the main
quest.

The simulation involves a bunch of tasks that go through a series of
steps with delays in between, and each step can affect some shared
state. I want it to run in fake virtual time so that the delays are
just administrative updates to variables without any realsleep()ing, and I want to ensure that the mutations happen in the
right order.

I thought about doing this by representing each task as anenum Statewith a bigmatch stateto handle each step. But then I
thought, isn’t async supposed to be able to write theenum Stateandmatch statefor me? And then I wondered how much the simulation
would be overwhelmed by boilerplate if I wrote it using async.

Rather than digging around for a crate that solves my problem, I
thought I would use this as an opportunity to learn a little about
lower-level async Rust.

Turns out, if I strip away as much as possible, the boilerplate can
fit on one side of a sheet of paper if it is printed at a normal font
size. Not too bad!

But I have questions…

* async fn-damentals
* pin a task
* noop context
* primops, generally
* primops, minimally
* contexts and wakers
* primops, commandingly
* primops, yieldingly
* fake sleep in action
* questions

## async fn-damentals

My starting point was to write:


async

fn

deep_thought
(
)
 ->
u32

{


42


}


fn

main
(
)

{


deep_thought
(
)
;


}

playground

When I calldeep_thought()I immediately get aFuture<Output = u32>.
As the compiler warns, none of the code indeep_thought()runs, it
just constructs a value of an ineffable type which contains the
initial state ofdeep_thought()’s state machine.

To actually run it, I need topoll()it.TheFuture::poll()methodhas a signature that immediately presents a number of
obstacles:


fn

poll
(


self
:

Pin
<
&
mut

Self
>
,


ctx
:

&
mut

Context
<
'
_
>
,


)
 ->
Poll
<
Self
::
Output
>

## pin a task

Unlike normal Rust data structures, aFuturecan contain references
to itself. (In a Rust function, variables can refer to other
variables, and aFuturecontains (roughly speaking) function
activation frames, hence it can be self-referential.) So, whereas
normal Rust data types can be moved, aFuturemust stay at the same
address even when it is not borrowed.ThePintypeis used to
immobilize aFuture.

For my purposes it’s easiest toPintheFuturein aBoxon the
heap. I’ll define astruct Taskto wrap thePinnedFutureso
that I can define a couple of methods on it. (More elaborate async
frameworks usually have more layers between their version ofTaskand itsFuture.)

This wrapper is generic over the ineffableFuttype and its
ultimate return typeOut(which fordeep_thought()isu32).


struct

Task
<
Fut
>

{


future
:

Pin
<
Box
<
Fut
>
>
,


}


impl
<
Fut
,

Out
>

Task
<
Fut
>


where


Fut
:

Future
<
Output
 =
Out
>
,


{


fn

spawn
(
future
:

Fut
)
 ->
Self

{


let
 future =
Box
::
pin
(
future
)
;


return

Task

{
 future
}
;


}


}

Constructing aTasklooks like,


let

mut
 task =
Task
::
spawn
(
deep_thought
(
)
)
;

## noop context

The second argument topoll()is aContext, which is a
wrapper around aWaker.

The simplest way to make aContextis by usingWaker::noop(),
which is enough for us to getdeep_thought()to actually run. As in
the fake-time simulation that I am procrastinating, 7.5 million years
pass in the blink of an eye.


let

mut
 ctx =
Context
::
from_waker
(
Waker
::
noop
(
)
)
;


match
 task
.
future
.
as_mut
(
)
.
poll
(
&
mut
 ctx
)

{


Poll
::
Pending
 =>
{


todo
!
(
)
;


}


Poll
::
Ready
(
answer
)
 =>
{


println
!
(
"the answer is {answer}"
)
;


}


}

playground

## primops, generally

An async function can call another async function, and (in async code
just like in normal code) the called async function does nothing but
return aFuture. To make it do something, the caller needs to.awaittheFuture. Under the covers.awaitcompiles down topoll()ing theFuture.

A chain of async.awaitcalls bottoms out in a primitive operation
that interacts with the outside world. A primitive async operation is
animpl Futurestate machine data structure, written manually
instead of relying on compiler trickery.

Typically, a primitiveFuturewill bepoll()ed twice:

* The first time, it arranges for the operation to happen then
returnsPoll::Pending. The async executor suspends thisTaskwhile the operation proceeds.
* After the operation is complete the async executor resumes theTaskbypoll()ing it, which immediately becomes a secondpoll()on on the primitiveFuture. This time it returnsPoll::Ready()with the result of the operation, which becomes
the value returned by.await.

A primitiveFuturecan implement a more complicated state machine
that needs to bepoll()ed more, but twice is the minimum necessary
to actually suspend aTask.

## primops, minimally

Continuing my approach of doing the least possible thing to illustrate
a point, here’s a stubFuturethat pretends to sleep. Its trivial
state machine is encoded in the delay value: if it’s zero, theFuturecontinues without suspending; if it’s non-zero, theFuturesuspends, but first resets the delay so that next time it will
continue.


struct

Sleep
(
u32
)
;


impl

Future

for

Sleep

{


type

Output
 =
(
)
;


fn

poll
(


mut

self
:

Pin
<
&
mut

Self
>
,

 _
:

&
mut

Context
<
'
_
>


)
 ->
Poll
<
(
)
>

{


if

self
.
0
 >
0

{


self
.
0
 =
0
;


return

Poll
::
Pending
;


}

else

{


return

Poll
::
Ready
(
(
)
)
;


}


}


}

As an example of using it,deep_thought()can pretend to spend a
long time by constructing aSleep()object (which is our minimal
state machine) then.awaitit to invokepoll().


async

fn

deep_thought
(
)
 ->
u32

{


Sleep
(
7_500_000
)
.
await
;


42


}

And the main loop now needs topoll()theTasktwice to run it to
completion.


loop

{


match
 task
.
future
.
as_mut
(
)
.
poll
(
&
mut
 ctx
)

{


Poll
::
Pending
 =>
{


println
!
(
"sleeping for 7.5 million years..."
)
;


}


Poll
::
Ready
(
answer
)
 =>
{


println
!
(
"the answer is {answer}"
)
;


return
;


}


}


}

playground

## contexts and wakers

In that minimal proof-of-concept, the fakeSleepprimitive does not
actually do anything other than suspend theTask, and the top-level
async executor loop blithely assumes it knows why theTaskwas
suspended.

The purpose of theContextand its innerWakeris to allow a
primitiveFutureto communicate with the async executor loop: to
arrange for the operation to happen, and suspend theTaskwhile the
operation proceeds.

So for my fakeSleepto account for the passing of fake time, I need
to construct my ownWakerthat does something more useful thanWaker::noop().

I believe the design intent is that aWakeris roughly speaking a
wrapper round a smart pointer that refers to the currentTask. When
a primitiveFuturesuspends a task, it stashes theWakerwith the
operation in progress. When the operation completes, theWakeris
told towake()itsTask, which puts it back on the async
executor’s loop to bepoll()ed.

To make aWaker, I need to make aRawWaker:


pub

const

unsafe

fn

Waker
::
from_raw
(


waker
:

RawWaker


)
 ->
Waker
;


pub

const

fn

RawWaker
::
new
(


data
:

*
const

(
)
,


vtable
:

&
'
static

RawWakerVTable


)
 ->
RawWaker
;

This is dismaying, it’s like hand-rolled object-oriented C. Instead
of a type-safedyn Trait, I have to cruft something together from
a raw pointer, a list of functions in a struct, and unsafe code.

(Edited to add, 2026-02-18)Arthur Carcano pointed out on
Lobstersthat I failed to noticetheWaketrait,
which provides a safe way to construct aWaker. However the safeWaketrait puts uncomfortable restrictions on the way primitiveFutures can work, making them more complicated than the solution I
found without using theWaketrait.

At this point I got stuck, despondently trying to work out how myTasks and executor loop should refer to each other, and what kind of
smart pointer I can smuggle through a raw*const()pointer.
Eventually I realised there’s a simpler way.

## primops, commandingly

There are a couple of ways that a primitiveFuturecan arrange for
an operation to happen:

* It can immediately make system calls and mutate global data
structures to fire off the operation, before suspending itself by
returningPoll::Pending. This requires that difficult tangle of
smart pointers.
* Or instead it can suspend itself first, returning a command that
the async executor will carry out on theTask’s behalf. This is
awkward becausePoll::Pendingcannot carry a payload. However,
theContextprovides a side-channel that I can use to smuggle
out a return value.

In imaginary safe Rust, aTaskcan return aCommandroughly as
follows:

* The executor loop prepares a place-holder variable for the command.


let

mut
 cmd =
Command
::
Run
;

* Itpoll()s theTask, passing a mutable borrow of the command.


let
 p = task
.
future
.
as_mut
(
)
.
poll
(
&
mut
 cmd
)
;

* When a primitiveFuturewants to perform an operation, it
overwrites the command before suspending theTask.


fn

poll
(


mut

self
:

Pin
<
&
mut

Self
>
,


cmd
:

&
mut

Command


)
 ->
Poll
<
(
)
>

{


*
cmd =
Command
::
Example
;


return

Poll
::
Pending
;


}

* When the async executor loop getsPoll::Pendingfrompoll(),
it looks at the command to decide what to do with theTask.

In real Rust I need to smuggle the borrowed&mut cmdthrough theRawWaker’s raw*const()pointer.

Since I’m not using theWakerto revive theTaskwhen its
operation completes, I can reuse theRawWakerVTablefromWaker::noop().

## primops, yieldingly

I’ll define aYieldtype that combines the primitive commands andPoll::Ready()in oneenum, and I’ll fix the top-level task’s
return type toFuture<Output = ()>. (Too much boilerplate is needed
to keep theOutputtype generic.)

“Yield” has a dual meaning: the result returned (yielded) from an
activity; and the task relinquishing (yielding) the CPU.


#
[
derive
(
Copy
,

Clone
,

Debug
)
]


enum

Yield

{


Run
,


Sleep
(
u32
)
,


// maybe other commands here


Done
(
)
,


}

The async executor loop callspoll()on aTask, which creates a
place-holderYieldand stashes a pointer to it in a freshContext.


impl
<
Fut
>

Task
<
Fut
>


where


Fut
:

Future
<
Output
 =
(
)
>
,


{


fn

poll
(
&
mut

self
)
 ->
Yield

{


let

mut
 yld =
Yield
::
Run
;


let
 data =
&
mut
 yld
as

*
mut

Yield

as

*
const

(
)
;


let
 vtable =
Waker
::
noop
(
)
.
vtable
(
)
;


let
 waker =
unsafe

{

Waker
::
new
(
data
,
 vtable
)

}
;


let

mut
 ctx =
Context
::
from_waker
(
&
waker
)
;


match

self
.
future
.
as_mut
(
)
.
poll
(
&
mut
 ctx
)

{


Poll
::
Pending
 => yld
,


Poll
::
Ready
(
(
)
)
 =>
Yield
::
Done
(
)
,


}


}


}

TheYieldtype is also used as the direct representation of a
primitiveFuture. An async function constructs aYeildand.awaits it, which causes theYieldto be returned via theContextto the async executor’s loop. Before suspending, theFutureYieldis reset toYield::Runso that execution continues
the next time theTaskispoll()ed. (Analogous to resetting theSleepdelay to zero in the previous example.)


impl

Future

for

Yield

{


type

Output
 =
(
)
;


fn

poll
(


mut

self
:

Pin
<
&
mut

Self
>
,


ctx
:

&
mut

Context
<
'
_
>
,


)
 ->
Poll
<
Self
::
Output
>

{


if

let

Yield
::
Run
 =
*
self

{


return

Poll
::
Ready
(
(
)
)
;


}

else

{


let
 yld = ctx
.
waker
(
)
.
data
(
)

as

*
mut

Yield
;


let
 yld =
unsafe

{
 yld
.
as_mut
(
)
.
unwrap
(
)

}
;


*
yld =
*
self
;


*
self
 =
Yield
::
Run
;


return

Poll
::
Pending
;


}


}


}

There’s more discussion of theunsafecode below.

## fake sleep in action

The async executor loop needs to carry out the commandsYielded by
its tasks. The classic data structure for timers is a min-heap keyed
on the wake-up time; fake time is just a normal timer queue without
any actual sleeping or delays between wake-up times.

After augmenting myTasktype with a wake-up time, I can write my
main program roughly like this sketch:


let

mut
 tasks =
BinaryHeap
::
new
(
)
;


for
 i
in

1
..=
TASKS

{

 tasks
.
push
(
Task
::
spawn
(
activity
(
i
,

LIMIT
)
)
)
;


}


while

let

Some
(
mut
 task
)
 = tasks
.
pop
(
)

{


match
 task
.
poll
(
)

{


Yield
::
Sleep
(
delay
)
 =>
{

 task
.
wake_up
 += delay
;

 tasks
.
push
(
task
)
;


}


Yield
::
Done
(
)
 =>
{


// drop completed task


}

 yld =>
panic
!
(
"unexpected {yld:?}"
)
,


}


}

The main program spawns someactivity()s that sleep in a loop for
differing amounts of time. They report their progress to stdout. For
this demo I want the tasks to print synchronously (no async IO!) to
illustrate the progress of their state machines.

This demo is greatly simplified but roughly the same shape as the
fake-time simulation that I’m procrastinating.


async

fn

activity
(
delay
:

u32
,

stop
:

u32
)

{


let

mut
 now =
0
;


println
!
(
"{now} {delay} start"
)
;


loop

{


Yield
::
Sleep
(
delay
)
.
await
;

 now += delay
;


if
 now < stop
{


println
!
(
"{now} {delay} continue"
)
;


continue
;


}

else

{


println
!
(
"{now} {delay} return"
)
;


return
;


}


}


}

You cansee the complete demo in action at the Rust
playground. Task 1 wakes up every tick, task 2 every other
tick, etc.

## questions

I don’t know why aWakerisn’t just an abstract generic type
parameter with some trait bounds, so that I could define it using safe
code. As far as I can tell the language and the standard library don’t
depend on its exact shape, so I would expect the details to be punted
to async runtime libraries. I guess there’s something I’m missing that
requires the standard library to partially restrict the shape of aWaker.

There are some weaknesses in myunsafecode. Miri says the code is
OK, which agrees with my handwavy correctness argument by analogy with
a mutable borrow. However I’m not certain that the compiler is
guaranteed to know thatyldcan be mutated bypoll().

An alternative might be to return the mutatedYieldfromTask::poll()by reconstructing the&mut Yieldreference from theContextin the same manner asYield::poll(). But then I’m not
certain the compiler will know that the borrowedyldneeds to live
all the way to the end of the function.

For now I’ve chosen the shorter code.

Having learned how to do it myself, I’m curious to hear of crates that
already solve this problem.
