---
title: 'GitHub - notaroomba/keybytes: A truly modular keyboard · GitHub'
url: https://github.com/notaroomba/keybytes
site_name: hackernews_api
content_file: hackernews_api-github-notaroombakeybytes-a-truly-modular-keyboard
fetched_at: '2026-10-26T23:45:32.503004'
original_url: https://github.com/notaroomba/keybytes
author: NotARoomba
date: '2026-10-25'
description: A truly modular keyboard. Contribute to notaroomba/keybytes development by creating an account on GitHub.
tags:
- hackernews
- trending
---

main
Branches
Tags
Go to file
Code
Open more actions menu

## Latest commit

 

## History

41 Commits
41 Commits

## Folders and files

Name
Name
Last commit message
Last commit date
assets
assets
 
 
blender
blender
 
 
cad
cad
 
 
firmware
firmware
 
 
hardware
hardware
 
 
production
production
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
BOM.csv
BOM.csv
 
 
JOURNAL.md
JOURNAL.md
 
 
README.md
README.md
 
 
View all files

## Repository files navigation

#### A truly modular keyboard with rearrangeable keys, magnetic cases and Bluetooth!

Key Features•Video Demo•PCB•Case•Credits•License

## Video Demo

keybytes-demo.mp4

## Key Features

* Rearrangeable layoutwhere every key is its own 1u PCB
* CH32V003RISC-V microcontroller on every key
* STM32WB55RGV6main board with Bluetooth and USB
* Pogo pins on all 4 sidesof every key for power and I2C
* Magnetic casesto hold the modules together
* Key programmingfrom the main board over pogo pins
* 2MB QSPI flash(W25Q16JV) to store the key firmware
* Battery chargingwith the BQ25895 and solder pads for a 1S LiPo
* Buck-Boost converter(TPS631000)
* RGB status LED
* USB-Cwith ESD protection
* Ceramic Bluetooth antenna

## PCB

Designed in KiCad! There are two boards, the Keybit and the Keyword, and both are 1u (19.05mm x 19.05mm).

### Keybit

A single key with a Cherry MX switch and a CH32V003. Every side has pogo pins for 3.3V, GND and I2C so it can connect to the keyword or to other keybits, and the pads on the corners are for programming.

Schematic:

Layout:

### Keyword

The main board that the keybits connect to. It is split into two PCBs that stack on top of each other. The top one has the STM32WB55RGV6, the antenna and the flash, and the bottom one has the USB-C, the charger and the buck-boost converter. The 3 pogo pins on the top are for programming the keybits.

Schematic:

Layout:

3D View:

## Case

Custom designed cases inOnshape, the STEP files are in thecadfolder.

## Credits

This project uses:

* KiCad
* OnShapefor case design
* Blenderfor 3D renders
* STM32CubeMX
* Hack Club Forge

## You may also like...

* Ember- A USB-C powered reflow hotplate with Bluetooth
* Cyberboard- A Raspberry Pi Pico-sized STM32 development board with Bluetooth
* Trace- A comprehensive PCB ruler with reference footprints
* Linea- An EMR tablet

## License

MIT

notaroomba.dev· 
GitHub@NotARoomba·