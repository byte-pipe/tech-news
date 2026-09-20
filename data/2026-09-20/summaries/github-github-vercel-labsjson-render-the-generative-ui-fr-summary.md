---
title: GitHub - vercel-labs/json-render: The Generative UI framework · GitHub
url: https://github.com/vercel-labs/json-render
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-09-20T14:35:37.098666
---

# GitHub - vercel-labs/json-render: The Generative UI framework · GitHub

# json-render Framework Overview

### Key Points

/json-render: A Generative UI framework that uses AI to generate interfaces from natural language prompts, constrained to components defined in a catalog.
Predefined components and actions for safe, predictable output.
Features:
- Generate dynamic, personalized UIs
- Fast and progressive rendering
- Cross-platform support across web and mobile apps
- 36 pre-built components, including shadcn/ui, React, Vue, Svelte, Solid, and React Native
- Compatible with Next.js apps and 3D scenes
- Predictable, JSON output matches schematic definition

### Purpose

json-render aims to make it easier to create complex, user interfaces by leveraging artificial intelligence (AI) to guide the rendering process.

### Quick Start Guide

1. Import the necessary components and schema definitions from `@json-render/core` and `@json-render/react/schema`.
2. Define your catalog using the `defineCatalog` function.
3. Use the `schema` function to create a Zod schema from your catalog definition.
4. Combine the schema with shadcn/ui components to generate the final UI.

### Supported Integration Options

json-render is designed to work seamlessly with multiple frameworks and libraries, including:

- React and React Native
- Vue and Svelte
- SolidJS
- Next.js apps
- Video rendering
- PDF documents
- HTML email
- Vue 3D scenes
- Ink UI
- Next.js full-stack apps
- 3D scenes using React Three Fiber or React Three Drei

By following the provided Quick Start Guide and using the supported integration options, developers can create complex, user interfaces using the json-render framework.