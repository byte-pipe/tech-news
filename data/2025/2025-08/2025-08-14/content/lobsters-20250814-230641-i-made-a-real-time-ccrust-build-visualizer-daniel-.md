---
title: I Made A Real-Time C/C++/Rust Build Visualizer ・ Daniel Hooper
url: https://danielchasehooper.com/posts/syscall-build-snooping/
site_name: lobsters
fetched_at: '2025-08-14T23:06:41.312224'
original_url: https://danielchasehooper.com/posts/syscall-build-snooping/
date: '2025-08-14'
published_date: '2025-08-13T00:00:00+00:00'
tags: compilers, performance, programming
---

Daniel Hooper
Home
 ・

Articles
 ・

Projects
 ・

X.com

Bluesky

Mastodon

RSS

# I Made A Real-Time C/C++/Rust Build Visualizer

August 13, 2025・6 minute read

Many software projects take a long time to compile. Sometimes that’s just due to the sheer amount of code, like in the LLVM project. But often a build is slower than it should be for dumb, fixable reasons.

I’ve had the suspicion thatmostbuilds are doing dumb stuff, but I had no way tosee it. So I’ve been working on a cross-platform tool to help speed up builds (you can try it, see below). It works with any build system or programming language (Not just C/C++). Its timeline looks like this:

It’s more than just a generic system profiler: it looks for build-specific problems. A few examples: using make without the-jflag, disproportionate time being spent on certain files or compiler phases (as reported by tools like clang’s-ftime-trace), and commands that could’ve been run in parallel but weren’t. It’s especially helpful for optimizing CI builds, which are often clean rebuilds without caching.

I named itWhat the Forkafter thefork()system call that spawns new processes. You use it by writingwtfbefore a build command:

$
# A few possible examples:

$ wtf make

$ wtf cargo build

$ wtf gradle build

$ wtf npm run build

$ wtf zig build

$ wtf -x
# starts a build of the front most Xcode window

Here it is recording the build of a macOS app:

Your browser does not support the video tag.

## How it works

A build is just a bunch of commands that produce your finished program. At its simplest, it could be a shell script like this:

#!/bin/bash

clang main.c -o program

That script requires 3 programs to produce the final result:bash,clang, and —surprise!—ld, the linker, which clang runs automatically. Unexpected build steps are often the source of slowdowns and are even more likely in bigger projects, which often use something likecargo,make,bazel,gradle, orxcodebuildinstead of a shell script. Those tools still just execute commands, but they also perform caching, dependency analysis, and scheduling to do the least amount of work as efficiently as possible.

While you can see the commands a build tool runs by watching the terminal output, that doesn’t tell you what commandsthosecommands run (likeclangrunningld) and doesn’t include detailed timing! So if we want to seeeverythinga build does, we need to listen for the system calls that start and terminate processes:fork,exec, andexit. Each operating system has a its own way to do that:

* macOS has the Endpoint Security API
* Linux hasptrace()
* Windows has the “Worst API Ever Made”: Event Tracing for Windows

Each of those API are a pain to use for different reasons, but they do provide the information required to reconstruct a timeline. Here is our simple shell script’s execution visualized in the macOS version ofWhat the Fork.

Keen readers will have noticed that these techniques allow the app to be used on any type of program that launches sub-processes - not just builds! If you have any ideas for how that might be useful outside of build optimization, let me know.

## Things I’ve Noticed

Being able to see your build reveals a lot. I’ve had engineers from Delta, Mozilla, and Apple try the tool on their projects and each one found something unexpected. Let me give you some examples.

I’ll start with an open source project that uses cargo to build. I’m going to zoom in on the compilation of a single dependency:

Oops! No parallelism! Files are compiled one at a time. It could be about 10 times faster if cargo ran multiple commands at once on my 10 core M1 CPU. I’d have never noticed this without a timeline visualization. If you want to see what good parallelism looks like, check out howninjabuilds the llvm project:

Every core of my machine is kept busy the entire time. It’s actually slightly over-subscribed with 12 jobs in flight on my 10 core machine, whichis intentionalin case some jobs are blocked on IO. Perfection. Perfect is boring though, lets look at a problem. Here’s a tiny slice of a CMake build from another open source project:

Here CMake gets Xcode’s path withxcode-select -print-path, the OS version withsw_vers, and then recursively calls cmake/make a few times for good measure, and finally compiles and links a file.

Only the green boxes in that timeline are doing useful work. One could argue thatnoneof what CMake does is “useful work”, in the sense that it just builds the thing that actually builds the project. Regardless, let’s just accept that CMake needs to do this weird cmake->make->make->clang dance to figure out the build environment.

Zooming out reveals that the weird dance happens 85 times!

Yikes, no parallelism. It also studiously re-checks the Xcode path and OS version 85 times, just in case the OS version changes mid-build.

Ok enough about cmake. There are other builds to explore! Here’sxcodebuildbuilding a 100,000 line Objective-C project:

Notice how it has gaps towards the end of the build where it only has one or two clang processes running, even when there is a lot more to do.

It also has 6 seconds of inactivity before starting any useful work. For comparison,ninjatakes 0.4 seconds to start compiling the 2,468,083 line llvm project. Ninja is not a 100% fair comparison to other tools, because it benefits from some “baked in” build logic by the tool that created the ninja file, but I think it’s a reasonable “speed of light” performance benchmark for build systems.

Continuing our tour of various builds, here’s Zig compiling theOrca Project:

What’s interesting here is thatzig buildbuilds dependencies in a random order (To expose ordering problems due to misconfigured builds). That means that sometimes it gets lucky with the ordering, like in the previous image where it’s fast. But sometimes it’s unlucky, like below where thecurldependency got scheduled at the verrrry end, so it doesn’t have any parallelism with the rest of the project:

And finally, here’s make/go compiling the github cli project:

That big blank area towards the left is all the project’s dependencies being downloaded, so if I wanted to speed up this project’s clean builds, I’d focus on reducing dependencies first. Dependencies are kind of a build-double-whammy because guess what those long “compile” commands are: the dependenciesgo-control-plane,protobuf,gojq, etc.

That’s just a sampling of the things I’ve learned by visualizing builds. Of course there are more nuanced issues you can find by looking at a process’s full command, but today I wanted to focus on things that I could show visually.

## Early Access

What the Forkruns on Windows, Linux, and macOS. If you’re interested in trying it and providing feedback, join the early access grouphere.

❖
Get notified about my next article:

Join Newsletter
More articles by Daniel

Support my work
