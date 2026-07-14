---
title: Building and Shipping Mac and iOS Apps Without Ever Opening Xcode
url: https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/
date: 2026-07-13
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-07-14T11:39:40.641951
---

# Building and Shipping Mac and iOS Apps Without Ever Opening Xcode

Building and Shipping Mac and iOS Apps Without Ever Opening Xcode:
=================================================================

To create and deploy Mac and iOS apps without opening the GUI of Xcodeapp is still a challenging process. However, there are shortcuts available to automate the process.

### Installing Xcode
To start, ensure that Xcode is installed properly:

*   `xcode-select` must be in the correct location for CLI tools.
    -   Check if command line toolchain is already selected: `xcode-select -p`
        -   or use `brew install xcode --cocoapaths`
        -   Note: The name "Command Line Tools" can be misleading.

### Installing XcodeGen
XcodeGen provides a separate tool for managing and generating app projects without opening the GUI of Xcode.

### Pre-Work Setup

*   **Sign in to your Apple ID**: Verify that you have an active Apple ID.
*   **Create a developer account (if not already exists)**: Sign up under the developer id used during project deployment. Only one developer ID is required for both macOS and iOS apps.

After these steps, all necessary tools can be obtained within Xcode.app:

-   `xcodebuild` executes builds automatically without requiring user interaction.
-   Notarization by xcodebuild enables automatic signing of your app, making it secure to deploy directly through the app store.

### Script-Based Deployment

The process involves writing a script to chain together steps like archive → Developer ID sign → notarize → staple → install. However, this script can be automated using `scripts/release.sh`:

*   This script is generated once and executed immediately.

### Building Process
This process is streamlined into:
1.  Creating the Developer ID certificate for signing.
2.  Notarizing your app automatically with `xcodebuild`.
3.  Stapling the signed app to Xcode.app.
4.  Installing the stapled app to Applications folder.

The script handles everything: notarization, sign-and-tap execution.

### TL;DR
Here are the key takeaways:

-   Install and ensure CLI tools such as `xcodebuild` and `find` with correct toolchain location.
-   Sign in to Apple ID for account creation (if you haven't already).
-   Follow a script that automatically deploys your app, with automated sign-and-tap generation.