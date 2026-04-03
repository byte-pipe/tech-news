---
title: Why Are We Still Doing GPU Work in JavaScript? (Live WebGPU Benchmark & Demo🚀) - DEV Community
url: https://dev.to/sylwia-lask/why-are-we-still-doing-gpu-work-in-javascript-live-webgpu-benchmark-demo-4j6i
site_name: devto
content_file: devto-why-are-we-still-doing-gpu-work-in-javascript-live
fetched_at: '2026-03-15T11:10:22.167299'
original_url: https://dev.to/sylwia-lask/why-are-we-still-doing-gpu-work-in-javascript-live-webgpu-benchmark-demo-4j6i
author: Sylwia Laskowska
date: '2026-03-12'
description: JavaScript has been the main language of the web for years. Its popularity probably surprised even... Tagged with webdev, javascript, typescript, webgpu.
tags: '#webdev, #javascript, #typescript, #webgpu'
---

JavaScript has been the main language of the web for years. Its popularity probably surprised even its creator, Brendan Eich, who famously built the first version of the language in just about a week.

One of the reasons JavaScript became so dominant is the sheer power of the browser. From a single application — the browser — we can access hundreds of millions of websites and applications. No need to download or install anything. That's huge part of the success.

And browser vendors have been working incredibly hard to make JavaScript faster and faster. Modern engines are extremely optimized. But there is still one fundamental limitation:

JavaScript runs on the CPU.

So what about tasks that are perfect for the GPU?

This is whereWebGPUenters the scene. 🚀Let’s take a look at what it can actually do — and when it really makes sense to use it.

By the way — myjsDaytalk is getting closer and closer! I’ll be speaking there about **WebGPU + WebAssembly, which is exactly the kind of things you see in this article: GPUs in the browser, compute shaders, and pushing the web a bit further than usual.

To celebrate that (and maybe calm my pre-conference nerves a little 😅), I recorded a short promo reel for the talk which you can findhere

If you feel like watching it and dropping a like, I’d really appreciate it.And if you’re coming to **jsDay, come say hi after the talk!🙂

## A Quick Note Before We Start

I already wrote about WebGPU in another article, so I won’t repeat the full introduction here:

Why WebGPU Feels Like the Future of the Web (Live Demo)

But let’s briefly recap one important thing.

WebGPU is not just about graphics — although it does that beautifully.It also gives us something extremely powerful:

access to GPU compute.

## CPU vs GPU (Quick Reminder)

This will be obvious to most of you, but let's make a quick distinction for beginners and those who slept through their first semester of college:

CPUsare great at doing a few complex things one after another.In the browser, that usually meansJavaScript or WebAssembly.

GPUsare great at doing simple thingsmassively in parallel.And in the browser, the API that lets us use them isWebGPU.

That’s why GPUs are so good at tasks where thesame operation needs to be repeated thousands or millions of times.

## I Wanted to Test It Myself

If you read my posts regularly, you probably know I don’t like taking things on faith. I prefer to try myself. 🙂

So I built a small application that benchmarksJavaScript vs WebGPU.

These are not super-academic benchmarks where the exact same algorithm is implemented line-by-line in different systems. I probably wouldn't have gotten a PhD from MIT thanks to them. 😅

Instead, I tried something more practical:

I tested how both technologies behave when they solve thesame problem in a way that is natural for them, without intentionally favoring either one.

You can explore everything here:

GitHub repo

https://github.com/sylwia-lask/webgpu-bench

Live demo

https://sylwia-lask.github.io/webgpu-bench/

Feel free to play with it yourself. 😄

## Scenario 1 — Particle Simulation

The first test was aparticle simulation.

If you read about WebGPU online — or ask ChatGPT — this is usually presented as a classic example of GPU superiority.

Each particle has two properties:

* position(x, y)
* velocity(vx, vy)

Every frame we update it like this:

x
 
=
 
x
 
+
 
vx

y
 
=
 
y
 
+
 
vy

Enter fullscreen mode

Exit fullscreen mode

And if the particle hits the screen border, we reverse the velocity to simulate a bounce.

Pseudo-code:

for
 
each
 
particle
:

 
pos
 
+=
 
vel

 
if
 
pos
.
x
 
<
 
0
 
or
 
pos
.
x
 
>
 
width
:

 
vel
.
x
 
=
 
-
vel
.
x

 
if
 
pos
.
y
 
<
 
0
 
or
 
pos
.
y
 
>
 
height
:

 
vel
.
y
 
=
 
-
vel
.
y

Enter fullscreen mode

Exit fullscreen mode

So the compute shader effectively performs something like:

pos
 
+=
 
vel

Enter fullscreen mode

Exit fullscreen mode

That’s basicallytwo float additions per particle(plus a bounce check).

## The Result

Surprisingly…there was almost no differencebetween the JavaScript and WebGPU implementations. Both versions produced very similar FPS.

Meanwhile, the WebGPU version requiredmuch more boilerplate code.

Why does that happen?

### 1️⃣ The algorithm is extremely simple

The particle update does only2–4 floating point operations per thread.

GPUs really shine when the work iscompute-heavy, not when it’s this lightweight.

### 2️⃣ Canvas 2D also ends up on the GPU

This is something many frontend developers don’t realize.

Even when you useCanvas 2D, the browser often renders it using GPU acceleration.

Browsers like Chrome or Edge internally use systems likeSkiaorDawn, which eventually issue draw calls to the GPU.

So in practice:

* WebGPU → you talk directly to the GPU
* Canvas 2D → the browser talks to the GPU for you

And the browser isvery well optimizedfor things likefillRect().

So the CPU version isn’t as “CPU-only” as people often think.

### Could GPU Win Here?

Probably yes — but only if we made the simulation more complex.

For example, something liken-body gravity, where every particle attracts every other particle. That would dramatically increase the amount of math.

But honestly… I was too lazy to implement that. 😅

## Scenario 2 — Matrix Multiplication

Now let’s look at something GPUs absolutely love.

Matrix multiplication.

Despite the scary name, the idea is simple. Imagine two grids of numbers. To compute one cell in the result matrix:

* we take onerowfrom the first matrix
* onecolumnfrom the second matrix
* multiply numbers pairwise
* add the results together

Example:

[1 2] [5 6]
[3 4] × [7 8]

Enter fullscreen mode

Exit fullscreen mode

To compute the top-left cell:

1×5 + 2×7 = 19

Enter fullscreen mode

Exit fullscreen mode

And this operation must be repeatedfor every cell in the result matrix.

For large matrices, that quickly becomesmillions of multiplications.

Which is exactly the kind of workload GPUs were designed for.

## The Result

Here the result was very clear.

WebGPU absolutely crushes JavaScript.

And the larger the matrices get, the bigger the difference becomes.

This makes perfect sense:

Matrix multiplication is essentiallythe same simple operation repeated thousands or millions of times— the exact scenario where GPUs shine.

And let's remember it's one of the most important operations in computer science. Matrix multiplication is heavily used in:

* computer graphics
* physics simulations
* scientific computing
* and of course… our belovedLLMs🤖

## Scenario 3 — Image Processing Pipeline

The third benchmark tested something closer to traditional graphics work: animage processing pipeline.

Here the GPU once againcompletely dominatesthe CPU implementation.

This kind of workload is very natural for GPUs:

* every pixel can be processed independently
* the same operation is applied to thousands or millions of pixels

Which again fits the GPU execution model perfectly.

## So Should We Replace JavaScript With WebGPU?

Of course not. 🙂

WebGPU is powerful — but it only makes sense for certain types of problems. In general, WebGPU shines when you need to:

* performmany simple operations
* onlarge amounts of data
* in parallel

For regular application logic, JavaScript remains the perfect tool.

## There Are Still Some Practical Limitations

WebGPU is also still a relativelyyoung technology.

If you control the environment and can require users to run modern browsers, you can absolutely start experimenting with it.

But if you’re building something for a wide audience — where someone might open your app in a strange Android browser from 2018 — you should probably be careful.

Or implement a fallback, for example using WebGL.

## The Boilerplate Problem

If you check the repository, you’ll notice that WebGPU requires quite a bit of setup.

You need to:

* request an adapter
* request a device
* create buffers
* configure pipelines
* manage command encoders
* and so on.

There’s a lot of boilerplate.

Yes, coding agents like Claude or ChatGPT can help with this.

But here’s a small warning ⚠️

WebGPU is still new, andLLMs are not always great at generating correct WebGPU code. Sometimes you will still need to go back to the classic developer workflow:

* reading documentation
* browsing GitHub issues
* debugging things manually

Just like in the good old days. 😄

## Final Thoughts

The question is no longerwhetherWebGPU will become important.

The real question ishow soon we will need it.

Because WebGPU is essentially a new, modern standard for working with GPUs in the browser.

And for the kinds of problems GPUs were designed to solve — it can be incredibly powerful. 🚀

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (54 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse