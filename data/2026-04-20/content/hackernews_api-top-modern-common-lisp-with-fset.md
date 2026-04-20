---
title: Top (Modern Common Lisp with FSet)
url: https://fset.common-lisp.dev/Modern-CL/Top_html/index.html
site_name: hackernews_api
content_file: hackernews_api-top-modern-common-lisp-with-fset
fetched_at: '2026-04-20T06:00:16.159001'
original_url: https://fset.common-lisp.dev/Modern-CL/Top_html/index.html
author: larve
date: '2026-04-16'
description: Top (Modern Common Lisp with FSet)
tags:
- hackernews
- trending
---

Next:Introduction and Obligatory Hype[Contents][Index]

# Modern Common Lisp with FSet¶

Version 1.0 (for FSet v2.4.2)

© 2026 Scott L. Burson

This document is published under the Creative CommonsCC BY-NC-SA 4.0license. This license
enables reusers to distribute, remix, adapt, and build upon the material in any medium or format for
noncommercial purposes only, and only so long as attribution is given to the creator. If you remix,
adapt, or build upon the material, you must license the modified material under identical terms.

This document contains no LLM-generated text — zero, zip, nada. (Yes, I do use em-dashes and
semicolons; yes, I have written every one myself.)

For errors noticed or other suggestions, please file issues onCommon-Lisp.Net’s GitLab instanceorGitHub.

## Table of Contents

* Introduction and Obligatory HypeWhy I Wrote FSetBenefits of Functional Collections
* Why I Wrote FSet
* Benefits of Functional Collections
* 1 Getting Started1.1 FSet Tutorial1.1.1 The Major FSet Types1.1.1.1 Sets Tutorial1.1.1.2 Maps Tutorial1.1.1.3 Seqs Tutorial1.1.1.4 Bags Tutorial1.1.2 Nested collections1.1.3 Assignment and updating1.2 Using FSet1.2.1 Importing FSet Symbols1.2.2 Misc-Extensions1.3 Emacs Customizations
* 1.1 FSet Tutorial1.1.1 The Major FSet Types1.1.1.1 Sets Tutorial1.1.1.2 Maps Tutorial1.1.1.3 Seqs Tutorial1.1.1.4 Bags Tutorial1.1.2 Nested collections1.1.3 Assignment and updating
* 1.1.1 The Major FSet Types1.1.1.1 Sets Tutorial1.1.1.2 Maps Tutorial1.1.1.3 Seqs Tutorial1.1.1.4 Bags Tutorial
* 1.1.1.1 Sets Tutorial
* 1.1.1.2 Maps Tutorial
* 1.1.1.3 Seqs Tutorial
* 1.1.1.4 Bags Tutorial
* 1.1.2 Nested collections
* 1.1.3 Assignment and updating
* 1.2 Using FSet1.2.1 Importing FSet Symbols1.2.2 Misc-Extensions
* 1.2.1 Importing FSet Symbols
* 1.2.2 Misc-Extensions
* 1.3 Emacs Customizations
* 2 Examples2.1 Histogram Construction2.2 Graph Walking2.3 Case Study: CL-Cont
* 2.1 Histogram Construction
* 2.2 Graph Walking
* 2.3 Case Study: CL-Cont
* 3 Conceptual Background3.1 What Is a Functional Datatype?3.2 Is Lisp a Functional Language?3.3 A Brief Introduction to Big-O3.4 The Common Lisp Object System
* 3.1 What Is a Functional Datatype?
* 3.2 Is Lisp a Functional Language?
* 3.3 A Brief Introduction to Big-O
* 3.4 The Common Lisp Object System
* 4 The Design of FSet4.1 Divergences from Common Lisp4.2 Comparison and Equality4.2.1 Abstract and Concrete Equality4.3 Seqs and Strings4.4 The@Macro4.5 Quasi-Mutating Operators4.6 Map and Seq Defaults
* 4.1 Divergences from Common Lisp
* 4.2 Comparison and Equality4.2.1 Abstract and Concrete Equality
* 4.2.1 Abstract and Concrete Equality
* 4.3 Seqs and Strings
* 4.4 The@Macro
* 4.5 Quasi-Mutating Operators
* 4.6 Map and Seq Defaults
* 5 FSet Data Structures5.1 Weight-Balanced Trees5.2 CHAMP Trees5.2.1 A Note on HAMT and Time Complexity5.3 Comparison and Hash Functions5.3.1 Which Elements are Compared or Hashed5.4 Generic Functioncompare5.4.1 Cross-Type Comparisons5.5 Generic Functionhash-value5.6 User-Defined Classes5.6.1 Value Types5.6.2 Reference Types5.6.3 Left Preference5.7 Custom Comparison and Hash Functions5.7.1 Strict Weak Orderings5.7.2 Non-FSet Collections5.8 Choosing a Data Structure5.9 Transients5.10 Dynamic Tuples
* 5.1 Weight-Balanced Trees
* 5.2 CHAMP Trees5.2.1 A Note on HAMT and Time Complexity
* 5.2.1 A Note on HAMT and Time Complexity
* 5.3 Comparison and Hash Functions5.3.1 Which Elements are Compared or Hashed
* 5.3.1 Which Elements are Compared or Hashed
* 5.4 Generic Functioncompare5.4.1 Cross-Type Comparisons
* 5.4.1 Cross-Type Comparisons
* 5.5 Generic Functionhash-value
* 5.6 User-Defined Classes5.6.1 Value Types5.6.2 Reference Types5.6.3 Left Preference
* 5.6.1 Value Types
* 5.6.2 Reference Types
* 5.6.3 Left Preference
* 5.7 Custom Comparison and Hash Functions5.7.1 Strict Weak Orderings5.7.2 Non-FSet Collections
* 5.7.1 Strict Weak Orderings
* 5.7.2 Non-FSet Collections
* 5.8 Choosing a Data Structure
* 5.9 Transients
* 5.10 Dynamic Tuples
* 6 FSet API Reference6.1 Notes on Time Complexity6.2 Sets6.2.1 Set Operations6.2.2 CH-Set Operations6.2.3 Transient-CH-Set Operations6.2.4 WB-Set Operations6.2.5 Complement Sets6.3 Maps6.3.1 Map Operations6.3.2 CH-Map Operations6.3.3 Transient-CH-Map Operations6.3.4 WB-Map Operations6.4 Bags6.4.1 Bag Operations6.4.2 CH-Bag Operations6.4.3 Transient-CH-Bag Operations6.4.4 WB-Bag Operations6.5 Seqs6.5.1 Seq Operations6.6 Replay Sets and Maps6.6.1 Replay Sets6.6.1.1 Replay-Set Operations6.6.1.2 CH-Replay-Set Operations6.6.1.3 Transient-CH-Replay-Set Operations6.6.2 Replay Maps6.6.2.1 Replay-Map Operations6.6.2.2 CH-Replay-Map Operations6.6.2.3 Transient-CH-Replay-Map Operations6.7 Binary Relations6.7.1 2-Relation Operations6.7.2 CH-2-Relation Operations6.7.2.1 Transient-CH-2-Relation Operations6.7.3 WB-2-Relation Operations6.8 Tuples6.9 Miscellaneous Functions6.10 Operations on CL Types6.11 Error Types6.12 The Bleeding Edge6.12.1 List Relations and Query Registries6.12.2 Interval Sets6.12.3 Bounded Sets
* 6.1 Notes on Time Complexity
* 6.2 Sets6.2.1 Set Operations6.2.2 CH-Set Operations6.2.3 Transient-CH-Set Operations6.2.4 WB-Set Operations6.2.5 Complement Sets
* 6.2.1 Set Operations
* 6.2.2 CH-Set Operations
* 6.2.3 Transient-CH-Set Operations
* 6.2.4 WB-Set Operations
* 6.2.5 Complement Sets
* 6.3 Maps6.3.1 Map Operations6.3.2 CH-Map Operations6.3.3 Transient-CH-Map Operations6.3.4 WB-Map Operations
* 6.3.1 Map Operations
* 6.3.2 CH-Map Operations
* 6.3.3 Transient-CH-Map Operations
* 6.3.4 WB-Map Operations
* 6.4 Bags6.4.1 Bag Operations6.4.2 CH-Bag Operations6.4.3 Transient-CH-Bag Operations6.4.4 WB-Bag Operations
* 6.4.1 Bag Operations
* 6.4.2 CH-Bag Operations
* 6.4.3 Transient-CH-Bag Operations
* 6.4.4 WB-Bag Operations
* 6.5 Seqs6.5.1 Seq Operations
* 6.5.1 Seq Operations
* 6.6 Replay Sets and Maps6.6.1 Replay Sets6.6.1.1 Replay-Set Operations6.6.1.2 CH-Replay-Set Operations6.6.1.3 Transient-CH-Replay-Set Operations6.6.2 Replay Maps6.6.2.1 Replay-Map Operations6.6.2.2 CH-Replay-Map Operations6.6.2.3 Transient-CH-Replay-Map Operations
* 6.6.1 Replay Sets6.6.1.1 Replay-Set Operations6.6.1.2 CH-Replay-Set Operations6.6.1.3 Transient-CH-Replay-Set Operations
* 6.6.1.1 Replay-Set Operations
* 6.6.1.2 CH-Replay-Set Operations
* 6.6.1.3 Transient-CH-Replay-Set Operations
* 6.6.2 Replay Maps6.6.2.1 Replay-Map Operations6.6.2.2 CH-Replay-Map Operations6.6.2.3 Transient-CH-Replay-Map Operations
* 6.6.2.1 Replay-Map Operations
* 6.6.2.2 CH-Replay-Map Operations
* 6.6.2.3 Transient-CH-Replay-Map Operations
* 6.7 Binary Relations6.7.1 2-Relation Operations6.7.2 CH-2-Relation Operations6.7.2.1 Transient-CH-2-Relation Operations6.7.3 WB-2-Relation Operations
* 6.7.1 2-Relation Operations
* 6.7.2 CH-2-Relation Operations6.7.2.1 Transient-CH-2-Relation Operations
* 6.7.2.1 Transient-CH-2-Relation Operations
* 6.7.3 WB-2-Relation Operations
* 6.8 Tuples
* 6.9 Miscellaneous Functions
* 6.10 Operations on CL Types
* 6.11 Error Types
* 6.12 The Bleeding Edge6.12.1 List Relations and Query Registries6.12.2 Interval Sets6.12.3 Bounded Sets
* 6.12.1 List Relations and Query Registries
* 6.12.2 Interval Sets
* 6.12.3 Bounded Sets
* 7 Iterating over FSet Collections7.1 Procedural Iteration Macros7.2 Stateful Iterators7.3 Functional Iterators7.4 Theat-indexOperation7.5 GMap7.5.1 GMap Base Argument Types7.5.2 GMap Base Result Types7.5.3 GMap FSet Argument Types7.5.4 GMap FSet Result Types7.6 Iterate
* 7.1 Procedural Iteration Macros
* 7.2 Stateful Iterators
* 7.3 Functional Iterators
* 7.4 Theat-indexOperation
* 7.5 GMap7.5.1 GMap Base Argument Types7.5.2 GMap Base Result Types7.5.3 GMap FSet Argument Types7.5.4 GMap FSet Result Types
* 7.5.1 GMap Base Argument Types
* 7.5.2 GMap Base Result Types
* 7.5.3 GMap FSet Argument Types
* 7.5.4 GMap FSet Result Types
* 7.6 Iterate
* 8 Generic Functionconvert
* 9 Printing and Reading9.1 Reader Macros9.2 JSON Printing and Parsing9.2.1 JSON Parsing9.2.2 JSON Printing9.3 Compiler Externalization
* 9.1 Reader Macros
* 9.2 JSON Printing and Parsing9.2.1 JSON Parsing9.2.2 JSON Printing
* 9.2.1 JSON Parsing
* 9.2.2 JSON Printing
* 9.3 Compiler Externalization
* 10 Recommendations for Language Designers10.1 Features of FSet10.2 Critiques of FSet10.3 History of Functional Collections10.4 Critiques of Other Libraries10.4.1 Clojure10.4.2 Scheme (R6RS)10.4.3 Racket10.4.4 Haskell10.4.5 Scala10.4.6 Google Guava10.4.7 Python
* 10.1 Features of FSet
* 10.2 Critiques of FSet
* 10.3 History of Functional Collections
* 10.4 Critiques of Other Libraries10.4.1 Clojure10.4.2 Scheme (R6RS)10.4.3 Racket10.4.4 Haskell10.4.5 Scala10.4.6 Google Guava10.4.7 Python
* 10.4.1 Clojure
* 10.4.2 Scheme (R6RS)
* 10.4.3 Racket
* 10.4.4 Haskell
* 10.4.5 Scala
* 10.4.6 Google Guava
* 10.4.7 Python
* Afterword
* Index

Next:Introduction and Obligatory Hype[Contents][Index]