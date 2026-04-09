---
title: "How we found a bug in Go's arm64 compiler"
url: https://blog.cloudflare.com/how-we-found-a-bug-in-gos-arm64-compiler/
date: 2025-10-08
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-09T11:14:43.185159
screenshot: hackernews_api-how-we-found-a-bug-in-go-s-arm64-compiler.png
---

# How we found a bug in Go's arm64 compiler

# How We Found a Bug in Go's Arm64 Compiler

August 8, 2025

* Thea Heinen

## **Investigating a Strange Panic**

Our team noticed that there were sporadic crashes on arm64 machines running our services. We thought this may be related to stack corruption and investigated further.

### Coredumps per hour

We started seeing fatal errors correlate with recovered panics, which we correlated with the amount of panics occurring within stack unwinding. This initially led us to assume that all fatalities happen while the code is unwinding and stop using panic/recover for error handling in our system.

## **Theoretical Mitigation**

Since stoping with an upstream release worked, it seemed like a reliable approach to mitigate fatal panics. However, this wasn't sustainable; we saw higher rates offatal panics than expected again. It showed that while the upstream fix solved the root cause (issue #73259), our system was still experiencing similar issues.

## **Deeper Dive**

We decided to investigate further and checked more closely for any patterns or correlations with our infrastructure, release rollouts, or even Mars' position relative to Earth. Since none of these factors were directly tied to our panics increasing or decreasing, we were left with an enigma: we didn't understand the root cause.

## **Root Cause**

With no clear pattern matching and other more superficial investigations, we had to be more creative. We realized that without a thorough investigation, it's easy for issues like this to go unresolved.

This is how our team discovered the root cause of several rare "panic" issues in Go's arm64 compiler
