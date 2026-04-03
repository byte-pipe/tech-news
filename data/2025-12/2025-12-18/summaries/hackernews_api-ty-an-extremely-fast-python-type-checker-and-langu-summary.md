---
title: ty: An extremely fast Python type checker and language server
url: https://astral.sh/blog/ty
date: 2025-12-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-18T11:22:33.725888
screenshot: hackernews_api-ty-an-extremely-fast-python-type-checker-and-langu.png
---

# ty: An extremely fast Python type checker and language server

**ty: An Extremely Fast Python Type Checker and Language Server**

### Overview

The article announces the Beta release of ty, an extremely fast Python type checker and language server written in Rust. It provides details on how ty was designed to power a language server, using "incrementality" to selectively re-run computations.

### Key Points

1. **Design Philosophy**: Ty is powered by "incrementality", allowing it to selectively run only necessary computations when editings a file or modifying an individual function.
2. **Performance**: Consistently faster than mypy and Pyright, with a gap of 80x-500x in execution time when running in an editor.
3. **Features**:
	* First-class intersection types
	* Advanced type narrowing
	* Sophisticated reachability analysis
4. **Implementation**: Built-in Rust code with active contributors under the MIT license, allowing it to be run anywhere that Python is written.
5. **Comparison**: Outperforms tools like Pyrefly in incremental updates on large projects.

### Conclusion

ty promises to provide a faster and more accurate type checking experience for developers building high-performance applications using the Python ecosystem. With its focus on performance, correctness, and user experience, ty could become an attractive alternative to existing tools like mypy and Pyright.
