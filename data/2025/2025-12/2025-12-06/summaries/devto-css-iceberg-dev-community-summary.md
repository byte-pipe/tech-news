---
title: CSS Iceberg - DEV Community
url: https://dev.to/alvaromontoro/css-iceberg-506c
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-06T11:09:41.489384
screenshot: devto-css-iceberg-dev-community.png
---

# CSS Iceberg - DEV Community

**CSS Iceberg Snow Theme - Winter Coding Challenge**
=====================================================

* **Description**: Create a zero-element drawing of an iceberg in CSS with minimal HTML elements.
* **Main Techniques**:
 + Zero-HTML setup using `:root` styles
 + Absolute positioning to maintain layout integrity
+ Repeating gradients for water and waves
* **Key Points**:
1. Create a linear gradient for the sky body and two conic gradientshadows.
2. Use `-clip-path` for the iceberg shape to apply a defined size and position.
3. Style `body::before` as an icon (iceberg).
4. Utilize `:after` for water and waves creation with radial and linear gradients respectively.

**Code**
```css
/* Set body styles with zero HTML elements */
*:root {
  -moz-appearance: none;
}

body {
  /* Sky gradient and shadows */
  background-image: linear-gradient(to bottom, #ccc, #aaa);
  background-size: 100% auto;
  background-position: center;
}

/* Water and waves styles using :after pseudo-element */
:after {
  content: '';
  display: block;
  margin: 0 auto;
  border-left: 200px solid rgba(0, 255, 255, 1);
}
```
In this example, the key techniques for a zero-HTML setup include:

* Using `:root` styles to modify global elements.
* Employing absolute positioning to maintain layout integrity.
* Repeating gradients provide visual interest without HTML elements.

The provided structure and implementation guide can help students create their own zero-element drawings using CSS.
