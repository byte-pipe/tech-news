---
title: jank programming language - Clojure/LLVM/C++
url: https://jank-lang.org/
site_name: hackernews_api
fetched_at: '2025-07-11T01:05:12.185004'
original_url: https://jank-lang.org/
author: akkad33
date: '2025-07-07'
description: The jank programming language
tags:
- hackernews
- trending
---

jank is ageneral-purpose programming languagewhich embraces theinteractive, value-orientednature of Clojure as well as the desire fornative compilation and minimal runtimes. jank isstrongly compatible with Clojureand considers itself a dialect of Clojure. Please note that jank is under heavy development; assume all features are planned or incomplete.Where jank differs from Clojure JVM is that its host is C++ on top of anLLVM-based JIT. This allows jank to offer the same benefits ofREPL-based developmentwhile being able toseamlessly reach into the native worldand compete seriously with JVM's performance.Still, jank is a Clojure dialect and thus includes itscode-as-data philosophy and powerful macro system. jank remains a functional-first language which builds upon Clojure's rich set ofpersistent, immutable data structures. When mutability is needed, jank offers a software transaction memory and reactive agent system to ensureclean and correct multi-threaded designs.Current progressGithubSponsor
