---
title: Programming Aphorisms
url: https://matklad.github.io/2026/02/11/programming-aphorisms.html
date: 2026-02-13
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-13T06:02:10.251386
---

# Programming Aphorisms

# Programming Knowledge as a Vocabulary of Tricks

This article explores the author's thought process in coding, suggesting that a significant portion of programming knowledge lies in applying a vocabulary of known techniques to new problems. The author uses a Zig programming example – refactoring a function to handle environment variable access in a new Zig version – to illustrate this point.

## Key Points:

* **Problem Solving as Trick Application:** The core idea is that solving new coding problems often involves recognizing and applying previously learned techniques.
* **Abstraction and Naming:** The author highlights the importance of raising the abstraction level by giving names and types to code structures (e.g., `HistoryOptions`). This aids in understanding and communication.
* **Avoiding Midlayer Mistakes:** The author mentions learning about the "midlayer mistake" from a GitHub comment, emphasizing the importance of user-configurable options in a design.
* **Utilizing Shortcuts:** The concept of "shortcuts" – reusable patterns or solutions – is discussed, drawing a parallel to the "Django Views – The Right Way" article.
* **Consistent Naming Conventions:** The author details their preference for specific naming schemes (e.g., `gpa` for allocator, `options` for configuration parameters) adopted from other projects.
* **Positional Dependency Injection (DI):** The author describes a deliberate approach to structuring function signatures using positional arguments for dependencies and named arguments for behavior-altering options.
* **Accumulation of Tricks:** The author views their programming knowledge as a collection of named tricks, acquired through extensive reading, exploration, and active recall.
* **Horizontal Gene Transfer:** The author uses the analogy of "horizontal gene transfer" from biology to describe the process of applying successful techniques from different domains.
* **Deliberate Trick Invention:** The author notes that they sometimes articulate and name new techniques they have been using implicitly.

## Summary of the Proposed Solution:

The author proposes a refactored `readHistory` function in Zig, demonstrating their approach to applying their "vocabulary of tricks":

* Introduces a `HistoryOptions` struct to encapsulate configurable options like the file path.
* Provides a `from_environment` function as a shortcut to create `HistoryOptions` from the environment.
* Uses positional DI for dependencies (`io`, `gpa`) and named arguments for configuration options.
* Names parameters and structures consistently based on conventions learned from other projects.

The author emphasizes that this is their initial starting point and not necessarily the definitive "right way" to solve the problem. The value lies in the process of recognizing and applying established patterns.
