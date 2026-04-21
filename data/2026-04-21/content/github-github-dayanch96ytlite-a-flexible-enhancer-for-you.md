---
title: 'GitHub - dayanch96/YTLite: A flexible enhancer for YouTube on iOS · GitHub'
url: https://github.com/dayanch96/YTLite
site_name: github
content_file: github-github-dayanch96ytlite-a-flexible-enhancer-for-you
fetched_at: '2026-04-21T11:59:32.577836'
original_url: https://github.com/dayanch96/YTLite
author: dayanch96
description: A flexible enhancer for YouTube on iOS. Contribute to dayanch96/YTLite development by creating an account on GitHub.
---

dayanch96

 

/

YTLite

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork20.1k
* Star4.7k

 
 
 
 
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

456 Commits
456 Commits
.github
.github
 
 
FAQs
FAQs
 
 
Resources
Resources
 
 
Utils
Utils
 
 
layout/
Library/
Application Support/
YTLite.bundle
layout/
Library/
Application Support/
YTLite.bundle
 
 
.gitignore
.gitignore
 
 
Makefile
Makefile
 
 
README.md
README.md
 
 
Settings.x
Settings.x
 
 
Sideloading.x
Sideloading.x
 
 
YTLite.h
YTLite.h
 
 
YTLite.plist
YTLite.plist
 
 
YTLite.x
YTLite.x
 
 
YTNativeShare.x
YTNativeShare.x
 
 
YouTubeHeaders.h
YouTubeHeaders.h
 
 
control
control
 
 
View all files

## Repository files navigation

# YouTube Plus (ex. YTLite)

A flexible enhancer for YouTube on iOS, featuring over hundred customizable options.

## Table of Contents

* Screenshots
* Main Features
* FAQ
* Reviews
* How to build a YouTube Plus app using GitHub Actions
* Supported YouTube Version
* Tweak Integration Details

## Screenshots

More screenshots

## Main Features

Download videos, audio (including audio track selection), thumbnails, posts, and profile pictures

Copy video, comment, and post information

Interface customization: Remove feed elements, reorder tabs, enable OLED mode, and as use Shorts-only mode

Player settings: Gestures, default quality, preferred audio track

Save, Load and Restore settings. Clear cache once or automatically on app startup

Built-in SponsorBlock

And much, much more

YouTube Plus preferences can be found in the YouTube Settings

All contributors are listed in the Contributors sectionUsed open-source libraries are listed in the Open Source Libraries section

Note

Starting from version 5.2, YTPlus requires a subscription.The last free version is5.2b4.

## FAQ

* 🇺🇸 English FAQ
* 🇷🇺 ЧаВо на Русском
* 🇮🇹 FAQ in Italiano
* 🇵🇱 FAQ po polsku

## Reviews

Review by@qbapon ONE Jailbreak:https://onejailbreak.com/blog/youtube-plus/

## How to build a YouTube Plus app using Github actions

Note

If this your first time, complete following steps before starting:

1. Fork this repository using the fork button on the top right
2. On your forked repository, go toRepository Settings>Actions, enableRead and Writepermissions.

How to build the YouTube Plus app

1. Click onSync fork, and if your branch is out-of-date, click onUpdate branch.
2. Navigate to theActions tabin your forked repository and selectCreate YouTube Plus app.
3. Click theRun workflowbutton located on the right side.
4. Mark or unmark the tweaks you want to integrate. Learn more about them in theTweak Integration Detailssection.
5. Prepare a decrypted .ipa file(we cannot provide this due to legal reasons), then upload it to a file provider (e.g., filebin.net, filemail.com, or Dropbox is recommended). Paste the URL of the decrypted IPA file in the provided field.
6. NOTE:Make sure to provide a direct download link to the file, not a link to a webpage. Otherwise, the process will fail.
7. Enter the tweak version from the releases (the latest release is selected by default). You can also change the BundleID and Display Name if desired.
8. Make sure all inputs are correct, then clickRun workflowto start the process.
9. Wait for the build to finish. You can download the YouTube Plus app from the releases section of your forked repo. (If you can't find the releases section, go to your forked repo and add /releases to the URL, i.e., github.com/user/YTLite/releases.)

How to build the YouTube Plus app with your own link for the YouTube Plus tweak

1. Click onSync fork, and if your branch is out-of-date, click onUpdate branch.
2. Navigate to theActions tabin your forked repository and select[BETA] Build YouTube Plus app.
3. Click theRun workflowbutton located on the right side.
4. Mark or unmark the tweaks you want to integrate. Learn more about them in theTweak Integration Detailssection.
5. Prepare a decrypted .ipa file(we cannot provide this due to legal reasons), then upload it to a file provider (e.g., filebin.net, filemail.com, or Dropbox is recommended). Paste the URL of the decrypted IPA file in the provided field.
6. Upload your beta tweak file to a file provider and paste direct link to theURL to the YouTube Plus tweak filefield. You can also change the BundleID and Display Name if desired.
7. NOTE:Make sure to provide a direct download link to the file, not a link to a webpage. Otherwise, the process will fail.
8. Make sure all inputs are correct, then clickRun workflowto start the process.
9. Wait for the build to finish. You can download the YouTube Plus app from the releases section of your forked repo. (If you can't find the releases section, go to your forked repo and add /releases to the URL, i.e., github.com/user/YTLite/releases.)

## Supported YouTube Version

* Latest confirmed:21.15.5
* Date tested:Apr 20, 2026
* YouTube Plus:5.2

## Tweak Integration Details

YouPiP

YouPiP is a tweak developed byPoomSmartthat enables the native Picture-in-Picture feature for videos in the iOS YouTube app.

YouPiP preferencesare available in theYouTube settings.

Source code and additional information are availablein PoomSmart's GitHub repository.

YTUHD

YTUHD is a tweak developed byPoomSmartthat unlocks 1440p (2K) and 2160p (4K) resolutions in the iOS YouTube app.

YTUHD preferencesare available in theVideo quality preferencessection underYouTube settings.

Source code and additional information are availablein PoomSmart's GitHub repository.

Return YouTube Dislikes

Return YouTube Dislikes is a tweak developed byPoomSmartthat brings back dislikes on the YouTube app.

Return YouTube Dislikes preferencesare available in theYouTube settings.

Source code and additional information are availablein PoomSmart's GitHub repository.

YouQuality

YouQuality is a tweak developed byPoomSmartthat allows to view and change video quality directly from the video overlay.

YouQuality can be enabledin theVideo overlaysection underYouTube settings.

Source code and additional information are availablein PoomSmart's GitHub repository.

DontEatMyContent

DontEatMyContent is a tweak developed bytherealFoxsterthat prevents the Notch/Dynamic Island from munching on 2:1 video content in the iOS YouTube app.

DontEatMyContent preferencesare available in theYouTube settings.

Source code and additional information are availablein therealFoxster's GitHub repository.

## About

A flexible enhancer for YouTube on iOS

### Topics

 ios

 downloader

 youtube

 jailbreak

 tweak

 sponsorblock

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

4.7k

 stars
 

### Watchers

31

 watching
 

### Forks

20.1k

 forks
 

 Report repository

 

## Releases27

YouTube Plus 5.2

 Latest

 

Apr 20, 2026

 

+ 26 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* patreon.com/dayanch96
* buymeacoffee.com/dayanch96

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Logos75.5%
* Objective-C24.2%
* Makefile0.3%