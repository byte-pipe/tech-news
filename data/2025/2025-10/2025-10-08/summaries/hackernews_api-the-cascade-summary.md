---
title: The Cascade
url: https://thecascade.dev/article/least-amount-of-css/
date: 2025-10-06
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-08T11:19:23.040417
screenshot: hackernews_api-the-cascade.png
---

# The Cascade

**Responsive and Accessible Website Principles**
=====================================================

To create a website that is both responsive and accessible, the following principles can be applied:

### 1. Responsive Web Design

*   Ensure images do not overflow the viewport by using maximum widths.
*   Provide a default font family, with options for lighter and darker themes.
*   Adjust line height to prevent tight spacing within elements.

### 2. Accessibility Features

*   Enable dark mode based on system preferences or allow users to toggle it manually.
*   Limit content width to maintain readability and accessibility.

**Code Implementation**
-----------------------

#### img, svg, video Support
---------------------------

```javascript
img,
svg,
video
{
  max-width: 100%;
  display: block;
}
```

#### Font Family and Size Adjustment
-------------------------------------

```html
<style>
  body {
    font-family: System UI; /* basicsystem-uifor example */
    -webkit-font-size: 1.25rem; /* for responsive fonts */
    line-height: 1.5; /* adjust line height to prevent tight spacing */

    /* default size adjustment */
    & .standard {
      width: calc(100% - 2rem); /* remove extra spaces between lines and elements */
    }
  }

  body {
    font-size: 18px;
    line-height: 1.7;
  }
</style>
```

#### Dark Mode Support
----------------------

```plaintext
<style>
  html {
    color-scheme: light dark; /* enable or disable dark mode as requested */
  }

  button {
    -webkit-appearance: none;
    background: none;
    border: none;
    padding: none;
    margin: 0; /* reset default styles */
  }
</style>

<style>
  html {
    lang: en;
    color-scheme: light dark;
  }
</style>
```

#### Restraining Content Width
------------------------------

```javascript
<style>
  main, article, aside, header, nav, section, footer {
    max-width: 70ch; /* set a minimum width */
    margin-left: auto; /* center horizontally """
    -webkit-box-sizing: border-box;
    -ms-expand: 0;
    padding: 20px; /* added padding for better layout control */
    margin-right: 4rem; /* add space after navigation elements */
}
</style>
```

**Best Practices**
--------------------

*   Always consider the default system fonts, colors, and spacing when designing.
*   Provide instructions on how to toggle dark mode manually or through device settings.
*   Use accessible attributes like aria-label for better screen reader experience.
