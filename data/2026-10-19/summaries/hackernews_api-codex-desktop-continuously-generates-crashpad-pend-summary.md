---
title: Codex Desktop continuously generates Crashpad pending dumps, growing without any limit: +5GB per day at least · Issue #25921 · openai/codex · GitHub
url: https://github.com/openai/codex/issues/25921
date: 2026-10-18
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-10-19T09:16:55.739405
---

# Codex Desktop continuously generates Crashpad pending dumps, growing without any limit: +5GB per day at least · Issue #25921 · openai/codex · GitHub

# Codex Desktop continuously generates Crashpad pending dumps, growing without any limit: +5 GB per day at least  

## Description  
- The Codex Desktop app creates paired `paired.dmp` and `_sidecar.json` files in  
  `~/Library/Application Support/com.openai.codex/web/Crashpad/pending`.  
- On the reporter’s machine the directory reached **4.9 GB** and **54 504 files** in a single day, and the count kept increasing during investigation.  
- The app remains usable; the issue is the unbounded background generation of Crashpad dumps, not a crash that prevents launching.  

## Environment  
- Product: Codex Desktop (macOS)  
- Version: 26.527.60818 (CFBundleVersion 3437)  
- Crashpad/Electron annotation: `prod=Codex_Mac,ver=148.0.7778.179`  
- macOS 13.3.1 (build 25D771280a)  
- Architecture: arm64  

## Observed evidence  
- Pending directory contents (as of 2026‑06‑02):  
  - 27 252 `.dmp` files  
  - 27 252 `_sidecar.json` files  
  - Total size ≈ 4.9 GB, 54 504 files.  
- File timestamps span from 2026‑06‑02 13:31 to 2026‑06‑02 21:08, showing continuous creation.  
- Two `browser_crashpad_handler` processes have been running since 2026‑05‑30 11:47, both using the same Crashpad database.  

## Expected behavior  
- Crash reports should be bounded, uploaded/processed, rotated, or not generated continuously while the application is functioning normally.  

## Actual behavior  
- Crashpad pending reports accumulate rapidly, consuming multiple gigabytes of disk space without cleanup.  

## Commands used for evidence collection  
- `du -sh "$HOME/Library/Application Support/com.openai.codex/web/Crashpad/pending"`  
- `find … -type f | wc -l` to count files  
- `find … -type f | sed 's/.*\.//' | sort | uniq -c | sort -nr` to list file‑type frequencies  
- `PlistBuddy` commands to read `CFBundleShortVersionString` and `CFBundleVersion` from the app bundle  
- `sw_vers` and `uname -m` for OS and architecture info  
- `ps ax -o pid,ppid,lstart,command | grep -E 'browser_crashpad_handler|com.openai.codex/web/Crashpad'` to locate Crashpad handler processes  

## Related issues  
- “Codex App update left old crashpad helper; relaunch could no‑op until clean restart” (#25259)  
- “Codex App UI freezes: worker crashes, massive git/worktree errors, and concurrent orphaned app‑server processes” (#11090)  
- “Can’t open app in Tahoe 26.2 (25C56)” (#10627) – prior Crashpad/macOS startup reports  

## Additional notes  
- The reporter is willing to share a recent `.dmp` file privately if OpenAI provides a safe upload path, but does not publish dumps publicly due to potential exposure of private data.