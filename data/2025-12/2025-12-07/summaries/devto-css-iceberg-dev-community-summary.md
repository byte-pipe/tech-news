---
title: CSS Iceberg - DEV Community
url: https://dev.to/alvaromontoro/css-iceberg-506c
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-07T11:09:32.922705
screenshot: devto-css-iceberg-dev-community.png
---

# CSS Iceberg - DEV Community

# CSS Iceberg Drawing with Zero HTML Elements
======================================================

This week's coding challenge focuses on creating an iceberg drawing using only CSS, without relying on any HTML elements. By leveraging techniques like `::before` and `::after` pseudo-elements, we can achieve a true zero-HTML setup.

## Key Points:
* Use linear gradient to create the sky effect
* Employ conic gradients for shadows and highlights
* Utilize clip-path and shade properties for the iceberg's surface
* Apply repeating radial gradient and linear gradient for water and waves

### Zero HTML Elements Setup:

We'll rely on `*:Root` elements, which can be set up to render CSS content even without explicit `<html>`, providing a true zero-HTML setup.

## Code Explanation:
```css
:root {
  --shade-color: #fff;
  --cone-gradients: var(--conie-radius), var(--cone-gn-point);
}

#body::before {
  clip-path property-value-shade();
  --conie-radius: 50px;
}

#body::after {
  radial-gradient(rotate(45deg), linear-gradient(to bottom, #fff 0%, #000 100%), darken(#000, 10%) calc(-1em rad) 300%);
}
```

## Explanation of Techniques:
* `::before` pseudo-element: used for the iceberg's surface, created with the correct values and settings
* Clip-path functionality: used to generate conic gradients for shadows
* Shade property: applied to create shades on the iceberg's surface
* Repeating radial gradient and linear gradient: used to simulate waves

## Live Demo:
View the code in action by navigating to the provided link: [CodePen - winter/css-iceberg-drawing-with-zero-html-elements](https://codepen.io/anndemo/pen/NNyRQxN)
```
```
