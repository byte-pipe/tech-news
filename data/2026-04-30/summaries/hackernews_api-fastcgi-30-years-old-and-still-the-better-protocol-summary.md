---
title: FastCGI: 30 Years Old and Still the Better Protocol for Reverse Proxies
url: https://www.agwa.name/blog/post/fastcgi_is_the_better_protocol_for_reverse_proxies
date: 2026-04-30
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-30T12:32:20.466334
---

# FastCGI: 30 Years Old and Still the Better Protocol for Reverse Proxies

# FastCGI: 30 Years Old and Still the Better Protocol for Reverse Proxies

## Introduction
- HTTP reverse‑proxying is fraught with security issues (e.g., desync attacks such as the Discord media‑proxy vulnerability).
- The root cause is the widespread use of HTTP between proxies and back‑ends, even though HTTP is ill‑suited for that role.
- FastCGI, a 30‑year‑old wire protocol, offers a safer alternative for proxy‑to‑backend communication.

## FastCGI as a Wire Protocol
- FastCGI defines only the transport format; it does **not** prescribe a process model.
- It can be used like HTTP: a long‑running daemon listens on a TCP or UNIX socket and receives requests over FastCGI.
- Existing application code can remain unchanged; handlers still use `http.ResponseWriter` and `http.Request`.

## Using FastCGI in Go
```go
// HTTP
l, _ := net.Listen("tcp", "127.0.0.1:8080")
http.Serve(l, handler)

// FastCGI
l, _ := net.Listen("tcp", "127.0.0.1:8080")
fcgi.Serve(l, handler)
```
- The only change is swapping `http.Serve` for `fcgi.Serve`; all other logic stays the same.

## Proxy Configuration Examples
| Proxy   | HTTP config                              | FastCGI config                                   |
|---------|------------------------------------------|--------------------------------------------------|
| nginx   | `proxy_pass http://localhost:8080;`     | `fastcgi_pass localhost:8080;`<br>`include fastcgi_params;` |
| Apache  | `ProxyPass / http://localhost:8080/`    | `ProxyPass / fcgi://localhost:8080/`            |
| Caddy   | `reverse_proxy localhost:8080 { transport http {} }` | `reverse_proxy localhost:8080 { transport fastcgi {} }` |
| HAProxy | `backend app_backend`<br>`server s1 localhost:8080` | `fcgi-app fcgi_app`<br>`docroot /`<br>`backend app_backend`<br>`use-fcgi-app fcgi_app`<br>`server s1 localhost:8080 proto fcgi` |

## Why HTTP Sucks for Reverse Proxies: Desync Attacks / Request Smuggling
- HTTP/1.1 lacks explicit message framing; the end of a message is inferred from its content, leading to divergent parsing.
- Different parsers can disagree on where one request ends and the next begins, enabling desync attacks.
- Patching parsers is a losing battle; new vulnerabilities keep appearing (e.g., James Kettle’s findings).
- HTTP/2 solves framing but only when both sides use it consistently; FastCGI has provided clear framing since 1996.

## Why HTTP Sucks for Reverse Proxies: Untrusted Headers
- Proxies need to convey trusted data (client IP, authenticated user, TLS details) to back‑ends.
- HTTP does this by inserting special headers (e.g., `X-Real-IP`), but there is no structural separation from client‑controlled headers.
- Mistakes in header sanitisation (case variations, multiple header names, differing middleware expectations) easily lead to trust‑boundary breaches.
- FastCGI separates trusted proxy data from client headers by prefixing HTTP headers with `HTTP_` and using distinct parameters (e.g., `REMOTE_ADDR`) for proxy‑supplied information.
- Go’s `net/http/fcgi` automatically maps these parameters to `http.Request` fields, eliminating the need for custom middleware.

## Advantages of FastCGI
- Robust, unambiguous message framing prevents desync and request‑smuggling attacks.
- Built‑in domain separation for trusted proxy data removes header‑injection risks.
- Simple integration with existing Go code and major reverse proxies (nginx, Apache, Caddy, HAProxy).
- Works with standard `http.Request` and `http.ResponseWriter` types, preserving developer ergonomics.

## Closing Thoughts
- FastCGI remains under‑used, partly due to its CGI‑derived name and general lack of awareness about HTTP reverse‑proxy security flaws.
- It has been in production at SSLMate for over a decade, proving its practicality.
- Limitations: no native WebSocket support, tooling gaps (e.g., `curl` cannot speak FastCGI), and some performance paths are less optimized than HTTP/1.1 or HTTP/2.
- For workloads that do not require WebSockets, FastCGI offers a simpler, more secure alternative; if performance ever becomes a bottleneck, scaling hardware is preferable to wrestling with HTTP‑related security complexities.