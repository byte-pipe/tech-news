---
title: Computers can be understood - Made of Bugs
url: https://blog.nelhage.com/post/computers-can-be-understood/
date: 2026-02-11
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-11T06:03:08.067387
---

# Computers can be understood - Made of Bugs

# Computers can be understood - Made of Bugs

This article explores the author's core belief that computer systems are fundamentally understandable through determined exploration and learning. The author argues against treating complex systems as "black boxes," asserting that while understanding every detail of every layer is impossible, understanding them to a sufficient level of abstraction is achievable.

## Software can be understood
The author's central tenet is the belief that computers and their software systems are inherently understandable. This isn't a mere theory but a deeply held conviction that any question about computers has a comprehensible answer obtainable through exploration. Despite the immense complexity of modern systems with numerous layers, the author contends that understanding can occur at various levels of abstraction, with specific layers being understood to any necessary depth.

## Computers are not magic
Computers operate on deterministic foundations, following strict rules. Abstractions built upon these foundations also behave predictably. There are no unknowable forces at play; all behaviors within a system can be understood by examining the underlying layers.

### Source, documentation, and reverse-engineering
Many modern systems utilize open-source software, allowing direct examination of their implementation. When source isn't available, extensive documentation often exists, such as processor interface documentation. If source and documentation are lacking, reverse-engineering through experimentation is possible, a skill commonly practiced by security engineers. The existence of large-scale reverse-engineering projects demonstrates the feasibility of understanding systems through this method.

## Manifestations of this mindset
### Understanding your dependencies
This mindset leads to actively learning about the systems one relies on. Developers often keep source code of dependencies readily available and investigate it when necessary for debugging or clarification.

### Debugging
A deep understanding of dependencies significantly aids in debugging. Tricky bugs often span multiple layers, requiring the ability to analyze behavior from various abstraction levels. These bugs can be challenging and are often engaging for engineers comfortable navigating different layers. The author shares a personal anecdote about debugging a memory flip that required understanding the interplay between user-space libraries, the kernel, the filesystem, and hardware.

### Documentation
A willingness to read source code reduces reliance on documentation. Source provides an authoritative answer when documentation is lacking. However, this can lead to an undervaluation of documentation by engineers who are adept at finding answers elsewhere, potentially resulting in poor system documentation.

### Security
Understanding security issues often necessitates working across multiple levels of abstraction. Attackers exploit practical system behavior, including deviations from documented or intended behavior. Analyzing security vulnerabilities like buffer overflows requires a deep understanding of the compiler, libraries, hardware, and more. The author's early career in security at Ksplice, focused on kernel security, fostered this deep-level understanding.
