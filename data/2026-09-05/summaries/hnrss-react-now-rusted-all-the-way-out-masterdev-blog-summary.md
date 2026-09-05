---
title: React Now Rusted All The Way Out – Master.dev Blog
url: https://blog.master.dev/react-now-rusted-all-the-way-out/
date: 2026-09-04
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-09-05T10:36:19.262518
---

# React Now Rusted All The Way Out – Master.dev Blog

# React Now Rusted All The Way Out – Summary

## Performance Gains
- Official Rust React Compiler support released on August 4 2026 (oxc team).  
- Switching a 1,036‑file React Router codebase (Outlyne) to the Rust compiler yielded a **~17.6×** speedup for the compiler stage (14.3 s → 0.81 s, single‑threaded).  
- Overall build time improved **~2.4×** (22.1 s → 9.3 s) because other build steps remain unchanged.  
- Faster builds reduce CI minutes cost and improve developer experience.

## Compiler Limitations & New Support
- New Rust compiler version resolves several previous Babel‑based limitations:  
  - Conditional logic inside `try/catch` blocks.  
  - Reassigning destructured component props used in nested closures.  
  - Computed object property keys.  
- These fixes added compatibility for **seven** additional functions in the app.  
- Remaining unsupported patterns: `throw` inside a `try` block and logical assignment operators (`??=`, `&&=`, `||=`).  
- Future fixes will arrive automatically with the Rust compiler, unlike the stagnant Babel version.

## Toolchain Consistency
- Both linter (Oxlint) and build now use the exact same React Compiler version, eliminating mismatches where a component could be unoptimized without lint warnings.  
- Consistent feature support across tooling prevents “coverage gaps” in production builds.

## Migration Guide

### Using `@vitejs/plugin-react` (Vite v8+)
1. Install the native compiler package:  
   ```bash
   npm install -D oxc-transform-react
   ```
2. Update `vite.config.js` to enable the compiler:  
   ```javascript
   import { defineConfig } from "vite";
   import react from "@vitejs/plugin-react";

   export default defineConfig({
     plugins: [react({ compiler: true })],
   });
   ```
3. Remove `@rolldown/plugin-babel` and related Babel config from the project.

### Without `@vitejs/plugin-react` (e.g., React Router Framework Mode)
1. Install the minimal Vite plugin:  
   ```bash
   npm install -D @acusti/vite-plugin-react-compiler
   ```
2. Replace the previous Babel‑based setup with the new plugin:  
   ```javascript
   import { defineConfig } from "vite";
   import reactCompiler from "@acusti/vite-plugin-react-compiler";
   import { reactRouter } from "@react-router/dev/vite";

   export default defineConfig({
     plugins: [reactRouter(), reactCompiler()],
     // optional custom config:
     // reactCompiler({ compiler: { /* your config */ } })
   });
   ```
3. Remove `vite-plugin-babel`, `babel-plugin-react-compiler`, and `@babel/preset-typescript` from `devDependencies`.

## Overall Benefits
- **Significant compile‑time reduction** translates to cheaper CI and happier developers.  
- **Expanded language support** removes previous blockers, enabling more idiomatic React code.  
- **Unified tooling** ensures linting and compilation stay in sync, preventing silent regressions.  
- Migration steps are straightforward and result in a cleaner, faster build pipeline.