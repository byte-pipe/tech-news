---
title: Notes by djb on using Fil-C
url: https://cr.yp.to/2025/fil-c.html
date: 2025-11-02
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-11-03T11:36:24.728067
screenshot: hackernews_api-notes-by-djb-on-using-fil-c.png
---

# Notes by djb on using Fil-C

# Notes by djb on using Fil-C (2025)

### Main Points

* Fil-C is a memory-safe C/C++ compiler compatible with many libraries and applications.
* It has been successfully tested without changes with various projects, including some non-free packages like bzip2.
* This article provides notes for users who want to use Fil-C on their systems.

### Key Highlights

* Fil-C works as intended out of the box without requiring any configuration or tweaking.
* Timings from a mini-PC system (6-core Ryzen 5) show significant performance gains over corresponding Clang-based systems.
* Fil-C is recommended for projects that require security and compatibility with outdated software tools.

### Related References

* Posting an asynchronous script (`ascript`) to demonstrate differences between Fil-C and upstream sources (Clang, glibc).
* A self-contained compilation script (`filian-install-compilerscript`) for Debian 13 to install Fil-C and relevant packages.
* Testing various Debian source package installations using `afilian-install-packagesscript`.
* Running Fil-C on a mini-PC system with optimized performance.

### Performance Comparison

* Time taken for Fil-C to compile code compared to Clang is between 1x (microbenchmarks) and 4x (cycles).
* File comparisons demonstrate significant performance gains over using Clang.
* A running example from Fil-C compiled Nethack shows it can run similar-to-the-unmodified-clang versions under a specific environment.

### Getting Started with Fil-C

* A link to download the `filian-install-compilerscript` script, requiring an account for installation.
* Briefly explaining steps to set up and configure Fil-C on Debian 13:
    * Creating necessary directories (e.g., `/var/empty`)
    * Installing required packages (`autoconf-dickey`, etc.).
* A description of the recommended setup environment (`mkdir -p /var/empty`) before installing packages.

### System Requirements

* Recommended setup for a Linux system under Debian 13:
    * 6-core Ryzen 5 CPU
    * 12GB RAM
    * 36GB swap
    * Latest version of Fil-C installed with Clang and other required libraries.
