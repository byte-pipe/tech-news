---
title: 609 - Futurelock / RFD / Oxide
url: https://rfd.shared.oxide.computer/rfd/0609
site_name: hackernews_api
fetched_at: '2025-11-01T11:08:19.052262'
original_url: https://rfd.shared.oxide.computer/rfd/0609
author: bcantrill
date: '2025-10-31'
description: 'Futurelock: A subtle risk in async Rust'
tags:
- hackernews
- trending
---

published
RFD

609

# RFD609Futurelock

This RFD can be accessed by the following groups:
[
public
]
State
published
RFD
609
Authors
David Pacheco

Updated

This RFD describesfuturelock: a type of deadlock where a resource owned by FutureAis required for another FutureBto proceed, while the Task responsible for both Futures is no longer pollingA. Futurelock is a particularly subtle risk in writing asynchronous Rust.

Oxide initially saw this problem inoxidecomputer/omicron#9259.

## Example of the problem

Consider the following program (in the playground):

use
 std
::
sync
::
Arc
;
use
 std
::
time
::
Duration
;
use
 tokio
::
sync
::
Mutex
;
use
 tokio
::
time
::
sleep
;
use
 futures
::
FutureExt
;
#
[
tokio
::
main
]
async
 fn
 main
()
 {
 // Create a lock that will be shared by multiple tasks.
 let
 lock
=
 Arc
::
new
(
Mutex
::
new
(()));
 // Start a background task that takes the lock and holds it for a few
 // seconds. This is just to simulate some contention. This function only
 // returns once the lock has been taken in the background task.
 start_background_task
(
lock
.
clone
())
.
await
;
 // The guts of the example.
 do_stuff
(
lock
.
clone
())
.
await
;
}
// Starts a background task that grabs the lock, holds it for 5 seconds,
// and then drops it. Returns once the task is holding the lock.
// The purpose of this is to simulate contention.
async
 fn
 start_background_task
(
lock
:
 Arc
<
Mutex
<
()
>>
)
 {
 // Use a channel to coordinate with the task so that it can tell us when
 // its taken the lock.
 let
 (
tx
,
 rx
)
 =
 tokio
::
sync
::
oneshot
::
channel
();
 let
 _
=
 tokio
::
spawn
(
async
 move
 {
 println!
(
"background task: start"
);
 let
 _guard
=
 lock
.
lock
()
.
await
;
 let
 _
=
 tx
.
send
(());
 sleep
(
Duration
::
from_secs
(
5
))
.
await
;
 println!
(
"background task: done (dropping lock)"
)
 });
 // Wait for the task to take the lock before returning.
 let
 _
=
 rx
.
await
;
}
// The guts of the example
async
 fn
 do_stuff
(
lock
:
 Arc
<
Mutex
<
()
>>
)
 {
 let
 mut
 future1
=
 do_async_thing
(
"op1"
,
 lock
.
clone
())
.
boxed
();
 // Try to execute `future1`. If it takes more than 500ms, do
 // a related thing instead.
 println!
(
"do_stuff: entering select"
);
 tokio
::
select!
 {
 _
=
 &
mut
 future1
=>
 {
 println!
(
"do_stuff: arm1 future finished"
);
 }
 _
=
 sleep
(
Duration
::
from_millis
(
500
))
 =>
 {
 do_async_thing
(
"op2"
,
 lock
.
clone
())
.
await
;
 }
 };
 println!
(
"do_stuff: all done"
);
}
async
 fn
 do_async_thing
(
label
:
 &
str
,
 lock
:
 Arc
<
Mutex
<
()
>>
)
 {
 println!
(
"
{
label
}
: started"
);
 let
 _
=
 lock
.
lock
()
.
await
;
 println!
(
"
{
label
}
: acquired lock"
);
 println!
(
"
{
label
}
: done"
);
}

This program reliably deadlocks. This surprises a lot of people! A background Task takes a lock, waits 5s, drops the lock and exits. In the meantime, wedo_stuff. That stuff consists of waiting for two Futures concurrently viaselect!. One future waits for the lock while the other sleeps for 0.5s and waits for the lock. So there’s just one lock and all logical streams of execution seem to execute concurrently. How could this possibly hang?

The interesting bits are all indo_stuff():

async
 fn
 do_stuff
(
lock
:
 Arc
<
Mutex
<
()
>>
)
 {
 let
 mut
 future1
=
 do_async_thing
(
"op1"
,
 lock
.
clone
())
.
boxed
();
 // Try to execute `future1`. If it takes more than 500ms, do
 // a related thing instead.
 println!
(
"do_stuff: entering select"
);
 tokio
::
select!
 {
 _
=
 &
mut
 future1
=>
 {

 println!
(
"do_stuff: arm1 future finished"
);
 }
 _
=
 sleep
(
Duration
::
from_millis
(
500
))
 =>
 {

 do_async_thing
(
"op2"
,
 lock
.
clone
())
.
await
;

 }
 };
 println!
(
"do_stuff: all done"
);
}
1
future1
 is the (boxed) future returned by
do_async_thing()
, an async function.
2
We’ll call the future returned by
sleep
:
future2
 (or, the "sleep" future).
3
The second branch of the
select!
 is its own future. We’ll call this
future3
.

It’s really important to understand what’s happening here so let’s be clear about the sequence.

First:

1. background task takeslock, begins holding it for 5 seconds
2. tokio::select!begins polling&mut future1.[1]This future attempts to take the lock, blocks, returnsPoll::Pending.
3. tokio::select!begins pollingfuture2(the sleep future) and blocks, returningPoll::Pending.

At this point:

* the background task holds the lock
* the main task is blocked intokio::select!on two different futures:future1is blocked on taking the lockfuture2(thesleepfuture) waiting for 500ms
* future1is blocked on taking the lock
* future2(thesleepfuture) waiting for 500ms

500ms later,tokiowakes up the main task becausefuture2(the sleep future) is ready. Insidetokio::select!:

* The task polls both futures.future1is still blocked on the lock and returnsPending.[2]future2(the sleep future) is ready and returnsReady.
* future1is still blocked on the lock and returnsPending.[2]
* future2(the sleep future) is ready and returnsReady.
* tokio::select!chooses the second branch&mut future1is dropped, but this is just a reference and so has no effect. Importantly, the future itself (future1) isnotdropped.the second branch is entered.do_async_thing("op2", …​)is called, creating a new futurefuture3. This future immediately blocks trying to take the lock, which is still held by the background task.
* &mut future1is dropped, but this is just a reference and so has no effect. Importantly, the future itself (future1) isnotdropped.
* the second branch is entered.do_async_thing("op2", …​)is called, creating a new futurefuture3. This future immediately blocks trying to take the lock, which is still held by the background task.

At this point, we have:

* the lock (still) held by the background task
* the lock’s wait queue contains two waiting futures:future1future3(the second arm of thetokio::select!)
* future1
* future3(the second arm of thetokio::select!)

There are two key points here:

1. The lock’s wait queue is literally a queue:onlyfuture1can take the lock once it is released by the background task (unlessfuture1is dropped).
2. The behavior oftokio::select!is to poll all branches' futuresonly until one of them returns `Ready`. At that point, it drops the other branches' futures and only runs the body of the branch that’s ready.

Critically: the same task is responsible for both of the futures waiting on the lock. But that task is currently only polling on one of them. Unfortunately, it’s the wrong one.

About 4.5 seconds later:

* The background task drops the lock.The lock is given tofuture1. (See below for more on why.)The task that polledfuture1(the main task) is woken up.
* The lock is given tofuture1. (See below for more on why.)
* The task that polledfuture1(the main task) is woken up.
* However, that task isnotpollingfuture1.future1is polled at the top-leveltokio::select!. But thetokio::select!has already chosen the other branch. It’s nowonlypollingfuture3. (In fact, even absent the imminent hang,future1would never be polled again. It would be cancelled without having completed when it got dropped at the end ofdo_stuff.)

Thus:

* There is only one task left. It’s blocked onfuture3.
* future3is blocked on a Mutex that’s owned byfuture1.
* future1cannot run (and therefore cannot drop the Mutex) until the task starts running it.

We call this specific kind of deadlockfuturelock. The program is stuck in this state forever.

### FAQ: why doesn’t the Mutex wake up the other future?

This particular example usestokio::sync::Mutex, which is a fair Mutex. That means that the lock is given to waiters in the order that they started waiting. Ithasto give it tofuture1.

An unfair Mutex would not fix things. The problem wouldn’t be guaranteed to happen with an unfair Mutex, but it wouldn’t be guaranteed not to, either. The Mutex does not (and cannot) know which future would be "better" to wake up, or which one is being polled. You could imagine an unfair Mutex that always woke up all waiters and let them race to grab the lock again. That would not suffer from risk of futurelock, but it would have thethundering herd problemplus all the liveness issues associated with unfair synchronization primitives. And it’s not how many synchronization primitives work.

It’s helpful to view this in terms ofresponsibilities: the Mutex’s job here is to wake up the next task waiting for the lock. And it’s doing that. It’s that task’s responsibility to check on all the futures that it’s responsible for. The Mutex cannot do that.

### FAQ: why isn’t thetokio::select!polling onfuture1? Isn’t that the whole idea oftokio::select!

The idea oftokio::select!is to poll on multiple futures concurrently and enter the branch for whichever one finishes first. Once one of the futures does finish (as thesleepone has in our case), control enters that specific branch. It essentially commits to that branch and it’s only running that branch at that point.

Thetokio::select!docsare explicit about this:

By running all async expressions on the current task, the expressions are able to run concurrently but not in parallel. This means all expressions are run on the same thread and if one branch blocks the thread, all other expressions will be unable to continue. If parallelism is required, spawn each async expression using tokio::spawn and pass the join handle to select!.

### FAQ: doesn’tfuture1get cancelled?

When one of the futures thattokio::select!is polling on completes, the others get dropped. In this case, what’s dropped is&mut future1. Butfuture1is not dropped, so the actual future is not cancelled.

Iffuture1didget cancelled, you’d get no deadlock. Try it: change the above to wait onfuture1instead of&mut future1. Alternatively, you can add an explicitdrop(future1);at line 51 between thesleepand thedo_async_thing. This mimics whatselect!does if we usefuture1rather than&mut future1.

Tasks vs. Futures
Note
Tasks vs. Futures

When first learning async Rust, it’s common to think of tasks and futures almost interchangeably. When you want parallelism, youspawna new task and give it the future that you want to run. If you want to do 10 things in parallel, you spawn 10 tasks and then wait for them all to finish.

You can have concurrency without tasks (and without parallelism) using something liketokio::select!. Within a single task, you can do 10 things concurrently (not in parallel) usingtokio::select!orFuturesUnorderedor the like. In this case, your one task is polling on all these futures and getting woken up when any of them might be ready.

Tasksare the top-level entities that the runtime executes. Each task runs one top-level future. That future can choose to do only do one thing at a time (as in the case of sequential code usingawait), or it can choose to do things concurrently by polling many futures, usingtokio::select!orFuturesUnorderedor the like.

## What causes futurelock?

The general problem here is that you have:

* taskTis blocked on futureF1completing (andTis directly awaitingF1)
* futureF1is blocked on futureF2in some way (e.g., acquiring a shared Mutex)
* futureF2is blocked on taskTpolling it, butTisn’t polling it because it’s only pollingF1

Most commonly this happens afterTstartedpollingF2earlier, but then switched toF1. This can happen in a bunch of different cases:

* usingtokio::select!with a&mut futureand awaiting in one of the other branches (our example above)
* polling futures from aFuturesOrdered/FuturesUnordered(e.g., by callingnext()) and then awaiting on anyotherfuture (e.g., each time one of the futures completes from the set, you do some async activity)
* in a hand-writtenFutureimpl that behaves analogously
Note

You can hit futurelock even if you never start polling one of the futures. Considerthis example:

use
 futures
::
FutureExt
;
#
[
tokio
::
main
]
async
 fn
 main
()
 {
 let
 (
tx
,
 rx
)
 =
 tokio
::
sync
::
oneshot
::
channel
();
 let
 _future1
=
 async
 {
 tx
.
send
(())
.
unwrap
();
 }
.
boxed
();
 let
 future2
=
 async
 {
 rx
.
await
.
unwrap
();
 };
 future2
.
await
;
}

This deadlocks, too. And for the same reason: this task is waiting on a future that itself depends on a future that this task is responsible for running. This is possible but feels contrived. This RFD focuses on cases where the dependency between futures relates to a shared resource. That generally requires that the futures all start running so they can get in line for the resource.

### How you can hit this withtokio::select!

Hitting this problem withtokio::select!(as in the example above) requires two things to be true:

* You must be passing a&mut futureto one of the branches. If you’re passing an owned future, then it will get dropped when thetokio::select!enters a different branch. That generally releases the resources that might have been blocking other futures.
* You must be usingawaitin one of the branches' handlers. If you’re not doing this, then the task does not get blocked on anyparticularfuture at the expense of the others.

That said, it’s just as problematic to have an owned futureacrossatokio::select!and awaitafterit (full example):

async
 fn
 do_stuff
(
lock
:
 Arc
<
Mutex
<
()
>>
)
 {
 let
 mut
 future1
=
 do_async_thing
(
"op1"
,
 lock
.
clone
())
.
boxed
();
 // Try to execute `future1`. If it takes more than 500ms, do
 // a related thing instead.
 println!
(
"do_stuff: entering select"
);
 tokio
::
select!
 {
 _
=
 &
mut
 future1
=>
 {
 println!
(
"do_stuff: arm1 future finished"
);
 }
 _
=
 sleep
(
Duration
::
from_millis
(
500
))
 =>
 {}
 };
 do_async_thing
(
"op2"
,
 lock
.
clone
())
.
await
;
 println!
(
"do_stuff: all done"
);
}

This results in exactly the same behavior.

### How you can hit this with Streams

If you pull a future from aStreamand then await a future that somehow depends on another Future in the stream, you can wind up with futurelock. Here’s what it looks like with FuturesOrdered (full example):

async
 fn
 do_stuff
(
lock
:
 Arc
<
Mutex
<
()
>>
)
 {
 let
 future1
=
 sleep
(
Duration
::
from_millis
(
500
))
.
boxed
();
 let
 future2
=
 do_thing
(
"op1"
,
 lock
.
clone
())
.
boxed
();
 let
 mut
 futs
=
 FuturesOrdered
::
new
();
 futs
.
push_back
(
future1
);
 futs
.
push_back
(
future2
);
 let
 _
=
 futs
.
next
()
.
await
;
 println!
(
"one future finished"
);
 do_thing
(
"op2"
,
 lock
.
clone
())
.
await
;
}

Anearly identical example creates futurelock withFuturesUnordered.

These are often used in a loop, so it may tend to look more like this (full example):

async
 fn
 do_stuff
(
lock
:
 Arc
<
Mutex
<
()
>>
)
 {
 let
 future1
=
 do_thing
(
"op1"
,
 lock
.
clone
())
.
boxed
();
 let
 future2
=
 sleep
(
Duration
::
from_millis
(
500
))
.
boxed
();
 let
 mut
 futs
=
 FuturesUnordered
::
new
();
 futs
.
push
(
future2
);
 futs
.
push
(
future1
);
 while
 let
 Some
(
_
)
 =
 futs
.
next
()
.
await
 {
 println!
(
"a future finished"
);
 do_thing
(
"op2"
,
 lock
.
clone
())
.
await
;
 }
}

It seems likely that futurelock is a risk when using many otherStream functions.

### What aboutjoin_all?

You can’t hit this withfutures::future::join_all. That’s because it polls all of its futures and does not stop polling any of the pending futures.

## Failure mode, debugging

Futurelock is a type of deadlock and tends to manifest as a hang of part or all of the program. When we saw this inomicron#9259, every future attempting to access the database became part of the futurelock. Since authorization uses the database, essentially every incoming HTTP request hung indefiniteily.

Debugging this problem from direct observation can be next to impossible. Typically, you’d only start looking at data long after the problem happened. At that point, it’s not clear what evidence you’d find even if you could peer into the executor state. The problem looks like apendingfuture whose task has been woken upbecauseof that future, but the task has not polled the future. (Maybetokio-consolecould help?)

In omicron#9259, we were able to determine (by tracing individual function calls with DTrace) that:

* all incoming requests were blocking on attempts to send on anmpscchannel with capacity 1
* the receiving end of this channel was regularly checking it and finding no messages queued

This confused us for quite a while. Why are senders blocking if there’s nothing in the channel? In hindsight, the answer’s implied by the documentation forSender, which says:

Sends a value, waiting until there is capacity.

…​

This channel uses a queue to ensure that calls to send and reserve complete in the order they were requested.

One can infer that a given call tosendmay block either because there is no capacityorbecause another sender’ssend()is not completing. Thatcouldbe because the channel is full, but in our case it’s because the future for that sender had run into futurelock.

It’s hard to give useful advice for debugging this sort of problem aside from advising that you consider futurelock as a possibility if you’re debugging a hang and some future appears blocked when other evidence suggests that it shouldn’t be.

## Determinations: avoiding this problem

Like async cancellation (see[rfd397]), futurelock defeats Rust’s goal of being able toreason locallyabout correctness. If we look at the pieces involved in our example:

* Usingtokio::select!to wait for any of a few things to happen
* Usingawaitin atokio::select!branch
* Using a&mut futurewithtokio::select!
* Using a Mutex[3]

None of these by itself is wrong, but combining them results in futurelock. Remember too that the Mutex could be buried beneath several layers of function calls in different modules or packages. It could require looking across many layers of the stack at once to be able to see the problem.

There’s no one abstraction, construct, or programming pattern we can point to here and say "never do this". Still, we can provide some guidelines.

### In general

The most specificgeneraladvice we can give is: any time you have a single task polling multiple futures concurrently, be extremely careful that the task never stops polling a future that it previously started polling.

One way to avoid this situation is to bias towards spawning futures in new tasks instead. There are other considerations with this approach: futures would be cancelled when they’re dropped, but tasks won’t be aborted when their JoinHandle is dropped. If you want this, seeAbortOnDropHandle.

### When usingtokio::select!

If you find yourself writing or reviewing code that doeseitherof these:

* Uses a&mut futureas one of the async expressions in thetokio::select!
* Awaits inside the handler of atokio::select!branch or after thetokio::select!before thefuturehas been dropped

then look for the other as well. If both are present, pay close attention to the risk of futurelock. To avoid it, you either need to avoid doing both of these things in the sametokio::select!call or else beverysure thatfuturenever blocks with shared resources held that could block other futures.

Let’s consider avariation of our original example:

 let
 mut
 future1
=
 do_async_thing
(
"op1"
,
 lock
.
clone
())
.
boxed
();
 // Execute `future1`. Every 500ms, do something related
 // (e.g., report progress).
 loop
 {
 println!
(
"do_stuff: entering select"
);
 tokio
::
select!
 {
 _
=
 &
mut
 future1
=>
 {
 println!
(
"do_stuff: arm1 future finished"
);
 break
;
 }
 _
=
 sleep
(
Duration
::
from_millis
(
500
))
 =>
 {
 do_async_thing
(
"op2"
,
 lock
.
clone
())
.
await
;
 }
 };
 }
 println!
(
"do_stuff: all done"
);

Here, we’ve wrapped thetokio::select!in a loop. This is a common pattern. The idea here is mainly to runfuture1, but every 500ms we do something related (like report progress or check if we should cancel the like).

The easiest way to make this safer is tospawnfuturein a new task. Then use theJoinHandlein thetokio::select!, likethis version:

 let
 future1
=
 do_async_thing
(
"op1"
,
 lock
.
clone
());
 let
 mut
 future1_task
=
 tokio
::
spawn
(
future1
);
 // Execute `future1`. Every 500ms, do something related
 // (e.g., report progress).
 loop
 {
 println!
(
"do_stuff: entering select"
);
 tokio
::
select!
 {
 _
=
 &
mut
 future1_task
=>
 {
 println!
(
"do_stuff: arm1 future finished"
);
 break
;
 }
 _
=
 sleep
(
Duration
::
from_millis
(
500
))
 =>
 {
 do_async_thing
(
"op2"
,
 lock
.
clone
())
.
await
;
 }
 };
 }
 println!
(
"do_stuff: all done"
);

This has the same desired effect of keepingfuture1running, but nowfuture1_taskis a separate future. It’s cancellable, and cancelling it won’t cancelfuture1. (If you want that, you can still usefuture1_task.abort().) This construction cannot result in futurelock.

If you’re not using a loop, this approach is even better: then you can just passfuture1_tasktotokio::select!(rather than&mut future1_task) and it’ll be more obvious that this is safe.

In the end,you should always be extremely careful withtokio::select!. That’s because:

* If you use it with borrowed futures, beware of futurelock.
* If you use it with owned futures, beware of cancel-safety (see[rfd397]and[rfd400]).

So either way you’ve got a subtle, non-locally-reasonable, undebuggable problem to worry about that the compiler can’t really help with.

### When usingStream

When using aFuturesOrderedorFuturesUnordered, consider instead usingtokio’sJoinSet. This provides a similar interface, but the futures you’re waiting for are all running in separate tasks.

If for whatever reason that’s not appropriate (e.g., you’re not usingtokio, or you really need aStreaminterface), then in the body of a loop that pulls completed futures from theStream, do not await any other futures. If you’re working with aFuturesUnordered, consider putting those futures into the set instead.

### When using bounded channels

Bounded channels are not really the issue here. Even in omicron#9259, the capacity=1 channel was basically behaving as documented and as one would expect. It woke up a sender when capacity was available, and the other senders were blocked to maintain the documented FIFO property. However, some of the patterns that we use with bounded channels are problematic on their own and, if changed, could prevent the channel from getting caught up in a futurelock.

In Omicron, we commonly use bounded channels withsend(msg).await. The bound is intended to cap memory usage and provide backpressure, but using the blockingsendcreates a secondunboundedqueue: the wait queue for the channel. Instead, we could consider using a larger capacity channel plustry_send()and propagate failure fromtry_send().

As an example, when we use the actor pattern, we typically observe that there’s only one actor and potentially many clients, so there’s not much point in buffering messagesinthe channel. So we usecapacity = 1and let clients block insend().await. But we could instead havecapacity = 16and have clients usetry_send()and propagate failure if they’re unable to send the message. The value16here is pretty arbitrary. You want it to be large enough to account for an expected amount of client concurrency, but not larger. If the value is too small, you’ll wind up with spurious failures when the client could have just waited a bit longer. If the value is too large, you can wind up queueing so much work that the actor is always behind (and clients are potentially even timing out at a higher level). One might observe:

Channel limits, channel limits: always wrong!

Some too short and some too long!

But as with timeouts, it’s often possible to find values that work in practice.

Usingsend_timeout()isnota mitigation because this still results in the sender blocking. It needs to be polled after the timeout expires in order to give up. But with futurelock, it will never be polled.

### Anti-pattern: just make the channel bigger

In ourinitial encounter with this problem, we had a boundedtokio::sync::mpscchannel of capacity 1. Why not bump the capacity up?

To avoid futurelock, the channel would have to have capacity big enough that nobody in the call stack could possibly have that many futures that they’ve started and aren’t polling. There is of course no way to know how big this needs to be, and it could change over time as the program evolves. Further, there are big side effects to having big channels like this in terms of latency, backpressure, and memory usage.

### Anti-pattern: try to avoid dependencies between futures

In principle, you could avoid this problem if you avoid dependencies between futures. Aside from usingspawnto do this, we do not recommend this in general because it’s brittle and risky.

First, it’s hard to know there are no dependencies. Any shared resource can be such a dependency: a bounded channel of any kind, a Mutex, a request to a remote service, etc. And it can be anywhere in the stack, including several dependency packages down the call chain.

Even if there’s no such dependencynow, one could be added later. You could imaginefuture1callingsome_crate::func1()andfuture2callingother_crate::func2()that seem like simple functions.some_cratecould decide to add a global Mutex that is otherwise safe and correct, but this would now breakyourtokio::select!that was previously assuming these futures shared no dependencies.

The exception to this is that usingtokio::spawnisa good way to replace one or more futures that could be subject to futurelock with ones that can’t. The returnedJoinHandleis a future that becomes ready under the same conditions as the underlying one, but it does not hold shared resources and it’s very unlikely that that would ever change as tokio evolves. (Such a change would almost certainly break lots of correctly-written programs.)

## Open Questions

Can we write clippy lints to:

* Warn when passing&mut futureto atokio::select!arm and suggest thattokio::spawnbe used instead, and
* Warn when usingawaitin atokio::select!arm? (This is problematic for other reasons anyway whenselect!is used in a loop.)

There are certainly cases to do this and it’s okay to override the warning, but it’d be nice to have that guard rail.

## Security Considerations

None actionable. Futurelock is a potential vector for denial of service, but it’s bad anyway, and we know we want to avoid it.

## External References

* [rfd397] Oxide Computer Co.RFD 397 Challenges with async/await in the control plane. 2023.
* [rfd400] Oxide Computer Co.RFD 400 Dealing with cancel safety in async Rust
* Example of the problem
* FAQ: why doesn’t the Mutex wake up the other future?
* FAQ: why isn’t thetokio::select!polling onfuture1? Isn’t that the whole idea oftokio::select!
* FAQ: doesn’tfuture1get cancelled?
* What causes futurelock?
* How you can hit this withtokio::select!
* How you can hit this with Streams
* What aboutjoin_all?
* Failure mode, debugging
* Determinations: avoiding this problem
* In general
* When usingtokio::select!
* When usingStream
* When using bounded channels
* Anti-pattern: just make the channel bigger
* Anti-pattern: try to avoid dependencies between futures
* Open Questions
* Security Considerations
* External References

### Table of Contents

Footnotes
* 1Note that steps 2 and 3 can happen in the other order becausetokio::select!polls its futures in random order. But the result is the same.View
* 2As above, it’s possible thatfuture2is polled first, in which casefuture1will not be polled at all. That doesn’t change anything else.View
* 3Although the use of the Mutex is simplistic, it’s realistic and correct: there are no lock ordering problems nor unsafe operations done with the lock held, etc.View
