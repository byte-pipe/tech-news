---
title: "Your browser renders everything, even what you can't see — `content-visibility: auto` fixes that - DEV Community"
url: https://dev.to/parsajiravand/your-browser-renders-everything-even-what-you-cant-see-content-visibility-auto-fixes-that-3g7c
date: 2026-08-04
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-10T15:32:07.349350
---

# Your browser renders everything, even what you can't see — `content-visibility: auto` fixes that - DEV Community

# Your browser renders everything, even what you can’t see — `content-visibility: auto` fixes that

## What rendering costs on long pages
- The main thread must compute styles, run layout, and paint every element before anything appears.
- Layout is performed for all elements, then the compositor clips to the viewport, so off‑screen work is still done.
- On pages with hundreds of rows or cards this extra work can dominate load time.

## How `content-visibility: auto` works
- Marks an element to be skipped for layout and paint until it is near the viewport.
- The element remains in the DOM and accessibility tree; find‑in‑page and keyboard navigation still see it.
- When the user scrolls close, the browser renders the element just before it becomes visible, and can discard it after scrolling past.

## Why `contain-intrinsic-size` is required
- Skipping layout removes the element’s height, causing it to collapse to zero and breaking scroll position.
- `contain-intrinsic-size: auto <estimate>` provides a placeholder height (e.g., 300 px) so the scrollbar stays stable.
- After the first render the browser updates the size automatically; using `auto` without a value would lock the placeholder forever.

## Practical usage
- Ideal for repeating, vertically stacked elements with clear boundaries: feed cards, table rows, comment items, documentation sections.
- Example CSS pattern:
  ```css
  .comment {
    content-visibility: auto;
    contain-intrinsic-size: auto 80px;
  }
  ```
- Avoid on elements that must report their size at load time (sticky headers, JS measurements before scroll) because the skip would return zero.

## Browser support
- Chrome 85 (2020), Firefox 125 (2024), Safari 18.0 (late 2024) all support the property.
- Older Safari silently ignores it, rendering the page without the optimization.

## Takeaway
- Open DevTools, record a Performance trace, and look for long “Layout” and “Paint” phases on data‑heavy pages.
- Applying `content-visibility: auto` with an appropriate `contain-intrinsic-size` estimate to repeating elements can cut rendering time dramatically (up to 7× faster in real tests) with no functional regressions.
- It is a production‑safe, single‑property optimization that requires no JavaScript changes.