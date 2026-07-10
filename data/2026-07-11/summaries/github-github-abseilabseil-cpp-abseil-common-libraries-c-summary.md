---
title: GitHub - abseil/abseil-cpp: Abseil Common Libraries (C++) · GitHub
url: https://github.com/abseil/abseil-cpp
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:38:35.362582
---

# GitHub - abseil/abseil-cpp: Abseil Common Libraries (C++) · GitHub

# Abseil – C++ Common Libraries

## About Abseil
- Open‑source collection of C++17‑compatible code that augments the C++ standard library.  
- Originates from Google’s internal code base, extensively tested and used in production.  
- Provides missing pieces or alternatives to the standard library, clearly marked in the code.  
- Not a competitor to the standard library; aims to share useful utilities with the broader C++ community.

## Quickstart
- Guides users through setting up the development environment, downloading the code, running tests, and building a simple binary.  
- Recommended first step for new users.

## Building Abseil
- Official build systems: **Bazel** and **CMake**.  
- Quickstart documentation includes detailed instructions for both build tools.  
- CMake support is available via separate CMake build instructions and a CMake Quickstart guide.

## Support
- Follows Google’s Foundational C++ Support Policy.  
- A compatibility table lists supported compiler versions, platforms, and build tools.

## Codemap (Library Components)
- **base** – Core utilities and initialization code; depends only on the C++ standard library.  
- **algorithm** – Extensions to `<algorithm>` and container‑based algorithm variants.  
- **cleanup** – `absl::Cleanup` for executing callbacks on scope exit.  
- **container** – Additional STL‑style containers, including unordered “Swiss table” containers.  
- **crc** – Functions for computing cyclic redundancy checks.  
- **debugging** – Leak checks, stacktrace, and symbolization utilities.  
- **flags** – Command‑line flag handling for binaries and libraries.  
- **hash** – Hashing framework and default hash functors.  
- **log** – `LOG`/`CHECK` macros and logging facilities.  
- **memory** – Memory‑management helpers augmenting `<memory>`.  
- **meta** – Type‑trait utilities similar to `<type_traits>`.  
- **numeric** – 128‑bit integer types and C++20 bitwise math functions.  
- **profiling** – Profiling utilities (private dependency of other libraries).  
- **random** – Pseudorandom value generation functions.  
- **status** – Error‑handling abstractions (`absl::Status`, `absl::StatusOr<T>`).  
- **strings** – Comprehensive string manipulation utilities.  
- **synchronization** – Concurrency primitives (`absl::Mutex`) and synchronization abstractions.  
- **time** – Time‑point, duration, formatting, and time‑zone handling utilities.  
- **types** – Non‑container utility types.  
- **utility** – General helper code.

## Releases
- Recommended “live‑at‑head” usage: regularly update to the latest `master` commit.  
- Long‑Term Support (LTS) releases are also provided, with back‑ported fixes for severe bugs.  
- Detailed release‑management policy is documented in the repository.

## License
- Distributed under the Apache License 2.0 (see `LICENSE` file for details).

## Links & Further Reading
- **Abseil Introduction** – Overview of the project.  
- **Why Adopt Abseil** – Design philosophy and motivations.  
- **Abseil Compatibility Guarantees** – Expectations for users and contributors.  

## Repository Statistics
- Stars: 17.5 k  
- Watchers: 676  
- Forks: 3.2 k  
- Primary languages: C++ (≈92 %), Starlark, CMake, others.