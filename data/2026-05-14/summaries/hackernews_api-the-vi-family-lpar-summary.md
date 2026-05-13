---
title: The vi family | LPAR
url: https://lpar.ATH0.com/posts/2026/05/the-vi-family/
date: 2026-05-06
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-05-14T06:02:30.844781
---

# The vi family | LPAR

# The vi family | LPAR

## Overview
- Linux user polls show vi‑style editors are the most popular.
- The original **vi** editor, a terminal‑based tool from 1977, is valued for its efficiency once mastered and its ubiquitous key bindings, which are supported in many modern IDEs (VS Code, IntelliJ IDEA, Xcode).
- After the 2.0 release in 1979, vi was limited to commercial AT&T UNIX licenses, prompting the creation of numerous free clones for personal computers in the 1980s.
- The article compiles a personal list of vi clones and derivatives, noting release dates, key features, and current status. Contributions of additional editors are welcomed.

## Major vi clones and derivatives
- **Original ex/vi (1977‑2017?)** – Heirloom‑ex‑vi; UTF‑8 support added, but struggles with very large files.
- **STevie (1987‑1989)** – Atari ST/Amiga clone; ancestor of Vim; generally superseded by newer options.
- **Elvis (1990‑2024?)** – Early clone for MS‑DOS, Minix, etc.; introduced multiple buffers, windows, syntax coloring, and file‑buffer editing for large files.
- **xvi (1992‑2017?)** – Small STevie derivative with multiple windows and buffers.
- **Vile (1991‑ )** – Derived from MicroEmacs; adds infinite undo, UTF‑8, syntax highlighting, and extra modes.
- **Vim (1991‑ )** – Most widely used clone; built on STevie; supports windows, buffers, extensive scripting, UTF‑8, very large files, and LLM‑generated code.
- **nvi (1994‑ )** – Reimplementation based on Elvis, aiming for original vi behavior; adds Perl/Tcl scripting and a database backend; limited UTF‑8 support.
- **OpenBSD vi / OpenVi (1994‑ )** – Cleaned‑up nvi derivative; lacks UTF‑8, macros, scripting, and syntax highlighting.
- **BusyBox vi (2001‑ )** – Tiny, incomplete vi implementation found in Alpine Linux and embedded systems.
- **IllumOS vi (2005‑ )** – Open‑sourced AT&T UNIX vi from SVR4, part of OpenSolaris.
- **nvi2 (2011‑ )** – Extends nvi with UTF‑8 and CJK encodings.
- **Neovim (2014‑ )** – Modernized Vim; drops legacy platform support, adds LSP, built‑in terminal, Lua scripting, and LLM‑generated code.
- **EVi (2026‑ )** – Fork of Vim before LLM code integration.
- **Vim Classic (2026‑ )** – Fork of Vim 8.3 (pre‑LLM) aiming for long‑term human maintenance.
- **ToyBox vi (2027?)** – Planned tiny vi implementation within the ToyBox (non‑GPL BusyBox alternative) project.

## Editors with vi‑style concepts but not true vi clones
- **Viper (1995‑ )** – vi key bindings for Emacs.
- **Kakoune (2012‑ )** – Modal editor inspired by vi, with distinct key bindings and external program calls.
- **Evil (2013‑ )** – vi‑modal editing layer for Emacs.
- **vis (2015‑ )** – vi‑like editor featuring structural regular expressions and ideas from the Plan 9 Sam editor.
- **Helix (2021‑ )** – New modal editor influenced by Kakoune and Vim, using its own key bindings.