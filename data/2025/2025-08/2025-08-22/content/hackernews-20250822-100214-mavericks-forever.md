---
title: Mavericks Forever
url: https://mavericksforever.com/
site_name: hackernews
fetched_at: '2025-08-22T10:02:14.034907'
original_url: https://mavericksforever.com/
author: Wowfunhappy
date: '2025-08-22'
---

#### In the fall of 2019, I came to a decision. It was time to leave modern macOS behind.

Adecade prior, switching to OS X had been a revelatory experience, as though the software was working in perfect sync with my mind. That feeling had long since disappeared. Each update seemed to chip away at something I liked about the platform. I needed to switch to a different operating system.

I surveyed the computing landscape. Windows was still fine, and Linux was still Linux. A normal person would have just picked one—but I was apparently not a normal person. I cared far too much about having theperfectcomputer, and I just couldn't get that wonderful memory out of my head...

What follows is partly my journey, and partly a guide for anyone who wants to follow in my footsteps. I don't know whether Irecommendfollowing in my footsteps, because it does take some work, but the results can be wonderful. If you're ready, here's how to do it.

## Hardware

### Macintosh

Every Mac released between October 2008 and September 2014 is capable of running Mac OS X 10.9 Mavericks. Maybe a friend has something in their closet?

Some notable models include:

#### Cylindrical "Trash Can" Mac Pro

If you don't need portability, the 2013 Mac Pro's Xeon processors and dual AMD FirePro GPUs remain extremely powerful in 2025!

#### Mid-2014 11" Macbook Air

At the opposite end of the spectrum, the tiny 11" Macbook Air will not win any awards for speed, but it is super easy to pick up and carry around. Apple doesn't make computers this small anymore.

This is the laptop I use as a secondary computer while travelling. Make sure to find one with 8 GB of memory!

#### Mid-2014 Retina Macbook Pro

If you want something portable but a bit more capable than a Macbook Air, these will run Mavericks beautifully. Beware: you are looking for the model originally released in July of 2014. The "Late 2014" models released the following October do not support Mavericks.

Whatever computer you choose, consider getting the battery replaced if it's a laptop. You may need to find a repair shop.

### Hackintosh

For myself, I built a Hackintosh to serve as my primary workstation. I wanted a system that would be old enough to run Mavericks, but powerful enough that I would never notice its age. Five years in to the experiment, this machine is still much more than sufficiently fast.

My hardware:

* Intel i7 4790K @ 4 GHz
* nVidia GeForce GTX 780 Ti
* Samsung 870 EVO SATA III SSD
* 32 GB DDR3 Memory

The primary limitations are as follows:

* CPU: Haswell or older.
* GPU: For nVidia, Kepler or older. For AMD, GCN 1.0 or older.
* Storage: SATA III. No NVMe drives!

Full Hackintosh instructions are beyond the scope of this website. However, I've put together acollection of tools and minimal guidewhich may work for you, depending on your hardware. This collection is based around the older Clover bootloader, because that's what I use on my own system.

Alternately, you can use the modern OpenCore bootloader.Dortania's OpenCore Install Guideis very comprehensive and includes information for older operating systems such as Mavericks.

## Why Mavericks, specifically?

Once I had decided to try downgrading my computing life, I needed a single version to settle on. I knew I wanted an operating system from before Apple abandoned the Aqua design language. I find that the classic design's strong sense of depth and rich color contrast makes my computer a lot more pleasant to use. And for reasons I can't explain, it also makes window management in particular a lot easier for me.

I experimented with three candidates inside Virtual Machines: OS X 10.6 Snow Leopard, OS X 10.8 Mountain Lion, and OS X 10.9 Mavericks. Mountain Lion was quickly eliminated:

* Speed. Mountain Lion was noticably slower than Mavericks on the same hardware, particularly in memory-constrained environments. Mavericks supports memory compression, and it makes a big difference!
* Aesthetics. Mountain Lion borrows many visual elements from early iOS, such as its linen-clad Notification Center and leather-bound Contacts app. I wanted a computer, not an iPhone. The Contacts app in Mavericks is actually closer to the one in Snow Leopard.
* App Compatibility. Mavericks supports more recent versions of apps like Affinity Photo and VMWare Fusion. iMessage works on Mavericks, as does Zoom. By contrast, I'm not aware of any software that works on Mountain Lion but not Mavericks.

Mountain Lion does have a more capable version of QuickTime, which I ultimately brought over to Mavericks. More on that later.

Choosing between Mavericks and Snow Leopard was more difficult. Snow Leopard has achieved something of a legendary status in the collective memory of many tech enthusiasts, and it's an operating system I have personal nostalgia for. Snow Leopard also supports Rosetta, potentially opening up a new library of classic PowerPC apps. However:

* Aesthetics. For the most part, I find Mavericks more visually appealing than Snow Leopard. Both versions share the same broad design language, but Apple made a lot of clever refinements between 2009 and 2013. Snow Leopard does have three visual elements which I unambiguously prefer: the scroll bars, the larger "traffic light" window control buttons, and the darker window chrome. I eventually modded the latter two into Mavericks; Snow Leopard's scroll bars are alas still stuck in Snow Leopard.
* Missing Features. In Snow Leopard, you can't rename the current document from the title bar, or reopen recent documents from the Dock menu. Snow Leopard can't use emojis—it doesn't support colored fonts—and its Finder has no concept of multiple tabs. Snow Leopard also lacks autosaving and full screen, and although these features were controversial when they were first introduced, I really appreciate their Mavericks incarnations.
* Web Browsers. There is no modern mainstream browser engine that works in Snow Leopard.

I do prefer many of Snow Leopard's default settings, but these can be recreated in Mavericks with a simple post-install script.

Mavericks it is.

## Obtaining Mavericks

For some inexplicable reason, Apple's website does not offer a Mavericks download link. Theirofficial listskips straight from Mountain Lion (10.8) to Yosemite (10.10). Perhaps Apple knows that Mavericks is just too good?

No matter. We can download Mavericks from Apple's OS Recovery Server. Open the Terminal app on any Mac (press ⌘-space and search for "Terminal"), then type or paste in the following and press return:

curl mavericksforever.com/get.sh | sh

If you're familiar with shell scripts, you may want to read the script before running it.

A Mavericks DMG image will be downloaded to your current working directory. If you can't find it, it may be in your home folder. A second file, "create-bootable-installer.command", will also be created alongside the DMG. To create a bootable Mavericks USB installer, insert a USB drive and open this second file.

You may already know how to do the rest. Insert the USB drive into a Mavericks-compatible Mac. Turn off the Mac, then turn it on with the option key held down. When asked to select a disk, choose the USB drive.

## Initial Setup

Whenever I've finished installing Mavericks, the first thing I do is open Terminal and run:curl mavericksforever.com/postinstall.sh | shThis script willUpdate Mavericks to the latest version available.Change some default settings to resemble Snow Leopard.Remove apps and features which don't work anymore, and would just make me sad if I saw them.The result of this script represents how I want to be greeted by a fresh Mavericks system.### Internet#### Web BrowsingWe need a modern web browser! Luckily, the incredible i3roly has us covered with Firefox Dynasty, a fully up-to-date version of Firefox modified to work on old versions of OS X. It works just like mainline Firefox, with every website that mainline Firefox does.I created a small Preference Pane which makes it easy to download new builds of Firefox Dynasty, and attempts to make Firefox better comform to Apple's Human Interface Guidelines. All real credit goes to i3roly.### Firefox Dynasty DownloaderFor OS X 10.7 – 10.9Last Updated August 14, 2025Browser maintained by i3rolySmall tweaks by WowfunhappyDownloadAfter installing the Preference Pane, I recommend completely deleting the ancient version of Safari included with Mavericks. Safari 9 isnotsafe to use in 2025!sudo rm -r /Applications/Safari.app#### Aqua ProxyFirefox Dynasty covers our web browsing needs, but we'll still run into trouble with other internet-enabled apps. Dictionary will say it can't connect to Wikipedia, and Mail will be unable to load many embedded images.These problems stem from Mavericks's outdated implementation of HTTPS/SSL/TLS. To fix them, use Aqua Proxy:### Aqua ProxyFor OS X 10.6 – 10.10Last Updated: June 14, 2025Created by WowfunhappyHelp old versions of Mac OS X talk to the modern internet.DownloadAqua Proxy is what's typically referred to as a local "Man-in-the-Middle Proxy Server". It sits between you and the internet, captures your computer's traffic, and modifies it to be compatible with modern servers before sending it on its way.### EmojisThe Unicode Consortium has introduced a lot of new emojis since Mavericks was released. We need to add them to Mavericks!### Emoji Update for MavericksFor OS X 10.8 – 10.9Last Updated October 13, 2020Created by WowfunhappyAdds newer emojis to the Mavericks emoji picker.Download### Time MachineThis will be short. Please do grab a USB hard drive and use it to set up Time Machine in System Preferences.Backups are good, and once Time Machine is set up, you can make a change to your system and then easily undo it later. For example...### Delete Applications You Don't UseIf you try to drag the Chess app to the trash, Finder will complain that "'Chess' can't be modified or deleted because it's required by OS X." Finder is wrong; Chess is not required, and you can delete it using the Terminal.I don't play Chess. I also don't use iTunes, don't own any DVDs, and don't read Apple iBooks on my computer. So, on a fresh install of Mavericks, I like to open the Terminal and run:sudo rm -rf "/Applications/Chess.app"sudo rm -rf "/Applications/DVD Player.app"sudo rm -rf "/Applications/iTunes.app"sudo rm -rf "/Applications/iBooks.app"Don't youlovehow hackable everything is? Removing stock apps from the Applications folder is completely safe—nothing will break—and this isyourcomputer, so you should make it your own. You can always restore apps later using Time Machine. Just don't delete System Preferences, or anything in the Utilities folder.

## Security Patches

Apple has not released a security patch for Mavericks since 2016. Today, it an inherently vulnerable operating system, and you will need to be a bit careful. Regularly back up your data to cold storage, never use an outdated web browser, and always keep your router's firmware up-to-date.

Although they are by no means comprehensive, I've also made some security patches you should install:

### Mail Security Patch

For OS X 10.9

Last Updated August 3, 2021

Created by Wowfunhappy

A mail plugin that fixes CVE-2020-9922, a zero-click vulnerability in Apple Mail.

Download

### Font Security Patch

For OS X 10.9

Last Updated July 18, 2025

Created by Wowfunhappy

with directions from Krackers

A small patch for the CVE-2023-41990 vulnerability.

Download

After installing the Font Security Patch, youmustkeepSystem Preferences→Security & Privacy→General→Allow apps downloaded fromset to "Anywhere", because the patched file has a different code signature.

## Logging Into Online Services

Logging into internet accounts from Mavericks can be a bit tricky sometimes. Here are guides for some common online services:

### Apple Accounts / iCloud

##### iCloud Contacts and Calendars

Start by logging in toSystem Preferences→Internet Accountswith the standard username and password for your Apple Account. System Preferences will say that "an Apple ID verification code is required" and you should recieve a verification code on one of your other devices.

Sign in again, but this time, put your password followed by the verification code you recieved into the password field. For example, if your password wascorrecthorsebatterystapleand your verification code was123456you would putcorrecthorsebatterystaple123456in the password field.

##### iCloud Mail and Notes

Make sure Aqua Proxy is installed. Then:

1. Create an app-specific passwordfor your Apple account
2. InSystem Preferences→Internet Accounts, clickAdd Other Account...
3. SelectAdd a Mail Accountand clickCreate...
4. Enter your name, email address ending in @icloud.com, and app password.
5. UnderIncoming Mail Server Info, enter:* Page 1:Account Type: IMAPMail Server: localhostUser Name: (your email) @icloud.com@imap.mail.me.comExample:johnappleseed@icloud.com@imap.mail.me.comYour user name should include exactly two @ symbols.Password: (your app password)
* Account Type: IMAP
* Mail Server: localhost
* User Name: (your email) @icloud.com@imap.mail.me.comExample:johnappleseed@icloud.com@imap.mail.me.comYour user name should include exactly two @ symbols.
* Example:johnappleseed@icloud.com@imap.mail.me.com
* Your user name should include exactly two @ symbols.
* Password: (your app password)
* Page 2:Path Prefix: (leave blank)Port: 6532Use SSL: (disable/uncheck)Authentication: Password
* Path Prefix: (leave blank)
* Port: 6532
* Use SSL: (disable/uncheck)
* Authentication: Password
6. UnderOutgoing Mail Server Info, enter:* Page 1:SMTP Server: localhostUser Name: (your email) @icloud.com@smtp.mail.me.comExample:johnappleseed@icloud.com@smtp.mail.me.comAgain, your user name should include two @ symbols.Password: (your app password)
* SMTP Server: localhost
* User Name: (your email) @icloud.com@smtp.mail.me.comExample:johnappleseed@icloud.com@smtp.mail.me.comAgain, your user name should include two @ symbols.
* Example:johnappleseed@icloud.com@smtp.mail.me.com
* Again, your user name should include two @ symbols.
* Password: (your app password)
* Page 2:Port: 6533Use SSL: (disable/uncheck)Authentication: Password
* Port: 6533
* Use SSL: (disable/uncheck)
* Authentication: Password

For MobileMe email addresses, substitute "@me.com" for "@icloud.com" above.

##### iMessage

Wait at least 30 minutes without attempting to sign in to any Apple services. Then:

1. InSystem Preferences→iCloud, click the box next toKeychain. If prompted "Requiring a password to unlock your screen is recommended", choose "Not Now". We are not actually going to enable iCloud Keychain.
2. Enter the password for your Apple account. System Preferences will say "iCloud Keychain could not be turned on", which is fine. However, you should recieve a verification code from Apple.
3. In the Messages app, sign into iMessage with (1) your Apple ID and (2) your password followed by the verification code you recieved. For example, if your password washunterand your verification code was654321, you would enterhunter654321in the password field.

If anything goes wrong, you may need to wait 30 minutes before trying again.

##### What Doesn't Work

iCloud Keychain will not work on Mavericks. I recommend using Bitwarden to manage passwords.

On most Apple accounts, Reminders created in Mavericks will not sync to other Apple devices via iCloud. To use Reminders across multiple devices, I recommendfruux.com.

You will not be able to log in to FaceTime on Mavericks.

#### Google Accounts

##### Login Instructions

To log in to a Google account from Mavericks, you will need to use an "app password" in lieu of your normal password. Go tomyaccount.google.com/security, select the "app passwords" option, and follow the instructions.

If you don't see an option for "app passwords", you will need to turn on "2-Step Verification" to make it appear. Unfortunately, there is no way to avoid turning on 2-Step Verification.

##### Troubleshooting

For some reason, a small number of Google accounts need to be added to Mavericks in a different way. If you are using an app password but still can't seem to sign in, follow the below instructions instead. This is usually not necessary and still requires an app password.

1. EmailInSystem Preferences→Internet Accounts, clickAdd Other Account...SelectAdd a Mail accountEnter your full email address and app password where indicatedWhen asked which services to enable, deselect everything except Mail
2. InSystem Preferences→Internet Accounts, clickAdd Other Account...
3. SelectAdd a Mail account
4. Enter your full email address and app password where indicated
5. When asked which services to enable, deselect everything except Mail
6. CalendarInSystem Preferences→Internet Accounts, clickAdd Other Account...SelectAdd a CalDAV accountEnter your full email address and app password where indicatedSet theserver addresstoapidata.googleusercontent.comEnter your full email address and app password where indicated
7. InSystem Preferences→Internet Accounts, clickAdd Other Account...
8. SelectAdd a CalDAV account
9. Enter your full email address and app password where indicated
10. Set theserver addresstoapidata.googleusercontent.com
11. Enter your full email address and app password where indicated

## Media Playback

### QuickTime Player

I just love watching videos in QuickTime Player X! It has a beautiful interface which gets out of the way when I don't need it but comes back exactly when I do.

Unfortunately, QuickTime works with very few video formats. It used to have a plugin infrastructure, which would have made it possible to add support for new video codecs like VP9 and HEVC—but wouldn't you know it, Apple removed plugin support beginning with version 10.3 introduced in, wait for it, Mavericks!

Well, that won't do! Replace QuickTime 10.3 with this patched version of QuickTime 10.2 from Mountain Lion.

### QuickTime Player X 10.2 Mod

For OS X 10.9

Last Updated: June 18, 2025

Created by Wowfunhappy

A version of QuickTime Player X 10.2 from Mountain Lion, modified to work on Mavericks. Supports third-party QuickTime components.

Download

### Components

Now install some components so QuickTime can play more types of media!

### Flip4Mac

For QuickTime 7 – 10.2

Created by Telestream, Inc.

Open and play .wmv and .wma files in QuickTime.

Download

### WFH Components

For QuickTime 7 – 10.2

Last Updated: June 23, 2025

Created by Wowfunhappy

Based on Perian

Open .mkv, .webm, and .flv files, play E‑AC‑3 and OPUS audio, play HEVC, VP9, AV1, and DivX video, and more.

Download

### XiphQT

For QuickTime 7 – 10.2

Created by Xiph.Org

Open and play .ogg and .ogv files in QuickTime.

Xiph.org ➢

With these components installed, QuickTime should be able to play every mainstream video format you come across.

There is one caveat. Some modern video formats require a lot of processing power to play at full speed. Newer devices use "hardware decoders" built into their chips to play these formats, but Mavericks-era hardware does not have that luxury. Your mileage will vary depending on your computer, the type of video, and the video's resolution and framerate.

### Downloading Videos

Now all we need are videos to play in QuickTime! Here are some ways to get them.

### Media Subscriptions

For OS X 10.9

Last Updated August 17, 2025

Created by Wowfunhappy

Add links to Youtube channels in System Preferences. Wake up to new videos in your Movies folder each morning.

Download

### Download Video Service

For OS X 10.6 – 10.14

Last Updated July 19

Created by Wowfunhappy

Download Youtube videos by highlighting the link, right clicking, and choosingServices→Download Video. It will appear in the Movies folder when ready.

Download

To download from Firefox, click and drag your mouse over the text of the URL to highlight it before you right click. Merely clicking to highlight won't work due to a Firefox bug.

## Archives & Images

Next, let's make Apple's other apps work with more types of files. I want to be able to open 7z files in Archive Utility and WebP images in Preview. These apps don't come with a built-in plugin infrastructure like QuickTime, so we'll need to install SIMBL.

### SIMBL for Mavericks

For OS X 10.9

Last Updated July 19

Original by Mike Solomon & w0lfschild

Updated by Wowfunhappy

An app enhancement system for the Mac. SIMBL makes it possible to install plugins that add functionality to existing apps.

Download

Now we're ready to install some SIMBL plugins!

### Archive Utility Plus

For OS X 10.9

Last Updated August 18

Created by Wowfunhappy

Allows Archive Utility to expand .7z, .rar, and other types of compressed files.

Download

### Preview Plus

For OS X 10.9

Last Updated July 31

Created by Wowfunhappy

Allows Preview to open WebP, HEIC, and AVIF images, as well as Markdown documents.

Download

##### Technical Details, for the Curious

###### Archive Utility

For most formats, Archive Utility works by calling command-line programs such as tar or gunzip to do the actual decompression. We can do that too! The plugin tells Archive Utility to use a copy of 7zz included in the bundle to decompress new formats.

###### Preview

Preview natively uses QuickLook generators to display iWork and Microsoft Office documents. The QuickLook API is well-documented, and many third-party generators exist, including for all the formats we'd like to work in Preview! Unfortunately, Preview has a built-in whitelist of file types it will display via QuickLook generators. The SIMBL plugin merely adds new formats to this whitelist.

## Customizations

Finally, some additional options for customizing your amazing Mavericks system!

### SIMBL Customization Plugin Pack

For OS X 10.9

Last Updated August 11

Created by various authors

A small collection of additional SIMBL plugins to further tailor your experience. Requires SIMBL. See the readme for information on what each plugin does.

Download

### Snow Leopard Window Controls

For OS X 10.9 Without a Retina screen

Last Updated July 19, 2025

Created by Wowfunhappy

A theme to make Mavericks's "traffic light" window control buttons larger, and its window chrome slightly darker, similar to Snow Leopard. Should only be used with standard-DPI "non-retina" screens.

Download

## That's it!

And with that, your computer should be all set up! If you're looking for more compatible apps, head over to the app library!

### Mavericks App Library
