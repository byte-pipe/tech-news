---
title: "Emacs 31 Is Around the Corner: The Changes I'm Already Daily Driving | Rahul's Blog"
url: https://www.rahuljuliato.com/posts/emacs-31-around-the-corner
date: 2026-06-18
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-19T01:19:18.078329
---

# Emacs 31 Is Around the Corner: The Changes I'm Already Daily Driving | Rahul's Blog

# Emacs 31 Is Around the Corner: The Changes I’m Already Daily Driving

## Overview  
- I have been building Emacs 31 from the `emacs-31` branch and using it as my “Emacs Solo” (no external packages) config for several months.  
- Every new feature I adopt is marked with an `; EMACS-31` comment so I can clean it up after the official release.  
- The article lists the changes I rely on today; all are either in `master` or very close, and none require third‑party packages.  
- Emacs 31 is still in pre‑release, so names and defaults may still shift.

## Tree‑sitter that just works  
- `treesit-auto-install-grammar` and `treesit-enabled-modes` are now `t` by default, so Emacs offers to fetch and compile missing grammars automatically.  
- No longer need to manually populate `treesit-language-source-alist` for languages such as TypeScript, Rust, TOML, YAML, Dockerfile, etc.; the mode definitions include the source URLs.  
- I can delete the old `add-to-list` blocks that pointed to external repos.  
- Caveat: auto‑installed grammar binaries are not segregated by architecture, so a binary built on x86_64 will fail on arm64 if the same `~/.emacs.d/` tree is shared.

## Built‑in `markdown‑ts‑mode` (experimental)  
- The mode ships in Emacs 31; I was the original author and Stéphane Marks joined as co‑author, adding most of the polish.  
- Features I use:  
  - Org‑like keybindings for navigating headings, folding sections, and moving between structural elements.  
  - Live, language‑specific fontification inside fenced code blocks (e.g., Emacs Lisp blocks get true `elisp` font‑lock).  
  - Editing commands inside code blocks respect the target language’s major mode.  
  - Inline image rendering replaces `![](path)` with the actual image in the buffer.  
- It is not auto‑enabled for `.md` files; you must load the library (`M-x load-library RET markdown-ts-mode`) and enable it manually or add it to `auto-mode-alist`.  
- I encourage users to try it and report bugs via `M-x report-emacs-bug` or direct feedback to me and Stéphane.

## Eglot rendering docs with `markdown‑ts` (also experimental)  
- Setting `eglot-documentation-renderer` to `'markdown-ts-view-mode` makes LSP hover documentation appear formatted, without extra packages.  
- I disable `eglot-code-action-indications` because some language servers produce noisy hints.  
- A pending change: `eglot-events-buffer-size` will be replaced by `eglot-events-buffer-config`; I have left a comment to clean this up later.

## Eldoc at point  
- Enabling `(eldoc-help-at-pt t)` shows the help text for the symbol under the cursor automatically.  
- Combined with `eldoc-echo-area-prefer-doc-buffer`, this provides continuous guidance while browsing unfamiliar code.

## Smarter, eager completion  
- The new variable `completion-eager-update` set to `t` makes the minibuffer completion UI update more responsively as you type.  
- (Further completion‑related toggles are introduced but not detailed in the excerpt.)