---
title: sstephenson/brat: Brutal Runner for Automated Tests, a parallel TAP testing harness for the POSIX shell - Codeberg.org
url: https://codeberg.org/sstephenson/brat
date: 2026-02-22
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-22T06:01:10.582787
---

# sstephenson/brat: Brutal Runner for Automated Tests, a parallel TAP testing harness for the POSIX shell - Codeberg.org

# Brat: Brutal Runner for Automated Tests

Brat is a parallel TAP testing harness designed for the POSIX shell. It's built with shell and awk, aiming for zero dependencies and portability across various Unix-like operating systems. Brat is intended to be easily embedded within projects, requiring no build step or configuration.

## Key Features and Concepts
* **POSIX Focus:** Targets the POSIX.1-2024 standard, ensuring broad compatibility.
* **Minimalism:**  Small codebase (under 1000 lines) for easy understanding and embedding.
* **TAP Output:**  Generates test results in a standard TAP (Test Automation Protocol) format, with color highlighting for pass/fail status.
* **Parallel Execution:** Supports parallel test execution using the `BRAT_JOBS` environment variable.
* **Test Syntax:** Uses a specific shell syntax within `.brat` files to define tests. Each test case is a shell function where every line acts as an assertion.
* **Automatic Setup:**  Automatically sets environment variables like `$FILE`, `$DIR`, and `$TEST_TMP` for each test.
* **Output Capture:** Captures stdout and stderr of tests to separate files, providing paths for analysis.
* **Spiritual Successor to Bats:**  Inspired by Bats, offering similar functionality with a more minimalist approach.

## Installation
Brat can be installed globally via a tarball and symlinking the `brat` executable, or locally within a project by cloning the repository and linking the executable.

## Usage
Tests are written in `.brat` files.  The `brat` command executes these tests, displaying results in TAP format.  The `test` command is used to run tests within a directory.

## Parallel Execution
Use the `-j` option followed by the number of jobs to run tests in parallel.

## Portability
Brat is designed to be highly portable, running on a wide range of POSIX-compliant systems, including sh, awk, Alpine Linux, Debian, Fedora, FreeBSD, macOS, and more.

## Comparison with Bats
| Feature | Bats | Brat |
|---|---|---|
| Shell | Bash | Any POSIX shell |
| Parallel Execution | Requires GNU parallel | Built-in (FIFO) |
| Output Format | TAP or proprietary | TAP (always), pretty format is TAP with highlighting |
| Output Capture | $stdout, $stderr (in-memory strings) | $stdout, $stderr (file paths) |
| Built-in Helpers | Rich | Minimal |
| Lifecycle Hooks | Per-test and per-module | Per-test only |

## Documentation
The README file provides detailed information on installation, writing tests, running tests, implementation notes, contributing, and licensing.
