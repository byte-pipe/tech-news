---
title: 'GitHub - TomBadash/MouseControl: A lightweight, open-source alternative to Logitech Options+ for remapping buttons on the Logitech MX Master 3S mouse · GitHub'
url: https://github.com/TomBadash/MouseControl
site_name: hnrss
content_file: hnrss-github-tombadashmousecontrol-a-lightweight-open-so
fetched_at: '2026-03-14T11:09:08.440649'
original_url: https://github.com/TomBadash/MouseControl
date: '2026-03-13'
description: A lightweight, open-source alternative to Logitech Options+ for remapping buttons on the Logitech MX Master 3S mouse - TomBadash/MouseControl
tags:
- hackernews
- hnrss
---

TomBadash

 

/

MouseControl

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork4
* Star493

 
 
 
 
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

13 Commits
13 Commits
.github
.github
 
 
core
core
 
 
images
images
 
 
ui
ui
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
Mouser.bat
Mouser.bat
 
 
Mouser.spec
Mouser.spec
 
 
README.md
README.md
 
 
build.bat
build.bat
 
 
main_qml.py
main_qml.py
 
 
readme_mac_osx.md
readme_mac_osx.md
 
 
requirements.txt
requirements.txt
 
 
View all files

## Repository files navigation

# Mouser — MX Master 3S Button Remapper

A lightweight, open-source, fully local alternative toLogitech Options+for
remapping every programmable button on theLogitech MX Master 3Smouse.

No telemetry. No cloud. No Logitech account required.

## Features

* macOS support—full macOS compatibility added thanks toandrew-sz, using CGEventTap for mouse hooking, Quartz CGEvent for key simulation, and NSWorkspace for app detection. SeemacOS Setup Guidefor details.
* Remap all 6 programmable buttons— middle click, gesture button, back, forward, horizontal scroll left/right
* Per-application profiles— automatically switch button mappings when you switch apps (e.g., different bindings for Chrome vs. VS Code)
* 22 built-in actionsacross navigation, browser, editing, and media categories
* DPI / pointer speed control— slider from 200–8000 DPI with quick presets, synced to the device via HID++
* Scroll direction inversion— independent toggles for vertical and horizontal scroll
* Gesture button support— full HID++ 2.0 divert on Bluetooth (no Logitech software needed)
* Auto-reconnection— automatically detects when the mouse is turned off/on or disconnected/reconnected and restores full functionality without restarting the app
* Live connection status— the UI shows a real-time "Connected" / "Not Connected" badge that updates as the mouse connects or disconnects
* Modern Qt Quick UI— dark Material theme with interactive mouse diagram and per-button action picker
* System tray— runs in background, hides to tray on close, toggle remapping on/off from tray menu
* Auto-detect foreground app— polls the active window and switches profiles instantly
* Zero external services— config is a local JSON file, all processing happens on your machine

## Screenshots

The UI shows an interactive diagram of the MX Master 3S. Click any button's hotspot dot to change its action.

## Supported Device

Property

Value

Device

Logitech MX Master 3S

Product ID

0xB034

Protocol

HID++ 4.5 (Bluetooth)

Connection

Bluetooth (USB receiver also works for basic buttons)

Note:The architecture is designed to be extensible to other Logitech HID++ mice, but only the MX Master 3S is tested.

## Default Mappings

Button

Default Action

Back button

Alt + Tab (Switch Windows)

Forward button

Alt + Tab (Switch Windows)

Middle click

Pass-through

Gesture button

Pass-through

Horizontal scroll left

Browser Back

Horizontal scroll right

Browser Forward

## Available Actions

Category

Actions

Navigation

Alt+Tab, Alt+Shift+Tab, Show Desktop (Win+D), Task View (Win+Tab)

Browser

Back, Forward, Close Tab (Ctrl+W), New Tab (Ctrl+T)

Editing

Copy, Paste, Cut, Undo, Select All, Save, Find

Media

Volume Up, Volume Down, Volume Mute, Play/Pause, Next Track, Previous Track

Other

Do Nothing (pass-through)

## Download & Run

No install required.Just download, extract, and double-click.

### Steps

1. Download→Mouser.zip(44 MB)
2. Extractthe zip to any folder (Desktop, Documents, wherever you like)
3. RunMouser.exe

That's it — the app will open and start remapping your mouse buttons immediately.

### What to expect

* Thesettings windowopens showing your mouse diagram
* Asystem tray iconappears near the clock (bottom-right)
* Button remapping isactive immediately
* Closing the windowdoesn't quitthe app — it keeps running in the tray
* To fully quit: right-click the tray icon →Quit Mouser

### First-time notes

* Windows SmartScreenmay show a warning the first time → clickMore info → Run anyway
* Logitech Options+must not be running (it conflicts with HID++ access)
* Config is saved automatically to%APPDATA%\Mouser

## Installation (from source)

### Prerequisites

* Windows 10/11ormacOS 12+ (Monterey)
* Python 3.10+(tested with 3.14)
* Logitech MX Master 3Spaired via Bluetooth or USB receiver
* Logitech Options+ must NOT be running(it conflicts with HID++ access)
* macOS only:Accessibility permission required (System Settings → Privacy & Security → Accessibility)

### Steps

#
 1. Clone the repository

git clone https://github.com/TomBadash/MouseControl.git

cd
 MouseControl

#
 2. Create a virtual environment

python -m venv .venv

#
 3. Activate it

.venv
\S
cripts
\a
ctivate 
#
 Windows (PowerShell / CMD)

source
 .venv/bin/activate 
#
 macOS / Linux

#
 4. Install dependencies

pip install -r requirements.txt

### Dependencies

Package

Purpose

PySide6

Qt Quick / QML UI framework

hidapi

HID++ communication with the mouse (gesture button, DPI)

pystray

System tray icon (legacy, may be removed)

Pillow

Image processing for icon generation

### Running

#
 Option A: Run directly

python main_qml.py

#
 Option B: Use the batch file (shows a console window)

Mouser.bat

#
 Option C: Use the desktop shortcut (no console window)

#
 Double-click Mouser.lnk

Tip:To run without a console window, usepythonw.exe main_qml.pyor the.lnkshortcut.

### Creating a Desktop Shortcut

AMouser.lnkshortcut is included. To create one manually:

$s
 
=
 (
New-Object
 
-
ComObject WScript.Shell).CreateShortcut(
"
$
(
[
Environment
]::GetFolderPath(
'
Desktop
'
)
)
\Mouser.lnk
"
)

$s
.TargetPath
 
=
 
"
C:\path\to\mouser\.venv\Scripts\pythonw.exe
"

$s
.Arguments
 
=
 
"
main_qml.py
"

$s
.WorkingDirectory
 
=
 
"
C:\path\to\mouser
"

$s
.IconLocation
 
=
 
"
C:\path\to\mouser\images\logo.ico, 0
"

$s
.Save
()

### Building the Portable App

To produce a standaloneMouser.exethat anyone can download and run without Python:

#
 1. Install PyInstaller (inside your venv)

pip install pyinstaller

#
 2. Build using the included spec file

pyinstaller Mouser.spec --noconfirm

#
 — or simply run the build script —

build.bat

The output is indist\Mouser\. Zip that entire folder and distribute it.

## How It Works

### Architecture

┌─────────────┐ ┌──────────┐ ┌────────────────┐
│ Mouse HW │────▶│ Mouse │────▶│ Engine │
│ (MX Master) │ │ Hook │ │ (orchestrator) │
└─────────────┘ └──────────┘ └───────┬────────┘
 ▲ │
 block/pass ┌────▼────────┐
 │ Key │
┌─────────────┐ ┌──────────┐ │ Simulator │
│ QML UI │◀───▶│ Backend │ │ (SendInput) │
│ (PySide6) │ │ (QObject)│ └─────────────┘
└─────────────┘ └──────────┘
 ▲
 ┌────┴────────┐
 │ App │
 │ Detector │
 └─────────────┘

### Mouse Hook (mouse_hook.py)

Alow-level Windows mouse hook(SetWindowsHookExWwithWH_MOUSE_LL) runs on a dedicated background thread with its own Win32 message pump. It intercepts:

* WM_XBUTTONDOWN/UP— side buttons (back/forward)
* WM_MBUTTONDOWN/UP— middle click
* WM_MOUSEHWHEEL— horizontal scroll
* WM_MOUSEWHEEL— vertical scroll (for inversion)

Intercepted events are eitherblocked(hook returns 1) and replaced with an action, orpassed throughto the application.

### Gesture Button Detection (3-tier)

The MX Master 3S gesture button doesn't send standard mouse events. Mouser uses a 3-tier detection system:

1. HID++ 2.0(primary, Bluetooth) — Opens the Logitech HID collection, discoversREPROG_CONTROLS_V4(feature0x1B04), and diverts CID0x00C3(gesture button). Best reliability.
2. Raw Input(fallback) — Registers for raw mouse input and detects extra button bits beyond the standard 5.
3. Middle-click fallback— When gesture button has an action but middle-click is unassigned, middle-click events route to the gesture action.

### App Detector (app_detector.py)

Polls the foreground window every 300ms usingGetForegroundWindow→GetWindowThreadProcessId→ process name. Handles UWP apps by resolvingApplicationFrameHost.exeto the actual child process.

### Engine (engine.py)

The central orchestrator. On app change, it performs alightweight profile switch— clears and re-wires hook callbacks without tearing down the hook thread or HID++ connection. This avoids the latency and instability of a full hook restart.

### Device Reconnection

Mouser handles mouse power-off/on cycles automatically:

* HID++ layer—HidGestureListenerdetects device disconnection (read errors) and enters a reconnect loop, retrying every 2–5 seconds until the device is back
* Hook layer—MouseHooklistens forWM_DEVICECHANGEnotifications and reinstalls the low-level mouse hook when devices are added or removed
* UI layer— connection state flows from HID++ → MouseHook → Engine → Backend (cross-thread safe via Qt signals) → QML, updating the status badge in real time

### Configuration

All settings are stored in%APPDATA%\Mouser\config.json(Windows) or~/Library/Application Support/Mouser/config.json(macOS). The config supports:

* Multiple named profiles with per-profile button mappings
* Per-profile app associations (list of.exenames)
* Global settings: DPI, scroll inversion, start options
* Automatic migration from older config versions

## Project Structure

mouser/
├── main_qml.py # Application entry point (PySide6 + QML)
├── Mouser.bat # Quick-launch batch file
├── README.md
├── requirements.txt
├── .gitignore
│
├── core/ # Backend logic
│ ├── engine.py # Core engine — wires hook ↔ simulator ↔ config
│ ├── mouse_hook.py # Low-level mouse hook + HID++ gesture listener
│ ├── hid_gesture.py # HID++ 2.0 gesture button divert (Bluetooth)
│ ├── key_simulator.py # SendInput-based action simulator (22 actions)
│ ├── config.py # Config manager (JSON load/save/migrate)
│ └── app_detector.py # Foreground app polling
│
├── ui/ # UI layer
│ ├── backend.py # QML ↔ Python bridge (QObject with properties/slots)
│ └── qml/
│ ├── Main.qml # App shell (sidebar + page stack + tray toast)
│ ├── MousePage.qml # Merged mouse diagram + profile manager
│ ├── ScrollPage.qml # DPI slider + scroll inversion toggles
│ ├── HotspotDot.qml # Interactive button overlay on mouse image
│ ├── ActionChip.qml # Selectable action pill
│ └── Theme.js # Shared colors and constants
│
└── images/
 ├── mouse.png # MX Master 3S top-down diagram
 ├── logo.png # Mouser logo (source)
 ├── logo.ico # Multi-size icon for shortcuts
 ├── logo_icon.png # Square icon with background
 ├── chrom.png # App icon: Chrome
 ├── VSCODE.png # App icon: VS Code
 ├── VLC.png # App icon: VLC
 └── media.webp # App icon: Windows Media Player

## UI Overview

The app has two pages accessible from a slim sidebar:

### Mouse & Profiles (Page 1)

* Left panel:List of profiles. The "Default (All Apps)" profile is always present. Per-app profiles show the app icon and name. Select a profile to edit its mappings.
* Right panel:Interactive mouse diagram with clickable hotspot dots on each button. Click a dot to expand an action picker with categorized chips. Changes save instantly to the selected profile.
* Add profile:ComboBox at the bottom lists known apps (Chrome, Edge, VS Code, VLC, etc.). Click "+" to create a per-app profile.

### Point & Scroll (Page 2)

* DPI slider:200–8000 with quick presets (400, 800, 1000, 1600, 2400, 4000, 6000, 8000). Reads the current DPI from the device on startup.
* Scroll inversion:Independent toggles for vertical and horizontal scroll direction.

## Known Limitations

* Windows & macOS only— Linux is not yet supported
* MX Master 3S only— HID++ feature indices and CIDs are hardcoded for this device (PID0xB034)
* Bluetooth recommended— HID++ gesture button divert works best over Bluetooth; USB receiver has partial support
* Conflicts with Logitech Options+— both apps fight over HID++ access; quit Options+ before running Mouser
* Scroll inversion is experimental— uses coalescedPostMessageinjection to avoid LL hook deadlocks; may not work perfectly in all apps
* Admin not required— but some games or elevated windows may not receive injected keystrokes

## Future Work

* More devices— support other Logitech HID++ mice (MX Master 3, MX Anywhere 3, etc.)
* Custom key combos— let users define arbitrary key sequences (e.g., Ctrl+Shift+P)
* Start with Windows— autostart via registry or Task Scheduler
* Improved scroll inversion— explore driver-level or interception-driver approaches
* Gesture button actions— swipe gestures (up/down/left/right) for multi-action gesture button
* Per-app profile auto-creation— detect new apps and prompt to create a profile
* Export/import config— share configurations between machines
* Tray icon badge— show active profile name in tray tooltip
* macOS support— added via CGEventTap, Quartz CGEvent, and NSWorkspace (thanks@andrew-sz)
* Linux support— investigatelibevdev/evdevhooks
* Plugin system— allow third-party action providers

## Contributing

Contributions are welcome! To get started:

1. Fork the repo and create a feature branch
2. Set up the dev environment (seeInstallation)
3. Make your changes and test with an MX Master 3S
4. Submit a pull request with a clear description

### Areas where help is needed

* Testing with other Logitech HID++ devices
* Scroll inversion improvements
* Linux porting
* UI/UX polish and accessibility

## Support the Project

If Mouser saves you from installing Logitech Options+, consider supporting development:

Every bit helps keep the project going — thank you!

## License

This project is licensed under theMIT License.

## Acknowledgments

* @andrew-sz— macOS port: CGEventTap mouse hooking, Quartz key simulation, NSWorkspace app detection, and NSEvent media key support

Mouseris not affiliated with or endorsed by Logitech. "Logitech", "MX Master", and "Options+" are trademarks of Logitech International S.A.

## About

A lightweight, open-source alternative to Logitech Options+ for remapping buttons on the Logitech MX Master 3S mouse

### Topics

 python

 macos

 linux

 productivity

 automation

 logitech

 logi

 controler

 mx-master

 logitech-options

 mouse-remapping

 mx-master-3s

 mx-master-4

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

493

 stars
 

### Watchers

2

 watching
 

### Forks

4

 forks
 

 Report repository

 

## Releases1

LogiControl v1.0.0

 Latest

 

Mar 2, 2026

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors1

* TomBadash

## Languages

* Python64.1%
* QML33.6%
* Batchfile1.6%
* JavaScript0.7%