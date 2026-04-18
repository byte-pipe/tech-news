---
title: GitHub - aaddrick/claude-desktop-debian: Claude Desktop for Debian-based Linux distributions · GitHub
url: https://github.com/aaddrick/claude-desktop-debian
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-04-18T11:38:04.305942
---

# GitHub - aaddrick/claude-desktop-debian: Claude Desktop for Debian-based Linux distributions · GitHub

**Claude Desktop Documentation**
==========================

**Overview**
------------

Claude Desktop is a Linux distribution that provides a native user experience for Windows applications on Linux systems. This documentation provides an overview of the project, including its purpose, features, and usage.

**Purpose**
----------

The primary goal of Claude Desktop is to provide a convenient and easy-to-use way to run Windows applications on Linux-based systems without relying on virtualization or Wine.

**Key Features**
----------------

* **Native Linux Support**: Run Claude Desktop directly on Linux without the need for virtualization or Wine.
* **MCP (Model Context Protocol) Support**: Full support for MCP, which enables full model context protocol integration into the desktop environment.
* **System Integration**: Global hotkey support and system tray integration, allowing for seamless execution of actions from within the application.

**Usage**
---------

To use Claude Desktop, follow these steps:

1. **Install the APT Repository**: Add the repository containing the Claude Desktop package to your Linux distribution's package index.
2. **Create a Configuration File**: Modify the `~/.config/Claude/claude_desktop_config.json` file to configure any desired settings.
3. **Launch the Application**: Run the `claude-desktop --doctorto` command from within the desktop application to access its configuration options and features.

**Installation**
--------------

The Claude Desktop project includes two main files:

* `build.sh`: A build script that compiles the application for various Linux distributions.
* `flake.lock`: A flake file that defines the dependencies required by the application.

To install Claude Desktop, follow these steps:

1. **Clone the Repository**: Clone the repository containing the Claude Desktop codebase into your Linux distribution's repository.
2. **Build the Application**: Run the `build.sh` script to create a compiled version of the application for your target Linux distribution.
3. **Launch the Application**: Run the `.claudedesktopconfiginit.sh` script and access the desktop application by running `claude-desktop --doctorto`.

**Notes**
--------

* This is an unofficial build script, so please visit Anthropic's website for official support and issue reporting.
* The CPU backend is currently non-functional on Linux due to issues with validation checks. Use the bubblewrap backend instead, which mounts your home directory as read-only.