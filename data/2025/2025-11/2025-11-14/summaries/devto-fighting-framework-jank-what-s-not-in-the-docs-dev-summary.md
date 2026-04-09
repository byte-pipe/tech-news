---
title: "Fighting Framework Jank (What's Not in the Docs) - DEV Community"
url: https://dev.to/michaelsolati/fighting-framework-jank-whats-not-in-the-docs-mj5
date: 2025-11-12
site: devto
model: llama3.2:1b
summarized_at: 2025-11-14T11:13:08.228821
screenshot: devto-fighting-framework-jank-what-s-not-in-the-docs-dev.png
---

# Fighting Framework Jank (What's Not in the Docs) - DEV Community

## The Performance Crisis: A Journey Through Frameworks and Browsers

As software developers, we're often drawn into debates over which framework or library produces better code and results. In this case, however, the focus turned inward after discovering that a seemingly performance issue was actually caused by the developer themselves.

### What Went Wrong?

The dashboard, touted with charts, tables, and animations, experienced a noticeable lag on one machine, prompting users to investigate further. After troubleshooting the issue, we discovered that the problem wasn't any specific framework or library but rather a combination of factors within our own codebase.

### The Core Issue: Not Focusing on Performance

The main culprit behind the janky component was a missed opportunity to focus on the true performance bottleneck: the browser itself. Instead of optimizing through libraries, we could have leveraged browser features that handled animations and rendering more efficiently.

### Learning from a Jekyll Storm Example (Just kidding!)

Fortunately, I took this as an opportunity to offload some of our performance concerns to the browser using its built-in features, a technique known as "browser-based optimization." Specifically, it involved:

*   **Offloading parsing** to let JavaScript focus on rendering while our framework still handles other requests.

This approach allowed us to mitigate the lag issues by giving the browser more control over rendering and improving overall UI responsiveness.

### Best Practices and Takeaways

To avoid similar performance issues in the future, we made a crucial step of self-checking. It's always essential to revisit one's own code and consider whether different approaches or techniques could make positive impacts on performance.

By applying learnings from this journey and incorporating browser-based optimization into our workflows, developers can focus more attention on high-priority tasks like writing efficient software rather than getting bogged down in nitpicky optimizations.
