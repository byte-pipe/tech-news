---
title: Async/await on the GPU - VectorWare
url: https://www.vectorware.com/blog/async-await-on-gpu/
site_name: hnrss
content_file: hnrss-asyncawait-on-the-gpu-vectorware
fetched_at: '2026-02-18T11:19:53.620180'
original_url: https://www.vectorware.com/blog/async-await-on-gpu/
date: '2026-02-17'
published_date: '2026-02-17T00:00:00Z'
description: GPU code can now use Rust's async/await. We share the reasons why and what this unlocks for GPU programming.
tags:
- hackernews
- hnrss
---

AtVectorWare, we are building the firstGPU-native software company. Today, we are excited to
announce that we can successfully use Rust'sFuturetrait andasync/awaiton the GPU. This milestone marks a significant step towards our vision
of enabling developers to write complex, high-performance applications that leverage the
full power of GPU hardware using familiar Rust abstractions.

## Concurrent programming on the GPU

GPU programming traditionally focuses on data parallelism. A developer writes a single
operation and the GPU runs that operation in parallel across different parts of the
data.

fn
 conceptual_gpu_kernel
(data) {

 // All threads in all warps do the same thing to different parts of data

 data[thread_id]
=
 data[thread_id]
*
 2
;

}

This model works well for standalone and uniform tasks such as graphics rendering,
matrix multiplication, and image processing.

As GPU programs grow more sophisticated, developers usewarp
specializationto introduce more complex
control flow and dynamic behavior. With warp specialization, different parts of the GPU
run different parts of the program concurrently.

fn
 conceptual_gpu_kernel
(data) {

 let
 communication
=
 ...
;

 if
 warp
==
 0
 {

 // Have warp 0 load data from main memory

 load
(data, communication);

 }
else
 if
 warp
==
 1
 {

 // Have warp 1 compute A on loaded data and forward it to B

 compute_A
(communication);

 }
else
 {

 // Have warp 2 and 3 compute B on loaded data and store it

 compute_B
(communication, data);

 }

}

Warp specialization shifts GPU logic from uniform data parallelism to explicit
task-based parallelism. This enables more sophisticated programs that make better use of
the hardware. For example, one warp can load data from memory while another performs
computations to improve utilization of both compute and memory.

This added expressiveness comes at a cost. Developers must manually manage concurrency
and synchronization because there is no language or runtime support for doing so.
Similar to threading and synchronization on the CPU, this is error-prone and difficult
to reason about.

## Better concurrent programming on the GPU

There are many projects that aim to provide the benefits of warp specialization without
the pain of manual concurrency and synchronization.

JAXmodels GPU programs as computation graphs that encode
dependencies between operations. The JAX compiler analyzes this graph to
determine ordering, parallelism, and placement before generating the program that
executes. This allows JAX to manage and optimize execution while presenting a high-level
programming model in a Python-based DSL. The same model supports multiple hardware
backends, including CPUs and TPUs, without changing user code.

Tritonexpresses computation in terms of blocks
that execute independently on the GPU. Like JAX, Triton uses a Python-based DSL to
define how these blocks should execute. The Triton compiler lowers block definitions
through amulti-level
pipelineofMLIR
dialects, where it applies
block-level data-flow analysis to manage and optimize the generated program.

More recently, NVIDIA introducedCUDA Tile.
Like Triton, CUDA Tile organizes computation around blocks. It additionally introduces
"tiles" as first-class units of data. Tiles make data dependencies explicit rather than
inferred, which improves both performance opportunities and reasoning about correctness.
CUDA Tile ingests code written in existing languages such as Python, lowers it to an
MLIR dialect calledTile IR, and executes on the
GPU.

We are excited and inspired by these efforts, especially CUDA Tile. We think it is a
great idea to have GPU programs structured around explicit units of work and data,
separating the definition of concurrency from its execution. We believe that GPU
hardware aligns naturally withstructured
concurrencyand changing the
software to match will enable safer and more performant code.

## The downsides of current approaches

These higher-level approaches to GPU programming require developers to structure code in
new and specific ways. This can make them a poor fit for some classes of applications.

Additionally, a new programming paradigm and ecosystem is a significant barrier to
adoption. Developers use JAX and Triton primarily for machine learning workloads where they
align well with the underlying computation. CUDA Tile is newer and more general but has
yet to see broader adoption. Virtually no one writes their entire application with these
technologies. Instead, they write parts of their application in these frameworks and
other parts in more traditional languages and models.

Code reuse is also limited. Existing CPU libraries assume a conventional language
runtime and execution model and cannot be reused directly. Existing GPU libraries rely
on manual concurrency management and similarly do not compose with these frameworks.

Ideally, we want an abstraction that captures the benefits of explicit and structured
concurrency without requiring a new language or ecosystem. It should compose with
existing CPU code and execution models. It should provide fine-grained control when
needed, similar to warp specialization. It should also provide ergonomic defaults for the
common case.

## Rust'sFuturetrait andasync/await

We believe Rust'sFuturetrait andasync/awaitprovide such an abstraction. They encode structured
concurrencydirectly in an existing language without committing to a specific execution
model.

A future represents a computation that may not be complete yet. A future does not
specify whether it runs on a thread, a core, a block, a tile, or a warp. It does not
care about the hardware or operating system it runs on. TheFuturetraititself is intentionally
minimal. Its core operation ispoll, which
returns eitherReadyorPending.
Everything else is layered on top. This separation is what allows the same async code to
be driven in different environments. For more detailed info, see theRust async
book.

Like JAX's computation graphs, futures are deferred and composable.Developers construct programs as values before executing them.
This allows the compiler to analyze dependencies and composition ahead of execution
while preserving the shape of user code.

Like Triton's blocks, futures naturally express independent units of concurrency.
Depending on how futures are combined, they represent whether a block of work runs
serially or in parallel. Developers express concurrency using normal Rust control flow,
trait implementations, and future combinators rather than a separate DSL.

Like CUDA Tile's explicit tiles and data dependencies, Rust's ownership model makes data
constraints explicit in the program structure.Futures capture the data they operate on and that captured
state becomes part of the compiler-generated state machine. Ownership, borrowing,Pin, and bounds such asSendandSyncencode how data can be
shared and transferred between concurrent units of work.

Warp specialization is not typically described this way, but in effect, it reduces to
manually written task state machines.Futures compile down to state machines that the Rust compiler generates and manages
automatically.

Because Rust's futures are just compiler-generated state machines there is no reason
they cannot run on the GPU. That is exactly what we have done.

## A world first:async/awaitrunning on the GPU

Runningasync/awaiton the GPU is difficult to demonstrate visually because the code
looks and runs like ordinary Rust. By design, the same syntax used on the CPU runs
unchanged on the GPU.

Here we define a small set of async functions and invoke them from a single GPU kernel
usingblock_on. Together, they exercise the core features of Rust's async model:
simple futures, chained futures, conditionals, multi-step workflows, async blocks, and
third-party combinators.

// Simple async functions that we will call from the GPU kernel below.



async
 fn
 async_double
(x
:
 i32
)
->
 i32
 {

 x
*
 2

}



async
 fn
 async_add_then_double
(a
:
 i32
, b
:
 i32
)
->
 i32
 {

 let
 sum
=
 a
+
 b;

 async_double
(sum)
.await

}



async
 fn
 async_conditional
(x
:
 i32
, do_double
:
 bool
)
->
 i32
 {

 if
 do_double {

 async_double
(x)
.await

 }
else
 {

 x

 }

}



async
 fn
 async_multi_step
(x
:
 i32
)
->
 i32
 {

 let
 step1
=
 async_double
(x)
.await
;

 let
 step2
=
 async_double
(step1)
.await
;

 step2

}



#[
unsafe
(no_mangle)]

pub
 unsafe
 extern
 "ptx-kernel"
 fn
 demo_async
(

 val
:
 i32
,

 flag
:
 u8
,

) {

 // Basic async functions with a single await execute correctly on the device.

 let
 doubled
=
 block_on
(
async_double
(val));



 // Chaining multiple async calls works as expected.

 let
 chained
=
 block_on
(
async_add_then_double
(val, doubled));



 // Conditionals inside async code are supported.

 let
 conditional
=
 block_on
(
async_conditional
(val, flag));



 // Async functions with multiple await points also work.

 let
 multi_step
=
 block_on
(
async_multi_step
(val));



 // Async blocks work and compose naturally.

 let
 from_block
=
 block_on
(
async
 {

 let
 doubled_a
=
 async_double
(val)
.await
;

 let
 doubled_b
=
 async_double
(chained)
.await
;

 doubled_a
.
wrapping_add
(doubled_b)

 });



 // CPU-based async utilities also work. Here we use combinators from the

 // `futures_util` crate to build and compose futures without writing new

 // async functions.

 use
 futures_util
::
future
::
ready;

 use
 futures_util
::
FutureExt
;



 let
 from_combinator
=
 block_on
(

 ready
(val)
.
then
(
move
 |
v
|
 ready
(v
.
wrapping_mul
(
2
)
.
wrapping_add
(
100
)))

 );

}

Getting this all working required fixing bugs and closing gaps across multiple compiler
backends. We also encountered issues in NVIDIA'sptxastool, which we reported and
worked around.

## Executors on the GPU

Usingasync/awaitmakes it ergonomic to express concurrency on the GPU. However, in
Rust futures do not execute themselves and must be driven to completion by an executor.
Rust deliberately does not include a built-in executor and instead third parties provide
executors with different features and tradeoffs.

Our initial goal was to prove that Rust's async model could run on the GPU at all. To do
that, we started with a simpleblock_onas our
executor.block_ontakes a single future and drives it to completion by repeatedly
polling it on the current thread. While simple and blocking, it was sufficient to
demonstrate that futures andasync/awaitcould compile to correct GPU code. While
theblock_onexecutor may seem limiting, because futures are lazy and composable we
were still able to express complex concurrent workloads via combinators and async
functions.

Once we had futures working end to end, we moved to a more capable executor. The Embassy
executor isdesigned for embedded systemsand operates in Rust's#![no_std]environment. This makes it a natural fit for GPUs, which lack a traditional
operating system and thus do not support Rust's standard library. Adapting it to run on
the GPU required very few changes. This ability to reuse existing open source libraries
is much better than what exists in other (non-Rust) GPU ecosystems.

Here we construct three independent async tasks that loop indefinitely and increment
counters in shared state to demonstrate scheduling.The tasks themselves do not perform useful computation. Each task awaits a simple
future that performs work in small increments and yields periodically. This allows the
executor to interleave progress between tasks.

#![no_std]

#![feature(abi_ptx)]

#![feature(stdarch_nvptx)]



use
 core
::
future
::
Future
;

use
 core
::
pin
::
Pin
;

use
 core
::
sync
::
atomic
::
{
AtomicU32
,
Ordering
};

use
 core
::
task
::
{
Context
,
Poll
};



use
 embassy_executor
::
Executor
;

use
 ptx_embassy_shared
::
SharedState
;



pub
 struct
 InfiniteWorkFuture
 {

 pub
 shared
:
 &
'
static
 SharedState

 pub
 iteration_counter
:
 &
'
static
 AtomicU32
,

}



impl
 Future
 for
 InfiniteWorkFuture
 {

 type
 Output
 =
 ();



 fn
 poll
(
self
:
 Pin
<
&mut
 Self
>, cx
:
 &mut
 Context
<'
_
>)
->
 Poll
<()> {

 // Check if host requested stop

 if
 self
.
shared
.
stop_flag
.
load
(
Ordering
::
Relaxed
)
!=
 0
 {

 unsafe
 {
core
::
arch
::
nvptx
::
trap
() };

 }



 // Track iterations and activity for demonstration purposes

 self
.
iteration_counter
.
fetch_add
(
1
,
Ordering
::
Relaxed
);

 self
.
shared
.
last_activity
.
fetch_add
(
1
,
Ordering
::
Relaxed
);



 // Simulate work

 unsafe
 {

 core
::
arch
::
nvptx
::
_nanosleep
(
100
);

 }



 cx
.
waker
()
.
wake_by_ref
();

 Poll
::
Pending

 }

}



// Three very similar tasks, incrementing different variables

#[embassy_executor
::
task]

async
 fn
 task_a
(shared
:
 &
'
static
 SharedState
) {

 InfiniteWorkFuture
 {

 iteration_counter
:
 &
shared
.
task_a_iterations,

 shared,

 }
.await

}



#[embassy_executor
::
task]

async
 fn
 task_b
(shared
:
 &
'
static
 SharedState
) {

 InfiniteWorkFuture
 {

 iteration_counter
:
 &
shared
.
task_b_iterations,

 shared,

 }
.await

}



#[embassy_executor
::
task]

async
 fn
 task_c
(shared
:
 &
'
static
 SharedState
) {

 InfiniteWorkFuture
 {

 iteration_counter
:
 &
shared
.
task_c_iterations,

 shared,

 }
.await

}



#[
unsafe
(no_mangle)]

pub
 unsafe
 extern
 "ptx-kernel"
 fn
 run_forever
(shared_state
:
 *mut
 SharedState
) {



 // ... executor setup and initialization ...



 // Safety: the CPU needs to ensure the buffer says alive

 // for as long as this is running

 let
 shared
=
 unsafe
 {
&const
 (
*
shared_state) };

 executor
.
run
(
|
spawner
|
 {

 if
 let
 Ok
(token)
=
 task_a
(shared) {

 spawner
.
spawn
(token);

 }

 if
 let
 Ok
(token)
=
 task_b
(shared) {

 spawner
.
spawn
(token);

 }

 if
 let
 Ok
(token)
=
 task_c
(shared) {

 spawner
.
spawn
(token);

 }

 });

}

Below is anAsciinemarecording of the GPU running the async
tasks via Embassy's executor. Performance is not representative as the example runs
empty infinite loops and uses atomics to track activity. The important point is that
multiple tasks execute concurrently on the GPU, driven by an existing, production-grade
executor using Rust's regularasync/await.

Taken together, we think Rust and its async model are a strong fit for the GPU. Notably,
similar ideas are emerging in other language ecosystems, such as NVIDIA'sstdexecwork for C++. The difference is these
abstractions already exist in Rust, are widely used, and are supported by a mature
ecosystem of executors and libraries.

## Downsides of Rust'sasync/awaiton the GPU

Futures are cooperative. If a future does not yield, it can starve other work and degrade
performance. This is not unique to GPUs, as cooperative multitasking on CPUs has the
same failure mode.

GPUs do not provide interrupts. As a result, an executor running on the device must
periodically poll futures to determine whether they can make progress. This involves
spin loops or similar waiting mechanisms. APIs such asnanosleepcan trade latency for efficiency, but this remains less efficient than interrupt-driven
execution and reflects a limitation of current GPU architectures. We have some ideas for
how to mitigate this and are experimenting with different approaches.

Driving futures and maintaining scheduling state increases register pressure. On GPUs,
this can reduce occupancy and impact performance.

Finally, Rust's async model on the GPU still carries the samefunction coloring
problemthat exists on the CPU.

## Future work

On the CPU, executors such asTokio,Glommio, andSmolmake different tradeoffs around scheduling,
latency, and throughput. We expect a similar diversity to emerge on the GPU. We are
experimenting with GPU-native executors designed specifically around GPU hardware
characteristics.

A GPU-native executor could leverage mechanisms such asCUDA
Graphsor CUDA Tile for efficient task scheduling or shared memory for fast communication
between concurrent tasks. It could also integrate more deeply with GPU scheduling
primitives than a direct port of an embedded or CPU-focused executor.

At VectorWare, we have recentlyenabledstdon the GPU.
Futures areno_stdcompatible, so this does not impact their core functionality.
However, having the Rust standard library available on the GPU opens the door to richer
runtimes and tighter integration with existing Rust async libraries.

Finally, while we believe futures andasync/awaitmap well to GPU hardware and align
naturally with efforts such as CUDA Tile, they are not the only way to express
concurrency. We are exploring alternative Rust-based approaches with different tradeoffs
and will share more about those experiments in future posts.

## Is VectorWare only focused on Rust?

We completed this work months ago. The speed at which we are able to make progress on
the GPU is a testament to the power of Rust's abstractions and ecosystem.

As a company, we understand that not everyone uses Rust. Our future products will
support multiple programming languages and runtimes. However, we believe Rust is
uniquely well suited to building high-performance, reliable GPU-native applications and
that is what we are most excited about.

## Follow along

Follow us onX,Bluesky,LinkedIn, or subscribe to ourblogto stay updated on our progress. We will be sharing more about our work in
the coming months. You can also reach us athello@vectorware.com.
