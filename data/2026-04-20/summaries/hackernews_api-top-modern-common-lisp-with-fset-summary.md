---
title: Top (Modern Common Lisp with FSet)
url: https://fset.common-lisp.dev/Modern-CL/Top_html/index.html
date: 2026-04-16
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-04-20T06:08:37.778023
---

# Top (Modern Common Lisp with FSet)

# Modern Common Lisp with FSet Documentation
=====================================

## Introduction and Obligatory Hype

This documentation is a comprehensive guide to the **FSet** library, a new framework for creating functional collections in modern Common Lisp.

## Table of Contents

* [Version 1.0] (not a bug, just an artifact of the format)
* [Introduction](#introduction)
* [Benefits of Functional Collections](#benefits-of-functionalCollections)
* [Getting Started](#getting-started)
* [Using FSet](#using-FSet)

## Introduction

**Modern Common Lisp with FSet** is a new library for creating functional collections in Modern Common Lisp. The library provides a set of tools and functions for building efficient, scalable data structures that are suitable for use in applications requiring fast data processing.

## Benefits of Functional Collections

Functional collections provide a range of benefits over traditional data structures, including:

* **Concise Code**: By using functional constructs, you can write more concise code that's easier to read and maintain.
* **Efficient Use of Memory**: Functional collections use a minimal amount of memory, making them ideal for applications where storage is limited.
* **Fast Data Processing**: The library provides optimized functions for processing data, ensuring fast performance in many cases.

## Getting Started

To use `FSet`, you'll need to:

1. Install the library: Run `pacme install fset` or download the source code and compile it yourself.
2. Import the symbol:
```lisp (import 'fset)
```
3. Create a collection object using one of the various types provided by FSet:
```lisp (make-set 1) : this will create an empty set.
```

## Using FSet

`FSet` offers a wide range of functions for creating, manipulating, and querying functional collections.

### Creating Collections

You can create various types of collections using `FSet`, including:

* **Sets**: A collection of unique elements (default).
* **Maps**: An associative array-like structure.
* **Seqs**: An ordered sequence of elements.
* **Bags**: A wrapper around a set or vector.
* **Assignment Operators**: allow updating values in the collection.

### Creating and Manipulating Collections

You can also use various functions to create new collections, manipulate existing ones, and update their contents.

```lisp
; Create an empty set
:example (make-set 1)

; Create a map
:example-map (mapcar #'< 1 2 3 4 5)

; Update the value of an element in a set
:example-update (set-eq 4 '5)
```

## Examples

### Histogram Construction

**Example 1:** Construct a histogram from data using `FSet`.

```lisp
(setf (hist-list "foo bar") :a)
```

### Graph Walking

**Example 2:** Walk the graph defined in the code using `FSet`.

```lisp
(setf (graph->list 'edge) :a b c)

; The resulting list will be:
:edge :edge a :edge b :edge c
```

### Case Study: CL-Cont

This is an example of how `.cont` methods can be used to manipulate collections.

```lisp

(create-list 1)
(setf (list->cont 'a) :a)
(mapcar #'> (list->cont 'b))
(seteql (graph->map #'> 'edge))
```

## Conceptual Background

* **Functional Datatype**: A functional concept is a data structure that supports the principles of immutable data. In FSet, sets are instances of this datatype.
* **Lisp**: This is a programming language known for its syntax and macro system.
* **Common Lisp Object System (CL-OS)**: The CL-OS provides an interface to low-level Lisp code facilities.

## The Design of FSet

FSet was designed with several key differences in mind:

* No external libraries or modules must be imported
* Functions can work directly on sets, maps and sequences, rather than needing additional types (e.g. lists)
* Optimizations for performance should always prioritize the collection's own memory usage
* `eq` is used to check if two collections are equal

## Theorems and Proofs

A set of formal proofs can be found in this documentation: [theorems.pdf](theorems.pdf)

The following code snippet demonstrates how you can write theorems related to `FSet`.