---
title: No Graphics API — Sebastian Aaltonen
url: https://www.sebastianaaltonen.com/blog/no-graphics-api
date: 2025-12-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-17T11:23:03.568154
screenshot: hackernews_api-no-graphics-api-sebastian-aaltonen.png
---

# No Graphics API — Sebastian Aaltonen

## Introduction to Graphics API Changes

As a developer with 30 years of experience in graphics programming, I have witnessed significant changes over the past decade in real-time computer graphics APIs.

### Current State: High-Level APIs vs. Low-Level Chips

For the last four years, I've been working on building a new renderer called HypeHype for WebGPU, Metal (Mac & iOS), and Vulkan (Android). At first glance, it's easy to see that PC graphics APIs have undergone a transformation.

* Today: Low-level hardware details and high-degree of optimization are valued more than ever before. **Key Points Highlighted Below**

### What We've Been Doing All Along

I want to emphasize that some information provided in this blog post is indeed from various open-source Linux drivers, including AMD RDNA ISA documents and GPUOpen, Nvidia PTX ISA documents.

### Progress Towards Modern Graphics APIs

AMD's Mantle architecture, Microsoft's DirectX 12, and Vulkan were initially well-received due to their performance advantages. However, I believe that **There Is Something Missing** and the lack of a fully fleshed-out "Mantile" ecosystem for developers who require specific tools and assets has led to more significant challenges. Meanwhile some hardware vendors are embracing WebGPU and Metal instead.

### Lessons Learned

Our initial research revealed numerous performance regressions after transitioning from DirectX 11 renderers to DirectX 12. The high-pressure environment within Ubisoft's internal engine development team resulted in these unexpected results. After re-examining the existing graphics APIs, **We Understand That We Need More Information** and more optimization.

### Key Takeaways

* Low-level hardware details are often overlooked
* High levels of efficiency require a clear understanding of how different rendering engines approach complexity
* Industry collaboration is key to resolving performance issues

### Conclusion
