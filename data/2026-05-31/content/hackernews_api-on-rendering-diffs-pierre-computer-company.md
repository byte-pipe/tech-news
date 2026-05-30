---
title: 'On Rendering Diffs :: Pierre Computer Company'
url: https://pierre.computer/writing/on-rendering-diffs
site_name: hackernews_api
content_file: hackernews_api-on-rendering-diffs-pierre-computer-company
fetched_at: '2026-05-31T06:00:27.099893'
original_url: https://pierre.computer/writing/on-rendering-diffs
author: Amadeus Demarzi
date: '2026-05-30'
description: A technical deep dive into how we built the @pierre/diffs package and CodeView component for zero-blanking diff rendering.
tags:
- hackernews
- trending
---

# PIERRE COMPUTER COMPANY █

← Back to Home

## ON RENDERING DIFFS

Posted on May 29, 2026 by@amadeus

 ██████╗ ██╗███████╗███████╗███████╗
 ██╔══██╗██║██╔════╝██╔════╝██╔════╝
██████████╗ ██║ ██║██║█████╗ █████╗ ███████╗
╚═════════╝ ██║ ██║██║██╔══╝ ██╔══╝ ╚════██║
 ██████╔╝██║██║ ██║ ███████║
 ╚═════╝ ╚═╝╚═╝ ╚═╝ ╚══════╝

 ██╗ ██████╗ ██╗███████╗███████╗███████╗
 ██║ ██╔══██╗██║██╔════╝██╔════╝██╔════╝
██████████╗ ██║ ██║██║█████╗ █████╗ ███████╗
╚═══██╔═══╝ ██║ ██║██║██╔══╝ ██╔══╝ ╚════██║
 ██║ ██████╔╝██║██║ ██║ ███████║
 ╚═╝ ╚═════╝ ╚═╝╚═╝ ╚═╝ ╚══════╝

You open a pull request expecting to understand what changed.

For small and medium changes, everything works. The code is readable, the files are there,
				you scroll around, add comments, and it’s all pretty seamless.

Then you open something larger. Maybe an agent generated the implementation, tests,
				fixtures, and snapshots. Maybe the branch just touched more files than expected. Either way,
				the review surface starts to degrade. It might only show you one file at a time, or require
				each file to be loaded separately before you can read it, or even make basic navigation feel
				sluggish.

Some of these are reasonable trade-offs for genuinely hard problems. But they still have a
				cost: reviewers feel the limits of the tool, and product teams have to build workarounds for
				these limits.

Diff rendering matters, but for most tools it is not the product. The product is what
				happens around the code: review workflows, automation, agent output, CI results, and
				collaboration. Code review should support that work, not become something every team has to
				build from scratch.

That is why, about 6 months ago, we releasedDiffs. Our goal was to make
				the code and diff rendering part just work, so teams could spend their time on the product
				around it.

Originally we launched with just the basic pieces:FileandFileDiffcomponents. We quickly got feedback about performance issues, so we
				followed up with a simple virtualizer that avoided rendering code when it was out of view
				and an API to move syntax highlighting into worker threads. The simple virtualizer helped,
				but it was a stopgap. There was still a lot of O(n×m) complexity, high memory usage, and virtualization blanking. What was missing was a
				higher-level component that could manage an entire review surface and handle the hard
				problems related to scale.

That missing layer becameCodeView: a virtualization-first component for
				reviewing code and diffs. And we built it around a deliberately impossible goal:

You should be able to just render any diff.

Not literally, of course. There are physical limits to browsers, compute, and memory. But
				practically speaking, I think we’ve come pretty close, and I’d like to share a bit about how
				we got there.

If you find long-form blog posts boring, go check out theCodeViewplayground
				atDiffsHub.comwhere you can pretty
				much view any PR or diff that GitHub will send our way. Nearly any diff, at any scale,
				nearly instantly.

diffshub[dot]comTake any public diff from GitHub and virtualize it nearly
					instantly, no matter how large, with DiffsHub. Built to show off our brand new CodeView
					component.To try it out, replace `github` with `diffshub` in your address
					bar.pic.twitter.com/5X30YwbpHn

				— Pierre (@pierrecomputer)
				
May 20, 2026

You can check out the CodeView component and more in the latest version of the diffs package
				on npm:@pierre/diffs, orread the docs.

## DIFFS LOOK SIMPLE UNTIL THEY ARE NOT

On the surface, rendering diffs in a browser may not seem very hard. It’s just text, right?
				Browsers are purpose-built to take raw HTML and turn that into something you can look at and
				interact with. Code is just text, after all.

But a good review surface needs more than text. It needs syntax highlighting, line numbers,
				annotations, comments, theming, split and unified layouts, wrapping modes, and enough
				customization to fit into someone else’s product. Each of those features adds cost and
				complexity. Syntax highlighting adds processing time and inflates DOM count. Comments
				involve additional layout complexity that we can’t fully control, and they still have to
				work seamlessly with your existing design system.

WithCodeView, we take that per-file complexity and scale it up; work that was
				cheap for a single diff now has meaningful cost across a large review. We can roughly break
				down the problems into three categories:

* Rendering— DOM complexity grows quickly, and the browser can become
					overloaded while scrolling or interacting with the page.
* Processing— Every file or diff operation gets multiplied, so work that
					was fast in isolation can become expensive when repeated thousands of times.
* Memory— Large files and diffs get transformed into rendering data
					structures, which can push against browser memory limits and make garbage collection more
					frequent.

Our simple virtualizer helped with some rendering problems, and moving highlighting off the
				main thread helped with parts of the processing problem. ButCodeViewneeded to
				treat rendering, memory, and processing as connected parts of the same problem.

## VIRTUALIZATION

Virtualization, or windowing, is a way of tackling the rendering problem. In its simplest
				form, the idea is to only render the part of the content near the viewport. As you scroll,
				the virtualizer renders the new content coming into view and removes content that has moved
				off screen.

Keeping the DOM small has a lot of benefits: lower memory usage, less layout work, less
				paint work, and fewer elements for the browser to manage. The trade-off is that the
				virtualizer has to estimate or measure how tall everything is, and it must coordinate those
				changes dynamically.

One thing that adds to this complexity is that browsers generally manage scroll compositing
				separately from JavaScript execution. This can help scrolling feel more responsive to user
				interactions, but it also means that JavaScript can easily lag behind scroll updates. This
				is often most noticeable when using the scrollbar to make large jumps or scrolling extremely
				quickly — the virtualizer can’t keep up and you’ll scroll into blank regions before the
				JavaScript has time to render the updated content.

Click to see blanking in the old virtualizer

### Common Virtualization Techniques

There are a few common ways to virtualize content in a browser, and each comes with its own
				set of trade-offs.

The most common approach is to create a real scrollable region with the full estimated
				height of the content, then position the visible items where they belong. This keeps
				scrolling native: the scrollbar, momentum, input handling, and accessibility all stay with
				the browser. The trade-off is that the rendered window can fall behind the visual scroll
				position. Fast scrolls and large scrollbar jumps can expose blank space before JavaScript
				has a chance to render the next range. You can reduce that by rendering a larger buffer
				outside the viewport, but that gives back some of the DOM, layout, and memory savings that
				virtualization was supposed to buy you.

Another approach is to keep the visible content in a sticky or fixed container and update
				what it shows withrequestAnimationFrame. In this model, blanking is
				impossible: the content container cannot scroll out of view because it’s not moving with the
				scroll position; it just looks like it is. However, if JavaScript cannot keep up, then
				scrolling can hitch or stutter because JavaScript is now part of the render update path.
				Browser behavior matters here too. Safari, for example, currently capsrequestAnimationFrameat 60Hz even on higher refresh-rate displays, which makes
				this approach feel worse than native scrolling on those devices.

A more extreme version is to emulate scrolling entirely: no native scrollable region, just a
				custom viewport, a fake scrollbar, and content updated viarequestAnimationFrameas the usermovesthrough the document. This can
				avoid browser scroll-size limits because the scroll position is now your own state, not the
				browser’s. But the cost is larger: you now own the details of making scrolling feel native,
				accessible, and correct across different operating systems and browsers.

### The Inverse Sticky Technique

ForCodeView, many of those virtualization trade-offs were not acceptable.
				Native browser scrolling mattered. WebKit-based environments needed to feel good because
				Tauri is a common target for developer tools. And blanking was not an option.

This left us stuck between different approaches that weren’t quite right. After some
				experimentation and frustration, we figured out a hybrid approach that could keep scrolling
				native, mostly decouple positioning fromrequestAnimationFrameupdates, and
				make blanking effectively impossible.

We’ve called our new technique theInverse Sticky Technique, but before we talk
				about how it works, first a quick primer on howstickypositioning works. The
				typical use case for sticky positioning is ensuring that section headers in a scrollable
				list stay in view as you scroll through it. You setposition: sticky; top: 0on
				your section headers and then when they should normally be scrolled out of view, they stay
				fixed to the top of the scroll view as the content below scrolls underneath.

						Section Title 1 
(stuck)

Item 1

Item 2

Item 3

Item 4

Item 5

						Section Title 2 
(stuck)

Item 6

Item 7

Item 8

Item 9

Item 10

						Section Title 3 
(stuck)

Item 11

Item 12

Item 13

Item 14

Item 15

Item 16

Item 17

Item 18

Item 19

Item 20

ForCodeView, we invert the usual sticky behavior. Instead of pinning the top
				of the rendered content to the top of the viewport as you scroll down, the bottom edge of
				the rendered region sticks to the bottom of the viewport when you scroll past it. When you
				scroll back up, the top edge sticks to the top of the viewport.

This gives us native scrolling while the viewport is inside the rendered range. If
				JavaScript falls behind, the rendered region sticks to one edge instead of scrolling away
				and exposing blank space. We can get that behavior with negativetopandbottomsticky offsets, both calculated with the same formula:(contentHeight - viewportHeight) * -1.

Pre Content Buffer

Here’s a quick demo showing theInverse Sticky Technique. We are
								currently halfway scrolled down a larger scroll region.

Try scrolling up or down. This content scrolls with you until you hit the sticky
								bounds, at which point this content will get stuck to the top or bottom.

Post Content Buffer

So to circle back to the goals we set for ourselves: we preserve native scrolling, render
				updates do not need to be frame-perfect to keep scrolling feeling smooth, and even large
				jumps cannot scroll past the rendered content into blank space.

 ┌────────────────────────────────────────────────────┐
 │ 
┌────────────────────────────────────────────────┐
 │

 │ 
│ │
 │

 │ 
│ Full-height content element │
 │

 │ 
│ │
 │

 │ 
│
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓ ▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓ Buffer element ▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓ before virtualized content ▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓ ▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 
│
 │
 │ 
│
 
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
 
│
 │

 │ 
│ │
 │

 │ 
│
 
┌────────────────────────────────────────────┐
 
│
 │
 │ 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 │

┌────────────────────────────────────────────────────────╖

│ ▀ ▀ ▀ ▓▓▓ Browser ▓▓▓ ║

├────────────────────────────────────────────────────────╢

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░ ░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░ Rendered content ░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░ ░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

│
 
│
 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 
│
 
║

╘════════════════════════════════════════════════════════╝

 │ 
│
 
│░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░│
 
│
 |
 │ 
│
 
└────────────────────────────────────────────┘
 
│
 |
 │ 
│ │
 |
 │ 
│ │
 |
 │ 
│ │
 |
 │ 
│ │
 |
 │ 
│ │
 |
 │ 
│ │
 |
 │ 
│ │
 |
 │ 
└────────────────────────────────────────────────┘
 |
 └────────────────────────────────────────────────────┘

				While we were shooting for 
impossible to blank
, Safari still found a way to
				break our hearts. Under sufficiently aggressive scrolling, it can get backed up at the
				compositing layer and expose blank space. It usually takes some work to pull off, but it is
				still technically possible.
			

## SCALABLE LAYOUTS

With virtualization in place, the next problem was calculating the layout and size of the
				scrollable region. A virtualizer works best when its estimates are close to reality. Bad
				estimates mean more corrective work after render: measuring DOM, updating item positions,
				adjusting scroll height, and sometimes fixing the scroll offset to keep the current content
				in place. The more often that happens, the more likely the page is to stutter or make the
				scrollbar jump around.

Fortunately, the first pass is pretty cheap. Files are basicallylineHeight * totalLines. Diffs are only a little more complex because we
				already have the parsed line counts and hunk metadata. From there, we just add the hunk
				separators into the estimate. Simplified, it looks like this:(lineHeight * diff.splitLineCount) + (diff.hunks.length * hunkSeparatorHeight).

### Rendering Line Ranges

With our rough estimates in place,CodeViewcan determine which files should be
				rendered. From there, each rendered file or diff gets the viewport size and position, and
				uses that to decide which lines should be rendered internally.

This architecture came from the previousVirtualizer, butCodeViewpushed us to optimize some of the expensive paths. The old
				implementation could end up iterating through a file or diff from the beginning to find
				where the rendered range should start and end. For most files and diffs, that cost was
				effectively invisible. But once we started testing much larger change sets, it became a
				problem. A hunk with hundreds of thousands of lines could become pathologically expensive
				because the lookup still had to start from zero.

To work around this, we added a cachedposition to linecheckpoint system. That
				lets us use binary search to find a closer starting point before doing the remaining range
				search.

Once a line range is rendered, each file can verify its internal estimate against the actual
				DOM and store any deltas. That lets the first-pass layout stay cheap while still correcting
				the cases where the estimate was wrong.

### Scroll Anchoring

Scroll anchoring is less about raw performance and more about keeping the view stable while
				layout changes. If content above your scroll position changes height, the browser normally
				tries to preserve what you were looking at instead of letting it jump around.

Browsers have built-in scroll anchoring for this, but virtualized views make that mostly
				impossible. The mounted DOM is constantly changing, and the browser cannot make a safe
				decision about which element to anchor to. ForCodeView, we disable the
				browser’s built-in anchoring withoverflow-anchor: noneand handle it
				ourselves.

The core idea is thatCodeViewcan choose an anchor from its own layout model
				before committing DOM changes. It does not need to ask the DOM what the user is looking at;
				it already knows which file or line should be visible at each scroll position.

A typical render update looks roughly like this:

* Find the first fully visible line or file.
* Store that line or file, along with its viewport offset, as the anchor.
* Commit DOM changes for the new rendered range.
* Reconcile any measured height changes.
* Check whether the anchor is still at the same viewport offset.
* If it moved, adjust the scroll position to put it back.

Taken together, rough estimates, line-range rendering optimizations, incrementally measured
				deltas, and scroll anchoring letCodeViewstay fast even with very large diffs,
				without requiring perfect layout information up front.

## DON’T FORGET ABOUT MEMORY

At this pointCodeViewwas in a pretty good place. It could render diffs as
				large as Bun’sZig to Rust rewriteor an even larger Node.jsV8 updatewithout
				falling over.

So, in typical Pierre fashion, we found a larger diff and kept going (we’re probablyhiringbtw). The next set of work
				came from trying to render the diff between Linuxv6 and v7more efficiently.

### Detaching Parsed Strings

Pathological cases like the Linux diff above can mean more than 700 MB of patch content to
				parse and render. One of the first things our diff renderers need is a data structure built
				from that patch file: line content and hunk metadata needed to render them efficiently and
				correctly.

The subtle problem is that parsed strings can keep more memory alive than you expect.
				Depending on how the JavaScript engine represents substrings, a small string can still
				reference the much larger string it came from. That means you can parse a huge patch, keep
				only the lines you need, and still accidentally retain the original giant input string.

In that case, copying strings can actually save memory. By forcing the parsed line content
				to detach from the original patch input, Diffs can keep the data they need without keeping
				the entire source string alive.

This was a good fit for an agent loop because the problem was narrow and easy to test. We
				had a clear hypothesis, a parser function with well-tested inputs and outputs, and an easy
				way to check whether each change improved memory usage and parse time.

┌──────────────────────────────────────────────────────╖
│ ║
│ Memory usage compared 
(Linux v6...v7 diff)
 ║
│ ║
├──────────────────────────────────────────────────────╢
│ ║
│ ████████████████████████████████████████████████░░ ║
│ ████████████████████████████████████████████████░░ ║
│ ║
│ 
Original (2.4 GB)
 ║
│ ║
│ 
──────────────────────────────────────────────────
 ║
│ ║
│ 
████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░
 ║
│ 
████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░
 ║
│ ║
│ 
Optimized (1.15 GB)
 ║
│ ║
╘══════════════════════════════════════════════════════╝

After about an hour of iteration, we had some clear wins. Memory usage on the Linux diff
				dropped from 2.4 GB to around 1.15 GB, and parse time dropped by about 80%.

### Pooling DOM Elements

Virtualization keeps the mounted DOM small, but it can also create a lot of DOM element
				churn. During aggressive scrolling,CodeViewmay remove one set of file or diff
				elements and mount another. Those allocations do not disappear for free: JavaScript objects,
				derived data, event handlers, and DOM nodes all eventually have to be cleaned up, and enough
				garbage collection can show up as main-thread pauses.

There was also repeated setup work every time a new file or diff was rendered. Each one
				lives inside a Shadow DOM wrapper that includes things like stylesheets, theme styles, and
				an SVG icon atlas. Recreating all of that every time an item scrolled in or out of view was
				unnecessary work.

So we added a pool for those containers. Instead of throwing the whole wrapper away,CodeViewcan clean out the item-specific DOM and reuse the shell for the next
				file or diff. That reduces allocation churn, avoids rebuilding the same wrapper structure
				over and over, and keeps garbage collection further away from the scrolling path.

A nice side effect of building the pool was that it forced us to be more deliberate about
				cleanup. Reusing containers safely meant being explicit about clearing references and
				removing item-specific state, which helped patch a few leaks along the way.

### SharingoptionsState

While we were testing against theLinux diff, one thing we noticed was that configuration changes were extremely expensive.

FileandFileDiffwere originally designed to each have their ownoptionsobject. That worked well for rendering a single file or diff, but it
				scaled poorly onceCodeViewwas managing tens of thousands of them. Options
				include things like split or unified layout, line numbers, line wrapping, and other display
				settings. When one of those values changed, we would end up walking every file or diff
				instance to give it a newly spread options object.

With enough instances, that became expensive quickly.

The fix was to keep theoptionsshape, but change where the state actually
				lived. Instead of giving every file or diff its own fresh config object,CodeViewowns the current options as the source of truth. Each rendered item
				gets a stable options object with specialized getters that read from that shared state.

From the item’s perspective, it still readsoptionslike normal. Underneath,
				those values are always coming from the latestCodeViewconfiguration.

That means cosmetic changes no longer require rewriting configuration across every item in
				the review.CodeViewcan update the shared state, re-render the mounted range,
				and let the visible files and diffs read the latest values through the same options object.
				Layout-affecting changes may still need to invalidate estimates, but we already spent time
				making those much more efficient earlier in the post. Anecdotally, we also noticed a 20-30
				MB memory reduction on the Linux diff after implementing this.

### Deferred Syntax Highlighting

This is a feature we’ve had in Diffs for a while, but it is still an important piece of
				making large reviews feel smooth. Syntax highlighting is one of the most expensive
				processing tasks we do. We useShikibecause it is fast enough for most
				cases, has a ton of language support, and can run in a variety of contexts: the browser, web
				workers, and server-side rendering.

But “fast enough” changes when you multiply it across a large review. A 2,000-line
				TypeScript file might only take a few milliseconds to highlight, but that is still expensive
				inside a strict frame budget, especially when many files are being rendered or updated at
				once and the main thread is already busy with rendering and virtualization work.

What’s important is that highlighting is deferred. Files and diffs can render first as plain
				text, then request highlighted output from the worker pool. Each worker owns its own Shiki
				highlighter, keeping the expensive work off the main thread while still allowing multiple
				highlight jobs to make progress.

Additionally, we keep an LRU cache of highlighted results and provide APIs toprimethe highlight cache if we know a file will be rendered soon. That helps
				avoid repeating work when code comes back into view, while still putting a hard limit on how
				much highlighted output can be retained.

The goal is for highlighting to improve the review surface, not block it. Code is readable
				immediately, and highlighting can progressively enhance the experience.

## WRAP THIS UP ALREADY

If you’ve made it this far: damn, thank you.♥

This has been a large project, with a lot of complicated work behind it. I’m proud of what
				we’ve managed to pull off inside the confines of a browser. Should all of this be happening
				in a browser? Probably not. But, you know, challenge accepted.

So far, we’ve mostly talked about the wins: the virtualization techniques, layout
				estimation, memory improvements, DOM pooling, shared options, and deferred highlighting.
				Those are real improvements, but there are still plenty of rough edges.

One of the bigger ones is CSS. Some of the most expensive parts of the virtualization system
				now come from layout and paint. In normal use, that’s usually fine. During aggressive
				scrolling, though, those costs can become the majority of the work. We’ve thrown someagentic research loopsat this, but so far we haven’t made much progress.

Another unresolved issue is serialization in the highlighting pipeline. If you
				syntax-highlight a file with tens of thousands of lines, sending that data back and forth
				through the worker pool gets noticeably expensive. At times, it’s enough to dominate the
				main thread. This is probably an area where a more server-based streaming approach would
				make sense.

Finally, while we do line-based virtualization, we don’t virtualize horizontal scrolling or
				extremely long lines, like you might see in minified JS or CSS. That means mounting one of
				those lines can still create a sizable DOM hit. We do have safeguards to stop the
				highlighter from crashing on very long lines, but that’s a separate problem.

Future plans for Diffs include things like lightweight editing, semantic diffs, and maybe
				even moving some of this work onto the server where it makes sense. In the meantime:

You should be able to just render any diff.

Sohit play on Sandstormand scroll somediffs.

### P.S. Apple, Safari, Please

Before I wrap this up, I wanted to end on a quick note about Safari. A lot ofCodeViewis built on browser primitives that worked consistently across Chrome
				and Firefox. In WebKit, that was not always the experience. Between poor performance and
				limited observability, many wins felt like one step forward and then a half step back.

This is not meant as a dunk on Safari. WebKit is an important target for us, especially
				because of macOS and the popularity of Tauri. I want nothing more than to build first-class
				experiences on WebKit.

Here’s a non-exhaustive list of issues we’ve run into while developingCodeViewand Diffs:

* Sticky compositing performance that appears significantly worse than Chrome or Firefox
					(cases where theInverse Sticky Techniquecan still blank under aggressive
					scrolling).
* Developer tools that make it difficult to trace performance issues across JavaScript,
					layout, paint, and compositing.
* What does the grayotherrepresent in frame timelines, and why is it often
					blowing up our frame buffers?
* Off-screen compositing rules that were difficult to predict
* Deep scrolling/layout bugs when injecting slot containers. Seehttps://bugs.webkit.org/show_bug.cgi?id=308027.
* requestAnimationFramestill being capped at 60Hz, even on higher refresh-rate
					displays.

Work on Safari or on WebKit? Would love to talk — email amadeuspierre.co.

← Back to Home