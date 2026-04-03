---
title: "I've FINALLY launched my Product!! - DEV Community"
url: https://dev.to/nombrekeff/ive-finally-launched-my-product-4am7
date: 2025-12-16
site: devto
model: llama3.2:1b
summarized_at: 2025-12-20T11:18:02.628988
screenshot: devto-i-ve-finally-launched-my-product-dev-community.png
---

# I've FINALLY launched my Product!! - DEV Community

## Introducing Cardboard.js on Product Hunt

Cardboard.js is now live on Product Hunt. This lightweight reactive UI library aims to provide simplicity and performance by:

* Eliminating the need for HTML, JSX, or separate CSS files
* Offering built-in state management
* Support for reactive updates (UI updates when state changes)
* Reusable components with CSS-in-JS style support

## Quick Introduction and Code Snippets

### Basic Usage

* Simply initialize Cardboard.js using JavaScript:
```javascript
import {
  tag,
  init,
  allTags
} from '@nkeff/cardboard-js';

const div = allTags();
init(root => {
  // Append elements to the root element
  root.append(
    div('Hello world!'),
  );
});
```
### A Simple Reactive Counter

* Create a reactive component using a state variable:
```javascript
const Counter = () => {
  const count = 0;

  return (
    button()
      .text(`Clicked ${count} times`)
      .stylesIf(count.greaterThan(5), { color: 'red' })
      .stylesIf(false, { backgroundColor: 'lightblue' })
      .styles({ value: true })
      .value(Count.value)
        .
        addStyle((color) => {
          document.body.style.color = color;
        })
    ;
  );
};
```
### Why it Matters

* Provides an easier alternative to frameworks with boilerplate code
* Fast and lightweight (only ~16KB)
* No need for HTML, CSS, or JSX if not used

## How You Can Help

* Support the project on Product Hunt by visiting: [producthunt.com](https://producthunt.com)
* Share your experiences with Cardboard.js on their social media channels.
