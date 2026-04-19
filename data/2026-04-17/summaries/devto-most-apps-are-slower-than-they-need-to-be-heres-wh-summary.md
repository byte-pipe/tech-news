---
title: Most Apps Are Slower Than They Need to Be — Here’s Why (Live Demo🛸) - DEV Community
url: https://dev.to/sylwia-lask/most-apps-are-slower-than-they-need-to-be-heres-why-live-demo-2hh8
date: 2026-04-16
site: devto
model: llama3.2:1b
summarized_at: 2026-04-17T06:13:46.877460
---

# Most Apps Are Slower Than They Need to Be — Here’s Why (Live Demo🛸) - DEV Community

Here is a concise and informative summary of the article:

**Practical WebGPU and WebAssembly Performance**

* The browser has evolved beyond just a UI layer, enabling complex computations, GPU processing, audio simulation, and machine learning model execution.
* Most platforms use these technologies separately; instead, we can combine them to achieve tangible gains.

**The Two Technologies: WebAssembly and WebGPU**

* **WebAssembly**: Runs on the CPU, allowing for direct execution of low-level, compiled code in the browser. It's designed to execute JavaScript-like code directly.
* **WebGPU**: Grants access to the GPU, providing a relatively direct and powerful form of interaction between the CPU and the GPU.

**Combining WebAssembly and WebGPU: A Demo**

The article presents a concrete example of combining these two technologies. The demo showcases how text typed into an input field is converted into particles that explode when clicked and dragged across the screen.

* **Rendered Text to Bitmap**: JavaScript renders the input text into an image bitmap using Canvas 2D.
* **WebAssembly-Implementation**: The bitmap is passed to WebAssembly, where a "somewhat over-engineered" algorithm maps the image into particles. This combination yields a significant performance gain (2-3× faster) compared to equipping everything with JavaScript only.

**Insights and Future Directions**

The author highlights the potential for these technologies to coexist in practical applications, providing developers with more effective tools to tackle complex tasks.