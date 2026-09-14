---
title: Distributed Systems Classics
url: https://nvartolomei.com/dist-sys-classics/
date: 2026-09-14
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-15T07:39:27.812288
---

# Distributed Systems Classics

# Distributed Systems Classics Summary

## Overview
A curated collection of foundational papers that have profoundly influenced distributed systems research. The list serves as a starting point for understanding core problems, algorithms, and concepts in the field.

## Key Papers and Contributions
- Leslie Lamport (1978) – *Time, clocks, and the ordering of events in a distributed system*  
  Introduces logical clocks and the happens‑before relation for reasoning about event ordering.

- Leslie Lamport, Robert Shostak, and Marshall Pease (1982) – *The Byzantine Generals Problem*  
  Formalizes the Byzantine fault model and establishes conditions for achieving agreement despite malicious failures.

- K. Mani Chandy and Leslie Lamport (1985) – *Distributed snapshots: determining global states of distributed systems*  
  Presents the snapshot algorithm for capturing consistent global states without halting the system.

- Michael J. Fischer, Nancy A. Lynch, and Michael S. Paterson (1985) – *Impossibility of distributed consensus with one faulty process*  
  Proves the FLP impossibility result, showing that deterministic consensus cannot be guaranteed in an asynchronous system with even a single crash failure.

- Brian M. Oki and Barbara H. Liskov (1988) – *Viewstamped Replication: A New Primary Copy Method to Support Highly‑Available Distributed Systems*  
  Describes a replication protocol that tolerates failures while maintaining consistency through view changes.

- Leslie Lamport (1998) – *The part‑time parliament*  
  Introduces the Paxos algorithm for fault‑tolerant consensus in asynchronous networks.

- Leslie Lamport (2001) – *Paxos Made Simple*  
  Provides an accessible exposition of Paxos, clarifying its core concepts and operation.

- Satoshi Nakamoto (2008) – *Bitcoin: A Peer‑to‑Peer Electronic Cash System*  
  Proposes a decentralized cryptocurrency using a proof‑of‑work consensus mechanism and a public ledger (blockchain).

- Marc Shapiro, Nuno Preguiça, Carlos Baquero, and Marek Zawirski (2011) – *Conflict‑free replicated data types*  
  Introduces CRDTs, data structures that guarantee eventual consistency without coordination.

- Diego Ongaro and John Ousterhout (2014) – *In search of an understandable consensus algorithm*  
  Presents Raft, a consensus protocol designed for clarity and ease of implementation while providing the same guarantees as Paxos.