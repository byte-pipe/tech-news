---
title: Building and Shipping Mac and iOS Apps Without Ever Opening Xcode
url: https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/
site_name: hackernews_api
content_file: hackernews_api-building-and-shipping-mac-and-ios-apps-without-eve
fetched_at: '2026-07-14T11:32:42.319236'
original_url: https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/
author: speckx
date: '2026-07-13'
description: describe
tags:
- hackernews
- trending
---

Lately, I’ve heard several Apple related podcasters talk about how bad Xcode is, and how Apple needs to make vibe-coding Mac and iOS apps better by making Xcode less inscrutable. They’re not wrong, but also I don’t understand why they’re even opening Xcode in the first place. With a little bit of pre-work, you can vibe code Mac and iOS apps to your heart’s content without looking at Xcode anymore.

And if you’re ever in doubt about how to make any of the following work, point Claude Code or your LLM coding tool of choice to this blog post, and let it figure it out. That’s literally its job, figuring out things you don’t want to have to.

## TL;DR

* Xcode.app must be installed, but it never has to be open.xcodebuild,notarytool,stapler, anddevicectlall live inside Xcode and run fine from a shell.
* A few one-time steps do need the GUI(or an interactive terminal): sign into your Apple ID, create a Developer ID certificate, store a notarization password. After that, builds and deploys are fully headless.
* The Mac app ships via one script—scripts/release.sh— which you write once. It runs the whole chain: archive → Developer ID sign → notarize → staple → install to/Applications.
* Signing is certificate-and-keychain based.The signing key lives in the login keychain;xcodebuildfinds it automatically. No secrets in the repo.

The one-time setup is the only part with any friction, so let’s get it out of the way first.

## Install Xcode

You do have to have Xcode installed, there’s no getting around that, because build depends on tools that live inside Xcode.app.

Once Xcode is installed, make sure it’s the selected command line toolchain, and not/Library/Developer/CommandLineTools. If the output of the check is/Applications/Xcode.app/Contents/Developer, you’re in good shape:

Terminal window
1
❯
 
xcode-select
 
-p
2
/Applications/Xcode.app/Contents/Developer

If it DOES return the path for the standalone CommandLineTools instead, point it to Xcode.

Terminal window
1
sudo
 
xcode-select
 
-s
 
/Applications/Xcode.app/Contents/Developer

NOTE: The name “Command Line Tools” can be confusing.

This is because there’s a standalone Command Line Tools package, available withxcode-select --install, which is the/Library/Developer/CommandLineToolsversion. This contains clang and git, but not the iOS SDK, notarytool, devicectl, and other items needed for full app development.

The complete toolchain is inside Xcode.app, at/Applications/Xcode.app/Developer, and it has everything you need. If you have Xcode installed, you don’t need the standalone Command Line Tools.

## Install XcodeGen

Xcode and its command line tools aren’t enough to generate and manage Xcode projects automatically. For that, you’re going to needXcodeGen. You candownload it from Githubor install it using homebrew:

Terminal window
1
brew
 
install
 
xcodegen

Long story short, Xcode projects are actually folders that macOS makes appear as files, and they contain everything about your project needed to create and compile your app. Xcode constantly modifies the files and file references constantly, and it creates issues for git repositories.

Xcodegen creates a project.yml (YAML) file with all your project settings, and then on every build, it recreates the entire .xcodeproj folder using that project.yml file. Only the YAML file has to be committed to git, and the whole .xcodeproj can be ignored from git’s perspective.

## Configure Xcode, Once

You do need to setup Xcode initially in order to never have to look at it again.

### Xcode License and Additional Components

First, either accept its license and install its additional components, or do it through the command line:

Terminal window
1
sudo
 
xcodebuild
 
-license
 
accept
2
sudo
 
xcodebuild
 
-runFirstLaunch

### Setup Your Apple Developer Account in Xcode

Next, open Xcode, click on Settings → Accounts and click on + to add your account.

NOTE: You have to have a paid Apple Developer account in order to distribute and notarize your apps.

And you will want them notarized in order to install them on you Mac and iOS devices and not have the OSes decided they’re malware and delete them.

### Create a Developer ID Application Certificate

Once that’s done, create a Developer ID Application certificate (Settings → Accounts → your Apple ID →Manage Certificates…→+→Developer ID Application), which creates a cert for signing the shipped .app bundle.

Please note that a Developer ID Application certificate and your Apple Development certificate are two separate things.

TheApple Developmentidentity is for building and running on your own devices — pushing to your iPhone, local debugging. TheDeveloper ID Applicationidentity is for the notarized.appthat survives Gatekeeper and runs on someone else’s Mac. The release script wants that second one.

Creating the certificate in Xcode installs both the certificateandits private key into your login keychain. That private key is what actually does the signing, and itcannot be re-downloaded— so don’t delete it, and back up your keychain.

When in doubt, ask your LLM of choice about them and have it help you get set up. It’s the one that’s going to be using Xcode for you anyway.

And finally,

### Store a Notarization Credential – Once, in Terminal

Notarization uploads your signed app to Apple for a malware scan.notarytoolauthenticates using a stored keychain profile that you create once, interactively — it prompts for an app-specific password, and there’s no way around the prompt:

Terminal window
1
xcrun
 
notarytool
 
store-credentials
 
App-Name
 
\
2
 
--apple-id
 
"
[email protected]
"
 
--team-id
 
YOUR-TEAM-ID
3
# paste an app-specific password when prompted

A few things worth knowing here:

* Name the profile after the app.Don’t borrow another app’s profile — it’ll work on your machine and then silently break on someone else’s.
* The app-specific password is not your Apple ID password.Generate one atappleid.apple.com→Sign-In & Security → App-Specific Passwords.
* These passwords go stale silentlywhenever you change your Apple ID password. A401 invalid credentialsout of notarization almost always means “go make a fresh app-specific password,” not “your setup is broken.”

Confirm it’s stored:

Terminal window
1
xcrun
 
notarytool
 
history
 
--keychain-profile
 
App-Name

Side topic here, I store my app-specific passwords in a 1Password vault that Claude Code has access to. That way whenever I’m creating a new app, I can tellITto create the notarization credential for me, and it knows to check its 1Password vault for the password. The whole point of using the LLM in the first place is to avoid doing things manually that you don’t want to do.

### Setup a Local.xconfig File and Add It to .gitignore

Real signing needs your team ID and bundle prefix, and I put those in a Local.xconfig file:

Terminal window
1
cp
 
Local.xcconfig.example
 
Local.xcconfig
2
# then edit Local.xcconfig to set:
3
# BUNDLE_PREFIX = your.real.prefix
4
# DEVELOPMENT_TEAM = YOUR-TEAM-ID

Again, if in doubt, ask Claude Code or your LLM of choice to create this for you.

## Set up the Agent Tools

### Create the Deploy Script

Deployment on my apps is handled via a script calledrelease.shthat lives in ascriptsfolder inside the repo. Without it, I don’t have an automated build pipeline.

I had Claude Code create mine: I told Claude, more or less:I want to archive, Developer ID-sign, notarize, staple, and install this app to /Applications without ever opening Xcode. Write me a script that does the whole chain and fails loudly if any step breaks.

It didn’t need me to explain the pipeline, because the pipeline isn’t a secret — archive withxcodebuild, export with-exportArchiveand anExportOptions.plist, submit withnotarytool --wait, attach the ticket withstapler, check withspctl. That’s the documented, conventional way to ship a Developer ID Mac app, and the model knows it. What it needed frommewas the project-specific stuff: the scheme name, the team ID, what to call the notary profile, where to install the result.

Then it wrote a first draft, we ran it, it broke, and we fixed it. That loop is not a failure mode, it’s just the process. I always look at AI workflows as works in progress, but it doesn’t take long before you can stop tweaking things and just start working.

This is the actual script from one of my app repos:

1
#!/usr/bin/env bash
2
# scripts/release.sh — produce a Developer ID-signed, notarized MY-APP-NAME.app and
3
# install it to /Applications.
4
#
5
# Requires (one-time): Xcode signed into your Apple ID, the paid Developer
6
# Program, and a notarytool credential profile. Defaults to the "MY-APP-NAME"
7
# profile; override with MY-APP-NAME_NOTARY_PROFILE=<name>.
8
#
9
# Usage: ./scripts/release.sh
10

11
set
 
-euo
 
pipefail
12

13
PROJECT
=
"
MY-APP-NAME.xcodeproj
"
14
SCHEME
=
"
MY-APP-NAME-macOS
"
15
APP_NAME
=
"
MY-APP-NAME
"
16
TEAM_ID
=
"
YOURTEAMID
"
17
NOTARY_PROFILE
=
"${
MY-APP-NAME_NOTARY_PROFILE
:-
MY-APP-NAME
}"
18

19
BUILD_DIR
=
"
build
"
20
ARCHIVE_PATH
=
"
$BUILD_DIR
/
$APP_NAME
.xcarchive
"
21
EXPORT_PATH
=
"
$BUILD_DIR
/Export
"
22
APP_PATH
=
"
$EXPORT_PATH
/
$APP_NAME
.app
"
23
INSTALL_DIR
=
"
/Applications
"
24
LSREGISTER
=
"
/System/Library/Frameworks/CoreServices.framework/Versions/A/Frameworks/LaunchServices.framework/Versions/A/Support/lsregister
"
25

26
cd
 
"$(
dirname
 
"
$0
")
/..
"
27

28
step
()
 
{
 
printf
 
"
\n\033[1;36m▸ %s\033[0m\n
"
 
"
$*
"
;
 
}
29
fail
()
 
{
 
printf
 
"
\n\033[1;31m✗ %s\033[0m\n
"
 
"
$*
"
 
>&2
;
 
exit
 
1
;
 
}
30

31
step
 
"
Pre-flight
"
32
command
 
-v
 
xcodegen
 
>
/dev/null
 
||
 
fail
 
"
xcodegen not installed (brew install xcodegen).
"
33
if
 
!
 
xcrun
 
notarytool
 
history
 
--keychain-profile
 
"
$NOTARY_PROFILE
"
 
>
/dev/null
 
2>&1
;
 
then
34
 
fail
 
"
notarytool profile '
$NOTARY_PROFILE
' missing. Create it with xcrun notarytool store-credentials.
"
35
fi
36

37
step
 
"
Regenerating project
"
38
xcodegen
 
generate
39

40
rm
 
-rf
 
"
$BUILD_DIR
"
;
 
mkdir
 
-p
 
"
$BUILD_DIR
"
41

42
step
 
"
Archiving (Release)
"
43
xcodebuild
 
-project
 
"
$PROJECT
"
 
-scheme
 
"
$SCHEME
"
 
-configuration
 
Release
 
\
44
 
-derivedDataPath
 
"
$BUILD_DIR
/derived
"
 
-archivePath
 
"
$ARCHIVE_PATH
"
 
\
45
 
-allowProvisioningUpdates
 
archive
46

47
step
 
"
Exporting Developer ID-signed app
"
48
cat
 
>
 
"
$BUILD_DIR
/ExportOptions.plist
"
 
<
<
EOF
49
<?
xml 
version
=
"
1.0
"
 
encoding
=
"
UTF-8
"
?>
50
<!DOCTYPE
 
plist
 
PUBLIC
 
"
-//Apple//DTD PLIST 1.0//EN
"
 
"
http://www.apple.com/DTDs/PropertyList-1.0.dtd
"
>
51
<plist
 
version=
"
1.0
"
><dict>
52
 
<key>method</key><string>developer-id</string>
53
 
<key>teamID</key><string>$TEAM_ID</string>
54
 
<key>signingStyle</key><string>automatic</string>
55
</dict></plist>
56
EOF
57
xcodebuild
 
-exportArchive
 
-archivePath
 
"
$ARCHIVE_PATH
"
 
-exportPath
 
"
$EXPORT_PATH
"
 
\
58
 
-exportOptionsPlist
 
"
$BUILD_DIR
/ExportOptions.plist
"
 
-allowProvisioningUpdates
59
[
 
-d
 
"
$APP_PATH
"
 
]
 
||
 
fail
 
"
Exported app not found at 
$APP_PATH
.
"
60

61
step
 
"
Notarizing (submitting to Apple, may take a few minutes)
"
62
ditto
 
-c
 
-k
 
--keepParent
 
"
$APP_PATH
"
 
"
$BUILD_DIR
/notarize.zip
"
63
xcrun
 
notarytool
 
submit
 
"
$BUILD_DIR
/notarize.zip
"
 
--keychain-profile
 
"
$NOTARY_PROFILE
"
 
--wait
64

65
step
 
"
Stapling ticket
"
66
xcrun
 
stapler
 
staple
 
"
$APP_PATH
"
67

68
step
 
"
Verifying Gatekeeper acceptance
"
69
spctl
 
-a
 
-vvv
 
-t
 
exec
 
"
$APP_PATH
"
70

71
step
 
"
Installing to 
$INSTALL_DIR
/
$APP_NAME
.app
"
72
pkill
 
-x
 
"
$APP_NAME
"
 
2>
/dev/null
 
||
 
true
73
rm
 
-rf
 
"
$INSTALL_DIR
/
$APP_NAME
.app
"
74
cp
 
-R
 
"
$APP_PATH
"
 
"
$INSTALL_DIR
/
"
75
[
 
-x
 
"
$LSREGISTER
"
 
]
 
&&
 
"
$LSREGISTER
"
 
-f
 
"
$INSTALL_DIR
/
$APP_NAME
.app
"
 
>
/dev/null
 
2>&1
 
||
 
true
76

77
step
 
"
Verifying installed bundle
"
78
xcrun
 
stapler
 
validate
 
"
$INSTALL_DIR
/
$APP_NAME
.app
"
79
spctl
 
-a
 
-vvv
 
-t
 
exec
 
"
$INSTALL_DIR
/
$APP_NAME
.app
"
80
printf
 
"
\n\033[1;32m✓ %s notarized, stapled, installed.\033[0m\n
"
 
"
$APP_NAME
"

It looks more complicated than it is, but it is a series of steps that you’d have to know need performed. Again, this is why you talk to your LLM, tell it what you want, and have it help build your workflow.

Some things to note:

set -euo pipefailhalts the script on any failing command immediately instead of blundering forward. There’s no half-finished state thatlookslike success.

cd "$(dirname "$0")/.."means the script hops to the repo root regardless of where you invoked it from, so./scripts/release.shworks whether you’re in the repo root or three directories down.

Thepre-flight blockchecks thatxcodegenexists and that the notary profile is actually storedbeforespending five minutes on an archive that’s doomed to fail at step five.

And the last two steps re-verify theinstalledbundle, not just the exported one. Belt and suspenders, but I’ve had a copy step silently mangle a bundle before and I’d rather find out from the script than from Gatekeeper three days later when it deletes my app for me.

### Create CLAUDE.md or AGENTS.md

release.shgives you a one-command deploy.CLAUDE.md(orAGENTS.mdfor basically every other model under the sun) is what makes the agent actuallyuseit without being told every single time.

I had Claude create my CLAUDE.md itself after going back and forth about the build process. Now whenever I create a new app, I tell it to reference the repo for one of my other apps and use the same methodology.

CLAUDE.md
1
## 
Build commands
2

3
```
bash
4
# Regenerate the Xcode project after changing project.yml or adding source files
5
xcodegen
 
generate
6

7
# Unit tests (YOUR-APP-NAMEKit only; fast, no Xcode build required)
8
swift
 
test
9

10
# macOS app
11
xcodebuild
 
-project
 
YOUR-APP-NAME.xcodeproj
 
-scheme
 
YOUR-APP-NAME-macOS
 
\
12
 
-destination 'platform=macOS' CODE_SIGNING_ALLOWED=NO build
13
```
14

15
## 
Release (Developer ID + notarization)
16

17
```
bash
18
./scripts/release.sh
 
# archive → Developer ID export → notarize → staple → install
19
```
20

21
The 
`
xcodebuild
`
 commands above use 
`
CODE_SIGNING_ALLOWED=NO
`
, which produces an
22
**
ad-hoc
**
 build: fine for CI and quick local checks, but Gatekeeper rejects it
23
and the iCloud KVS / App Group entitlements don't bind (no team prefix). For a
24
real menu-bar build that survives quarantine and lets iCloud sync work, use
25
`
scripts/release.sh
`
. It signs with Developer ID, notarizes via the 
`
YOUR-APP-NAME
`
26
notarytool keychain profile, staples the ticket, and installs to
27
`
/Applications/YOUR-APP-NAME.app
`
.

## That’s It

And that’s the whole one-time setup. From here on, nothing needs a mouse.

## How the build actually runs — no GUI in the loop

Everything below is plain command-line invocation. Xcode.app never launches; these tools live inside it but run standalone. This is exactly what Claude Code executes through its shell.

### Fast, Unsigned Checks

For “does it compile / do the tests pass,” you don’t need signing at all:

Terminal window
1
# Unit tests — pure SPM, no Xcode build at all
2
swift
 
test
3

4
# Compile the macOS app (ad-hoc, unsigned — fine for CI/local sanity)
5
xcodebuild
 
-project
 
TZed.xcodeproj
 
-scheme
 
TZed-macOS
 
\
6
 
-destination
 
'
platform=macOS
'
 
CODE_SIGNING_ALLOWED=NO
 
build
7

8
# Compile the iOS app + widget extension for the simulator
9
xcodebuild
 
-project
 
TZed.xcodeproj
 
-scheme
 
TZed-iOS
 
\
10
 
-destination
 
'
generic/platform=iOS Simulator
'
 
CODE_SIGNING_ALLOWED=NO
 
build

CODE_SIGNING_ALLOWED=NOgives you anad-hocbuild: it compiles and runs in a simulator, but Gatekeeper rejects it and entitlements like iCloud KVS and App Group don’t bind. That’s the fast inner loop.

### The Mac Release Pipeline

One command does the entire shippable chain — the script from Part two:

Terminal window
1
./scripts/release.sh

Archive, Developer ID export, notarize, staple, verify, install. If any step fails it stops and tells you which one broke. Need a different notary profile? Override it:TZED_NOTARY_PROFILE=<name> ./scripts/release.sh.

### Deploying to a Real iPhone, Headless

iOS has no notarization step — that’s a Mac-distribution concept. Getting a build onto a connected iPhone isxcodebuildplusdevicectl, both inside Xcode’s toolchain:

Terminal window
1
# Build & sign for a real device (uses the Apple Development cert + provisioning)
2
xcodebuild
 
-project
 
TZed.xcodeproj
 
-scheme
 
TZed-iOS
 
\
3
 
-destination
 
'
generic/platform=iOS
'
 
\
4
 
-allowProvisioningUpdates
 
\
5
 
-derivedDataPath
 
build/ios
 
archive
 
-archivePath
 
build/TZed-iOS.xcarchive
6

7
# Install the built .app onto the connected device by its UDID
8
xcrun
 
devicectl
 
device
 
install
 
app
 
\
9
 
--device
 
<DEVICE-UDID>
 
build/ios/…/TZed.app

devicectl list deviceslists connected and paired devices with their UDIDs. Device builds sign with theApple Developmentidentity (not Developer ID) plus a development provisioning profile, which-allowProvisioningUpdatesfetches for you.

## How code signing works when there’s no GUI

If you’ve only ever signed apps by ticking a box in Xcode, it’s worth understanding what’s actually going on under there, because none of it needs the GUI at build time.

The private key does the signing.When you created that Developer ID Application certificate, Apple issued a certificate and your Mac generated a matching private key, both landing in your login keychain.codesign(whichxcodebuildcalls) uses the private key to sign the binary; the certificate — which chains up to Apple’s root — gets embedded so anyone can verify it.

Automatic signing picks the identity for you.The release script usessigningStyle: automatic, soxcodebuildselects the right identity by team ID and pulls any needed provisioning profile from Apple on the fly. No profiles checked into the repo.

Entitlements bind at sign time.Each target has a.entitlementsfile (sandbox, network client, iCloud KVS, App Group). These only take effect when the app is signed with a real team identity, which is theotherreason ad-hoc builds can’t ship: the iCloud and App-Group entitlements quietly don’t bind without the team prefix, and you get to spend an hour wondering why your key-value store is empty.

Notarization isn’t signing.Signing proveswhobuilt the app. Notarization is a separate step where Apple scans the signed app for malware and issues a ticket; stapling attaches that ticket so Gatekeeper trusts the app offline. For a hidden-UI menu bar app (LSUIElement), notarization is what keeps XProtect from flagging it.

The secrets never touch git.The signing private key lives in the login keychain. The notarization app-specific password lives in the notarytool keychain profile. Neither ever gets written into the repo.

You can verify any signed build by hand:

Terminal window
1
codesign
 
-dv
 
--verbose=4
 
/Applications/TZed.app
 
# who signed it, with what cert
2
spctl
 
-a
 
-vvv
 
-t
 
exec
 
/Applications/TZed.app
 
# would Gatekeeper allow it?
3
stapler
 
validate
 
/Applications/TZed.app
 
# is the notarization ticket attached?

## What the agent actually uses

There’s no magic here. Claude Code drives all of this through a plain, non-interactive shell — there’s no special “build” MCP server or plugin doing something clever. It’sxcodebuild,xcrun notarytool,xcrun stapler,spctl,codesign,devicectl,xcodegen, andswift. Standard CLI tools, the same ones we’d use ourselves.

The glue is theCLAUDE.mdfrom Part two. It tells the agent the notary-profile convention, the two build paths, and that shipping meansrelease.sh. The result is Claude just runs the thing, without me re-explaining it every session.

The one step that stays interactive isnotarytool store-credentials, and that’s a choice rather than a limitation: youcouldpass--passwordand script it, but that means putting an app-specific password in your shell history. Type it once by hand, let the keychain or 1Password hold it, and everything downstream is automated.

## Why Xcode never needs to be open

Put the GUI workflow next to the headless one and the whole thing just lines up:

JOB
GUI WAY
HEADLESS WAY
Generate project
Xcode manages 
.xcodeproj
xcodegen generate
 from 
project.yml
Build
⌘B / Run button
xcodebuild … build
Archive
Product → Archive
xcodebuild … archive
Export signed app
Organizer → Distribute
xcodebuild -exportArchive
Notarize
Organizer upload
xcrun notarytool submit --wait
Staple
(automatic in Organizer)
xcrun stapler staple
Install to /Applications
drag-and-drop
cp -R
 + 
lsregister
Deploy to iPhone
Run on device
xcodebuild archive
 + 
devicectl device install

The GUI is only ever needed for that one-time credential setup. After that, the entire lifecycle is scriptable, which is exactly whatrelease.shfinalizes, and exactly why the agent can own it end to end while I go do something more interesting than watching a progress bar.

If you want to try it yourself, the order is: install Xcode and xcodegen, do the credential setup, then sit down with Claude and build your ownrelease.shandCLAUDE.md. That last part is the actual work, and it’s an hour or two at most. After that, “ship a new build” becomes one sentence. After the first app setup, Claude Code can copy the same setup to apply to future apps.