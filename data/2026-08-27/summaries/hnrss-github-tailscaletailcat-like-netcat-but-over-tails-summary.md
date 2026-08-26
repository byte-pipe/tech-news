---
title: "GitHub - tailscale/tailcat: like netcat, but over Tailscale's data plane, without Tailscale's control plane · GitHub"
url: https://github.com/tailscale/tailcat
date: 2026-08-26
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-27T06:40:56.323727
---

# GitHub - tailscale/tailcat: like netcat, but over Tailscale's data plane, without Tailscale's control plane · GitHub

# Tailcat – Netcat‑like Tool Over Tailscale’s Data Plane  

## Overview  
- Tailcat is a Go library and CLI that provides netcat‑style functionality using Tailscale’s WireGuard‑encrypted data plane, without requiring the Tailscale control plane.  
- Connections are established via Tailscale’s magicsock (WireGuard) with DERP as a fallback NAT‑hole‑punching relay.  
- All traffic is end‑to‑end encrypted; no Tailscale account, root privileges, or system‑wide routing changes are needed.  

## Installation  
- Go: `go install github.com/tailscale/tailcat/cmd/tailcat@latest`  
- Nix flakes: `nix run github:tailscale/tailcat` or `nix profile install github:tailscale/tailcat`  

## Basic Usage  

### Pipe stdin/stdout between two machines  
1. **Server**: `tailcat` – prints a short connection token (ephemeral address) and waits.  
2. **Client**: `echo hello | tailcat <token>` – sends data to the server, which then outputs it.  

### Expose local TCP ports  
- Server: `tailcat --serve=8080,8443` (or `--serve=all`) – creates a token for the forwarded ports.  
- Client: `tailcat <token> 8080` – connects to the remote port and can issue HTTP requests, etc.  

### Auth‑free SSH server (Linux/macOS)  
- Server: `tailcat --serve=no-auth-ssh` – runs an SSH server without authentication.  
- Client: `tailcat ssh <token>` or `tailcat ssh <token> ls -la` – opens an SSH session over the tunnel.  

### Miscellaneous Commands  
- `tailcat ping --until-direct` – tests connectivity, reporting whether packets travel via DERP or direct UDP.  
- `tailcat socks` – starts a SOCKS5 proxy over the tunnel; can be used with `curl`.  
- `tailcat --serve=exit-node` – acts as an exit node for the client.  
- `tailcat parse <token>` – prints the token’s WireGuard public key and DERP region as JSON.  
- `tailcat resolve <short‑token>` – expands a short token into a self‑contained long token with embedded DERP info.  
- `tailcat --full-address` – makes the server print the long token directly.  

## Key Management  
- **Ephemeral keys (default)**: each server run generates a fresh in‑memory WireGuard key; the token is valid only for that session.  
- **Saved keys**: `tailcat genkey` creates a persistent key stored in `~/.config/tailcat/keys/`. Using a saved key makes the address reusable across restarts.  
- CLI indicates whether an address is ephemeral or based on a saved key.  
- Options:  
  - `--key=new` – force an ephemeral key even if a saved key exists.  
  - `--key=<name>` – use a specific saved key.  
  - `tailcat genkey --delete --key=default` – remove a saved key.  
  - `tailcat genkey --list` – list all saved keys.  

## DERP Relays  
- Default DERP map: `https://tailcat.dev/derpmap.json`.  
- Users can rely on the free rate‑limited DERP relays or run their own.  

## Library Usage  
- The Go library can be imported as `github.com/tailscale/tailcat`.  
- One side runs a Tailcat server (listener) to obtain a connection token; the other side uses the token to connect as a client.  

## License  
- Tailcat is fully open source.