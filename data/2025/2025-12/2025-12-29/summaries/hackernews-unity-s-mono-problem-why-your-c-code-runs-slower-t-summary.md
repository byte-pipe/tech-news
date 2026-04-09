---
title: "Unity's Mono problem: Why your C# code runs slower than it should | Marek's blog"
url: https://marekfiser.com/blog/mono-vs-dot-net-in-unity/
date: 2025-12-29
site: hackernews
model: llama3.2:1b
summarized_at: 2025-12-29T11:10:30.997629
screenshot: hackernews-unity-s-mono-problem-why-your-c-code-runs-slower-t.png
---

# Unity's Mono problem: Why your C# code runs slower than it should | Marek's blog

Here is a concise and informative summary of the article:

**Execution of C# code in Unity's Mono runtime is slow**

* The execution of C# code in Unity's Mono runtime is significantly slower than expected, with modern .NET being up to three times faster.
* A few small benchmarks have shown speedups of up to 15x, but Unity developers are not yet able to run games on the .NET Modernization framework.
* The current delay of over two years to become production-ready has allowed existing .NET code to be reused in Unity.

**Background and Performance Gap**

* Unity uses the Mono runtime, which is one of only four viable multi-platform implementations of .NET.
* Microsoft opened-sourced .NET (notably .NET Core) in 2014, leading to improvements in performance and cross-platform support.
* Roslyn compiler platform, JIT compiler, and other features have been added since then.

**Implementation Status**

* The Unity engineers are working on porting the engine to .NET CoreCLR, with a goal of 2x-5x performance boost over Mono.
* However, this project has yet to complete, as the core CLR is not available for use in games written for Unity.

**Benchmark Example**

* A unit test was developed and used to demonstrate a significant speed improvement (up to 3x faster) by running under .NET 10 instead of Unity's Mono.
