---
title: Modular: Mojo🔥 is now open source!
url: https://www.modular.com/blog/mojo-open-source
date: 2026-08-19
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-21T06:51:58.024048
---

# Modular: Mojo🔥 is now open source!

# Mojo🔥 is now open source!

## Announcement
- Modular announces that the Mojo language is fully open source under the Apache 2.0 license with LLVM exceptions.  
- The source code for the compiler, tooling, and related components is available in the modular GitHub repository.  
- Mojo 1.0, with source stability, was released last week; the compiler and toolchain are now open sourced.

## License
- Apache 2.0 is described as a “gold standard” for languages and compilers, offering broad flexibility for various applications.  
- LLVM extensions further permit building and distributing binaries compiled from Mojo.  
- The open‑source strategy balances a small design team with community feedback, having previously open‑sourced the standard library, kernel code, tools, and support.

## Getting and building the compiler
- Repository: `https://github.com/modular/modular.git`.  
- Build command (Bazel):
  ```bash
  ./bazelw run --config=build-mojo KGEN:mojo -- run hello.mojo
  ```
- To run the full test suite for the standard library:
  ```bash
  ./bazelw test --config=build-mojo mojo/stdlib/test/...
  ```
- For faster setup without rebuilding, use `--config=prebuilt-mojo` to download the latest nightly binary.  
- Prebuilt compiler is still required for customizing MAX kernels or models.

## Contributions
- The standard library has accepted contributions since 2024.  
- Contributions to the compiler and tooling are not yet open; they aim to open this by the end of the year.  
- Community can ask questions and share projects via Modular’s forum.

## Additional resources
- Links to related Modular blog posts (e.g., ModCon 2026, Qualcomm acquisition).  
- Calls to action: sign up for the cloud platform, browse open models, and subscribe to the newsletter.