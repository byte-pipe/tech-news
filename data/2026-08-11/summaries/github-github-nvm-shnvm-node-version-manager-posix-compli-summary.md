---
title: GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions · GitHub
url: https://github.com/nvm-sh/nvm
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-08-11T11:48:48.944408
---

# GitHub - nvm-sh/nvm: Node Version Manager - POSIX-compliant bash script to manage multiple active node.js versions · GitHub

**Node Version Manager (nvm)**

nvm is a tool for managing multiple active versions of the Node.js runtime environment. It allows developers to easily switch between different versions, making it easier to collaborate with others or try out different projects without having to worry about conflicting dependencies.

### Key Features:

* **Multiple Node Versions**: nvm supports installing and managing multiple versions of Node.js in a single installation.
* **Easy Installation**: Simply install the `nvm` tool via the npm package manager, and it will create a new directory for each version, making it easy to switch between them.
* **Convenient Commands**: nvm provides a set of commands to manage different versions, such as checking if a specified version is installed by running `nvm confirm <version>`.
* **CICD Integrations**: nvm supports Docker for Development (CICD) environments and allows developers to easily switch between different versions.

### Setup and Usage:

1. Install the `nvm` tool using npm: `npm install -g nvm`
2. Create a new directory for your project, and add an `nvm.sh` file with the following content:
```
source ~/.bash-profile
if [ \$OSTYPE == "msys" ]; then
    eval "$(nvm init)"
else
    eval "$(nvm install bash)"
fi
```
3. Add a `.env` file to your project directory and store your Node.js version in it, e.g., `node_version=14.x`.
4. Update your Shell configuration to point to the latest Node.js installer (if not using Bash). For example:
```bash
export PATH=" ~/.nvm/bin:$PATH"
```
That's it! You're now ready to use `nvm` from within your project.

### Troubleshooting:

* **Installation issues**: Try deleting the `.nvm` directory and installing nvm again.
* **Error connecting to package manager**: Ensure that the `env` file for the current operating system is properly configured (e.g., for Linux, it's `~/.bash_profile_nvm` or `~/.zprofile`).
* **Missing dependencies**: Check your `.env` file and ensure all required directories exist.