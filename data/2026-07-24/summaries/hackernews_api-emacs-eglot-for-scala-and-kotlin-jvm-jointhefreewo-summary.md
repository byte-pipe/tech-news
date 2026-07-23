---
title: Emacs Eglot for Scala and Kotlin (JVM) - jointhefreeworld
url: https://jointhefreeworld.org/blog/articles/emacs/emacs-eglot-scala-kotlin/index.html
date: 2026-07-21
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-24T05:40:43.905082
---

# Emacs Eglot for Scala and Kotlin (JVM) - jointhefreeworld

# Summary of “Emacs Eglot for Scala and Kotlin (JVM) – jointhefreeworld”

## Motivation  
- Emacs 29 includes Eglot, a lightweight LSP client that follows the Emacs philosophy.  
- Traditional advice pushes IntelliJ IDEA for JVM languages, but IntelliJ is heavyweight, consumes large amounts of RAM, and locks users into a proprietary ecosystem.  
- Emacs offers three advantages:  
  * Unix‑style separation of concerns via LSP (Eglot handles transport, language servers do the heavy lifting).  
  * Unlimited hackability through Emacs Lisp (e.g., advising JSON‑RPC payloads).  
  * A unified editing interface across all file types.

## Hooks, Keybindings, and Initial Setup  
- Managed with `use-package` (no external download, `:ensure nil`).  
- `eglot-ensure` is hooked into almost every programming mode, including both classic and Tree‑sitter variants (e.g., `scala-ts-mode`, `kotlin-ts-mode`).  
- Auto‑formatting is enabled via `before-save` hook (`eglot-format-buffer`).  
- Keybindings are placed under the `C-c i` prefix for consistency:  
  * `C-c i i` – `eglot-find-implementation`  
  * `C-c i e` – `eglot` (menu)  
  * `C-c i k` – `eglot-shutdown-all`  
  * `C-c i r` – `eglot-rename`  
  * `C-c i x` – `eglot-reconnect`  
  * `C-c i a` – `eglot-code-actions`  
  * `C-c i m` – `eglot-menu`  
  * `C-c i f` – `eglot-format-buffer`  
  * `C-c i h` – `eglot-inlay-hints-mode`  
- Initial variables set:  
  * `eglot-autoshutdown t` – clean up server processes when no buffers remain.  
  * `eglot-extend-to-xref t` – allow cross‑reference navigation into external libraries.  
  * Other flags enable auto‑reconnect, progress reporting, and longer connection timeouts.

## Fine‑Tuning Server Definitions  
- Default entries for Scala and Kotlin are removed to avoid collisions.  
- Scala (Metals) server is added with JVM options: `-Xmx4G`, `-XX:+UseZGC`, and HTTP enabled via `:initializationOptions`.  
- Kotlin server uses the IntelliJ‑backed `intellij-server --stdio`.  

## Global Workspace Configuration  
- `eglot-workspace-configuration` acts as a universal `settings.json`.  
- Highlights for Metals:  
  * Automatic import of all builds.  
  * HTTP enabled, super‑method lenses, inferred type display, semantic highlighting.  
  * Inlay hints tuned to show inferred types and type parameters, while disabling implicit conversions and arguments.  
  * JVM properties for Bloop (`-Xmx4G`).  
- Additional language settings include Haskell (`ormolu` formatter), TypeScript/JavaScript formatting rules, Rust‑Analyzer (clippy, cargo features, macro diagnostics), YAML schema validation, and Nix formatting (`nixfmt`).  

## Notable Outcomes  
- The configuration provides a production‑ready, fast, and memory‑efficient development environment for Scala and Kotlin without relying on IntelliJ.  
- By leveraging Emacs Lisp, bugs or missing features in language servers can be patched on the fly.  
- The unified interface lets the same completion, navigation, and formatting tools be used across diverse file types.  

## Conclusion  
- The setup is not claimed to be perfect, but it delivers a near‑perfect developer experience, high speed, and low resource usage.  
- Emacs + Eglot demonstrates that JVM language development can be done efficiently in a fully open‑source, hackable environment.