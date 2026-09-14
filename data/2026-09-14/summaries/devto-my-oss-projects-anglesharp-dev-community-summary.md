---
title: My OSS Projects: AngleSharp - DEV Community
url: https://dev.to/florianrappl/my-oss-projects-anglesharp-3b8j
date: 2026-09-09
site: devto
model: llama3.2:1b
summarized_at: 2026-09-14T16:54:06.233113
---

# My OSS Projects: AngleSharp - DEV Community

## My OSS Project: AngleSharp - The Journey Behind the Code

I'm excited to share the story behind AngleSharp, a .NET library that parses HTML, SVG, MathML, CSS, and XML, and gives you back a fully-featured, spec-conformant DOM.

### What is AngleSharp?

AngleSharp is a C# library that aims to deliver a W3C DOM API equivalent without relying on browsers. Instead of using HTML-like syntax, it uses traditional DOM structures.

### The Idea Behind AngleSharp

In 2013, my first open-source project on GitHub. I was flying to the Microsoft MVP Summit, and I brought a printed copy of the HTML5 spec with me. I started coding on the plane, applying the spec to the source code. By the time we landed, the parser was already functional, producing a DOM.

**The Pain Points of Browser Implementations**

However, I quickly discovered that the real bottleneck of browser implementations lies in handling a wide range of edge cases, error handling, and forgiving nature of humans when it comes to markup. As a result, the "happy path" is only 20% of the actual spec.

### Maintaining the Code with a Heavy Heart

After the initial excitement, the reality of maintaining the code set in stone became overwhelming. Every project hit a similar wall: frustration, testing pauses, and self-doubt. This phase is common, but it's essential to recognize when it's time to take a step back, re-evaluate priorities, and consider abandoning the project.

AngleSharp ultimately succeeded in delivering a valuable library, albeit not without learning valuable lessons along the way. If you're considering diving into complex projects, be prepared to face challenges head-on.

## What's Next

While we've made great progress, there's room for improvement. We're actively working on enhancing AngleSharp with additional features and techniques to overcome the limitations of current implementations.

AngleSharp is more than just a tool; it's a testament to the power of perseverance and dedication to creating something valuable, even in the face of seemingly insurmountable challenges.