---
title: </> htmx ~ The fetch()ening
url: https://htmx.org/essays/the-fetchening/
date: 2025-11-03
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-04T11:12:18.717929
screenshot: hackernews_api-htmx-the-fetch-ening.png
---

# </> htmx ~ The fetch()ening

# Fetching a New Age on HtMX

November 01, 2025

By Carson Gross

## The Road to Fetching

### Overview of Our Newfound Disposition towards Fetching

A year or so ago, I made a passionate promise that we would never release version three of the powerful and versatile HtMX. Yet, the seed was planted when I started experimenting with my own implementation of ideas in HtMX. This project led to the creation of fixi.js, which brought me closer familiarity with key concepts available in JavaScript.

## The Future of HtMX

A series of events led me down a path of introspection about our current implementation and its quirks and cruft (a term coined by the HtMX community). Recognizing that adopting fetch as the core AJAX infrastructure would significantly improve stability, it was decided to adapt the existing codebase. This change will not affect most users, except those relying heavily on the events model.

## Key Changes in fetching

### The Fetch-ing Revolution

1. **XMLHttpRequest is Abandoned**: In lieu of leveraging the powerhouses that fetch provides (async infrastructure), this latest iteration of HtMX will leverage fetch as its core AJAX toolkit, thereby removing one of the most debated aspects between ourselves and our users.

2.  **Explicit Attribute Inheritance**

    In this updated version, attribute inheritance from CSS properties is replaced by explicit modifier `inherited`. The syntax to achieve this looks like the following:

    ```html
div
hx-target:inherited = "#output"
```
    This means that if no other rules apply (or ` hx-target` rule isn't set), elements within the specified div will automatically inherit from its root element.

3.  **The Tyranny of Local History**

    This new implementation includes a fundamental overhaul on history retrieval, making our navigation experience significantly smoother. The current structure was based upon storing history locally within browser cache.

To better understand how these changes will affect users, look for details below:


*   Enhanced API stability
*   Key improvements to event handling and user interfaces
