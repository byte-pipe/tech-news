---
title: How We Saved Big and Simplified Our Image Pipeline: Adopting bunny.net on DEV - DEV Community
url: https://dev.to/devteam/how-we-saved-big-and-simplified-our-image-pipeline-adopting-bunnynet-on-dev-3d53
date: 2026-06-16
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-06-17T06:02:08.893627
---

# How We Saved Big and Simplified Our Image Pipeline: Adopting bunny.net on DEV - DEV Community

# How We Saved Big and Simplified Our Image Pipeline: Adopting bunny.net on DEV

## Background and Philosophy  
- DEV’s core goal is ultra‑fast web performance, keeping the architecture lean and caching aggressively at the edge.  
- Fastly handles HTML edge caching, so most page requests never hit the Puma servers.  
- User‑uploaded media (covers, avatars, screenshots, banners) grew into billions of high‑resolution assets, exposing weaknesses in the media pipeline.

## Problems with the Existing Multi‑CDN Setup  
- **Patchwork architecture**: different CDNs for different parts, an image‑proxy service, and raw assets stored in AWS S3.  
- **On‑the‑fly transformations**: images were resized and converted at request time, leading to repeated processing.  
- **Scraper & traffic tax**: RSS readers, crawlers, and aggressive bots bypassed cache keys, causing constant re‑fetches and re‑optimizations.  
- **Egress fees**: each cache miss forced a fetch from S3, incurring high cloud egress costs.  
- **Transformation pricing**: premium CDNs charged per thousand processed images, inflating costs with millions of active posts.  
- **Operational friction**: multiple providers meant complex header configs, CORS issues, and scattered routing rules, increasing debugging time.

## Why bunny.net Was Chosen  
- Personal familiarity: the author had used bunny.net successfully in many side projects, appreciating its clean developer experience.  
- **Bunny Optimizer & Perma‑Cache**:  
  - Dynamic image transformation via simple query parameters, auto‑negotiating WebP/AVIF, reducing file size up to 80 % without quality loss.  
  - Perma‑Cache permanently stores optimized variants at the edge, eliminating repeat origin fetches and eradicating egress fees.  
- **Edge Scripting**:  
  - Runs TypeScript/JavaScript at the edge (Deno/V8), providing lightweight, type‑safe middleware.  
  - Replaces custom Rails image proxies and complex URL‑building logic, keeping view code clean.

## Implementation in Forem  
- Forem’s image pipeline is built around a pluggable `Images::Optimizer` service, allowing any CDN provider to be swapped via a strategy pattern.  
- Adding bunny.net involved creating a `BunnyProvider` that maps standard parameters (width, height, fit, gravity) to bunny.net’s URL format.  
- The service continues to abstract the provider, so view templates call a unified helper without caring about the underlying CDN.

## Results and Benefits  
- **Cost reduction**: bandwidth and egress fees dropped to a fraction of previous spend.  
- **Performance gains**: optimized images are served directly from edge storage, reducing latency and load on origin servers.  
- **Operational simplicity**: single CDN for media, unified configuration, and removal of multi‑CDN header/CORS complexities.  
- **Scalability**: edge scripting and perma‑cache handle scraper spikes gracefully, preventing costly recomputation.  
- **Developer experience**: clean TypeScript edge scripts and a plug‑and‑play optimizer keep the Rails monolith focused on core business logic.