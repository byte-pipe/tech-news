---
title: 'GitHub - TelegramMessenger/Telegram-iOS: Telegram-iOS · GitHub'
url: https://github.com/TelegramMessenger/Telegram-iOS
site_name: github
content_file: github-github-telegrammessengertelegram-ios-telegram-ios
fetched_at: '2026-04-06T11:21:46.207749'
original_url: https://github.com/TelegramMessenger/Telegram-iOS
author: TelegramMessenger
description: Telegram-iOS. Contribute to TelegramMessenger/Telegram-iOS development by creating an account on GitHub.
---

TelegramMessenger



/

Telegram-iOS

Public

* NotificationsYou must be signed in to change notification settings
* Fork2.5k
* Star8.2k




 
master
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

29,953 Commits
29,953 Commits
.github
.github
 
 
.vscode
.vscode
 
 
Telegram
Telegram
 
 
Tests
Tests
 
 
build-system
build-system
 
 
buildbox
buildbox
 
 
docs
docs
 
 
scripts
scripts
 
 
submodules
submodules
 
 
third-party
third-party
 
 
tools
tools
 
 
.bazelrc
.bazelrc
 
 
.cursorignore
.cursorignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitlab-ci.yml
.gitlab-ci.yml
 
 
.gitmodules
.gitmodules
 
 
BUILD.bazel
BUILD.bazel
 
 
CLAUDE.md
CLAUDE.md
 
 
MODULE.bazel
MODULE.bazel
 
 
MODULE.bazel.lock
MODULE.bazel.lock
 
 
README.md
README.md
 
 
Random.txt
Random.txt
 
 
WORKSPACE
WORKSPACE
 
 
build_number_offset
build_number_offset
 
 
versions.json
versions.json
 
 
View all files

## Repository files navigation

# Telegram iOS Source Code Compilation Guide

We welcome all developers to use our API and source code to create applications on our platform.
There are several things we require fromall developersfor the moment.

# Creating your Telegram Application

1. Obtain your own api_idfor your application.
2. Pleasedo notuse the name Telegram for your app — or make sure your users understand that it is unofficial.
3. Kindlydo notuse our standard logo (white paper plane in a blue circle) as your app's logo.
4. Please study oursecurity guidelinesand take good care of your users' data and privacy.
5. Please remember to publishyourcode too in order to comply with the licences.

# Quick Compilation Guide

## Get the Code

git clone --recursive -j8 https://github.com/TelegramMessenger/Telegram-iOS.git

## Setup Xcode

Install Xcode (directly fromhttps://developer.apple.com/download/applicationsor using the App Store).

## Adjust Configuration

1. Generate a random identifier:

openssl rand -hex 8

1. Create a new Xcode project. UseTelegramas the Product Name. Useorg.{identifier from step 1}as the Organization Identifier.
2. OpenKeychain Accessand navigate toCertificates. LocateApple Development: your@email.address (XXXXXXXXXX)and double tap the certificate. UnderDetails, locateOrganizational Unit. This is the Team ID.
3. Editbuild-system/template_minimal_development_configuration.json. Use data from the previous steps.

## Generate an Xcode project

python3 build-system/Make/Make.py \
 --cacheDir="$HOME/telegram-bazel-cache" \
 generateProject \
 --configurationPath=build-system/template_minimal_development_configuration.json \
 --xcodeManagedCodesigning

# Advanced Compilation Guide

## Xcode

1. Copy and editbuild-system/appstore-configuration.json.
2. Copybuild-system/fake-codesigning. Create and download provisioning profiles, using theprofilesfolder as a reference for the entitlements.
3. Generate an Xcode project:

python3 build-system/Make/Make.py \
 --cacheDir="$HOME/telegram-bazel-cache" \
 generateProject \
 --configurationPath=configuration_from_step_1.json \
 --codesigningInformationPath=directory_from_step_2

## IPA

1. Repeat the steps from the previous section. Use distribution provisioning profiles.
2. Run:

python3 build-system/Make/Make.py \
 --cacheDir="$HOME/telegram-bazel-cache" \
 build \
 --configurationPath=...see previous section... \
 --codesigningInformationPath=...see previous section... \
 --buildNumber=100001 \
 --configuration=release_arm64

# FAQ

## Xcode is stuck at "build-request.json not updated yet"

Occasionally, you might observe the following message in your build log:

"/Users/xxx/Library/Developer/Xcode/DerivedData/Telegram-xxx/Build/Intermediates.noindex/XCBuildData/xxx.xcbuilddata/build-request.json" not updated yet, waiting...

Should this occur, simply cancel the ongoing build and initiate a new one.

## Telegram_xcodeproj: no such package

Following a system restart, the auto-generated Xcode project might encounter a build failure accompanied by this error:

ERROR: Skipping '@rules_xcodeproj_generated//generator/Telegram/Telegram_xcodeproj:Telegram_xcodeproj': no such package '@rules_xcodeproj_generated//generator/Telegram/Telegram_xcodeproj': BUILD file not found in directory 'generator/Telegram/Telegram_xcodeproj' of external repository @rules_xcodeproj_generated. Add a BUILD file to a directory to mark it as a package.

If you encounter this issue, re-run the project generation steps in the README.

# Tips

## Codesigning is not required for simulator-only builds

Add--disableProvisioningProfiles:

python3 build-system/Make/Make.py \
 --cacheDir="$HOME/telegram-bazel-cache" \
 generateProject \
 --configurationPath=path-to-configuration.json \
 --codesigningInformationPath=path-to-provisioning-data \
 --disableProvisioningProfiles

## Versions

Each release is built using a specific Xcode version (seeversions.json). The helper script checks the versions of the installed software and reports an error if they don't match the ones specified inversions.json. It is possible to bypass these checks:

python3 build-system/Make/Make.py --overrideXcodeVersion build ... # Don't check the version of Xcode

## About

Telegram-iOS

### Resources

 Readme



### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

8.2k

 stars


### Watchers

307

 watching


### Forks

2.5k

 forks


 Report repository



## Releases31

Telegram 10.0.3 (26855)

 Latest



Sep 13, 2023



+ 30 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Swift46.2%
* C41.5%
* Objective-C5.3%
* Assembly3.1%
* C++1.6%
* Objective-C++0.8%
* Other1.5%
