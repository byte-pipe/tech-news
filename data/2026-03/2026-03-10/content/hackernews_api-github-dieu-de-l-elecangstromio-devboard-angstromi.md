---
title: 'GitHub - Dieu-de-l-elec/AngstromIO-devboard: AngstromIO, one of the smallest devboards out there, barely longer than a USB C connector, based on the Attiny1616 MCU. And a dual CH340 board for programming and debugging, and another devboard, based on the CH32V003 · GitHub'
url: https://github.com/Dieu-de-l-elec/AngstromIO-devboard
site_name: hackernews_api
content_file: hackernews_api-github-dieu-de-l-elecangstromio-devboard-angstromi
fetched_at: '2026-03-10T06:00:17.988682'
original_url: https://github.com/Dieu-de-l-elec/AngstromIO-devboard
author: zachlatta
date: '2026-03-08'
description: AngstromIO, one of the smallest devboards out there, barely longer than a USB C connector, based on the Attiny1616 MCU. And a dual CH340 board for programming and debugging, and another devboard, based on the CH32V003 - Dieu-de-l-elec/AngstromIO-devboard
tags:
- hackernews
- trending
---

Dieu-de-l-elec

 

/

AngstromIO-devboard

Public

* NotificationsYou must be signed in to change notification settings
* Fork4
* Star211

 
 
 
 
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

38 Commits
38 Commits
IMG
IMG
 
 
AIO schematic.svg
AIO schematic.svg
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

# AngstromIO-devboard

AngstromIO is one of the smallest devboards out there, barely longer than a USB-C connector, based on the Attiny1616 MCU. 2 GPIOs as well as I2C lines are broken out.
I made a dual CH340 programming board too, both for UPDI programming and debugging (one way Serial Communication).
I also designed a breadboard friendly, experimentation board for the CH32V003, with a 4 by 5 charlieplexed LED matrix.

While the AngstromIO is a tiny devboard, yet powerful, that could be embbeded in any space constrained projects, the CH32 devboard is more an experimentation board, for me to learn how to program this awesome chip on the MounriverStudio programming and how to program a charlieplexed matrix. The Programmer is an all in one module, that will make debugging with the Serial monitor while programming easy: one board for both.

# Key features:

### AngstromIO Key features:

* One of the smallest devboards: 8.9mm by 9mm, USB-C included
* Attiny1616 MCU, 16Kb flash, low power, arduino compatible (for basic libraries at least)
* USB-C for power, runs at 5V
* 2x RGB addressable LEDs (SK6805-EC15)
* Pins broken out: SCL, SDA, PB2 (TX), PA3, +5V, GND, and UPDI for programming

### Programmer Key features:

* Dual CH340E setup:One for programming (set as SerialUPDI programmer),One for debugging (Serial Communication, USB to UART)
* One for programming (set as SerialUPDI programmer),
* One for debugging (Serial Communication, USB to UART)
* 2 USB-C for data transfer, only the USB-C for Serial provides 5V to the board
* On board 3.3V LDO
* 3.3V/5V operating voltage selection

### CH32 devboard Key features:

* Breadboard friendly devboard
* cheap 25cents CH32V003, Risc-V MCU, 26Kb flash
* USB-C for power, the CH32 runs at 3.3V but PC6 and PC5 are 5V tolerant
* On board 3.3V LDO
* 4x5 charlieplexed LED matrix
* SWIO programming, proper programmer required (WCH linkE)

# Pinout:

# Software:

### AngstromIO Software:

Arduino compatible, some libraries may not work, but some have been arranged/made by SpenceKonde like Wire (I2C) and tinyNeoPixel (for more information, see:https://github.com/SpenceKonde/megaTinyCore/tree/master/megaavr/libraries)

### CH32 devboard Software:

Programmed on the Mounriver studio IDE

# PCB design:

PCB designed in EasyEDA Pro, 2 layers, 1.0mm thick, Purple soldermask
All 3 designs panelized into one PCB.

# Schematic:

# PCB Layout:

# Renders:

🚧 to be continued...

# BOM:

### AngstromIO BOM:

🚧 coming soon...

### Programmer BOM:

🚧 coming soon...

### CH32 devboard BOM:

🚧 coming soon...

## About

AngstromIO, one of the smallest devboards out there, barely longer than a USB C connector, based on the Attiny1616 MCU. And a dual CH340 board for programming and debugging, and another devboard, based on the CH32V003

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

211

 stars
 

### Watchers

2

 watching
 

### Forks

4

 forks
 

 Report repository

 

## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors1

* Dieu-de-l-elecC Gaillard