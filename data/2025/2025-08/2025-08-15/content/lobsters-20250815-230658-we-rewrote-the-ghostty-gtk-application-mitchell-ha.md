---
title: We Rewrote the Ghostty GTK Application – Mitchell Hashimoto
url: https://mitchellh.com/writing/ghostty-gtk-rewrite
site_name: lobsters
fetched_at: '2025-08-15T23:06:58.231594'
original_url: https://mitchellh.com/writing/ghostty-gtk-rewrite
date: '2025-08-15'
published_date: '2025-08-14T00:00:00.000Z'
tags: zig
---

# Mitchell Hashimoto

# We Rewrote the Ghostty GTK Application

August 14, 2025

Wejust completedrewriting the Ghostty GTK application fully embracing theGObject type systemfrom Zig
and also verifying withValgrindevery step of the way.
The result is a more feature rich, stable, and maintainable Ghostty
on Linux and BSD.

There are multiple interesting, technical topics from this process, but
I want to focus in on two (1) interfacing with the GObject type system from
Zig and (2) verifying a GTK application with Valgrind and reflecting on the
memory issues Valgrind found in a Zig codebase.

## Background

First, some quick background. Ghostty is a cross-platform (macOS, Linux,
FreeBSD) terminal emulator. Ghostty sets itself apart from other cross-platform
terminal emulators by using a platform-native application or GUI framework
for each platform1.

On macOS, Ghostty is amulti-thousand line Swift applicationbuilt with Xcode.
On Linux and BSD, Ghostty is amulti-thousand line GTK applicationleveraging direct integrations withX11,Wayland, etc.
Tying it all together, there is avery large shared core written in Zigthat exports a C ABI compatible API.

For full motivation on why Ghostty was the way it was before and why
we decided to rewrite the GTK application now, see theoriginal "gtk-ng" PR.
I'm going to keep this post focused on the takeaways rather than the
motivation.

## GObject Type System and Zig

Whatever your feelings are about OOP and memory management, the reality
is that if you choose GTK, you're forced into interfacing insome waywith the GObject type system. You can't avoid it.

Well youcan avoid itand wedid avoid it. And it leads to a mess
trying to tie the lifetimes of your non-reference-counted objects to the
reference counted ones. There was an entire class of bug that kept popping
up in the Ghostty GTK application that could basically be summed up as:
the Zig memory or the GTK memory has been freed, but not both.

Besides the correctness issues, avoiding the object system also forced
us away from using GTK-native features such as signals (events), properties
(which can be bound to by GUI elements), actions (invoking one-way behavior
from afar), and more.

Let's look at a concrete example: reloadable configuration. The
configuration in Ghostty is represented by a Zig-ownedConfigstructure.
Many different parts of the GUI need to be aware of the configuration:
windows, tabs, menus, splits, etc.

Reloading configuration was a complicated, CPU-intensive (relatively),
and error-prone task because we had to ensure theentire GUIupdated
before we could free the oldConfig.

Now, the ZigConfigstructure is wrapped in areference-countedGhosttyConfigGObject.
When we reload the config, we overwrite our property and let the GObject
property change notification system ripple through the application (sometimes
across multiple event loop ticks). When the old configuration no longer has
any references, it frees. Conceptually much simpler.

In addition to memory management, we can now more easily create custom GTK
widgets. This let us fully embrace modern GTK UI technologies such
asBlueprint.
For example, here is ourterminal window Blueprint file.
This has already led to more easily introducing GUI features like a new
GTK titlebar tabs option, an animated border on bell, etc.

## Valgrind with GTK and Zig

This topic deserves an entire blog post on its own. The gist of it is that
from the first PR to the last, we've run every change and Ghostty feature
through Valgrind and addressed any issues to ensure that there are no memory
leaks, undefined memory access, etc.

Running Valgrind on a GTK application is pretty nasty. We need apretty large suppression file.
I know its a lot, but 80% of that file is provided by GTK itself. The
remainder is primarily 3rd party libraries and GPU drivers. There are perhaps
one or two suppressions I find suspicious (and commented as such).

The important part is we were able to identify a number of bugs along the
way that would'vedefinitelyslipped under the radar. For example, I learned
that if youforget to clear a GObjectWeakRefduring dispose,
it'll cause undefined memory access in thetarget (referenced)object when it
disposes at some point in the future (can be hours, days!). That undefined
memory access happens to befine99% of the time, but once in awhile it
causes a crash. Fun! Valgrind found this without problem.

Memory safety seems to... erm...activatecertain conversations. So let me
say two things:

1. Our Zig codebase had one leak and one undefined memory access.That wasreally surprising to me(in a good way). Our Zig codebase is large,
complex, and uses tons of memory tricks for performance that could easily
lead to unsafe behaviors. I thought we'd have a lot more issues, honestly.
Also, the one leak found was during calling a
3rd party C API (so Zig couldn't detect it). So this is a huge success.Zig has a leak-detecting debug allocator and various safety checks
that are only on during debug and test builds in the Ghostty project.
Additionally, Zig has integrations with Valgrind. For example, Zig
emits a Valgrind client request to mark some memory as undefined whenever
you set a value asundefined(keyword) in Zig. This helps find even
more issues.This experience has really shown me that this isworking, despite
not having any of these protections in our release builds.
2. All other memory issues revolved around C API boundaries.Every other
issue we found (and there were dozens) was directly within the complex
lifetimes of the GObject system or on C API boundaries. My takeaway here
is that you absolutely need tooling like Valgrind to safely call across
C APIs (even if they're not written in C).For most complex libraries that expose a C API, the C API represents
a boundary where object lifetime is transferred or blurred. Whatever
language you're using to interact with it, the safety you're guaranteed
is only as good as understanding the semantics of the API and writing
a good wrapper.

The features Zig provides around memory safety are well documented.
There are a lot of academic or theoretical discussions about what Zig
does or does not do and whether that's good or bad. Those are valuable
discussions to be had, but so are empirical results. This process is showing
empirical results from a large, complex, multi-threaded, multi-platform
Zig project when every individual feature is run with scrutiny under Valgrind.
Takeaway from that what you want, I don't want to start any flame wars!

Going forward, I plan to continue to run every GTK PR within Valgrind
and improving our project documentation so maintainers and contributors
can do so as well (we already have a couple up and running!).

## Conclusion

This is now my 5th time writing the GUI part of Ghostty from scratch:
once with GLFW, once on macOS with SwiftUI, then on macOS with AppKit
plus SwiftUI, once on Linux with GTK procedurally, and now on Linux
with GTK and the full GObject type system.

Each time, I've learned something new and valuable, and I've carried that
experience into each iteration (and across platforms). Even this time,
I've learned some new tricks that I plan on taking back over to macOS.

I want to also highlight that the entire GTK subsystem maintenance team
hopped on board to help complete the rewrite. They did a lot of work, too.

The new, rewritten Ghostty GTK application is now the default when
you build Ghostty from source onmain, and will be shipped to everyone
in the 1.2 release coming in just a few weeks.

## Footnotes

1. Linux people get really worked up when I say "platform-native". There
is no such thing on Linux, but reasonable people agree that something like a
GTK app (or Qt) feels "native" onmost desktopsover other applications.↩

August 14, 2025
