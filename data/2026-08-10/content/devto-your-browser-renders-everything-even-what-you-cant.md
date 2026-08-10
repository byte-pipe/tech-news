---
title: 'Your browser renders everything, even what you can''t see — `content-visibility: auto` fixes that - DEV Community'
url: https://dev.to/parsajiravand/your-browser-renders-everything-even-what-you-cant-see-content-visibility-auto-fixes-that-3g7c
site_name: devto
content_file: devto-your-browser-renders-everything-even-what-you-cant
fetched_at: '2026-08-10T15:30:26.084671'
original_url: https://dev.to/parsajiravand/your-browser-renders-everything-even-what-you-cant-see-content-visibility-auto-fixes-that-3g7c
author: Parsa Jiravand
date: '2026-08-04'
description: When you open a long page — a news feed, an admin table, a documentation article — the browser lays... Tagged with css, webdev, performance, frontend.
tags: '#css, #webdev, #performance, #frontend'
---

When you open a long page — a news feed, an admin table, a documentation article — the browser lays out and paints every element on it. All 500 table rows. All 300 feed cards. All the sections you'll never scroll to in this session. Then it does it again when anything changes, and again on resize. That work is real, it costs time, and most of it is invisible to the user right now.

content-visibility: autois the CSS property that says: skip rendering this element until it's near the viewport. The element stays in the DOM, the accessibility tree includes it, find-in-page searches it — but the browser doesn't spend layout or paint budget on it until the user scrolls close enough to need it.

## What "rendering" actually costs on long pages

Browser rendering isn't just placing pixels on screen. The main thread has to compute styles for each element, run layout to calculate sizes and positions, and then paint. Each step depends on the previous one, and the browser has to process every element before any of it can display.

The browser doesn't know which elements are visible at layout time. It calculates positions for everything, then clips to the viewport during compositing — by which point the expensive work is already done. For a page with 500 rows, that's 500 elements burning through the full pipeline before the user sees anything.

## content-visibility: autoin two lines

.feed-card
 
{

 
content-visibility
:
 
auto
;

 
contain-intrinsic-size
:
 
auto
 
300px
;

}

Enter fullscreen mode

Exit fullscreen mode

That's the entire implementation. The browser groups each.feed-cardinto a containment context. For any card that isn't near the viewport, it skips layout and paint completely. When the user scrolls toward it, the browser renders it before it enters view. When the user scrolls past it again, the browser can discard the paint and reclaim memory.

The improvement on real-world long pages is not incremental. Google measured a 7× faster rendering time for a news page after applyingcontent-visibilityto article cards. For a content-heavy page with a slow device, that difference is the line between "loaded" and "still loading."

## The gotcha:contain-intrinsic-sizeis not optional

When the browser skips layout for an off-screen element, it doesn't know how tall it is. Without a size, the element collapses to zero height. A page with 500 collapsed elements has the wrong scrollbar, and scroll position jumps around as elements render in — the classic "why does the page keep moving" experience.

contain-intrinsic-sizegives the browser a placeholder size for skipped elements:

contain-intrinsic-size
:
 
auto
 
300
px
;

Enter fullscreen mode

Exit fullscreen mode

Theautokeyword here matters. After the browser renders an element for the first time, it remembers the actual height and uses that for future off-screen cycles. The300pxis the initial estimate — a placeholder for elements that haven't been seen yet. It doesn't need to be exact, just close enough to keep the scrollbar stable during the initial render.

Withoutauto, the browser always uses the hint value and never updates it from actual layout, which breaks variable-height elements permanently.

## 🎮 Try it yourself

▶️ Open the interactive playground →

500 cards, a live timer, and a side-by-side comparison — run both buttons and watch the numbers.

## What it does not break

A common concern: if the browser skips rendering, does accessibility, keyboard navigation, or find-in-page break?

It does not. The browser maintains the DOM and the accessibility tree regardless ofcontent-visibility. Ctrl+F / Cmd+F finds text inside skipped elements and scrolls them into view, triggering rendering for that element on the way. Pressing Tab to reach a focusable element inside a skipped container triggers immediate rendering for that container. Screen readers traverse the DOM, not the render tree — off-screen elements are still accessible.

The only thingcontent-visibility: autoskips is visual rendering work: layout, paint, and compositing. The element is off-screen, not absent.

## Where to apply it — and where not to

The property is most effective on repeating elements with clear boundaries: feed cards, table rows, comment threads, list items, documentation sections. If the element is one of many similar elements stacked vertically, and most of them are off-screen at load time, it's a strong candidate.

/* Good candidates */

.comment
 
{
 
content-visibility
:
 
auto
;
 
contain-intrinsic-size
:
 
auto
 
80px
;
 
}

.data-row
 
{
 
content-visibility
:
 
auto
;
 
contain-intrinsic-size
:
 
auto
 
48px
;
 
}

.article-section
 
{
 
content-visibility
:
 
auto
;
 
contain-intrinsic-size
:
 
auto
 
400px
;
 
}

Enter fullscreen mode

Exit fullscreen mode

Don't apply it to elements that need to report their size at load time — sticky headers, elements measured in JavaScript withgetBoundingClientRect()before scroll, or anything in a layout that depends on all children being fully laid out simultaneously. For those, the browser's skip means the measurement returns zero and the calculation breaks.

## Browser support

content-visibilityisBaseline 2024: Chrome 85 (August 2020), Firefox 125 (April 2024), Safari 18.0 (September 2024). Safari completing the set in late 2024 made it safe for production without fallbacks, assuming a modern browser baseline. For older Safari, the property is silently ignored — the page renders normally, just without the optimization.

## 🧠 Test yourself

Think it clicked?Take the 8-question quiz →

Instant feedback, a hint on every question, and an explanation for each answer — right or wrong.

## The takeaway

Open DevTools on your longest page, run a Performance recording during load, and look at the "Layout" and "Paint" entries on the main thread. If they're wide and the page is slow to become interactive,content-visibility: autoon the repeating elements is often the fastest fix available — one CSS property that can halve rendering time on data-heavy pages. Addcontain-intrinsic-size: auto <your-estimate>alongside it to keep the scrollbar accurate, and the change is production-safe with no other modifications required.

Thanks for reading! Let's stay connected:

* ⭐GitHub— follow me and star the projects:github.com/parsajiravand
* 💬Discord— join the frontend best-practices community:discord.gg/d9KRhuAwQ
* 📸Instagram— frontend best practices, daily:@bestpractice___
* 💼LinkedIn—linkedin.com/in/parsa-jiravand
* ✉️Email(work & contract inquiries):bestpractice2026@gmail.com

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse