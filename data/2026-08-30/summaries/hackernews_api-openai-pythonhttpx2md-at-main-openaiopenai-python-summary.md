---
title: openai-python/httpx2.md at main · openai/openai-python · GitHub
url: https://github.com/openai/openai-python/blob/main/httpx2.md
date: 2026-08-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-30T06:02:33.520679
---

# openai-python/httpx2.md at main · openai/openai-python · GitHub

# Migrating to HTTPX2

## Overview
- The OpenAI Python SDK now uses **HTTPX2** for both synchronous and asynchronous HTTP clients.  
- `httpx` is no longer installed automatically; `httpx2` is bundled with the SDK.  

## Default HTTP client
- Creating `OpenAI()` or `AsyncOpenAI()` without a custom client works unchanged (API calls, streaming, retries, timeouts, etc.).  
- No extra installation needed beyond `pip install openai`.  
- If your code imported `httpx` only because the old SDK pulled it in, add a direct `httpx` dependency or switch imports to `httpx2`.  

## TLS certificates and trust stores
- HTTPX2 uses the **operating‑system trust store** instead of `certifi`.  
- This may break verification in minimal containers, corporate proxies, or custom cert bundles.  
- Fixes:  
  - Install CA certificates into the OS store.  
  - Or set environment variables:  
    - `SSL_CERT_FILE=/path/to/ca-bundle.pem`  
    - `SSL_CERT_DIR=/path/to/ca-directory`  
  - For custom clients, pass an `ssl.SSLContext` via `verify`.  

## Custom HTTP client
- Use HTTPX2 client classes (`httpx2.Client`, `httpx2.AsyncClient`) and helper factories:  
  - `DefaultHttpx2Client` / `DefaultAsyncHttpx2Client` preserve SDK defaults (timeouts, pool, redirects).  
  - Example configurations: proxy, custom transport, granular timeouts.  
- Legacy names (`DefaultHttpxClient`, `DefaultAsyncHttpxClient`) still exist but now create HTTPX2 clients; prefer the new names.  

## Replacing HTTPX objects
| Old HTTPX object | New HTTPX2 object |
|------------------|-------------------|
| `httpx.Client` | `httpx2.Client` |
| `httpx.AsyncClient` | `httpx2.AsyncClient` |
| `httpx.Timeout` | `httpx2.Timeout` |
| `httpx.URL` | `httpx2.URL` |
| `httpx.Limits` | `httpx2.Limits` |
| `httpx.HTTPTransport` | `httpx2.HTTPTransport` |
| `httpx.AsyncHTTPTransport` | `httpx2.AsyncHTTPTransport` |
| `httpx.MockTransport` | `httpx2.MockTransport` |

- Numeric timeout values and string URLs remain unchanged.  

## Authentication and event hooks
- Handlers now receive `httpx2.Request` and `httpx2.Response` objects.  
- Update custom auth classes, transport subclasses, and any tracing or middleware to use the corresponding `httpx2` classes.  

## Raw responses, streaming, and exceptions
- SDK response models unchanged.  
- When using a native HTTPX2 client:  
  - `response.http_response` is an `httpx2.Response`.  
  - `response.http_request` is an `httpx2.Request`.  
- Use `cast_to=httpx2.Response` for unparsed responses.  
- Catch SDK exceptions (`openai.APITimeoutError`, `openai.APIConnectionError`); underlying transport errors will be HTTPX2 exceptions.  

## aiohttp extra
- `openai[aiohttp]` now provides an HTTPX2‑based transport (`DefaultAioHttpClient`), which is an `httpx2.AsyncClient`.  
- No legacy `httpx` or `httpx-aiohttpadapter` is installed.  

## Request mocking and testing
- Mocks must work with HTTPX2 requests/responses (`httpx2.MockTransport`).  
- Update any RESPX usage to a version compatible with HTTPX2, or use the temporary legacy client escape hatch if migration is not immediate.