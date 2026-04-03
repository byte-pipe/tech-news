---
title: "noq, noq, who's there? - Iroh"
url: https://www.iroh.computer/blog/noq-announcement
date: 2026-03-19
site: hnrss
model: llama3.2:1b
summarized_at: 2026-03-20T11:16:10.978148
---

# noq, noq, who's there? - Iroh

# noq Summary

The article discusses the development and introduction of **noq**, a new QUIC (Quick UDP Internet Connection) implementation that includes multipath support and NAT traversal features.

## Key Points:

* noq is a general-purpose QUIC implementation, not just limited to iroh's usecase
* It has been around since v0.96 and provided transport layer support for **irōh**
* A forked version of **quinnback** in 2024 was considered due to heavy workload on **iq**, management of NAT traversal, and juggling congestion states
* **noq**'s fork started small with the goal of contributing back code from **quirn** while keeping the maintenance effort minimal
* A hard fork with continued collaboration is recommended as it avoids problems caused by constant changes

## noq Features:

* **QUIC Multipath**: Support for multiple paths (relay, direct IPv4, direct IPv6) in a single QUIC context
* **QUIC NAT Traversal**: Implementation of the draft for handling Network Address Translators (NATs)
* The implementation is designed to be generic and intended for use by any QUM ( QUIC Unbound Modular UDRF) purpose

## noq Goals:

* To provide a robust QUIC implementation that can handle diverse networking scenarios
* Minimize the burden of maintenance on QUIN (Quinn) maintainers
* Encourage collaboration while avoiding iteration cycles

The article concludes by highlighting **noq**'s commitment to transparency and cooperation, as well as its goal to be an essential part of any QUM development efforts.