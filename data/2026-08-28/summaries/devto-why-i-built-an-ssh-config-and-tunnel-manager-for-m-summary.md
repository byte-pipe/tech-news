---
title: Why I Built an SSH Config and Tunnel Manager for macOS - DEV Community
url: https://dev.to/malusev998/why-i-built-an-ssh-config-and-tunnel-manager-for-macos-58n8
date: 2026-08-26
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-08-28T17:07:10.370469
---

# Why I Built an SSH Config and Tunnel Manager for macOS - DEV Community

# Why I Built an SSH Config and Tunnel Manager for macOS

## Motivation
- All internal tools (Grafana, Prometheus, staging clusters, AI tooling) are behind a bastion host and require SSH access.
- I was typing long commands such as `ssh -N -L 3000:localhost:3000 -J bastion prod-1` multiple times a day on three different machines.
- I created a native macOS app to edit `~/.ssh/config` without breaking its formatting, save tunnel presets, and open tunnels directly inside the app.

## The VPN Question
- I prefer SSH because I already understand it, it is present on every Linux server and developer machine, and it avoids adding a new daemon, credentials, and failure modes.
- Using a VPN would hide the network layer but would require additional maintenance; explicit port forwards are easier to manage for me.

## Shell Aliases Do Not Survive Three Machines
- My workflow spans a MacBook (macOS) and Linux machines, each with different shells, key paths, and host inventories.
- Synchronizing shell aliases across these environments proved unreliable; missing or outdated aliases caused errors.
- The SSH config file is already portable and universally understood, making it the natural place to store connection information.

## Nothing Tells You What Config Keys Mean
- Standard editors treat `~/.ssh/config` as plain text; misspelled directives are only discovered at connection time.
- The app embeds a **KeywordRegistry** with 95 entries that provide:
  - Real‑time auto‑completion.
  - A searchable “Add Setting” picker.
  - Inline documentation for each keyword.
- The editor is lossless: comments, blank lines, and custom indentation remain untouched; only the edited directive is rewritten.

## The Tunnel Engine Never Runs ssh
- macOS App Store sandbox rules prevent launching the system `ssh` binary, so tunnels are created in‑process using `swift-nio-ssh`.
- All three forwarding modes are implemented:
  - `-L` creates a local listener that forwards to a target.
  - `-D` runs a dynamic SOCKS5 proxy listener.
  - `-R` requests remote forwarding and maps it to a local port.
- `ProxyJump` directives are recursively resolved, inheriting configuration exactly as OpenSSH would.
- Added missing capabilities to `swift-nio-ssh`:
  - RSA key support via a custom key handler.
  - Post‑quantum key‑exchange fallback for macOS versions lacking native ML‑KEM.
- Reconnection uses deterministic exponential backoff with jitter, isolated in a testable module.
- Trade‑offs:
  - `ProxyCommand` is not supported (cannot spawn subprocesses).
  - `ControlMaster` directives are parsed but not executed.
  - Active tunnels terminate when the app quits.
- For cases that require the native binary, the app copies the exact `ssh` command to the clipboard.

## Seeing Connection State Is Most of the Value
- The dashboard visualizes active tunnels, flapping connections, resolved identity keys, and detailed error diagnostics.
- A built‑in `known_hosts` auditor performs static analysis to flag malformed entries without contacting the network.