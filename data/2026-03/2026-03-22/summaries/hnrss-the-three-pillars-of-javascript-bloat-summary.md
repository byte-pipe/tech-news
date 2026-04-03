---
title: The Three Pillars of JavaScript Bloat
url: https://43081j.com/2026/03/three-pillars-of-javascript-bloat
date: 2026-03-22
site: hnrss
model: llama3.2:1b
summarized_at: 2026-03-22T11:26:22.866604
---

# The Three Pillars of JavaScript Bloat

## The Three Pillars of JavaScript Bloat: Understanding Dependency Trees

The increasing reliance on npm's dependency management has driven growth in the community and improved node.js performance for many users. However, this also brings its own set of issues, particularly with dependency trees. Here are three key aspects to consider:

### 1. Older Runtime Support (with Safety and Realms)

*   The graph illustrates how some packages bundle smaller functions (`is-string`, `hasOwn`, and others) that should be taken for granted in modern JavaScript.
      *   These small utilities rely on outdated engines (or old Node.js versions) to function correctly, leading to a "cleanup" initiative that identifies and removes redundant code from the tree.
*   Safety features like ES5 compatibility help mitigate potential issues with older engines. For example:
    *   `forEach` and other common array methods are only available in ES5.
    *   Functions like `Object.keys` require extra implementation for old Node.js versions.

### 2. Protection Against Global Namespace Mutation

*   This pillar deals with maintaining the integrity of the global scope within Node.js, preventing malicious updates to the built-in modules.
*   The concept of "primordial objects" introduces a safeguard against potential issues when modifying these objects' properties.
*   Packages like `Math.intrinsic` re-export specific functions from math libraries to avoid introducing mutations.

### 3. Cross Realm Values

*   Additionally, maintaining cohesion across different Node.js realms becomes crucial in establishing consistent API implementations for various packages.
*   This could be achieved by reusing existing utilities and minimizing the need to recreate them individually.

By understanding these three key aspects of JavaScript bloat in dependency trees, you can better grasp why certain modules are needed and what it takes to address their presence.