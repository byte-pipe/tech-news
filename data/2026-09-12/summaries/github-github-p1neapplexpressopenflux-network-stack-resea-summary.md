---
title: GitHub - p1neappleXpress/OpenFlux: Network stack research tool. TCP tunnel with pluggable transports. · GitHub
url: https://github.com/p1neappleXpress/OpenFlux
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-09-12T01:23:21.192915
---

# GitHub - p1neappleXpress/OpenFlux: Network stack research tool. TCP tunnel with pluggable transports. · GitHub

# OpenFlux Summary

## Disclaimer
- The author does not encourage using OpenFlux to bypass restrictions or violate platform rules.
- The project is non‑commercial, contains no paid features, hidden subscriptions, or commercial benefit.
- Responsibility for forks, modifications, or derivative versions lies with their authors.
- The code is provided “as is” without warranties.

## Overview
- OpenFlux is a network‑stack research tool that creates a TCP tunnel with pluggable transports.
- Data flow: **Client (SOCKS5) → Transport → Exit Node → Internet**.

## Requirements
- Go version 1.26.3 or newer (for building desktop client and exit‑node binary).
- Android NDK v27.0.12077973+ (for Android client).
- Xcode v26.6+ (for iOS client).
- A Linux VPS/VDS to run the exit node.

## Transports
- **Yandex** – sends packets via Yandex Docs cursor messages.
- **Max** – sends packets via WebRTC DataChannel (experimental; avoid using primary or critical Max accounts).

## Architecture
```
universal-bypass-tool/
├─ main.go
├─ transport/
│  ├─ transport.go          # Transport interface
│  ├─ yandex/                # Yandex Docs backend
│  └─ oneme/                 # Max Messenger backend
├─ tunnel/
│  ├─ tunnel.go              # TCP tunnel core
│  ├─ endpoint.go            # Virtual NIC
│  └─ rawsocket.go           # Raw socket (exit node)
├─ socks5/                   # SOCKS5 server
├─ network/                  # Checksums, packet parsing
└─ utils/                    # Debug logging
```

## Build Instructions
- **Desktop client / exit‑node binary**
  ```bash
  go mod tidy
  go build -o universal-bypass-tool .
  ```
- **Android client**
  ```bash
  export ANDROID_NDK_HOME=<your Android NDK path>
  ./build_android.sh
  ```
- **iOS client**
  ```bash
  export XCODE_PATH="<your Xcode.app path>"   # optional, defaults to /Applications/Xcode.app
  ./build_ios.sh
  ```

## Usage
### Exit node setup
1. Root access is required.
2. Only the legacy Yandex document editor is supported.
3. Run:
   ```bash
   sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
   sudo ./universal-bypass-tool --exit-node --url "YOUR_YANDEX_DOC_URL" --debug
   ```

### Desktop client setup
```bash
./universal-bypass-tool --client --url "YOUR_YANDEX_DOC_URL" --socks5 :1080 --debug
```
- Configure your browser (or other applications) to use SOCKS5 proxy at `localhost:1080`.

## Flags
- `--client` – run as client.
- `--exit-node` – run as exit node.
- `--socks5` – SOCKS5 listen address (default `:1080`).
- `--url` – Document URL for Yandex Docs (default `https://localhost`).
- `--maxToken` – Auth token for Max transport.
- `--maxUid` – User ID for Max transport.
- `--debug` – enable verbose logging (default `false`).
- `--transport` – select transport backend (`yandex` by default).

## Implementing Custom Transports
- Implement the `Transport` interface defined in `transport/transport.go`.
- Register the new transport in the `main.go` switch block.

## License
- Licensed under the GNU General Public License v3.0 or later.
- Third‑party licenses are listed in the `NOTICE` file.