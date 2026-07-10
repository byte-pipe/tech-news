---
title: Interview With Mitchell Hashimoto
url: https://alexalejandre.com/programming/interview-with-mitchell-hashimoto/
date: 2026-07-10
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-07-11T01:39:10.543318
---

# Interview With Mitchell Hashimoto

# Interview With Mitchell Hashimoto

## Background
- Creator of Vagrant, Packer, Consul, Terraform, Vault, Nomad, Waypoint, and now Ghostty and Vouch.  
- Has spent roughly 15 years building command‑line (CLI) applications.  
- Recently left HashiCorp to sharpen technical skills, explore GPU programming, desktop/single‑node systems, and the Zig language.  

## Why Ghostty and terminals?
- Wanted to understand how terminal emulators work after years of building CLIs.  
- Sought a fast, feature‑rich, natively cross‑platform terminal that could run tools like Vim and compilers, then be discarded.  
- Developed Ghostty privately, sharing it first with a Discord friends group before a wider beta.  

## Pushing terminals harder
- Sees terminals as an application platform comparable to browsers or desktop runtimes, but believes they should remain lightweight and secure.  
- Emphasizes composition: CLI tools already act like functions (UNIX “do one thing” philosophy).  
- Suggests improving protocols to enhance automation, scriptability, and integration (e.g., better PTY signalling).  

## Views on non‑legacy terminal APIs
- Looks to existing ecosystems (web DOM/JS, Apple AppKit/SwiftUI, Windows WinUI, Linux GTK/Qt) for inspiration rather than inventing from scratch.  
- No custom protocols have been introduced yet; research of decades‑old clipboard and UI standards guides his approach.  

## Proposed terminal extensions
- **n‑screen API**: Allow creation of unlimited off‑screen buffers, overlay screens with independent grid sizes, and render separate windows from the terminal emulator (e.g., native tabs for Neovim).  
- **Button protocol**: Extend OSC‑8‑style hyperlinks so that clickable elements persist in scrollback and can send custom messages to programs, enabling actions like opening files from history.  

## Standards and future direction
- Notes the lack of a modern standards body for terminals; current de‑facto standards arise from popular terminal implementations.  
- Explored replacing PTY with Wayland concepts but abandoned the idea.  
- Open to creating a new “text‑based application” environment with a translation layer for legacy apps, rather than trying to retrofit the existing terminal model.  

## Balancing vision with user needs
- Believes open‑source maintainers have no formal obligation to users (“as is, no warranty”), yet strives to improve software quality.  
- Alternates between fixing community‑reported issues and pursuing personal, longer‑term goals.  
- Acknowledges the tension between building ideal solutions and addressing immediate real‑world problems.