---
title: Babashka 1.12.215: Revenge of the TUIs
url: https://blog.michielborkent.nl/babashka-1.12.215.html
date: 2026-02-19
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-19T06:04:03.910836
---

# Babashka 1.12.215: Revenge of the TUIs

# Babashka 1.12.215: Revenge of the TUIs

This release of BabaShka, a fast-starting native Clojure scripting runtime, introduces significant improvements, particularly in terminal user interface (TUI) support and developer experience.

## Key Highlights
### JLine3 and TUI Support
BabaShka now includes JLine3, a Java library for building interactive terminal applications. This enables features like terminals, line readers with history and tab completion, styled output, and keyboard bindings directly within bb scripts. A simple example demonstrates interactive prompt handling. The `babashka.termiinal` namespace provides a `tty?` function to detect terminal connections, allowing for conditional behavior based on the environment.
### charm.clj Compatibility
The addition of JLine3 and interpreter improvements makes BabaShka compatible with charm.clj, a new Clojure library for TUIs using the Elm architecture. This allows developers to build rich TUI applications that start instantly as native binaries. A complete example demonstrates the use of charm.clj with BabaShka.
### Deftype with Map Interfaces
Previously, Deftype in BabaShka lacked support for JVM interfaces like `IPersistentMap`. This release adds support for map interfaces, enabling libraries defining custom map-like types (common in Clojure) to function correctly. This unlocks compatibility with libraries like `core.cache` and `linked`.
### Riddley and Cloverage Compatibility
Riddley, a code walking library, now works with BabaShka due to changes aligning SCI's behavior with JVM Clojure. This includes improvements to `deftype`, `case`, and `macroexpand-1`. Cloverage compatibility has been submitted upstream and passes all tests on both JVM and BabaShka.
### Console REPL Improvements
The REPL experience has been significantly enhanced with JLine3 integration, offering multi-line editing, Clojure-aware tab completion, ghost text, Eldoc (automatic argument help), Doc-at-point, persistent history, and improved Ctrl+C handling.
### SCI Improvements
The underlying SCI interpreter has received several improvements, including functional interface adaptation, type tag inference, and bug fixes related to `readwithnil`, `letfn`, `ns-map`, `NPE`, and method class routing.
### Other Improvements
The release also includes support for Unicode characters in the REPL and various other minor enhancements.

## BabaShka Conf 2026
BabaShka Conf is happening again in Amsterdam, with the Call for Proposals open until the end of February. They are currently seeking a gold sponsor.
