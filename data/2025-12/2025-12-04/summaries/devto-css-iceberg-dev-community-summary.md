---
title: CSS Iceberg - DEV Community
url: https://dev.to/alvaromontoro/css-iceberg-506c
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-04T11:09:03.694211
screenshot: devto-css-iceberg-dev-community.png
---

# CSS Iceberg - DEV Community

# Winter Iceberg Drawing in Zero-HTML CSS
====================================================

## Overview of Approach
---------------------

The author aimed to create an iceberg drawing without using any HTML elements. Instead, they relied on CSS pseudo-elements and style manipulation to achieve the desired outcome.

## Solution Overview
-------------------

### 1. Preparing for Implementation

*   The sky will serve as a backdrop: a linear gradient providing shade to dark blue.
*   Two conic gradients will create shadows, giving depth to the iceberg.

### 2. Styling the Iceberg

*   `body::before` will house the iceberg with clipping paths and conic gradient shading.
*   `body::after` is used for water and wave rendering with a repeating horizontal radial gradient and linear gradient for depth.

## Example Code
 -------------

```css
body {
    /* sky backdrop */
}

/* create iceberg template */
body::before {
    content: '';
    position: absolute;
    top: 0;
    bottom: 100%;
}

body::before::before {
    clip-path: polygon(25% 0%, 75% 50%, 0% 100%);
    border-shade: #00b2ff;
    clip-path-transform-origin: center bottom;
    stroke-width: 1px;
    position: absolute;
}
```

## Additional Tips
-------------------

For further implementation and optimization, consider exploring additional techniques such as SVG elements for more precise control over visuals or utilizing browser-specific features like `-webkit-appearance` to simulate specific effects.

By adhering to this solution, one can visually recreate the winter iceberg on a pure CSS-powered HTML canvas.
