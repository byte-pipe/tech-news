---
title: Building Conflux - My Own Real-time Collaboration Engine in Rust - DEV Community
url: https://dev.to/kayleecodez/building-conflux-my-own-real-time-collaboration-engine-in-rust-41lm
date: 2025-11-13
site: devto
model: llama3.2:1b
summarized_at: 2025-11-14T11:10:16.995547
screenshot: devto-building-conflux-my-own-real-time-collaboration-en.png
---

# Building Conflux - My Own Real-time Collaboration Engine in Rust - DEV Community

Here is a concise and informative summary of the article:

**Introduction**

* The author wanted to understand how real-time collaboration systems, such as Google Docs and Figma, work without conflicts.
* She recognized that these systems don't involve "high-level" technology, just simple ideas built into software.

**Why Build Conflux?**

* Conflux is a real-time collaboration engine written in Rust, intended for developers who want to understand the underlying mechanics.
* The author built Conflux to demonstrate how to implement CRDT (Conflict-free Replicated Data Type) systems.

**What is a CRDT?**

* A CRDT is a data structure that allows multiple updates to be merged into a single, consistent state without conflicts.
* The key properties of a CRDT are:
	+ **Never conflicts**: Updates don't cause problems with other concurrent changes.
	+ **Mergeable**: Each update can be merged with any prior updates in the system.
	+ **Everyone sees the same state**: All clients see the final, consistent state after all updates have been committed.

**The "Real Stuff" Behind CRDTs**

* When implementing a CRDT-based collaboration system, developers must:
	1. Implement instructions to describe changes to be made.
	2. Send these instructions to all clients and servers.
	3. The server, with the help of algorithms, reconciles these instructions to produce a final state.

**How Conflux Works**

* Conflux's CRDT implementation uses a simple rule for merging updates: it adds or replaces terms as needed to maintain consistency.
* This system allows multiple users to update and see their changes immediately without conflicts.

**Conclusion**

* Understanding how CRDTs and real-time collaboration systems work is crucial for building scalable, reliable applications.
* Conflux is a starting point for understanding the basics of these technologies.
