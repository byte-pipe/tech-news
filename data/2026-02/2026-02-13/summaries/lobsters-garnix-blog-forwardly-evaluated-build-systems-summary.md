---
title: Garnix Blog: Forwardly-evaluated build systems
url: https://garnix.io/blog/garn2/
date: 2026-02-13
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-13T06:03:06.747558
---

# Garnix Blog: Forwardly-evaluated build systems

# Forwardlly-evaluaated build systems

This article discusses a new approach to speeding up build systems by caching the evaluation process itself, rather than just the build artifacts. The author highlights the performance issues with traditional build systems like Nix, particularly in large monorepos and for tasks like developer shell entry.

## Context
The Nix pipeline involves evaluating a Nix expression to produce a derivation, which is then serialized into a build recipe and used by the builder to create artifacts in the Nix store. The author's project, Garn, aims to improve the evaluation speed by using TypeScript as the frontend language and implementing a forward-evaluating caching mechanism.

## Garn's Approach to Caching
Garn differs from the standard Nix flake cache by tracking the actual reads performed during the evaluation process. This allows it to create a cache key that depends on the specific dependencies used, rather than the entire repository state. This results in more targeted and effective caching.

## Trace-based Caching Mechanism
Garn keeps a record of the `garn.ts` file hash and all files read during evaluation. On subsequent runs, it checks if a cache exists for the same `garn.ts` version and if the read files are the same. If so, it returns the cached result. This approach ensures the cache is only invalidated when necessary, leading to significant speed improvements.

## Performance Benchmarks
The article presents benchmarks comparing Garn's performance to the default Nix and Nix Flakes. The results show that Garn can significantly reduce evaluation times, often by 2-7% compared to Nix, and in some cases, by as much as 2% compared to the default Nix. This is particularly noticeable when changes are made to files that are only read during the evaluation.

## Advantages and Disadvantages
Garn's forward-evaluating cache offers several advantages, including faster evaluation times and reduced memory usage. However, it has a limitation: if expensive computations are used by multiple outputs, the cache will not be reused between them.

## Forward Build Systems
The author notes that Garn's approach aligns with the concept of forward build systems, where the build script is executed once and its results are cached, rather than reasoning backward from a target. This contrasts with traditional build systems like Make.
