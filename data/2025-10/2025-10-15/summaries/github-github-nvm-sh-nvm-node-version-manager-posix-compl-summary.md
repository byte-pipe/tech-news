---
title: GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions
url: https://github.com/nvm-sh/nvm
date:
site: github
model: llama3.2:1b
summarized_at: 2025-10-15T11:14:16.662184
screenshot: github-github-nvm-sh-nvm-node-version-manager-posix-compl.png
---

# GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions

*   **Introduction**: `nvm-sh` is a Node.js version manager that provides easy management of multiple active node.js versions, allowing users to switch between them with ease.
*
*   **MIT License**: The software is distributed under the MIT license, which allows for free use and modification without any restrictions.
*

### User Experience

#### Installation
*   To install `nvm-sh`, run:
    ```bash
npm install -g nvm-sh
```
*   This command downloads and installs the `nvm-sh` client globally.

#### Initial Setup
*   Run `nvm init --color` to set up a new virtual node with the requested architecture.
*   You can also upgrade existing nodes without logging out by specifying the specific version when running `nvm self-upgrade <version>`:
    ```bash
nvm self-upgrade 14.17.0
```
#### Managing Node Versions
*   To create a temporary new node, use `nvm install <npm-version>`.
*   Use `nvm use <new-npm-version>` to switch to the installed client with the specified npm version.
*   You can also create an alias for common packages by running `--global` after installing nodes:
    ```bash
nvm install my-new-npm-version --global
```
*   The following example demonstrates the new node manager:

    ```markdown
# nvm

### Hello from nvm!

# Installing Node.js to our system
  # npm package manager
## Create a Node.js version manager (via npm)
> npm install -g nvm-sh

### Install nvm globally and upgrade existing nodes
To create an initial Node.js version manager:
*   Run `nvm init --color`
*   To upgrade all existing nodes with a particular minor release (`npm <version>`, e.g., `npm 14.17.0 upgrade`) on your host system.

### Initial Setup

# Using the nvm client globally
To switch your current Node.js version quickly, install and enable it via npm:
```bash
# Run this command after installing nvm
nvm self-upgrade <version>

# Example: Switching to v14.17.0 of NVM.
```
After enabling a global `nvm` for a specific user (e.g., as `user1`), you can run the following commands:
```bash
nvm install 14.17.0
nvm use 14.17.0
nvm global upgrade <version>
```

### Switching nodes

*   Use the command `(nvm default <version>)`
*   You can also switch directly to a virtual "node" via `nvm alias` or simply by running (without using nvm with npm) `my-version`.
*    To use multiple versions, keep them separate in different directories. For instance:
        ```bash
mkdir -p ~/.nvm
cd ~/.nvm
npm install nvm@latest
```

### Customizations

*   To change the package.json and .env files using npm's commands for a specific node installed with `nvm`, you can run these commands from within your user directory:
    ```bash
npm install -g npmconfig
```
        This generates the global NPM configuration script based upon what we initially set up

### Testing Conventions

*   For local development, use `nvm` to check if running as the root-user.
*
### Troubleshooting**

#### Installing Node.js using NVM

*   When you encounter an error during installation, verify that your system has not reached Windows Defender exception status (`nvm install is blocked on your system`) and that npm is installed correctly.

#### Errors with nvm usage while installing packages with specific or outdated versions

*   After attempting to upgrade with `npm <version>`, which may require a package manager like apt or yum, use the following command instead (`apt` or `yum`) to install:
    ```bash
sudo apt-get update
```

#### Issues with node version when you are using an installed client with v14.17.0 while switching between different versions of npm.

You can run the following code snippet to switch from a non-upgraded Node.js 14.x installation using nvm:

```python
import subprocess

# Get current installed Node.js v14.x
v14_stdout = subprocess.run(['npm', 'config', '--global', 'node', '-version'], stdout=subprocess.PIPE, text=True)

# Get default npm version for your project.
npm_v_out = subprocess.run(['npm', 'config', '--global', 'package.json'], stdout=subprocess.PIPE, text=True)
npm_text = npm_v_out.stdout.decode('utf-8')

# Switch to the desired node.js version (14.x) when you want
v14_stdout = subprocess.run(['npm', 'config', '--global', 'node', '-version'])

npx nvm install 13.17.0 # Choose v13.x

```

## Usage Guide

### Installation

```bash
npm install -g nvm-sh
```
This step downloads and installs `nvm-sh` globally.

**Usage**

-   To switch using the default node version:

    ```bash
nvm self-upgrade <version>  # Using the nvm command line interface (CLI)
```
*   You can change to another node by running `(nvm use <version>)`.
