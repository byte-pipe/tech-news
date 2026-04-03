---
title: How a single typo led to RCE in Firefox – kqx
url: https://kqx.io/post/firefox0day/
date: 2026-02-19
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-19T06:03:29.004957
---

# How a single typo led to RCE in Firefox – kqx

# How a single typo led to RCE in Firefox – kqx

This article details a vulnerability discovered in Firefox's SpiderMonkey JavaScript engine, specifically within the Wasm component. The vulnerability, introduced by a single typo in a commit (fcc2f20e35ec), allows for Code Execution within the Firefox renderer process.

## The Guilty Commit

The bug is a typographical error where a `|` character was mistakenly omitted. This resulted in the code incorrectly storing 0 instead of a pointer with the least significant bit (LSB) set. This LSB setting is crucial for SpiderMonkey's JIT compiler to distinguish between a forwarding pointer (used during garbage collection of WebAssembly arrays) and a regular header.

## In-line vs. Out-of-line Arrays

The article explains the difference between in-line and out-of-line storage of WebAssembly arrays. In-line arrays are stored directly after the `WasmArrayObject`, while out-of-line arrays reside in a separate memory region managed by the garbage collector. For out-of-line arrays, a header is used to point to the data.

## The Vulnerable Code Path

The vulnerability occurs in the `WasmArrayObject::obj_moved()` function, which is called when the garbage collector moves a WebAssembly array. To ensure the JIT compiler can find the array's new location, a forwarding pointer is stored in the old header. The typo causes this forwarding pointer to be set to 0, which is misinterpreted as an in-line array. This leads to the garbage collector incorrectly handling the out-of-line array as if it were in-line.

This bug is only exploitable within WebAssembly functions optimized by the JIT compiler.

## Getting a Crash

The author demonstrates the vulnerability with a proof-of-concept (POC) that triggers a crash by repeatedly allocating and populating a WebAssembly array while triggering minor garbage collection. The crash is caused by a read access to an invalid memory address due to the incorrect handling of the out-of-line array's forwarding pointer.
