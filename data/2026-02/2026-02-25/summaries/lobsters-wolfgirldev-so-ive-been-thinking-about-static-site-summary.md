---
title: "wolfgirl.dev - So I've Been Thinking About Static Site Generators"
url: https://wolfgirl.dev/blog/2026-02-23-so-ive-been-thinking-about-static-site-generators/
date: 2026-02-25
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-25T06:01:40.398225
---

# wolfgirl.dev - So I've Been Thinking About Static Site Generators

# So I've Been Thinking About Static Site Generators

This article discusses the author's requirements for a new static site generator (SSG) and their plans to develop one. The author differentiates between SSGs for personal use (quirky) and those for a mass audience (more common but flawed). Having experience with the latter, the author aims to create a new SSG that fulfills unmet needs.

## I Have A Need... For Speed™️

The author's top priorities for an SSG are:
1. Easy porting of the current website.
2. Extremely fast build times.
The author defines "fast" as fast across all aspects of the build process, not just one. Analysis of the current site's build process reveals that JavaScript transformations are likely the bottleneck, suggesting a need for a compiled language.

## (1) I Want Fast Clean Builds

While not the primary focus, fast clean builds are desired. The author's current site's build time is 12.34 seconds, with only a small fraction of that time spent in actual system calls. This indicates that JavaScript performance issues are likely the cause of the slow build.

## (2) Build MUST Be In A Compiled Language

Using a compiled language is considered essential for achieving fast content transformations. Several existing Markdown-to-HTML and HTML-to-minified-HTML programs are suitable choices. However, even with compiled languages, the overall build process can be slow if it involves excessive file I/O and process spawning.

## (3) Build SHOULD Be A Single Process

The ideal build process would involve a single compiled program that reads all files into memory, performs transformations, and writes back only the changed content. This minimizes file I/O and allows for faster in-memory transformations, a characteristic of known-fast SSGs.

## (4) I Want Fast Re-Builds When Content Changes

The author desires very fast re-builds, aiming for sub-100ms, ideally sub-20ms. This requires an incremental build system that only rebuilds the necessary parts of the site when content changes. However, implementing proper incremental builds is complex. A naive approach of rebuilding everything upon any change can be inefficient.

## => Build MUST Use A Real Incremental Algorithm

To achieve efficient incremental builds, the author plans to use a real incremental algorithm. Several approaches are mentioned, including:
1. The Red-Green Algorithm (used by Rust).
2. Nix's derivation model.
3. Jade's post-modern build system.
4. Build Systems à la Carte.

The author favors the Red-Green Algorithm due to its ability to mark steps as "green" (unchanged) even with "red" (changed) dependencies, ensuring that only truly affected parts of the site are rebuilt. The article includes a detailed dependency graph and explanation of how the Red-Green algorithm would handle the author's specific use case.
