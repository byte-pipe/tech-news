---
title: How Python's GIL actually works (and when it bites you) - DEV Community
url: https://dev.to/lovestaco/how-pythons-gil-actually-works-and-when-it-bites-you-3f2
site_name: devto
content_file: devto-how-pythons-gil-actually-works-and-when-it-bites-y
fetched_at: '2026-05-15T11:42:18.981364'
original_url: https://dev.to/lovestaco/how-pythons-gil-actually-works-and-when-it-bites-you-3f2
author: Athreya aka Maneshwar
date: '2026-05-10'
description: Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is... Tagged with webdev, productivity, programming, python.
tags: '#webdev, #productivity, #programming, #python'
---

Hello, I'm Maneshwar. I'm building git-lrc, a Micro AI code reviewer that runs on every commit. It is free and source-available on Github.Star Usto help devs discover the project. Do give it a try and share your feedback for improving the product.

I remember the first time the GIL ruined my evening.

I was working onFreeDevToolsand had a script that needed to parse, validate, and rewrite metadata for a few hundred thousand small markdown files and finally stores it into sqlite DB.

The bulk of my work was pure Python, a lot of looping, dictionary lookups, string concatenation, and small object churn. No NumPy, no Pillow, no native libraries doing the heavy lifting.

The single-threaded version was going to take forever, so I did what any reasonable person would do, I threw threads at it.

Eight worker threads. Should be a lot faster, right?

It was the same speed. Maybe a hair slower. I stared at the terminal for a solid minute thinking I'd done something wrong.

I had not done something wrong. I had met the GIL.

## So what is it

GIL stands forGlobal Interpreter Lock.

The short version: it's a lock inside CPython (the standard Python you almost certainly use) that ensures only one thread executes Pythonbytecodeat a time, within a single interpreter.

That word "bytecode" is doing a lot of work, and we'll come back to it.For now, the simple version is: even if your laptop has 16 cores and you spin up 50 threads, only one of those threads is running Python code at any given instant. The rest are waiting their turn.

The threads do take turns.

CPython periodically gives other waiting threads a chance to acquire the GIL (the interval is 5 ms by default, tunable viasys.setswitchinterval()).

The actual handoff happens at the next safe point in the bytecode evaluation loop, so things look concurrent, even though no two threads are executing Python in parallel.

An analogy: you can hire ten cooks, but if there's only one knife, nine of them are watching the tenth one chop onions. They can rotate, but they can't chop simultaneously (Unless one of the cooks leaves the kitchen to wait for ingredients, which is roughly what happens during blocking I/O.)

One important caveat before we go further:the GIL is a CPython thing.Other Python runtimes like Jython and IronPython don't use the same GIL model, and modern CPython now also ships an experimental free-threaded build.

When people say "Python has a GIL," they really mean "the most common Python implementation has a GIL."

## Why does this exist

Not because anyone was lazy. The GIL is a real engineering tradeoff.

Python primarily manages memory with reference counting, plus a cyclic garbage collector for reference cycles.

Every variable assignment, every function call, every time you stuff something into a list, there's a counter being incremented or decremented in the background.

If two threads update those counters simultaneously without coordination, you get race conditions, and race conditions in memory management lead to crashes and corrupted data.

The alternatives to the GIL is fine-grained locking on every object, or rewriting the memory model that come with their own costs: more overhead per operation, slower single-threaded code, and a much harder life for anyone writing C extensions.

Much of the C extension ecosystem (NumPy, Pillow, lxml, every database driver) was built assuming the GIL exists. Rewriting all of that for thread safety is a generational project.

So the GIL stuck around because the tradeoff genuinely favored it: simpler implementation, faster single-threaded code, and an easy contract for C extensions.

The cost was no parallel execution of Python bytecode and for most users, that tradeoff was acceptable.

## Let's actually see it

Here's a script that demonstrates the limitation. Two heavy countdowns, run sequentially, then again with threads:

import
 
time

import
 
threading

def
 
countdown
(
n
):

 
while
 
n
 
>
 
0
:

 
n
 
-=
 
1

COUNT
 
=
 
50_000_000

start
 
=
 
time
.
time
()

countdown
(
COUNT
)

countdown
(
COUNT
)

print
(
f
"
sequential: 
{
time
.
time
()
 
-
 
start
:
.
2
f
}
s
"
)

start
 
=
 
time
.
time
()

t1
 
=
 
threading
.
Thread
(
target
=
countdown
,
 
args
=
(
COUNT
,))

t2
 
=
 
threading
.
Thread
(
target
=
countdown
,
 
args
=
(
COUNT
,))

t1
.
start
();
 
t2
.
start
()

t1
.
join
();
 
t2
.
join
()

print
(
f
"
threaded: 
{
time
.
time
()
 
-
 
start
:
.
2
f
}
s
"
)

Enter fullscreen mode

Exit fullscreen mode

This benchmark is intentionally synthetic, a real workload has more nuance but it makes the core limitation visible in a way nothing else does.

## The plot twist: threading isn't useless

Here's the part that took me embarrassingly long to internalize.

The GIL is released when Python is doing blocking I/O or, more precisely, when the C code implementing that I/O explicitly releases it.

Reading a file, waiting on a network request, querying a database, sleeping, the underlying C call releases the GIL during the wait, lets other threads run, then reacquires it on the way back.

Which means threading is genuinely useful, just not for what I initially thought.

import
 
time

import
 
threading

def
 
fake_request
():

 
time
.
sleep
(
2
)
 
# pretend this is a network call

start
 
=
 
time
.
time
()

fake_request
()

fake_request
()

fake_request
()

print
(
f
"
sequential: 
{
time
.
time
()
 
-
 
start
:
.
2
f
}
s
"
)

start
 
=
 
time
.
time
()

threads
 
=
 
[
threading
.
Thread
(
target
=
fake_request
)
 
for
 
_
 
in
 
range
(
3
)]

for
 
t
 
in
 
threads
:
 
t
.
start
()

for
 
t
 
in
 
threads
:
 
t
.
join
()

print
(
f
"
threaded: 
{
time
.
time
()
 
-
 
start
:
.
2
f
}
s
"
)

Enter fullscreen mode

Exit fullscreen mode

The rule of thumb that finally clicked for me:

* if your workload is mostlywaiting on I/O, threads often help a lot
* if your workload is mostlycomputing in pure Python bytecode, threads usually won't speed it up

Web scrapers, API clients, anything that talks to a database or the filesystem for this, threading (orasyncio) is great.

Tight pure-Python loops that crunch data, threads will let you down.

Quick aside onasyncio, since it keeps coming up:asyncioisn't an alternative to threading for using more cores.

It'sconcurrency in a single threadi.e one event loop juggling many I/O-bound coroutines without the overhead of OS threads.

It's excellent for high-concurrency I/O workloads, but it does not bypass the GIL for CPU-bound Python code.

If your workload is CPU-bound,asynciowon't probably save you either.

## When threadsdouse multiple cores

This is the section I wish someone had handed me a year ago.

The GIL only restricts execution ofPython bytecode.

C extensions can release the GIL while they do their work in native code, and many of them do exactly that.

When the GIL is released inside a C extension, other Python threads can run in parallel on multiple cores.

This is why "threads can't use multiple cores in Python" is one of the most repeated half-truths on the internet.

Threads doing work inside a well-written C extension absolutely can.

If the underlying numerical or native library releases the GIL and isn't already saturating your CPU internally, threading on top can give you some parallelism. (If you want to go down the rabbit hole,this Stack Overflow threadhas the canonical back-and-forth on the question)

This is also why scientific Python feels so much faster than the language has any right to be: most of the actual work is happening in C/C++/Fortran, and the GIL gets out of the way for the duration.

## Okay but what if I genuinely need to crunch in pure Python

This is wheremultiprocessingcomes in.

Each process gets its own Python interpreter, its own memory, its own GIL. Spin up four processes on a four-core machine, and you actually get four cores' worth of work — no lock fighting, no taking turns.

import
 
time

from
 
multiprocessing
 
import
 
Process

def
 
countdown
(
n
):

 
while
 
n
 
>
 
0
:

 
n
 
-=
 
1

if
 
__name__
 
==
 
"
__main__
"
:

 
COUNT
 
=
 
50_000_000

 
start
 
=
 
time
.
time
()

 
p1
 
=
 
Process
(
target
=
countdown
,
 
args
=
(
COUNT
,))

 
p2
 
=
 
Process
(
target
=
countdown
,
 
args
=
(
COUNT
,))

 
p1
.
start
();
 
p2
.
start
()

 
p1
.
join
();
 
p2
.
join
()

 
print
(
f
"
multiprocessing: 
{
time
.
time
()
 
-
 
start
:
.
2
f
}
s
"
)

Enter fullscreen mode

Exit fullscreen mode

For sufficiently CPU-heavy workloads on multi-core systems, this is usually faster than the sequential version.. Won't always be exactly half, it depends on your CPU topology, thermal headroom, and what else your machine is doing but yeah, you'll see some parallelism.

The catch: processes are heavier than threads. They take longer to spin up, they don't share memory by default, and passing data between them involves serialization (usually pickling), which has its own gotchas. If you've ever seen aCan't pickle local objecterror, you've met one of them.

For most everyday cases, reach forconcurrent.futures.ProcessPoolExecutor.It's a friendlier wrapper that makes multiprocessing feel almost as easy as threading.

## The places it actually bites in real life

Times I've watched people (also me) get burned:

* writing a "fast" data transformation in pure Python with threads, expecting linear scaling, getting none
* threading a pandas pipeline that's mostly.apply()with a Python function. pandas drops into C and releases the GIL for vectorized ops, but.apply()calls back into Python — and Python is back to one thread at a time
* web scrapers that thread theparsingwith a pure-Python parser instead of thefetching. fetching is I/O (good for threads). HTML parsing can become CPU-bound, especially withhtml.parser. Withlxml, you'd be fine because lxml releases the GIL, parser choice matters

The throughline is always the same: figure out whether your bottleneck iswaiting,computing in pure Python, orcomputing in a C extension. Threading helps the first and third, not the middle.

## Wait, isn't the GIL going away

Sort of.

PEP 703the proposal to make the GIL optional in CPython — was accepted by the Steering Council in 2023, with explicit conditions: the rollout had to be gradual, ecosystem disruption had to stay manageable, and the entire effort could still be rolled back if it proved too disruptive.

Python 3.13 (October 2024) shipped the firstexperimental free-threaded buildof CPython alongside the normal GIL-enabled build.It allows running Python without the GIL, though many extension modules still rely on GIL assumptions and may re-enable it automatically when imported.

Python 3.14substantially improved the experimental free-threaded runtime.The adaptive interpreter was re-enabled, single-threaded performance penalties dropped substantially, and the project moved into Phase II of the Steering Council's rollout plan where free-threaded Python is considered supported, but still optional and not the default runtime.

CPython is clearly moving toward a future where no-GIL Python is viable but we're not at the point where the standard build is going away anytime soon.

## What to actually do with all this

If I had to compress everything I wish someone had told me earlier:

When your code is slow, before reaching for any concurrency, profile it. Find out where the time is going. Then ask one question:is this thread waiting, computing in pure Python, or computing inside a C extension?

* waiting → threading orasynciowill help a lot
* pure Python → threading won't help; reach for multiprocessing, or find a library that drops to C (NumPy, polars, anything with a native backend)
* C extension that releases the GIL → threading already helps; you may not need anything else

And don't feel dumb if you've been bitten by this. Everyone has. The GIL is one of those things that's obvious in hindsight and completely opaque the first time you hit it.

Now you've hit it on purpose, in a controlled environment, with a blog post next to you. That puts you ahead of where I was.

## References

* Python Wiki — Global Interpreter Lock
* Python FAQ — Can't we get rid of the Global Interpreter Lock?
* PEP 703 — Making the Global Interpreter Lock Optional in CPython
* Python HOWTO — Python support for free threading
* What's New in Python 3.14 — Free-threaded CPython
* Steering Council notice on PEP 703
* Python docs —concurrent.futures.ProcessPoolExecutor
* Python docs —multiprocessingintroduction
* SciPy Cookbook — Parallel Programming
* Stack Overflow — Is Python capable of running on multiple cores?

AI agents write code fast. They also silently remove logic, change behavior, and introduce bugs -- without telling you. You often find out in production.

git-lrc fixes this. It hooks into git commit and reviews every diff before it lands. 60-second setup. Completely free.*

Any feedback or contributors are welcome! It's online, source-available, and ready for anyone to use.

⭐ Star it on GitHub:

## HexmosTech/git-lrc

### Free, Micro AI Code Reviews That Run on Commit

|🇩🇰 Dansk|🇪🇸 Español|🇮🇷 Farsi|🇫🇮 Suomi|🇯🇵 日本語|🇳🇴 Norsk|🇵🇹 Português|🇷🇺 Русский|🇦🇱 Shqip|🇨🇳 中文|

# git-lrc

## Free, Micro AI Code Reviews That Run on Commit

 

 
 
 
 
 
 

AI agents write code fast. They alsosilently remove logic, change behavior, and introduce bugs -- without telling you. You often find out in production.

git-lrcfixes this.It hooks intogit commitand reviews every diffbeforeit lands. 60-second setup. Completely free.

## See It In Action

See git-lrc catch serious security issues such as leaked credentials, expensive cloud
operations, and sensitive material in log statements

git-lrc-intro-60s.mp4

## Why

* 🤖AI agents silently break things.Code removed. Logic changed. Edge cases gone. You won't notice until production.
* 🔍Catch it before it ships.AI-powered inline comments show youexactlywhat changed and what looks wrong.
* 🔁Build a…

View on GitHub

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse