---
title: GitHub - nginx/nginx: The official NGINX Open Source repository. · GitHub
url: https://github.com/nginx/nginx
date: 
site: github
model: gpt-oss:120b-cloud
summarized_at: 2026-06-07T06:01:51.710283
---

# GitHub - nginx/nginx: The official NGINX Open Source repository. · GitHub

# NGINX Repository Overview

## How it works

- **Modules**  
  - Core functionality is extended by individual modules.  
  - Modules can be built as static (compiled into the binary) or dynamic (loaded at runtime).  
  - Use `nginx -V` to list static modules included in a binary.

- **Configurations**  
  - NGINX is configured via text‑based files containing directives.  
  - Available directives depend on the modules compiled or loaded.

- **Runtime architecture**  
  - A master process reads configuration and manages worker processes.  
  - One or more worker processes handle client requests.  
  - The number of workers can be fixed or auto‑scaled to CPU cores.  
  - Shared memory is used for inter‑process data such as rate‑limiting counters.

## Downloading and installing

- **Stable vs. Mainline binaries**  
  - Stable: built from stable branches, includes only critical fixes.  
  - Mainline: built from the master branch, contains latest features and bug fixes.

- **Linux installation**  
  - Add the official NGINX repository to the system’s package manager.  
  - Install and verify packages using the native package manager.  
  - Future upgrades are handled through the same manager.

- **FreeBSD installation**  
  - Follow the official NGINX documentation at https://nginx.org/en/docs/install.html.

- **Windows executables**  
  - Available for both stable and mainline releases.  
  - Intended for development and testing; the Windows build is still proof‑of‑concept.

- **Dynamic modules**  
  - Supported since version 1.9.11.  
  - Can be installed and configured after the core binary is built.  
  - Official dynamic module packages are distributed from the same repository.  
  - Example: the `njs` module adds JavaScript scripting capabilities.

## Getting started with NGINX

- **Beginner’s Guide** – introductory material for new users.  
- **SSL/TLS** – configure HTTPS servers to enable secure traffic.  
- **Load balancing** – set up NGINX as an HTTP load balancer.  
- **Rate limiting** – control request rates using shared memory zones.  
- **Building from source**  
  - Install build dependencies.  
  - Clone the repository, configure the build, compile, and install.  
  - Test the installed binary and report issues or contribute code.  

## Additional resources

- Full NGINX documentation includes detailed installation, configuration, debugging, and module references.  
- Support, security policies, contribution guidelines, and changelog are provided in the repository files.