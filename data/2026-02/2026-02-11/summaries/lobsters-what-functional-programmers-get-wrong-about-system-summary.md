---
title: What Functional Programmers Get Wrong About Systems - Ian Duncan
url: https://iankduncan.com/engineering/2026-02-09-what-functional-programmers-get-wrong-about-systems/
date: 2026-02-11
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-11T06:03:38.582953
---

# What Functional Programmers Get Wrong About Systems - Ian Duncan

# What Functional Programmers Get Wrong About Systems - Ian Duncan

This article argues that functional programming's emphasis on reasoning about programs can lead to an underestimation of the complexities of real-world systems, particularly in distributed environments. While FP tools like static typing and algebraic data types are powerful for local correctness, they don't fully address system-level properties.

## Your monolith is a distributed system
The author asserts that all production systems, including monoliths, are inherently distributed systems due to interactions between components across networks, databases, and third-party services. Correctness in production is not a property of a single program but of the entire deployment ensemble, which involves multiple versions of code running concurrently.

## The unit of correctness is the set of deployments
The central claim is that the unit of correctness in production is the set of deployments, not the individual program. A type checker verifies a single artifact, but it doesn't account for the interactions and potential incompatibilities between different versions of that artifact running simultaneously. Bugs often arise from these interactions.

## Multiple versions are always running
In production, multiple versions of code are always running concurrently (e.g., rolling deployments, blue-green deployments, canary releases). This creates challenges when introducing changes, as older versions may encounter data or schemas not recognized by the new version, leading to errors. Type systems, designed for single-version reasoning, cannot fully capture these scenarios.

## Addressing the limitations
The article highlights that serialization formats like Protocol Buffers and Avro address the compatibility issues arising from multiple versions by using numeric field tags and requiring schema information at deserialization. Erlang/OTP is presented as a notable exception, having built the concept of managing multiple versions of modules directly into the language and runtime, allowing for state migration during upgrades. The two-version limit in OTP's design is crucial for keeping the mixed-version state space manageable.
