---
title: iOS - Testing! :-D · Issue #5421 · streetcomplete/StreetComplete · GitHub
url: https://github.com/streetcomplete/StreetComplete/issues/5421
date: 2026-10-01
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-01T17:20:45.889605
---

# iOS - Testing! :-D · Issue #5421 · streetcomplete/StreetComplete · GitHub

**iOS - Testing! :-D**

**Overview**

The current issue is an error while loading. To resolve this, users must be signed in to change notification settings.

**Current Status**

11/11 issues completed

**Current Status by Labels**

Concerning iOS only

**Ticket Description**

The current ticket provides an overview of the issue, including its causes, impact, and solution. The user must have signed in to change notification settings.

**Approach**

The code base is written in 100% Kotlin, and Kotlin code can be transpiled to JavaScript and JavaScript code for machine code generation, but many dependencies are pure Kotlin libraries. An iOS version can be done using Kotlin Multiplatform. The UI code will be shared using Compose Multiplatform, which is currently in alpha for iOS.

**Step-by-Step Approach**

1. Separate platform-specific code from application logic and replace Android/Java dependencies with Kotlin multiplatform dependencies.
2. Incrementally migrate the UI code to Compose Multiplatform.
3. Separate data access and UI state code from pure UI code and use view models.
4. Migrate the UI code to AndroidJetpack Compose.
5. Migrate the data access and UI state code to Compose Multiplatform.

**Milestone Progress**

11/11 issues completed

**Related Projects**

1. Master Ticket to coordinate development on an iOS port of StreetComplete