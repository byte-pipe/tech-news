---
title: Announcing TypeScript 6.0 - TypeScript
url: https://devblogs.microsoft.com/typescript/announcing-typescript-6-0/
date: 2026-03-26
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-03-26T01:03:00.888715
---

# Announcing TypeScript 6.0 - TypeScript

# Announcing TypeScript 6.0 – Summary

## Overview
- TypeScript 6.0 is released as the final version built on the existing JavaScript codebase.
- It serves as a bridge to the upcoming TypeScript 7.0, which will run on a new Go‑based compiler and language service.
- The release includes both alignment changes for the future and independent new features.

## Installation
- For users already familiar with TypeScript:
  ```bash
  npm install -D typescript
  ```
- The package can also be used directly in Visual Studio Code or installed from npm.

## Changes Since Beta and Release Candidate
- Improved type‑checking for function expressions in generic calls, especially in generic JSX contexts.
- Extended deprecation of the `import … assert {…}` syntax to cover `import()` calls with an `assert` option.
- Updated DOM type definitions to match the latest web standards, including adjustments to the Temporal APIs.

## New Features

### Less Context‑Sensitivity on `this`‑less Functions
- Arrow functions were already inferred correctly; method syntax previously caused “parameter of type unknown” errors due to contextually sensitive inference.
- TypeScript 6.0 now treats methods without actual `this` usage as non‑contextually‑sensitive, allowing inference to succeed.
- This change improves generic function inference and was contributed by Mateusz Burzyński.

### Subpath Imports Starting with `#/`
- Node.js now permits subpath imports that begin with `#/`, enabling a simple `#/` prefix for internal module aliases.
- Example `package.json` entry:
  ```json
  {
    "imports": {
      "#/*": "./dist/*"
    }
  }
  ```
- TypeScript now supports this pattern, simplifying import paths that previously required an extra segment (e.g., `#root/*`).

## Preparing for TypeScript 7.0
- TypeScript 7.0 is close to completion and will be based on the new Go implementation.
- Users of 6.0 are encouraged to try the native previews of 7.0 in VS Code or via npm.
- Most 6.0 changes are designed to align code and tooling with the upcoming 7.0 behavior.

## Additional Notes
- The release maintains the familiar TypeScript experience while paving the way for performance and multi‑threading improvements in future versions.
- Documentation and getting‑started guides remain available on the official TypeScript website.
