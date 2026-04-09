---
title: Enabling developers in GitHub Codespaces - DEV Community
url: https://dev.to/fastly/enabling-developers-in-github-codespaces-1l3a
date: 2025-10-07
site: devto
model: llama3.2:1b
summarized_at: 2025-10-08T11:17:49.559020
screenshot: devto-enabling-developers-in-github-codespaces-dev-commu.png
---

# Enabling developers in GitHub Codespaces - DEV Community

**Enabling Developers with GitHub Codespaces: A Guide**

GitHub Codespaces enable developers to explore and develop applications without downloading or installing anything locally. Here's a summary of key points:

* **Codespace Overview**: A codespace is a web editing environment that uses the VS Code editor, allowing for development activities in the cloud.
* **Getting Started**: Access codespaces from GitHub by clicking on the "Codebutton" on a specific branch.
* **Features**:
	+ Automatic dependency installation and app setup
	+ Preview app UI in the codespace
	+ Bash script deployment at the click of a button
	+ Customization options: hide UI elements, display custom buttons
* **Containerization**: Codespaces run in Docker containers, specifying dependencies from repo content.

**Technical Details**

* **Container Config**: Specified container metadata to configure app execution and setup tasks.
* **Post-Attach Command**: Runs commands at startup to install NPM packages and execute scripts.
* **Ports**: Expose apps through specific ports using the Simple Browser.

The post also covers additional features such as:

*   Using Visual Studio Code 2019.1 or later with a custom Docker image
*   Accessing codespaces from within an existing VS Code project
