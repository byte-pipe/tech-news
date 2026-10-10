---
title: CPython eyes UTF-8 as default internal string storage · freenode
url: https://freenode.net/article/cpython-eyes-utf-8-as-default-internal-string-storage
site_name: tldr
content_file: tldr-cpython-eyes-utf-8-as-default-internal-string-stor
fetched_at: '2026-10-10T16:08:00.816666'
original_url: https://freenode.net/article/cpython-eyes-utf-8-as-default-internal-string-storage
date: '2026-10-10'
published_date: '2026-10-10T13:35:21.877538+00:00'
description: Inada Naoki’s pre-PEP and reference build aim to ease Stable ABI use and C/Rust interop, while maintainers flag risks for existing C extensions.
tags:
- tldr
---

Languages & Toolchains
By rvalue
October 10, 2026

# CPython eyes UTF-8 as default internal string storage

Inada Naoki’s pre-PEP and reference build aim to ease Stable ABI use and C/Rust interop, while maintainers flag risks for existing C extensions.

L

Inada Naoki has floated a pre-PEP to make UTF-8CPython’s primary internal representation for Unicode strings, backed by a working reference implementation. The goal is to shrink the gap between Python’s Flexible String Representation (thePEP 393design that is an implementation detail, not Stable ABI) and the UTF-8 world that C, C++, andRustlibraries already expect.

Today many extension modules reach for the fastest fixed-width APIs for speed. That habit locks them out of the Stable ABI. Storing UTF-8 natively would remove the cost of building a UTF-8 cache and make hand-rolled bridges to native code less painful. Large strings that mix mostly ASCII with a few wide characters could also shrink in memory. Lengths would still be counted in code points; surrogates would follow the surrogatepass convention.

Victor Stinner called the change “scary for C extensions.” APIs such as PyUnicode_DATA() have never failed; under the proposal they can return null on allocation failure, and unprepared modules would crash. Petr Viktorin suggested making the old entry points abort fatally on OOM while new fallible versions are introduced and the old ones deprecated. Naoki adopted that approach in the proof of concept. Random indexing would initially still materialize a fixed-width cache so str[i] stays O(1); a PyPy-style position table is left for a later stage when the cache can be retired.

A survey of the top 4,000 bulk of PyPI packages showed heavy use of the fixed-width path, much of it via Cython. Cython maintainer da-woods said the necessary generator changes look manageable. Ronald Oussoren said PyObjC would track layout changes but would prefer a longer-term API that stops requiring direct poking at string internals.

Naoki plans a public UTF-8 accessor that tolerates surrogates and an allocation-free iterator for callers that cannot consume raw UTF-8. Whether the fixed-width form stays as a lazy alternative, how hashing interacts with bytes keys, and the exact deprecation timeline remain open questions before a formal PEP is written. PyPy already runs with UTF-8 internally, which the author cites as evidence that catastrophic slowdowns are unlikely, though some workloads will gain and others will lose.

#python
#cpython
#unicode
#utf-8
#stable-abi
#c-api