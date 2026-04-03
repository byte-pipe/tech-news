---
title: How we reduced the size of our Agent Go binaries by up to 77% | Datadog
url: https://www.datadoghq.com/blog/engineering/agent-go-binaries/
date: 2026-02-26
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-26T06:01:45.845163
---

# How we reduced the size of our Agent Go binaries by up to 77% | Datadog

# How we reduced the size of our Agent Go binaries by up to 77% | DataDog

This article details DataDog's efforts to significantly reduce the size of their Go binaries, achieving reductions of up to 77% between versions 7.60.0 and 7.68.0 over approximately six months. This was crucial due to increasing artifact sizes impacting network costs, resource usage, and usability on resource-constrained platforms like serverless, IoT devices, and containerized workloads.

## Key Points:

* **Significant Size Reduction:** DataDog reduced the size of their Go binaries by up to 77% without sacrificing functionality.
* **Methodology:** The reduction was achieved through systematic dependency auditing, targeted refactors, and re-enabling powerful linker optimizations.
* **Complexity of DataDog Agent:** The DataDog Agent is composed of numerous builds tailored to different operating systems, architectures, and environments, relying on Go build tags and dependency injection.
* **Growing Artifact Size:** Over time, adding features and dependencies led to a substantial increase in artifact size, particularly in the Linux amd64 package.
* **Dependency Management:** The Go compiler selects dependencies based on build constraints, including operating system, architecture, and build tags.
* **Strategies for Reducing Dependencies:** Two main strategies were employed:
    * **Build Tags:** Using build tags (e.g., `//go:build unused`) to prevent unnecessary packages and their dependencies from being included.
    * **Code Isolation:** Moving code into separate packages to control which dependencies are pulled into a specific binary.
* **Tools for Analysis:** DataDog utilizes `go list` and `goda` to analyze Go binary sizes and import dependencies, providing insights into included packages and their relationships.
* **Linker Optimization:** The linker plays a crucial role in determining and removing unused symbols from packages, impacting the final binary size.

## How the DataDog Agent is built and delivered

The DataDog Agent is a complex software with numerous builds adapted for various platforms and environments. These builds are constructed from a common codebase using Go build tags and dependency injection to include specific features and dependencies. Over time, the addition of features and dependencies led to a significant increase in artifact size, impacting network costs, resource usage, and usability.

## Identifying and removing unnecessary dependencies

DataDog's approach to size reduction involved understanding how the Go compiler selects dependencies and utilizing build tags and code isolation to prevent unwanted packages from being included in the binaries. They leveraged tools like `go list` and `goda` to analyze dependencies and identify areas for optimization.

## Tools for analyzing Go binary size and imports

DataDog uses `go list` to list packages included in a binary based on build tags and environment variables. `goda` provides a more detailed analysis by generating dependency graphs, showing both direct and indirect imports and estimating package sizes. This helps in understanding the impact of different dependencies on the final binary size.
