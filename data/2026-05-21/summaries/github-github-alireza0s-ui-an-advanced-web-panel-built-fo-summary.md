---
title: GitHub - alireza0/s-ui: An advanced Web Panel • Built for SagerNet/Sing-Box · GitHub
url: https://github.com/alireza0/s-ui
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-05-21T12:06:34.007058
---

# GitHub - alireza0/s-ui: An advanced Web Panel • Built for SagerNet/Sing-Box · GitHub

# s-ui Overview and Quick Start Guide
===============

## Introduction

s-ui is an advanced Web Panel built on SagerNet/Sing-Box, designed for personal learning and communication. This project is primarily intended for educational purposes only.

## Installation
------------

### Linux/macOS Install

To install the latest version of s-ui using Docker, run the following commands:

```bash
bash <(
curl -Ls https://raw.githubusercontent.com/alireza0/s-ui/master/install.sh
)
```

Alternatively, to install a specific legacy version, add the desired version to the end of the installation command:
```bash
VERSION=1.0.0 bash <(
curl -Ls https://raw.githubusercontent.com/alireza0/s-ui/VERSION/install.sh
)
```
### Windows Installation

To install s-ui using Docker on Windows:

1. Download the latest Windows release from GitHub Releases.
2. Extract the ZIP file to your Windows directory.
3. Run `install-windows.bat` as administrator.
4. Follow the installation wizard.

## Usage and Navigation
----------------------

The s-ui panel allows for branching, labeling of files in folders, code navigation, and execution of scripts and batch files (runSUI.sh).

### Branches

To create a new branch:

* Go to `Branches`
* Click on the branch you wish to edit

### Files/Media

* Navigate to file locations: main, api, cmd
* View Last commit message and date
* Open more actions menu to explore commands (e.g., git log)

## Development/Contribution
-------------------------

### Committing Changes

Use `git commit` to update your local repository. For versioning details, refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file.

### Running and Monitoring s-ui

To execute scripts (runSUI.sh), navigate to the corresponding directory and run:
```bash
./runSUI.sh
```
For more information on monitoring progress, check out the [Dockerfile.frontend-artifact.yml](docker-build-test.sh) file.