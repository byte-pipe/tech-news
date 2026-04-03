---
title: macOS dotfiles should not go in ~/Library/Application Support @ rebecca®
url: https://becca.ooo/blog/macos-dotfiles/
date: 2025-08-26
site: lobsters
model: llama3.2:1b
summarized_at: 2025-08-26T23:33:26.462378
---

# macOS dotfiles should not go in ~/Library/Application Support @ rebecca®

**Problem or Opportunity: Misconfigured Command-Line Tools on macOS**

The article highlights a common problem faced by developers building command-line tools for macOS - they often mistakenly rely on `~/Library/Application Support` instead of implementing the XDG Base Directory Specification. This behavior is not only inefficient but also fails to accommodate users' expectations, causing frustration and user complaints.

**Market Indicators: User Adoption and Revenue**

The author cites statistics from popular libraries such as Python's `platformdirs`, JavaScript's `env-paths`, Rust's `dirscrate`, and Go's `ardg/xdg`, which indicate that command-line tools are increasingly shifting towards preferring `.config` directories. While not all applications using these libraries follow this convention, the trend suggests a growing market for optimized configuration directory management.

According to a rough estimate of 242 million downloads per month in Python, 95 million in JavaScript, and 4.8 million in Rust, along with an additional 913 packages relying on `ardg/xdg`, it's clear that developers are increasingly catering to user expectations while adopting more efficient configuration directory solutions.

**Technical Feasibility: Solving the Problem**

Implementing the XDG Base Directory Specification requires careful consideration of complex aspects such as:

* Determining the optimal configuration directory
* Handling different operating systems and environments (e.g., Linux vs. macOS)
* Ensuring backward compatibility with existing tools and libraries

While implementing a solution may require additional complexity, it allows developers to cater to both user expectations and efficient configuration management.

**Business Viability Signals: Willingness to Pay and Existing Competition**

The author argues that the primary business obstacle is people's expectations vs. reality. To overcome this, your solo developer business should focus on:

* Providing high-quality solutions catering to the needs of users.
* Building a strong online presence through engaging documentation, community support, and successful customer testimonials.

If you can demonstrate that your command-line tool management solution offers significant benefits over relying on `~/Library/Application Support`, you will attract more customers and increase demand for your service.

**Specific Numbers and Quotes: Pricing and Revenue**

The article does not explicitly mention pricing or revenue. However, based on the estimated numbers mentioned in the text (e.g., 242 million downloads per month, 95 million), we can estimate potential revenue figures. A rough estimate would suggest that these libraries support tens of millions of developers worldwide, with each script requiring manual configuration according to the XDG guidelines.

Given the sheer scale and user base, it's possible that your command-line tool management solution could generate a significant portion of this revenue. However, without more concrete estimates or sales figures from existing customers, we can only speculate on potential earnings based solely on the outlined market indication.
