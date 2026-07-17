---
title: GitHub - vercel-labs/native: Toolkit for building native desktop apps · GitHub
url: https://github.com/vercel-labs/native
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-07-17T11:37:09.126628
---

# GitHub - vercel-labs/native: Toolkit for building native desktop apps · GitHub

**Native SDK Overview**
=======================

### Introduction

The Native SDK is a complete toolkit for building native desktop applications. It provides an expressive authoring model, allowing developers to create rich and interactive UI components without competing with the performance of web-based runtimes.

### Key Features

*   **Declarative markup**: View markup in `src/app.native` files binds values and dispatches messages (e.g., incrementing a counter)
*   **Native rendering engine**: The engine draws every pixel into real OS windows
*   **Deterministic reference renderer**: Captures images based on the color scheme set by the developer

### Quick Start Guide

1.  Install the CLI using `npm install -g @native-sdk/cli`
2.  Create and run a new app using `native init my_app` and then `cd my_app && native dev`

### View, Logic, Manifest Separated

The Native SDK consists of three main components:

*   **View**: The declarative markup for the UI (e.g., `src/app.native`)
*   **Logic**: The logic and state changes are handled in `src/core.ts`
*   **Manifest**: The build configuration is defined in a separate file (`build.zig`)