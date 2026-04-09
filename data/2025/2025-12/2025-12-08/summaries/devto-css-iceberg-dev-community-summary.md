---
title: CSS Iceberg - DEV Community
url: https://dev.to/alvaromontoro/css-iceberg-506c
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-08T11:11:25.192501
screenshot: devto-css-iceberg-dev-community.png
---

# CSS Iceberg - DEV Community

# Creating a Zero-HTML Canvas Drawing using CSS

## Overview

The article discusses creating an iceberg drawing using only CSS without any HTML elements. The author showcases their process, highlighting the use of `::before` and `::after` pseudo-elements, along with custom styles applied directly to the root element (`:root`) to achieve a true zero-HTML setup.

## Key Points

* Using multiple elements is initially considered but ultimately discarded in favor of a single technique.
* The drawing consists of three distinct parts: sky, iceberg, and water/waves created using linear gradients, clip-paths, conic gradients, and repeating radials.
* Only `::before` and `::after` pseudo-elements are used for custom styling, as they provide more flexibility than absolute positioning.

## Step-by-Step Guide

* Use a browser with support for `<body>`'s `::before` and `::after` pseudo-elements (e.g., Apache and Firefox).
* Utilize the root element (`:root`) to apply styles directly.
* Create a linear gradient for the sky with conic gradients for the iceberg using `clip-path` and shading.
* Generate a repeating horizontals radial gradient for water/waves and adjust its depth using `linear-gradient`.
* Apply custom styling to the root element using custom properties.

## Conclusion

The article demonstrates an innovative approach to creating artwork without relying on HTML elements. By leveraging `::before` and `::after`, as well as direct root element manipulation, it is possible to achieve a low-HTML setup using only CSS.
