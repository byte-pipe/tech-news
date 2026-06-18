---
title: GitHub - glojurelang/glojure: Clojure interpreter hosted on Go, with extensible interop support. · GitHub
url: https://github.com/glojurelang/glojure
date: 2026-06-17
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:18:57.394633
---

# GitHub - glojurelang/glojure: Clojure interpreter hosted on Go, with extensible interop support. · GitHub

# Glojure – Clojure Interpreter Hosted on Go

## Overview
- Glojure is an early‑stage interpreter for Clojure written in Go, allowing seamless use of Go libraries from Clojure code.  
- It is a “hosted” language: all Go values can be treated as Glojure values and vice‑versa.  
- Bugs, missing features, and limited performance are expected until a v1 release, but it already runs a substantial subset of the core Clojure library.

## Prerequisites
- Go version 1.19 or higher (runtime requires at least Go 1.24).

## Installation
```bash
go install github.com/glojurelang/glojure/cmd/glj@latest
```
- After installation, start the REPL with `glj`.

## Usage

### glj Command‑Line Tool
- Provides a traditional Clojure development experience.
- Common options:
  - `glj --help` – show help.
  - `glj --version` – display version (e.g., v0.3.0).
- REPL features:
  - Vi (default) and Emacs editing modes.
  - Multiline editing with auto‑indent.
  - Tab completion for symbols, namespaces, and aliases.
  - Smart indentation (2‑space tabs, full‑level backspace).
  - Persistent history saved to `~/.glj_history`.
  - Bracketed paste, job control (`Ctrl+Z` / `fg`), and interrupt (`Ctrl+C`).
- Evaluate expressions directly:
  ```bash
  glj -e '(println "Hello, World!")'
  ```
- Run a Clojure script file:
  ```bash
  glj hello.glj World
  ```
- Create executable programs by writing `.glj` scripts and invoking `glj script.glj`.

### Embedding Glojure in Go Applications
- Use Glojure as a scripting engine inside Go binaries.
- Typical use cases:
  - Scriptable configuration.
  - User‑extensible plugins written in Clojure.
  - Combining Go performance with Clojure expressiveness.
  - Custom I/O or sandboxed execution environments.
- Basic embedding pattern:
  ```go
  import (
      "fmt"
      _ "github.com/glojurelang/glojure/pkg/glj"
      "github.com/glojurelang/glojure/pkg/runtime"
  )

  func main() {
      result := runtime.ReadEval(`(defn factorial [n] (if (<= n 1) 1 (* n (factorial (dec n))))) (factorial 5)`)
      fmt.Printf("5! = %v\n", result) // prints 5! = 120
  }
  ```
- Exchanging functions between Go and Clojure:
  - Export a Go function to Clojure via `glj.Var(...).SetRoot`.
  - Invoke a Clojure function from Go using `glj.Var(...).Invoke`.

### Interoperability with Go Packages
- Standard library packages are pre‑included (e.g., `fmt`, `net/http`, `time`, etc.).
- Package names are munged to avoid symbol clashes (e.g., `net:http.MethodGet`).
- Additional packages can be exposed by generating a “package map” with `gen-import-interop` and compiling it into the executable.

## When to Use Which Approach
- **glj command** – for standalone Clojure programs, interactive REPL work, script execution, quick expression evaluation, or learning Clojure with Go interop.
- **Embedding** – for adding scripting to existing Go applications, building extensible platforms, controlling the runtime environment, or mixing Go and Clojure in a single binary.

## Extending the Standard Library
- Run the generator to create Go interop code for extra packages:
  ```bash
  go run github.com/glojurelang/glojure/cmd/gen-import-interop -packages=package1,package2
  ```
- Compile the generated code together with your application to make the new packages available in Glojure code.