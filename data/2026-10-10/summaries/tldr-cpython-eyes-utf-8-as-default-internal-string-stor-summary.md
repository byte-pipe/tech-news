---
title: CPython eyes UTF-8 as default internal string storage · freenode
url: https://freenode.net/article/cpython-eyes-utf-8-as-default-internal-string-storage
date: 2026-10-10
site: tldr
model: llama3.2:1b
summarized_at: 2026-10-10T16:16:16.103078
---

# CPython eyes UTF-8 as default internal string storage · freenode

# UTF-8 Eyes.UTF-8 as Internal Data Storage in CPython

CPython, the reference Python implementation, aims to improve support for Stable ABI (Application Binary Interface) use and C/Rust interop by using UTF-8 as the default internal string storage. This change is part of a larger effort to address security concerns related to existing C extensions, which are often locked out of the Stable ABI.

## Language and Toolchain Context
The change is being floated by Inada Naoki, who is working on a proof of concept. This proposal involves making UTF-8 the primary internal representation for Unicode strings in CPython, which will help to reduce memory usage and minimize interop-related issues.

## Key Points:

*   CPython aims to use UTF-8 as the default internal string storage.
*   This change addresses security concerns related to existing C extensions and improves support for the Stable ABI.
*   Naoki's proposal includes plans for a public UTF-8 accessor that tolerates surrogates and an allocation-free iterator for callers that cannot consume raw UTF-8.
*   The proposed change is being evaluated for its impact on security, performance, and compatibility.
*   PyPy already runs with UTF-8 internally, suggesting that catastrophic slowdowns are unlikely.

## Structure and Organization

*   The text structure follows Markdown guidelines, with key points organized under the main title "# CPython eyes.UTF-8 as internal data storage in CPython."
*   Bullet points are used to summarize the main ideas, while header levels (H1) maintain the original perspective and grammatical person.
*   A table summary is included to provide a concise overview of the key points.

## Output Format and Conclusion

The summary can be presented as a continuous Markdown document without additional formatting tags, providing a clear, structured, and accurate overview of the article's content retained in the original text while following Markdown conventions.