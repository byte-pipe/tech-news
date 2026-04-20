---
title: GitHub - cloudflare/workerd: The JavaScript / Wasm runtime that powers Cloudflare Workers · GitHub
url: https://github.com/cloudflare/workerd
date:
site: github
model: llama3.2:1b
summarized_at: 2026-03-17T11:39:51.368980
---

# GitHub - cloudflare/workerd: The JavaScript / Wasm runtime that powers Cloudflare Workers · GitHub

**Cloudflare's JavaScript/Wasm Runtime: Workerd**

### Overview
Workrd is a JavaScript/Wasm server runtime based on the same code that powers Cloudflare Workers. It provides an application server, development tool, and programmable HTTP proxy.

**Key Features**

* **Server-first design**: Written for servers, not Command-Line Interface (CLI) or Graphical User Interface (GUI).
* **Standard-based APIs**: Built-in APIs are based on web platform standards such as `fetch()`.
* **Nanoservices** : Split into components that are decoupled and independently-deployable like microservices, but with performance of a local function call.
* **Homogeneous deployment**: Deploy all nanoservices to every machine in the cluster, making load balancing much easier.
* **Capability bindings**: Configuration uses capabilities instead of global namespaces to connect nanoservices to each other and external resources.

**Use Cases**

* Apply Server as an application server to self-host applications designed for Cloudflare Workers.
* Use Workrd development tool to develop and test code locally.
* Programmable HTTP proxy (forward or reverse) for efficient network handling.
