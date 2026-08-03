---
title: "Octane — React's programming model, compiled"
url: https://octanejs.dev
date: 2026-08-03
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-08-04T06:01:57.867369
---

# Octane — React's programming model, compiled

# Octane — React’s programming model, compiled

## Core concepts
- Successor to Inferno, built around performance with a compiler‑first architecture.  
- Eliminates the virtual DOM, rules of hooks, and manual dependency arrays; the compiler automatically tracks usages.  
- Hooks, memo, context, portals, transitions, actions, controlled forms and Suspense are all supported.  
- Templates compile to cloned DOM nodes that are updated directly; keyed lists move only the necessary nodes.  

## Hook usage
- Hooks can be placed inside conditions or after early returns because the compiler infers dependencies.  
- Example (`Counter.tsrx`) shows `useEffect` inside an `if (!props.paused)` block without explicit dependency array.  
- The compiler infers `[count]` for the effect automatically.  

## Concurrency and rendering
- Independent `use()` calls start concurrently, allowing nested fetches to begin earlier.  
- Streaming SSR streams each boundary as soon as it is ready.  

## Migration from React
- Octane components remain plain functions with props, hooks and context, preserving familiar data flow.  
- Existing `.tsx` files can be converted to `.tsrx` incrementally; the component model does not require redesign.  
- `OctaneCompat` enables a React 19 app to render compiled Octane islands, preserving native events, React context, SSR and hydration.  
- Only React Server Components are not directly compatible; other features (hooks, Suspense, context) carry over.  

## Signals decision
- Signals can be used but are not the foundation; Octane keeps components as plain top‑to‑bottom functions, letting the compiler handle bookkeeping.  
- Benchmarks show Octane remains competitive even against signal‑based frameworks.  

## Ecosystem
- 53 first‑party bindings cover state, data, routing, UI, forms, charts, 3D, etc.  
- Example: `@octanejs/three` ports React Three Fiber for live Three.js scenes that load on scroll.  

## Performance overview
- Over 11,500 test executions across compiler, runtime, SSR and bindings; 3,900+ distinct cases in the core suite.  
- Benchmark table (geometric mean relative to Octane = 1×) highlights:
  - Octane is the baseline; most frameworks are slower (e.g., React 19 ≈ 2.9× slower overall).  
  - Solid, Svelte and Ripple are closer to Octave performance in several suites.  
  - In signal‑favoring workloads, Octane is slower than dedicated signal frameworks but still within a competitive range.  

## Getting started
- Install Octane, write components in `.tsrx`, or use `OctaneCompat` to integrate with an existing React codebase.  
- Review migration examples such as the `App.tsx` snippet that wraps a compiled `Counter` island with `<OctaneCompat>`.  

## Summary
- Octane offers a familiar React‑style API while removing virtual‑DOM overhead and manual hook rules through compile‑time analysis.  
- It enables incremental migration, extensive first‑party bindings, and competitive performance across a wide range of benchmarks.