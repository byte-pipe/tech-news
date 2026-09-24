---
title: 'GitHub - julyx10/lap: An offline-first photo manager for large local libraries · GitHub'
url: https://github.com/julyx10/lap
site_name: github
content_file: github-github-julyx10lap-an-offline-first-photo-manager-f
fetched_at: '2026-09-24T15:44:12.768725'
original_url: https://github.com/julyx10/lap
author: julyx10
description: An offline-first photo manager for large local libraries - julyx10/lap
---

julyx10

 

/

lap

Public

* NotificationsYou must be signed in to change notification settings
* Fork167
* Star2.7k

 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

1,169 Commits
1,169 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
.github
.github
 
 
docs
docs
 
 
i18n
i18n
 
 
scripts
scripts
 
 
src-tauri
src-tauri
 
 
src-vite
src-vite
 
 
.gitignore
.gitignore
 
 
.gitmodules
.gitmodules
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
PRIVACY.md
PRIVACY.md
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# Lap - Private Local Photo Manager

### Open-source desktop photo manager for macOS, Windows, and Linux.

English |Deutsch|Français|Español|Português|Русский|简体中文|日本語|한국어

Lap is an open-source, local-first photo manager for browsing family albums, finding old photos quickly, and managing large personal media libraries offline.
It is a privacy-focused alternative to cloud photo services: no forced upload, local AI search, folder-first workflow, and free to use.

## Download Lap

Open thelatest release page, then download the file that matches your system:

Platform

Package

Note

macOS (Apple Silicon / Intel)

_aarch64.dmg
 / 
_x64.dmg

Notarized by Apple

Windows 10/11 (x64 / ARM64)

_x64_en-US.msi
 / 
_arm64_en-US.msi

Unsigned — if SmartScreen blocks the download, click 
Keep anyway

Linux (x64 / ARM64)

_amd64.deb
 / 
_arm64.deb

For Debian-based distros (Ubuntu, Debian, Linux Mint, etc.)

Linux (x64 / ARM64)

_amd64.AppImage
 / 
_aarch64.AppImage

Make the file executable, then double-click to run

### macOS with Homebrew

brew tap julyx10/lap
brew install --cask lap

## Screenshots

## Why Lap

* Local-first by design: your photos stay on your own disk, with no required cloud account or upload.
* No library lock-in: work directly with your existing folders instead of importing everything into a closed database.
* Private AI tools: search, similarity, smart tags, and face features run locally on your machine.
* Built for large collections: optimized for smooth browsing and organization across libraries with 100k+ files.
* Open source and free: no subscription, no forced ecosystem, and code you can inspect.

## Features

* Flexible library browsingby date, folder, location, camera, lens, tags, ratings, and faces, with random sorting and a small-image filter.
* Interactive Map Viewto explore geotagged photos and videos in clusters that follow your current filters.
* Smart Albumssave rule-based views with custom grouping and sorting.
* Collections and tagsto organize selected files in bulk without moving or duplicating the originals.
* Local AI searchfor text prompts, visual similarity, subjects, face clustering, and optional multilingual search in 50+ languages.
* Apple Live Photos and Google Motion Photoswith motion playback and a unified Smart Album filter.
* RAW + JPEG/HEIC pairsdisplayed as one item, with linked files kept together during file operations.
* Configurable RAW thumbnails and previewsusing RAW rendering or the camera's embedded preview.
* Folder-first workflowwith multiple libraries, drag-and-drop import, copy-paste import, filesystem sync, and safe move/copy/delete operations.
* Date-organized importwith day, month, year, or single-folder layouts, original filenames, and duplicate skipping.
* Culling and comparison toolsincluding a four-pane image comparison viewer.
* Duplicate cleanupwith reclaimable-space summaries and bulk removal across duplicate sets.
* Customizable viewingwith thumbnails up to 1024 px, adjustable grid sizes and corners, and Quick Preview or separate viewer windows.
* Desktop integrationwith multiple external apps and wallpaper selection on macOS, Windows, and GNOME Linux.
* Built-in editingfor crop, rotate, flip, resize, and basic image adjustments.
* Broad format supportfor 60+ photo, RAW, and video formats.

## Metadata, Collections, and Moving Files

Lap is folder-first, but not every piece of information shown in Lap is embedded in the original file. This distinction matters when you also manage the same folders in Finder, Explorer, or another photo app.

### What stays with the file

* Your original photos and videos always remain ordinary files in their existing folders.
* File metadata already embedded in a file, such as EXIF capture date, camera, lens, GPS, and orientation, is read from that file when Lap indexes it.
* Saving a built-in image edit writes the resulting image to the selected destination.
* When you rename, move, copy, or delete filesin Lap, Lap updates its local catalog at the same time. It also keeps supported grouped assets, such as Apple Live Photo components, AAE sidecars, and enabled RAW + JPEG/HEIC pairs, together.

### What is stored locally by Lap

The following are Lap library data. They are stored in Lap's local database or library configuration, not written into EXIF, IPTC, or XMP sidecars:

* Collections, Tags, Comments, Favorites, Ratings, and Culling states (including Picks and Rejects)
* Smart Albums and their rules, grouping, sorting, and ordering
* AI search data, face data, thumbnails, and other index/cache data

This data does not travel with a file when it is copied, exported, or moved outside Lap, and it is not available automatically to other applications.

### Working with files outside Lap

Lap can rescan folders and detect many filesystem changes. But changes made outside Lap—such as renaming, moving, replacing, or copying files—can disrupt organization that is stored only in Lap.

For the most reliable results, rename and move files in Lap whenever you rely on Collections, Tags, Comments, Favorites, Ratings, or culling states. If you also manage files outside Lap, back up Lap's database and configuration together with your photos. You can manage the database location and create a backup inSettings → Storage.

Deleting Lap's database or configuration removes this local organization and index data, but does not delete your original media files.

## Uninstall Lap

Lap works directly with your existing photo folders. Uninstalling Lap, or deleting its database and cache files, doesnotdelete your original photos.

The standard uninstall steps remove the application. To remove Lap completely, quit Lap first, uninstall the application, then delete its local database, thumbnail cache, and configuration files using the cleanup command for your platform.

### macOS

If you installed Lap with Homebrew:

brew uninstall --cask lap

For a manual installation, quit Lap and moveLap.appfrom theApplicationsfolder to the Trash.

To remove all Lap database, cache, and configuration files:

rm -rf 
"
$HOME
/Library/Application Support/com.julyx10.lap
"
 \
 
"
$HOME
/Library/Caches/com.julyx10.lap
"
 \
 
"
$HOME
/Library/WebKit/com.julyx10.lap
"

rm -f 
"
$HOME
/Library/Preferences/com.julyx10.lap.plist
"

### Windows

OpenSettings > Apps > Installed apps, findLap, and selectUninstall.

Then open PowerShell and remove all Lap database, cache, and configuration files:

Remove-Item
 
-
Recurse 
-
Force 
-
ErrorAction SilentlyContinue 
"
$
env:
LOCALAPPDATA
\com.julyx10.lap
"

Remove-Item
 
-
Recurse 
-
Force 
-
ErrorAction SilentlyContinue 
"
$
env:
APPDATA
\com.julyx10.lap
"

### Linux

For DEB installations, uninstall the package:

sudo apt remove lap

For AppImage installations, quit Lap and delete the downloaded.AppImagefile.

Then remove all Lap database, cache, and configuration files:

rm -rf 
"
$HOME
/.local/share/com.julyx10.lap
"
 \
 
"
$HOME
/.cache/com.julyx10.lap
"
 \
 
"
$HOME
/.config/com.julyx10.lap
"

If you selected a custom database storage directory in Lap settings, delete that directory separately after confirming that it contains only Lap database files.

## Build from Source

Requirements: Node.js 20+, pnpm, Rust stable.

#
 macOS system deps

xcode-select --install
brew install nasm pkg-config autoconf automake libtool cmake

#
 Linux system deps

#
 sudo apt install libwebkit2gtk-4.1-dev libappindicator3-dev librsvg2-dev \

#
 patchelf nasm clang pkg-config autoconf automake libtool cmake

#
 Clone and build

git clone --recursive https://github.com/julyx10/lap.git

cd
 lap
git submodule update --init --recursive
cargo install tauri-cli --version 
"
^2.0.0
"
 --locked
./scripts/download_models.sh 
#
 Windows: .\scripts\download_models.ps1

./scripts/download_ffmpeg_sidecar.sh 
#
 Windows: .\scripts\download_ffmpeg_sidecar.ps1

cd
 src-vite 
&&
 pnpm install 
&&
 
cd
 ..
cargo tauri dev

## Supported Formats

Lap supports 60+ photo, RAW, and video formats.

Type

Formats

Images

JPG/JPEG/JFIF, PNG, GIF, BMP, TIFF, WebP, HEIC/HEIF/HIF, AVIF, JXL, PSD, EXR, HDR/RGBE, TGA, JPEG 2000 (JP2/J2K/J2C/JPC/JPF/JPX), DDS, DPX, QOI

RAW photos

CR2, CR3, CRW, NEF, NRW, ARW, SRF, SR2, RAF, RW2, ORF, PEF, DNG, SRW, RWL, MRW, 3FR, MOS, DCR, KDC, ERF, MEF, RAW, MDC

Videos

MP4, MOV, M4V, MKV, AVI, FLV, TS/M2TS, WMV, WebM, 3GP/3G2, F4V, VOB, MPG/MPEG, ASF, DIVX and more. H.264 playback is supported on all platforms, with automatic compatibility processing when native playback is unavailable. HEVC/H.265 and VP9 are natively supported on macOS.

### Linux Video Playback

Lap uses system GStreamer plugins for video playback, including in the AppImage. If videos fail to play on Ubuntu, Debian, or Linux Mint, install:

sudo apt install gstreamer1.0-libav gstreamer1.0-plugins-good

## Architecture

* Core: Tauri + Rust
* Frontend: Vue + Vite + Tailwind CSS
* Data: SQLite

### Key Libraries

Library

Purpose

LibRaw

RAW image decoding and thumbnail extraction

libheif

HEIC/HEIF/HIF image decoding and preview generation

libjpeg-turbo

Fast JPEG decoding and thumbnail generation

FFmpeg

Video processing and thumbnail generation

Video.js

Cross-platform video playback UI

ONNX Runtime

Local AI model inference engine

CLIP

Image-text similarity search

InsightFace

Face detection and recognition

Leaflet

Interactive map for geotagged photos

daisyUI

UI component library

## License

GPL-3.0-or-later. SeeLICENSE.

## Privacy

Read thePrivacy Policyfor details on data handling and optional online services.