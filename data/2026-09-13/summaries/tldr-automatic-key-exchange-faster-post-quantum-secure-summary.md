---
title: Automatic Key Exchange: faster, post-quantum secure origin handshakes for 45 billion daily connections (and counting) | Cloudflare Blog
url: https://blog.cloudflare.com/automatic-key-exchange-for-origins/
date: 2026-09-13
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-09-13T02:06:45.156897
---

# Automatic Key Exchange: faster, post-quantum secure origin handshakes for 45 billion daily connections (and counting) | Cloudflare Blog

# Automatic Key Exchange: faster, post‑quantum secure origin handshakes for 45 billion daily connections (and counting)

## Background
- TLS 1.3 requires the client to pick a key‑exchange algorithm in the first ClientHello.  
- If the server prefers a different algorithm it sends a HelloRetryRequest (HRR), adding an extra round‑trip.  
- Cloudflare historically always sent an X25519 keyshare, which works for >95 % of origins but is sub‑optimal for ~30 % and is not quantum‑resistant.

## What Automatic Key Exchange does
- Extends the previous Automatic SSL/TLS system by **measuring** each origin’s supported key‑exchange groups instead of guessing.  
- Probes origins with lightweight handshakes offering a single group (X25519, P‑256, P‑384, P‑521, X25519‑MLKEM768).  
- Stores the result and uses the preferred algorithm on the first ClientHello, automatically selecting the post‑quantum hybrid X25519‑MLKEM768 when the origin supports it.

## Impact
- HRR rate dropped from ~52 % to 3.7 %, saving >150 ms at the 90th percentile of handshake latency.  
- Hundreds of thousands of domains now have post‑quantum‑secure connections without any manual configuration; the number is growing daily.  
- Reduces exposure to “harvest‑now, decrypt‑later” attacks and moves the Internet toward quantum‑security by the target Q‑Day (2029).

## Why the previous approach was costly
- X25519 keyshares are small (32 B) and fit in a single packet; post‑quantum keyshares (1,216 B) can exceed packet size, causing some legacy middleboxes to drop the handshake.  
- Some origins prefer P‑256 or P‑384, triggering HRR even for purely classical connections.  
- Relying on HRR as a safety valve added unnecessary round‑trips and latency.

## How the system works
1. **Scanning** – Cloudflare runs a few TLS 1.3 handshakes per origin, each offering one key‑exchange group.  
2. **Capability map** – The responses build a per‑origin capability table.  
3. **Tailored ClientHello** – For each request to an origin, Cloudflare selects the optimal keyshare (preferring X25519‑MLKEM768 when available).  
4. **Automatic fallback** – If an origin cannot handle the chosen group, the normal TLS fallback mechanisms apply, but this situation is now rare.

## Future outlook
- The share of origins supporting post‑quantum algorithms has risen from 0.5 % to 12.8 % and is expected to keep climbing as hosting stacks upgrade.  
- Automatic Key Exchange removes the need for site operators to become cryptography experts; quantum‑secure handshakes become the default.  
- Continued rollout will further shrink handshake latency and increase the proportion of quantum‑resistant connections across the Internet.