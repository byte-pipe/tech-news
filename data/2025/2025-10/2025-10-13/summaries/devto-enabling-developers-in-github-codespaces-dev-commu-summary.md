---
title: Enabling developers in GitHub Codespaces - DEV Community
url: https://dev.to/fastly/enabling-developers-in-github-codespaces-1l3a
date: 2025-10-07
site: devto
model: llama3.2:1b
summarized_at: 2025-10-13T11:17:34.290957
screenshot: devto-enabling-developers-in-github-codespaces-dev-commu.png
---

# Enabling developers in GitHub Codespaces - DEV Community

**Using GitHub Codespaces for Developer Enablement**

* Replace Glitch-based onboarding projects with Compute platform implementation
* Eliminate local tooling installation requirements for learners
* Learn how to use codespaces in development activities without installing anything locally

**Overview of Codespace Features**

* Install dependencies and run an app automatically using bash scripts
* View app UI previews in the codespace
* Deploy apps via button clicks with bash scripts
* Hide UI elements to minimize distractions

**Key Takeaways:**

* A codespace is a web editing environment within GitHub, running in a Docker container
* Codespaces allow development activities without installing anything locally
* Container spec allows specifying dependencies and lifecycle events (e.g., installation of NPM packages)
* Codespaces support previewing apps and exposing them through ports

**Container Spec Examples:**

* Node.js (targeting JavaScript projects) with npm installation and package script execution
* Simple Browser for running local apps and mapping to specific ports
