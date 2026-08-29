---
title: GitHub - kaifcodec/user-scanner: 🕵️‍♂️ (2-in-1) Email & Username OSINT suite for deep data extraction just from a single Email/Username. Analyzes 455+...
url: https://github.com/kaifcodec/user-scanner
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:02:01.768457
---

# GitHub - kaifcodec/user-scanner: 🕵️‍♂️ (2-in-1) Email & Username OSINT suite for deep data extraction just from a single Email/Username. Analyzes 455+...

# User‑Scanner Repository Overview

## Project Description
- A 2‑in‑1 OSINT suite for deep email and username intelligence.  
- Supports 455+ scan vectors (≈175 email sites, ≈280 username platforms).  
- Provides rapid digital‑footprint mapping, behavior analysis, metadata extraction, and account verification.

## Key Features
- Deep email & username OSINT across hundreds of platforms.  
- Rich metadata scraping (avatars, bios, follower counts, UID, seller status, etc.).  
- Cross‑scan & pivot engine that mines handles, profile links, and secondary emails, then recursively scans related vectors.  
- Model Context Protocol (MCP) server for native AI agent integration (Claude Desktop, Cursor, Antigravity, other LLMs).  
- Hudson Rock infostealer breach intelligence via `--hudson` flag.  
- High‑throughput parallel engine using httpx and curl_cffi with TLS fingerprint impersonation.  
- Permutation & alias generator for wildcard‑based username variations.  
- Export reports in PDF (with photos), JSON, CSV.  
- Built‑in proxy rotation with auto‑detection (http, socks5) and health validation (`--validate‑proxies`).  
- Responsive terminal UI with dynamic progress grids and clear status messages.

## Installation Options
- **PyPI (recommended)**  
  ```bash
  python3 -m pip install --upgrade pip
  pip install user-scanner
  # optional MCP support
  pip install "user-scanner[mcp]"
  ```
- **Virtual environment** – create and activate a venv, then `pip install user-scanner`.  
- **Nix** – run instantly: `nix run github:kaifcodec/user-scanner/main -- --help` or open a temporary shell with `nix shell github:kaifcodec/user-scanner/main`.

## Basic Usage
- Scan a single username: `user-scanner -u johndoe`  
- Scan a single email: `user-scanner -e johndoe@gmail.com`  
- Cross‑scan & pivot: add `--cross-scan` (optional depth, link verification).  
- Hudson Rock breach check: `--hudson` with `-u` or `-e`.  
- Targeted category/module scans: `-c dev`, `-m github,instagram`, list grids with `-lu` / `-le`.  
- Bulk scanning from files: `-uf usernames.txt`, `-ef emails.txt`.  
- Export reports: `-f pdf -o report.pdf` (or json/csv).  
- Verbose output and show all results: `-v --all`.  
- Proxy rotation with validation: `-P proxies.txt --validate-proxies`.

## AI & LLM Integration (MCP Server)
- Start server: `user-scanner-mcp` (add `-v` for verbose).  
- Configure client (e.g., Claude Desktop) to call the server via JSON:
  ```json
  {
    "mcpServers": {
      "user-scanner": {
        "command": "user-scanner-mcp"
      }
    }
  }
  ```
- Exposed tools for agents:  
  - `scan_username` – deep username enrichment, recursive cross‑scan, proxy handling.  
  - `scan_email` – deep email verification, link pivoting, custom proxies.  
  - `list_available_modules` – dynamic discovery of supported platforms and categories.

## Documentation Hub
- CLI flags reference.  
- Cross‑scan & pivoting guide.  
- Pattern syntax guide for username permutations.  
- Library mode guide.  

These resources reside in the `docs/` directory of the repository.