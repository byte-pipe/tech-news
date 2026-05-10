---
title: "Replacing a 3 GB SQLite database with a 10 MB FST (finite state transducer) binaryAndrew Quinn's TILs"
url: https://til.andrew-quinn.me/posts/replacing-a-3-gb-sqlite-database-with-a-7-mb-fst-finite-state-trandsucer-binary/
date: 2026-05-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-11T06:05:00.022386
---

# Replacing a 3 GB SQLite database with a 10 MB FST (finite state transducer) binaryAndrew Quinn's TILs

# Replacing a 3 GB SQLite database with a 10 MB FST binary – Andrew Quinn’s TIL

## Background
- The author worked on **tsk**, a Finnish‑English dictionary with incremental “search‑as‑you‑type”.
- Prefix search is the core problem; the usual solution is a trie.
- The first implementation in Go used a trie with basic optimizations and fit in ~60 MB.

## Why the Trie Failed
- Finnish is heavily agglutinative: a single base word can have over a hundred possible endings.
- The number of distinct suffixes grows rapidly, making the trie size explode.
- Attempting to store 40–60 million inflected forms would require far more RAM than a typical laptop can provide.

## Interim Solution
- Switched to a separate SQLite database with Full‑Text Search (FTS) for the inflection data.
- This worked without perceptible delay but required a one‑time 3 GB download, which was not ideal for a “pocket dictionary”.

## Discovering Finite State Transducers (FSTs)
- Inspired by BurntSushi’s article on indexing billions of keys with automata in Rust.
- FSTs can compactly represent ordered sets or maps of strings and support fast prefix, fuzzy, and suffix searches.
- Unlike tries, FSTs share both prefixes and suffixes, which is perfect for languages with many repeated inflectional endings.

## Implementation in Rust
- Wrote a minimal Rust program to extract data from the SQLite database and build an FST.
- The resulting binary was about **10 MB**, a 300× reduction compared to the original 3 GB database.

## Results
- The static data load at runtime avoids the main weakness of FSTs (dynamic updates).
- The Pro version of the application now fits in ~20 MB, three times smaller than the previous free version.
- Memory footprint is dramatically reduced while maintaining fast lookup performance.

## Lessons Learned
- Choosing the “bad easy” solution (SQLite) gave a working prototype but left a large footprint.
- Revisiting the problem with a different language (Rust) and data structure (FST) yielded a far superior outcome.
- For problems that need speed, portability, and better memory ergonomics, Rust and FSTs can be a strong combination.
- Re‑solving a problem with new tools can uncover hidden efficiencies, especially when dealing with highly regular linguistic data.