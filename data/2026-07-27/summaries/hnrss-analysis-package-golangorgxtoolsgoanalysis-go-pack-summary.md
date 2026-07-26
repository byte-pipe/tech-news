---
title: analysis package - golang.org/x/tools/go/analysis - Go Packages
url: https://pkg.go.dev/golang.org/x/tools/go/analysis
date: 2026-07-26
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-27T06:53:30.893751
---

# analysis package - golang.org/x/tools/go/analysis - Go Packages

# analysis package - golang.org/x/tools/go/analysis

## Background
- A static analysis inspects a Go package and reports diagnostics or other results (e.g., refactorings, facts).  
- “Checker” is an informal term for an analysis that reports mistakes, such as the `printf` checker.  
- A **modular** analysis works one package at a time but can store facts from lower‑level packages and reuse them in higher‑level packages, similar to separate compilation.  
- By sharing a common interface, analyzers can be plugged into many driver programs: command‑line tools (`vet`), IDEs, build systems, test frameworks, code review tools, indexers, documentation viewers, and large‑scale batch pipelines.

## Analyzer
- The core type is `Analyzer`, which statically describes an analysis: name, documentation, flags, dependencies, result type, and the analysis function itself.  
- Typical declaration:

  ```go
  var Analyzer = &analysis.Analyzer{
      Name: "unusedresult",
      Doc:  "check for unused results of calls to some functions",
      Run:  run,
      // other fields...
  }
  ```

- Drivers import the required analyzers and list them, e.g.:

  ```go
  var analyses = []*analysis.Analyzer{
      unusedresult.Analyzer,
      nilness.Analyzer,
      printf.Analyzer,
  }
  ```

- Important fields of `Analyzer`:
  - `Name`, `Doc`: used for help messages.  
  - `Flags`: a `flag.FlagSet` defining analyzer‑specific options; drivers decide how to expose them.  
  - `RunDespiteErrors`: if true, the analyzer runs even when the package has parse or type errors.  
  - `ResultType`: the concrete type of the value returned by `Run`, made available to dependent analyzers.  
  - `Requires`: list of other analyzers whose results are needed; determines execution order.  
  - `FactTypes`: types of facts that can be stored and retrieved across package boundaries.  
  - `Validate`: checks basic sanity (acyclic `Requires` graph, unique result/fact types, etc.).  
  - `Run`: function called with a `*Pass` to perform the analysis on a single package.

## Pass
- A `Pass` represents applying a specific `Analyzer` to a particular Go package.  
- Key fields:
  - `Fset`, `Files`, `Pkg`, `TypesInfo`: provide syntax trees, type information, and source positions.  
  - `OtherFiles`: names of non‑Go files (e.g., assembly) belonging to the package.  
  - `IgnoredFiles`: files excluded by the current build configuration but possibly included in others.  
  - `ResultOf`: map from required analyzers to their computed results, respecting the `Requires` list.  
  - `Report`: function to emit a `Diagnostic`. A helper `Reportf` formats messages conveniently.  
- `Diagnostic` structure:

  ```go
  type Diagnostic struct {
      Pos      token.Pos
      Category string // optional short identifier
      Message  string
  }
  ```

  - No severity field; drivers are expected to let users filter or prioritize diagnostics based on analyzer name and optional category.  
- Utilities:
  - `Pass.ReadFile` can read the contents of non‑Go files; the file can then be added to the `FileSet` to obtain positions for diagnostics.  

These components together enable modular, reusable static analyses that can be orchestrated by a wide range of driver programs.