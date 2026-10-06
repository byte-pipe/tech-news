---
title: Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped - GrapheneOS Discussion Forum
url: https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped
site_name: hackernews_api
content_file: hackernews_api-pixel-11-doesnt-yet-meet-the-grapheneos-security-s
fetched_at: '2026-10-06T16:47:56.518830'
original_url: https://discuss.grapheneos.org/d/41564-pixel-11-doesnt-yet-meet-the-grapheneos-security-standards-and-may-be-skipped
author: finnlab
date: '2026-10-06'
description: GrapheneOS discussion forum
tags:
- hackernews
- trending
---

Loading...

 This site is best viewed in a modern browser with JavaScript enabled.
 

 Something went wrong while trying to load the full version of this site. Try hard-refreshing this page to fix the error.
 

# Pixel 11 doesn't yet meet the GrapheneOS security standards and may be skipped

### GrapheneOS

We have a partial port of GrapheneOS to the Pixel 11 series after a week of work on it. We're unable to complete the port due to lack of support for ARM hardware memory tagging in software, firmware and potentially hardware. It appears Google cut an important security feature to save money.

ARM hardware memory tagging (MTE) is used by GrapheneOS across the entire base OS including the kernel and every standard base OS process. It's only temporarily disabled for a few device-specific processes. It greatly improves protection against nearly all remote exploits and many local exploits.

Pixel 8 launched with hardware MTE support in October 2023. We integrated it into our hardened_malloc project and began using it across the OS later that month. Android and the Pixel OS never started using it by default. Android Advanced Protection Mode in Android 16 enables it for a few processes.

Apple's Memory Integrity Enforcement (MIE) is an always enabled feature on the iPhone 17. It's simply a high quality implementation of MTE using the latest standard extensions. It uses MTE in the most secure mode in the kernel and a large portion of userbase. They did a very good job integrating it.

Apple's MIE and Android 16+ AAPM don't use MTE for user installed apps unless those explicitly opt in. GrapheneOS enables it for more apps automatically and has a toggle for users to opt-in for every user installed app. There's a per-app toggle to opt-out for incompatible apps which is uncommon.

Neither iOS or Android encourage app developers to opt into MTE and other more aggressive security features used in the base OS. Apple's docs warn developers of performance and stability issues. Our approach enables forcing using MTE in the standard allocators regardless.

Pixel 11 does have security improvements including moving to post-quantum secure verified boot (ML-DSA) and replacing Samsung Shannon IMS with AOSP IMS. Titan M3 should significantly improve protection against data extraction in Before First Unlock state. It's too bad they ruined it by cutting MTE.

Pixel 11 series is a lot more expensive for an incremental improvement to the CPU, the same underpowered GPU and reduced RAM for the Pro base models. They finally caught up to the last generation of Qualcomm cellular radio. It's overpriced, the upgrades aren't impressive and losing MTE is appalling.

Compared to the Pixel 11, a Snapdragon 8 Elite Gen 5 has ~40% higher single threaded CPU performance,80% higher multi threaded performance, over 100% higher GPU performance and a far better cellular radio. It also finally has MTE. The next gen is what will be in the first Motorola with GrapheneOS.

Pixel 9a and earlier (including Nexus devices) were the Android Open Source Project reference devices. Pixel support was removed from AOSP with Android 16. It's now harder to support Pixels than many other devices and massive progress towards open source firmware and driver libraries was discarded.

Compared to the stock Pixel OS, GrapheneOS ships AOSP patches months earlier and Linux kernel patches many months earlier. However, we rely on them for firmware and most driver updates. We also want to move to new kernel branches earlier. These things can be improved with our Motorola partnership.

We strongly recommend against buying Pixel 11 devices. Pixel 8, 9 and 10 have much better overall security for GrapheneOS. Pixel 10 is cheaper with similar hardware and MTE. Pixel 11's Titan M3 should improve BFU security for users without a strong passphrase, but losing MTE craters AFU security.

We haven't determined what to do about this situation. It may be best for us to skip the Pixel 11 series devices. We can shift our focus entirely to the upcoming Motorola devices instead. Pixel 10a was really a 9th gen Pixel, so hopefully the Pixel 11a does the same with 10th gen and includes MTE.

https://bsky.app/profile/grapheneos.org/post/3mua32q4ds22ehttps://grapheneos.social/@GrapheneOS/117179231167297908https://x.com/GrapheneOS/status/2093731615243411862

### AtmosphericIgnition

Is there a way to tell if the MTE hardware is physically present on the device, or if the firmware has it disabled and not exposed?

### DeletedUser1111

I suggest that this thread should be pinned.

### MetropleX

AtmosphericIgnitioncurrent research points to not being present, however, per the above:

We're unable to complete the port due to lack of support for ARM hardware memory tagging in software, firmware and near certainly hardware.

### xxx

Bummer! As we have the 10, 10a and the upcoming Moto it saves a lot of work. Shame on google.

### alonely0

I would strongly prefer if we kept support for Pixels, given MTE is far from the only benefit of GOS, and we still support older models without it (even if for historical reasons).

We are between a rock and a hard place, but I don't think it's necessarily preferable to bet it all on Motorola having phones with GOS support indefinitely. I'd rather we keep Pixels on the back-burner, even if on a Tier-2 sort of thing.

### Eirikr70

I'll still wait for the 11a praying! I might get a 10a then if it doesn't fit the bill!

### legreteco

Eirikr70the 11a will likely have the Tensor G6 as well, so I'd not bet on it.

### Breyyn

Very disappointed in this, wanted to get a 512GB Base Pixel 11 as the 512GB P10 Pro's in Canada are basically all out of stock everywhere unless paying retail price. Guess I'll have to suck it up and wait for a Moto. Shame on Google.

### GazelleInitial

Is it that big of a deal? Most apps are disabled by default on mine for mte

### Sonic

I believe the GrapheneOS foundation should not compromise on their security requirements. If the Pixel 11 series does not have MTE, then it should not be supported. Users who are not aware of the security regression in the Pixel 11 series might get one rather than an older, more secure model because people typically have the mindset that "newer is better".

Please do not compromise on security because of Google. MTE is, to my knowledge, one of the strongest security features of GrapheneOS. It should always be present going forward.

### DeletedUser1111

GazelleInitialIt's recommended toenable MTE by default(from the Owner profile) (last paragraph)

### GazelleInitial

DeletedUser1111interesting. Done.Let's see what I need to disable.

### ClickClickDrone

alonely0

MTE is one of the minimum requirements for GrapheneOS going forward, and is a very important security improvement against memory corruption bugs.

It makes no sense to give exceptions to that requirement, and MTE is now one of the standard expected features.

### Eirikr70

ClickClickDroneYes, just a pity that for a moment there will be only fairly expensive phones supporting GrapheneOS.

### Unkn0wn-3nt1ty

GazelleInitial

As someone whos done this from the start (and changes app iif lacking supporrt for MTE), ive maybe a handful of apps that dont support MTE. Good luck :)

### deltuzirtu

Maybe that's a good thing. Better to focus your attention on Motorola devices instead.

### Eagle_Owl

GazelleInitialOn my Pixel phones MTE is enabled for all apps.All apps are working fine.

@GrapheneOS: Yes, Apple has done a great job with its current CPU A19. But it's a shame that developers don't use it for their own apps. And it's a shame that Apple hasn't taken the opportunity to provide MacBook Neo users with this great protection against malware as well!

No, the decision-makers at Apple are stupid, stingy, and greedy, because they're just giving customers the older A18. As an entry-level model, the MacBook Neo could have been the first "desktop computer" with real malware protection (there is nothing to stop MTE aka MIE from being brought to the next M chips).

No, this is not off-topic, because I want to emphasize how important this protection mechanism is in today's world, where criminals have the security vulnerability examined by AI within a few hours immediately after the release of critical security updates and generate exploits fully automatically and thus attack every device on the same day that has not installed the security patch immediately (!).

Conclusion: nowadays you can not longer do without MTE/MIE!

### Iceschillendrig

BreyynYou can get a refurbished one online for a good price.

Next Page »