---
title: "GitHub - wojtczyk/trust: TRUST – Coding Rust like it's 1989 · GitHub"
url: https://github.com/wojtczyk/trust
date: 2026-05-07
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-05-08T08:13:08.338516
---

# GitHub - wojtczyk/trust: TRUST – Coding Rust like it's 1989 · GitHub

# TRUST – Coding Rust like it's 1989

## Overview
- Retro terminal UI IDE for Rust projects, inspired by classic blue‑screen DOS environments.  
- Experimental nostalgia project that can edit files, browse Rust projects, and execute Cargo commands.  

## Features
- Full‑screen text editor with dirty‑buffer indicator (`*` in the title).  
- Project pane showing directories and Rust‑related files while skipping `.git`, `target`, and common build folders.  
- Bottom pane captures compiler and test output.  
- Ability to build and run TRUST itself from within TRUST.  

## Installation & Run
- Run with `cargo run -- /path/to/rust/project`.  
- If no path is provided, the current directory is opened.  

## Keyboard Shortcuts
- F1: help  
- F2 / Ctrl+S: save  
- F3 / Ctrl+O: open selected file  
- Backspace: go to parent directory in project pane  
- F4 / Tab / Ctrl+F: cycle focus between panes  
- F5 / Ctrl+R: `cargo run`  
- F7: `cargo check`  
- F8 / Ctrl+T: `cargo test`  
- F9 / Ctrl+B: `cargo build`  
- F10: open menu bar  
- Ctrl+C, Ctrl+V, Ctrl+X: copy, paste, cut  
- Esc / Ctrl+Q: quit  
- Alt+X: delete line  
- Alt+U: duplicate line  
- Shift + navigation keys: select text  

## Menus
- Open with F10; navigate with left/right arrows, up/down arrows, and Enter.  
- Esc closes the menu; mouse clicks also work.  
- **File > New**: prompts for filename and creates it in the current project pane directory.  
- **Project > New project**: opens Cargo project dialog (parent directory, project name, binary/library selector).  
- **Window**: switches between panes and contains the former focus option.  

## Mouse Interaction
- Click inside editor to move cursor; drag to select text.  
- Click project pane to open files or navigate directories; click any pane to focus it.  
- Drag vertical divider to resize project and editor panes; drag top border of compiler/message pane to resize.  
- Scroll within any pane to move through content.  

## FAQ
- **Why?** Rust deserves a blue‑screen IDE reminiscent of the old days.  
- **File saving?** Yes, via F2 or Ctrl+S; dirty buffers are marked with `*`. Use at your own risk as it is a fun project.  
- **Affiliation?** No affiliation with classic DOS IDE vendors; it is an independent nostalgia project.  

## Repository Information
- Stars: 82  
- Forks: 1  
- Primary language: Rust (100 %)  
- License: MIT  

## Topics
- rust, terminal, retro, ide, tui, cargo, ratatui