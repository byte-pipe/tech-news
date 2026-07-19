---
title: "My benchmark's Python column was N/A for a year — CPython's 4300-digit limit, and eight other bugs - DEV Community"
url: https://dev.to/gde/my-benchmarks-python-column-was-na-for-a-year-cpythons-4300-digit-limit-and-eight-other-bugs-1hgk
date: 2026-07-15
site: devto
model: llama3.2:1b
summarized_at: 2026-07-19T11:31:44.628333
---

# My benchmark's Python column was N/A for a year — CPython's 4300-digit limit, and eight other bugs - DEV Community

# Summer Bug Smash: Clear the Lineup Submission

## The Codebase Overview
The codebase is a multi-language A2A (Agent-to-Agent) performance suite built with four agents, including Python and Go, Gemini tool-calling, ADK handlers, Node.js, and Rust as direct handlers.

## The Problem: Column of Data Not Found

*   On the benchmark's column for Mersenne primes in Clear the Lineup track, there was a 24th prime that caused the tool to raise an error due to its 4,300-digit limit when using string conversion.
*   This problem arose because the Python agent was structured in such a way that it could never produce data at or above N=24.

## The Bug Fix

1.  **Switch from Wall Clock to Performance Counter**: Replace `time.time()` (wall clock time) with `time.perf_counter()` for more accurate timing.
2.  **Regression Test Added**: Implement a regression test to verify the changes were applied correctly.

## The Harness Example
*   In the harness, the Python agent processes input in prose first before converting it into structured data, which is then used as input by other agents.

## Performance Metrics

*   Node.js: Measures time taken for direct code execution.
*   Rust: Measures time taken for direct code execution.
*   Go: Measures time taken for direct code execution.