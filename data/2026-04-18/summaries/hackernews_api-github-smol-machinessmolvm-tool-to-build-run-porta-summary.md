---
title: GitHub - smol-machines/smolvm: Tool to build & run portable, lightweight, self-contained virtual machines. · GitHub
url: https://github.com/smol-machines/smolvm
date: 2026-04-17
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-04-18T11:44:55.726195
---

# GitHub - smol-machines/smolvm: Tool to build & run portable, lightweight, self-contained virtual machines. · GitHub

**SmolVM Overview**

* SmolVM is a lightweight, portable virtual machine (VM) that provides isolation and flexibility for running custom Linux applications.
* It allows for sub-second cold start, elastic memory usage, and seamless deployment across platforms.

**Key Features:**

1. **Isolation**: SmolVM runs independently with isolated environments, ensuring user data remains secure.
2. **Platform independence**: Works on macOS, Linux, and cross-platform platforms (macOS, Linux).
3. **Elastic memory usage**: Efficiently allocates resources based on the workload, reducing memory consumption.
4. **Portable executables**: Packs into self-contained binaries that can be run without installing dependencies.

**Installation:**

1. Clone the repository using `git clone https://example.com/smolvm`.
2. Install on macOS + Linux: `curl -sSL https://smolmachines.com/install.sh | bash`.

**Quick Start:**

1. Run a command in an ephemeral VM with `smolvm machine run --net --image <platform> -- sh -c command`
2. Interactively access the VM with `smolvm machine run --net -it --image <platform> -- /bin/sh`

**Use Cases:**

* Sandbox untrusted code
* Host filesystem, network, and credentials separation
* Lock down egress and control incoming traffic

**Network Setup:**

| Setting | Default | Configured |
| --- | --- | --- |
| Network | Off by default | Allow specific hosts only (e.g., registry.npmjs.org) |

**Packing into Executables:**

1. Create an executable package using `smolvm pack create --image <target> <packaged files>`
2. Run the packaged machine with `./python312 run -- python3 --version`
