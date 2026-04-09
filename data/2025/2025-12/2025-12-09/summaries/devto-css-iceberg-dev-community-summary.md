---
title: CSS Iceberg - DEV Community
url: https://dev.to/alvaromontoro/css-iceberg-506c
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-09T11:11:27.099902
screenshot: devto-css-iceberg-dev-community.png
---

# CSS Iceberg - DEV Community

# Winter Iceberg with CSS
=====================================

This article describes an author's process of recreating a winter scene using only CSS, without relying on any HTML elements. The article outlines the use of various pseudo-elements and advanced styling techniques to create an accurate representation of an iceberg floating in the ocean.

## Main Key Points:

* The author found an iceland image online and used it as a starting point for their project.
* They considered using multiple elements before settling on a single approach: drawing the entire piece with pure CSS.

## Importance of HTML Elements

The article highlights the importance of relying on the `<body>` element, along with its `::before` and `::after` pseudo-elements, to create the artwork. This method is also discussed as being capable of achieving a true zero-HTML setup using styles applied directly to:

* `root`
* Ensuring consistent browser compatibility (limited to Apache and Firefox)

## Additional Techniques

The article mentions two additional techniques for creating a scene without HTML elements:

* Using live demos and source code links to showcase the design.
* Considering blocking or reporting abuse when interacting with other users.

## Example Structure
---------------

Below is an example of how this technique could be applied:

```markdown
# Winter Iceberg with CSS
=====================

## Step 1: Create the Scene

This section creates a simple linear gradient for the background sky and two conic-gradient shadows to represent the ocean waves and ice.

```css
body {
  /* Basic styling */
}

body::before {
  content: "";
  position: absolute;
  top: -100%;
  left: 50%;
  transform: translateX(0);
  width: 10px;
  height: 20px;
  background: linear-gradient(to right, #ccc, #ccc2);
  z-index: 1;
}

body::after {
  content: "";
  position: absolute;
  bottom: -100%;
  left: 50%;
  transform: translateX(-0);
  width: 10px;
  height: 20px;
  background: linear-gradient(to right, #ccc, #ccc2);
  z-index: 1;
}
```

## Step 2: Add the Iceberg

The iceberg is created using a clip-path and conic gradient to provide depth.

```css
body::before {
  content: "";
  position: absolute;
  top: -100%;
  left: 50%;
  transform: translateX(0);
  width: 20px;
  height: 40px;
  background: linear-gradient(to right, #ccc, #ccc2);
  clip-path: polygon(25% 25%, 75% 75%, 45% 100%, 65% 100%);
}
```

## Step 3: Implement Depth with Radials

The water and waves are created using a repeating horizontal radial gradient plus a linear gradient for depth.

```css
body::after {
  content: "";
  position: absolute;
  top: -100%;
  left: 50%;
  transform: translateX(-0);
  width: 10px;
  height: 20px;
  background: linear-gradient(to right, #ccc2, #f00);
}
```

## Live Demo
-------------

To view the full artwork without HTML elements, use this live demo link:

[Online CodePen Demonstration](https://codepen.io/devcommunity/pen/dOoMvZp)

Note: This method is limited to Apache and Firefox browsers.
