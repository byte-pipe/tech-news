---
title: What Happens When You Run `npm run dev` - DEV Community
url: https://dev.to/lovestaco/what-happens-when-you-run-npm-run-dev-ae9
date: 2026-05-19
site: devto
model: llama3.2:1b
summarized_at: 2026-05-21T12:12:34.235208
---

# What Happens When You Run `npm run dev` - DEV Community

Here's a concise and informative summary of the article:

**Introduction to npm Run Dev**

You've run `npm run dev` approximately 1,000 times - it should make sense now. Here's an overview of what happens behind the scenes:

* ** npm Setup**: npm sets up your Node.js environment with the right dependencies.
* **npm Spawns a Child Process**: npm adds your package to PATH and spawns a child process that runs `vite`, a modern web development script for Vite.
* **Vite Bootstraps**: Vite reads your `vite.config.js` (or `.ts`) file, registers plugins, and performs pre-processing on dependencies using Go.

**Vite's Development Process**

1. **Builds ES Modules**: `vite.compile()` converts CommonJS dependencies to ESM modules.
2. **Saves Cache**: Vite caches compiled modules for fast subsequent requests.
3. **Starts HTTP Server**: Vite spawns a Node.js HTTP server listening on port 5173.

**Internal Module Graph**

1. **Module Resolution**: The browser fetches each file individually using `script type="module"`.
2. **Graph Traversal**: Each requested file builds the internal module dependency graph, which is lazy and only includes nodes that are necessary for the current request.
3. **Serves Modules as ES Modules**: Vite serves each requested file as a native ES Module to the browser.

Overall, `npm run dev` allows you to quickly develop and test your web applications with minimal setup and infrastructure changes. The article assumes some familiarity with Node.js, JavaScript, and HTTP servers, but still provides a solid understanding of how npm Run Dev works its magic behind the scenes.