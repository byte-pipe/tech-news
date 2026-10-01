---
title: 'iOS - Testing! :-D · Issue #5421 · streetcomplete/StreetComplete · GitHub'
url: https://github.com/streetcomplete/StreetComplete/issues/5421
site_name: hackernews_api
content_file: hackernews_api-ios-testing-d-issue-5421-streetcompletestreetcompl
fetched_at: '2026-10-01T17:18:11.700729'
original_url: https://github.com/streetcomplete/StreetComplete/issues/5421
author: Snowly
date: '2026-10-01'
description: 'This ticket is something like the master ticket to coordinate development on an iOS port of StreetComplete. It replaces #1892 which also included a lot of discussion and research / observation work. TLDR: Have a look at the Project Board...'
tags:
- hackernews
- trending
---

streetcomplete

 

/

StreetComplete

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork457
* Star4.9k

# iOS - Testing! :-D#5421

Open
11 / 11
11 of 11 issues completed
Open
iOS - Testing! :-D
#5421
11 / 11
11 of 11 issues completed
Labels
iOS
Concerning iOS only
Concerning iOS only

## Description

westnordost
opened 
on Dec 20, 2023
Issue body actions

This ticket is something like the master ticket to coordinate development on an iOS port of StreetComplete. It replaces#1892which also included a lot of discussion and research / observation work.

### TLDR: Have a look at theProject Boardfor a list of tasks. Contributions are welcome!

Also have a look at theSlides from SotM Europe 2024 talk(I added speaker notes to make this understandable when flipping through).

# Approach

The code base of this app is written in 100% Kotlin, a modern programming language that is quite similar to Swift. Kotlin code can be transpiled to JavaScript and also to machine code, just like Swift. Furthermore, many dependencies of this app by now are pure Kotlin libraries.

An iOS version of this app hence can be done withKotlin Multiplatform.

The UI code can be shared usingCompose Multiplatform, which is currently inalphabetafor iOS. It is a fork/extension ofJetpack Composewith largely the same API. Jetpack Compose is a reactive UI framework in which developers define the UI completely in code (similar idea as SwiftUI, Flutter, ...). We'll have to re-create the entire UI (incrementally) in Compose, though.

This will keep the amount of code that needs to be platform dependent (Android / iOS) to a minimum.

This approach has the big advantage over others in that further maintenance of this project will not increase significantly, as there will continue to be just one code base. In comparison to using the framework Flutter for multiplatform (as used byEvery Door), it allows us to largely not touch the Kotlin codebase. When using Flutter, we'd need to rewrite it all in Dart.

# Steps in a nutshell

* Separate all platform specific code from application logic. Replace Android/Java dependencies for application logic with Kotlin multiplatform dependencies
* Incrementally migrate the UI code to Compose Multiplatform:Separate data access and UI state code from pure UI code (use view models:Use ViewModels#5070)Migrate the UI code that currently uses Android XML layouts to AndroidJetpack Compose. This can be done incrementally when done bottom-up (seemigration strategy guide)Then, migrate from Jetpack Compose to Compose Multiplatform. This is a small step compared with the first one.
* Separate data access and UI state code from pure UI code (use view models:Use ViewModels#5070)
* Migrate the UI code that currently uses Android XML layouts to AndroidJetpack Compose. This can be done incrementally when done bottom-up (seemigration strategy guide)
* Then, migrate from Jetpack Compose to Compose Multiplatform. This is a small step compared with the first one.

# Current State

This section will be updated continuously.

The steps necessary are described in detail in a Kanban-styleProject Board. (Some tasks have not been created yet because they 100% depend on other tasks completed first and some research). Unless stated otherwise, they are explicitly up for the taking by people who read this and (I hope 😊) want to contribute to the development towards an iOS port. If you would like to implement one of the tasks described, comment in that ticket.

We very roughly estimated some time ago that developing a full port to iOS would take one man-year of work. So, the scope of this remains very large. We will only realistically achieve it together with lots of contributions from the community. Luckily, this is exactly what has been happening in the last years.In the first half of 2024, I have been able to work on this full-time. The migration is now about 50% complete.

So, let's shift gears!

## How you can help

* You could take over a task from the project board! Or, you could familiarize yourself with the mentioned technologies / frameworks to make meaningful contributions later. In particular: Jetpack Compose /Compose Multiplatform. This is very new to me too, so I have to find my feet here, too
* You can sponsor development! See the title "Sponsor this project" in the sidebar on the main page. More money allows me to devote more time to development on this app in general. If you know any eligible sources for larger scale funding, talk to me!
* You can help with maintenance and issue triage in general. Time saved on that is time I can put into furthering development on this!
Reactions are currently unavailable

## Metadata

## Metadata