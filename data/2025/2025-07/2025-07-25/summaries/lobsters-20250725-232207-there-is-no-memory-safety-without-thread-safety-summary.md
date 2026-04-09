---
title: There is no memory safety without thread safety
url: https://www.ralfj.de/blog/2025/07/24/memory-safety.html
date: 2025-07-25
site: lobsters
model: llama3.2:1b
summarized_at: 2025-07-25T23:22:07.297998
---

# There is no memory safety without thread safety

Here is a 4-paragraph analysis focusing on the problem or opportunity being discussed:

In this article, the solo developer business owner is evaluating whether to create a memory safety system that separates different aspects of program development, such as input/output and thread safety. The author argues that the traditional distinction between memory safety and thread safety may not be sufficient and advocates for a more fundamental approach: removing undefined behavior altogether.

The article highlights two specific problems with current approaches to memory safety: distinguishing between memory safety (preventing use-after-free or out-of-bounds access) and avoiding threads crashes (which involve concurrent access to shared resources). The author notes that these distinctions are not always meaningful in practice, as the two issues may overlap. Furthermore, current memory safety approaches require a significant increase in complexity, making them unattractive for solo developers.

A closer examination of the example provided reveals the limitations of traditional safety concepts. By storing interface types as pairs of pointer and value pointers, Go inadvertently creates a data structure that can lead to undefined behavior when accessed from different threads or with incorrect assumptions about the underlying memory layout. The author likens this to a program that attempts to access an invalid memory address as if it were a valid one.

The article concludes by emphasizing the need for a more fundamental approach to memory safety. The author advocates for removing undefined behavior altogether, which would eliminate many of the complexities and difficulties associated with traditional safety approaches. By doing so, solo developers could focus on building high-quality software without worrying about obscure low-level pitfalls that plague today's memory safety systems.

As the article makes clear, making significant changes to an existing system is a daunting task for a solo developer. To address these concerns, solo developers need to demonstrate a passion for prioritizing quality over complexity and be willing to invest time in learning about new technologies and methodologies. Specifically, this may involve:

* Investing in formal education or training on fundamental software engineering concepts
* Building experience with languages, frameworks, and tools that align with traditional safety approaches
* Staying up-to-date with the latest research and advances in software development methodologies

To demonstrate commitment to memory safety, solo developers should also be willing to invest time and effort into testing their code thoroughly and providing good quality documentation.
