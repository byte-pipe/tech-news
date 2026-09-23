---
title: I Turned DEV.to Into a Walkable 3D Library — Debugging It Has Been a Nightmare - DEV Community
url: https://dev.to/mikachu/i-turned-devto-into-a-walkable-3d-library-debugging-it-has-been-a-nightmare-4lkd
site_name: devto
content_file: devto-i-turned-devto-into-a-walkable-3d-library-debuggin
fetched_at: '2026-09-23T15:19:26.221957'
original_url: https://dev.to/mikachu/i-turned-devto-into-a-walkable-3d-library-debugging-it-has-been-a-nightmare-4lkd
author: Mika Flowers
date: '2026-09-23'
description: DEV Library is my idea of first-person 3D reimagining of DEV.to. Not a themed scene with some... Tagged with buildinpublic, webdev, nextjs, ai.
tags: '#buildinpublic, #webdev, #nextjs, #ai'
---

Shift from AI vibe coding to real debugging

DEV Library is my idea of first-person 3D reimagining of DEV.to. Not a themed scene with some article cards floating around, but the actual live catalogue, pulled from the Forem API, rendered as a walkable archive. Shelves. Rooms. Districts. Real cover images on real book spines. You move through it with WASD instead of scrolling a feed.

The idea sounds fun in a sentence. Building it has mostly been a long series of things breaking in ways I didn't expect, followed by me figuring out why.

This whole thing started as vibe coding, almost entirely for the Sanity x Dev.to Hackathon. I described what I wanted, and it appeared — cinematic lighting, spatial audio, entire systems I hadn't fully thought through myself.

That works great right up until the project gets big enough that things start breaking in ways a regenerated response can't actually fix. Once the catalogue was real and the scene had to survive thousands of live articles streaming in instead of a dozen mocked ones, I stopped being able to just describe my way out of problems. I had to open the animation loop, trace refs, and actually understand what was happening under the hood — not because I wanted to, but because "try again" stopped working. This post is mostly about that part.

## The stack

This is built on Next.js and Three.js — no game engine, no visual scene editor, nothing with a viewport where you drag an object and watch it move. Three.js is a JavaScript library for rendering 3D graphics in the browser using WebGL, and everything in it is code. There's no inspector panel with X/Y/Z fields you can nudge with arrow keys. If a shelf is floating six units too high, you don't drag it down — you find the line of code that sets its position and change the number.

That sounds like a minor inconvenience until you're trying to place hundreds of shelves relative to a curving, procedurally generated hallway. In something like Unity or Unreal, you'd see the mismatch instantly and drag things into place. In Three.js, you're reasoning about coordinates blind — changing a number, waiting for the scene to rebuild, walking into it with WASD to see if it's right, and doing that loop again if it isn't. Every position, rotation, and offset in this project exists only as a number in a function somewhere, not as something you can see and grab.

That's the actual reason so many of the bugs below are about where things are rather than what things look like. Coordinate math doesn't forgive vibe coding the way visual styling does — a color that's slightly off still looks fine, but a shelf position that's slightly off either clips through a wall or floats in the void, and you won't know which until you physically walk there.

## It didn't start here

This began as Oniria, Oni for short. — a first-person 3D dream journal. Memories as glowing orbs, relationship tethers between them you could physically fly along. It grew fast: cinematic lighting, spatial audio, recursive dream-diving, memory decay, an "Observatory" mode to zoom out and see your whole dream history at once. By the time I stopped to look around, I was 197 commits ahead of main and thirteen thousand lines deep, and I had to ask the obvious question: is this too much for a hackathon?

The answer reframed the problem instead of shrinking it:

"The scope is too big for a hackathon if we keep treating every idea as equally important. But that doesn't mean Oniria itself is 'too much.' The problem is now product focus, not ambition."

So I picked one 90-second experience and froze everything else behind it. Somewhere in that process I looked at what I'd actually built — first-person flight through a graph of linked, related things — and asked a different question: what if this wasn't about dreams at all?

A codebase explorer idea came first (folders as worlds, imports as hallways). It never shipped, but it cracked something open: the engine wasn't really about dreams, it was a way to turn any linked, browsable structure into a place. So I asked for something stranger — import the entire DEV.to website into the engine. Literally surf the web.

## Issue #1: the first version was a conspiracy board

It technically worked. Articles, profiles, tags, search results, all floating in space simultaneously. Technically impressive. Completely unnavigable — you'd spawn into a cloud of unrelated nodes with no sense of where to look first.

This wasn't really a bug so much as a design failure, but it set the tone for everything after it: the fix wasn't a new feature, it was a metaphor. A library. Rooms as topics. Shelves as feeds. Books as articles. People get their own rooms. One idea did more for usability than every rendering improvement I'd made up to that point, because architecture can tell you where to go in a way floating labels never could.

## Issue #2: the library rearranged itself while I was standing in it

Once real DEV articles started streaming in instead of a handful of mocked ones, the library needed hundreds, then thousands of shelves. That's when navigation quietly broke.

The cause: shelves had been positioning themselves relative to each other. Reasonable-sounding, until you realize it means navigation was an emergent side effect of layout instead of something the world actually guaranteed. Every time another page of articles streamed in, shelf positions could shift underneath the player. On a normal website, rerendering a list is boring. In a first-person space, it can teleport the person standing inside it.

This is the architectural decision the whole project ended up hanging off of:

The path is authoritative. Everything else decorates the path.

One deterministic causeway became the coordinate system for the entire library — a function called archivePathPoint(bay) that converts a logical "bay" index into a world-space position. Shelves, fog, skyline, energy lanes, camera clamping — all of it now samples from that same fixed route instead of improvising its own position. Shelf placement itself moved to a seeded deterministic function, taking stable inputs (shelf ID, approximate bay, side of the path, jitter) so the world could still look organic without shelves jumping to new spots every time React state updated.

That single rule fixed an entire category of bugs at once. Streaming in more of the catalogue stopped being dangerous the moment shelves stopped being the thing defining the world.

## Issue #3: zoneRef.current is not a function

This is the one that actually made me sit down and trace code line by line instead of just asking for another pass. It's also the clearest example of that shift I mentioned up top — the point where vibe coding stopped being enough on its own.

Runtime
 
TypeError

zoneRef
.
current
 
is
 
not
 
a
 
function

900
 
|
 
if 
(
nearestSection
 
!==
 
currentSection
)
 
{

901
 
|
 
currentSection
 
=
 
nearestSection

902
 
|
 
zoneRef
.
current
(
nearestSection
)

Enter fullscreen mode

Exit fullscreen mode

zoneRef.current being called like a function meant it wasn't holding one. I went into the animation loop and traced where zoneRef actually got assigned — it was set inside a useEffect with a dependency on currentSection, but the animation loop was already running before that effect fired for the first time. A stale-closure timing problem: the ref existed, just not yet, relative to when the render loop reached for it.

This is the part nobody quite prepares you for with AI-assisted building. It can hand you cinematic rendering, spatial audio, and a fully explorable 3D library shockingly fast. It cannot hand you the fifteen minutes of "wait, when does this effect actually run relative to the render loop" that fixing this required. That part you still have to do yourself.

## Where it's at right now

The catalogue streams in bounded pages instead of one blocking request. Shelves are seeded deterministically so they don't reshuffle as more content loads. The camera survives scene rebuilds. Districts organize themselves by real article tags instead of a fixed taxonomy. Nearby shelves react — brightening, waking their covers — while distant ones dim, which turned out to matter more than I expected: in 2D, hierarchy comes from typography and layout; inside a 3D archive with dozens of shelves visible at once, distance and brightness are the only hierarchy you get.

It's not done. I'm still working out how much of the catalogue can stay loaded before distant shelves start costing more frame time than they're worth. The skyline and haze systems are tuned but not perf-verified across a weaker GPU. And I'm sure there's at least one more zoneRef-shaped bug waiting somewhere in there that I haven't walked into yet.

But for the first time, it actually behaves like the thing I set out to build: not a DEV.to-themed scene, but an attempt to make the whole living catalogue into somewhere you can actually walk — one broken ref, one flickering cover, and one screen-eating book at a time.

More soon, including when this turns into my actual Sanity Challenge submission — where the CMS side of this story gets to be the main character instead of a supporting one.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse