---
title: "GitHub - SimoneAvogadro/android-reverse-engineering-skill: Claude Code skill to support Android app's reverse engineering · GitHub"
url: https://github.com/SimoneAvogadro/android-reverse-engineering-skill
date:
site: github
model: llama3.2:1b
summarized_at: 2026-04-17T06:14:02.183202
---

# GitHub - SimoneAvogadro/android-reverse-engineering-skill: Claude Code skill to support Android app's reverse engineering · GitHub

*   **Android Reverse Engineering & API Extraction - Claude Code skill**: A Java-based reverse engineering skill that decompiles Android APK, XAPK, JAR, and AAR files and extracts HTTP APIs used by the app.
*   **Functionality**:
    *   Decompiles APK, XAPK, JAR, and AARs using `jadx` and `Fernflower/Vineflower`.
    *   Extracts and documents Retrofit endpoints, OkHttp calls, hardcoded URLs, auth headers, and tokens.
    *   Traces call flows from Activities/Fragments down to HTTP calls.
    *   Analyzes app structure: manifests, packages, architecture patterns.
*   **Requirements**:
    *   Java JDK 17+
    *   `jadx` (CLI)
*   **Installation**:
    *   Add skill via GitHub plugin
    *   Install from a local clone using Git and Claude Code
*   **Usage**:
    +   Slash command: `decompile path/to/app.apk`
    +   Natural language commands: "Decompile this APK", "Reverse engineer this Android app"
    +   Manual scripts can be used standalone, checking dependencies and installing missing ones (detects OS and package manager automatically)
