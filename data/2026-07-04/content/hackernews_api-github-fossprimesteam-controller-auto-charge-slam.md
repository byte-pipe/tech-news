---
title: 'GitHub - FossPrime/Steam-Controller-Auto-Charge: Slam the controller into the magnetic puck until it charges · GitHub'
url: https://github.com/FossPrime/Steam-Controller-Auto-Charge
site_name: hackernews_api
content_file: hackernews_api-github-fossprimesteam-controller-auto-charge-slam
fetched_at: '2026-07-04T19:31:08.222466'
original_url: https://github.com/FossPrime/Steam-Controller-Auto-Charge
author: zdw
date: '2026-07-03'
description: Slam the controller into the magnetic puck until it charges - FossPrime/Steam-Controller-Auto-Charge
tags:
- hackernews
- trending
---

FossPrime

 

/

Steam-Controller-Auto-Charge

Public

* NotificationsYou must be signed in to change notification settings
* Fork9
* Star299

 
 
 
 
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
.github/
workflows
.github/
workflows
 
 
data
data
 
 
public
public
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
index.html
index.html
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
shell.nix
shell.nix
 
 
triton_2026_steam_controller_spec.md
triton_2026_steam_controller_spec.md
 
 
tsconfig.app.json
tsconfig.app.json
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
vite.config.ts
vite.config.ts
 
 
View all files

## Repository files navigation

# Steam Controller Auto-Charge

Steam Controller Auto-Charge is an open-source web application designed to automatically pilot a Steam Controller into its magnetic charging puck using optical flow computer vision and WebHID telemetry.

## Features

* Optical Flow Tracking:Utilizes OpenCV.js to track user-selected points on the controller and the charging puck via an overhead camera.
* WebHID Telemetry & Haptic Navigation:Connects to the Triton Controller natively via WebHID, streaming input and telemetry (Report 67). Navigates the controller towards the puck by firing 70Hz asymmetric haptic pulses through the internal dual Linear Resonant Actuators (LRAs).
* Proximity Creep Mode:Automatically cuts haptic pulse frequency by 50% when the controller is within 150 pixels of the puck to ensure a gentle magnetic dock.
* Battery Status Polling:Intercepts Report ID121(0x79) to confirm successful magnetic charging, and parses Report ID67(0x43) to display live battery percentage and battery cell voltage (mV).

## Setup

### Requirements

* Nix Package Manager: Theonlybuild dependency you need. It works seamlessly on Windows, Mac, and Linux.A Chromium-based browser supporting the WebHID API.An overhead webcam pointing down at your desk.
* A Chromium-based browser supporting the WebHID API.
* An overhead webcam pointing down at your desk.

1. Mount a webcam directly overhead pointing at the desk.
2. Start the project with a single command (this will automatically fetch dependencies and build the WASM module):

nix-shell --run 
"
npm install && npm run dev
"

## Usage

1. Mount a webcam directly overhead pointing at the desk.
2. Place the Steam Controller Auto-Charge puck on the desk.
3. Place your Steam Controller on the desk, upright.
4. Open the web interface and clickConnect Steam Controllerto pair it via WebHID.
5. Click✨ Auto-Trackto engage automatic tracking. The button will highlight to indicate it's active and will automatically resume tracking on page reload. Click it again to disengage.
6. The controller will now autonomously navigate to the puck using a Lucas-Kanade optical flow loop combined with object avoidance powered by an in-browser Rust/WASM CNN!

(Note: Manual tracking is still available if you prefer. Just click the puck, then the top of the controller, then the bottom of the controller).

## Architecture

* App.vue: Vue 3 application logic handling camera streams, UI reactivity, PID tracking loop, and OpenCV.js Lucas-Kanade optical flow (calcOpticalFlowPyrLK).
* steamController.ts: WebHID abstraction class mapping standard API calls to the Steam Controller's specific byte payloads for LRA pulses and battery status polling.
* objectDetector.ts&objectWorker.ts: Offloads object detection to a Web Worker to ensure the main tracking loop remains fluid.
* wasm-object-detect/: Rust implementation compiled to WebAssembly for high-performance visual processing.

## Thanks

Huge thanks to Very Lazy Pixel for inspiring this project!
Check out their video here:https://www.youtube.com/watch?v=g-8S8zk4dn8

## License

This project is licensed under the MIT License - see theLICENSEfile for details.

## About

Slam the controller into the magnetic puck until it charges

fossprime.github.io/Steam-Controller-Auto-Charge/

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

299

 stars
 

### Watchers

2

 watching
 

### Forks

9

 forks
 

 Report repository

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Vue31.2%
* TypeScript30.6%
* Rust25.2%
* Python6.7%
* CSS3.8%
* Nix2.2%
* HTML0.3%