---
title: Changelog 32 - Slick Seventeen, Awesome Applications, Universal USB Tools – LineageOS
url: https://lineageos.org/Changelog-32/
site_name: hackernews_api
content_file: hackernews_api-changelog-32-slick-seventeen-awesome-applications
fetched_at: '2026-10-11T16:32:52.733952'
original_url: https://lineageos.org/Changelog-32/
author: LineageOS
date: '2026-10-11'
description: You know what's funnier than 24?
tags:
- hackernews
- trending
---

# Changelog 32 - Slick Seventeen, Awesome Applications, Universal USB Tools

###### Written on October 11, 2026 by Nolen Johnson (npjohnson)

## 24 - Getting Sentimental

Hey there! Welcome back!

We’re a bit sentimental about this release, as it precedes a really fun upcoming milestone.

On December 24, 2026, LineageOS will celebrate 10 years. It’s a remarkable milestone for a project
built by a passionate community of developers, maintainers, contributors, and users who have kept
so many devices alive along the way.

This release is part of that story: one more step forward, and a small moment to appreciate how
far we’ve come. Here’s to the next decade. And thank you for your continued patronage, support,
and belief in the project.

The last year has been crazy, but we have remained dedicated to bringing
an updated LineageOS based on Android 17 to the masses!

We’ve been hard at work rebasing all of our changes and features since Android 17’s release in June.
Android 17’s first release mainly contained iterative improvements and some UI/UX refinements, but
due to our previous efforts adapting to Google’s heavy refactoring over the last several versions,
we were able to rebase onto Android 17’s code-base faster than anticipated. Yes you read that right:
We’re early this year!

### Security Patches

* Security patches from August 2025 to October 2026 have been merged to LineageOS 18.1 through 24.0.As always, we will merge full security bulletins and change the security patch level string to match
on all branches that Google actively distributes bulletins for - which as of writing is Android 14
(LineageOS 21) and newer.We also plan to continue backporting and merging security bulletin patches to 18.1, 19.1, and 20.0,
though as there is no “attestable” set of patches provided by Google for these versions, we will not
 modify the security patch level string.
* As always, we will merge full security bulletins and change the security patch level string to match
on all branches that Google actively distributes bulletins for - which as of writing is Android 14
(LineageOS 21) and newer.
* We also plan to continue backporting and merging security bulletin patches to 18.1, 19.1, and 20.0,
though as there is no “attestable” set of patches provided by Google for these versions, we will not
 modify the security patch level string.
* Legacy branch patching has progressed greatly:Security patches through November 2025 have been merged for the legacy branches 15.1, 16.0, and 17.1This gets closer to closing the rather exhaustive effort to backport all feasible security patches.The December 2025 bulletins pulled in some rather difficult to backport patches, which we were
unable to adapt - but if you’re able to, push them to Gerrit for review!
* Security patches through November 2025 have been merged for the legacy branches 15.1, 16.0, and 17.1This gets closer to closing the rather exhaustive effort to backport all feasible security patches.The December 2025 bulletins pulled in some rather difficult to backport patches, which we were
unable to adapt - but if you’re able to, push them to Gerrit for review!
* This gets closer to closing the rather exhaustive effort to backport all feasible security patches.
* The December 2025 bulletins pulled in some rather difficult to backport patches, which we were
unable to adapt - but if you’re able to, push them to Gerrit for review!

### Application Updates

LineageOS isn’t just about the OS itself: our suite of core apps continues to evolve as well.
At this point, many of our applications are updated to Material Design 3 Expressive! Go check
them out! This cycle brings some major improvements:

* Canvas - A brand new image editor:Handles all your basic photo editing needs, such as: cropping, white balance, filters, etc.Pairs well with our existing Glimpse gallery, and Aperture camera applications!
* Handles all your basic photo editing needs, such as: cropping, white balance, filters, etc.
* Pairs well with our existing Glimpse gallery, and Aperture camera applications!
* Catapult (Android TV Launcher) - Special thanks to Contributor Timi Rautamäki:A battery indicator was added for mobile devices and handheld consolesVarious UI updates, mainly the animations and icons were revamped.
* A battery indicator was added for mobile devices and handheld consoles
* Various UI updates, mainly the animations and icons were revamped.
* Etar:Updated to the newest upstream version.Multiple fixes having been sent back to the upstream repo!
* Updated to the newest upstream version.
* Multiple fixes having been sent back to the upstream repo!
* Jelly (Browser)Support PWA-like apps via the shortcut mechanism
* Support PWA-like apps via the shortcut mechanism
* Twelve (Music)Improved load times with a large media libraryNow shows your “Most played” albums/genres in activity tabFixed audio tracks getting stuck with offload enabledImproved Jellyfin support.
* Improved load times with a large media library
* Now shows your “Most played” albums/genres in activity tab
* Fixed audio tracks getting stuck with offload enabled
* Improved Jellyfin support.
* Updater - Special thanks to Contributor pjgowtham:More Material Design 3 Expressive goodness! Alongside a complete redesign including better animations and better brandingUpdates arestreamedby default!
This will greatly decrease installation time on A/B devices!Improved UX and logical flow, as well as built-in notes to explain things to usersOn non-A/B, the recovery partition is now automatically updated on the boot subsequent to a successful updateTablet and TV layouts are greatly improved!
* More Material Design 3 Expressive goodness! Alongside a complete redesign including better animations and better branding
* Updates arestreamedby default!
This will greatly decrease installation time on A/B devices!
* Improved UX and logical flow, as well as built-in notes to explain things to users
* On non-A/B, the recovery partition is now automatically updated on the boot subsequent to a successful update
* Tablet and TV layouts are greatly improved!
* Seedvault:Updated to the newest upstream version.Multiple fixes having been sent back to the upstream repo!
* Updated to the newest upstream version.
* Multiple fixes having been sent back to the upstream repo!
* SetupWizard - Special thanks to Contributor Saalim:Complete Material Design 3 Expressive implementation along with new fluid animations and beautiful assetsOnboarding flow rearchitectedDevice-specific hooks to allow maintainers to insert device-specific pages for peripherals/etc.
* Complete Material Design 3 Expressive implementation along with new fluid animations and beautiful assets
* Onboarding flow rearchitected
* Device-specific hooks to allow maintainers to insert device-specific pages for peripherals/etc.
* WebView:Has been updated to version 155.0.8059.30.
* Has been updated to version 155.0.8059.30.

### WebUSB Flash Tools

Installing LineageOS just got a little simpler.

We’re launching new browser-based flash tools for several common device-installation methods:

* ADB
* Fastboot
* Amlogic Burn protocol
* Samsung Odin protocol

These tools use WebUSB to communicate directly with compatible devices from your browser, reducing
the need to find, install, and run separate flashing utilities. They’re designed to make the installation
process more approachable, especially for users who are comfortable following device-specific instructions
but would rather avoid extra desktop software.

This does not replace our existing installation guides. The LineageOS Wiki will continue to document
the established installation methods, and those instructions remain the default and supported path for each device.

Instead, the WebUSB tools are an additional option for users who want a more streamlined flashing
experience. Availability and compatibility will vary by device, browser, operating system, and USB
connection, so please read the tool’s guidance carefully before proceeding.

As always, flashing custom software carries risk. Back up anything important, confirm that you
have selected the correct files and device, and follow the instructions presented by the tool.

You can try the new flash tools atflash.lineageos.org.

We’re excited to offer another way to make installing LineageOS more straightforward, while keeping
our established documentation and workflows intact.

Massive thank you to Contributors Nicholas Lim and Luk1337 for their hard work on these!

### CI/CD Improvements

We’ve done a lot of work to ensure submissions are properly tested and pre-reviewed, as well as build-tested:

Continuous Integration (CI) posts CI+1/CI-1 votes on most application repos, as well as several
other core repos. This CI runs things like:

* pre-committo run any number of processes
* lint/clang-format/other formatting checks
* REUSEcompliance/licensing checks
* Many more specific uses per-repo

Continuous Deployment (CD) now pushes APKs and other such build artifacts in a GitHub Actions
run each time a commit is merged.

### A11Y Accessibility Audit

LineageOS just completed a full end-to-end installation process and application suite Accessibility
Audit that was performed free-of-charge by thea11yproject!

We are greatly appreciative of their amazing work on this audit! The goal was to make LineageOS
more accessible - and some changes such as recovery navigation/UI have already seen reworking.

We are also very thankful for the free accessibility-in-development training they gave
over 40 contributors in a web-seminar!

Stay tuned for more information, and potentially a future blog post on outcomes!

### Deprecations / Legacy Devices

Overall, we feel that the 24.0 branch has reached feature and stability parity with 23.2 and is
ready for initial release.

LineageOS 24.0 will launch building for a decent selection of devices, with additional devices to
come as they meet the requirements specified by theCharterand are
made ready for builds by their maintainer.

We would also like to announce formally that even though some devices using Linux Kernel versions 4.4 and 4.9
have been ported to LineageOS 23.2 and 24.0, we have decided to only accept LineageOS 22.2 submissions for
these devices. The legacy kernel versions and devices associated with them carry countless platform commits
that are rather hacky and difficult to continue to pull forward to newer Android versions.

LineageOS 22.2 still supports many devices running4.4and4.9, and will continue to receive
builds and security patches merged monthly until Google stops distributing official security-bulletins
for Android 15 - and you can still submit new LineageOS 22.2 devices for official builds!

In addition, on LineageOS 23.2/24.0 we’re currently only shipping kernels that have 1:1 eBPF backports,
build fully without GCC, and have many other important backported features.

### Upgrading to LineageOS 24.0

To upgrade, please follow the upgrade guide for your device by navigating to ithereand then by clicking on “Upgrade to a higher version of LineageOS”.

If you’re coming from an unofficial build, you need to follow the good ole’ install guide for your
device, just like anyone else looking to
install LineageOS for the first time. These can be found at the same placehereby clicking on your device and then on “Installation”.

Please note that if you’re currently on an official build, youDO NOTneed to wipe your device,
unless your device’s wiki page specifically dictates otherwise, as is needed for some devices with
massive changes, such as a repartition.

### Careful Commonization

Several of our contributors have been working hard on SoC-specific common kernels that others
can base their kernels on, and merge on a somewhat regular basis to pull in the latest features/security
patches to save maintainers additional effort.

Go check them out and consider basing your device kernels on them!

Supported SoCs right now are:

SoC (system-on-chip)

Kernel Version

Android Version

AMLogic GXL/G12A/G12B/SM1

4.9

13, 14, 15

AMLogic G12A/G12B/SM1/NE/NO

5.15

16, 17

Qualcomm MSM8998/MSM8996

4.4

13, 14, 15

Qualcomm MSM8953

4.9

13, 14, 15

Qualcomm SDM845

4.9

13, 14, 15

Qualcomm SM8150

4.14

13, 14, 15, 16, 17

Qualcomm SDM660

4.19

13, 14, 15, 16, 17

Qualcomm SM8250

4.19

13, 14, 15, 16, 17

Qualcomm SM8350

5.4

13, 14, 15, 16, 17

Qualcomm SM8450

5.10

13, 14, 15, 16, 17

Qualcomm SM8550

5.15

13, 14, 15, 16, 17

Qualcomm SM8650

6.1

14, 15, 16, 17

Qualcomm SM8750

6.6

15, 16, 17

Qualcomm SM8850

6.12

17

Moreover, many legacy devices require interpolating libraries that we colloquially refer to as
“shims” - these have long been device and maintainer managed, but this cycle we have decided to
commonize them to make the effort easier on everyone and not duplicate effort!

You can check it outhereand
contribute shims that other devices may need or add new components to additional
shims and compatibility layers. Head over to ourguideon using Gerrit to get started.

### Wiki

TheLineageOS Wikihas also been expanded over the years and now
offers, in addition to the known and tested instructions for all supported devices, some
improvements:

* Material Design 3 Expressive was implemented where possible!
* OurFAQhas been greatly expanded, and the page redesigned
* Samsung devices: Migrated away from ODIN/Heimdall to the awesome FOSS tool,samloader-rs

We’d also like to remind everyone to follow the instructions on their device’s respectiveWiki page.
Android’s partitioning and update mechanisms have continued to evolve from system-as-root and A/B
partitions to dynamic partitions and Virtual A/B. Through all this change, the “typical” installation
steps that you may have once expected now be incomplete or incorrect for a particular device.

Our maintainers are expected to verify the published instructions for their devices, and the Wiki
provides increasingly flexible, device-specific guidance for installation, updates, and upgrades.
Please use it rather than relying on old guides, video guides, or steps remembered from a previous device.

### Developers, Developers, Developers

Or, in this case, maintainers, maintainers, maintainers. We want your device submissions!

If you’re a developer and would like to submit your device for officials, it’s easier than ever.
Just follow the instructionshere.

The above also applies to people looking to bring back devices that were at one point official but
are no longer supported - seriously - even if it’s not yet completely compliant, submit it! Maybe
we can help you complete it.

After you submit, within generally a few weeks, but in most cases a week, you’ll receive some
feedback on your device submission; and if it’s up to par, you’ll be invited to our communications
channels and your device will be forked to LineageOS’s official repositories.

Don’t have the knowledge to maintain a device, but want to contribute to the platform? We have lots
of other things you can contribute to.
For instance, our apps suite is always looking for new people to helpimprove them, or you cancontribute to the wikiby adding
more useful information & documentation.Gerritis always open for submissions! Once
you’ve contributed a few things, email us at devrel(at)lineageos.org detailing your work, and we’ll
get you in the loop.

### Generic Targets

We’ve talked about these before, but these are important, so we will cover them again.

Although we’ve had buildable generic targets since 2019, to make LineageOS more accessible to
developers, and really anyone interested in giving LineageOS a try, we’ve documented how to use
them in conjunction with the AndroidEmulator/Android Studio!

Additionally, similar targets can now be used to build GSI in mobile, Android TV configurations,
and Android Automotive making LineageOS more accessible than ever to
devices using Google’sProject Treble.
We won’t be providing official builds for these targets, due to the fact the user experience varies
entirely based on how well the device manufacturer complied with Treble’s requirements, but feel
free to go build them yourself and give it a shot!

Please note that Android 12 (and by proxy all later Android versions) diverged GSI and Emulator
targets. Emulator targets reside inlineage_sdk_$arch, while GSI targets reside inlineage_gsi_$arch, andCuttlefishtargets
reside inlineage_cf_$arch.

Additionally, targets now exist for QEMU-based virtual machine software (libvirt, UTM, etc), which
have greatly improved in quality over the past year. Instructions on building and utilizing these
targets can be found onthe Wiki.

And one more thing… The generic targets mentioned above all require either an existing Android device,
or some sort of virtualization/emulation software stack to run. Recently, Contributor 0xCAFEBABE
introduced a very different kind of generic target that can be run on various types of bare-metal
hardware devices.

While it’s still in experimental state, it has successfully booted on:

* Common x86_64 PCs
* Apple Silicon Macs
* NVIDIA DGX Spark
* Qualcomm Snapdragon X Series Laptops
* And potentially more to come!

If interested, please take a look at the documentationhere!

### Translations

Bilingual? Trilingual? Anything-lingual?

If you think you can help translate LineageOS to a different language, jump over toour wikiand have a go!
If your language is not supported natively in Android, reach out to us on Crowdin and we’ll take
the necessary
steps to include your language.
For instance, LineageOS is the first custom Android distribution that has complete support
for the Welsh (Cymraeg) language thanks to its community of translators.

Please, contribute to translations only if you are reasonably literate in the target language;
poor translations waste both our time and yours.

### Build roster

#### Added 24 devices

Device name

Wiki

Maintainers

Moved from

ASUS ZenFone 8

sake

DD3Boh, mikooomich

23.2

ASUS Zenfone Max Pro M1

X00TD

Vivekachooz

20

AYN Odin 2

odin2

AnierinBliss, djchittoor, onelots

23.2

AYN Odin2 Portal

odin2portal

AnierinBliss, balika011, bgcngm

23.2

AYN Thor

odin2thor

AnierinBliss, npjohnson

 

Amazon Fire Max 11

sunstone

R0rt1z2

 

DroidLogic Developer Kit (S905X4-B/K) / DroidLogic ADT-4/4+/4 (Low Ram)

ohm

npjohnson

23.2

F(x)tec Pro¹ X

pro1x

BadDaemon, bgcngm, mccreary, npjohnson, qsnc, tdm

23.2

Fairphone 4

FP4

mikeioannina

23.2

Fairphone 5

FP5

mikeioannina

23.2

Google Pixel 10 Pro Fold

rango

mikeioannina

 

Google Pixel 10 Pro XL

mustang

mikeioannina

 

Google Pixel 10 Pro

blazer

mikeioannina

 

Google Pixel 10

frankel

mikeioannina

 

Google Pixel 10a

stallion

mikeioannina

 

Google Pixel 4 XL

coral

mikeioannina, npjohnson

23.2

Google Pixel 4

flame

mikeioannina, npjohnson

23.2

Google Pixel 4a 5G

bramble

mikeioannina

23.2

Google Pixel 4a

sunfish

mikeioannina

23.2

Google Pixel 5

redfin

mikeioannina

23.2

Google Pixel 5a

barbet

mikeioannina

23.2

Google Pixel 6 Pro

raven

mikeioannina

23.2

Google Pixel 6

oriole

mikeioannina

23.2

Google Pixel 6a

bluejay

mikeioannina

23.2

Google Pixel 7 Pro

cheetah

mikeioannina

23.2

Google Pixel 7

panther

mikeioannina

23.2

Google Pixel 7a

lynx

mikeioannina, niclimcy

23.2

Google Pixel 8 Pro

husky

mikeioannina

23.2

Google Pixel 8

shiba

mikeioannina

23.2

Google Pixel 8a

akita

mikeioannina

23.2

Google Pixel 9 Pro Fold

comet

mikeioannina

23.2

Google Pixel 9 Pro XL

komodo

mikeioannina

23.2

Google Pixel 9 Pro

caiman

mikeioannina

23.2

Google Pixel 9

tokay

mikeioannina

23.2

Google Pixel 9a

tegu

mikeioannina

23.2

Google Pixel Fold

felix

mikeioannina

23.2

Google Pixel Tablet

tangorpro

LuK1337, mikeioannina, npjohnson

23.2

Lenovo Z5 Pro GT

heart

themard, optionaltoast

23.2

Lenovo Z6 Pro

zippo

Lucchetto, themard, einargednochsson

23.2

Motorola ThinkPhone by motorola

bronco

demon000, elginsk8r

23.2

Motorola defy 2021

bathena

Deivid Ignacio Parra (Deivid21), Francisco Sanchez (Fraaxius)

23.2

Motorola edge 20 pro

pstar

npjohnson, SGCMarkus

23.2

Motorola edge 20

berlin

npjohnson, SGCMarkus

23.2

Motorola edge 2021

berlna

SyberHexen

23.2

Motorola edge 2024

avatrn

elginsk8r

23.2

Motorola edge 30 fusion / Motorola moto S30 Pro

tundra

themard, electimon, npjohnson

23.2

Motorola edge 30 neo

miami

marcost2

23.2

Motorola edge 30

dubai

themard, sb6596, Demon000

23.2

Motorola edge 40 pro / Motorola moto X40 / Motorola edge+ (2023)

rtwo

sgcmarkus, themard

23.2

Motorola edge s / Motorola moto g100

nio

dianlujitao

23.2

Motorola moto e7 plus / Lenovo K12

guam

Rajin Gangadharan (GRajin), Deivid Ignacio Parra (Deivid21)

23.2

Motorola moto g 5G - 2024

fogo

mikeioannina

23.2

Motorola moto g power 2021

borneo

Syed Fawwaz Hussain (Fazwalrus), Deivid Ignacio Parra (Deivid21)

23.2

Motorola moto g stylus 5G (2022)

milanf

AnierinBliss

23.2

Motorola moto g stylus 5G (2023)

genevn

elginsk8r, mikeioannina

23.2

Motorola moto g stylus 5G

denver

Vivekachooz

23.2

Motorola moto g10 / Motorola moto g10 power / Lenovo K13 Note

capri

Deivid Ignacio Parra (Deivid21), Sultanahamer

23.2

Motorola moto g15 / Motorola moto g15 power / Motorola moto g05

lamu

R0rt1z2, surblazer

23.2

Motorola moto g200 5G / Motorola Edge S30

xpeng

themard

23.2

Motorola moto g30 / Lenovo K13 Pro

caprip

mikeioannina, Deivid Ignacio Parra (Deivid21)

23.2

Motorola moto g32

devon

Dhina17, mikeioannina, Deivid Ignacio Parra (Deivid21)

23.2

Motorola moto g34 5G / Motorola moto g45 5G

fogos

mikeioannina

23.2

Motorola moto g42

hawao

Dhina17, mikeioannina, Deivid Ignacio Parra (Deivid21)

23.2

Motorola moto g50

ibiza

Onelots

23.2

Motorola moto g52

rhode

Dhina17, mikeioannina, tomoms, Deivid Ignacio Parra (Deivid21)

23.2

Motorola moto g82 5G

rhodep

AnandSuresh02, sevenrock

23.2

Motorola moto g84 5G

bangkk

mikeioannina

23.2

Motorola moto g9 play / Motorola moto g9 / Lenovo K12 Note

guamp

DelightReza, Deivid Ignacio Parra (Deivid21)

23.2

Motorola moto g9 power / Lenovo K12 Pro

cebu

Deivid Ignacio Parra (Deivid21)

23.2

Motorola one action

troika

Stricted, npjohnson, DaemonMCR

23.2

Motorola one vision / Motorola p50

kane

Stricted, npjohnson, DaemonMCR

23.2

Nothing Phone (1)

Spacewar

zlewchan, ko_ko_konb

23.2

Nubia Mini 5G

TP1803

ArianK16a, npjohnson

23.2

OSOM OV1

pyrite

mikeioannina, npjohnson

23.2

OnePlus 11 5G

salami

bgcngm

23.2

OnePlus 12R

aston

inferno0230

23.2

OnePlus 13

dodge

bgcngm, chandu078, dianlujitao, ItsVixano

23.2

OnePlus 15

infiniti

chandu078

 

OnePlus 15T

fairlady

LuK1337

 

OnePlus 7 Pro / OnePlus 7 Pro (T-Mobile)

guacamole

LuK1337, elginsk8r

23.2

OnePlus 7

guacamoleb

shantanu-sarkar

23.2

OnePlus 7T / OnePlus 7T (T-Mobile)

hotdogb

LuK1337, Onelots

23.2

OnePlus 7T Pro

hotdog

qsnc

23.2

OnePlus 8 / OnePlus 8 (T-Mobile)

instantnoodle

jabashque

23.2

OnePlus 8 Pro

instantnoodlep

LuK1337

23.2

OnePlus 8T / OnePlus 8T (T-Mobile)

kebab

LuK1337, mikeioannina

23.2

OnePlus 9 / OnePlus 9 (T-Mobile)

lemonade

mikeioannina, tangalbert919, ZVNexus

23.2

OnePlus 9 Pro / OnePlus 9 Pro (T-Mobile)

lemonadep

LuK1337, bgcngm, mikeioannina

23.2

OnePlus 9R

lemonades

DaemonMCR, Tuan Anh

23.2

OnePlus 9RT

martini

basamaryan

23.2

OnePlus Ace 3

astonc

inferno0230

23.2

OnePlus Ace 5 Pro

hummer

awa-xaga

23.2

OnePlus Nord CE 2 Lite 5G

oscaro

Vivekachooz

23.2

OnePlus Nord CE 3 Lite 5G / OnePlus Nord N30 5G

larry

Vivekachooz

23.2

OnePlus Nord CE4

benz

inferno0230

23.2

OnePlus Nord N10

billie

danascape

21

OnePlus Nord N200

dre

tangalbert919, elginsk8r

23.2

OnePlus Pad 2 Pro / OnePlus Pad 3

erhai

LuK1337, bgcngm

23.2

OnePlus Pad 3 Pro / OnePlus Pad 4

iceland

StudioKeys

 

Razer Edge 5G / Razer Edge WiFi

nicole

AnierinBliss, balika011, mikeioannina, npjohnson

23.2

Realme 10 Pro 5G

luigi

Vivekachooz

23.2

Realme 9 5G

oscarru

Vivekachooz

 

Realme 9 Pro 5G

oscar

Vivekachooz

23.2

Realme GT7 Pro Racing Edition

piloti

ItsVixano

 

Realme GT7 Pro

pista

kmiit

 

Realme Q5

oscarc

Vivekachooz

 

Retroid Pocket 6

RP6

AnierinBliss

23.2

Retroid Pocket Nova

RPN

AnierinBliss

23.2

SDMC DV9135

tifa

Tuan Anh

 

SHIFTphone 8.0 / SHIFTphone 8.1

otter

amartinz, mikeioannina

23.2

Samsung Galaxy A21s

a21s

DaemonMCR

23.2

Samsung Galaxy A52 4G

a52q

Simon1511

23.2

Samsung Galaxy A52s 5G

a52sxq

Simon1511

23.2

Samsung Galaxy A72

a72q

Simon1511

23.2

Samsung Galaxy A73 5G

a73xq

Simon1511

23.2

Samsung Galaxy M52 5G

m52xq

Simon1511

23.2

Samsung Galaxy Note20 (4G/5G)

c1s

CmdCtrlDevic3

23.2

Samsung Galaxy Note20 Ultra (4G/5G)

c2s

CmdCtrlDevic3

23.2

Samsung Galaxy S20 (4G/5G)

x1s

ExtremeXT, fcuzzocrea

23.2

Samsung Galaxy S20 FE (Exynos)

r8s

CmdCtrlDevic3

23.2

Samsung Galaxy S20 Ultra (5G)

z3s

ExtremeXT, fcuzzocrea

23.2

Samsung Galaxy S20+ (4G/5G)

y2s

ExtremeXT, fcuzzocrea

23.2

Samsung Galaxy S22 Ultra

b0s

ExtremeXT

23.2

Samsung Galaxy S22

r0s

ExtremeXT

23.2

Samsung Galaxy S22+

g0s

ExtremeXT

23.2

Samsung Galaxy S23

dm1q

DaemonMCR, josip-k, krazey

23.2

Samsung Galaxy Tab A7 10.4 2020 (LTE)

gta4l

chrmhoffmann

23.2

Samsung Galaxy Tab A7 10.4 2020 (Wi-Fi)

gta4lwifi

chrmhoffmann

23.2

Samsung Galaxy Tab S7 (LTE)

gts7l

bgcngm

23.2

Samsung Galaxy Tab S7 (Wi-Fi)

gts7lwifi

bgcngm

23.2

Samsung Galaxy Tab S7+ (LTE/5G)

gts7xl

bgcngm

 

Samsung Galaxy Tab S7+ (Wi-Fi)

gts7xlwifi

bgcngm

 

Solana Saga

ingot

mikeioannina, npjohnson, tomoms

23.2

Sony Xperia 1 II

pdx203

hellobbn

23.2

Sony Xperia 1 III

pdx215

hellobbn

23.2

Sony Xperia 1 IV

pdx223

Tuan Anh

23.2

Sony Xperia 1 V

pdx234

hellobbn

23.2

Sony Xperia 1 VI

pdx245

BotchedRPR

23.2

Sony Xperia 10 IV

pdx225

LuK1337, jmpfbmx

23.2

Sony Xperia 10 V

pdx235

jmpfbmx, LuK1337

23.2

Sony Xperia 10 VII

pdx257

LuK1337, jmpfbmx

23.2

Sony Xperia 10

kirin

LuK1337

23.2

Sony Xperia 5 II

pdx206

kyasu, hellobbn

23.2

Sony Xperia 5 III

pdx214

kyasu, hellobbn

23.2

Sony Xperia 5 IV

pdx224

Tuan Anh, wolfhechel

23.2

Sony Xperia 5 V

pdx237

kyasu, hellobbn

23.2

Sony Xperia XA2 Plus

voyager

LuK1337

23.2

Sony Xperia XA2 Ultra

discovery

LuK1337

23.2

Sony Xperia XA2

pioneer

LuK1337, jmpfbmx

23.2

Xiaomi 12 Pro

zeus

Aelin, ArianK16a

23.2

Xiaomi 12

cupid

Aelin, ArianK16a

23.2

Xiaomi 12S Pro

unicorn

Aelin, ArianK16a

23.2

Xiaomi 12S Ultra

thor

Aelin, ArianK16a

23.2

Xiaomi 12S

mayfly

Flower Sea

23.2

Xiaomi 12T Pro / Xiaomi Redmi K50 Ultra

diting

Aelin, ArianK16a

23.2

Xiaomi 13 Pro

nuwa

Minus

23.2

Xiaomi 13

fuxi

lolipuru

23.2

Xiaomi MIX Fold 2

zizhan

Aelin, ArianK16a

23.2

Xiaomi Mi 10 Pro

cmi

luffitys

23.2

Xiaomi Mi 10 Ultra

cas

binbin323

23.2

Xiaomi Mi 10T / Xiaomi Mi 10T Pro / Xiaomi Redmi K30S Ultra

apollon

Khalvat-M, Ramisky

23.2

Xiaomi Mi 10T Lite 5G / Xiaomi Mi 10i 5G / Xiaomi Redmi Note 9 Pro 5G

gauguin

Penguin766, Lynnrin

23.2

Xiaomi Mi A3

laurel_sprout

Skyblueborb, Onelots

23.2

Xiaomi POCO F3 / Xiaomi Redmi K40 / Xiaomi Mi 11X

alioth

althafvly, chrmhoffmann

23.2

Xiaomi POCO F5 (Global) / Xiaomi POCO F5 (India) / Xiaomi Redmi Note 12 Turbo

marble

Aelin, ArianK16a

23.2

Xiaomi POCO F5 Pro / Xiaomi Redmi K60

mondrian

Aelin, ArianK16a

23.2

Xiaomi POCO F6 Pro / Xiaomi Redmi K70

vermeer

Lunark

23.2

Xiaomi Redmi 12C / Xiaomi Redmi 12C NFC / Xiaomi POCO C55

earth

surblazer

23.2

Xiaomi Redmi 9

lancelot

surblazer

23.2

Xiaomi Redmi K60 Pro

socrates

WenHao2130

23.2

Xiaomi Redmi Note 10S / Xiaomi Redmi Note 10S NFC / Xiaomi Redmi Note 10S Latin America / Xiaomi POCO M5s

rosemary

surblazer

23.2

Xiaomi Redmi Note 8 / Xiaomi Redmi Note 8T

ginkgo

Skyblueborb, mikeioannina, programminghoch10

23.2

Xiaomi Redmi Note 9

merlinx

surblazer

23.2

Zinwa Q25 Pro

Q25

electimon, basamaryan, npjohnson, Androbots

23.2

#### Added 23.2 devices

Device name

Wiki

Maintainers

Moved from

LG Velvet 5G

caymanlm

lifehackerhansol, Simex

 

LG Wing

winglm

Simex

 

Motorola edge 30 ultra

eqs

demon000, Tomoms

22.2

Nubia Red Magic 5G (Global) / Nubia Red Magic 5G (China) / Nubia Red Magic 5S (Global) / Nubia Red Magic 5S (China)

nx659j

zlewchan

22.2

Xiaomi Mi 11 Pro

mars

WilliamSado

22.1

Xiaomi Mi 11i / Xiaomi Redmi K40 Pro / Xiaomi Redmi K40 Pro+ / Xiaomi Mi 11X Pro

haydn

adarshgrewal

22.2

#### Added 22.2 devices

Device name

Wiki

Maintainers

Moved from

AYN Odin (M0)

odin_m0

rtx4d

 

AYN Odin (M2)

odin_m2

rtx4d

 

Freebox Pop / TV (Realtek Wi-Fi/Bluetooth)

nicepool_rtk

chrmhoffmann, npjohnson

 

Google ADT-2

beast

npjohnson

 

LG G6 (Canada - ENG BL)

h873

npjohnson, Simex, basamaryan, Androbots, AShiningRay, ROMSG, Geel

21