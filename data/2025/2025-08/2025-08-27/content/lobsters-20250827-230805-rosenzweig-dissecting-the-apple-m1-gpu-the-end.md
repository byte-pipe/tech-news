---
title: Rosenzweig – Dissecting the Apple M1 GPU, the end
url: https://rosenzweig.io/blog/asahi-gpu-part-n.html
site_name: lobsters
fetched_at: '2025-08-27T23:08:05.890761'
original_url: https://rosenzweig.io/blog/asahi-gpu-part-n.html
date: '2025-08-27'
tags: graphics, reversing
---

In 2020, Apple
released the M1 with a custom GPU. We got to work reverse-engineering
the hardware and porting Linux. Today, you can run Linux on a range of
M1 and M2 Macs, with almost all hardware working: wireless, audio, and
full graphics acceleration.

Our story begins in December 2020, whenHector Martinkicked offAsahi Linux. I was working forCollaboraworking on Panfrost, the open
source Mesa3D driver for Arm Mali GPUs. Hector put out a public call for
guidance from upstream open source maintainers, and I bit. I just
intended to give some quick pointers. Instead, Ibought myself a Christmas presentand
got to work. In between my university coursework and Collabora work, I
poked at theshader
instruction set.

One thing led to another. Within a few weeks, Idrew a
triangle.

In 3D graphics, once you can draw a triangle, you can doanything.

Pretty soon, I started work on ashader
compiler. After my final exams that semester, I took a few days off
from Collabora to bring upan OpenGL
drivercapable of spinning gears with my new compiler.

Over the next year, I keptreverse-engineeringand improving the driver untilit could run 3D
games on macOS.

Meanwhile,Asahi Linawrote a kernel
driver for the Apple GPU. My userspace OpenGL driver ran on macOS,
leaving her kernel driver as the missing piece for an open source
graphics stack. In December 2022, weshipped graphics
acceleration in Asahi Linux.

In January 2023, I started my final semester in my Computer Science
program at theUniversity of
Toronto. For years I juggled my courses with my part-time job and my
hobby driver. I faced the same question as my peers: what will I do
after graduation?

Maybe Panfrost? I started reverse-engineering of the Mali Midgard GPU
back in 2017, when I was still in high school. That led to an internship
at Collabora in 2019 once I graduated, turning into my job throughout
four years of university. During that time, Panfrost grew from a kid’s
pet project based on blackbox reverse-engineering, to a professional
driver engineered by a team with Arm’s backing and hardware
documentation. I did what I set out to do, and the project succeeded
beyond my dreams.It was
time to move on.

WhatdidI want to do next?

* Finish what I started with the M1. Ship a great driver.
* Bring full, conformant OpenGL drivers to the M1. Apple’s drivers are
not conformant, but we should strive for the industry standard.
* Bring full, conformant Vulkan to Apple platforms, disproving the
myth that Vulkan isn’t suitable for Apple hardware.
* Bring Proton gaming to Asahi Linux. Thanks to Valve’s work for the
Steam Deck, Windows games can run better on Linux than even on Windows.
Why not reap those benefits on the M1?

Panfrost was my challenge until we “won”. My next challenge? Gaming
on Linux on M1.

Once I finished my coursework, I started full-time on gaming on
Linux. Within a month, we shippedOpenGL 3.1
on Asahi Linux. A few weeks later, we passedofficial
conformance for OpenGL ES 3.1. That put us at feature parity with
Panfrost. I wanted to go further.

OpenGL (ES) 3.2 requires geometry shaders, a legacy feature not
supported by either Arm or Apple hardware. The proprietary OpenGL
drivers emulate geometry shaders with compute, but there was no open
source prior art to borrow. Even though multiple Mesa drivers need
geometry/tessellation emulation, nobody did the work to get there.

My early progress on OpenGL was fast thanks to the mature common code
in Mesa. It was time to pay it forward. Over the rest of the year, I
implemented geometry/tessellation shader emulation. And also the rest of
the owl. In January 2024, I passed conformance for the fullOpenGL
4.6specification, finishing up OpenGL.

Vulkan wasn’t too bad, either. I polished the OpenGL driver for a few
months, but once I started typing a Vulkan driver, I passed1.3
conformancein a few weeks.

What remained was wiring up the geometry/tessellation emulation to my
shiny new Vulkan driver, since those are required for Direct3D. Et
voilà,Proton
games.

Along the way,Karol
Herbstpassed OpenCL 3.0 conformance on the M1, running my compiler
atop his “rusticl” frontend.

Meanwhile, when the Vulkan 1.4 specification was published, we were
ready andshipped
a conformant implementation on the same day.

After that, I implemented sparse texture support, unlocking Direct3D
12 via Proton.

…Now what?

* Ship a great driver?Check.
* Conformant OpenGL 4.6, OpenGL ES 3.2, and OpenCL 3.0?Check.
* Conformant Vulkan 1.4?Check.
* Proton gaming?Check.

That’s a wrap.

We’ve succeeded beyond my dreams. The challenges I chased, I have
tackled. The drivers are fully upstream in Mesa. Performance isn’t too
bad. With the Vulkan on Apple myth busted, conformant Vulkan is now
coming to macOS viaLunarG’s
KosmicKrispproject building on my work.

Satisfied, I am now stepping away from the Apple ecosystem. My
friends in the Asahi Linux orbit will carry the torch from here. As for
me?

Onto
the next challenge!

Back to home
