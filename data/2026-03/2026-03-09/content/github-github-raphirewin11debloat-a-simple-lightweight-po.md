---
title: 'GitHub - Raphire/Win11Debloat: A simple, lightweight PowerShell script that allows you to remove pre-installed apps, disable telemetry, as well as perform various other changes to declutter and customize your Windows experience. Win11Debloat works for both Windows 10 and Windows 11. · GitHub'
url: https://github.com/Raphire/Win11Debloat
site_name: github
content_file: github-github-raphirewin11debloat-a-simple-lightweight-po
fetched_at: '2026-03-09T11:18:06.795241'
original_url: https://github.com/Raphire/Win11Debloat
author: Raphire
description: A simple, lightweight PowerShell script that allows you to remove pre-installed apps, disable telemetry, as well as perform various other changes to declutter and customize your Windows experience. Win11Debloat works for both Windows 10 and Windows 11. - Raphire/Win11Debloat
---

Raphire

 

/

Win11Debloat

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star40.9k

 
 
 
 
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

361 Commits
361 Commits
.github
.github
 
 
Assets
Assets
 
 
Regfiles
Regfiles
 
 
Schemas
Schemas
 
 
Scripts
Scripts
 
 
.gitignore
.gitignore
 
 
Apps.json
Apps.json
 
 
DefaultSettings.json
DefaultSettings.json
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
Run.bat
Run.bat
 
 
Win11Debloat.ps1
Win11Debloat.ps1
 
 
View all files

## Repository files navigation

# Win11Debloat

Win11Debloat is a lightweight, easy to use PowerShell script that allows you to quickly declutter and customize your Windows experience. It can remove pre-installed bloatware apps, disable telemetry, remove intrusive interface elements and much more. No need to painstakingly go through all the settings yourself or remove apps one by one. Win11Debloat makes the process quick and easy!

The script also includes many features that system administrators and power users will enjoy. Such as a powerful command-line interface, support for Windows Audit mode and the option to make changes to other Windows users. Please refer to ourwikifor more details.

#### Did this script help you? Please consider buying me a cup of coffee to support my work

## Usage

Warning

Great care went into making sure this script does not unintentionally break any OS functionality, but use at your own risk! If you run into any issues, please report themhere.

### Quick method

Download & run the script automatically via PowerShell.

1. Open PowerShell or Terminal, preferably as an administrator.
2. Copy and paste the command below into PowerShell:

&
 ([
scriptblock
]::Create((irm 
"
https://debloat.raphi.re/
"
)))

1. Wait for the script to automatically download Win11Debloat.
2. Carefully read through and follow the on-screen instructions.

This method supports command-line parameters to customize the behaviour of the script. Please clickherefor more information.

### Traditional method

Manually download & run the script.

1. Download the latest version of the script, and extract the .ZIP file to your desired location.
2. Navigate to the Win11Debloat folder
3. Double click theRun.batfile to start the script. NOTE: If the console window immediately closes and nothing happens, try the advanced method below.
4. Accept the Windows UAC prompt to run the script as administrator, this is required for the script to function.
5. Carefully read through and follow the on-screen instructions.

### Advanced method

Manually download the script & run the script via PowerShell. Recommended for advanced users.

1. Download the latest version of the script, and extract the .ZIP file to your desired location.
2. Open PowerShell or Terminal as an administrator.
3. Temporarily enable PowerShell execution by entering the following command:

Set-ExecutionPolicy
 Unrestricted 
-
Scope 
Process
 
-
Force

1. In PowerShell, navigate to the directory where the files were extracted. Example:cd c:\Win11Debloat
2. Now run the script by entering the following command:

.\Win11Debloat.ps1

1. Carefully read through and follow the on-screen instructions.

This method supports command-line parameters to customize the behaviour of the script. Please clickherefor more information.

## Features

Below is an overview of the key features and functionality offered by Win11Debloat. Please refer tothe wikifor more information about the default settings preset.

Tip

All of the changes made by Win11Debloat can easily be reverted and almost all of the apps can be reinstalled through the Microsoft Store. A full guide on how to revert changes can be foundhere.

#### App Removal

* Remove a wide variety of preinstalled apps. Clickherefor more info.

#### Privacy & Suggested Content

* Disable telemetry, diagnostic data, activity history, app-launch tracking & targeted ads.
* Disable tips, tricks, suggestions & ads across Windows.
* Disable Windows location services & app location access.
* Disable Find My Device location tracking.
* Disable 'Windows Spotlight' and tips & tricks on the lock screen.
* Disable 'Windows Spotlight' desktop background option.
* Disable ads, suggestions and the MSN news feed in Microsoft Edge.
* Hide Microsoft 365 ads on the Settings 'Home' page, or hide the 'Home' page entirely.

#### AI Features

* Disable & remove Microsoft Copilot.
* Disable Windows Recall. (W11 only)
* Disable Click to Do, AI text & image analysis tool. (W11 only)
* Prevent AI service (WSAIFabricSvc) from starting automatically. (W11 only)
* Disable AI Features in Edge. (W11 only)
* Disable AI Features in Paint. (W11 only)
* Disable AI Features in Notepad. (W11 only)

#### System

* Disable the Drag Tray for sharing & moving files. (W11 only)
* Restore the old Windows 10 style context menu. (W11 only)
* Turn off Enhance Pointer Precision, also known as mouse acceleration.
* Disable the Sticky Keys keyboard shortcut. (W11 only)
* Disable Storage Sense automatic disk cleanup.
* Disable fast start-up to ensure a full shutdown.
* Disable BitLocker automatic device encryption.
* Disable network connectivity during Modern Standby to reduce battery drain. (W11 only)

#### Windows Update

* Prevent Windows from getting updates as soon as they're available.
* Prevent automatic restarts after updates while signed in.
* Disable sharing of downloaded updates with other PCs, also known as Delivery Optimization.

#### Appearance

* Enable dark mode for system and apps.
* Disable transparency effects
* Disable animations and visual effects.

#### Start Menu & Search

* Remove or replace all pinned apps from start for the current user, or for all existing & new users. (W11 only)
* Disable the recommended section in the start menu. (W11 only)
* Disable the Phone Link mobile devices integration in the start menu. (W11 only)
* Disable Bing web search & Copilot integration in Windows search.
* Disable Microsoft Store app suggestions in Windows search. (W11 only)
* Disable Search Highlights (dynamic/branded content) in the taskbar search box. (W11 only)
* Disable local Windows search history.

#### Taskbar

* Align taskbar icons to the left. (W11 only)
* Hide or change the search icon/box on the taskbar. (W11 only)
* Hide the taskview button from the taskbar. (W11 only)
* Disable widgets on the taskbar & lock screen.
* Hide the chat (meet now) icon from the taskbar. (W10 only)
* Enable the 'End Task' option in the taskbar right click menu. (W11 only)
* Enable the 'Last Active Click' behavior in the taskbar app area. This allows you to repeatedly click on an application's icon in the taskbar to switch focus between the open windows of that application.
* Choose how app icons are shown on the taskbar when using multiple monitors. (W11 only)
* Choose combine mode for taskbar buttons and labels. (W11 only)

#### File Explorer

* Change the default location that File Explorer opens to.
* Show file extensions for known file types.
* Show hidden files, folders and drives.
* Hide the Home or Gallery section from the File Explorer navigation pane. (W11 only)
* Hide duplicate removable drive entries from the File Explorer navigation pane, so only the entry under 'This PC' remains.
* Add all common folders (Desktop, Downloads, etc.) back to 'This PC' in File Explorer. (W11 only)
* Hide the 3D objects, music or OneDrive folder from the File Explorer navigation pane. (W10 only)
* Hide the 'Include in library', 'Give access to' and 'Share' options from the context menu. (W10 only)

#### Multi-tasking

* Disable window snapping. (W11 only)
* Disable Snap Assist suggestions when snapping a window. (W11 only)
* Disable Snap Layout suggestions when dragging windows to the top of screen and when hovering on the maximize button. (W11 only)
* Change if tabs are shown when snapping or pressing Alt+Tab. (W11 only)

#### Optional Windows Features

* Enable Windows Sandbox, a lightweight desktop environment for safely running applications in isolation. (W11 only)
* Enable Windows Subsystem for Linux which allows you to run a Linux environment directly on Windows. (W11 only)

#### Other

* Disable Xbox Game Bar integration & game/screen recording. This also disablesms-gamingoverlay/ms-gamebarpopups if you uninstall the Xbox Game Bar.
* Disable bloat in Brave browser (AI, Crypto, News, etc.)

#### Advanced Features

* Option toapply changes to a different user, instead of the currently logged in user.
* Sysprep modeto apply changes to the Windows Default user profile. Which ensures, all new users will have the changes automatically applied to them.

## Contributing

We welcome contributions of all kinds! Please see ourContributing Guidelinesfor detailed instructions on how to get started and best practices for contributing.

## License

Win11Debloat is licensed under the MIT license. See the LICENSE file for more information.

## About

A simple, lightweight PowerShell script that allows you to remove pre-installed apps, disable telemetry, as well as perform various other changes to declutter and customize your Windows experience. Win11Debloat works for both Windows 10 and Windows 11.

### Topics

 windows

 cli

 privacy

 powershell

 interactive

 tweaks

 optimize

 windows-10

 ps1

 cleanup

 windows10

 bloatware

 automated

 powershell-script

 debloat

 registry-tweaks

 windows-11

 debloater

 bloatware-removal

 windows11

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

40.9k

 stars
 

### Watchers

192

 watching
 

### Forks

1.6k

 forks
 

 Report repository

 

## Releases24

Release 2026.03.07

 Latest

 

Mar 7, 2026

 

+ 23 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* ko-fi.com/raphire

Learn more about GitHub Sponsors

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* PowerShell99.0%
* Batchfile1.0%