---
title: An Interactive Intro to CRDTs | jakelazaroff.com
url: https://jakelazaroff.com/words/an-interactive-intro-to-crdts/
date: 2026-03-03
site: hnrss
model: llama3.2:1b
summarized_at: 2026-03-04T11:25:49.594694
---

# An Interactive Intro to CRDTs | jakelazaroff.com

**What is a CRDT?**

A CRDT (Conflict-free Replicated Data Type) is a type of data structure that allows multiple entities to access and update shared data simultaneously without worrying about conflicts or inconsistencies. CRDTs are designed to enable rich and collaborative applications, such as Google Docs and Figma, without the need for a central server to sync changes.

**Key Characteristics:**

* Each peer (computer) can update its own state instantaneously without a network request to check with other peers.
* The peers may have different states at different points in time, but are guaranteed to converge on a single agreed-upon state.
* CRDTs are designed to be scalable, fault-tolerant, and reliable.

**Two Types of CRDTs:**

* **State-based CRDTs:** transmit their full state between peers and merge all states together to obtain a new state.
* **Operation-based CRDTs:** transmit only the actions taken by users, allowing for more efficient and lightweight updates without compromising consistency.

**CRDTs and Challenges:**

* **Message Delivery Constraints:** operation-based CRDTs impose constraints on the communication channel, requiring messages to be delivered exactly once and in causal order to each peer.
* **Scalability:** CRDTs can be challenging to scale in large numbers due to the need for peer-to-peer communication.

**Conclusion:**

CRDTs are a fundamental concept in distributed systems, enabling multiple entities to collaborate on shared data without incurring the overhead of network latency. By understanding the basics of CRDTs, developers can build more robust and efficient applications, such as collaborative workflows and real-time data updates.
