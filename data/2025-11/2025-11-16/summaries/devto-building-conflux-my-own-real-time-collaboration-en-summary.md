---
title: Building Conflux - My Own Real-time Collaboration Engine in Rust - DEV Community
url: https://dev.to/kayleecodez/building-conflux-my-own-real-time-collaboration-engine-in-rust-41lm
date: 2025-11-13
site: devto
model: llama3.2:1b
summarized_at: 2025-11-16T11:09:45.273801
screenshot: devto-building-conflux-my-own-real-time-collaboration-en.png
---

# Building Conflux - My Own Real-time Collaboration Engine in Rust - DEV Community

# Building Conflux - A Real-time Collaboration Engine in Rust

## Key Points and Main Ideas

* The author built Conflux, a small real-time collaboration engine in Rust to understand how complex systems like Google Docs and Slack's chat interfaces work.
* Traditional real-time collaboration uses "high-level" but unclear solutions like Git, which don't directly replicate actual system behavior.
* A better approach is to implement a Conflict-free Replicated Data Type (CRDT), such as ACRTs (Addressive Concurrency and Replication Types).
* CRDTs allow multiple nodes to coordinate updates without conflicts, ensuring everyone has the same state.

## The "Real Stuff" Behind it

* In a traditional version control system, like Git, everyone sees the full history of changes.
* This is problematic in real-time collaboration: when multiple people edit the same text, all versions need to be synchronized.
* CRDTs solve this by sending only necessary instructions.
* For example:
	+ When one person edits text (instruction 1), local CRDT doesn't indicate the change globally; it generates an instruction (2).
	+ Another person sends "Add: ' world' at position 5" to the server, which then propagates (3 and 4).

## The Benefits of a CRDT-Based System

* Allows for real-time synchronization without conflicts.
* Ensures everyone reaches the same state through mathematical rules (instruction merging).
* No more version control issues like Git's merge conflicts.

## Conclusion

Conflux demonstrates how traditional collaborative systems can be built with simpler, more robust technologies like CRDTs. It also highlights that implementing a complex solution in code is possible and desirable, rather than relying on outdated methods like Git.
