---
title: 'GitHub - mobile-dev-inc/Maestro: Painless E2E Automation for Mobile and Web · GitHub'
url: https://github.com/mobile-dev-inc/Maestro
site_name: github
content_file: github-github-mobile-dev-incmaestro-painless-e2e-automati
fetched_at: '2026-03-19T11:17:35.249101'
original_url: https://github.com/mobile-dev-inc/Maestro
author: mobile-dev-inc
description: Painless E2E Automation for Mobile and Web. Contribute to mobile-dev-inc/Maestro development by creating an account on GitHub.
---

mobile-dev-inc



/

Maestro

Public

* NotificationsYou must be signed in to change notification settings
* Fork695
* Star12.1k




 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

1,521 Commits
1,521 Commits
.github
.github
 
 
.idea
.idea
 
 
.run
.run
 
 
assets
assets
 
 
e2e
e2e
 
 
gradle
gradle
 
 
maestro-ai
maestro-ai
 
 
maestro-android
maestro-android
 
 
maestro-cli
maestro-cli
 
 
maestro-client
maestro-client
 
 
maestro-ios-driver
maestro-ios-driver
 
 
maestro-ios-xctest-runner
maestro-ios-xctest-runner
 
 
maestro-ios
maestro-ios
 
 
maestro-orchestra-models
maestro-orchestra-models
 
 
maestro-orchestra
maestro-orchestra
 
 
maestro-proto
maestro-proto
 
 
maestro-studio
maestro-studio
 
 
maestro-test
maestro-test
 
 
maestro-utils
maestro-utils
 
 
maestro-web
maestro-web
 
 
recipes
recipes
 
 
scripts
scripts
 
 
.editorconfig
.editorconfig
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
RELEASING.md
RELEASING.md
 
 
build.gradle.kts
build.gradle.kts
 
 
debug.keystore
debug.keystore
 
 
detekt.yml
detekt.yml
 
 
gradle.properties
gradle.properties
 
 
gradlew
gradlew
 
 
gradlew.bat
gradlew.bat
 
 
installLocally.sh
installLocally.sh
 
 
logo.png
logo.png
 
 
maestro
maestro
 
 
settings.gradle.kts
settings.gradle.kts
 
 
tmp.sh
tmp.sh
 
 
View all files

## Repository files navigation

Tip

Great things happen when testers connect —Join the Maestro Community

Maestrois an open-source framework that makes UI and end-to-end testing for Android, iOS, and web apps simple and fast.Write your first test in under five minutes using YAML flows and run them on any emulator, simulator, or browser.

## Table of Contents

* Why Maestro?
* Getting Started
* Resources & Community
* Contributing
* Maestro Studio – Test IDE
* Maestro Cloud – Parallel Execution & Scalability

## Why Maestro?

Maestro is built on learnings from its predecessors (Appium, Espresso, UIAutomator, XCTest, Selenium, Playwright) and allows you to easily define and test your Flows.

By combining a human-readable YAML syntax with an interpreted execution engine, it lets you write, run, and scale cross-platform end-to-end tests for mobile and web with ease.

* Cross-platform coverage– test Android, iOS, and web apps (React Native, Flutter, hybrid) on emulators, simulators, or real devices.
* Human-readable YAML flows– express interactions as commands likelaunchApp,tapOn, andassertVisible.
* Resilience & smart waiting– built-in flakiness tolerance and automatic waiting handle dynamic UIs without manualsleep()calls.
* Fast iteration & simple install– flows are interpreted (no compilation) and installation is a single script.

Simple Example:

# flow_contacts_android.yaml

appId: com.android.contacts
---
- launchApp
- tapOn: "Create new contact"
- tapOn: "First Name"
- inputText: "John"
- tapOn: "Last Name"
- inputText: "Snow"
- tapOn: "Save"

## Getting Started

Maestro requires Java 17 or higher to be installed on your system. You can verify your Java version by running:

java -version

Installing the CLI:

Run the following command to install Maestro on macOS, Linux or Windows (WSL):

curl -fsSL "https://get.maestro.mobile.dev" | bash

The links below will guide you through the next steps.

* Installing Maestro(includes regular Windows installation)
* Build and install your app
* Run a sample flow
* Writing your first flow

## Resources & Community

* 💬Join the Slack Community
* 📘Documentation
* 📰Blog
* 🐦Follow us on X

## Contributing

Maestro is open-source under the Apache 2.0 license — contributions are welcome!

* Checkgood first issues
* Read theContribution Guide
* Fork, create a branch, and open a Pull Request.

If you find Maestro useful, ⭐ star the repository to support the project.

## Maestro Studio – Test IDE

Maestro Studio Desktopis a lightweight IDE that lets you design and execute tests visually — no terminal needed.
It is also free, even though Studio is not an open-source project. So you won't find the Maestro Studio code here.

* Simple setup– just download the native app for macOS, Windows, or Linux.
* Visual flow builder & inspector– record interactions, inspect elements, and build flows visually.
* AI assistance– use MaestroGPT to generate commands and answer questions while authoring tests.

Download Maestro Studio

## Maestro Cloud – Parallel Execution & Scalability

When your test suite grows, run hundreds of tests in parallel on dedicated infrastructure, cutting execution times by up to 90%. Includes built-in notifications, deterministic environments, and complete debugging tools.

Pricing for Maestro Cloud is completely transparent and can be found on thepricing page.

👉Start your free 7-day trial

 Built with ❤️ by Maestro.dev

## About

Painless E2E Automation for Mobile and Web

maestro.dev

### Topics

 android

 ios

 ui-automation

 blackbox-testing

### Resources

 Readme



### License

 Apache-2.0 license


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

12.1k

 stars


### Watchers

62

 watching


### Forks

695

 forks


 Report repository



## Releases134

CLI 2.3.0

 Latest



Mar 10, 2026



+ 133 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors105

+ 91 contributors

## Languages

* Kotlin77.3%
* TypeScript9.0%
* Objective-C6.8%
* Swift4.9%
* Shell1.2%
* JavaScript0.7%
* Other0.1%
