---
title: Libghostty Is Coming – Mitchell Hashimoto
url: https://mitchellh.com/writing/libghostty-is-coming
site_name: hackernews
fetched_at: '2025-09-23T19:09:10.434814'
original_url: https://mitchellh.com/writing/libghostty-is-coming
author: kingori
date: '2025-09-23'
published_date: '2025-09-22T00:00:00.000Z'
---

# Mitchell Hashimoto

# Libghostty Is Coming

September 22, 2025

Over two years ago, inone of my first public talks about Ghostty,
I shared my vision forlibghostty: an embeddable library for any application
to embed their own fully functional, modern, and fast terminal emulator.
Libghostty is finally starting to take shape, and I'm excited to share
more details about my plans for it.

The first libghostty library will belibghostty-vt: a zero-dependency
library that provides an API for parsing terminal sequences and
maintaining terminal state, extracted directly from Ghostty's real-world proven
core. It doesn't even require libc!

Disclaimer: This post is predominantly a roadmap update for libghostty and announcing what
will be the first shippable component of it. The Zig API is available for testing now, but the C
API is not ready and will be coming very shortly. In both cases, it is early testing quality and
not ready for general usage.

## Why libghostty?

Let's start with some background on why I believe libghostty must exist.

There are hundreds of programs that implement some form of terminal emulation.
The most obvious are the actual general purpose terminal emulators like
Ghostty, Kitty, iTerm2, etc. But terminal multiplexers liketmuxorzellijare
also full terminal emulators!1Editors embed their own terminal
emulators too, such asjeditermfor
JetBrains products,Xterm.jsfor VS Code,
orAlacrittyin Zed.

In addition to fully functional terminal emulators, many websites and applications
implement read-only terminal emulation to display logs or command output.
For example,GitHub Actions outputparses simple color sequences (but not much else). And hosting providers
like Vercel or Render implement a simple form of terminal emulation
allowing line clearing and redrawing within build logs as well as
parsing colors.

Many of these implementations are ad-hoc, one-off solutions. They aren't
using any shared library or codebase.2Terminal emulation is a classic
problem that appears simple on the surface but is riddled with unexpected
complexities and edge cases.3As a result, most of these implementations
are incomplete, buggy, and slow.4

Beyond correctness, implementing any form of terminal emulation is awaste of timefor most developers. Terminal emulation is not the core
business of JetBrains, Visual Studio Code, GitHub, Vercel, Render, etc.
It'd benefit them if they could have a stable, reusable solution
that's consistent everywhere.

My answer to this is libghostty: a cross-platform, minimal dependency
library that exposes a C API so feature-rich, correct, and fast terminal
functionality can be embedded by any application anywhere.

## The Beginning:libghostty-vt

The first libghostty library will belibghostty-vt: a zero-dependency
(not even libc) library that provides an API for parsing terminal sequences
and maintaining terminal state such as cursor position, current styles,
text wrapping, and more.

Parsing terminal sequences is the most core functionality of a terminal
emulator, and is required by full terminal emulators like Ghostty down to
simple read-only style-only views such as GitHub Actions or Vercel build output.

Thestate diagrammight
appear relatively simple at first glance, but an implementation
is unexpectedly challenging to get right. For example,Jediterm doesn't handle intermediates correctly,
causing the widely supported "change cursor shape" sequence to swallow
a character in every JetBrains editor at the time of this post.

For style-only parsing, many developers skip the full state diagram. Instead,
they do some light web searching, parse simple
ANSI sequences such as\e[31or\e[41m, and claim "color support."
But style-only sequences are vastly more complex than that, for example they
support RGB which itself can be ina dozen formats.
And I still haven't found a single web console that rendersthis complex style sequencecorrectly.5

libghostty-vtaims to fix all of this.

libghostty-vtis extracted from Ghostty and inherits all of the real world
benefits: SIMD-optimized parsing, very good Unicode support, highly optimized
memory usage, a robust fuzzed and Valgrind-tested codebase, excellent feature
compatibility such as parsing Kitty Graphics Protocol or Tmux Control Mode, and more.

All of this is packaged up into a single zero-dependency C API (it doesn't
even rely on libc), allowing it to be easily embedded into any popular
language ecosystem.

Given the minimal footprint,libghostty-vtwill bewidely portable.Initial targets will be macOS and Linux for bothx86_64andaarch64architectures, since those are the primary targets for Ghostty the
application. But I plan to expand support to additional targets such as Windows,
embedded devices, and the web via WASM.libghosttywill have broader
support than Ghostty the GUI, due to its tighter scope.

## The Long Term

libghostty-vtis just the beginning. Longer term, we will provide morelibghostty-<x>libs that expose additional functionality such as input
handling (keyboard encoding is a big one), GPU rendering (provide us with
an OpenGL or Metal surface and we'll take care of the rest), GTK widgets
and Swift frameworks that handle the entire terminal view, and more.

As fundamental pieces stabilize, we will continue to offer more and more
functionality. These will be structured as a family of libraries to minimize
dependency requirements, code size, and overall maintenance complexity.

## libghostty-vtStatus

I just merged the pull requestexposinglibghostty-vtas a Zig module.
This PR includes a minimal example program, too. If you're a Zig developer,
you can start experimenting withlibghostty-vtimmediately.

The C API isn't ready yet, but it is what I'm working onright nowand
it'll be available for testing soon. All of the work required is defining the
C API, since the core logic is of course all there and has been used by Ghostty
for years. Plus, the Ghostty macOS app already consumes aninternal-only C API.

If you look at the internal-only C header, please ignore the mess. It isn't agoodC API. It is
internal-only and exists to satisfy the needs of the macOS application. This isn't a generally
consumable libghostty, although it is used byreal commercial products
alreadyto embed Ghostty. We'll take a clean slate approach defining the C
API for wider usage.

I plan to versionlibghosttyseparately from Ghostty the application.
This blog post marks the public alpha (not promising API stability)
and I'm hoping to motivate some developers to come use it and eventually
write some language bindings once the C API is ready.

I hope to ship a tagged version oflibghostty-vtwithin the next 6 months,
but it'll all depend on if its ready or not.

## Looking for Feedback

We're at the critical stage of libghostty where we're designing the API,
and the best way to design an API is with feedback from real consumers.
Ghostty is one consumer, we have some community members working on other
libghostty-consuming projects, but we could use as many as we can get!

If you see a use case in your projects or organization for libghostty,
pleasejoin the Ghostty Discordand collaborate
with the developers working on this. If you don't want to join Discord,
email me (email in the footer of this website).

The state oflibghosttyat this stage could be consideredalpha,
so don't expect a polished, stable experience. We're looking for hackers
that want to get on the ground early.

The "alpha" quality is with respect to the API (functions and types) itself. The core logic is
shared with Ghostty and is extremely stable and proven in the real world.

## The Next Frontier

I'm super excited that Ghostty the application has finally reached the
stability where we can start moving towards thelibghosttygoal.libghosttyis the next frontier for Ghostty and I think it has the
ability to make a far larger impact than Ghostty can as a standalone
application itself.

Don't worry, there's plenty of changes for Ghostty the application
and none of this diminishes my excitement or plans for that. Wider
usage oflibghosttywill result in a more feature rich and stable
Ghostty application, too, since Ghostty itself is a consumer oflibghostty.

Boo. 👻

## Footnotes

1. These own the pty to their children, parse all the escape codes, manage
screen state, and ultimately "render" by emitting their own escape codes
to a parent terminal emulator.↩
2. Many websites do use Xterm.js and the GTK ecosystem haslibvte.
But this only covers a tiny fraction of the landscape and each of the
aforementioned examples are limited in their own scope.↩
3. I've spent the better part of 3 years working
on terminal emulation and we'restill finding weird edge cases.↩
4. Here are a couple real examples of impactful issues:Jediterm didn't handle intermediates properly,Apple's Terminal.app just bleeds DCS sequences into the output.
I'm not calling anyone out specifically, just showing that these issues
exist and terminal emulation is very hard to get right.↩
5. A lot of general terminal emulators also got this wrong,including Ghostty just 9 months ago.↩

September 22, 2025
