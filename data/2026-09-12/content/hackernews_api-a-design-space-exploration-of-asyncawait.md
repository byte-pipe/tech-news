---
title: A Design Space Exploration of Async/Await
url: https://cel.cs.brown.edu/blog/design-space-async-await/
site_name: hackernews_api
content_file: hackernews_api-a-design-space-exploration-of-asyncawait
fetched_at: '2026-09-12T13:52:48.122616'
original_url: https://cel.cs.brown.edu/blog/design-space-async-await/
author: wcrichton
date: '2026-09-09'
description: Every language pitches async/await as synchronous-looking code, and the same two keywords appear everywhere. But behind the shared syntax hide nine independent design decisions, and no two of seven modern runtimes agree on what even the simplest async programs should do! In this paper we map the design space of async/await so you can find out where your language stands.
tags:
- hackernews
- trending
---

Many programming languages now provide theasync/awaitkeywords for expressing concurrency. The design rationale is pretty consistent: to make concurrent programs look more like straight-line code (see:Python,Rust, orSwift). We therefore describe the paradigm which encompasses async/await asstraight-line asynchrony, as opposed to using event loops or callbacks.

Language designs for straight-line asynchrony have been brewing for over 15 years. In this project, we wanted to understand: how similar or different is async/await between languages? The short answer is a lot more different than we expected. We wrote a paper,“A Design Space Exploration of Async/Await”, to explain how.

## So you think you know async/await?

To demonstrate how much modern languages can diverge, here’s a small async program written in pseudocode. One function writes to a log, and another fires off the log write as a background task and moves on.

async
 fn
 write_to_log
()
:

 print
(
"A"
)

 // simulate a slow log write

 await
 sleep
(
2
)

 print
(
"B"
)

async
 fn
 fire_and_forget
()
:

 task 
=
 spawn 
write_to_log
()

 // return without awaiting the task

async
 fn
 main
()
:

 await
 fire_and_forget
()

 await
 sleep
(
1
)

 print
(
"C"
)

What would you expect this program to print?

Check my answer

There isn’t really a right answer, because you were probably rightfor some language. Below is how seven modern async runtimes actually behave:

Show me the outputs

Four different answers, for a program whose entire job is to write a log line in the background. And it gets worse.In the paper, we show that across the seven runtimes,no twoproduce the same output for three variations of this simple program!

Do youactuallyknow your language’s async semantics?

## Why the disagreement?

While watching videos froma programming influenceryou may have have heard the terms “cold” or “hot” async function calls. The idea is that “hot starts” return a task that is immediately running in the runtime, while “cold starts” return an inert object that does nothing until awaited.

Hot vs. cold functions is what we call an asyncdesign dimension:a design decision that affects the observable semantics of program execution (as opposed to matters of pure performance). We call this particular dimension “Eagerness”, andin the paperwe identify nine such dimensions from modern implementations of straight-line asynchrony. Below we’ve grouped these nine dimension into three categories that roughly correspond to the lifetime of a task: Start of Life, End of Life, and Cancellation.

Click a language to trace its design choices through the table.

Start of Life
Eagerness

How to evaluate an async function application.

Lazy

Evaluate to a coroutine without executing further.

Python·Rust

Eager

Evaluate in current thread, and schedule as task on await.

C#·JavaScript

Suspension

Guarantees on whether await points suspend.

Static

Await points guaranteed to suspend.

JavaScript

Dynamic

No guarantees on awaiting tasks.

C#·Swift·Tokio·Smol·Asyncio·Trio

End of Life
Extent

The default interval of time during which a task may exist.

Indefinite

Tasks by default may exist until the end of the runtime.

JavaScript·C#·Tokio·Smol·Asyncio

Dynamic

Tasks by default may exist until the end of their spawning scope.

Swift·Trio

Reference Strength

[For Indefinite Extent]The type of reference to a task held by the runtime.

Strong

The runtime holds a strong reference.

JavaScript·C#·Tokio

Weak

The runtime holds a weak reference.

Asyncio·Smol

Destruction

How a task is cleaned up at the end of its extent.

Awaited

The task is awaited to completion.

JavaScript·Trio

Cancelled

The task is cancelled, and then possibly awaited.

Swift·Tokio·Smol·Asyncio

Terminated

The program exits.

C#

Propagation

What happens to exceptions in unawaited tasks.

Destructive

Exceptions are reraised by dependents.

Trio

Never

The exception is kept within the task.

JavaScript·C#·Tokio·Smol·Asyncio·Swift

Cancellation
Awareness

Whether a task is able to respond to being cancelled.

Unaware

The task cannot respond to being cancelled.

Rust

Aware

The task can respond to being cancelled.

Asyncio·Trio·Swift

Direction

How cancellation is communicated through the task graph.

Top-Down

Starting from the root task, and communicated from dependents to dependencies.

Rust

Bottom-Up

Starting from the root’s dependencies and communicated to dependents.

Asyncio·Trio

Simultaneous

To all transitive dependencies at once.

Swift

Persistence

[For Aware Cancellation]How long a cancellation of a task lasts.

Transient

A task can ignore cancellation and proceed as normal.

Asyncio

Persistent

A task can ignore cancellation but remains cancelled.

Trio·Swift

Two of these axes are particularly relevant for our example program. Languages withDynamic Extentdo not allow tasks to outlive the functions in which they were spawned. Unlike the other languages, Swift and Python+Trio chose Dynamic Extent. This means that within the functionfire_and_forget, the task associated withwrite_to_logcannot outlive the functionfire_and_forget.

Although Swift and Trio both chose Dynamic Extent, they differ in choice of Destruction. At the end of thefire_and_forgetfunction scope, Swift usesCancelled Destruction,and cancelstaskwhile Trio usesAwaited Destructionand politely waits forwrite_to_logto finish. The choices of Extent and Destruction explain why Swift prints “AC” and Trio prints “ABC”.

Each design dimension has trade-offs of performance, memory usage, ergonomics, semantics, etc. There’s no right or wrong answers, and each language has its own design rationale. But with so many decisions, explaining the output for even small programs becomes quite involved!

To make our design space more precise, we translated it into a formal semantics on a core calculus of asynchronous programs. This model lets us explain exactly why the sample program diverges by tracing its execution.

The figure below provides a glimpse of how this formal model can be used to explain different execution outcomes. The figure shows the trace of the model, highlighting the semantic decisions that lead to different outcomes. Each box is an abstract-machine state. Each arrow is a small-step reduction, labeled with the rules that fire. Most rules behave identically in every runtime; the highlighted ones are the design decisions, and each highlight is a fork in the road.

async
 
fn
 
write_to_log
():
 
print
 
“A”
; 
await
 
sleep
(
2
); 
print
 
“B"
async
 
fn
 
fire_and_forget
():
 task = 
spawn
 
write_to_log
()
async
 
fn
 
main
():
 
await
 
fire_and_forget
();
 
await
 
sleep
(
1
); 
print
 
“C"
block_on
(
main
())
out: ε
acjkmrs
C[ 
spawn
 
write_to_log
() ]
out: ε
acjkmrs
C[ task ]
T: (
2
, write_to_log, 
print
 
“B”
)
out: A
cj
C[ task;
 
cancel task;
 
try
 
await task
 
catch e -> ()
]
Q: 
print
 
“A”
; 
await
 
sleep
(
2
); 
print
 
“B"
out: ε
s
C[ 
spawn
 coro ]
out: ε
akmr
C[ task ]
Q: 
print
 
“A”
; 
await
 
sleep
(
2
); 
print
 
“B"
out: ε
akm
C[ task; 
await task
 ]
Q: 
print
 
“A”
; 
await
 
sleep
(
2
); 
print
 
“B"
out: ε
r
block_on
(())
T: (
2
, write_to_log, 
print
 
“B”
)
out: AC
acjk
C[ 
throw “cancelled”
 ]
out: A
s
(); 
await
 
sleep
(
1
); 
print
 
“C"
out: A
s
(); 
await
 
sleep
(
1
); 
print
 
“C"
out: ε
m
(); 
await
 
sleep
(
1
); 
print
 
“C"
out: AB
r
out: ACB
j
out: C
m
out: AC
acks
out: ABC
r
Block-Wait
Async-App
Await
Async-App
eager
OS-IO
Async-App
semi-eager
Async-App
lazy
Spawn
dynamic
Spawn
indefinite
OS-IO
Signal
Schedule
Schedule
OS-IO
Signal
Cancel-Unstarted
OS-IO
Signal
Schedule
Block-Done
Schedule
OS-IO
Signal
Await-Task
OS-IO
Signal
Schedule
Block-Done
Schedule
OS-IO
Await
Catch-Exn
OS-IO
Signal
Schedule
Block-Done
Block-Done
terminated
Signal
Schedule
Block-Done
awaited
languages
a
 = 
Asyncio
c
 = 
C#
j
 = 
JavaScript
k
 = 
Tokio
m
 = 
Smol
r
 = 
Trio
s
 = 
Swift

To understand this diagram, and the decisions that went into designing your favorite language’s async/await system, read our new paper“A Design Space Exploration of Async/Await”!