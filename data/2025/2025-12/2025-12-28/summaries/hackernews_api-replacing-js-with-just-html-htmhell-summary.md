---
title: Replacing JS with just HTML - HTMHell
url: https://www.htmhell.dev/adventcalendar/2025/27/
date: 2025-12-28
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-28T11:19:19.723695
screenshot: hackernews_api-replacing-js-with-just-html-htmhell.png
---

# Replacing JS with just HTML - HTMHell

# Replacing JavaScript with Just HTML: Native Solutions for Accordions, Expanding Content Panels, Input Filtering Suggestions Dropdowns, Modals and Popovers, Offscreen Navigation Menus

by Aaron T. Grogg, published on December 27, 2025

## What is needed to replace JS?

* JavaScript needs to be replaced with a native HTML or CSS solution
* Users can download less code for better performance
* Existing JS functionality should be handed over to native HTML or CSS for more focused tasks


## Native Solutions for Frequently Used Features

### Accordions / Expanding Content Panels

* Use the `<details>` element to create an HTML-only replacement for JavaScript-based accordions
* Add a "open" attribute to set the default appearance and restrict only one open panel at a time
* Customize the appearance with CSS and trigger the open-close via JS (optional)



### Input Filtering Suggestions Dropdowns

* Provide an input field instead of a dropdown list
* Hand over existing JavaScript functionality for optimal performance
* Remove unused JS code and replace it with native HTML or CSS


## Best Practices for Implementing Native Solutions

* Use attribute selectors to target specific elements in the DOM
* Customize appearances using CSS properties like border, padding, background color, etc.
* Optimize button behavior using JS for better user experience (optional)
* Consider removing unused JS code and replacing it with native HTML or CSS


## Example Code

```html
<!-- <details> element replaced with a custom approach -->
<input id="example-input" type="text" multiple />

<button type="button" js-enabled>Show/Hide</button>

<template #show-example>
  <!-- Hidden content section would be shown here -->
</template>
```
