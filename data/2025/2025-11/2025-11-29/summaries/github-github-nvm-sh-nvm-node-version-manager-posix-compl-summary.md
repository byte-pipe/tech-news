---
title: GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions
url: https://github.com/nvm-sh/nvm
date:
site: github
model: llama3.2:1b
summarized_at: 2025-11-29T11:11:14.516814
screenshot: github-github-nvm-sh-nvm-node-version-manager-posix-compl.png
---

# GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions

## nvm-sh: Node Version Manager - POSIX-Compliant Bash Script
===========================================================

### Overview

The `nvm-sh` package provides a Node.js version manager that enables multiple-node environments with ease. It is designed to work seamlessly in the terminal, making it a valuable tool for developers.

### Key Features

*   **Posix-compliant**: The version manager adheres strictly to POSIX (Portable Operating System Interface) guidelines, ensuring compatibility across operating systems.
*   **Node.js support**: `nvm-sh` can manage multiple active Node.js versions, making it ideal for running multiple projects or environments with different Node versions.
*   **Signed-in required**: Users must be signed in to change notification settings and update their package lists.

### License

The open-source `nvm-sh` project is released under the MIT license. This allows users to freely distribute, modify, and use the software for personal or commercial purposes.

## Installation
---------------

To install `nvm-sh`, run the following command:
```bash
# Install global repository source (optional)
curl -fsL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh |sh

# Activate nvm globally in a new terminal
source ~/.bash_profile || . /opt/homebrew/bin/zshrc

# Confirm installation and create user group for the service to manage multiple versions of Node
nvm install <version> && nvm users add <username>
```
This process can take around 5-10 minutes.

### Initial Setup and Navigation
-----------------------------------

*   Once installed, `nvm` will guide you through a terminal navigation wizard-style prompts.
*   Create different branches using the following command:
    ```bash
# Navigate to a different Node version
nvm use <version>
```
This enables multiple-node environments with ease. To deactivate and return to the default Node setup, simply run `nvm deactivation` in a new terminal window.

### Example Use Cases
---------------------

*   **Project Setup**: Create multiple new directories for your projects to manage each under their own version of Node.js.
*   **Version Management**: Switch between active versions as needed without affecting dependencies or package lists.

By following these steps and key points, `nvm-sh` becomes a convenient and efficient tool for managing Node.js versions in the terminal.
