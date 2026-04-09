---
title: NIH Is Far Cheaper Than The Wrong Dependency
url: https://lewiscampbell.tech/blog/250718.html
site_name: lobsters
fetched_at: '2025-07-18T23:07:57.213241'
original_url: https://lewiscampbell.tech/blog/250718.html
date: '2025-07-18'
description: Frivilous dependencies are the enemy of maintainability.
tags: practices, scaling
---

# NIH Is Far Cheaper Than The Wrong Dependency

(Title written with apologies toSandi Metz.)

One of the biggest fallacies in coding is that dependencies have zero downsides. It's treated as free functionality you don't have to write yourself. Wow, what a deal!

But dependencies absolutely have a cost.

* They may require a significant time investment to learn to use. Often they're so large and complex that simply writing the functionality yourself is faster than learning. Sometimes it's easier to write it yourself thaninstallthe dependency...
* Their breaking changes can trigger expensive re-writes of your own code to handle a new interface.
* You need to ensure they end up on your clients' machine.

Let us consider this last point; how many absurdly complicated containerisation or bundling setups do we encounter in our work because someone does not want to "reinvent the wheel" and instead opts to use large, complex dependencies? How many times did people take the time to appreciate they've re-invented an entirely different wheel that has nothing to do with their apps core functionality, just to deploy and run the bloody thing?

Instructive here isTigerbeetle, a financial database written entirely with Vanilla Zig:

TigerBeetlehas a “zero dependencies” policy, apart from the Zig toolchain. Dependencies, in general, inevitably lead to supply chain attacks, safety and performance risk, and slow install times. For foundational infrastructure in particular, the cost of any dependency is further amplified throughout the rest of the stack.

Similarly, tools have costs. A small standardized toolbox is simpler to operate than an array of specialized instruments each with a dedicated manual. Our primary tool is Zig. It may not be the best for everything, but it's good enough for most things. We invest into our Zig tooling to ensure that we can tackle new problems quickly, with a minimum of accidental complexity in our local development environment.

## A Framework for Evaluating Dependencies

I am aware this post is areductio ad absurdummagnet. "What so you make your own silicon wafers?", etc, etc. (Programmers of a certain generation might bring up a webcomic and butterflies).
Ultimately, we all depend on something. But not all dependencies are created equal. Allow me to introduce my Framework for Evaluating Dependencies.

We have five categories:

Ubiquity

How widely available is it? Are target environments likely to have it pre-installed? Will we need to complicate deployment with containerisation or bundling?

Stability

How frequent are breaking changes, deprecations, or shifts in the "meta"?

Depth

How much functionality lies beneath the API/interface? How much harder would it be to do without the dependency?

Ergonomics

Is the abstraction provided declarative? Is the API pleasant to use?

Watertightness

Does the abstraction leak? How often must you consider the underlying technology?

Dependency peddlers typically only talk about ergonomics, and ignore other criteria.

With that in mind, let's evaluate some dependencies:

## Good Dependencies

### POSIX System Calls

Ubiquity

Can be used on Linux, Android, macOS, BSDs, etc.

Stability

Extremely stable, breaking changes are rare.

Depth

Incredibly deep. A single
open
 call hides hundreds of thousands of lines of kernel code.

Ergonomics

Mediocre. Uses many flags and old school C conventions, but not terrible.

Watertightness

Mostly good, though storage devices can have their own conception of what "persisted" means.

### ECMA-48 Terminal Control Codes

Ubiquity

Other than cmd.exe in windows I can't think of a major terminal emulator that doesn't respond to these.

Stability

No changes to the standard since 1991.

Depth

The alternative I think would be to make your own standard for a character framebuffer. Not an impossible task but a bit much to spin off for a project.

Ergonomics

Not all that bad, if you can ignore the line noise of the Esc character.

Watertightness

Very good. Very rarely do you need to care about what hardware your terminal emulator is running on.

### The Web Platform (Web APIs, HTML, JS, CSS etc)

Ubiquity

The web browser is the most widely deployed document rendered/app platform/virtual machine on earth. They're everywhere and these days largely evergreen.

Stability

Fairly big commitment to backwards compatibility.

Depth

Very deep, writing your own browser to render your page or website is not feasible.

Ergonomics

They're alright. Some cruft, but the documentation and developer tooling is excellent.

Watertightness

Outside of maybe interacting with files, audio, video, it's a pretty water tight abstraction.

## Bad Dependencies

I will leave this as an exercise for the reader!

But remember; think critically, evaluate the costs as well of the benefits, and choose wisely.
