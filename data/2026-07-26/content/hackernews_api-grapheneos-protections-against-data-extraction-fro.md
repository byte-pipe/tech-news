---
title: GrapheneOS protections against data extraction from locked devices - GrapheneOS Discussion Forum
url: https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices
site_name: hackernews_api
content_file: hackernews_api-grapheneos-protections-against-data-extraction-fro
fetched_at: '2026-07-26T19:29:35.940733'
original_url: https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices
author: Cider9986
date: '2026-07-26'
description: GrapheneOS discussion forum
tags:
- hackernews
- trending
---

Loading...

 This site is best viewed in a modern browser with JavaScript enabled.
 

 Something went wrong while trying to load the full version of this site. Try hard-refreshing this page to fix the error.
 

# GrapheneOS protections against data extraction from locked devices

### GrapheneOS

GrapheneOS has strong defenses against data extraction. It heavily builds upon the standard security features provided by Android 17 and the most secure hardware available for Android. Currently, only Pixels provide the hardware security features and updates required by GrapheneOS. That's going to change in 2027 thanks to our partnership with Motorola Mobility and progress being made by Qualcomm.

Disk encryption provides strong protection for data. Even the most sophisticated attackers aren't going to be directly breaking it. They either need to exploit the OS while in After First Unlock state or brute force the PIN/password.

Android 16 QPR2 calls for a secure element implementing rate limiting ramping up delays. It's 4 hours after 10 and 41 days after 15. Only 20 attempts are allowed. For usability, It rejects the most recent 5 unique failed attempts early to avoid wasting attempts on repeated errors. GrapheneOS only supports devices implementing the latest generation secure element rate limiting.

https://source.android.com/docs/security/features/authentication/rate-limiting

The secure element on the supported devices also has insider attack resistance. That's implemented by requiring the Owner user to successfully authenticate before the secure element firmware can be updated. A valid signing key and greater version number aren't enough alone. The purpose of this is preventing any government from bypassing the rate limiting by coercing the creation of a firmware update removing the rate limit.

Pixels have used a secure element with an internal timer implementing rate limiting and insider attack resistance since the Pixel 2 launched near the end of 2017. Here's a post about this from back in 2018:

https://android-developers.googleblog.com/2018/05/insider-attack-resistance.html

The secure element and integration into the OS has become far better since then, but it shows this goes back a long way and isn't a new feature.

GrapheneOS also raises the character limit for passwords from 16 to 128. This enables using high entropy diceware passphrases not depending on the secure element rate limiting.

To make a strong passphrase convenient to use without ruining it with biometric unlock, GrapheneOS adds an optional 2nd factor fingerprint PIN. We reduce the allowed fingerprint attempts from 20 to 5 and failure to enter the correct 2nd factor PIN counts towards it. This enables using 6-8 random diceware words as the main unlock method required in Before First Unlock and fingerprint+PIN using a short PIN for convenience. Using a valid fingerprint prompts to enter the 2nd factor PIN which is needed to complete unlocking the screen and hardware keystore.

GrapheneOS greatly improves the exploit protections for the OS with hardened memory allocators and other features. It heavily uses hardware-based security features including hardware memory tagging (MTE) to protect against exploits. A partial overview of those protections is here:

https://grapheneos.org/features#exploit-protection

GrapheneOS adds specialized protection against attacks with physical access too. For example, it blocks new USB connections at a software and hardware level by default while locked and disables USB data as soon as there are no active USB connections.

GrapheneOS shipped a locked device auto-reboot timer back in June 2021. It can be set between 10 minutes and 72 hours. We enabled it by default using 72 hours and then lowered it 18 hours. It automatically returns the device to Before First Unlock state due to our memory zeroing as part of tearing down the OS and booting. We got Pixels to add memory zeroing for booting the firmware fastboot mode in April 2024. Apple and Google added a locked device auto-reboot timer in iOS 18.1 and Android 16. For Android, it can be enabled with the Android Advanced Protection Mode. Our implementation is better for multiple reasons but it's a useful feature regardless.

Android uses separate encryption keys for each secondary user and Private Space. GrapheneOS adds support for putting both back into Before First Unlock state without a reboot via end session for secondary users or toggles for either to do it by default. It's still much better for the device to be rebooted to get the main user back at rest, completely clear leftover data from RAM and block secure element updates.

Our duress PIN/password feature is a minor feature fitting into the bigger picture. It wipes the device when it's entered in any OS prompt for the current profile's PIN or password. It will wipe the device when entered into the authentication prompt for changing a sensitive setting or anything else requiring it, not only the lockscreen. It works across every profile including secondary users and Private Spaces, not only the main user. The duress PIN will also wipe the device when entered as a 2nd factor PIN for fingerprint unlock, but not a SIM PIN.

There are multiple ways to use the duress PIN/password feature including writing it down on a phone case or a paper kept in a wallet. People should carefully consider how to use it in an actual duress situation where there can be physical or legal consequences for wiping the device. GrapheneOS doesn't require it to protect data from being extracted from the device, but it takes recovering it completely off the table even with the PIN/password for each profile on the device.

GrapheneOS doesn't depend on the duress PIN/password to protect user data. It's one of the tools it provides among the major privacy and security improvements it offers as a whole. Our features page provides an overview of what GrapheneOS offers compared to standard Android 17. It covers most of the major features we provide and many of the minor ones but there's also a lot more beyond it. Our release notes are a lot more exhaustive since we make sure to cover everything when it's added, changed or removed.

https://grapheneos.org/featureshttps://grapheneos.org/releases#changelog

### FunkTastic

GrapheneOSThis thread should be pinned.

### moonlitmartyr

GrapheneOSamazing writeup, thank you. How big of an attack surface is USB PD? I was wondering if there's a way to eliminate that with a toggle someday and just live with 5v charging rather than entirely disabling the charging port which is a more extreme but albeit very effective way to prevent USB PD attacks. To the best of my knowledge even with charging only its still there since it's not a standard data connection but I could be wrong.

### Handlebar6933

GrapheneOSAsskully373mentioned, separate BFU and AFU credentials would be great for those of us who frequently get locked out of biometric login.

### skully373

Is it in the road map to add the ability to do a long password for BFU unlock and then only PIN for AFU as opposed to requiring a fingerprint and PIN for the 2FA? For some of us, our fingers get wrecked at work and fingerprint unlock often fails. So the ability to require a good password after reboot and just a PIN for regular use during the day would be an awesome feature addition. Like how an encrypted Linux machine works. Complicated decryption password, convenient unlock password.

Thank you for all your hard work.

### Handlebar6933

skully373Yes please! Some of us cannot afford to get the newer ultrasonic fingerprint Pixels, so we often get locked out while in the middle of the street or even when trying to pay for something. In those situations, having a complex password can be a great inconvenience. However, we still want to have the best protection against BFU brute force attacks.

### Matth

Since you might get into legal troubles in some cases, would a feature of adding a minor duress PIN, that does not wipe the device, but simply reboot it, be useful?

I could imagine, where like at a border control, your phone might not be in your possession anymore, so you can’t reboot the device anymore. Giving out this PIN wouldn’t destroy evidence, yet making it much harder to exploit it.

### Notme

Matthyour phone might not be in your possession anymore, so you can’t reboot the device anymore

There is a feature called auto-reboot exist.

GrapheneOS shipped a locked device auto-reboot timer back in June 2021. It can be set between 10 minutes and 72 hours. We enabled it by default using 72 hours and then lowered it 18 hours. It automatically returns the device to Before First Unlock state due to our memory zeroing as part of tearing down the OS and booting.Source : OP.

### Notme

Matthalso imagine it.Police:(they are on your face) Gimme passwd.You: (gives PIN)The phone reboots.You: 😜The Police: oh well, it rebooted. Let's leave. We can't do anything.

Edit: Auto-reboot scenario.Police:(they are on your face) Gimme passwd.The phone reboots.You: I didn't do anything.🤷

### Pocketstar

NotmePerhaps it might be a good idea to let them find the little paper with the duress pin stuck in the phone sleeve themselves, if they unlock it with the duress pin without you providing it yourself, it may keep you out of legal trouble? (Check your local laws on destroying evidence)

### GrapheneOS

moonlitmartyrYou can currently set USB-C to Off to fully disable charging and then set it back to Charging-only or Charging-only while locked when you want to charge it. You can still charge it while it's powered off or in charging, fastboot or recovery with it set to Off. You can also just pause it during boot at the verified boot screen. It's not going to end up stuck without power with no way to charge it.

### MyIdentityIsntImportant

moonlitmartyrJust to drop this in here for anyone who might not have thought about it (just like I hadn't in the beginning), even with the USB port completely off, Pixels can be charged via wireless chargers as usual. So maybe getting a cheap-ish wireless charging pad might be worth it to some just for this reason alone.

### FunkTastic

PocketstarI have more cunning approach. I use both GrapheneOS and iOS, the latter for bank/gov apps. The PIN I use on iOS is set as duress on GrapheneOS. I don't turn away from surveillance cameras when entering it.

### ProfessorMonks

Did you write this article to reassert GrapheneOS' protections, in light of the recent headline?https://www.theguardian.com/us-news/2026/jul/23/cop-city-protester-phone

tl;dr - man is interrogated and put under duress to unlock device. He provides duress password which wipes the device.

Interestingly, they put him on a watchlist for protesting a police training center but questioned him on CSAM (presumably as a pretext).

### Pocketstar

ProfessorMonksDid you write this article to reassert GrapheneOS' protections, in light of the recent headline?https://www.theguardian.com/us-news/2026/jul/23/cop-city-protester-phone

tl;dr - man is interrogated and put under duress to unlock device. He provides duress password which wipes the device.

Interestingly, they put him on a watchlist for protesting a police training center but questioned him on CSAM (presumably as a pretext).

This abuse of law enforcement is but one of many reasons why we have GrapheneOS; in order to protect ourselves against this form of government corruption.It also prevents dissidents (like women in some countries) from getting imprisoned in corrupt countries and it protects whistleblowers. The GrapheneOS developers are the protectors of these lives, I cannot praise them enough for it.

### moonlitmartyr

MyIdentityIsntImportantthat's really interesting, thank you.

### Hat

Could you please explain the data protection measures that apply to unlocked devices? How does it defend itself when plugged into a corrupt device, such as a car or a screen?

For example, the desktop mode automatically launches on Android 17 when the Pixel is plugged in, with the screen controlling the USB.