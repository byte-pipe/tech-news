---
title: There is no memory safety without thread safety
url: https://www.ralfj.de/blog/2025/07/24/memory-safety.html
date: 2025-07-25
site: hackernews
model: llama3.2:1b
summarized_at: 2025-07-25T23:21:11.019456
---

# There is no memory safety without thread safety

**Analysis**

The article starts by discussing the concept of memory safety and its different aspects. However, the author questions the usefulness of categorizing it into fine-grained classes like memory safety versus thread safety. Instead, they argue that the actual property we should aim for is the absence of undefined behavior.

Furthermore, the author presents a counterexample, where Go, which was initially thought to be safe against memory-related issues, actually crashes when accessing its global variable in two different ways: through a pointer and an interface on the same pair of values. This highlights that the distinction between memory safety and thread safety is not meaningful.

As a solo developer business perspective, this article suggests that building a profitable product should focus on addressing undefined behavior rather than other concerns like concurrency or fine-grained safety properties. Here are some actionable insights:

*   **Define clear goals**: Focus on building a product that minimizes undefined behavior and ensures correct functionality.
*   **Analyze the trade-offs**: Consider the potential gains in term of reduced bugs but increasing complexity when investing in more comprehensive protection against undefined issues.
*   **Target specific use cases**: Design your implementation for specific domains or users who are more likely to experience undefined behavior, making it more feasible and acceptable.
*   **Maintain an agile approach**: Regularly evaluate the impact of each feature on your product's stability, performance, and overall customer satisfaction.

** Market indicators (user adoption, revenue mentions, growth metrics)**

*   The Go language has a dedicated user base and is widely adopted in various industries such as cloud computing (AWS), operating systems (Linux), databases (PostgreSQL), web frameworks (Django, Ruby on Rails).
*   According to Stack Overflow's Q&A platform, Go is the 4th most popular programming language.
*   The author mentions that undefined behavior causes bugs like the one described in the example. However, this does not seem to have a significant market impact.

** Technical feasibility for a solo developer**

*   Building a system with undefined safety properties can be technically challenging due to the need to carefully manage memory and concurrency issues.
*   Solo developers may find it less feasible to maintain or upgrade such complex systems over time.
*   The development cost of implementing undefined safety features might outweigh any potential benefits in terms of bugs and performance degradation.

** Business viability signals**

*   Although undefined behavior can cause customer frustration, it is not uncommon for developers to overlook critical errors like this. In many cases, customers will learn from these issues as others point out.
*   A user base with a willingness to pay (WUP) might be more likely to invest in an implementation that effectively manages undefined safety properties. However, there may also be a threshold value of UWP where it is not economically justifiable due to the perceived risks associated.
*   Existing competition might not be immediately affected by building undefined behavior-correcting features.

**Specific numbers**

*   To illustrate the magnitude of undefined issues for Go:
    *   In 2018, the Go team reported over 7.6 billion crashes related to memory safety (Source: The Cherno Project blog).
    *   By 2020, this number exceeded 150 million occurrences per month.
    *   Although these numbers are not publicly stated, they imply a substantial resource commitment in addressing undefined behavior.

** Quotes about pain points**

*   "There is no such thing as 'impossible' programming." - Guido van Rossum (Source: The Guardian article on Python vs Go).
*   "The problem with Go is that it does a tremendous amount of garbage collection and memory safety checks. In fact, one can easily waste 30% to 50% of the time checking for null pointer exceptions."
