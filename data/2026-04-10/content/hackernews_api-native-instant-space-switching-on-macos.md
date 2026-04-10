---
title: Native Instant Space Switching on MacOS
url: https://arhan.sh/blog/native-instant-space-switching-on-macos/
site_name: hackernews_api
content_file: hackernews_api-native-instant-space-switching-on-macos
fetched_at: '2026-04-10T11:21:48.077682'
original_url: https://arhan.sh/blog/native-instant-space-switching-on-macos/
author: Arhan Chaudhary
date: '2026-04-09'
description: Arhan's Blog
tags:
- hackernews
- trending
---

# Native Instant Space Switching on MacOS

 

Published• 3 min read
•more postsView on

 
 
 

The worst part about the MacOS window management situation is the inability to instantly switch spaces, and that Apple hascontinuously ignored requeststo disable the nauseating switching animation. Sure, it’s notthatlong, but I switch spaces often enough to the point where it becomes very noticeable and drives me insane.

I believe to have found the best solution to instant space switching!

But before I show you, of course, other people share the same sentiment. I claim that none of the surveyed contemporary solutions, except for what I bring up at the end of this article, suffice for what I want:

1. Enable the “Reduce motion” setting in System Settings.This is always the default answer to this question online, and I’m sick of it! It doesn’t even solve the problem, but rather replaces it with an equally useless fade-in animation. It also has the side effect of activating theprefers-reduced-motionmedia query on web browsers.
2. Install theyabaitiling window manager and use its instant space switcher.And to be fair, it works pretty well. There are only two problems: for one, yabai does this by binary patching a part of the operating system. This is only possible by disablingSystem Integrity Protectionat your own discretion. For the second, installing yabai forces you to learn and use it as your tiling window manager1. I personally usePaperWM.spoonas my window manager. Both of which are incompatible when installed together.
3. Use a third-party virtual space manager facade, hiding and showing windows as needed when switching spaces.Some popular options areFlashSpaceandAeroSpace virtual workspaces. I actually offer no criticism other than that they are not native to MacOS, and feel unnecessary given that all we want to do is disable an animation.
4. Pay for a license forBetterTouchTool. Enable “Move Right Space (Without Animation)” and “Move Left Space (Without Animation)”.

Without further ado, I managed to findInstantSpaceSwitcherbyjurplelon GitHub. It is a simple menu bar application that achieves instant space switching while offeringnoneof the aforementioned drawbacks.

 
 
 
 
 
 
Here I have InstantSpaceSwitcher paired up with 
SpaceName
.
 
 

InstantSpaceSwitcher does not require disabling Security Integration Protection; it works by simulating a trackpad swipe with a large amount of velocity. It additionally allows you to instantly jump to a space number. The last thing it provides is a command line interface.

The installation instructions are not listed on the README, so they are:

$
 git
 clone
 https://github.com/jurplel/InstantSpaceSwitcher

$
 cd
 InstantSpaceSwitcher

$
 ./build.sh

InstantSpaceSwitcher should now be available as a native application.

After running the above, the command line interface is available at:

$
 .build/release/ISSCli
 --help

Usage:
 .build/release/ISSCli
 [left
|
right
|
index
 <
n
>
]

Did I mention that the repository literally has one star on GitHub (me)? I want more people to discover InstantSpaceSwitcher and consider it trustworthy; hence, please consider giving it astarif you find it helpful.

Until next time!

## Footnotes

1. I foundinstantspaceson GitHub, which attempts to isolate yabai’s instant space switcher. Unfortunately, I tried, and I really tried, but I could not get it to work on MacOS Tahoe. Although I prefer InstantSpaceSwitcher anyways, please let me know if you can get it working!↩

 

↑ Scroll to top ↑