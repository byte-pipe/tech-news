---
title: GitHub - catchorg/Catch2: A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14, C++17 and later (C++11 support is in v2.x br...
url: https://github.com/catchorg/Catch2
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:38:48.826874
---

# GitHub - catchorg/Catch2: A modern, C++-native, test framework for unit-tests, TDD and BDD - using C++14, C++17 and later (C++11 support is in v2.x br...

# Catch2 – Modern C++ Test Framework

## Overview
- Catch2 is a unit‑testing framework for C++ that also offers micro‑benchmarking and simple BDD macros.  
- Designed for simplicity: test names can be any string, assertions read like normal C++ boolean expressions, and sections allow localized setup/teardown.  

## Key Features
- **Unit testing** with natural syntax (`TEST_CASE`, `REQUIRE`).  
- **Micro‑benchmarking** via `[!benchmark]` tag and `BENCHMARK` macro.  
- **BDD support** through dedicated macros.  
- No external dependencies; works with C++14, C++17 and later (C++11 in v2.x, C++03 in v1.x).  

## Example Usage
### Unit test
```cpp
#include <catch2/catch_test_macros.hpp>
#include <cstdint>

uint32_t factorial(uint32_t n) {
    return n <= 1 ? n : factorial(n-1) * n;
}

TEST_CASE("Factorials are computed", "[factorial]") {
    REQUIRE(factorial(1) == 1);
    REQUIRE(factorial(2) == 2);
    REQUIRE(factorial(3) == 6);
    REQUIRE(factorial(10) == 3'628'800);
}
```

### Micro‑benchmark
```cpp
#include <catch2/catch_test_macros.hpp>
#include <catch2/benchmark/catch_benchmark.hpp>
#include <cstdint>

uint64_t fibonacci(uint64_t n) {
    return n < 2 ? n : fibonacci(n-1) + fibonacci(n-2);
}

TEST_CASE("Benchmark Fibonacci", "[!benchmark]") {
    REQUIRE(fibonacci(5) == 5);
    REQUIRE(fibonacci(20) == 6'765);

    BENCHMARK("fibonacci 20") { return fibonacci(20); };

    REQUIRE(fibonacci(25) == 75'025);
    BENCHMARK("fibonacci 25") { return fibonacci(25); };
}
```
*Benchmarks run only when the `[!benchmark]` tag is specified.*

## Version 3 Highlights
- Transition from a single‑header library to a normal multi‑header library with separately compiled implementation.  
- Ongoing documentation updates to reflect the new structure.  
- Migration guide available in the docs; v2.x remains on a separate branch for legacy support.

## Documentation Structure
1. **Why another C++ test framework?** – rationale and design goals.  
2. **Tutorial – Getting started** – step‑by‑step guide for new users.  
3. **Reference** – detailed API description.

## Community & Support
- Issue tracker on GitHub for bugs and feature requests.  
- Discord server (`discord.gg/4CWS9zD`) for discussion and questions.  
- Widely used in both open‑source and commercial projects.

## Repository Statistics
- **Stars:** 20.6 k  
- **Watchers:** 500  
- **Forks:** 3.4 k  
- **Languages:** C++ 90.1 %, CMake 5.5 %, Python 3.3 %, others minor.  

## Licensing & Governance
- Distributed under the **Boost Software License 1.0 (BSL‑1.0)**.  
- Code of conduct, contribution guidelines, and security policy are provided in the repository.  

## Getting the Code
- Main development occurs on the `devel` branch (v3).  
- Stable v2 releases are available on the `v2.x` branch; v1.x (C++03) is on `Catch1.x`.  

---  
*Catch2 aims to make C++ testing straightforward, expressive, and portable across modern language standards.*