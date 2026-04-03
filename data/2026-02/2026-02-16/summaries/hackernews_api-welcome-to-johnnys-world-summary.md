---
title: "Welcome to Johnny's World"
url: https://marler8997.github.io/blog/fixed-windows/
date: 2026-02-15
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-16T06:02:45.672187
---

# Welcome to Johnny's World

# I Fixed Windows Native Development

This article discusses the challenges of managing dependencies for native development on Windows, specifically the complexities associated with Visual Studio. The author argues that the traditional approach of simply listing "Install Visual Studio" as a dependency is problematic, as it leads to a vast and often opaque installation process with numerous potential issues.

## Why is this tragedy unique to Windows?

Unlike Linux, where toolchains are typically managed by package managers, Visual Studio involves thousands of components distributed through a complex GUI installer. This makes it difficult to ensure consistent installations and manage different versions. Common problems include long download times, lack of transparency regarding installed files, version control issues, and a fragile development environment setup.

## A new way

The author introduces `msvcup`, an open-source command-line tool designed to address these issues. `msvcup` installs the necessary MSVC toolchain and Windows SDK into isolated, versioned directories, ensuring reproducible builds across different machines. It is idempotent and fast, capable of installing the entire toolchain, including cross-compilation support for ARM, in minutes.

## How?

`msvcup` leverages JSON manifests published by Microsoft to identify and download only the required components from their CDN. It avoids the need for manual environment setup by utilizing `msvcup autoenv` to create an automatic environment with necessary wrapper executables. This approach eliminates the reliance on the fragile `Developer Command Prompt` and ensures consistent toolchain versions for all developers and CI systems.

The author highlights the benefits of using `msvcup`, including:

* **Versioned installations:** Components are installed into isolated directories, allowing for easy side-by-side management and removal.
* **Cross-compilation:** Built-in support for cross-compiling to and from ARM architectures.
* **Lock file support:** A self-contained list of all downloaded packages ensures everyone uses the same versions.

The author and their team at Tuple have integrated `msvcup` into their build system and CI, eliminating the need for users and CI systems to pre-install Visual Studio. This has enabled them to build hundreds of C/C++ projects, including those targeting ARM, with consistent toolchains. The author concludes that `msvcup` represents a significant step towards treating native development dependencies like modern software dependencies – versioned, isolated, and declarative.
