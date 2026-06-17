---
title: GrapheneOS has been ported to Android 17 and official releases are coming soon - GrapheneOS Discussion Forum
url: https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon
site_name: hackernews_api
content_file: hackernews_api-grapheneos-has-been-ported-to-android-17-and-offic
fetched_at: '2026-06-17T12:27:16.217445'
original_url: https://discuss.grapheneos.org/d/36469-grapheneos-has-been-ported-to-android-17-and-official-releases-are-coming-soon
author: Cider9986
date: '2026-06-16'
description: GrapheneOS discussion forum
tags:
- hackernews
- trending
---

Loading...

 This site is best viewed in a modern browser with JavaScript enabled.
 

 Something went wrong while trying to load the full version of this site. Try hard-refreshing this page to fix the error.
 

# GrapheneOS has been ported to Android 17 and official releases are coming soon

### GrapheneOS

Today is the official release day for Android 17. We've already fully ported GrapheneOS to Android 17 and are in the process of pushing the code to our public repositories. We're building a final official release based on Android 16 QPR2 today and we'll do an initial Android 17 release tomorrow.

We've already tested the Android 17 port of GrapheneOS on the Pixel 6a, 7, 7a, 8, 10a, 10 and 10 Pro Fold. It will be possible for people to start building and testing it themselves later today once we finish pushing the code. We'll start the process of public testing for official releases tomorrow.

To clarify the 2nd paragraph, we've ported GrapheneOS to Android 17 for all of the supported devices. That's a list of the devices we already built and tested it. Our initial public release will be available for all the supported devices and we'll have tested it on each by then.

### Johnnyloans

GrapheneOS

Google's blog post doesn't say specifics but it sounds like the Pixel 6 and 6 pro won't get Android 17 from them.

Is it the same for GOS?

### moonlitmartyr

GrapheneOSthank you so much for all of your hard work and effort!!!!!

### VAULT

GrapheneOSI laughed out loud. You guys are insanely professional... I worked for large, market-leading multinationals and you blow them away! Your work is so appreciated!

VAULT

### de0u

JohnnyloansGoogle's blog post doesn't say specifics but it sounds like the Pixel 6 and 6 pro won't get Android 17 from them.

Is it the same for GOS?

NormanWhat are the biggest changes/differences between the current release and the upcoming one? Is there already a list?

I suspect that right now the best use of developer time is getting the release out, as opposed to setting that work aside to answer questions about the work. It's great to hear that we're likely to be able to test an alpha release of GrapheneOS in a day or two, so waiting a day or two seems like the thing to do.

### int_32

JohnnyloansPixel 6 got Android 17 update

### Norman

What are the biggest changes/differences between the current release and the upcoming one? Is there already a list? It's always a bit hard for me to tell what Google incorporates into PixelOS or directly integrates with Google Services and what is actually changing for AOSP which pertains to GOS.

### Carrousel7956

NormanPretty sure everything listedhereis for AOSP and not Google apps or services.

### 0xC0DED0D0

Let's gooo! 🥳

### de0u

Things to know:

1. It seems likely that Android 17 for GrapheneOS will go through the standard alpha/beta/stable cycle. Because most devices are on the stable release channel (look in System Updater), most users willnotreceive Android 17 when the release announcement goes out. That is expected and does not mean that anything is going wrong.
2. Rollout progress can be tracked for each device type by checking its table on the web site -- for example, the 9a release status is here:https://grapheneos.org/releases#tegu. If possible, please avoid posting questions about why Android 17 hasn't arrived on a specific device yet until after the release is shown as stable in the release table for that device. It is possible that some devices will get a stable Android 17 before other devices.
3. Users wishing to get Android 17 as fast as possibleto help with testingcan adjust System Updater to the alpha channel, but it is possible for this to have negative side effects. It is possible that alpha-release testing (and/or beta-release testing) may uncover issues! Once a device has installed an Android 17 release of GrapheneOS, it will not be possible to go back to an Android 16 releasewithout wiping all data on the device. And if a serious issue is uncovered, fixing it could in theory take days. So users who are excited about Android 17 but who are not willing to deal with some annoyance for multiple days might be best off just waiting for a few days.

Please note that I do not speak for the GrapheneOS project.

### 0xC0DED0D0

de0umost users will not receive Android 17 when the release announcement goes out.

Fully expect a longer than usual testing cycle. No worries. Good luck,@GrapheneOSand testers! 🤓👍

Thanks for all your hard work.

### pizzadequeso

does GOS android 17 support airdrop on newer pixel devices?

### GrapheneOS4life

Thank a lot team

### Developer-Dude

Yay!! 🎉🚀

### Nyte

When will the A17 manifest get pushed?

### keycap_puller

Regarding theLocal network accesssetting - will there be an additional toggle in GOS similar to the existingNetworktoggle?WasACTION_PICK_CONTACTSinspired by GOS?

### mar2112

You guys are amazing.

### Developer-Dude

Wonder if there's any UI changes that GrapheneOS will get? Not like I will expect a lot (if any), but it'd be cool!

### awkgrafina

Way to go!

### goda90

Is GOS going to keep the new Android 17 restriction on the accessibility services only being allowed for permitted accessibility tools?

Since there's no built in "digital wellbeing" tool, I use a trusted open source app to track and limit distractions and it relies on the accessibility services, but I imagine this new restriction would break it.

### GrapheneOS

goda90That's not an Android 17 restriction but rather part of their Android Advanced Protection Mode extensions tied to Google Play. We don't have to make things such an all or nothing choice as iOS Lockdown Mode and Android Advanced Protection Mode do. We can go through the Advanced Protection features and decide which parts are useful to have as separate settings. We could also make a way to review overall privacy and security settings instead of a coarse global toggle.

Next Page »