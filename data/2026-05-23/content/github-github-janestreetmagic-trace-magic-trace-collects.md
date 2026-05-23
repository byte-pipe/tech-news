---
title: 'GitHub - janestreet/magic-trace: magic-trace collects and displays high-resolution traces of what a process is doing · GitHub'
url: https://github.com/janestreet/magic-trace
site_name: github
content_file: github-github-janestreetmagic-trace-magic-trace-collects
fetched_at: '2026-05-23T11:28:38.051715'
original_url: https://github.com/janestreet/magic-trace
author: janestreet
description: magic-trace collects and displays high-resolution traces of what a process is doing - janestreet/magic-trace
---

janestreet

 

/

magic-trace

Public

* NotificationsYou must be signed in to change notification settings
* Fork172
* Star5.6k

 
 
 
 
master
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

337 Commits
337 Commits
.github
.github
 
 
.vscode
.vscode
 
 
bin
bin
 
 
debian
debian
 
 
demo
demo
 
 
direct_backend
direct_backend
 
 
docs
docs
 
 
lib/
magic_trace
lib/
magic_trace
 
 
src
src
 
 
test
test
 
 
vendor
vendor
 
 
.git-blame-ignore-revs
.git-blame-ignore-revs
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.ocamlformat
.ocamlformat
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE.md
LICENSE.md
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
dune
dune
 
 
dune-project
dune-project
 
 
magic-trace.opam
magic-trace.opam
 
 
magic-trace.opam.locked
magic-trace.opam.locked
 
 
View all files

## Repository files navigation

# magic-trace

# Overview

magic-trace collects and displays high-resolution traces of what a process is doing. People have used it to:

* figure out why an application running in production handles some requests slowly while simultaneously handling a sea of uninteresting requests,
* look at what their code isactuallydoing instead of what theythinkit's doing,
* get a history of what their application was doing before it crashed, instead of a mere stacktrace at that final instant,
* ...and much more!

magic-trace:

* has2%-10% overhead,
* doesn't require application changes to use,
* tracesevery function callwith ~40ns resolution, and
* renders a timeline of call stacks going back (a configurable) ~10ms.

You use it likeperf: point it to a process and off it goes. The key difference fromperfis that instead of sampling call stacks throughout time, magic-trace usesIntel Processor Traceto snapshot a ring buffer ofall control flowleading up to a chosen point in time1. Then, you can explore an interactive timeline of what happened.

You can point magic-trace at a function such that when your application calls it, magic-trace takes a snapshot. Alternatively, attach it to a running process and detach it withCtrl+C, to see a trace of an arbitrary point in your program.

# Testimonials

"Magic-trace is one of the simplest command-line debugging tools I have ever used."

* Francis Ricci, Jane Street

"Magic-trace is not just for performance. The tool gives insight directly into what happens in your program, when, and why. Consider using it for all your introspective goals!"

* Andrew Hunter, Jane Street

I use perf a ton, and I think that both perf and magic-trace give perspectives that the other doesn't. The benefit I got from magic-trace was entirely based on the fact that it works in slices at any zoom level, so I was able to see all the function calls that a 70ns function was performing, which was invisible in perf.

* Doug Patti, Jane Street

more testimonials...

# Install

1. Make sure the system you want to trace issupported. The constraints that most commonly trip people up are: VMs are mostly not supported, Intel only (Skylake2or later), Linux only.
2. Grab a release binary from thelatest release page.If downloading the prebuilt binary (not package),chmod +x magic-trace3If downloading the package, runsudo dpkg -i magic-trace*.debThen, test it by runningmagic-trace -help, which should bring up some help text.
3. If downloading the prebuilt binary (not package),chmod +x magic-trace3
4. If downloading the package, runsudo dpkg -i magic-trace*.deb

# Getting started

1. Here's a sample C program to try out. It's a slightly modified version of the example inman 3 dlopen. Download that, build it withgcc demo.c -ldl -o demo, then leave it running./demo. We're going to use that program to learn howdlopenworks.
2. Runmagic-trace attach -pid $(pidof demo). When you see the message that it's successfully attached, wait a couple seconds andCtrl+Cmagic-trace. It will output a file calledtrace.fxt.gzin your working directory.

1. Openmagic-trace.org, click"Open trace file"in the top-left-hand and give it the trace file generated in the previous step.

1. That should have expanded into a trace. Zoom in until you can see an individual loop throughdlopen/dlsym/cos/printf/dlclose.* Wzooms into wherever your mouse cursor is pointed (you'll need to zoom in a bunch to see anything useful),
* Szooms out,
* Amoves left,
* Dmoves right, and
* scroll wheel moves your viewport up and down the stack. You'll only need to scroll to see particularly deep stack traces, it's probably not useful for this example.

1. Click and drag on the white space around the call stacks to measure. Plant flags by clicking in the timeline along the top. Using the measurement tool, measure how long it takes to runcos. On my screen it takes ~5.7us.

Congratulations, you just magically traced your first program!

In contrast to traditionalperfworkflows, magic-trace excels at hypothesis generation. For example, you might notice that taking 6us to runcosis a really long time! If you zoom in even more, you'll see that there's actually five pink "[untraced]" cells in there. If you re-run magic-trace with root and pass it-trace-include-kernel, you'll see stacktraces for those. They're page fault handlers! The demo program actually callscostwice. If you zoom in even more near the end of the 6uscoscall, you'll see that the second call takesfarless time and does not page fault.

# How to use it

magic-trace continuously records control flow into a ring buffer. Upon some sort of trigger, it takes a snapshot of that buffer and reconstructs call stacks.

There are two ways to take a snapshot:

We just did this one:Ctrl+Cmagic-trace. If magic-trace terminates without already having taken a snapshot, it takes a snapshot of the end of the program.

You can also trigger snapshots when the application calls a function. To do so, pass magic-trace
the-triggerflag.

* -trigger '?'brings up a fuzzy-finding selector that lets you choose from all
symbols in your executable,
* -trigger SYMBOLselects a specific, fully mangled, symbol you know ahead of time, and
* -trigger .selects the default symbolmagic_trace_stop_indicator.

Stop indicators are powerful. Here are some ideas for where you might want to place one:

* If you're using an asynchronous runtime, any time a scheduler cycle takes too long.
* In a server, when a request takes a surprisingly long time.
* After the garbage collector runs, to see what it's doing and what it interrupted.
* After a compiler pass has completed.

You may leave the stop indicator in production code. It doesn't need to do anything in particular, magic-trace just needs the name. It is just an empty, but not inlined, function. It will cost ~10us to call, butonly when magic-trace actually uses it to take a snapshot.

# Documentation

More documentation is available onthe magic-trace wiki.

# Discussion

Join uson Discordto chat synchronously, or theGitHub discussion groupto do so asynchronously.

# Contributing

If you'd like to contribute:

1. read the build instructions,
2. set up your editor,
3. take a quick tour through the codebase, then
4. hit up the issue trackerfor a good starter project.

# Privacy policy

magic-trace does not send your code or derivatives of your code (including traces) anywhere.

magic-trace.orgis alightly modified fork of Perfetto, and runs entirely in your browser. As far as we can tell, it does not send your trace anywhere. If you're worried about that changing one day,set up your own local copy of the Perfetto UIand use that instead.

# Acknowledgements

Tristan Humeis the original author of magic-trace. He wrote it while working atJane Street, who currently maintains it.

Intel PT is the foundational technology upon which magic-trace rests. We'd like to thank the people at Intel for their years-long efforts to make it available, despite its slow uptake in the greater software community.

magic-trace would not be possible withoutperfs extensive support for Intel PT.perfdoes most of the work in interpreting Intel PT's output, and magic-trace likely wouldn't exist were it not for their efforts. Thank you,perfdevelopers.

magic-trace.orgis a fork ofPerfetto, with minor modifications. We'd like to thank the people at Google responsible for it. It's a high quality codebase that solves a hard problem well.

The ideas behind magic-trace are in no way unique. We've written down a list ofprior artthat has influenced its design.

## Footnotes

1. perfcan do this too, but that's not how most people use it. In fact, if you peek under the hood you'll see that magic-trace usesperfto drive Intel PT.↩
2. Strictly speaking, anything newer than Broadwell, but this is not a platform we regularly test on, and timing resolution is worse (~1us).↩
3. https://github.com/actions/upload-artifact/issues/38↩

## About

magic-trace collects and displays high-resolution traces of what a process is doing

magic-trace.org

### Topics

 profile

 intel

 tracing

 visualizer

 introspection

 x86

 performance-tools

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

5.6k

 stars
 

### Watchers

41

 watching
 

### Forks

172

 forks
 

 Report repository

 

## Releases10

magic-trace v1.2.4

 Latest

 

Apr 13, 2025

 

+ 9 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* OCaml99.7%
* Other0.3%