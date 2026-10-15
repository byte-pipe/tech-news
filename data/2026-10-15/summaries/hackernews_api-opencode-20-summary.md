---
title: OpenCode 2.0
url: https://anoma.ly/notes/opencode-2-0/
date: 2026-10-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-15T15:37:11.644663
---

# OpenCode 2.0

**OpenCode 2.0: A Major Overhaul**

The latest version of OpenCode introduces several new features, improvements, and bug fixes, including:

* Automatic server run as a single background process on the client machine
* Fixing flaky test cases
* Adding dark mode support
* Enhancing review and testing functionality

**Key Highlights:**

* The service now runs automatically in a single background process
* New clients have been added, supporting vanilla JavaScript and effect-based functionality
* Improved testing and review features

### The Service Now Runs Automatically

The OpenCode server now automatically runs as a single background process in the client machine. This has several benefits:

* **Improved Performance**: The server can serve files without interruption
* **Reduced Load on Loaders**: The server can handle file uploads without requiring a separate load process

### New Clients and Features

* **New Client Package**: A new client package has been shipped with the OpenCode software, supporting vanilla JavaScript and effect-based functionality
* **Improved Test Cases**: New clients have been added to support working with new test scenarios

### API Improvements

* **New API**: The OpenCode server supports a new **`worktree_create`** endpoint, which can be used to create new worktrees
* **Improved Error Handling**: The server now handles flaky test cases by quarantining them and reopening them in the future
* **Rate Limiting**: The server now supports rate limiting for uploads

### Additional Enhancements

* **Improved Tab Management**: The server now can interrupt and close a tab, as well as request it to do so
* **Enhanced Review and Testing**: New features have been added to support working with new review and testing scenarios

### Configuration Update

* **New Configuration Loader**: A new configuration loader has been added to improve load times

**Next Steps**

* **Test and Verify**: Further testing and verification should be performed to ensure all features and improvements are working as intended
* **Update Documentation**: Updated documentation should be created to reflect new features and improvements