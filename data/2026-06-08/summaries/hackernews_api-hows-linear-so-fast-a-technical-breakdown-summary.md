---
title: "How's Linear so fast? A technical breakdown"
url: https://performance.dev/how-is-linear-so-fast-a-technical-breakdown
date: 2026-06-08
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-06-08T11:02:38.325465
---

# How's Linear so fast? A technical breakdown

# How's Linear so fast? A technical breakdown

## What the article covers
- Using a browser‑side database (IndexedDB) as the primary data source  
- Techniques to make the first load feel instant  
- Overview of Linear’s sync engine  
- Design decisions aimed at speed  
- Role of animations  

## Database in the browser
- Linear stores data locally in IndexedDB; UI reads from this store instead of waiting for server responses.  
- Mutations are applied instantly to an in‑memory MobX observable, then queued for asynchronous sync with the server.  
- This “local‑first” approach removes visible network latency, eliminating spinners and loading states.  
- Optimistic updates (e.g., with SWR or TanStack Query) achieve similar results, but Linear built a custom sync engine to batch and flush transactions efficiently.  
- Core principle: UI responsiveness should depend on local state changes, not on round‑trip time to the backend.  

## Stack overview
### Frontend
- React + react‑dom  
- MobX for observable state graph  
- TypeScript (single language)  
- Rolldown‑Vite (current bundler) with plugin‑react‑oxc  
- ProseMirror + y‑prosemirror (rich‑text, Yjs CRDT)  
- Radix UI primitives, Emotion + StyleX (atomic CSS)  
- Comlink (worker RPC)  
- idb (IndexedDB wrapper)  
- graphql‑request (GraphQL transport)  
- Sentry, Inter Variable font  

### Backend
- Node.js + TypeScript  
- PostgreSQL on Cloud SQL (highly partitioned issues table)  
- Memorystore Redis (event bus, cache, sync cursors)  
- turbopuffer (vector DB for similar‑issue detection)  
- Kubernetes on GCP (one workload per concern)  
- Cloudflare Workers (multi‑region edge proxy)  

### Other clients
- Desktop: Electron (same web code)  
- Mobile: native Swift (iOS) and Kotlin (Android) re‑implementations  

### Marketing site
- Next.js (static)  
- styled‑components, inline SVG sprite  

- Linear deliberately stays with client‑side rendering (CSR); the simplicity of a fully client‑side app avoids server‑client mental‑model complexity and contributes to perceived speed.  

## Making the first load feel instant
- Initial load bottlenecks: HTML → JS/CSS download → authentication → API calls.  
- Linear iterated its build pipeline four times (Parcel → Rollup → Vite → Rolldown) to shrink shipped assets.  
- Reported improvements after the latest migration:  
  - 50 % less code shipped  
  - 30 % smaller bundle after compression  
  - Cold‑cache page loads 10–30 % faster  
  - Time‑to‑first‑paint of the active‑issues view reduced by 59 %  

These engineering choices—local‑first data handling, aggressive bundle optimization, and a lean client‑only architecture—combine to give Linear its characteristic millisecond‑level responsiveness.