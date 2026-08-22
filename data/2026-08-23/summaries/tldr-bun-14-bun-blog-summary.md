---
title: Bun 1.4 | Bun Blog
url: https://bun.com/blog/bun-v1.4
date: 2026-08-23
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-23T06:01:05.774617
---

# Bun 1.4 | Bun Blog

# Bun 1.4 – Release Summary

## Installation options
- **curl**: `curl -fsSL https://bun.sh/install | bash`
- **PowerShell**: `irm bun.sh/install.ps1 | iex`
- **npm**: `npm install -g bun`
- **Homebrew**: `brew install oven-sh/bun/bun`
- **Docker**: `docker pull oven/bun`

## Upgrade
- Run `bun upgrade` to move to 1.4.

## Major new features
- Added **Bun.Image**, **Bun.WebView**, **Bun.markdown**, **Bun.cron()**, **Bun.Terminal**.
- New CLI flags: `bun run --parallel`, `bun test --parallel`.
- Package‑management helpers: `bun audit fix`, `bun dedupe`, `bun prune`.
- Core rewritten from Zig to Rust.

## Node.js compatibility
- Integrated **+1,517** Node.js test suite cases (largest jump since 1.0).
- Pass rates (selected modules):
  - `node:http`, `node:fs`, `node:cluster`, `node:timers`, `node:zlib`, `node:vm`, `node:streampass` – 97 %
  - `node:quic` – 99 %
  - `node:events`, `node:trace_events`, `node:sqlite` – 100 %
- Ongoing compatibility tracking available online.
- Not 100 % yet, but most ecosystem packages work unchanged.

## Ecosystem support
- **Playwright 1.4.0** runs on Bun (CDP, UI, Chromium on Windows).
- **Next.js 16** (`bun next build`) works with Turbopack and React Compiler.
- **vitest 1.4.0** supports coverage, threads, and forks.
- **OpenTelemetry 1.4.0** and **dd-trace 1.4.0** function with Bun.
- Additional packages now compatible:
  - Nuxt, testcontainers, dockerode, https-proxy-agent, socks-proxy-agent, crawlee, @grpc/grpc-js, ConnectRPC, amqplib, @aws-sdk/client-s3, TypeORM, nock, Fastify, light‑my‑request, happy‑dom, piscina.

## New Node.js APIs in Bun
- `worker_threads` enhancements (resourceLimits, stdout, stderr, eval options).
- WebSocket events: `'upgrade'`, `'unexpected-response'`.
- `socket.upgradeTLS({ isServer: true })` for server‑side STARTTLS.
- `node:cluster` socket sharing.
- Implemented `node:repl`, `node:trace_events`, `node:domain`.

## Production performance improvements
- **CPU**: idle usage ↓ 5×; large app p99 ↓ 2× (24 % → 10 %); small app idle ↓ 5×.
- **Memory**: reductions of 13 %–48 % across common HTTP servers.
- **Startup**: 
  - Windows: 2.5× faster (15.5 ms vs 39 ms).
  - Linux: 2× faster (5.1 ms vs 10.9 ms) and < 50 % memory.
- **Binary size**: up to 17 % smaller on Linux/Windows; macOS binaries ~1 MB larger.

### Sample memory comparison (1 M requests, 64 connections)

| Server | Bun 1.4 | Bun 1.3 | Node 26 | Δ vs 1.3 |
|--------|--------|--------|--------|----------|
| fastify | 120 MB | 233 MB | 156 MB | –48 % |
| express | 92 MB | 169 MB | 145 MB | –46 % |
| node:http | 81 MB | 135 MB | 107 MB | –40 % |
| next.js | 285 MB | 397 MB | 342 MB | –28 % |
| bun.serve | 36 MB | 45 MB | n/a | –20 % |
| vite dev server | 233 MB | 268 MB | 214 MB | –13 % |

## Observability tools
- `bun --cpu-prof` → Chrome DevTools/VS Code.
- `bun --heap-prof` → V8‑compatible heap snapshot.
- `node:inspector` session for live CPU profiling.
- Datadog and OpenTelemetry integrations work out‑of‑box.
- Async stack traces now point to user code for async operations.
- New `--cpu-prof-md` flag outputs a Markdown CPU profile with top functions and call tree.

## Summary
Bun 1.4 delivers a substantial boost in Node.js compatibility, introduces several high‑level APIs, rewrites the runtime in Rust, and achieves notable reductions in CPU, memory, startup time, and binary size, while keeping existing tooling and popular frameworks fully functional.