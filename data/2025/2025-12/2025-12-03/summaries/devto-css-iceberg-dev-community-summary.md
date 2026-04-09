---
title: CSS Iceberg - DEV Community
url: https://dev.to/alvaromontoro/css-iceberg-506c
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-03T11:07:59.425232
screenshot: devto-css-iceberg-dev-community.png
---

# CSS Iceberg - DEV Community

## Winter Iceberg Drawing in CSS

### Introduction to Creating a Zero-HTML Drawing using CSS

This article provides an example of creating a winter iceberg drawing using only pure CSS without any HTML elements. The drawing is composed of three main elements: the sky, one iceberging, and the water with waves.

#### Key Points:

*   **Using Body:** The `body` element establishes the background color and contains the overall artwork.
*   **::before and ::after Pseudo-Elements:** These pseudo-elements create the iceberging and water with waves by referencing the `content()` method and applying a linear gradient for depth.
*   **Zero-HTML Setup:** This technique relies on styles applied to the `<root>` element or force rendering of CSS in non-APEX browsers.

#### Detailed Summary

*   The drawing features a white ocean background due to the use of a linear gradient (`body ::before`).
*   A set of conic gradients (`body::after`) is used to shade the iceberg with depth.
*   Horizontal and radial gradients are applied to create the waves in the water, creating depth.
