---
title: Building Conflux - My Own Real-time Collaboration Engine in Rust - DEV Community
url: https://dev.to/kayleecodez/building-conflux-my-own-real-time-collaboration-engine-in-rust-41lm
date: 2025-11-13
site: devto
model: llama3.2:1b
summarized_at: 2025-11-19T11:09:46.914187
screenshot: devto-building-conflux-my-own-real-time-collaboration-en.png
---

# Building Conflux - My Own Real-time Collaboration Engine in Rust - DEV Community

**Real-Time Collaboration Engine in Rust: Conflux**

* **Key Ideas and Concepts:**
    + Real-time collaboration system without bloating
    + Built Conflux as a small, easy-to-understand solution for understanding real-time sync systems
    + Conflict-free Replicated Data Type (CRDT) as the underlying approach
* **What is a CRDT?**
    + A data structure that never conflicts, where every update is mergeable and can be freely edited by multiple users without locking.
    + Always converges to a single state through collaborative updates.
    + "Conflict-free" and "normal" way of updating the system break down
* **The Real Stuff Behind Conflux:**
    + Implemented CRDT for collaboration, which involves generating instructions (at each 5th position in a document) that other users need to follow for an accurate final state
    + Server and clients receive these instructions, merge them using mathematical rules to achieve the required state
* **Benefits of Using Conflux:**
    + Easy to understand and implement as a small solution compared to real-time systems
    + Enables collaboration without locking conflicts or bloating

**Structure of Conflux**

| Aspect | Details |
| --- | --- |
| Architecture | CRDT-based data structure for updating |
| Update Process | Collaborative update through instruction generation |
| Mathematical Rules | Merge instructions using conflict-free merge technique |
| Final State | Achieved by converging to a single state through collaborative updates |

**In Conclusion**

Conflux is a real-time collaboration engine built in Rust, leveraging the concept of Conflict-free Replicated Data Types (CRDTs) for seamless and efficient data updates. By understanding CRDTs from the ground up, we can see how Conflux effectively handles updates without conflicts, enabling accurate and collaborative systems like Google Docs, Figma, Replit, and VSCode Live Share.
