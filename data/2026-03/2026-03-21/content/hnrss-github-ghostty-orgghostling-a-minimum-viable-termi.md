---
title: 'GitHub - ghostty-org/ghostling: A minimum viable terminal emulator built on top of the libghostty C API. Ex minimo, infinita nascuntur. 👻🐣 · GitHub'
url: https://github.com/ghostty-org/ghostling
site_name: hnrss
content_file: hnrss-github-ghostty-orgghostling-a-minimum-viable-termi
fetched_at: '2026-03-21T19:10:43.841038'
original_url: https://github.com/ghostty-org/ghostling
date: '2026-03-20'
description: A minimum viable terminal emulator built on top of the libghostty C API. Ex minimo, infinita nascuntur. 👻🐣 - ghostty-org/ghostling
tags:
- hackernews
- hnrss
---

ghostty-org

 

/

ghostling

Public

* NotificationsYou must be signed in to change notification settings
* Fork16
* Star521

 
 
 
 
main
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

53 Commits
53 Commits
.github
.github
 
 
fonts
fonts
 
 
.envrc
.envrc
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CMakeLists.txt
CMakeLists.txt
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
bin2header.cmake
bin2header.cmake
 
 
demo.gif
demo.gif
 
 
flake.lock
flake.lock
 
 
flake.nix
flake.nix
 
 
main.c
main.c
 
 
View all files

## Repository files navigation

# Ghostling - Minimal libghostty Terminal

Ghostling is a demo project meant to highlight a minimum
functional terminal built on the libghostty C API in asingle C file.

The example uses Raylib for windowing and rendering. It is single-threaded
(although libghostty-vt supports threading) and uses a 2D graphics renderer
instead of a direct GPU renderer like the primaryGhosttyGUI. This is to
showcase the flexibility of libghostty and how it can be used in a variety of
contexts.

Warning

The Ghostling terminal isn't meant to be a full featured, daily use
terminal. It is a minimal viable terminal based on libghostty. Also, since
this is basically a demo, I didn't carefully audit every single place for
correctness, and this is C, so you've been warned!

## What is Libghostty?

Libghostty is an embeddable library extracted fromGhostty'score,
exposing a C and Zig API so any application can embed correct, fast terminal
emulation.

Ghostling useslibghostty-vt, a zero-dependency library (not even libc) that
handles VT sequence parsing, terminal state management (cursor position,
styles, text reflow, scrollback, etc.), and renderer state management. It
contains no renderer drawing or windowing code; the consumer (Ghostling, in
this case) provides its own. The core logic is extracted directly from Ghostty
and inherits all of its real-world benefits: excellent, accurate, and complete
terminal emulation support, SIMD-optimized parsing, leading Unicode support,
highly optimized memory usage, and a robust fuzzed and tested codebase, all
proven by millions of daily active users of Ghostty GUI.

## Features

Despite being a minimal, thin layer above libghostty, look at all the
features youdo get:

* Resize with text reflow
* Full 24-bit color and 256-color palette support
* Bold, italic, and inverse text styles
* Unicode and multi-codepoint grapheme handling (no shaping or layout)
* Keyboard input with modifier support (Shift, Ctrl, Alt, Super)
* Kitty keyboard protocol support
* Mouse tracking (X10, normal, button, and any-event modes)
* Mouse reporting formats (SGR, URxvt, UTF8, X10)
* Scroll wheel support (viewport scrollback or forwarded to applications)
* Scrollbar with mouse drag-to-scroll
* Focus reporting (CSI I / CSI O)
* And more. Effectively all the terminal emulation features supported
by Ghostty!

### What Is Coming

These features aren't properly exposed by libghostty-vt yet but will be:

* Kitty Graphics Protocol
* OSC clipboard support
* OSC title setting

These are things that could work but haven't been tested or aren't
implemented in Ghostling itself:

* Windows support (libghostty-vt supports Windows)

This list is incomplete and we'll add things as we find them.

### What You Won't Ever Get

libghostty is focused on core terminal emulation features. As such,
you don't get features that are provided by the GUI above the terminal
emulation layer, such as:

* Tabs
* Multiple windows
* Splits
* Session management
* Configuration file or GUI
* Search UI (although search internals are provided by libghostty-vt)

These are the things that libghostty consumers are expected to implement
on their own, if they want them. This example doesn't implement these
to try to stay as minimal as possible.

### Limitations Due to Upstreams

There are some known issues with this demo:

* Kitty keyboard protocol support is broken with some inputs. This is
due to limitations of the underlying Raylib input system; it doesn't
support rich enough input events to fully and correctly implement the Kitty
keyboard protocol. This is aknown issue.
The libghostty-vt API supports Kitty keybaord protocol correctly, but
requires correct input events to do so.

## Building

Requirements:

* CMake3.19+
* Ninja
* A C compiler
* Zig0.15.x on PATH
* macOS:Command Line Tools or Xcode

cmake -B build -G Ninja
cmake --build build
./build/ghostling

Warning

Debug builds are VERY SLOW since Ghostty included a lot of extra
safety and correctness checks. Do not benchmark debug builds.

For a release (optimized) build:

cmake -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build

After the initial configure, you only need to run the build step:

cmake --build build

## FAQ

### Why Not Zig?

libghostty-vt has a fully capable and proven Zig API. Ghostty GUI itself
uses this and is a good -- although complex -- example of how to use it.
However, this demo is meant to showcase the minimal C API since C is so
much more broadly used and accessible to a wide variety of developers and
language ecosystems.

### What about Rust or any other language?

libghostty-vt has a C API and can have zero dependencies, so it can be used
with minimally thin bindings in basically any language. I'm not sure yet if
the Ghostty project will maintain official bindings for languages other than C
and Zig, but I hope the community will create and maintain bindings for many
languages!

### Does libghostty require Raylib?

No no no!libghostty has no opinion about the renderer or GUI framework
used; it's even standalone WASM-compatible for browsers and other environments.

libghostty provides ahigh-performance render state APIwhich only keeps track of thestaterequired to build a renderer. This is the
same API used by Ghostty GUI for Metal and OpenGL rendering and in this repository
for the Raylib 2D graphics API. You can layer any renderer on top of this!

### Why CMake, Raylib, etc.?

I needed to picksomething. Really, any build system and any library
could be used. CMake is widely used and supported, and Raylib is a simple
and elegant library for windowing and 2D rendering that is easy to set up.
Don't get bogged down in these details!

## About

A minimum viable terminal emulator built on top of the libghostty C API. Ex minimo, infinita nascuntur. 👻🐣

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

521

 stars
 

### Watchers

2

 watching
 

### Forks

16

 forks
 

 Report repository

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* C91.3%
* CMake6.2%
* Nix2.4%
* Shell0.1%