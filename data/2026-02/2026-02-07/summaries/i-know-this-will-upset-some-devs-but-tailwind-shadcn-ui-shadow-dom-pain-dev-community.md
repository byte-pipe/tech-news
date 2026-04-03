---
title: I Know This Will Upset Some Devs, but Tailwind + Shadcn/ui + Shadow DOM = Pain - DEV Community
url: https://dev.to/ujja/i-know-this-will-upset-some-devs-but-tailwind-shadcnui-shadow-dom-pain-44l7
date: 2026-02-05
site: devto
model: llama3.2:1b
summarized_at: 2026-02-07T11:09:39.874619
screenshot: devto-i-know-this-will-upset-some-devs-but-tailwind-shad.png
---

# I Know This Will Upset Some Devs, but Tailwind + Shadcn/ui + Shadow DOM = Pain - DEV Community

**Pain Inclusive: Why Shadow DOM + Tailwind CSS = Unacceptable**

The recent post by @sylwia-lask raises concerns about using multiple third-party libraries, including Tailwind CSS and shadcn/UI, in conjunction with Shadow DOM. The author shares a personal experience and outlines the challenges of achieving seamless integration.

**Key Points:**

* The article highlights how combining Shadow DOM with Tailwind CSS can lead to inconsistencies and pain when implementing custom styling.
* Tailwind's utility-first approach is designed for global styles, whereas Shadow DOM isolates components from external styles.
* The author argues that using multiple libraries doesn't guarantee smooth integration; it might actually create more problems.
* Troubleshooting involves checking individual component implementations, which can be time-consuming and error-prone.

**The Setup:**

The post describes a React application wrapping web components with Tailwind CSS and shadcn/UI for UI elements. The goal is to achieve seamless style encapsulation using Shadow DOM.

**Problem 1:** Shadow DOM vs. Tailwind CSS - A Fundamental Conflict
Tailwind's global stylesheet can't penetrate the Shadow DOM boundary, resulting in inconsistent styling.
The author shares an example of how the combination leads to a broken component, illustrating the potential for significant inconsistencies.

**Key Takeaways:**

* Be aware of the fundamental conflict between Shadow DOM and Tailwind CSS.
* Choose carefully according to your project's specific needs.
* Troubleshooting requires testing individual components to identify issues.

**TL;DR:**
Using Tailwind CSS with Shadow DOM is not ideal; consider upgrading one or both libraries to reduce pain. If you do decide to use them together, ensure to test thoroughly to minimize inconsistencies and optimize styles.
