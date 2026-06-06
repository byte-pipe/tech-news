---
title: GitHub - microsoft/mxc: Policy-driven, layered isolation and containment · GitHub
url: https://github.com/microsoft/mxc
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-07T06:01:35.736638
---

# GitHub - microsoft/mxc: Policy-driven, layered isolation and containment · GitHub

# Microsoft Execution Container (MXC) – Summary

## Overview
- MXC is a sandboxed code‑execution system for running untrusted code (model output, plugins, tools) on Windows, Linux, and macOS.  
- It abstracts multiple containment backends behind a unified JSON configuration schema and a TypeScript SDK.

## Warning
- The repository contains an early preview; sandbox implementations are still evolving.  
- Current policies may be overly permissive and should not be treated as security boundaries.  
- Security‑researcher collaboration is welcomed while MXC matures.

## Features
- **Cross‑platform** support (Windows, Linux, macOS) with platform‑appropriate backends.  
- **JSON‑based configuration** using a versioned schema to define execution parameters and security policies.  
- **Multiple containment backends**: ProcessContainer, Windows Sandbox, LXC, Bubblewrap, Seatbelt (macOS), MicroVM (NanVix), Hyperlight, IsolationSession, WSLC.  
- **Policy‑driven sandboxing** covering:
  - Filesystem: read‑only and read‑write path lists (denied paths not yet on Windows).  
  - Network: proxy support (not on macOS); allow/block outbound and host filtering (not yet on Windows).  
  - UI: clipboard, display, and GUI access controls.  
- **State‑aware lifecycle**: provision → start → exec → stop → deprovision for session sandboxes.  
- **TypeScript SDK** (`@microsoft/mxc-sdk`) offering one‑shot and state‑aware APIs.  
- **Diagnostics**: debug logging and ETW tracing for troubleshooting.

## Supported Platforms & Default Backends
| Platform | Default Backend | Other Available Backends |
|----------|----------------|--------------------------|
| Windows 11 24H2+ | ProcessContainer | windows_sandbox, wslc, microvm, hyperlight, isolation_session |
| Linux x64 / ARM64 | Bubblewrap | lxc, microvm, hyperlight |
| macOS ARM64 / x64 (schema 0.6.0‑alpha+) | Seatbelt | – |

- Stable backends (processcontainer, bubblewrap, lxc) work without experimental mode.  
- Experimental backends require `{ experimental: true }` in `SandboxSpawnOptions` or the `--experimentalCLI` flag.

## Build Requirements
- Rust toolchain (pinned to 1.93 via `src/rust-toolchain.toml`).  
- Node.js ≥ 18 and npm (for SDK and CLI).  

## Project Structure
- `src/` – Rust workspace (native binaries and shared libraries).  
- `sdk/` – TypeScript SDK (`@microsoft/mxc-sdk`).  
- `schemas/` – JSON configuration schemas (stable and development).  
- `docs/` – Documentation (schema reference, backend guides, design docs).  
- `tests/` – Test assets (configs, examples, scripts).  
- `scripts/` – Build and utility scripts.

## Build Instructions
### Windows
- `build.bat` – release build for current architecture.  
- `build.bat --debug` – debug build.  
- `build.bat --all` – release for both x64 and ARM64.  
- `build.bat --with-microvm` – include NanVix micro‑VM binaries.

### Linux
- `./build.sh` – release build.  
- `./build.sh --debug` – debug build.  
- `./build.sh --rust-only` – build only Rust binaries (skip SDK/CLI).

### macOS
- `./build-mac.sh` – release build for native architecture.  
- `./build-mac.sh --all` – build for both Apple Silicon and Intel.  
- `./build-mac.sh --debug` – debug build.  
- `./build-mac.sh --rust-only` – build only Rust binary.

All scripts compile the platform‑specific Rust binary, copy it into `sdk/bin/<arch>/`, and then build the TypeScript SDK.

## Testing
- **Rust unit tests**: `cargo test --workspace` (or target specific crates).  
- **SDK tests**: `npm test` (unit) and `npm run test:integration` (integration).  
- **End‑to‑end tests**: `cargo test -p wxc_e2e_tests`.

## Usage
### Native Binary
```bash
# Run with a JSON config file
wxc-exec.exe config.json

# Pass a Base64‑encoded config
wxc-exec.exe --config-base64 <base64-json>

# Enable debug output
wxc-exec.exe --debug config.json
```
- Linux: `./lxc-exec config.json`  
- macOS: `./mxc-exec-mac --experimental config.json`

### TypeScript SDK
```bash
npm install @microsoft/mxc-sdk

import {
  spawnSandboxFromConfig,
  createConfigFromPolicy,
  getAvailableToolsPolicy,
  getTemporaryFilesPolicy,
  getPlatformSupport,
} from '@microsoft/mxc-sdk';

if (!getPlatformSupport().isSupported) {
  throw new Error('MXC not available on this host');
}

const tools = getAvailableToolsPolicy(process.env);
const temp  = getTemporaryFilesPolicy();

const config = createConfigFromPolicy({
  version: '0.6.0-alpha',
  filesystem: {
    readonlyPaths: tools.readonlyPaths,
    readwritePaths: temp.readwritePaths,
  },
  network: { allowOutbound: false },
  timeoutMs: 30_000,
});

config.process!.commandLine = 'python -c "print(\'hello from sandbox\')"';

const child = spawnSandboxFromConfig(config, { usePty: false });

child.stdout!.on('data', d => process.stdout.write(d));
child.on('close', code => console.log(`sandbox exited with ${code}`));
```

The SDK handles policy creation, platform capability checks, and sandbox spawning, allowing both one‑shot execution and more complex, state‑aware workflows.