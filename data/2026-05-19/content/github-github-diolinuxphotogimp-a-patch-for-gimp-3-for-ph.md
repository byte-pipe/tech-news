---
title: 'GitHub - Diolinux/PhotoGIMP: A Patch for GIMP 3+ for Photoshop Users · GitHub'
url: https://github.com/Diolinux/PhotoGIMP
site_name: github
content_file: github-github-diolinuxphotogimp-a-patch-for-gimp-3-for-ph
fetched_at: '2026-05-19T12:04:01.083470'
original_url: https://github.com/Diolinux/PhotoGIMP
author: Diolinux
description: A Patch for GIMP 3+ for Photoshop Users. Contribute to Diolinux/PhotoGIMP development by creating an account on GitHub.
---

Diolinux

 

/

PhotoGIMP

Public

* NotificationsYou must be signed in to change notification settings
* Fork365
* Star10.4k

 
 
 
 
master
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

189 Commits
189 Commits
.config/
GIMP/
3.0
.config/
GIMP/
3.0
 
 
.local/
share
.local/
share
 
 
docs
docs
 
 
screenshots
screenshots
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# 🎨 PhotoGIMP

PhotoGIMPis a free, community-driven patch that transformsGIMP(GNU Image Manipulation Program) into a layout that feels familiar toAdobe Photoshopusers. If you're switching from Photoshop to GIMP and want to feel at home right away, PhotoGIMP is for you.

New to GIMP?GIMP is a free and open-source image editor available for Linux, macOS, and Windows. It can do most things Photoshop can — photo retouching, image composition, graphic design, and more — all for free. PhotoGIMP just makes itlook and feelmore like Photoshop.

## ✨ Features

* Photoshop-like tool layout— Tools are reorganized to mimic the positions you're used to in Adobe Photoshop.
* Custom Splash Screen— A unique PhotoGIMP splash screen greets you on startup.
* Maximized canvas space— Default settings are optimized to give you the largest possible working area.
* Photoshop keyboard shortcuts— Keyboard shortcuts followAdobe's official documentationfor the Windows version.
* Custom icon & name— A dedicated.desktopfile gives PhotoGIMP its own icon and app name in your system menu.

## 📷 Screenshots

PhotoGIMP Diolinux Splash Art

GIMP 3.0 with the PhotoGIMP patch applied

## 📋 Requirements

Before installing PhotoGIMP, make sure you have:

Requirement

Details

GIMP 3.0 or newer

Download from: 
gimp.org
 or 
Flathub
 (Linux)

Run GIMP at least once

GIMP needs to generate its config files before PhotoGIMP can overwrite them. 
Install GIMP → open it → close it → then install PhotoGIMP.

## ⚙ How to Install

Warning

Back up your current GIMP settings before installing!PhotoGIMP overwrites GIMP's configuration files. If you have custom settings you want to keep, save a backup copy first. See the backup instructions in each section below.

### 🐧 Flatpak (Linux)

#### Backup (optional)

If you want to keep your current GIMP settings, back them up first:

cp -r 
~
/.config/GIMP/3.0 
~
/GIMP-3.0-backup

#### Install

1. Make sure you already have GIMP installedfrom Flathub.
2. Open GIMP once, then close it— this creates the config folders that PhotoGIMP needs.
3. Download the latest release:
👉Download PhotoGIMP for Linux (.zip)
4. Extract the.zipfileinto your home folder(~).* This will place files into~/.configand~/.local, which are hidden folders.
* To see hidden folders in your file manager, pressCtrl+H.
* When prompted about existing files, choose"Replace"or"Overwrite".
5. Open GIMP — you should see the new PhotoGIMP layout! 🎉

💡 Using a non-Flatpak GIMP?

If you installed GIMP from your distro's package manager (apt, dnf, pacman, etc.) instead of Flatpak, the config folder is in the same location (~/.config/GIMP/3.0), so the steps above still work. Just make sure you have GIMP version 3.0 or newer.

### 🪟 Windows

#### Backup (optional)

If you want to keep your current GIMP settings, back them up first:

1. PressWindows+Rto open the Run dialog.
2. Type%APPDATA%\GIMPand pressEnter.
3. Copy the entire3.0folder to a safe location (e.g., your Desktop).

#### Install

1. Make sure you haveGIMP installed from the official website.
2. Open GIMP once, then close it— this creates the config folders that PhotoGIMP needs.
3. Download the latest release:
👉Download PhotoGIMP for Windows (.zip)
4. Extract the contents ofPhotoGIMP.zipto any folder (e.g., your Desktop).
5. Open the extracted folder andcopy the3.0folder.
6. PressWindows+Rto open the Run dialog.
7. Type%APPDATA%\GIMPand pressEnter— this opens GIMP's settings folder.
8. Pastethe3.0folder here.
9. When prompted about existing files, select"Replace the files in the destination".
10. Open GIMP — you should see the new PhotoGIMP layout! 🎉

💡 Optional: Change the GIMP shortcut icon

You can also downloadphotogimp.icoand update the icon on the GIMP shortcut located at:

%appdata%\Microsoft\Windows\Start Menu\Programs\GIMP 3.0.0

Right-click the shortcut →Properties→Change Icon→ browse to the downloaded.icofile.

🍫 Install via Chocolatey (alternative)

If you useChocolatey, you can install PhotoGIMP with a single command:

choco install photogimp

Maintained by:André Augusto

### 🍎 macOS

#### Backup (optional)

If you want to keep your current GIMP settings, back them up first:

1. Open Finder.
2. PressCmd+Shift+Gand go to~/Library/Application Support/GIMP.
3. Copy the entireGIMPfolder to a safe location (e.g., your Desktop).

#### Install

1. Make sure you haveGIMP installed from the official website.
2. Open GIMP once, then close it— this creates the config folders that PhotoGIMP needs.
3. Download the latest release:
👉Download PhotoGIMP for macOS (.zip)
4. Extract the contents ofPhotoGIMP.zipto any folder (e.g., your Desktop).
5. Open the extracted folder andcopy the3.0folder.
6. Open Finder, pressCmd+Shift+Gto open "Go to Folder".
7. Type~/Library/Application Support/GIMPand pressEnter.
8. If you see a2.10folder from a previous installation,delete itto avoid conflicts.
9. Pastethe3.0folder inside the GIMP folder.
10. When prompted about existing files, select"Replace"or"Merge".
11. Open GIMP — you should see the new PhotoGIMP layout! 🎉

## 📦 What's Inside the Patch

PhotoGIMP replaces or adds the following files in GIMP's configuration directory:

File / Folder

What it does

shortcutsrc

Keyboard shortcuts mapped to match Photoshop

toolrc

Tool configuration and ordering

sessionrc

Window layout and panel positions

dockrc

Dock / panel configuration

gimprc

General GIMP preferences (canvas, grid, etc.)

contextrc

Active tool/color context settings

splashes/

Custom PhotoGIMP splash screen

theme.css

Minor UI theme adjustments

templaterc

Pre-defined canvas templates

On Linux, the patch also installs:

* A custom.desktopfile (app launcher with PhotoGIMP name and icon)
* A custom application icon in~/.local/share/icons/

## 🗑 How to Uninstall

To remove PhotoGIMP and restore GIMP to its default state, simply delete GIMP's config folder and reopen GIMP — it will regenerate fresh default settings.

### Linux

rm -rf 
~
/.config/GIMP/3.0

Then open GIMP again — it will create a brand new default configuration.

If you made a backup earlier, restore it instead:

cp -r 
~
/GIMP-3.0-backup 
~
/.config/GIMP/3.0

### Windows

1. PressWindows+R, type%APPDATA%\GIMPand pressEnter.
2. Delete the3.0folder.
3. Open GIMP — it will recreate the default settings.

Or restore your backup by pasting the backed-up3.0folder back.

### macOS

1. Open Finder, pressCmd+Shift+G.
2. Go to~/Library/Application Support/GIMP.
3. Delete the3.0folder.
4. Open GIMP — it will recreate the default settings.

Or restore your backup by pasting the backed-up folder back.

## ❓ Troubleshooting / FAQ

Caution

PhotoGIMP does not have an official website.The only official source for the project is its GitHub repository:https://github.com/Diolinux/PhotoGIMP/

PhotoGIMP didn't change anything — GIMP looks the same

* Make sure you extracted the files to thecorrect location. The most common mistake is extracting to the wrong folder.
* Linux: The.configand.localfolders must be in your home directory (~). They are hidden — pressCtrl+Hin your file manager to see them.
* Windows: The3.0folder must be inside%APPDATA%\GIMP, not next to it.
* macOS: The3.0folder must be inside~/Library/Application Support/GIMP.
* Did youclose GIMPbefore pasting the files? GIMP may overwrite incoming settings on exit.

I get an error when opening GIMP after installing PhotoGIMP

* This usually means the GIMP version doesn't match. PhotoGIMP is built forGIMP 3.0+. If you're running GIMP 2.x, it won't be compatible.
* Try deleting the config folder and reinstalling — see theHow to Uninstallsection.

Can I use PhotoGIMP with GIMP 2.10?

No. This version of PhotoGIMP is designed exclusively forGIMP 3.0 and newer. The configuration format changed significantly between GIMP 2.x and 3.x.

Will PhotoGIMP delete my custom brushes, fonts, or plug-ins?

No. PhotoGIMP only replaces configuration files (shortcuts, layout, preferences). Your personal brushes, fonts, gradients, and plug-ins remain untouched.

Can I customize the shortcuts after installing PhotoGIMP?

Absolutely! PhotoGIMP just sets a starting point. You can change any shortcut in GIMP viaEdit → Keyboard Shortcuts.

How do I update PhotoGIMP to a new version?

Just download the latest release and follow the installation steps again — it will overwrite the previous PhotoGIMP configuration.

## 🤝 Contributing

Found a bug? Have a suggestion? We'd love your help!

* Report an issue:Open an issue
* Submit a fix:Create a pull request
* Translate: Help us translate the README into more languages! See theTranslationssection.

## 🌍 Translations

This README is available in other languages:

* 🇮🇹Italiano (Italian)
* 🇵🇱Polski (Polish)
* 🇧🇷Português (Brazilian Portuguese)
* 🇷🇺Русский (Russian)

Want to add your language? Fork the repo, create adocs/README_xx.mdfile, and submit a pull request!

## 🏆 Credits

* This project would not be possible without the amazingGIMPteam.
* A BIG thanks to all Diolinux's supporters onYouTube.
* Splash screen & icons fromAdriel Filipe Design.

## 👥 Contributors

## 📄 License

PhotoGIMP is licensed under theGNU General Public License v3.0.

## About

A Patch for GIMP 3+ for Photoshop Users

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

10.4k

 stars
 

### Watchers

114

 watching
 

### Forks

365

 forks
 

 Report repository

 

## Releases3

PhotoGIMP 3

 Latest

 

Mar 17, 2025

 

+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* CSS100.0%