---
title: GitHub - FareedKhan-dev/kimi-k3-in-c: A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no...
url: https://github.com/FareedKhan-dev/kimi-k3-in-c
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-05T15:24:56.005275
---

# GitHub - FareedKhan-dev/kimi-k3-in-c: A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no...

# GitHub - FareedKhan-dev/kimi-k3-in-c

## Overview
- Portable C99 implementation of the 2.78‑trillion‑parameter Kimi K3 model.  
- Enables inference on a single CPU using only 8.24 GB of RAM.  
- No external BLAS libraries, GPU drivers, or deep‑learning frameworks required.  

## Key Features
- Pure C99 codebase with optional Python bindings.  
- Minimal memory footprint suitable for edge devices.  
- Benchmarks and example scripts included for quick testing.  
- Comprehensive documentation and contribution guidelines.  

## Directory Structure
- **.github/** – GitHub workflows and issue templates.  
- **benchmarks/** – Performance measurement scripts and results.  
- **cmake/** – CMake modules for building the project.  
- **docs/** – Detailed usage instructions and API reference.  
- **examples/** – Sample programs demonstrating model loading and inference.  
- **include/k3/** – Public header files exposing the library interface.  
- **scripts/** – Helper scripts for model conversion and preprocessing.  
- **src/** – Core implementation of the K3 inference engine.  
- **tests/** – Unit and integration tests to verify correctness.  
- **third_party/** – External dependencies bundled for convenience.  
- **tools/** – Utilities for model inspection and debugging.  
- Configuration files: `.clang-format`, `.editorconfig`, `.gitattributes`, `.gitignore`.  
- Project metadata: `CHANGELOG.md`, `CONTRIBUTING.md`, `CONTRIBUTORS.md`, `LICENSE`, `NOTICE`, `README.md`, `SECURITY.md`.  
- Build system: `CMakeLists.txt`, `Makefile`.  
- Python packaging: `pyproject.toml`, `ruff.toml`.  

## Build & Usage
- Build with CMake: `cmake -S . -B build && cmake --build build`.  
- Optional Python package can be installed via `pip install .` after building.  
- Run examples from the `examples/` directory to perform inference on sample inputs.  

## Documentation
- The `README.md` provides a quick start guide, hardware requirements, and performance numbers.  
- Detailed API reference and usage patterns are located in the `docs/` folder.  

## License & Contributions
- Distributed under the terms specified in the `LICENSE` file.  
- Contributions are welcomed; see `CONTRIBUTING.md` for guidelines and `CODE_OF_CONDUCT` policies.