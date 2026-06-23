---
title: oak · oak
url: https://oak.space/oak/oak
date: 2026-06-22
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-06-23T10:21:25.989224
---

# oak · oak

# Oak Repository Summary

## Overview
- Open‑source core of **Oak**: version control designed for AI agents.
- Implements branch‑per‑session workflow, branch descriptions instead of commit messages, and lazy, content‑addressed mounts.
- Faster than Git for agent workloads due to on‑demand hydration.

## Crates
| Crate | Path | crates.io | Purpose |
|-------|------|-----------|---------|
| oakvcs-core | `core/` | oakvcs-core | VCS foundation: BLAKE3 hashing, chunking, diff/merge, Blob/Manifest/Commit/Tree model, optional local repo (SQLite + Git). |
| oakvcs-cli | `cli/` | oakvcs-cli | `oak` command‑line binary built on oakvcs-core. |

## Using the Library in Your Project
- `oakvcs-core` can be added independently for data‑model and hashing only.  
  ```toml
  [dependencies]
  oakvcs-core = { version = "0.99.0", default-features = false }
  ```
- Imported as `oak_core`; enable `local-repo` feature for on‑disk repository support.

## Installing the CLI
- Public beta (v0.99.0). Quick install via prebuilt binary:  
  ```bash
  curl -fsSL oak.space/install | sh
  ```
- Supports macOS (Apple Silicon) and Linux (x86_64). `oak upgrade` updates the binary in place.

### Windows (x86_64)
- Download `oak-windows-x86_64.exe` from the latest GitHub release, rename to `oak.exe`, and add to `PATH`, **or** build with Cargo: `cargo install oakvcs-cli`.
- `oak mount` uses Projected File System (ProjFS); enable once per machine:  
  ```powershell
  Enable-WindowsOptionalFeature -Online -FeatureName Client-ProjFS -NoRestart
  ```
- All other commands (clone, push, pull, commit) work without ProjFS.

## Building from Source
- Build whole workspace: `cargo build --workspace`.
- Run CLI tests: `cargo test -p oakvcs-cli`.
- Release build and tooling: `make build`.
- Non‑mutating release readiness check: `make release-proof`.
- CLI links to local `oak-core` via workspace path; no extra setup required.

## License
- Apache‑2.0 (see `LICENSE` file).

## AI Contribution Note
- Repository was authored primarily by AI with human oversight.  
- Contributions or corrections can be sent to `contact@oak.space` or discussed on the Oak Discord.