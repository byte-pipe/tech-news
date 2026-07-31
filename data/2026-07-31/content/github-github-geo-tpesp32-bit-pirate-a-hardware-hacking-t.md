---
title: 'GitHub - geo-tp/ESP32-Bit-Pirate: A Hardware Hacking Tool with Web-Based CLI That Speaks Every Protocol · GitHub'
url: https://github.com/geo-tp/ESP32-Bit-Pirate
site_name: github
content_file: github-github-geo-tpesp32-bit-pirate-a-hardware-hacking-t
fetched_at: '2026-07-31T11:44:07.354501'
original_url: https://github.com/geo-tp/ESP32-Bit-Pirate
author: geo-tp
description: 'A Hardware Hacking Tool with Web-Based CLI That Speaks Every Protocol - GitHub - geo-tp/ESP32-Bit-Pirate: A Hardware Hacking Tool with Web-Based CLI That Speaks Every Protocol'
---

geo-tp

 

/

ESP32-Bit-Pirate

Public

* NotificationsYou must be signed in to change notification settings
* Fork383
* Star4.7k

 
 
 
pioarduino
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

1,413 Commits
1,413 Commits
.github/
workflows
.github/
workflows
 
 
images
images
 
 
lib
lib
 
 
partitions
partitions
 
 
src
src
 
 
test
test
 
 
webui
webui
 
 
.gitignore
.gitignore
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
platformio.ini
platformio.ini
 
 
View all files

## Repository files navigation

# ESP32 Bit Pirate

ESP32 Bit Pirateis open-source firmware that turns your device into a multi-protocol development and analysis tool, inspired by the legendary Bus Pirate.

It supports sniffing, sending, scripting, and interacting with various digital protocols (I2C, UART, 1-Wire, SPI, etc.) via a serial terminal or web-based CLI. It also communicates with radio protocols like Bluetooth, Wi-Fi, Sub-GHz and RFID.

The official project website centralizes everything:ESP32 Bit Pirate Website.

From there you caninstall the firmware, open theweb tools, followhardware guides, explorerecipes, and access thedocumentation.

## Features

* Interactive command-line interface (CLI) viaUSB Serial or WiFi Web.
* Modes for:HiZ(default)I2C(scan, glitch, slave mode, dump, eeprom)SPI(eeprom, flash, sdcard, slave mode)UART/Half-Duplex UART(bridge, read, write)1WIRE(ibutton, eeprom)2WIRE(sniff, smartcard) /3WIRE(eeprom)DIO(Digital I/O, read, pullup, set, pwm)Infrared(send, record, universal remote)USB(HID, flashrom, storage, usb-uart)Bluetooth(BLE HID, scan, spoofing, sniffing)Wi-Fi/Ethernet(sniff, deauth, nmap, netcat)JTAG(scan, SWD, openOCD)LED(animations, set LEDs)I2S(test speakers, mic, play sound)CAN(sniff, send and receive frames)SUBGHZ(analyze, record, replay)RFID(read, write, clone)RF24(scan, send, receive)FM(analyze, broadcast)CELL(dump sim card, sms, call)
* HiZ(default)
* I2C(scan, glitch, slave mode, dump, eeprom)
* SPI(eeprom, flash, sdcard, slave mode)
* UART/Half-Duplex UART(bridge, read, write)
* 1WIRE(ibutton, eeprom)
* 2WIRE(sniff, smartcard) /3WIRE(eeprom)
* DIO(Digital I/O, read, pullup, set, pwm)
* Infrared(send, record, universal remote)
* USB(HID, flashrom, storage, usb-uart)
* Bluetooth(BLE HID, scan, spoofing, sniffing)
* Wi-Fi/Ethernet(sniff, deauth, nmap, netcat)
* JTAG(scan, SWD, openOCD)
* LED(animations, set LEDs)
* I2S(test speakers, mic, play sound)
* CAN(sniff, send and receive frames)
* SUBGHZ(analyze, record, replay)
* RFID(read, write, clone)
* RF24(scan, send, receive)
* FM(analyze, broadcast)
* CELL(dump sim card, sms, call)
* Protocol sniffersI2C, UART, SPI, 1Wire, 2wire, CAN, Wi-Fi, Bluetooth, SubGhz.
* Baudrateauto-detection, AT commands and various tools for UART.
* Registers manipulation,EEPROM dump tools, identify devices for I2C.
* Read all sort ofEEPROM, Flashand various others tools for SPI.
* Scripting usingBus Pirate-style bytecodeinstructions orPython.
* Device-B-Gone command with more than80 supported INFRARED protocols.
* Direct I/O management,PWM, servo, GPIOs state.
* Analyze radio signals and frequencieson every bands.
* Near than50 addressable LEDs protocolssupported.
* Ethernet and WiFiare supported to access networks.
* Import and export data with theLittleFS over HTTP.
* Pirate assistantto help you with the firmware.
* USB-Uart dongle, SPI programmer, logic analyzerand more.
* Web Serial toolsto use USB Serial over a web browser.

## Supported Devices

Device

Description

ESP32 S3 Dev Kit

More than 20 available GPIO, 1 button

LILYGO T-Display

13 GPIO (1 Qwicc), screen, 2 buttons

LILYGO T-Embed

9 GPIO (Grove, Header), screen, encoder, speaker, mic, SD card

LILYGO T-Embed CC1101

4 GPIO (2x Qwiic), screen, encoder, speaker, mic, SD Card, CC1101, PN532, IR TX, IR RX , battery

LILYGO T-Embed CC1101 Plus

4 GPIO (2x Qwiic), screen, encoder, speaker, mic, SD Card, CC1101, NRF24, PN532, IR TX, IR RX , battery

M5 AtomS3 Lite

8 GPIO (Grove, Header), IR TX, 1 buttton

M5 Cardputer

2 GPIO (Grove), screen, keyboard, mic, speaker, IR TX, SD card, battery, 
standalone mode

M5 Cardputer ADV

12 GPIO (Grove, Header), screen, keyboard, mic, speaker, IR TX, SD card, IMU, battery, 
standalone mode

M5 StampS3

9 GPIO (exposed pins), 1 button

M5 Stick S3

13 GPIO (Grove, Header), screen, mic, speaker, IR TX, IR RX, IMU, 3 buttons, battery

Seeed Studio Xiao S3

9 GPIO (exposed pins), 1 button

* Other ESP32-S3-based BoardsAll boards based on theESP32-S3 can be supported, provided they have at least8 MB of flash.You canflash the s3 dev-kit firmware onto any ESP32-S3 board.Keep in mind that thedefault pin mapping in the firmware may not matchyour specific board.
* All boards based on theESP32-S3 can be supported, provided they have at least8 MB of flash.
* You canflash the s3 dev-kit firmware onto any ESP32-S3 board.
* Keep in mind that thedefault pin mapping in the firmware may not matchyour specific board.

## Getting Started

1. 🔧 Flash the firmware* Use theESP32 Bit Pirate Web Flasherto burn the firmware directly from a web browser.
* You can also burn it onM5Burner, in the StickS3, AtomS3, M5StampS3 or Cardputer category.
2. 🔌 Connect via Serial or Web* Serial: any terminal app, or thefree browser-based Web Serial terminal(seeConnect via Serial)
* Web: configure Wi-Fi and access the CLI via browser (seeWi-Fi Connection)
3. 🧪 Use commands like:mode
help
scan
sniff
...

## Wiki

📚Visit the Wikifor detailed documentation on every mode and command.

Includes:

* Terminal mode- About serial and web terminal.
* Mode overviews- Browse supported modes.
* Serial setup- Serial access via USB.

The wiki is the best place to learn how everything works.

## Scripting

🛠️Automate interactions with the ESP32 Bit PirateusingPython scripts over serial.

You can write and test scripts directly in the browser with theESP32 Bit Pirate Python Lab.

Including:Logging data in a file, eeprom and flash dump, interracting with GPIOs, LED animation...

## Expander

🔌Expand the capabilities of the ESP32 Bit Piratewith additional hardware modules.
The Expander adds support for theWiFi 5 GhZor other radio protocols.

## Dock

🔧A docking station for the ESP32 S3 DevKitdesigned to work with original Bus Pirate adapters.It allows you to plug and use the originalBus Pirateecosystem of adapters and accessories.

(Coming soon)

## Command-Line Interfaces

The ESP32 Bit Pirate firmware provides three command-line interface (CLI) modes:

Interface

Advantages

Ideal for...

Web Interface

- Accessible from any browser
- PC, tablets, mobiles
- Works over Wi-Fi
- No cables needed

Quick tests, demos, headless setups

Serial Interface

- Faster performance
- Instant responsiveness
- Handles large data smoothly

Intensive sessions, frequent interactions

Standalone

- Only for the Cardputer
- On device keyboard
- On device screen

Portable sessions, Quick tests

All interfaces share the same command structure and can be used interchangeably (more details).

## Mobile Web Interface over WiFi

## Standalone Mode for the Cardputer

## Browser-Based Web Serial Tools

TheESP32 Bit Pirate Web Serial Toolsprovides direct access to the Serial CLI from a compatible browser, without installing PuTTY, minicom, or another terminal application.

## Contribute

SeeHow To Contributesection, which outlines asimple way to add a new commandto any mode.

## Visuals Assets

Seeimages, logo, presentations, photo, video, illustrations. These visuals can befreely used in blog posts, documentation, videos, or articlesto help explain and promote the firmware.

## Warning

⚠️Voltage Warning: Devices should only operate at3.3Vor5V.

* Donotconnect peripherals using other voltage levels — doing so maydamage your ESP32.

⚠️Usage Warning: This firmware is provided foreducational, diagnostic, and interoperability testing purposes only.

* Do not use it to interfere with, probe, or manipulate devices without proper authorization.
* Avoid any unauthorized RF transmissions (e.g., sub-GHz) that could violate local regulations or disrupt networks and communications.
* The authors are not responsible for any misuse of this software or hardware, including legal consequences resulting from unauthorized access or signal emission.
* Always stay within the bounds of your country’s laws and responsible disclosure policies.