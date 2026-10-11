---
title: Migrating a Real TypeScript OSS Library from tsup to tsdown 🔧 - DEV Community
url: https://dev.to/nyaomaru/migrating-a-real-typescript-oss-library-from-tsup-to-tsdown-5b80
date: 2026-10-07
site: devto
model: gpt-oss:120b-cloud
summarized_at: 2026-10-12T06:01:19.510656
---

# Migrating a Real TypeScript OSS Library from tsup to tsdown 🔧 - DEV Community

# Migrating a Real TypeScript OSS Library from tsup to tsdown

## Why migrate a package that already builds correctly
- is‑kit is a zero‑dependency TypeScript library for runtime type guards.  
- The existing build used **tsup** and was stable, but maintenance concerns motivated a move to **tsdown**, which is built on Rolldown, has an active ecosystem, and is positioned as a migration path from tsup.  
- The core question was: *Can the build be switched to tsdown without changing what existing consumers receive?*

## Package contract that needed to be preserved
- The library exposes explicit exports in `package.json`:
  ```json
  {
    "exports": {
      ".": {
        "types": "./dist/index.d.ts",
        "import": "./dist/index.mjs",
        "require": "./dist/index.js"
      }
    }
  }
  ```
- The migration had to keep the three files `dist/index.mjs`, `dist/index.js`, and `dist/index.d.ts` unchanged, together with:
  - identical ESM/CJS runtime behavior  
  - declaration compatibility and banner  
  - the same export set  

## Migration steps (almost trivial)
- Removed `tsup` and installed `tsdown`.  
- Replaced `tsup.config.ts` with `tsdown.config.mts` (using `.mts` to avoid Node treating the config as a module).  
- Mapped most options directly:
  - `entry: ["src/index.ts"]`
  - `format: ["esm","cjs"]`
  - `dts: true`
  - `clean: true`
  - `outDir: "dist"`
  - `target: "esnext"`
  - `banner: { dts: dtsBanner }`

## First build succeeded but broke the contract
- tsdown produced files:
  - `index.mjs`, `index.cjs`, `index.d.mts`, `index.d.cts`
- The original `package.json` still pointed to `dist/index.js` and `dist/index.d.ts`, which no longer existed.  
- Publishing at this point would have broken CJS consumers and TypeScript resolution.  
- Lesson: a successful build does **not** guarantee that the published package contract is preserved.

## Fixing the public contract without changing extensions
- Used `outExtensions` (renamed from `outExtension` in tsdown) to map formats to the original filenames:
  ```ts
  outExtensions: ({ format }) => ({
    dts: format === "cjs" ? ".d.ts" : ".d.mts",
    js: format === "cjs" ? ".js" : ".mjs"
  })
  ```
- Resulting output matched the original contract:
  - `dist/index.mjs`
  - `dist/index.js`
  - `dist/index.d.mts`
  - `dist/index.d.ts`
- The change is not a tsdown bug; tsdown chooses sensible defaults based on package type, but existing packages must retain their established filenames.

## Verifying the published package with a smoke test
- Existing `npm test:package` script builds, packs, installs the tarball in a temporary project, and runs consumer‑level checks.  
- After migration, the test was expanded to validate:
  - Export paths for `import`, `require`, and `types`  
  - Zero runtime dependencies  
  - Same number of ESM and CJS exports (83)  
  - Preservation of the declaration banner  
  - Successful runtime import/require  
  - Compatibility with TypeScript versions 5.7 through 7.0  
- All checks passed, confirming that the artifact users install remains unchanged.

## Output size comparison
| Metric | tsup | tsdown | Difference |
|--------|------|--------|------------|
| JS + dts total | 116,503 B | 144,007 B | +23.6 % |
| ESM JavaScript | 15,787 B | 29,410 B | +86.3 % |
| CJS JavaScript | 19,318 B | 31,155 B | +61.3 % |
| dts (one format) | 40,699 B | 41,721 B | +2.5 % |
| npm pack tarball | 37,226 B | 42,366 B | +13.8 % |
- tsdown retained more comments and region markers, leading to larger bundles.

## Takeaways
- When migrating a published library, the **package contract** (filenames, export map, declaration banner) is more important than the mere success of the build.  
- Use `outExtensions` to keep legacy filenames when the bundler’s defaults differ.  
- A **smoke test that packs and installs the artifact** is essential to catch contract regressions before publishing.  
- Expect some increase in bundle size with tsdown due to richer output metadata, but the trade‑off can be worthwhile for maintainability and ecosystem support.