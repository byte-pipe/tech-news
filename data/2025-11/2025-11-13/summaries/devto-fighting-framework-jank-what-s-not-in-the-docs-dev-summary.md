---
title: "Fighting Framework Jank (What's Not in the Docs) - DEV Community"
url: https://dev.to/michaelsolati/fighting-framework-jank-whats-not-in-the-docs-mj5
date: 2025-11-12
site: devto
model: llama3.2:1b
summarized_at: 2025-11-13T11:09:20.632958
screenshot: devto-fighting-framework-jank-what-s-not-in-the-docs-dev.png
---

# Fighting Framework Jank (What's Not in the Docs) - DEV Community

## Summary

The article addresses common issues faced by developers who ship new dashboards, highlighting the importance of understanding the performance and optimization techniques used in front-end frameworks like React or Vue. The author shares their personal experience with a janky dashboard that displayed smooth animations but stuttered when viewed on different machines, leading to a significant decrease in performance.

The main idea is not about blaming the framework but rather recognizing the limitations of optimizing libraries within the browser itself and taking advantage of its capabilities for better performance.

## Key Points

* The author's "janky" dashboard was an anomaly with smooth animations but slowed down when viewed on different machines.
* The author realized that the issue was not with the framework, but rather a flaw in their own code that relied on frameworks' optimization techniques.
* Profiling revealed two main job responsibilities of the component: rendering a static SVG icon and firing off an analytics event.
* The problem was caused by hydration costs (creating Virtual DOM nodes) and main thread blockages (combining the React function with the browser's work on the screen).
* To fix this, the author turned to "one weird trick": offloading parsing tasks to the browser.

## Technical Considerations

* Performance optimization techniques can be complex and depend on various factors like rendering strategies, CSS animations, and layout management.
* Debugging and profiling tools are crucial in identifying performance bottlenecks and understanding how different components interact with each other.
* A thorough test suite is essential to ensure that the fix works consistently across all environments and platforms.

## Best Practices

* Understand the browser's capabilities and limitations when optimizing front-end code.
* Avoid relying heavily on libraries' optimization techniques, instead leveraging browsers' strengths for better performance.
* Keep testing and profiling regularly to identify and address performance issues early on.
