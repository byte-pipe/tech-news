---
title: Learn how to build a disclosure component using the native HTML details tag - DEV Community
url: https://dev.to/micaavigliano/learn-how-to-build-an-expandable-and-collapsible-component-using-the-native-html-details-tag-1h8j
date: 2026-08-17
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-19T04:07:48.479565
---

# Learn how to build a disclosure component using the native HTML details tag - DEV Community

# Summary of “Learn how to build a disclosure component using the native HTML details tag”

## Introduction
- The article shows how to create a reusable, accessible disclosure component using only the native `<details>` and `<summary>` elements, without JavaScript or additional ARIA attributes.

## Functional requirements for an accessible disclosure
- **Keyboard interaction**: When focus is on `<summary>`, Enter or Space must toggle collapse/expand.  
- **Tab navigation**: Tab moves to the next interactive element inside the disclosure, or to the next element on the page if none exist.  
- **Shift + Tab**: Moves focus to the previous interactive element.  
- **Screen‑reader feedback**: The state (collapsed/expanded) and the accessible name must be announced.

## Anatomy of the `<details>` element
- `<details>` – wrapper for the whole component.  
- `<summary>` – first direct child, acts as the header/control. Acceptable content includes headings (`<h1>`‑`<h6>`) and phrasing content.  
- `::marker` – pseudo‑element that renders the disclosure triangle.  
- `::details-content` – pseudo‑element representing the content sibling of `<summary>`; no extra wrapper needed.

## Attributes
- `open` – when present, the component is expanded by default; omitted means collapsed.  
- `name` – optional; useful for grouping multiple `<details>` so that opening one closes the others automatically.

## CSS strategies

### Styling the `<summary>`
- By default `<summary>` has `display: list-item`, which provides the native disclosure icon.  
- The icon can be customized via `::marker` (e.g., color, size).  

### Removing the native icon
- Apply `display: flex` (or another non‑list display) to `details > summary` to hide the default triangle.  
- Add a custom visual cue (e.g., an SVG) with `aria-hidden="true"` so assistive technologies rely on the native state announcement.

### Using `::details-content` (available since September 2025)
- Allows styling the collapsible content without extra markup.  
- Example collapsed state:  
  ```css
  details::details-content {
    block-size: 0;
    overflow: clip;
  }
  ```
- Expanded state (when `[open]` is present):  
  ```css
  details[open]::details-content {
    padding: 0.85rem;
  }
  ```
- Optional animation respecting `prefers-reduced-motion`: transition of `block-size`, `padding-block`, and `content-visibility`.

### Semantic markup example
```html
<details>
  <summary>Title</summary>
  <p>Paragraph content</p>
  <h4>Subheading</h4>
  <ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
  </ul>
</details>
```
- No non‑semantic `<div>` wrappers are required.

## Keyboard navigation table
- **Tab** – focus moves to the disclosure or to the next interactive element.  
- **Shift + Tab** – focus moves to the previous interactive element.  
- **Space / Enter** – toggles the open/closed state of the `<details>`.

## Screen‑reader behavior (selected examples)
- **VoiceOver macOS + Safari**: Announces “collapsed/expanded, summary” and toggles with Control + Option + Space.  
- **VoiceOver macOS + Chrome**: Announces “collapsed/expanded, disclosure triangle, group”.  
- **VoiceOver macOS + Firefox**: Same pattern as Chrome.  
- The native `<details>` element ensures consistent state announcements across browsers and assistive technologies.

## Takeaway
- The native `<details>`/`<summary>` pair satisfies all core accessibility requirements out‑of‑the‑box.  
- CSS pseudo‑elements (`::marker`, `::details-content`) provide full visual control while preserving semantics and keyboard/AT support.  
- No JavaScript or extra ARIA markup is needed to build a robust, reusable disclosure component.