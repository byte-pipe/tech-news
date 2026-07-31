---
title: 'GitHub - mokshablr/gander: Take a gander at any file. Offline, zero-permission Android viewer for PDF, Word, Excel, PowerPoint, photos, video, audio, Markdown and code. · GitHub'
url: https://github.com/mokshablr/gander
site_name: hnrss
content_file: hnrss-github-mokshablrgander-take-a-gander-at-any-file-o
fetched_at: '2026-08-01T03:07:14.066346'
original_url: https://github.com/mokshablr/gander
date: '2026-07-31'
description: Take a gander at any file. Offline, zero-permission Android viewer for PDF, Word, Excel, PowerPoint, photos, video, audio, Markdown and code. - mokshablr/gander
tags:
- hackernews
- hnrss
---

mokshablr

 

/

gander

Public

* NotificationsYou must be signed in to change notification settings
* Fork2
* Star193

 
 
 
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

23 Commits
23 Commits
.github
.github
 
 
app
app
 
 
docs
docs
 
 
fastlane/
metadata/
android/
en-US
fastlane/
metadata/
android/
en-US
 
 
gradle/
wrapper
gradle/
wrapper
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.gradle.kts
build.gradle.kts
 
 
gradle.properties
gradle.properties
 
 
gradlew
gradlew
 
 
gradlew.bat
gradlew.bat
 
 
settings.gradle.kts
settings.gradle.kts
 
 
View all files

## Repository files navigation

# Gander 🪿

Take a gander at any file.A tiny, open source, fully offlinefile viewer for Androidthat opens
PDF, Word, Excel, PowerPoint, photos, videos, audio, Markdown, text and code in one app,
withzero permissions, no ads, no tracking and no internet access at all.

Every phone ships with a dozen half-viewers that bounce your documents to cloud services.
Gander is the opposite: one small APK (about 15 MB) that renders everythingon the device.
It cannot phone home because it does not even hold the INTERNET permission.

## Screenshots

Home: recents and folders

Folder browsing

PDF

Word (.docx)

PowerPoint (.pptx)

Excel (.xlsx)

## Features

* One viewer for everything: documents, spreadsheets, slides, images, video, audio, Markdown, code
* Pinch zoom and smooth scrollingeverywhere, with deep zoom into huge photos (tiled decoding)
* Recent fileswith thumbnail previews (image, video frame, PDF first page)
* Folder browsingthrough one-time system grants, still without any storage permission
* Share sheet and "Open with" integration: share a file from any app (chat, mail, browser) into Gander, or tap it in a file manager
* Find in document: search inside Word, Excel, slides, Markdown, text and code with match navigation
* Share and locate: send the open file to any app, or jump to its folder in the file manager
* Private by construction: no permissions, no INTERNET, no analytics, no accounts, nothing leaves the phone
* Modern Android: Material 3, dark mode, edge to edge, works on Android 8.0+

## Supported formats

Category

Formats

Renderer

Documents

PDF

Pdfium (native)

Word 
.docx

docx-preview, offline in a sandboxed WebView

Spreadsheets

.xlsx
 
.xls
 
.xlsm
 
.xlsb
 
.csv
 
.ods

SheetJS, offline

Slides

PowerPoint 
.pptx

PPTXjs, offline

Photos

JPG, PNG, WebP, BMP, HEIC/HEIF

Tiled deep-zoom image view, EXIF aware

GIF (animated), SVG, AVIF, ICO

WebView

Video

MP4, M4V, MOV, MKV, WebM, 3GP, AVI, FLV, MPEG-TS

Media3 ExoPlayer

Audio

MP3, M4A, AAC, FLAC, WAV, OGG, Opus, AMR

Media3 ExoPlayer

Markdown

.md
 rendered as formatted HTML

marked + DOMPurify, offline

Text and code

.txt
 
.json
 
.xml
 logs, most source files

Text viewer

Legacy binary.docand.pptare not supported (no faithful offline renderer exists);
the app explains this and suggests re-saving as.docx/.pptx. Binary.xlsworks.

## Install

Runs onAndroid 8.0 (API 26) and up.

1. Download the latest APK fromReleases:Gander-x.y-arm64.apkfits practically every phone from 2017 onward
(use theuniversalAPK for very old or x86 devices).
2. Copy it to your phone, tap it, and allow "install unknown apps" when asked.
3. Optional: Play Protect may warn about an unknown developer; that is what
sideloaded open source looks like. Tap "Install anyway".

Updating: install the new APK over the old one; recents and folder grants survive.

Automatic updates without a store: installObtainiumand addhttps://github.com/mokshablr/ganderas an app source. It follows the tagged
GitHub releases here and updates Gander like a store would.

Verify before installing: every release is signed with the same key, so you can
confirm an APK really came from this repo. Obtainium can pin the fingerprint below,
and for a file you have already downloaded:

apksigner verify --print-certs Gander-x.y-arm64.apk

Signing certificate SHA-256:

5B:5C:F6:4A:94:23:7C:D5:F0:E0:85:76:00:38:BC:1C:EB:DF:18:DA:BA:5C:B3:EA:CA:7C:15:9F:22:A7:E2:4B

## How the zero-permission trick works

Gander receives files through the Storage Access Framework and "Open with" intents,
so the OS hands it exactly the documents you chose and nothing else. Office formats
render inside a locked-down WebView whose every request is intercepted byWebViewAssetLoader: bundled JS libraries load from app assets and the document
streams from the content URI. No network stack is ever touched, and the app does
not declare the INTERNET permission, so there is nothing to audit or trust.

Folder browsing usesACTION_OPEN_DOCUMENT_TREEgrants. Note that Android itself
refuses to grant the Downloads root to any app; grant Documents, DCIM or a
subfolder of Downloads instead.

## Build from source

To build it yourself you need JDK 17+ and the Android SDK (platform 35). These are
build requirements only. The installed app runs on Android 8.0 (API 26) and up.

./gradlew assembleDebug 
#
 installable debug build

./gradlew assembleRelease 
#
 unsigned without a keystore

Release signing expects a local, untracked keystore atkeystore/gander.jks(store and key passwordgander-local, aliasgander); generate one with:

keytool -genkeypair -keystore keystore/gander.jks -alias gander \
 -keyalg RSA -keysize 2048 -validity 10000 \
 -storepass gander-local -keypass gander-local -dname 
"
CN=Gander
"

The keystore is gitignored on purpose: it is a personal signing key and must
never land in a public repo.

## Architecture in one paragraph

ViewerActivityroutes by file extension first, MIME type second (FileKind.kt),
into one of four surfaces: a native Pdfium view for PDF, a tiledSubsamplingScaleImageViewfor photos, Media3 ExoPlayer for video and audio, or a
sandboxed WebView for everything rendered by vendored JS libraries
(app/src/main/assets/viewer/). The home screen (MainActivity) lists recents
(persisted SAF grants) and granted folders (DocumentsContract child queries), with
thumbnails generated off-thread and cached (Thumbs.kt).

Vendored viewer libraries and their licenses: JSZip (MIT), docx-preview
(Apache-2.0), SheetJS CE (Apache-2.0), PPTXjs + divs2slides (MIT), jQuery 1.11
(MIT), D3 3.x + NVD3 (BSD/Apache), marked (MIT), DOMPurify (Apache-2.0/MPL).

## Roadmap

* F-Droid listing
* Legacy.doc/.pptsupport if a usable offline renderer appears
* iOS companion (thin QuickLook wrapper)

## Contributing

Issues and small PRs are welcome, seeCONTRIBUTING.md.
If Gander is useful to you, a star helps other people find it.

## License

MIT. Vendored viewer libraries keep their own licenses, listed above;
all are MIT/Apache/BSD and compatible.