---
title: KDEConnect - KDE Community Wiki
url: https://community.kde.org/KDEConnect
site_name: hackernews_api
fetched_at: '2025-10-21T19:08:01.484257'
original_url: https://community.kde.org/KDEConnect
author: snthd
date: '2025-10-12'
description: 'KDE Connect: Enabling communication between all your devices'
tags:
- hackernews
- trending
---

From KDE Community Wiki

This is the community page forKDE Connect. Feel free to edit it! It should contain useful and up-to-date resources for both users and developers.

## What is KDE Connect?

KDE Connectis a project that enables all your devices to communicate with each other. Here are a few thingsKDE Connectcan do:

* Receive your phone notifications on your desktop computer and reply to messages
* Control music playing on your desktop from your phone
* Use your phone as a remote control for your desktop
* Run predefined commands on your PC from connected devices. See the list ofexample commandsfor more details.
* Check your phones battery level from the desktop
* Ring your phone to help finding it
* Share files and links between devices
* Browse your phone from the desktop
* Control the desktop's volume from the phone

To achieve this,KDE Connect:

* implements a secure communication protocol over the network, and allows any developer to create plugins on top of it.
* Has a component that you install on your desktop.
* Has a KDE Connect client app you run on your phone.

This video from 2013 demonstrates some other cool features:https://www.youtube.com/watch?v=KkCFngNmsh0

More info atAlbert Vaka'sorNico'sblog.

## Installation and Usage

Please see theKDE ConnectUserbase pagefor detailed information on the different waysKDE Connectcan be installed and used.

## Build KDE Connect from source

KDE Connectis a free/libre open source software which has been in development since 2013. It connects to many different parts of the OS, and therefore you'll need to build many KDE dependencies.

### Linux Desktop

For beginners it's highly recommended to use a meta-build system such as "kde-builder", by following the main instructions forBuilding KDE software. These meta-build systems have the benefit of minimising changes to your desktop environment installation and containing the dev files to a single directory.

After you've built the KDE dependencies, you can build theKDE Connectapp itself, such askde-builder kdeconnect. Then run the app + daemon such as:

killall kdeconnectd kdeconnect-app ; kde-builder --run kdeconnectd & kde-builder --run kdeconnect-app

Or if you choose to build KDE using Craft, see the build instructions for KDE Connect with Crafthere.

For more experienced developers, KDE Connect can be built directly from source using CMake and system-installed dependencies, such as by followingBuild KDE manually using CMake, and then you can directlyBuild KDE Connect using CMake.

### Windows

KDE Connect is officially supported on Windows.
Seeherefor build instructions.

### Android

The most convenient dev-flow way is to pass theproject URLtoAndroid Studio, build the app and install it to your phone.
Remember to uninstall any already-installed KDE Connect app from your target Android device.
You can also build the android app through CLI using gradle.

You can also run the app in an emulated Android device for devel. See [/Android_Emulator/ here] for instructions.

### iOS

SinceKDE Connect iOSis being developed in native frameworks, a recent version of Xcode is required to build the app. However, due to the special entitlements used in the complete version of KDE Connect, it can only be signed by the KDE e.V. development team. A wiki page is currently being written with information on how building and distribution would work and the possible resources available to contributors without macOS access.

### MacOS

KDE Connectworks fairly well on macOS, however there is no official version as of yet. Seeherefor build instructions.

You can get the Nightly Build from theBinary Factory.

### Special Mentions

Special instructions for specific topics:

#### Plasmoid Development

You can useplasmawindowedto easily run the Plasmoid (even on non-KDE environments).

Set up your dev environment as above, then runmake install, then runplasmawindowed org.kde.kdeconnectto launch the Plasmoid and see your changes.

#### Mobile-Friendly QML App

The kdeconnect-app component of the desktop version is suitable for mobile Linux environments, too.

#### Desktop SMS Messaging App

KDE Connecthas an SMS messaging app which lets you type and view SMS messages from your computer.
It supports basic features and works correctly most of the time.
If you are interested in trying or developing it, you can build it from source.
It is automatically built as part of the rest ofKDE Connectand is output as 'kdeconnect-sms'.

## Development

KDE Connectis a perfect project to start contributing to KDE. You'll need a basic understanding of programming concepts, the rest can be learned by doing. Experience with Android or Qt is beneficial, but not needed.

We have a group to discuss development. You can access it fromMatrixorLibera IRC network(#kdeconnect). If you cannot find the correct room on Matrix, it might help if you first join theKDE Matrix Space. You can read more about KDE's use of MatrixhereFeel free to ask any development-related questions there. We also have amailing list.

All patches are submitted on Gitlab. The Android repository ishereand the C++ Desktop repository ishere. Be sure to select the most relevant template. You don't need to assign any reviewers, the developers are subscribed to notifications. Should this be your first patch, it's good to know that it might take some time before your patch is reviewed (we all work onKDE Connectin our free time), and you'll probably have to make some changes a couple of times. That's not because you're new, that's what happens for all reviews (even for long-time contributors).

There are a couple of tasks marked as Junior Jobs on ourworkboard. Those have some extra information on how to approach them that help you get started.

### Setting up KDE Connect Repository for Development

KDE Connectis actually composed of two repositories; one for the Android implementation and one for the C++ (Desktop) implementation. You can have a local clone of both on your computer and the steps to set them up are the same. For these directions, I will use the C++ repository, but if you want the Android repository, just replace every instance of 'kdeconnect-kde' with 'kdeconnect-android'

1. Fork the repository* With your web browser, open the Web GUI to KDE Connect's GitLab:https://invent.kde.org/network/kdeconnect-kde
* If you are not already, sign in with your KDE identity by clicking the "Sign In" button in the top left
* Click the "Fork" button, near the top right
* Wait for the forking to complete
2. Clone your fork* Open your new fork in the GitLab web GUI
* Click the "Clone" button in the top right
* Select the method of cloningI recommend SSH. This will require you add an SSH public key to your KDE GitLab account.An HTTPS clone will require you to log in with your KDE Identity credentials to push changes.
* I recommend SSH. This will require you add an SSH public key to your KDE GitLab account.
* An HTTPS clone will require you to log in with your KDE Identity credentials to push changes.
* In the folder you want to clone, do 'git clone <cloning path from above>'

You are all set up! See the optional steps for ways to make life easier.

#### Set up second remote (Optional)

Having a second remote allows you to have your local 'master' branch track the upstream kdeconnect-kde master branch, so you can easily get all the latest changes.

These steps assume you are using command-line git. If you are using a GUI tool, the steps will be different, but the ideas will be the same.

1. On the command line, change to your local repository clone
2. Execute:

# Note that we use HTTPS cloning here so that you don't need a verified account to pull changes!

git

remote

add

upstream

https://invent.kde.org/network/kdeconnect-kde.git
git

fetch

upstream
git

checkout

-b

upstream-master

--track

upstream/master

1. Now whenever there are new changes upstream, simply pull the upstream-master branch, then merge or rebase your local branches onto those changes!

### Development tips

#### Restarting the daemon

Whenever you do a change to KDE Connect you need to restart the daemon for the change to take effect.

killall

kdeconnectd
build/bin/kdeconnectd

#### Debug Logging

By default, most Linux distributions tell Qt to restrict what logging you will see. You can control this using the QT_LOGGING_RULES variable. Running something like the below command will show most all logging.

export

QT_LOGGING_RULES
=
"*.debug=true; qt.*.debug=false"

#### DBus inspection

The daemon communicates with various UI components (Plasmoid, CLI, Indicator etc.) over DBus. QDbusViewer allows inspecting the DBus interface provided by the daemon which can be incredibly useful for debugging.

### Running KDE Connect on an emulator

How to setup runningKDE Connecton an emulator is described hereAndroid_Emulator

## Release Process

The following sections describe how to release a new version KDE Connect

### C++ Application

#### Tarballs

Tarball releases are handled automatically through KDE's release process. These are typically consumed by downstream distros in their release process.

#### Windows Store

1. This should ideally be done at the same time as the .exe upload, using the build from the same version.
2. Do some QA on a build you would like to release. Navigate to therepository pipelines, grab the latest signed *-sideload.appx of a release (not master) build you would to release and test it. Make sure all the plugins work, and make sure the UI elements look right.
3. When ready to release run the manual job `microsoftstore_qt6` in the pipeline step to upload the .appx to the Microsoft store.
4. If the job complains about `Branch is not cleared for publishing. Skipping`, you need to add the release branch here:https://invent.kde.org/albertvaka/ci-utilities/-/blob/master/signing/microsoftstorepublisher-projects.yaml
5. Open theMicrosoft Store partner centerand login with your `@kdeev.onmicrosoft.com` credentials. If you don't have access to the partner center, you need to file a sysadmin ticket, as describedhere.
6. If you want to modify the store listing, note you can download & upload as a CSV that contains all languages, so it's easy to modify them in bulk.
7. Submit the update for review. In submission options you can chose that it goes live as soon as it's reviewed, otherwise you will have to come back in a couple days after the release is approved to make it public.

#### Windows EXE

1. This should ideally be done at the same time as the Windows Store upload, using the build from the same version.
2. Grab the *.exe and the *.exe.sha256 from the build. Install it, test that it works.
3. Upload the .exe, .exe.sha256, -dbg.7z, and -dbg.7z.sha256 to the release network, as described here:https://community.kde.org/ReleasingSoftware#Uploading_the_Tar
4. File a sysadmin ticket, and request that the .exe and -dbg.7z files from the build you tested be uploaded to the stable download path, likehttps://download.kde.org/stable/release-service/23.08.0/windows/
5. Once the download files are in the mirror network, update the appstream data likehttps://invent.kde.org/network/kdeconnect-kde/-/commit/5639905b8dc3c36675bd8c042db7e2849023f6dc
6. Update the link inhttps://kdeconnect.kde.org/download.html, the website repo is inhttps://invent.kde.org/websites/kdeconnect-kde-org

### Android

Before making an Android release we have to:

* Bump the version name and number in theAndroidManifest.xml file.
* Create an annotated version tag on git (the name should start with "v").

#### Google Play Store

We build and sign the APK packages for the Play Store ourselves (we don't use Google's App Bundles which get signed by Google). To release on the Play Store you need two things:

* Access to the KDE organization on theGoogle Play Console.
* The KDE Connect signing key and passphrase.

We build an APK from a git version tag using Android Studio (Build > Generate Signed Bundle/APK and then select APK) and upload it to theGoogle Play Consolethrough the web UI.

#### FDroid

TheFDroid packageis not built by us. It is built and signed by the FDroid build server. Version information is stored in ametadata file on FDroid’s Gitlab. We don't update the metadata file manually for new releases, though.

FDroid periodically (every 2-3 days) scans our git repo and if there's a new version tagged it will update the metadata and trigger a build automatically. Each build attempt produces logs which can be checked to debug issues.

The FDroid community is quite active and they usually reply fast when we open an issue or a MR (eg: to update the app description or some other metadata).

#### Huawei

Ping @Jannis Göing on the Telegram channel.

### iOS

#### Apple App Store

Video recording: Using App Store Connect for KDE Connect iOS

Retrieved from "
https://community.kde.org/index.php?title=KDEConnect&oldid=103483
"
