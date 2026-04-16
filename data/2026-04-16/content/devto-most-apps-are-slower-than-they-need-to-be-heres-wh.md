---
title: Most Apps Are Slower Than They Need to Be — Here’s Why (Live Demo🛸) - DEV Community
url: https://dev.to/sylwia-lask/most-apps-are-slower-than-they-need-to-be-heres-why-live-demo-2hh8
site_name: devto
content_file: devto-most-apps-are-slower-than-they-need-to-be-heres-wh
fetched_at: '2026-04-16T19:59:56.472616'
original_url: https://dev.to/sylwia-lask/most-apps-are-slower-than-they-need-to-be-heres-why-live-demo-2hh8
author: Sylwia Laskowska
date: '2026-04-16'
description: We’re a quarter into the 21st century, and the browser has quietly evolved into something much more... Tagged with javascript, react, webassembly, webgpu.
tags: '#javascript, #react, #webassembly, #webgpu'
---

Practical WebGPU and WebAssembly performance

We’re a quarter into the 21st century, and the browser has quietly evolved into something much more than just a UI layer. It can run complex computations, leverage the GPU, process audio, simulate physics, and even run machine learning models. And yet… most of the time, we still treat it like a tool for forms and dashboards.

I wanted to show what happens when we actually take advantage of what the platform already gives us.

The jsday conference in Bologna has just come to an end, and it was honestly amazing. If you’re wondering whether it’s worth attending events like this — it absolutely is. It’s an endless source of inspiration, far beyond what you get from articles or tutorials. If you have a minute, I’d really appreciate a like on myLinkedIn post

If you’ve been following my posts, you probably know that my talk was about WebGPU and WebAssembly, and what we can gain by using them in the browser.

So what are these two technologies, and why does it make more sense to talk about them together rather than separately?

They are complementary by design. WebAssembly runs on the CPU and allows us to execute low-level, compiled code directly in the browser. WebGPU, as the name suggests, gives us access to the GPU — not in some abstracted, limited way, but in a relatively direct and powerful form.

If you want a deeper dive, I’ve written more about them here:WASM →https://dev.to/sylwia-lask/will-webassembly-kill-javascript-lets-find-out-live-demo-43lnWebGPU →https://dev.to/sylwia-lask/why-webgpu-feels-like-the-future-of-the-web-live-demo--2bjh

But instead of talking about them in isolation, I wanted to show a concrete example of what happens when you combine them.

Because I’m not a fan of theory without practice, I built a small demo.

👉 Repo:https://github.com/sylwia-lask/text-goes-boom👉 Live demo:https://sylwia-lask.github.io/text-goes-boom/(Fair warning — especially the JS canvas benchmark can get your CPU quite warm 😅)

What does it do? You type text into an input field. The text is converted into particles. And when you click and drag your mouse across it… the text explodes.

Completely useless? Yes. Slightly addictive? Also yes 😅

## What’s happening under the hood?

First, the text from the input is rendered into an image bitmap using plain JavaScript and Canvas 2D. This is exactly the kind of task where the classic browser APIs are already perfectly sufficient, and there’s no real reason to move it elsewhere — especially for a demo like this.

Next, the bitmap is passed to WebAssembly. This is where I run a deliberately “somewhat over-engineered” algorithm that maps the image into particles. I wanted WASM to actually have something meaningful to do, and let’s be honest — it also just looks cooler this way. Out of curiosity, I benchmarked it against an equivalent implementation written in JavaScript.

As you can see, this is where we get the first tangible gain. WebAssembly is roughly 2–3× faster in this case. And this isn’t even a best-case scenario — I put quite a bit of effort into optimizing the JavaScript version as well, just to make things fair and not give Rust an easy win.

In this particular demo, the difference doesn’t matter that much because this step only runs once during rebuild. But it’s not about this one case — it’s about the order of magnitude. What happens if you need to perform a similar operation hundreds or thousands of times? That’s where this starts to become very real.

And then comes the part where things get interesting.

The particles are passed to WebGPU — and this is where the browser really starts to flex.

The “classic” JavaScript + Canvas 2D implementation starts struggling on my machine at around 40k particles.

Frame rate drops, everything slows down, and you can feel the limits pretty quickly.

Meanwhile, WebGPU… doesn’t even flinch.

More than 500,000 particles. Each with its own physics. Smooth animation. Stable FPS.

At this point it stops being a small optimization and starts feeling like a completely different class of capability. The same browser, the same app, the same machine — but a totally different level of performance, simply by using the right tool for the job.

## Where does this actually matter?

This is obviously not your typical frontend CRUD setup. You probably don’t need WebGPU to build a dashboard or a form, and in many cases the real bottleneck is the network, not computation.

But there are entire classes of problems where this approach makes a huge difference: real-time data visualization, physics simulations, graphics-heavy interfaces, audio processing, games, image or video transformations, and of course — matrix-heavy workloads like machine learning and LLMs running directly in the browser.

And the funny thing is, you don’t need this… until suddenly you really do. A product evolves, requirements grow, performance becomes an issue, or you want to move part of the workload from the backend to the client. That’s when things start getting interesting.

## One more thing

If you take a look at the repository, you might notice something important.

This is just a regular React app.

There’s no exotic architecture, no “from another planet” stack. Yes, there’s Rust compiled to WASM and there are WebGPU shaders — but they’re simply embedded into a standard frontend setup. The rest of the app looks exactly like something you could start in your project tomorrow.

That was intentional. I wanted to show that this isn’t some distant, experimental playground reserved for niche use cases. It’s something you can already integrate into real-world applications — incrementally, when you actually need it.

Of course, WebGPU is not yet universally supported, so you’ll need a fallback strategy. But at this point, for a large portion of users, there’s little reason not to start exploring it.

## Final thought

The browser is no longer just a place where we render UI.

It’s a serious compute platform — one that already gives us access to both CPU and GPU, right out of the box.

You don’t need WebAssembly or WebGPU in every project. Most of the time, you’ll be perfectly fine without them.

But the moment you start hitting performance limits, or your problem shifts from “moving data around” to “actually computing things”… you might realize that the platform already had the solution all along.

And all you had to do was use it. 🚀

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (18 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse