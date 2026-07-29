---
title: Model Configuration | Kimi Code Docs
url: https://www.kimi.com/code/docs/en/kimi-code/models
date: 2026-07-29
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-07-30T06:33:28.546736
---

# Model Configuration | Kimi Code Docs

# Model Configuration Summary

## Model Overview
- Two primary models: **Kimi K3** and **Kimi K2.7 Code**, each with four Model IDs.  
- Model IDs: `k3`, `k3-256k`, `kimi-for-coding`, `kimi-for-coding-highspeed`.  
- **k3-256k** offers a 256k context window with lower quota consumption; **k3 (1M)** provides up to 1 M context for higher‑tier members.  
- **kimi-for-coding-highspeed** runs ~5–6× faster but uses ~3× more quota.  

### Switching Guidance
- Switching between 1M and 256k contexts may require a **compact** operation to reduce the current session’s context below 256k.  
- Compact before switching if the session exceeds the target limit or contains video files (256k model does not support video).  
- Switching from 256k to 1M does not affect the cache; no compact needed.  

## Model Details
| Model ID | Version | Description | Speed | Context Window | Reasoning Effort | Thinking | Availability | Multimodal Input |
|----------|---------|-------------|-------|----------------|------------------|----------|--------------|------------------|
| k3 | Kimi K3 | Flagship coding model, 2.8T params | Regular | Up to 1M (Allegretto+) | low / high / max (default high) | ON | Moderato+ (1M for Allegretto+) | Image, video |
| k3-256k | Kimi K3 | 256k context version, lower quota | Regular | 256k only | low / high / max (default high) | ON | Moderato+ | Image only |
| kimi-for-coding | K2.7 Code | Good for code completion and routine tasks | Regular | 256k | low / high / max (default high) | ON | All members | Image, video |
| kimi-for-coding-highspeed | K2.7 Code HighSpeed | Same ability, 5–6× faster output | HighSpeed (6× speed, 3× quota) | 256k | low / high / max (default high) | ON | Allegretto+ | Image, video |

## Membership Impact
- Higher plans unlock larger context windows, faster models, and multimodal capabilities.  
- Lack of plan entitlement results in **401** errors for inaccessible models or features.  

## Common Issues & Fixes
- **Usage spikes after model change**: cache miss forces re‑prefill; start a new session to reduce consumption.  
- **401 errors**: verify plan includes the requested model, context size, and HighSpeed access.  
- **HighSpeed not faster**: ensure correct Model ID (`kimi-for-coding-highspeed`) and recognize that tool overhead (file I/O, command execution) is not accelerated.  
- **Frequent reasoning‑effort switches**: each switch invalidates cache; keep effort consistent or start a new session when changing.  

## Switching Models

### General Usage Notes
- Always start a **new session** when changing Model IDs to avoid cache invalidation.  
- Use the **Model ID**, not the version name, in API calls.  
- Keep **Thinking** enabled for K3 and K2.7 Code; disabling routes requests to K2.6.  

### Official Clients
- **Kimi Code CLI**: use `type/model` command; re‑login if the latest model is missing.  
- **VS Code extension**: select model from dropdown; restart VS Code if not listed.  

### Third‑Party Tools
1. Generate an API Key in the Kimi Code Console.  
2. Set the Base URL and Model ID in the tool’s configuration.  

| Protocol | Base URL |
|----------|----------|
| OpenAI compatible | `https://api.kimi.com/coding/v1` |
| Anthropic compatible | `https://api.kimi.com/coding/` |

- Refer to tool‑specific guides (Claude Code, OpenCode, Codex) for detailed steps.  

### Pre‑setup for K3 in Third‑Party Tools
- **Context window**: manually set to `1048576` if the tool defaults lower.  
- **Reasoning effort mapping**:  
  - `null` / `undefined` → high (default)  
  - `ultra`, `max`, `xhigh` → max  
  - `high`, `medium` → high (recommended)  
  - `low`, `minimum`, `light` → low  
  - `none` → thinking disabled (error if unsupported)