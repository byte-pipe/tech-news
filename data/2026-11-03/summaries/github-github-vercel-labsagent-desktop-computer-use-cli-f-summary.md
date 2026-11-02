---
title: GitHub - vercel-labs/agent-desktop: Computer use CLI for AI agents · GitHub
url: https://github.com/vercel-labs/agent-desktop
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-11-03T06:08:26.713765
---

# GitHub - vercel-labs/agent-desktop: Computer use CLI for AI agents · GitHub

# agent-desktop

## Overview
- CLI and C library that lets AI agents read and operate desktop applications through the OS accessibility tree on macOS, Windows, and Linux.  
- Agents receive a JSON snapshot containing a reference (`ref`) for each interactable element, act on a ref, then take another snapshot to verify the result—no pixel matching is used.  
- macOS implementation reuses a private command host that retains native accessibility objects; the host exits after 15 minutes of inactivity.  
- Headless mode performs actions via the accessibility API without moving the cursor or taking focus; the `--headed` flag enables physical input.  

## Installation
- Install globally with npm (or Bun, Yarn, pnpm): `npm install -g agent-desktop` and verify with `agent-desktop version`.  
- Native binaries for x64 and ARM64 are bundled; a direct native archive is also available from GitHub Releases.  
- Homebrew and Scoop packages are being prepared; no custom taps or buckets are maintained.  
- Platform‑specific permission requirements:  
  * **macOS** – Accessibility permission (`agent-desktop permissions --guide`).  
  * **Windows** – No extra grant beyond the terminal’s integrity level.  
  * **Linux** – Requires a graphical session with `at-spi2-core`.  

## Quick start
1. List available apps: `agent-desktop list-apps`.  
2. Take an interactive snapshot: `agent-desktop snapshot --app Finder -i`.  
3. Act on a ref from the snapshot: `agent-desktop click @s8f3k2p9:e8`.  
4. Re‑snapshot to confirm the UI change.  

- Refs are scoped to their snapshot; using a bare ref (e.g., `@e8`) is rejected.  
- When the UI changes, actions may return `STALE_REF` or `AMBIGUOUS_TARGET`; take a new snapshot and use fresh refs.  
- For windows with ambiguous targets, specify `--window-id` as shown in error details.  
- Dense interfaces can be explored with a skeleton snapshot (`snapshot --skeleton`) followed by focused snapshots on specific regions.  
- PowerShell requires quoting refs (`'@s8f3k2p9:e8'`) because an unquoted `@` triggers the splatting operator.  

## For AI agents
- Retrieve skill definitions:  
  * `agent-desktop skills get desktop` – loop, refs, verification, retry rules.  
  * `agent-desktop skills get platform` – OS‑specific differences.  
- Add the skill to an agent harness: `npx skills add https://github.com/vercel-labs/agent-desktop --skill agent-desktop`.  
- Document usage in `AGENTS.md` with the commands above.  
- Every command outputs a JSON envelope containing `ok` and either `data` or `error`.  
  * Errors include a code, disposition, and usually a suggestion; retry only when `error.disposition.retryissafe`.  
  * Full contract, error codes, and exit codes are described in `docs/json-output.md`.  

## Commands
- **Observe**: `snapshot`, `find`, `get`, `is`, `screenshot`, `list-surfaces`.  
- **Act on a ref**: `click`, `double-click`, `triple-click`, `right-click`, `type`, `set-value`, `clear`, `focus`, `select`, `toggle`, `check`, `uncheck`, `expand`, `collapse`, `scroll`, `scroll-to`.  
- **Keyboard & mouse**: `press`, `hover`, `drag`, `mouse-move`, `mouse-click`, `mouse-wheel`, `key-down`, `key-up`, `mouse-down`, `mouse-up`.  
- **Apps & windows**: `launch`, `close-app`, `list-apps`, `list-windows`, `list-displays`, `focus-window`, `resize-window`, `move-window`, `minimize`, `maximize`, `restore`, `open-system-surface`.  
- **Notifications**: `list-notifications`, `dismiss-notification`, `dismiss-all-notifications`, `notification-action`.  
- **Clipboard**: `clipboard-get`, `clipboard-set`, `clipboard-clear`.  
- **Other**: `wait`, `session`, `trace`, `cursor-overlay`, `status`, `permissions`, `version`, `batch`, `skills`.  

## Platform support
| Feature | macOS | Windows | Linux |
|---|---|---|---|
| Accessibility tree | Yes | Yes | Yes (AT‑SPI) |
| Click / type / keyboard | Yes | Yes | AT‑SPI; X11 / GNOME keys |
| Mouse input | Yes | Yes | X11, `--headed` |
| Screenshot | Yes | Yes | X11 windows; Wayland portal |
| Clipboard | Yes | Yes | Yes (Wayland needs `wl-clipboard`) |
| App & window management | Yes | Yes | Launch/list; X11 window control |
| Notifications | Yes | Yes | GNOME Shell |
| Shell surfaces (`open-system-surface`) | Yes | Yes | Planned |
| Planned extras | – | GNOME tray, Action Center | – |

- Detailed notes on Windows surface handling and Linux X11/Wayland are in `docs/install.md`.  
- `agent-desktop skills get platform` prints the full capability table for the current OS.  

## Language bindings
- Each release includes `libagent_desktop_ffi` for macOS, Linux, and Windows, enabling in‑process calls instead of spawning the CLI.  
- The FFI entry points, memory ownership, and threading rules are documented by `agent-desktop skills get ffi`.  
- Example (Python `ctypes`):  
  ```python
  import ctypes
  lib = ctypes.CDLL("./lib/libagent_desktop_ffi.dylib")
  lib.ad_adapter_create.restype = ctypes.c_void_p
  lib.ad_adapter_destroy.argtypes = [ctypes.c_void_p]
  assert lib.ad_init(6) == 0   # AD_RESULT_OK
  adapter = lib.ad_adapter_create()
  lib.ad_adapter_destroy(adapter)
  ```  

## Safety & privacy
- Snapshots, clipboard contents, screenshots, command output, and debug artifacts may contain private desktop data.  
- Keep such data out of public logs or uploads.  
- An optional `JEV` helper can send screen descriptions to a configured model provider; it operates separately from the native CLI.