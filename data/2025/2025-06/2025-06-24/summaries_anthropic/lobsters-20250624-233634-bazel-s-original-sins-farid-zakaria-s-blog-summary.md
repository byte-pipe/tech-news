---
title: Bazel’s Original Sins | Farid Zakaria’s Blog
url: https://fzakaria.com/2025/06/22/bazel-s-original-sins
date: 2025-06-24
site: lobsters
model: anthropic/claude-3-haiku-20240307
summarized_at: 2025-06-24T23:36:34.655767
---

# Bazel’s Original Sins | Farid Zakaria’s Blog

Here's a 3-4 paragraph analysis of the 'Bazel's Original Sins' article from a solo developer business perspective:

The article discusses several key problems with the Bazel build system that the author has encountered through their experience working on a large migration to Bazel at Google. These "original sins" of Bazel present both challenges and opportunities for a solo developer looking to build a profitable business.

The first problem highlighted is Bazel's default read-only mounting of the root '/' directory into the build sandbox. This can lead to subtle differences and rebuilds due to accidental dependencies on shared system libraries, binaries, or toolchains. As a solo developer, this level of complexity and potential for hidden bugs would be a major hurdle. However, it also points to a clear user pain point and need for a more robust, hermetic build system that just works.

The second issue is Bazel's limited support for Windows, which the author notes was not even a consideration in Google's internal 'Blaze' system. For a solo developer targeting a broader market beyond just Linux users, this lack of cross-platform support would be a significant limitation. Yet it also suggests an opportunity to build a Bazel-like tool that seamlessly supports Windows, macOS, and Linux out of the box.

The final "sin" is Bazel's reinvention of dependency management, which the author argues has led to many of the same problems it sought to solve. This points to the challenge of building a developer tool that truly simplifies complex problems. However, the author's suggestion of a curated, public 'third_party' repository for Bazel users could be a compelling business opportunity for a solo developer - providing a value-added service on top of the core Bazel platform.

Overall, the article highlights the technical complexities and user pain points around build systems that a solo developer could potentially solve. While the challenges are significant, the market indicators (user adoption, revenue potential) and the author's insights suggest there may be viable business opportunities for a skilled solo developer willing to tackle these "original sins" of Bazel.
