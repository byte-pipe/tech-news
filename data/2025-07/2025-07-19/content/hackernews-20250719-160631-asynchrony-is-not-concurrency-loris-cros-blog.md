---
title: Asynchrony is not Concurrency | Loris Cro's Blog
url: https://kristoff.it/blog/asynchrony-is-not-concurrency/
site_name: hackernews
fetched_at: '2025-07-19T16:06:31.158662'
original_url: https://kristoff.it/blog/asynchrony-is-not-concurrency/
author: kristoff_it
date: '2025-07-19'
description: Yes I know about that one talk from Rob Pike.
---

# Loris Cro

Personal Website

About

 	  •  

Twitter

 	  •  

Twitch

 	  •  

YouTube

 	  •  

GitHub

# Asynchrony is not Concurrency

July 18, 2025•12min read • byLoris Cro

Yes I know about that one talk from Rob Pike.

The title of this blog post is not something you hear people say often, if ever. What you do hear people say is “concurrency is not parallelism”, but that’s not as useful, in my opinion.

Let’s see how Wikipedia defines those terms:

Concurrencyrefers to the ability of a system to execute multiple tasks through simultaneous execution or time-sharing (context switching)

Parallel computingis a type of computation in which many calculations or processes are carried out simultaneously.

What if I told you we’re missing a term to describe another aspect of concurrent programming and, because of it, we’re all collectively missing a key piece of understanding that has shaped our software ecosystems for the worse?

Well, I spoiled it in the title: the missing term is ‘asynchrony’, but why?

## Two files

Say that you have to save two files and order does not matter:

io
.
async
(
saveFileA
,

.
{
io
}
)
;

io
.
async
(
saveFileB
,

.
{
io
}
)
;

A could be saved before B, or B could be saved before A, and all would be fine. You could also writesome ofA, thensome ofB, and then back to A, to finally complete writing B. That also would be correct, and in fact that’s what tends to happen when using evented I/O to save sufficiently complex files concurrently.

But, most importantly,it’s perfectly legitimate to do all the work to save one file first and, only once that’s done, to begin saving the second file. Maybe that would not be the most efficient thing to do, but the code would still be correct.

## Two sockets

Let’s take a look now at another example: say that you need to create a TCP server and connect to itfrom within the same program.

io
.
async
(
Server
.
accept
,

.
{
server
,

io
}
)
;

io
.
async
(
Cient
.
connect
,

.
{
client
,

io
}
)
;

Like before, the order doesn’t matter: the client could begin a connection before the server starts accepting (the OS will buffer the client request in the meantime), or the server could start accepting first and wait for a bit before seeing an incoming connection.

Unlike before,it is mandatory that the execution of both tasks overlap.

In the file example it was fine to do all the work for A first and all the work for B last, but not in this second case, because the server needs to be activewhilethe client tries to connect.

## Asynchrony, Concurrency, Parallelism

In common lingo, we would describe both the code snippets presented above as “concurrent” and stop there, but that will lose us some nuance, so here’s my proposed definitions for these terms:

Asynchrony: the possibility for tasks to run out of order and still be correct.

Concurrency: the ability of a system to progress multiple tasks at a time, be it via parallelism or task switching.

Parallelism: the ability of a system to execute more than one task simultaneously at the physical level.

With these definitions in hand, here’s a better description of the two code snippets from before: both scripts express asynchrony, but the second onerequiresconcurrency.

## Why even bother?

Ok, cool, we now can be more precise when describing code snippets, so what did we gain?

For dramatic effect, allow me to answer this question in the negative and tell you what it is that we lost by not being aware enough of the difference between asynchrony and concurrency.

Because of our lack of understanding:

We have created language ecosystems where library authors must duplicate effort (e.g.redis-pyvsasyncio-redis) orworse.

We have created aworseexperiencefor library users where async code is viral and where a even a single dependency with async code demands that users give up their ability to write normal, synchronous code.

And to mitigate all these problems, we have created unholy escape hatches that cause suboptimal behavior at best anddeadlocksat worst.

Let’s switch back to answering the question in the positive.

## In Zig Asynchrony is not Concurrency

I already wrote a blog post onZig’s new async I/Ostory, but I only dedicated a short section at the end on this aspect, which led me to expand on it in this post.

In Zig asynchrony is not concurrency because the usage ofio.asyncdoes not imply concurrency. In other words: code that usesio.asynccan be run in single-threaded blocking mode.

Let’s look again at the file example:

io
.
async
(
saveFileA
,

.
{
io
}
)
;

io
.
async
(
saveFileB
,

.
{
io
}
)
;

When run in single-threaded blocking mode, the code above will be equivalent to this:

saveFileA
(
io
)
;

saveFileB
(
io
)
;

It’s easy to imagine how this can be done, allio.asynchas to do is run the given function immediately (instead of spawning a new thread for it, or doing any other form of task switching).

This means that a library author can useio.asyncin their code and not force their users to move away from single-threaded blocking I/O.

Conversely, code that doesnotuseio.asynccan still take advantage of concurrency. But wouldn’t doing that cause deadlocks?

The answer is that this is an ill-posed question. What makes synchronous code behave well in the presence of concurrency are two things (aside from plain multithreading):

1. Usage of evented I/O syscalls (io_uring, epoll, kequeue, etc.) instead of blocking ones.
2. Usage of task switching primitives to continue doing work while I/O operations are being carried out by the OS.

Neither of these things is something you see at the surface level (so looking at synchronous code tells you usually very little) and especially wrt the second point,asyncis not the task switching primitive, because it only concerns itself with asynchrony, not concurrency (and task switching is – by the definition I gave above – a concept specific to concurrency).

The task switching primitive is usually calledyield, let’s take a look at how that works in the case of green threads:

Take the synchronous code example again, wrap it in a function for extra clarity and let’s also pass down the names of the two files to write. This last change will become useful in a moment.

fn

saveData
(


io
:

Io
,


nameA
:

[
]
const

u8
,


nameB
:

[
]
const

u8

)

!
void

{


try

saveFileA
(
io
,

nameA
)
;


try

saveFileB
(
io
,

nameB
)
;

}

When we executesaveDatawe callsaveFileAwhich in turn will, at some point, call a function to write bytes to a file. In Zig’s design this is done by using anioparameter, but there are plenty of different ways to make this work. What matters is that at some point we get to an implementation ofwritespecific to the green threads execution model.

Thewritefunction will request to perform a write to the file and then, instead of blocking while the operation is carried out, the syscall will return immediately (in the case of io_uring it’s not even a syscall, it’s just a memory write to a ring buffer).

At this point the write operation has been submitted and our program needs to switch to a different task while this one waits for the operation to complete. In other words, we need to yield.

In the case of green threads, yielding is performed by stack swapping. We save at a location in memory the state of all general purpose registers in the CPU (including program counter and stack pointer), and we load another “snapshot” from memory to the CPU (again, including program counter and stack pointer which now point to machine code in a different part of the executable, and to a different stack in memory).

The snapshot that we’re loading was previously saved using this same technique by the event loop which yielded to resume a task that was reported as ready to resume by a notification from the OS. Now that we’re switching back to the event loop, the same will happen again.

While I described stack swapping with some level of detail, it should be noted that this is more or less the same way in which your OS schedules threads on CPU cores. If you want to see a fully concrete example of stack swapping in action, I’veimplemented it live on Twitch in a barebones riscv32 kernel.

I won’t get into the weeds of a stackless coroutines implementation, but the core principle is the exact same: designing a yielding primitive that lets you switch tasks.Hereyou can see the latest proposal for Zig, where historically the stackless task switching primitive has been implemented bysuspendandresume.

Now that task switching is clear, let’s go back to the event loop. IfsaveDatais written in a synchronous manner, what can the event loop do while it waits for evented I/O to complete?

The answer is that it depends on the rest of the program. Concurrency needs to exploit asynchrony and, if there’s none, then no tasks can be in execution at the same time, like in this case for example:

pub

fn

main
(
)

!
void

{


const

io

=

newGreenThreadsIo
(
)
;


try

saveData
(
io
,

"a.txt"
,

"b.txt"
)
;

}

But the fact thatsaveDatadoesn’t express asynchrony does not prevent other parts of the program from expressing it:

pub

fn

main
(
)

!
void

{


const

io

=

newGreenThreadsIo
(
)
;


io
.
async
(
saveData
,

.
{
io
,

"a"
,

"b"
}
)
;


io
.
async
(
saveData
,

.
{
io
,

"c"
,

"d"
)
;

}

In this case the two different calls tosaveDatacan be scheduled concurrently because they are asynchronous to one another, and the fact that they don’t express any internal asynchrony does not compromise the execution model.

This allows normal synchronous code and asynchronous code to run concurrently in the same program without any issue.No need for code duplication of libraries, and no need for users to accept Faustian bargains in order to use an “async library” (note how that terminology is meaningless in light of our new understanding, that is just “a library” now!).

If this result feels surprising to you, it’s probably because you’re used to async being tied to stackless coroutines, which normally causes the usage ofasyncandawaitkeywords to propagate virally throughout the code. But, as an example, Go doesn’t have this same problem: most code is synchronous and yet Go does run goroutines concurrently (because all I/O is evented and because Go can task switch).

We’re finally ready to look at one final example to complete our understanding!

## Concurrency as a requirement

For convenience, here’s a copy of the definitions I’ve introduced in the beginning:

Asynchrony: the possibility for tasks to run out of order and still be correct.

Concurrency: the ability of a system to progress multiple tasks at a time, be it via parallelism or task switching.

Parallelism: the ability of a system to execute more than one task simultaneously at the physical level.

Now let’s take a look again at the client-server example:

io
.
async
(
Server
.
accept
,

.
{
server
,

io
}
)
;

io
.
async
(
Cient
.
connect
,

.
{
client
,

io
}
)
;

As mentioned earlier, this situation is different than thesaveDataone. HereServer.acceptandClient.connectrequire concurrency because blocking onServer.acceptwill preventClient.connectfrom ever executing.

Unfortunately this code doesn’t express this requirement, which is why I called it a programming error when I presented this example in my post about Zig’s new async I/O.

This is how you will solve it in Zig:

try

io
.
asyncConcurrent
(
Server
.
accept
,

.
{
server
,

io
}
)
;

io
.
async
(
Cient
.
connect
,

.
{
client
,

io
}
)
;

asyncConcurrentguarantees thatServer.acceptwill run concurrently with the rest of the code. This documents in the code that concurrency is required for correctness, which will also let the program error out when attempting to run it over a non-concurrentIoimplementation. But that’s not all!

Did you notice thatio.asyncdoes not need to betryed?

Let’s imagine that we’re running our program over an implementation ofIothat spawns a new OS thread for each async task. If it can’t error out, what happens when there are too many threads active at the same time? Does it just crash?

No, it runs the function directly!

This is a snippet from the currentIoimplementation that uses green threads, where a similar concept applies: each green thread (calledFiberin the implementation) needs to be allocated in memory and, if that fails, the function is simply run immediately:

const

fiber

=

Fiber
.
allocate
(
event_loop
)

catch

{


// The next line runs the function


// passed as an argument to io.async


start
(
context
.
ptr
,

result
.
ptr
)
;


return

null
;

}
;

Just to drive the point home one last time: this is a legitimate thing to do because asynchrony does not imply concurrency.io.asyncConcurrentdoes guarantee concurrency instead, and that’s why it has to be a failable function.

Before we jump to the last section about conclusions, I’d like to point out that the code snippets above are all realistic but, to remove clutter, I have omitted error handling and the code that awaits futures returned from async calls. Readmy other blog postto see complete code snippets, although that is not necessary to understand this post.

## Conclusions

First and foremost, I hope to have convinced you that asynchrony is not concurrency.

Secondly,Ihope to have givenyouhope that we can climb out of the current async/await local minima that afflicts most implementations, that code doesn’t have to be duplicated, and that both asynchronous and synchronous code can co-exist in the same codebasewithout any compromise.

Lastly, I hope to have given you an intuition for how async I/O is going to work in Zig.

If you want to have a sneak peek of the upcoming Zig async I/O redesign,Monday 21st of July 2025 at 7pm CEST I will belive on Twitch(more timezones and info here) with Andrew to read the thread pool implementation, the green threads implementation, and to write myself a non-concurrent implementation ofIoin order to test live if everything that I talked about in this post is actually true.

Spoilers: I already tried and it all works. Welcome to theFuturewe’ve been all awaiting.

←

Zig's New Async I/O

  or  

Back to the Homepage
