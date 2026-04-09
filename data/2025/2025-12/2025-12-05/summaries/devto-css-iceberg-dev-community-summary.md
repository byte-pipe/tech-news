---
title: CSS Iceberg - DEV Community
url: https://dev.to/alvaromontoro/css-iceberg-506c
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-05T11:08:04.842377
screenshot: devto-css-iceberg-dev-community.png
---

# CSS Iceberg - DEV Community

## HTML Rendering with CSS Zero-HTML Setup

### Overview

The article discusses a technique of creating artwork using pure CSS without relying on HTML elements. The author showcases how to achieve this by manipulating the root element (`:root`) and applying styles directly.

### Key Points

* Using browser-specific methods (e.g., ` Apache and Firefox`) to render the styles
* Techniques for achieving zero-HTML setup with only web page content
* Applying CSS directly to `::before` and `::after` pseudo-elements

## Structure of Zero-HTML Setup

The technique involves creating a zero HTML document by manipulating the `:root` element and using CSS properties such as `-moz-box-shadow`, `-webkit-box-shadow`, and `-ms-box-shadow`.

### Example Breakdown

*   `%html` and `%body` elements remain unchanged
    *   `%html` is used to store the head section, including title tags, meta tags, and character encoding information.
    *   `%body` contains all other content, such as style sheets, scripts, images, and HTML elements.
*   Using browser-specific methods:
    *   For example, in Apache (a Mozilla-compliant browser), you can apply box-shadow styles directly to `::before` and `::after` pseudo-elements using vendor prefixes like `-moz-box-shadow`, `-webkit-box-shadow`, and `-ms-box-shadow`.

These techniques enable the creation of artwork without relying on HTML elements, making it an effective approach for zero-HTML setups.
