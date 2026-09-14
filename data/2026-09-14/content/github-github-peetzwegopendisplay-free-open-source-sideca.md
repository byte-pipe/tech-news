---
title: 'GitHub - peetzweg/opendisplay: Free, open-source Sidecar/Duet alternative — use your iPhone or iPad as a true second monitor for your Mac over USB or WiFi. Low latency H.264, Retina HiDPI, touch input. · GitHub'
url: https://github.com/peetzweg/opendisplay
site_name: github
content_file: github-github-peetzwegopendisplay-free-open-source-sideca
fetched_at: '2026-09-14T16:47:19.916993'
original_url: https://github.com/peetzweg/opendisplay
author: peetzweg
description: Free, open-source Sidecar/Duet alternative — use your iPhone or iPad as a true second monitor for your Mac over USB or WiFi. Low latency H.264, Retina HiDPI, touch input. - peetzweg/opendisplay
---

peetzweg

 

/

opendisplay

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork245
* Star3.4k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

271 Commits
271 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
Mac
Mac
 
 
MacReceiver
MacReceiver
 
 
MacTests
MacTests
 
 
Shared
Shared
 
 
assets
assets
 
 
fastlane
fastlane
 
 
iOS
iOS
 
 
public
public
 
 
src
src
 
 
tools
tools
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
COMPATIBILITY.md
COMPATIBILITY.md
 
 
Gemfile
Gemfile
 
 
Gemfile.lock
Gemfile.lock
 
 
LICENSE
LICENSE
 
 
PROTOCOL.md
PROTOCOL.md
 
 
README.md
README.md
 
 
generate.sh
generate.sh
 
 
index.html
index.html
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
project.yml
project.yml
 
 
run.sh
run.sh
 
 
tsconfig.json
tsconfig.json
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

# OpenDisplay

Turn your spare Apple devices into second monitors for your Mac — free, open source, no subscription.

iPhone, iPad, and spare Macs. A self-hosted
alternative to Apple Sidecar, Duet Display, and Luna Display: true extended
display (not just mirroring), Retina-sharp, over USB or WiFi, with touch and
scroll input.

Website·Quick start·How it works·FAQ·Contributing

## Why OpenDisplay exists

Turning an iPhone or iPad into an external display for a Mac is a solved
problem — but every existing option has a catch:

* Apple Sidecaris free but requires both devices on thesame Apple ID,
doesn't support iPhones at all, and only works on supported hardware pairs.
* Duet Displaymoved to a subscription.
* Luna Displayrequires a hardware dongle.

OpenDisplay is the missing option: afree, open-source, no-account,
no-dongleway to use the iOS device you already own as a true second
display. If you were about to write your own — don't! Contribute here
instead; the hard parts (virtual display creation, low-latency H.264
pipeline, USB transport, input injection) are already working.

## Features

* 🖥️True display extension— macOS treats the device as a real second
monitor (drag windows to it, arrange it in System Settings), not a mirror.
Mirroring is also available as a mode.
* 🔌USB-wired for lowest latency— streams over the Lightning/USB-C
cable via macOS's built-inusbmuxd; plug in and go, no network, no
WiFi jitter, no helper tools.
* 📶WiFi with zero config— the iPhone advertises itself via Bonjour;
pick it from a dropdown on the Mac.
* 🔍Retina / HiDPI— the virtual display matches the device panel
pixel-for-pixel (@2x), so text is sharp.
* 👆Touch input built in— your iPhone becomes a touchscreen for macOS:tap to click,drag to drag, andtwo-finger scrollthat feels
like a trackpad. (Apple Pencil support is on the roadmap.)
* 🔄Portrait or landscape— rotate the device and the virtual display
rebuilds itself as a vertical monitor at native resolution.
* ⚡Low-latency pipeline— hardware H.264 encode (VideoToolbox,
real-time mode, no B-frames), TCP_NODELAY, frame-drop backpressure with
keyframe recovery, decode-and-render viaAVSampleBufferDisplayLayer.
* 💻A spare Mac as a display— install the smallOpenDisplay
Receiverapp (macOS 12+) on an old Mac and any other Mac extends onto it
over WiFi or a Thunderbolt/Ethernet cable, at native Retina resolution.
* 🔒Self-hosted & private— your screen never touches anyone's server.
Two small apps, one TCP connection, that's it.

## Comparison

OpenDisplay

Apple Sidecar

Duet Display

Luna Display

Price

Free, open source

Free

Subscription

$$$ + dongle

iPhone as display

✅

❌ (iPad only)

✅

✅

Different Apple IDs

✅

❌

✅

✅

Wired (USB)

✅

✅

✅

❌

True extension

✅

✅

✅

✅

Touch input

✅

✅

✅

✅

Self-hosted / auditable

✅

—

❌

❌

## FAQ

Why do I see the purple screen-recording indicator in the menu bar?That's a macOS privacy indicator shown foranyapp that captures the
screen — Duet, Luna, OBS, and Zoom trigger it too. Apple Sidecar doesn't,
only because it's implemented inside the OS rather than on public capture
APIs. It cannot (and shouldn't) be hidden by an app; it's how macOS tells
you a capture is running.

The Mac app doesn't show my iPhone in the Connection menu (WiFi).Both sides needLocal Networkpermission, and both failsilentlywithout it: check Privacy & Security → Local Network on the Macandon
the iPhone, make sure both are on the same WiFi network, and keep the
iPhone app open in the foreground. USB mode is unaffected.

What USB cable or version do I need?Your cablemust support data— a
charge-only USB cable willnotwork. Look for a cable described as adata,sync, orcharging and data-transfercable. A data-capable USB 2.0
cable is enough; USB 3, Thunderbolt, and video Alt Mode are not required.
OpenDisplay streams H.264 over a TCP connection through macOS's built-inusbmuxd, not as a USB video device. Its highest-quality preset uses 18 Mb/s,
well below USB 2.0's 480 Mb/s high-speed link rate, so USB 2.0 has ample
bandwidth for the stream. USB 1.x is not supported or tested. For best
reliability, use a known-good data/sync cable, unlock the device, accept theTrust This Computerprompt if it appears, and avoid unreliable hubs or
adapters.

Does it support iPad?The receiver app is universal (iPhone + iPad);
iPad is the same codebase. iPad-specific polish (Pencil, pressure) is on the
roadmap.

Can another Mac be the display?Yes. InstallOpenDisplay Receiver(a separate, small app from the same release) on the spare Mac. It only needsmacOS 12 Montereyor newer, so Macs from around 2015 onward qualify even
though the sending Mac needs macOS 14. The receiver shows up on the sending Mac
like a phone does and becomes a real extended Retina display. Over WiFi it works out of the box. For a cable, connect the two
Macs with aThunderbolt or USB4 cable(macOS creates aThunderbolt Bridgenetwork between them), with anEthernetcable or adapters, or — on recent
macOS on both Macs — a plainUSB-C data cable(macOS runs a small network
link over it; approve theallow accessory to connectprompt on each Mac,
which appears depending on which Mac is plugged into which). The sender moves
the session onto the cable automatically, even one plugged in mid-session, and
the device row saysCable. Older Macs with a Mini DisplayPort-shaped
Thunderbolt 1 or 2 port work with a Thunderbolt 3 to 2 adapter and a
Thunderbolt 2 cable.
Input from the receiving Mac's keyboard and mouse is a follow-up
(#147).

Why H.264 and not HEVC/AV1?Hardware H.264 encode/decode is universally
fast and the latency is excellent. HEVC is a planned option for better
quality-per-bit.

Is my screen content sent anywhere?No. One direct TCP connection
between your Mac and your device, over your cable or your LAN. No servers,
no accounts, no analytics. Full details — including what the apps store
locally and the current WiFi-encryption caveat — on theprivacy page.

What's the license? Can I fork it or use it commercially?GPL-3.0. Use, study, and adapt it freely — commercially too. If
you distribute a modified version it must stay open source under the same
license with the original attribution intact, so improvements flow back
instead of into closed forks. (Releases up to v0.4.x were MIT-licensed and
remain available under those terms.)

Will it break on a macOS update?Possibly —CGVirtualDisplayis
private API. The same risk applies to every virtual-display product.
The capture/streaming pipeline itself uses only public APIs.

Audio?Out of scope for now.

## Compatible apps

The official apps cover a Mac sender and an iPhone/iPad receiver on iOS 16.4+.
Other people have built their own clients that speak the same protocol, so
you can also use an Android device or an older iPad as a display, or drive
one from Linux. The wire protocol is specified inPROTOCOL.md, so a new client can be written against the spec
instead of reverse-engineered from the Swift sources. If your hardware is
not covered yet, start here:

Android receivers

* gprot42/android-opendisplay- GrapheneOS receiver for de-Googled Pixel phones and tablets, Android 8.0+
* josepacelli/opendisplay-android- Android receiver, Android 8.0+, works with an unmodified Mac app

Older iOS receivers

* cuongpham1/ipad-iphone-second-monitor-ios12-free- iOS 12 client for iPads and iPhones that cannot run the official app

Linux senders

* tixwho/opendisplay-linux- drive an iPhone or iPad from a Wayland desktop (KDE Plasma, Hyprland)

These are fan-made projects, not official builds. They are not affiliated
with OpenDisplay and are not maintained, reviewed, or supported by us, so
please report issues with them in their own repositories. Listing them here
also says nothing about our own plans: an official OpenDisplay app may still
ship for any of these platforms later.

## How it works

MAC (sender) iPHONE / iPAD (receiver)
CGVirtualDisplay ← macOS believes a monitor is attached
 → ScreenCaptureKit (capture the virtual display)
 → VideoToolbox H.264 (hardware, real-time)
 → TCP [4-byte length][Annex B frame] ═══════→ NWListener :9000
 → AVSampleBufferDisplayLayer
 ← JSON control messages (hello, touch, scroll) ═══
 → CGEvent injection (click / drag / scroll)

Thephone listens and the Mac connects— that ordering is what makes the
exact same code work over USB (via theusbmuxddaemon built into every
macOS install) and WiFi. The phone
announces its native panel size; the Mac creates aCGVirtualDisplayat
exactly half that in points (@2x HiDPI) and streams the pixels back.

Everything that crosses the socket — framing, discovery, the video format,
every control message — is specified inPROTOCOL.md. How the
protocol evolves across releases is covered inCOMPATIBILITY.md.

CGVirtualDisplayis aprivate CoreGraphics API(the same one used by
BetterDisplay and DeskPad) — which is precisely why this project can't ship
on the App Store and lives on GitHub instead.

## Install

You needtwo apps: a Mac app (captures and sends) and an iOS app
(receives and displays). To use asecond Macas the display, installOpenDisplay Receiveron it instead of the iOS app.

### Prebuilt downloads (Mac)

GrabOpenDisplay.dmgfrom thelatest release.
The app is signed with a Developer ID certificate and notarized by Apple, so it
opens with a plain double-click on macOS 14+ — no Gatekeeper warning. Open the.dmgand drag the app to Applications.

For a Mac that shouldbethe display, grabOpenDisplayReceiver.dmgfrom
the same release instead. It runs on macOS 12+ and is signed and notarized
the same way; both apps update themselves via Sparkle.

### iPhone app

NeedsiOS / iPadOS 16 or newer— including the 16.7.x line, which is where
Apple left the iPad 5 (2017), the iPad Pro 1st gen, the iPhone 8 and the
iPhone X. If your iPad can't be updated past 16.7, it can still be a second
display (#72).

* TestFlight(recommended): join the public beta attestflight.apple.com/join/3NYaY11c.
* Build from source: open the project in Xcode, select your free Apple ID
under Signing, hit Run. Takes ~2 minutes.

## Quick start (from source)

### Prerequisites

brew install xcodegen 
#
 project generation

Xcode 15+ and a free or paid Apple developer account (to sideload the iOS
app onto your device).

### Build

git clone https://github.com/peetzweg/opendisplay.git

cd
 opendisplay

echo
 
"
DEVELOPMENT_TEAM=YOURTEAMID
"
 
>
 .env 
#
 your Apple team ID, for signing

./generate.sh 
#
 runs xcodegen with your .env

xcodebuild -project OpenSidecar.xcodeproj -scheme OpenSidecarMac \
 -configuration Debug -derivedDataPath build build
xcodebuild -project OpenSidecar.xcodeproj -scheme OpenSidecariOS \
 -configuration Debug -destination 
'
generic/platform=iOS
'
 \
 -derivedDataPath build -allowProvisioningUpdates build

(Or openOpenSidecar.xcodeprojin Xcode and hit Run on each target. Your
team ID is shown atdeveloper.apple.com/accountunder Membership, or just pick your team in Xcode's Signing pane.)

### Run (USB — recommended)

1. Install + openOpenDisplayon the iPhone (it listens on port 9000).
2. On the Mac, run./run.sh(or just open the app) — it talks to macOS's
built-inusbmuxddirectly and auto-connects over the cable. No tunnel
tools needed.
3. GrantScreen Recording(for capture) andAccessibility(for touch)
when macOS asks — one time each.
4. Drag a window onto your new display. Done.

### Run (WiFi)

Open the iPhone app, then pick"iPhone (WiFi)"from the Connection menu
in the Mac app. Discovery is automatic via Bonjour. USB has lower latency;
WiFi has no cable.

### Permissions checklist

macOS and iOS gate several things this app needs — most prompt on first use,
but somefail silentlyif denied or missed. The Mac app shows a live
permission status panel; the iPhone app has a settings screen (shake the
phone, or tap Settings & Help when idle).

Where

Permission

Needed for

If missing

Mac

Screen Recording

capturing the display

black screen on the phone

Mac

Accessibility

touch/scroll input

taps do nothing

Mac

Local Network

WiFi discovery

no device in the Connection menu

iPhone

Local Network

WiFi discovery

Mac can't find the phone

All live underPrivacy & Securityin System Settings (Mac) / Settings
(iPhone). The Local Network ones are only needed for WiFi mode — USB works
without them. If the prompt never appeared, toggle the entry manually or
force-quit and reopen the app.

### Getting the logs for a bug report

Both apps keep a local log of connection events. Nothing is uploaded anywhere;
the logs only leave a device when you share them.

* Mac:clickLogsin the app panel. Finder opens with~/Library/Logs/OpenDisplayselected.
* iPhone/iPad:shake the device (or tapSettings & Helpwhen idle), then
openConnection log. Share hands the file to Mail, Messages or Files; copy
puts the text on the clipboard for pasting straight into an issue.

The phone log is the half usually missing from a WiFi report: whether the
receiver ever announced itself, whether its listener restarted, whether the
decoder was failing. Attach both if you can.

## Roadmap

Tracked asroadmap issues— pick one up if you'd like to contribute!

Connectivity & distribution

* #16Encrypted WiFi transport with pairing code
* App Store release of the iOS app + notarized Mac downloads

Input

* #4Apple Pencil with pressure and tilt
* #5Right-click and multi-touch gestures
* #6Hardware keyboard passthrough
* #7On-screen modifier key sidebar

Display & media

* #9Resolution & quality settings
* #10HEVC encoding
* #12Audio forwarding

Experience

* #11Menu bar app mode with auto-connect
* #13Battery & lifecycle awareness

Exploratory

* #14Remote access beyond the local network
* #15Additional client platforms

Done: prebuilt releases, built-in USB connectivity (no helper tools), WiFi via Bonjour, portrait mode, touch + two-finger scroll, performance overlay, iPad support, multiple devices at once (#8— every connected device becomes its own extended display), a Mac as the display (#17, WiFi or Thunderbolt/Ethernet cable).

## Auto-update (macOS app)

The macOS app updates itself withSparkle—
an open-source framework,nota hosted service. Update checks hit only
our own infrastructure:

* The app reads anappcastfeed hosted on the landing-page site:https://opendisplay.app/appcast.xml(SUFeedURLinproject.yml).
* The release workflow (.github/workflows/release.yml,build-macjob)
runs Sparkle'sgenerate_appcastagainst the notarizedOpenDisplay.dmg,
signs it with the EdDSA key, commits the result topublic/appcast.xml,
and dispatches the Pages deploy — so the published feed points download
links at the GitHub Release assets.
* Sparkle verifies both the EdDSA signature and Apple's notarization before
installing. The app checks automatically in the background
(SUEnableAutomaticChecks) and offers a manual"Check for Updates…"button next toQuitin the menu-bar window.

### Maintainer prerequisites (before auto-update goes live)

Auto-update isscaffolded but inertuntil the signing keys are in place.
The private signing key isnevercommitted — it lives only as a CI
secret. To switch it on:

1. Generate the key pair.Run Sparkle'sgenerate_keysonce (it ships
in the Sparkle SPM artifact bundle and in the release tarball atbin/generate_keys). It prints apublickey and stores theprivatekey in your login keychain.
2. Public key →paste it intoSUPublicEDKeyinproject.yml(replace
theREPLACE_WITH_SUPUBLICEDKEY_FROM_generate_keysplaceholder), then
re-runxcodegen generateand commit.
3. Private key →add it as theSPARKLE_PRIVATE_KEYGitHub Actions
secret (export it withgenerate_keys -x private_key.pemif needed). The
appcast step inrelease.ymlno-ops gracefully while this secret is
absent, so releases keep working until you're ready.
4. Thefirst appcast publishes on the next releaseafter both keys are
set. Confirmhttps://opendisplay.app/appcast.xmlresolves, thentest
the full update flow on a real signed/notarized build(check → download
→ verify → relaunch) — this can't be validated in CI.

## Contributing

Issues and PRs are very welcome — especially for the roadmap items above.
The codebase is intentionally small: ~4 Swift files per platform, withSparkle(SPM) as the macOS app's only
runtime dependency, for auto-update. TheHow it workssection above is the architecture doc; seeMac/CGVirtualDisplayPrivate.hfor the private API surface.

Releases are automated withrelease-please: useConventional Commits(feat:,fix:,docs:, …) and a release PR with a generated changelog appears
automatically — merging it tags the release and attaches prebuilt
artifacts.

## License

GPL-3.0— Copyright (c) 2026 Philip Poloczek.

Free to use, study, and adapt. If you distribute a modified version it
must remain open source under the same license, with the original
attribution intact — improvements flow back to everyone instead of into
closed forks. (Versions up to v0.4.x were MIT-licensed; those releases
remain available under MIT.)

Keywords: iPhone second monitor Mac, iPad external display, free Sidecar
alternative, Duet Display alternative, open source screen extension macOS,
use iPhone as extra screen, virtual display Mac, USB second display.