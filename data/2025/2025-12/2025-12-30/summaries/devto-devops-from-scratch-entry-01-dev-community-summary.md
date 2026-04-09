---
title: DevOps From Scratch: Entry #01 - DEV Community
url: https://dev.to/maame-codes/devops-from-scratch-entry-01-47pm
date: 2025-12-26
site: devto
model: llama3.2:1b
summarized_at: 2025-12-30T11:08:25.162733
screenshot: devto-devops-from-scratch-entry-01-dev-community.png
---

# DevOps From Scratch: Entry #01 - DEV Community

## Linux Foundation: The "Cockpit" of the Cloud
### An Introduction to Linux and DevOps
Linux has been widely used for several decades, with its versatility extending beyond the operating system itself. This passage is an introduction to starting a new journey into Linux development.

### Key Features and Terminology

* **DevOps**: A field that combines development, operation, and maintenance of software systems.
* **Linux OS**: The core application running on the computer hardware.
* **Docker Container, AWS Instance**: Examples of how Docker containers are used in various environments.
* **Kubernetes Node**: An instance of a Kubernetes node where applications run.

### Linux File Hierarchy System (FHS)
The FHS is an open-standard organization's model for organizing a file system. Everything on the system can be categorized into files with specific places of location.

- **/bin and /usr/bin**: Executable tools.
- **/etc**: Important configuration files.
- **/var/log**: Critical error log files.
- **/tmp**: Temporary data storage.

### The Pipe Philosophy
Pipes allow for the combination of commands in a sequence. When used, they enable connection between applications or between system services.

| **Operation** | **Function** |
| --- | --- |
| > | Appends output to a file overwriting it completely (replaces content). |
| << | Overwrites input but doesn't remove existing data entirely (appends new information). |
| | Pipes connections between commands, allowing for sequential execution of tasks. |

This passage provides comprehensive introduction to Linux fundamentals and its application in DevOps practices.
