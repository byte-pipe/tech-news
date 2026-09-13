---
title: Reverse engineering my e-scooter and rewriting the firmware in rust | Blog
url: https://bensimms.moe/reverse-engineering-scooter/
site_name: hackernews_api
content_file: hackernews_api-reverse-engineering-my-e-scooter-and-rewriting-the
fetched_at: '2026-09-13T21:17:57.460670'
original_url: https://bensimms.moe/reverse-engineering-scooter/
author: vinhnx
date: '2026-09-10'
published_date: '2026-08-09'
description: Reverse engineering my e-scooter and rewriting the firmware in Rust
tags:
- hackernews
- trending
---

..
/
reverse-engineering-scooter

Published on2026-08-09

By 
Ben

# Reverse engineering my e-scooter and rewriting the firmware in rust

I reverse engineered the hardware and firmware of my Egret GT E-Scooter. I describe how I got in, analysed communication between components, and reverse engineered firmware. I speak about writing custom firmware for the display unit.

### Introduction

Last year, I bought myself anEgret GT. It’s an e-scooter that touts a range of 100km and has very large tyres which makes driving it quite comfortable. To make sure you know that it’s a high-end e-scooter, it comes with a 320x480 LCD display used as a HUD, on which the speed, driving mode, battery level and range are displayed.

Now because I have tobreaktinker with everything I own, I eventually decided to start figuring out how this thing worked. I can’t remember exactly why, but it was possibly due to the fact that holding the ‘down’ button on the keypad while powering the scooter would cause it to enter a firmware update mode. If you clicked a button to exit this menu, you would enter the normal ‘driving’ mode, and would be able to use the scooter without entering the PIN. While I always secure the scooter with a reasonably good lock, this still irked me a bit.

The first thing I started on was the mobile app, which allows you to unlock the scooter remotely, change a few settings, and view the battery level. I won’t bore you with the process, but what I found from skimming through the bluetooth handlers of the app was the following:

1. The scooter can perform firmware updates over bluetooth, and seemingly there exists a few different places a firmware update can go (display, controller, button panel).
2. Some metrics which are not shown in the app or on the scooter are transmitted over bluetooth, such as the time spent in each driving mode, device temperature, motor current, battery voltage, battery charging history. Details such as the total driving time, odometer, and charge history are transmitted to the manufacturer and stored attached to the scooter’s ID, this behaviour is not clearly mentioned in the app :)))))))
3. The scooter doesn’t know its Vehicle Identification Number until the app connects and sets it. If you set this using a bluetooth debug app yourself, the Egret app can be spoofed to think the scooter is a different model. I tried to spoof the VIN of the 45km/h model of the scooter to see if the speed limit was implemented with such a simple check, but this didn’t work.

Eventually I became bored at playing with the bluetooth interface and turned to the USB-C port on the display. The manufacturer states that this is just for charging phones, and after some testing with different devices I did conclude that if the data pins were connected, the display unit wouldn’t act as either a USB host or device. But I knew better, and ordered a USB-C breakout board. When this arrived, I plugged it in and probed each pin with an oscilloscope. To my surprise, two of the USB-C pins were being used as a CAN bus (which smells horribly noncompliant).

### CAN Bus sniffing

Figure 1: An oscilloscope attached to the CAN bus of the scooter, decoding messages.

To sniff this can traffic, I threw together an abomination (pictured inFigure 2) using an ESP32-C6, a SN65HVD230, and a MCP2515^0.

Figure 2: The device

I put together a quick program which initialised the CAN peripherals and logged every can message. Then I plugged my CAN logger into the scooter and recorded the messages during startup:

Copy code
Copy
Copied!
1
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
2
CAN_FRAME:1025,false,[74, bd, 0, 0, 16, c, 0, 0]
3
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
4
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
5
CAN_FRAME:1025,false,[74, bd, 0, 0, 16, c, 0, 0]
6
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
7
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
8
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
9
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
10
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
11
CAN_FRAME:1025,false,[73, bd, 0, 0, 3, c, 0, 0]
12
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
13
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
14
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
15
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
16
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
17
CAN_FRAME:1025,false,[73, bd, 0, 0, 3, c, 0, 0]
18
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
19
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
20
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
21
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
22
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
23
CAN_FRAME:1025,false,[72, bd, 0, 0, ef, b, 0, 0]
24
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
25
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
26
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
27
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
28
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
29
CAN_FRAME:1025,false,[72, bd, 0, 0, ef, b, 0, 0]
30
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
31
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
32
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
33
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
34
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
35
CAN_FRAME:1025,false,[74, bd, 0, 0, e9, b, 0, 0]
36
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
37
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
38
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
39
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
40
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
41
CAN_FRAME:1025,false,[74, bd, 0, 0, e9, b, 0, 0]
42
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
43
CAN_FRAME:774,false,[55, 0, 0, 0, 2, 0, 0, 0]
44
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
45
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
46
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
47
CAN_FRAME:768,false,[0, 5a, 64, 5a, 64, 0, 0, 0]
48
CAN_FRAME:494,false,[60, 0, 0, 0, 0, 0, 0, 0]
49
CAN_FRAME:495,false,[4c, 44, 2e, 43, 52, 2e, 53, 38]
50
CAN_FRAME:495,false,[30, 37, 2e, 43, 2e, 32, 2e, 31]
51
CAN_FRAME:495,false,[45, 47, 2e, 32, 2e, 32, 2e, 31]
52
CAN_FRAME:495,false,[31, 0, 0, 0, 0, 0, 0, 0]
53
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
54
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
55
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
56
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
57
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
58
CAN_FRAME:768,false,[0, 5a, 64, 5a, 64, 0, 0, 0]
59
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
60
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
61
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
62
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
63
CAN_FRAME:1856,true,[4b, 0]
64
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
65
CAN_FRAME:1025,false,[74, bd, 0, 0, e4, b, 0, 0]
66
CAN_FRAME:1857,true,[4b, 0, 0, 0, 69, 99, 52, 42]
67
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
68
CAN_FRAME:1860,true,[1]
69
CAN_FRAME:1861,true,[1, 15, 57, 20, 50, 59, 54, 34]
70
CAN_FRAME:774,false,[54, 0, 0, 0, 2, 0, 0, 0]
71
CAN_FRAME:513,false,[0, 0, 0, 0, 2]
72
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, ff, 1f]
73
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
74
CAN_FRAME:768,false,[0, 5a, 64, 5a, 64, 0, 0, 0]
Copy code
Copy
Copied!
1
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
2
CAN_FRAME:1025,false,[74, bd, 0, 0, 16, c, 0, 0]
3
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
4
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
5
CAN_FRAME:1025,false,[74, bd, 0, 0, 16, c, 0, 0]
6
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
7
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
8
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
9
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
10
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
11
CAN_FRAME:1025,false,[73, bd, 0, 0, 3, c, 0, 0]
12
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
13
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
14
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
15
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
16
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
17
CAN_FRAME:1025,false,[73, bd, 0, 0, 3, c, 0, 0]
18
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
19
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
20
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
21
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
22
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
23
CAN_FRAME:1025,false,[72, bd, 0, 0, ef, b, 0, 0]
24
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
25
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
26
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
27
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
28
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
29
CAN_FRAME:1025,false,[72, bd, 0, 0, ef, b, 0, 0]
30
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
31
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
32
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
33
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
34
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
35
CAN_FRAME:1025,false,[74, bd, 0, 0, e9, b, 0, 0]
36
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
37
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
38
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
39
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
40
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
41
CAN_FRAME:1025,false,[74, bd, 0, 0, e9, b, 0, 0]
42
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
43
CAN_FRAME:774,false,[55, 0, 0, 0, 2, 0, 0, 0]
44
CAN_FRAME:513,false,[0, 0, 0, 0, 0]
45
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, 21, 0]
46
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
47
CAN_FRAME:768,false,[0, 5a, 64, 5a, 64, 0, 0, 0]
48
CAN_FRAME:494,false,[60, 0, 0, 0, 0, 0, 0, 0]
49
CAN_FRAME:495,false,[4c, 44, 2e, 43, 52, 2e, 53, 38]
50
CAN_FRAME:495,false,[30, 37, 2e, 43, 2e, 32, 2e, 31]
51
CAN_FRAME:495,false,[45, 47, 2e, 32, 2e, 32, 2e, 31]
52
CAN_FRAME:495,false,[31, 0, 0, 0, 0, 0, 0, 0]
53
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
54
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
55
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
56
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
57
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
58
CAN_FRAME:768,false,[0, 5a, 64, 5a, 64, 0, 0, 0]
59
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
60
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
61
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
62
CAN_FRAME:495,false,[0, 0, 0, 0, 0, 0, 0, 0]
63
CAN_FRAME:1856,true,[4b, 0]
64
CAN_FRAME:1024,false,[0, 40, 87, 4, 0, 0, 0, 0]
65
CAN_FRAME:1025,false,[74, bd, 0, 0, e4, b, 0, 0]
66
CAN_FRAME:1857,true,[4b, 0, 0, 0, 69, 99, 52, 42]
67
CAN_FRAME:1028,false,[20, 4e, 0, 0, 1, 0, b9, b]
68
CAN_FRAME:1860,true,[1]
69
CAN_FRAME:1861,true,[1, 15, 57, 20, 50, 59, 54, 34]
70
CAN_FRAME:774,false,[54, 0, 0, 0, 2, 0, 0, 0]
71
CAN_FRAME:513,false,[0, 0, 0, 0, 2]
72
CAN_FRAME:515,false,[0, 0, 0, 0, 0, 0, ff, 1f]
73
CAN_FRAME:528,false,[0, 0, 0, 0, 0, 0, 0, 0]
74
CAN_FRAME:768,false,[0, 5a, 64, 5a, 64, 0, 0, 0]

The CAN bus proved to be quite noisy, so to figure out what was going on I built a small tool usingeguito show a plot of can messages against time. By plotting each can message as a dot with the y-axis as the can message ID, it becomes very easy to identify which messages are commands, responses, and periodic data.

Unfortunately at this point I still didn’t have a good idea which purpose each message had. But by sniffing the bus while running the scooter, I was able to quickly figure out which messages were used in communicating the throttle, driving mode, and motor speed:

* 0x300: Sent by the display to the controller. Contains the current driving mode (walk, eco, drive, sport), whether the headlight is on, and in walk mode contains a counter in the last nibble. Sending a message where the fourth byte isa5instead of the usual5acauses the controller to reset.An example iswhich decodes to:Driving modeWalk (0x00_90)HeadlightOperating (0x64)Walk counter0
* 0x306: Sent by the display to the controller. Contains the throttle position, the blinker lights, and the speed limit of the scooter. The speed limit has no effect on the standard GT controller, but on the GTS it sets the speed limit to 25, 35, or 45km/h. For some reason the throttle level is transmitted as a 9 bit unsigned integer with the MSB being the first bit of the second byte.An example iswhich decodes to:Throttle511Left blinkertrueRight blinkerfalseSpeed limit25km/h (0)
* 0x201: Contains motor speed, and some status flags.An example iswhich decodes to:Motor speed1031Walk modefalseHeadlight onfalseBrake light ontrue

In the end, I documented all of the CAN messages:here.

At this point I was now able to do some amusing stuff, like controlling the scooter’s motor remotely, but this isn’t very practical or interesting. This project kind of stalled at this point as I had no access to the firmware and therefore there was little more I could do. A few months later I noticed that it was possible to buy replacement motor controller and display units online. I couldn’t resist the opportunity, so I ordered replacements of both.

### Teardowns and firmware extraction

The first component I tore down was the controller. This was particularly difficult as the rear plate was secured very tightly with crosshead screws, of which the heads of two stripped immediately, requiring me to dremel a slot. The device was also filled with some type of potting compound, but very thankfully the compound was actually quite soft and could easily be scraped away.

After removing the potting compound, I was presented with quite the gift: None of the active components had had their markings etched away, and there was a row of four pads on the back side of the board. The MCU was marked with APM32E103xCxE (a STM32F103 clone), therefore these pins are very likely the SWD port. By usingOpenOCD^1I was able to dump the flash and the RAM^2contents shortly after boot.

With the firmware dumped I could start analysing it with Ghidra^3. I very quickly found the main CAN message handler, which allowed me to further document the purpose of each CAN message.

Figure 3: Decompilation showing the handlers for messages 0x300 and 0x306

I also discovered that a total of three applications live on the controller MCU: A bootloader located at 0x8000000, an ‘updater’ at 0x8003000, and the main application at 0x8006200. The bootloader sets up the CAN bus and listens for a short time to see if any ‘update’ packets arrive, to see if a firmware update over the CAN bus is in progress. For some reason both the bootloader and ‘updater’ firmware contain a mechanism to update the application firmware over CAN bus, both use a different update scheme.

Figure 4:
 
Ghidra open on the ‘bootload’ function of the controller. This can be identified by it writing the address of the reset function (
image[1]
) to the start of RAM (
0x20000000
), setting the stack pointer (
image[0]
), and then jumping to the reset function. The reset function will handle setting up the NVIC.
Figure 5:
 
The application image. The first two words are the initial stack pointer address and the reset function, followed by the addresses of the interrupt handlers. Note how it’s quite repetitive, this makes it easy to identify.

Another funny note is that at 0x8006000 the length of the application firmware is stored, but not as a four or eight byte unsigned integer as you’d inspect, but instead as an ascii string of the base-10 representation of the number. Even wilder is that the entire region after the length up to 0x80061ff is padded with ascii space characters, and terminated with\r\n.

Figure 6:
 
The contents of memory just before the main application starts.

After exploring a small amount further, I decided to turn my attention to the display unit. The majority of the code in the controller appears to be the FOC motor control code, and I didn’t feel particularly comfortable modifying the safety critical part of the device, especially after discovering that the controller contains some fairly reasonable safety precautions, such as shutting down if the display stops sending valid throttle positions after a short period.

### Display unit

Cracking open the display unit required much more effort than the controller. It’s constructed from a reasonably tough and thick (2mm) injection molded body, so I used a dremel to cut into the back side. I had assumed the front screen cover was heat welded on, and so I also started using a dremel around the edge, but once I had cut a slot and had some leverage, I was able to simply pry the cover off as it was only glued.

Figure 7: Topside of the display unit, I’m using a 
Glasgow
 as the debugger

The board for the display was quite interesting as it had several unused through hole pin header rows and multiple microcontrollers. I identified the chips to be the following:

1. Main MCU: AT32F415
2. Bluetooth MCU: CH573
3. NFC reader IC: FM17520
4. CAN Transceiver
5. SPI flash chip: W25Q128FV

One debug header was the SWD port for the main MCU, so I repeated the process of dumping the firmware there. Another provided access to the SPI flash, so I also dumped this, but it only contained only the bitmap images used by the GUI shown on the display.

The display firmware is structure similarly to the control unit, with a bootloader which is capable of receiving firmware updates over the CAN bus.

1. The display unit firmware is structured as a bootloader and a main application at 0x8008000.
2. The GUI is drawn using SEGGER EMWin.
3. The bluetooth MCU communicates over GPIOA 2 and 3 using UART at 57500k, using a simple framing scheme. When a bluetooth attribute is read, the CH573 sends a request message with a number indicating a handler in the main MCU firmware. The main MCU sends back a response message with the same command number and the response body.
4. The NFC module also communicates over UART at 115200k, with a slightly different protocol. I didn’t look into this much further.
5. The button panel on the handlebars of the scooter communicates with the display unit also over UART, at 9600k. The only message it sends is a simple bitfield of the buttons that are pressed. Interestingly, it handles the blinking of the indicators itself; It blinks the lights and also has two bits in its message which indicates the blinker state. It appears to also be able to receive firmware updates.
6. The CAN bus is connected over pins GPIOA 11 and 12.
7. The display is a ST7796 controller, connected over a parallel interface; All 16 pins on GPIOB are used as a parallel data bus, which allows the firmware to update the state of all pins in just one instruction.
8. The ADC reads from three channels: An ambient light sensor on ch12, the throttle voltage on ch13, and the battery voltage on ch15. The firmware only reads the battery voltage to trigger an error message when it is too low, for all other usages of the battery level the firmware reads a variable updated by a CAN message sent by the battery. (Yeah, the battery is on the bus.)
9. The firmware of the display unit is, like the controller, updated over CAN. And again like the controller, the actual update code lives in the bootloader; The application firmware simply reboots itself if it sees an update initiation message, the bootloader then sees the next message and starts the update process. Yes, this also means that it’s possible to modify the firmware of any scooter without authentication :)))))

Initially the display firmware was a pain to reverse engineer, the version of Ghidra that I was using had a bug which caused it to not properly tag function pointers located in areas identified as data, due to the pointers having their lower bits set (indicating that the function uses THUMB instructions). Since the firmware is structured around tables of callbacks - for CAN, bluetooth, and GUI screens - I was unable to locate the callers of a lot of functions. By luck I at some point encountered the function which scans through the CAN handlers table and was able to ascertain the structure of the CAN handler table, and since every entry in the table specifies the ID to match on, and optionally an interval and a tx and/or rx callback, I was now able to quickly locate the corresponding code for each CAN message that I observed.

Figure 8: Ghidra with the function of the display unit which handles sending the 
0x300
 CAN message
Figure 9: A table of CAN handlers defined at 0x200001a0
Figure 10: The entry for CAN message 0x306, it has a transmit callback and a specified interval

Through extensive cross referencing of both the display and controller firmware, I was able to build up a mostly complete understanding of the CAN messages, the only messages I didn’t complete were some related to the apple find my feature, which I’m not particularly interested in because I don’t have an iphone and instead built my own tracker device using openhaystack, which has the extra benefit of not triggering any ‘tracker following’ messages as it rotates identity every 30 minutes :)

Next up was figuring out the GPIO and peripheral configurations, which I’d need to begin writing my own firmware. Thankfully this is actually pretty easy as the firmware is using themanufacturer provided peripheral libraryand also didn’t use any form of LTO when compiling, so the decompilation output for the compiled HAL provided functions very closely matches the source.

Figure 11: Decompilation result for the GPIO_Init function, which is pretty much identical to the 
source
Figure 12: Decompilation of the function initialising UART5, we can see which pins are statically configured as tx and rx by the contents of the 
GPIO_Pins
 field, and the configuration of the UART peripheral. The baud rate is passed as a parameter for some reason.

Using this technique of matching up decompiled library functions with source code, and using the name and type information obtained by doing so to discover peripheral configs, allowed me to fully map out all the GPIO pins and the configurations of all the peripherals..

Another thing that aided in my reverse engineering was that the firmware had left in a debug menu (it seems to be unreachable from the actual firmware, but the code is still there). The debug menu displays some button and headlight statuses, so I was instantly able to fill out a ‘button state’ enum.

Figure 13: Decompilation of the debug menu

At this point I had pretty much figured out enough information to begin writing my own firmware; The CAN messages required to operate the motor controller were fully mapped out, as were the GPIO pins and peripheral configurations, and I’d also reverse engineered the UART protocol of the bluetooth MCU. I’d even put together a block diagram of all the individual components of the scooter that communicate:

Running my own firmware on the cracked open display unit would be trivial, as I can just use a debug probe to flash it. But to get my firmware onto a usable display unit I’d need to reverse engineer the firmware update process.

### Firmware updates

Thankfully (for me) the firmware update process ended up being extremely simple, with no cryptography involved and the main lifecycle of a firmware update living entirely within one function in the bootloader.

A firmware update starts in a CAN message handler for ID 0x384. If the message isthen the firmware resets, and if the message isthen the scooter erases the flash regions used to store the VIN and scooter configuration.

Figure 14: Ghidra with the function of the display unit which handles CAN messages with ID 0x384
Figure 15: The core of the firmware update loop, after a chunk’s CRC is validated, the bootloader directly writes into flash.

The device performing the firmware update then continues to sendmessages until the bootloader starts up, sees an update initiation message, and replies with. The updater device then sends 64 byte chunks spread over 9 CAN 0x384 frames, where each frame has the following structure:

* Frame 0
* Frame 1..9
* Frame 9

The CRC isCRC-16-CCITTover thedata. The data of each chunk is padded with zeros to make 64 bytes before calculating the CRC.sequenceis an unsigned byte, starting at 0 and incrementing for each chunk transmitted, after 0xFF it wraps to 0.

The first chunk is not the first 64 bytes of the firmware, but instead the update file name (for example:AT_R2_JHZY_GT1_GE_FM_HW02_4.0.2) as a null terminated string, followed by the firmware length as a base-10 encoded, null terminated string. The bootloader replies to the first chunk four times with, and all subsequent chunks with one.

After the first chunk is sent, the updater device then sends the firmware image a chunk at a time. The scooter replies with onemessage after the last CAN message of a frame is sent and the CRC is validated. After the firmware has been transmitted, the updater sends, which triggers a reboot of the display unit. The update mechanism directly writes over the application image in flash, so a failed update will brick the display. However, the bootloader always checks for the presence ofpackets when powering up, allowing a firmware update to begin even if the application code isn’t functional.

In summary, the update process follows this sequence diagram (you can tell I’m having fun with typst here :)):

Figure 16: Sequence diagram of update process

To actually do the firmware update, I extended the CAN dumping firmware that I wrote earlier intothis, which simply flashes a firmware image embedded inside.

Great, I can now update the firmware on the device. To confirm this worked I tried it out with the firmware image I’d dumped from the cracked open device to begin with, and it worked first time.

### Rewrite it in rust

Now I could begin writing some firmware in Rust. There was a small problem though, the display unit MCU is the AT32F415, which is a STM clone, but it seems to not be a clone of a specific STM chip, but instead a mish-mash of STM32 peripherals, most appear to match up with the STM32F1, but the RTC seems to be from a STM32F3. This is annoying because it means I can’t just jumpstart to writing firmware usingEmbassy, instead I need to first build my own HAL^4.

Kossnikitahad already started on this using a fork of stm32-rs, so I was thankfully able to take this andstart adding supportfor the peripherals I needed. I must admit I mostly cheated here; for most of the peripherals I started by taking the implementation from Embassy, and then I, with both the datasheet of the stm32f1 and the at32f415 open, updated the peripheral code to match the register names used by the AT32. There’s very likely a better way here, such as adding the chip as an entry instm32-metapac, which is a subproject of Embassy which processes SVD files to create PAC^5crates, but I initially assumed the AT32 was more different than it is.

I started by bringing up each peripheral, the clocks and timers first, as a timer allows me to add anembassy-time-driverimplementation. Then the ADC, external GPIO interrupts, UART, CAN, and RTC peripherals. With the HAL drivers implemented I could then start writing code to drive the display, read the ADC inputs, and talk over the CAN and UART buses.

Bringing up the display was entirely straightforward, using themipidsicrate for the display driver, all I had to do myself was add aParallelInterfaceimplementation in the HAL that allows writing a u16 to all the GPIO pins in one operation:

rust
Copy code
Copy
Copied!
1
///
 A bus of gpio pins
2
///
3
///
 SHIFT: which range of pins are we operating on: 0 => 0..16, 8 => 8..16
4
///
 MASK: bitmask used to select which pins are members of this bus. The mask is unshifted.
5
pub
 
struct
 
Bus
<
const
 P: 
char
, 
const
 SHIFT: 
u8
, 
const
 MASK: 
u16
, MODE = DefaultMode> {
6
 _mode: PhantomData<MODE>,
7
}
8
9
impl
<
const
 P: 
char
, 
const
 SHIFT: 
u8
, 
const
 MASK: 
u16
, MODE> 
Bus
<P, SHIFT, MASK, MODE> {
10
 
fn
 
_set_state
(
&
mut
 self, state: 
u16
) {
11
 
unsafe
 {
12
 (
*
Gpio::<P>::ptr()).
odt
().
modify
(|r, w| {
13
 
//
 we only need to read the previous state if the mask doesn't
14
 
//
 cover everything.
15
 
let
 prev 
=
 
if
 
const
 { 
MASK
 
&
 
0xFFFF
 
!=
 
0xFFFF
 } {
16
 r.
bits
() 
&
 
!
(
MASK
 
as
 
u32
)
17
 } 
else
 {
18
 
0
19
 };
20
 
let
 new 
=
 ((state 
<
<
 
SHIFT
) 
&
 
MASK
) 
as
 
u32
;
21
 w.
bits
(prev 
|
 new)
22
 });
23
 }
24
 }
25
26
 
fn
 
_get_state
(
&
self) -> 
u16
 {
27
 
unsafe
 {
28
 
let
 unshifted 
=
 (
*
Gpio::<P>::ptr()).
odt
().
read
().
bits
() 
&
 
!
(
MASK
 
as
 
u32
);
29
 (unshifted 
>
>
 
SHIFT
) 
as
 
u16
30
 }
31
 }
32
}
33
34
impl
<
const
 P: 
char
, 
const
 SHIFT: 
u8
, 
const
 MASK: 
u16
> 
mipidsi
::
interface
::
OutputBus
35
 
for
 
Bus
<P, SHIFT, MASK, Output>
36
{
37
 
type
 
Word
 
=
 
u16
;
38
39
 
const
 
KIND
: mipidsi::interface::InterfaceKind 
=
 InterfaceKind::Parallel16Bit;
40
41
 
type
 
Error
 
=
 Infallible;
42
43
 
#
[
inline
(
always
)
]
44
 
fn
 
set_value
(
&
mut
 self, value: 
Self
::
Word) -> 
Result
<(), 
Self
::
Error> {
45
 
self
.
set_state
(value);
46
 
Ok
(())
47
 }
48
}
rust
Copy code
Copy
Copied!
1
///
 A bus of gpio pins
2
///
3
///
 SHIFT: which range of pins are we operating on: 0 => 0..16, 8 => 8..16
4
///
 MASK: bitmask used to select which pins are members of this bus. The mask is unshifted.
5
pub
 
struct
 Bus<
const
 P: 
char
, 
const
 SHIFT: 
u8
, 
const
 MASK: 
u16
, MODE = DefaultMode> {
6
 _mode: PhantomData<MODE>,
7
}
8
9
impl
<
const
 P: 
char
, 
const
 SHIFT: 
u8
, 
const
 MASK: 
u16
, MODE> Bus<P, SHIFT, MASK, MODE> {
10
 
fn
 
_set_state
(
&
mut
 
self
, 
state:
 
u16
)
 
{
11
 
unsafe
 
{
12
 
(
*
Gpio
::<
P
>::
ptr
()).
odt
().
modify
(|r,
 
w|
 
{
13
 
//
 we only need to read the previous state if the mask doesn't
14
 
//
 cover everything.
15
 
let
 prev 
=
 
if
 
const
 
{
 
MASK
 
&
 
0xFFFF
 
!=
 
0xFFFF
 
}
 
{
16
 r
.
bits
()
 
&
 
!
(
MASK
 
as
 
u32
)
17
 
}
 
else
 
{
18
 
0
19
 
};
20
 
let
 new 
=
 
((
state 
<
<
 
SHIFT
)
 
&
 
MASK
)
 
as
 
u32
;
21
 w
.
bits
(
prev 
|
 new
)
22
 
});
23
 
}
24
 
}
25
26
 
fn
 
_get_state
(
&
self)
 
->
 
u16
 
{
27
 
unsafe
 
{
28
 
let
 unshifted 
=
 
(
*
Gpio
::<
P
>::
ptr
()).
odt
().
read
().
bits
()
 
&
 
!
(
MASK
 
as
 
u32
);
29
 
(
unshifted 
>
>
 
SHIFT
)
 
as
 
u16
30
 
}
31
 
}
32
}
33
34
impl
<
const
 P: 
char
, 
const
 SHIFT: 
u8
, 
const
 MASK: 
u16
> mipidsi::interface::OutputBus
35
 for Bus<P, SHIFT, MASK, Output>
36
{
37
 
type
 
Word
 
=
 
u16
;
38
39
 
const
 KIND: mipidsi::interface::InterfaceKind 
=
 InterfaceKind::Parallel16Bit;
40
41
 
type
 
Error
 
=
 Infallible;
42
43
 #[inline(always)]
44
 
fn
 
set_value
(
&
mut
 
self
, 
value:
 
Self
::
Word
)
 
->
 
Result
<()
, 
Self
::
Error
>
 
{
45
 
self
.
set_state
(
value
);
46
 
Ok
(())
47
 
}
48
}

We can then declare the pins used in the display as rust types:

rust
Copy code
Copy
Copied!
1
pub
 
type
 
Bus
 
=
 at32f4xx_hal::gpio::Bus<'B', 0, 0xFFFF, Output>;
2
pub
 
type
 
CsPin
 
=
 Pin<'C', 13, Output>;
3
pub
 
type
 
DcPin
 
=
 Pin<'C', 14, Output>;
4
pub
 
type
 
RdPin
 
=
 Pin<'C', 0, Output>;
5
pub
 
type
 
WrPin
 
=
 Pin<'C', 15, Output>;
6
pub
 
type
 
RstPin
 
=
 Pin<'C', 1, Output>;
7
pub
 
type
 
Backlight
 
=
 PwmChannel<at32f4xx_hal::pac::TMR2, 0>;
8
pub
 
type
 
InnerDisplay
 
=
 mipidsi::Display<
9
 mipidsi::interface::ParallelInterface<Bus>,
10
 mipidsi::models::ST7796,
11
 RstPin,
12
>;
13
14
pub
 
fn
 
init
(
15
 
mut
 rd: RdPin,
16
 
mut
 cs: CsPin,
17
 dc: DcPin,
18
 wr: WrPin,
19
 rst: RstPin,
20
 bus: Bus,
21
 delay: 
&
mut
 SysDelay,
22
 backlight: Backlight,
23
) -> Display {
24
 cs.
set_low
();
25
 rd.
set_high
();
26
27
 
let
 interface 
=
 mipidsi::interface::ParallelInterface::new(bus, dc, wr);
28
 
let
 
mut
 display 
=
 mipidsi::Builder::new(mipidsi::models::
ST7796
, interface)
29
 .
reset_pin
(rst)
30
 .
invert_colors
(mipidsi::options::ColorInversion::Inverted)
31
 .
orientation
(mipidsi::options::Orientation {
32
 rotation: mipidsi::options::Rotation::Deg0,
33
 mirrored: 
true
,
34
 })
35
 .
color_order
(mipidsi::options::ColorOrder::Bgr)
36
 .
init
(delay)
37
 .
unwrap
();
38
39
 Display {
40
 _cs_pin: cs,
41
 _rd_pin: rd,
42
 inner: display,
43
 backlight,
44
 }
45
}
rust
Copy code
Copy
Copied!
1
pub
 
type
 
Bus
 
=
 at32f4xx_hal::gpio::Bus<'B', 0, 0xFFFF, Output>;
2
pub
 
type
 
CsPin
 
=
 Pin<'C', 13, Output>;
3
pub
 
type
 
DcPin
 
=
 Pin<'C', 14, Output>;
4
pub
 
type
 
RdPin
 
=
 Pin<'C', 0, Output>;
5
pub
 
type
 
WrPin
 
=
 Pin<'C', 15, Output>;
6
pub
 
type
 
RstPin
 
=
 Pin<'C', 1, Output>;
7
pub
 
type
 
Backlight
 
=
 PwmChannel<at32f4xx_hal::pac::TMR2, 0>;
8
pub
 
type
 
InnerDisplay
 
=
 mipidsi::Display<
9
 mipidsi::interface::ParallelInterface<Bus>,
10
 mipidsi::models::ST7796,
11
 RstPin,
12
>;
13
14
pub
 
fn
 
init
(
15
 
mut
 
rd:
 RdPin,
16
 
mut
 
cs:
 CsPin,
17
 
dc:
 DcPin,
18
 
wr:
 WrPin,
19
 
rst:
 RstPin,
20
 
bus:
 Bus,
21
 
delay:
 
&
mut
 SysDelay,
22
 
backlight:
 Backlight,
23
)
 
->
 Display
 
{
24
 cs
.
set_low
();
25
 rd
.
set_high
();
26
27
 
let
 interface 
=
 
mipidsi
::
interface
::
ParallelInterface
::
new
(
bus
,
 dc
,
 wr
);
28
 
let
 
mut
 display 
=
 
mipidsi
::
Builder
::
new
(
mipidsi
::
models
::
ST7796
,
 interface
)
29
 
.
reset_pin
(
rst
)
30
 
.
invert_colors
(
mipidsi
::
options
::
ColorInversion
::
Inverted
)
31
 
.
orientation
(
mipidsi
::
options
::
Orientation 
{
32
 rotation
:
 
mipidsi
::
options
::
Rotation
::
Deg0
,
33
 mirrored
:
 
true
,
34
 
})
35
 
.
color_order
(
mipidsi
::
options
::
ColorOrder
::
Bgr
)
36
 
.
init
(
delay
)
37
 
.
unwrap
();
38
39
 Display 
{
40
 _cs_pin
:
 cs
,
41
 _rd_pin
:
 rd
,
42
 inner
:
 display
,
43
 backlight
,
44
 
}
45
}

And now we have aDisplaywhich we can draw to. By opening up the compiled firmware in Ghidra we can also confirm that the data transmission loop turns into a simple loop which writes a sequence of bytes to a single MMIO register:

c
Copy code
Copy
Copied!
1
void
 __rustcall mipidsi:
:
interface:
:
parallel:
:
send_command
<
>
(ParallelInterface
<
>
 
*
self,u8 command,
&
[u8] args)
2
3
{
4
 byte 
*
pbVar1;
5
 u8 
*
puVar2;
6
7
 _DAT_40010c0c 
=
 command 
&
 
0x
ff
;
8
 _DAT_422202b8 
=
 
1
;
9
 _DAT_42220238 
=
 
1
;
10
 pbVar1 
=
 args.data_ptr;
11
 
for
 (puVar2 
=
 args.len; puVar2 
!=
 
0x
0
; puVar2 
=
 puVar2 
+
 
-
1
) {
12
 _DAT_40010c0c 
=
 
*
pbVar1;
13
 pbVar1 
=
 pbVar1 
+
 
1
;
14
 _DAT_422202bc 
=
 
1
;
15
 _DAT_4222023c 
=
 
1
;
16
 }
17
 
return
;
18
}
c
Copy code
Copy
Copied!
1
void
 __rustcall mipidsi:
:
interface:
:
parallel:
:
send_command
<
>
(ParallelInterface
<
>
 
*
self,u8 command,
&
[u8] args)
2
3
{
4
 byte 
*
pbVar1;
5
 u8 
*
puVar2;
6
7
 _DAT_40010c0c 
=
 command 
&
 0x
ff
;
8
 _DAT_422202b8 
=
 
1
;
9
 _DAT_42220238 
=
 
1
;
10
 pbVar1 
=
 args.
data_ptr
;
11
 
for
 (puVar2 
=
 args.
len
; puVar2 
!=
 0x
0
; puVar2 
=
 puVar2 
+
 
-
1
) {
12
 _DAT_40010c0c 
=
 
*
pbVar1;
13
 pbVar1 
=
 pbVar1 
+
 
1
;
14
 _DAT_422202bc 
=
 
1
;
15
 _DAT_4222023c 
=
 
1
;
16
 }
17
 
return
;
18
}

With the display working, I next worked on implementing encoding and decoding of the CAN and bluetooth protocols. For this I useddekuas it allows you to declare byte and bit level parsers for structs using a quite concise macro^6:

rust
Copy code
Copy
Copied!
1
///
 513
2
#
[
derive
(
deku::DekuRead
,
 deku::DekuSize
,
 defmt::Format
,
 Clone
,
 PartialEq
,
 Eq
)
]
3
#
[
cfg_attr
(
test
,
 
derive
(
deku::DekuWrite
,
 Debug
)
)
]
4
#
[
deku
(
bit_order 
=
 
"
lsb
"
,
 endian 
=
 
"
little
"
)
]
5
pub
 
struct
 
ControllerSpeed
 {
6
 
///
 In km/h * 100
7
 
#
[
deku
(
pad_bytes_after 
=
 
"
2
"
)
]
8
 
pub
 motor_speed: 
u16
,
9
10
 
#
[
deku
(
bits 
=
 1
)
]
11
 
pub
 walk_mode: 
bool
,
12
13
 
#
[
deku
(
bits 
=
 1
)
]
14
 
pub
 headlight_on: 
bool
,
15
16
 
#
[
deku
(
bits 
=
 1
,
 pad_bits_after 
=
 
"
5
"
)
]
17
 
pub
 brake_light_on: 
bool
,
18
}
19
20
#
[
test
]
21
fn
 
test_display_throttle
() {
22
 
let
 
mut
 buf 
=
 [
0
u8
; 
8
];
23
 
deser_roundtrip
(
&
mut
 buf, 
&
DisplayThrottle::new(
511
, 
false
, 
false
, 
0
));
24
 
assert_eq!
(buf, [
0xff
, 
0b1
, 
0x00
, 
0x00
, 
0x02
, 
0x00
, 
0x00
, 
0x00
]);
25
26
 
deser_roundtrip
(
&
mut
 buf, 
&
DisplayThrottle::new(
511
, 
true
, 
false
, 
0
));
27
 
assert_eq!
(buf, [
0xff
, 
0b011
, 
0x00
, 
0x00
, 
0x02
, 
0x00
, 
0x00
, 
0x00
]);
28
29
 
deser_roundtrip
(
&
mut
 buf, 
&
DisplayThrottle::new(
511
, 
true
, 
true
, 
2
));
30
 
assert_eq!
(buf, [
0xff
, 
0b111
, 
0x00
, 
0x02
, 
0x02
, 
0x00
, 
0x00
, 
0x00
]);
31
32
 
deser_roundtrip
(
&
mut
 buf, 
&
DisplayThrottle::new(
1
, 
false
, 
true
, 
2
));
33
 
assert_eq!
(buf, [
0x01
, 
0b100
, 
0x00
, 
0x02
, 
0x02
, 
0x00
, 
0x00
, 
0x00
]);
34
35
 
deser_roundtrip
(
&
mut
 buf, 
&
DisplayThrottle::new(
256
, 
false
, 
true
, 
2
));
36
 
assert_eq!
(buf, [
0x00
, 
0b101
, 
0x00
, 
0x02
, 
0x02
, 
0x00
, 
0x00
, 
0x00
]);
37
}
rust
Copy code
Copy
Copied!
1
///
 513
2
#[derive(deku::DekuRead, deku::DekuSize, defmt::Format, Clone, PartialEq, Eq)]
3
#[cfg_attr(test, derive(
deku::DekuWrite
,
 Debug
))]
4
#[deku(bit_order 
=
 
"
lsb
"
, endian 
=
 
"
little
"
)]
5
pub
 
struct
 ControllerSpeed {
6
 
///
 In km/h * 100
7
 #[deku(pad_bytes_after 
=
 
"
2
"
)]
8
 
pub
 motor_speed: 
u16
,
9
10
 #[deku(bits 
=
 1)]
11
 
pub
 walk_mode: 
bool
,
12
13
 #[deku(bits 
=
 1)]
14
 
pub
 headlight_on: 
bool
,
15
16
 #[deku(bits 
=
 1, pad_bits_after 
=
 
"
5
"
)]
17
 
pub
 brake_light_on: 
bool
,
18
}
19
20
#[test]
21
fn
 
test_display_throttle
()
 
{
22
 
let
 
mut
 buf 
=
 
[
0
u8
;
 
8
];
23
 
deser_roundtrip
(
&
mut
 buf
,
 
&
DisplayThrottle
::
new
(
511
,
 
false
,
 
false
,
 
0
));
24
 
assert_eq!
(
buf
,
 
[
0xff
,
 
0b1
,
 
0x00
,
 
0x00
,
 
0x02
,
 
0x00
,
 
0x00
,
 
0x00
]);
25
26
 
deser_roundtrip
(
&
mut
 buf
,
 
&
DisplayThrottle
::
new
(
511
,
 
true
,
 
false
,
 
0
));
27
 
assert_eq!
(
buf
,
 
[
0xff
,
 
0b011
,
 
0x00
,
 
0x00
,
 
0x02
,
 
0x00
,
 
0x00
,
 
0x00
]);
28
29
 
deser_roundtrip
(
&
mut
 buf
,
 
&
DisplayThrottle
::
new
(
511
,
 
true
,
 
true
,
 
2
));
30
 
assert_eq!
(
buf
,
 
[
0xff
,
 
0b111
,
 
0x00
,
 
0x02
,
 
0x02
,
 
0x00
,
 
0x00
,
 
0x00
]);
31
32
 
deser_roundtrip
(
&
mut
 buf
,
 
&
DisplayThrottle
::
new
(
1
,
 
false
,
 
true
,
 
2
));
33
 
assert_eq!
(
buf
,
 
[
0x01
,
 
0b100
,
 
0x00
,
 
0x02
,
 
0x02
,
 
0x00
,
 
0x00
,
 
0x00
]);
34
35
 
deser_roundtrip
(
&
mut
 buf
,
 
&
DisplayThrottle
::
new
(
256
,
 
false
,
 
true
,
 
2
));
36
 
assert_eq!
(
buf
,
 
[
0x00
,
 
0b101
,
 
0x00
,
 
0x02
,
 
0x02
,
 
0x00
,
 
0x00
,
 
0x00
]);
37
}

The neat thing about doing this in rust is that I could then take these definitions and use them in a completely different program to decode the CAN logs into something human readable:

Copy code
Copy
Copied!
1
L1 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
2
L2 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3094 })
3
L3 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
4
L4 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
5
L5 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3094 })
6
L6 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
7
L7 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
8
L8 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
9
L9 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
10
L10 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
11
L11 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48499, current_ma: 3075 })
12
L12 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
13
L13 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
14
L14 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
15
L15 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
16
L16 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
17
L17 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48499, current_ma: 3075 })
18
L18 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
19
L19 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
20
L20 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
21
L21 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
22
L22 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
23
L23 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48498, current_ma: 3055 })
24
L24 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
25
L25 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
26
L26 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
27
L27 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
28
L28 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
29
L29 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48498, current_ma: 3055 })
30
L30 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
31
L31 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
32
L32 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
33
L33 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
34
L34 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
35
L35 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3049 })
36
L36 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
37
L37 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
38
L38 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
39
L39 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
40
L40 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
41
L41 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3049 })
42
L42 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
43
L43 id=774 ext=false from=display DisplayThrottle(DisplayThrottle { throttle: 85, left_blinker: false, right_blinker: false, speed_limit: 0, magic: DekuConst })
44
L44 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
45
L45 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
46
L46 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
47
L47 id=768 ext=false from=display DisplaySpeedMode(DisplaySpeedMode { mode: 0, mode_high: 90, headlight: 100, magic: Normal, speed_mode_byte: 0, walk_counter: 0 })
48
L48 id=494 ext=false from=display unknown [60, 00, 00, 00, 00, 00, 00, 00]
49
L49 id=495 ext=false from=unknown unknown [4c, 44, 2e, 43, 52, 2e, 53, 38]
50
L50 id=495 ext=false from=unknown unknown [30, 37, 2e, 43, 2e, 32, 2e, 31]
51
L51 id=495 ext=false from=unknown unknown [45, 47, 2e, 32, 2e, 32, 2e, 31]
52
L52 id=495 ext=false from=unknown unknown [31, 00, 00, 00, 00, 00, 00, 00]
53
L53 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
54
L54 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
55
L55 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
56
L56 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
57
L57 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
58
L58 id=768 ext=false from=display DisplaySpeedMode(DisplaySpeedMode { mode: 0, mode_high: 90, headlight: 100, magic: Normal, speed_mode_byte: 0, walk_counter: 0 })
59
L59 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
60
L60 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
61
L61 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
62
L62 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
63
L63 id=1856 ext=true from=display unknown [4b, 00]
64
L64 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
65
L65 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3044 })
66
L66 id=1857 ext=true from=unknown unknown [4b, 00, 00, 00, 69, 99, 52, 42]
67
L67 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
68
L68 id=1860 ext=true from=display unknown [01]
69
L69 id=1861 ext=true from=battery unknown [01, 15, 57, 20, 50, 59, 54, 34]
70
L70 id=774 ext=false from=display DisplayThrottle(DisplayThrottle { throttle: 84, left_blinker: false, right_blinker: false, speed_limit: 0, magic: DekuConst })
71
L71 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: true, brake_light_on: false })
72
L72 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 8191 })
73
L73 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
74
L74 id=768 ext=false from=display DisplaySpeedMode(DisplaySpeedMode { mode: 0, mode_high: 90, headlight: 100, magic: Normal, speed_mode_byte: 0, walk_counter: 0 })
Copy code
Copy
Copied!
1
L1 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
2
L2 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3094 })
3
L3 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
4
L4 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
5
L5 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3094 })
6
L6 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
7
L7 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
8
L8 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
9
L9 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
10
L10 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
11
L11 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48499, current_ma: 3075 })
12
L12 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
13
L13 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
14
L14 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
15
L15 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
16
L16 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
17
L17 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48499, current_ma: 3075 })
18
L18 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
19
L19 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
20
L20 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
21
L21 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
22
L22 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
23
L23 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48498, current_ma: 3055 })
24
L24 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
25
L25 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
26
L26 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
27
L27 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
28
L28 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
29
L29 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48498, current_ma: 3055 })
30
L30 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
31
L31 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
32
L32 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
33
L33 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
34
L34 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
35
L35 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3049 })
36
L36 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
37
L37 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
38
L38 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
39
L39 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
40
L40 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
41
L41 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3049 })
42
L42 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
43
L43 id=774 ext=false from=display DisplayThrottle(DisplayThrottle { throttle: 85, left_blinker: false, right_blinker: false, speed_limit: 0, magic: DekuConst })
44
L44 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: false, brake_light_on: false })
45
L45 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 33 })
46
L46 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
47
L47 id=768 ext=false from=display DisplaySpeedMode(DisplaySpeedMode { mode: 0, mode_high: 90, headlight: 100, magic: Normal, speed_mode_byte: 0, walk_counter: 0 })
48
L48 id=494 ext=false from=display unknown [60, 00, 00, 00, 00, 00, 00, 00]
49
L49 id=495 ext=false from=unknown unknown [4c, 44, 2e, 43, 52, 2e, 53, 38]
50
L50 id=495 ext=false from=unknown unknown [30, 37, 2e, 43, 2e, 32, 2e, 31]
51
L51 id=495 ext=false from=unknown unknown [45, 47, 2e, 32, 2e, 32, 2e, 31]
52
L52 id=495 ext=false from=unknown unknown [31, 00, 00, 00, 00, 00, 00, 00]
53
L53 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
54
L54 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
55
L55 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
56
L56 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
57
L57 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
58
L58 id=768 ext=false from=display DisplaySpeedMode(DisplaySpeedMode { mode: 0, mode_high: 90, headlight: 100, magic: Normal, speed_mode_byte: 0, walk_counter: 0 })
59
L59 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
60
L60 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
61
L61 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
62
L62 id=495 ext=false from=unknown unknown [00, 00, 00, 00, 00, 00, 00, 00]
63
L63 id=1856 ext=true from=display unknown [4b, 00]
64
L64 id=1024 ext=false from=battery BatteryCommandState(BatteryCommandState { command: 16384, state: 1159, estimated_range: 0 })
65
L65 id=1025 ext=false from=battery BatteryVoltageCurrent(BatteryVoltageCurrent { voltage_mv: 48500, current_ma: 3044 })
66
L66 id=1857 ext=true from=unknown unknown [4b, 00, 00, 00, 69, 99, 52, 42]
67
L67 id=1028 ext=false from=battery BatteryCapacityTemp(BatteryCapacityTemp { capacity_mah: 20000, battery_charged: true, battery_charging: false, battery_temp: 270 })
68
L68 id=1860 ext=true from=display unknown [01]
69
L69 id=1861 ext=true from=battery unknown [01, 15, 57, 20, 50, 59, 54, 34]
70
L70 id=774 ext=false from=display DisplayThrottle(DisplayThrottle { throttle: 84, left_blinker: false, right_blinker: false, speed_limit: 0, magic: DekuConst })
71
L71 id=513 ext=false from=controller ControllerSpeed(ControllerSpeed { motor_speed: 0, walk_mode: false, headlight_on: true, brake_light_on: false })
72
L72 id=515 ext=false from=controller ControllerSpeedMode(ControllerSpeedMode { unknown: 8191 })
73
L73 id=528 ext=false from=controller ControllerSpeedLimit(ControllerSpeedLimit { speed_limit: false })
74
L74 id=768 ext=false from=display DisplaySpeedMode(DisplaySpeedMode { mode: 0, mode_high: 90, headlight: 100, magic: Normal, speed_mode_byte: 0, walk_counter: 0 })
Listing 2: The same CAN logs shown earlier, now decoded

### Actor-modelling

Now that the protocols are implemented, it becomes quite easy to write state machines using Embassy to handle incoming messages (both external messages from the CAN bus or bluetooth MCU, or internally defined messages for communicating button presses, events triggered by the UI, and ADC readings) and update relevant state. Overall, using the actor model for firmware is really quite a breeze, when all tasks communicate over well defined interfaces instead of reading and writing to shared global memory, reasoning about the system becomes simplified, and in my case, writing an emulator tool to test the GUI proved easy.

In the end, I ended up with this set of actors and relationships:

Figure 17: Diagram of tasks (Grey) and resources (Coloured). Arrows indicate direction of data flow.

#### The ADC Task

This task reads the ADC periodically, and publishes readings onto a channel that other tasks can subscribe to.

rust
Copy code
Copy
Copied!
1
pub
 
static
 
ADC_READINGS
: embassy_sync::pubsub::PubSubChannel<embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex, AdcReading, 4, 4, 1> 
=
 embassy_sync::pubsub::PubSubChannel::new();
2
3
pub
 
static
 
THROTTLE_READINGS
: embassy_sync::watch::Watch<embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex, Throttle, 4> 
=
 embassy_sync::watch::Watch::new();
4
5
pub
 
static
 
AMBIENT_READINGS
: embassy_sync::watch::Watch<embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex, AmbientLight, 4> 
=
 embassy_sync::watch::Watch::new();
6
7
async 
fn
 
adc_task_
(
8
 
mut
 adc: Adc<ADC1>,
9
 
//
 ambient light
10
 ch12: Pin<'C', 2, Analog>,
11
12
 
//
 throttle
13
 ch13: Pin<'C', 3, Analog>,
14
) {
15
 
let
 
mut
 do_sample_ticker 
=
 embassy_time::Ticker::every(Duration::from_millis(
50
));
16
17
 
let
 state_reading_ch 
=
 
ADC_READINGS
.
publisher
().
unwrap
();
18
 
let
 throttle_reading_ch 
=
 
THROTTLE_READINGS
.
sender
();
19
 
let
 ambient_reading_ch 
=
 
AMBIENT_READINGS
.
sender
();
20
21
 
//
 the ambient light level is averaged so that it doesn't flicker
22
 
let
 
mut
 ambient_light_averager 
=
 MovingAverage::<
u16
, 
u32
, 16>::new();
23
24
 
loop
 {
25
 
//
 sample the throttle and ambient light every 50ms
26
 do_sample_ticker.
next
().await;
27
28
 defmt::trace
!
(
"
ADC measuring ambient
"
);
29
 
let
 val 
=
 adc.
convert
(
&
ch12, SampleTime::Cycles_480).await;
30
 
let
 avg 
=
 ambient_light_averager.
average
(val);
31
 
let
 ambient_light 
=
 AmbientLight::from_raw(avg);
32
 state_reading_ch
33
 .
publish
(AdcReading::AmbientLight(ambient_light))
34
 .await;
35
 ambient_reading_ch.
send
(ambient_light);
36
37
 defmt::trace
!
(
"
ADC measuring throttle
"
);
38
 
let
 val 
=
 adc.
convert
(
&
ch13, SampleTime::Cycles_480).await;
39
 
let
 thr 
=
 Throttle::from_raw(val);
40
 state_reading_ch.
publish
(AdcReading::Throttle(thr)).await;
41
 throttle_reading_ch.
send
(thr);
42
 }
43
}
rust
Copy code
Copy
Copied!
1
pub
 
static
 ADC_READINGS: embassy_sync::pubsub::PubSubChannel<embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex, AdcReading, 4, 4, 1> 
=
 embassy_sync::pubsub::PubSubChannel::new();
2
3
pub
 
static
 THROTTLE_READINGS: embassy_sync::watch::Watch<embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex, Throttle, 4> 
=
 embassy_sync::watch::Watch::new();
4
5
pub
 
static
 AMBIENT_READINGS: embassy_sync::watch::Watch<embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex, AmbientLight, 4> 
=
 embassy_sync::watch::Watch::new();
6
7
async 
fn
 
adc_task_
(
8
 
mut
 
adc:
 
Adc
<
ADC1
>
,
9
 
//
 ambient light
10
 
ch12:
 
Pin
<
'C', 2, Analog
>
,
11
12
 
//
 throttle
13
 
ch13:
 
Pin
<
'C', 3, Analog
>
,
14
)
 
{
15
 
let
 
mut
 do_sample_ticker 
=
 
embassy_time
::
Ticker
::
every
(
Duration
::
from_millis
(
50
));
16
17
 
let
 state_reading_ch 
=
 
ADC_READINGS
.
publisher
().
unwrap
();
18
 
let
 throttle_reading_ch 
=
 
THROTTLE_READINGS
.
sender
();
19
 
let
 ambient_reading_ch 
=
 
AMBIENT_READINGS
.
sender
();
20
21
 
//
 the ambient light level is averaged so that it doesn't flicker
22
 
let
 
mut
 ambient_light_averager 
=
 
MovingAverage
::<
u16
, 
u32
, 16
>::
new
();
23
24
 
loop
 
{
25
 
//
 sample the throttle and ambient light every 50ms
26
 do_sample_ticker
.
next
().
await
;
27
28
 
defmt
::
trace
!
(
"
ADC measuring ambient
"
);
29
 
let
 val 
=
 adc
.
convert
(
&
ch12
,
 
SampleTime
::
Cycles_480
).
await
;
30
 
let
 avg 
=
 ambient_light_averager
.
average
(
val
);
31
 
let
 ambient_light 
=
 
AmbientLight
::
from_raw
(
avg
);
32
 state_reading_ch
33
 
.
publish
(
AdcReading
::
AmbientLight
(
ambient_light
))
34
 
.
await
;
35
 ambient_reading_ch
.
send
(
ambient_light
);
36
37
 
defmt
::
trace
!
(
"
ADC measuring throttle
"
);
38
 
let
 val 
=
 adc
.
convert
(
&
ch13
,
 
SampleTime
::
Cycles_480
).
await
;
39
 
let
 thr 
=
 
Throttle
::
from_raw
(
val
);
40
 state_reading_ch
.
publish
(
AdcReading
::
Throttle
(
thr
)).
await
;
41
 throttle_reading_ch
.
send
(
thr
);
42
 
}
43
}

To handle converting raw ADC readings to usable numbers, I use the following newtype pattern:

rust
Copy code
Copy
Copied!
1
#
[
derive
(
Eq
,
 PartialEq
,
 Default
,
 defmt::Format
,
 Clone
,
 Copy
,
 Debug
)
]
2
pub
 
struct
 
Throttle
(pub 
u16
);
3
4
impl
 
Throttle
 {
5
 
pub
 
const
 
INITIAL
: 
Self
 
=
 
Self
(
0
);
6
7
 
//
 value we report to the controller when throttle is fully depressed
8
 
const
 
OUT_MAX
: 
u32
 
=
 
360
;
9
10
 
fn
 
from_raw
(raw: 
u16
) -> 
Self
 {
11
 
//
 value the adc reads when throttle is fully depressed
12
 
const
 
MAX_RAW
: 
u32
 
=
 
2820
;
13
14
 
//
 value the adc reads when the throttle is unpressed
15
 
const
 
MIN_RAW
: 
u32
 
=
 
730
;
16
17
 
Self
(
18
 (raw 
as
 
u32
)
19
 .
clamp
(
MIN_RAW
, 
MAX_RAW
)
20
 .
saturating_sub
(
MIN_RAW
)
21
 .
saturating_mul
(
Self
::
OUT_MAX
)
22
 .
saturating_div
(
MAX_RAW
 
-
 
MIN_RAW
)
23
 .
saturating_truncate
(),
24
 )
25
 }
26
27
 
pub
(
crate
) 
fn
 
for_bluetooth
(
&
self) -> 
u8
 {
28
 
const
 
MAX_BT
: 
u32
 
=
 
146
;
29
30
 (
self
.
0
 
as
 
u32
)
31
 .
saturating_mul
(
MAX_BT
)
32
 .
saturating_div
(
Self
::
OUT_MAX
)
33
 .
saturating_truncate
()
34
 }
35
36
 
pub
 
fn
 
adjust_for_speed_limit
(
37
 
&
self,
38
 
//
 current speed limit setpoint (e.g. 271)
39
 speed_limit: 
u16
,
40
 
//
 speed limit set on the controller
41
 
//
 (250/350/450). for a speed_limit of 271
42
 
//
 this should be 350.
43
 controller_speed_limit: 
u16
,
44
 ) -> 
u16
 {
45
 
//
 This is just a linear scale for now. I need to find how the speed
46
 
//
 actually responds over throttle values.
47
 (
self
.
0
 
as
 
u32
)
48
 .
saturating_mul
(speed_limit 
as
 
u32
)
49
 .
saturating_div
(controller_speed_limit 
as
 
u32
)
50
 .
saturating_truncate
()
51
 }
52
}
rust
Copy code
Copy
Copied!
1
#[derive(Eq, PartialEq, Default, defmt::Format, Clone, Copy, Debug)]
2
pub
 
struct
 Throttle(pub 
u16
);
3
4
impl
 Throttle {
5
 
pub
 
const
 INITIAL: 
Self
 
=
 
Self
(
0
);
6
7
 
//
 value we report to the controller when throttle is fully depressed
8
 
const
 OUT_MAX: 
u32
 
=
 
360
;
9
10
 
fn
 
from_raw
(raw:
 
u16
)
 
->
 
Self
 
{
11
 
//
 value the adc reads when throttle is fully depressed
12
 
const
 
MAX_RAW
:
 
u32
 
=
 
2820
;
13
14
 
//
 value the adc reads when the throttle is unpressed
15
 
const
 
MIN_RAW
:
 
u32
 
=
 
730
;
16
17
 
Self
(
18
 
(
raw 
as
 
u32
)
19
 
.
clamp
(
MIN_RAW
,
 
MAX_RAW
)
20
 
.
saturating_sub
(
MIN_RAW
)
21
 
.
saturating_mul
(
Self
::
OUT_MAX
)
22
 
.
saturating_div
(
MAX_RAW
 
-
 
MIN_RAW
)
23
 
.
saturating_truncate
(),
24
 
)
25
 
}
26
27
 
pub
(
crate
) 
fn
 
for_bluetooth
(
&
self)
 
->
 
u8
 
{
28
 
const
 
MAX_BT
:
 
u32
 
=
 
146
;
29
30
 
(
self
.
0
 
as
 
u32
)
31
 
.
saturating_mul
(
MAX_BT
)
32
 
.
saturating_div
(
Self
::
OUT_MAX
)
33
 
.
saturating_truncate
()
34
 
}
35
36
 
pub
 
fn
 
adjust_for_speed_limit
(
37
 
&
self
,
38
 
//
 current speed limit setpoint (e.g. 271)
39
 
speed_limit:
 
u16
,
40
 
//
 speed limit set on the controller
41
 
//
 (250/350/450). for a speed_limit of 271
42
 
//
 this should be 350.
43
 
controller_speed_limit:
 
u16
,
44
 
)
 
->
 
u16
 
{
45
 
//
 This is just a linear scale for now. I need to find how the speed
46
 
//
 actually responds over throttle values.
47
 
(
self
.
0
 
as
 
u32
)
48
 
.
saturating_mul
(
speed_limit 
as
 
u32
)
49
 
.
saturating_div
(
controller_speed_limit 
as
 
u32
)
50
 
.
saturating_truncate
()
51
 
}
52
}

#### The ‘System state’ task

The system state (I’m bad at naming) task is used to maintain the read-only and calculated state of the system, that is: The battery level, current speed, temperature, and the odometer and predicted range.

rust
Copy code
Copy
Copied!
1
#
[
derive
(
PartialEq
,
 Eq
,
 defmt::Format
,
 Clone
)
]
2
pub
 
struct
 
SystemState
 {
3
 
///
 motor speed, in deca meters per hour (speed / 100 = km/h)
4
 
pub
 motor_speed: 
u16
,
5
 
pub
 headlight_on: 
bool
,
6
 
pub
 brake_light_on: 
bool
,
7
8
 
pub
 controller_temp: 
u8
,
9
 
pub
 system_voltage: SystemVoltage,
10
 
pub
 controller_speed_limit_mode: 
bool
,
11
12
 
pub
 battery_current: 
i16
,
13
 
pub
 battery_debug: BatteryDebug,
14
 
pub
 battery_info: BatteryInfo,
15
16
 
pub
 throttle: Throttle,
17
 
pub
 ambient_light: AmbientLight,
18
19
 
pub
 buttons: Buttons,
20
 
///
 in km
21
 
pub
 odometer: 
u16
,
22
23
 
///
 in km
24
 
pub
 predicted_range: 
u16
,
25
}
26
27
#
[
embassy_executor
::
task
]
28
async 
fn
 
system_state_updater
() {
29
 
let
 can_messages 
=
 
CAN_MESSAGES
.
receiver
();
30
 
let
 bt_commands 
=
 
BT_COMMANDS
.
receiver
();
31
 
let
 
mut
 adc_readings 
=
 
crate
::adc::
ADC_READINGS
.
subscriber
().
unwrap
();
32
 
let
 state_updated 
=
 
STATE_UPDATES
.
sender
();
33
 
let
 
mut
 buttons_reader 
=
 
BUTTON_STATE_WATCH
.
receiver
().
unwrap
();
34
35
 
let
 
mut
 update_private_state_ticker 
=
36
 Ticker::every(Duration::from_secs(
PRIVATE_STATE_UPDATE_PERIOD_SECS
));
37
38
 
let
 
mut
 private_state 
=
 PrivateState::default();
39
40
 
loop
 {
41
 
let
 updated 
=
 
match
 select::select5(
42
 can_messages.
receive
(),
43
 bt_commands.
receive
(),
44
 adc_readings.
next_message_pure
(),
45
 buttons_reader.
changed
(),
46
 update_private_state_ticker.
next
(),
47
 )
48
 .await
49
 {
50
 select::Either5::First(can_msg) 
=>
 {
51
 
update_state
(|s| s.
update_from_can_message
(
&
can_msg));
52
 private_state.
update_from_can_message
(
&
can_msg);
53
 
true
54
 }
55
 select::Either5::Second(
_
) 
=>
 
false
,
56
 select::Either5::Third(reading) 
=>
 {
57
 
update_state
(|s| s.
update_from_adc_reading
(reading))
58
 }
59
 select::Either5::Fourth(buttons) 
=>
 {
60
 
update_state
(|s| s.buttons 
=
 buttons);
61
 
true
62
 }
63
 select::Either5::Fifth(
_
) 
=>
 {
64
 private_state.
periodic_update
();
65
 
update_state
(|s| private_state.
update_public
(s));
66
 
true
67
 }
68
 };
69
70
 
if
 updated {
71
 state_updated.
send
(());
72
 }
73
 }
74
}
75
76
impl
 
SystemState
 {
77
 
pub
 
fn
 
update_from_can_message
(
&
mut
 self, msg: 
&
CanMessage) {
78
 
match
 msg {
79
 CanMessage::ControllerStatus(ControllerStatus { battery_level, 
..
 }) 
=>
 {
80
 
self
.battery_info.level_from_controller 
=
 
*
battery_level;
81
 }
82
 CanMessage::ControllerSpeed(ControllerSpeed {
83
 motor_speed,
84
 headlight_on,
85
 brake_light_on,
86
 
..
87
 }) 
=>
 {
88
 
self
.motor_speed 
=
 
*
motor_speed;
89
 
self
.headlight_on 
=
 
*
headlight_on;
90
 
self
.brake_light_on 
=
 
*
brake_light_on;
91
 }
92
 CanMessage::ControllerTempMotor(ControllerTempMotor { temp, voltage }) 
=>
 {
93
 
self
.controller_temp 
=
 
*
temp;
94
 
self
.system_voltage.from_controller 
=
 
*
voltage;
95
 }
96
 CanMessage::ControllerSpeedMode(ControllerSpeedMode { 
..
 }) 
=>
 {}
97
 CanMessage::ControllerSpeedLimit(ControllerSpeedLimit { speed_limit }) 
=>
 {
98
 
self
.controller_speed_limit_mode 
=
 
*
speed_limit;
99
 }
100
 CanMessage::BatteryCommandState(BatteryCommandState {
101
 command,
102
 state,
103
 estimated_range,
104
 }) 
=>
 {
105
 
self
.battery_debug 
=
 BatteryDebug {
106
 command: 
*
command,
107
 state: 
*
state,
108
 estimated_range: estimated_range.
truncate
(),
109
 }
110
 }
111
 CanMessage::BatteryVoltageCurrent(BatteryVoltageCurrent {
112
 voltage_mv,
113
 current_ma,
114
 }) 
=>
 {
115
 
self
.system_voltage.from_battery 
=
 voltage_mv.
truncate
();
116
 
self
.battery_current 
=
 current_ma.
truncate
();
117
 }
118
 CanMessage::BatteryChargeLevel(BatteryChargeLevel {
119
 relative_soc,
120
 absolute_soc_mah,
121
 }) 
=>
 {
122
 
self
.battery_info.relative_soc 
=
 relative_soc.
truncate
();
123
 
self
.battery_info.absolute_soc 
=
 absolute_soc_mah.
truncate
();
124
 }
125
 CanMessage::BatteryStateOfHealth(BatteryStateOfHealth {
126
 relative_soh,
127
 absolute_soh_mah,
128
 }) 
=>
 {
129
 
self
.battery_info.relative_soh 
=
 
*
relative_soh;
130
 
self
.battery_info.absolute_soh 
=
 absolute_soh_mah.
truncate
();
131
 }
132
 CanMessage::BatteryCapacityTemp(BatteryCapacityTemp {
133
 capacity_mah,
134
 battery_charged,
135
 battery_charging,
136
 battery_temp,
137
 }) 
=>
 {
138
 
self
.battery_info.capacity 
=
 
*
capacity_mah;
139
 
self
.battery_info.charged 
=
 
*
battery_charged;
140
 
self
.battery_info.charging 
=
 
*
battery_charging;
141
 
self
.battery_info.temperature 
=
 
*
battery_temp;
142
 }
143
 
_
 
=>
 {}
144
 }
145
 }
146
}
rust
Copy code
Copy
Copied!
1
#[derive(PartialEq, Eq, defmt::Format, Clone)]
2
pub
 
struct
 SystemState {
3
 
///
 motor speed, in deca meters per hour (speed / 100 = km/h)
4
 
pub
 motor_speed: 
u16
,
5
 
pub
 headlight_on: 
bool
,
6
 
pub
 brake_light_on: 
bool
,
7
8
 
pub
 controller_temp: 
u8
,
9
 
pub
 system_voltage: SystemVoltage,
10
 
pub
 controller_speed_limit_mode: 
bool
,
11
12
 
pub
 battery_current: 
i16
,
13
 
pub
 battery_debug: BatteryDebug,
14
 
pub
 battery_info: BatteryInfo,
15
16
 
pub
 throttle: Throttle,
17
 
pub
 ambient_light: AmbientLight,
18
19
 
pub
 buttons: Buttons,
20
 
///
 in km
21
 
pub
 odometer: 
u16
,
22
23
 
///
 in km
24
 
pub
 predicted_range: 
u16
,
25
}
26
27
#[embassy_executor::task]
28
async 
fn
 
system_state_updater
()
 
{
29
 
let
 can_messages 
=
 
CAN_MESSAGES
.
receiver
();
30
 
let
 bt_commands 
=
 
BT_COMMANDS
.
receiver
();
31
 
let
 
mut
 adc_readings 
=
 
crate
::
adc
::
ADC_READINGS
.
subscriber
().
unwrap
();
32
 
let
 state_updated 
=
 
STATE_UPDATES
.
sender
();
33
 
let
 
mut
 buttons_reader 
=
 
BUTTON_STATE_WATCH
.
receiver
().
unwrap
();
34
35
 
let
 
mut
 update_private_state_ticker 
=
36
 
Ticker
::
every
(
Duration
::
from_secs
(
PRIVATE_STATE_UPDATE_PERIOD_SECS
));
37
38
 
let
 
mut
 private_state 
=
 
PrivateState
::
default
();
39
40
 
loop
 
{
41
 
let
 updated 
=
 
match
 
select
::
select5
(
42
 can_messages
.
receive
(),
43
 bt_commands
.
receive
(),
44
 adc_readings
.
next_message_pure
(),
45
 buttons_reader
.
changed
(),
46
 update_private_state_ticker
.
next
(),
47
 
)
48
 
.
await
49
 
{
50
 
select
::
Either5
::
First
(
can_msg
)
 
=>
 
{
51
 
update_state
(|s|
 
s
.
update_from_can_message
(
&
can_msg
));
52
 private_state
.
update_from_can_message
(
&
can_msg
);
53
 
true
54
 
}
55
 
select
::
Either5
::
Second
(
_
)
 
=>
 
false
,
56
 
select
::
Either5
::
Third
(
reading
)
 
=>
 
{
57
 
update_state
(|s|
 
s
.
update_from_adc_reading
(
reading
))
58
 
}
59
 
select
::
Either5
::
Fourth
(
buttons
)
 
=>
 
{
60
 
update_state
(|s|
 
s
.
buttons 
=
 buttons
);
61
 
true
62
 
}
63
 
select
::
Either5
::
Fifth
(
_
)
 
=>
 
{
64
 private_state
.
periodic_update
();
65
 
update_state
(|s|
 
private_state
.
update_public
(
s
));
66
 
true
67
 
}
68
 
};
69
70
 
if
 updated 
{
71
 state_updated
.
send
(());
72
 
}
73
 
}
74
}
75
76
impl
 SystemState {
77
 
pub
 
fn
 
update_from_can_message
(
&
mut
 
self
, 
msg:
 
&
CanMessage
)
 
{
78
 
match
 msg 
{
79
 
CanMessage
::
ControllerStatus
(
ControllerStatus 
{
 battery_level
,
 
..
 
})
 
=>
 
{
80
 
self
.
battery_info
.
level_from_controller 
=
 
*
battery_level
;
81
 
}
82
 
CanMessage
::
ControllerSpeed
(
ControllerSpeed 
{
83
 motor_speed
,
84
 headlight_on
,
85
 brake_light_on
,
86
 
..
87
 
})
 
=>
 
{
88
 
self
.
motor_speed 
=
 
*
motor_speed
;
89
 
self
.
headlight_on 
=
 
*
headlight_on
;
90
 
self
.
brake_light_on 
=
 
*
brake_light_on
;
91
 
}
92
 
CanMessage
::
ControllerTempMotor
(
ControllerTempMotor 
{
 temp
,
 voltage 
})
 
=>
 
{
93
 
self
.
controller_temp 
=
 
*
temp
;
94
 
self
.
system_voltage
.
from_controller 
=
 
*
voltage
;
95
 
}
96
 
CanMessage
::
ControllerSpeedMode
(
ControllerSpeedMode 
{
 
..
 
})
 
=>
 
{}
97
 
CanMessage
::
ControllerSpeedLimit
(
ControllerSpeedLimit 
{
 speed_limit 
})
 
=>
 
{
98
 
self
.
controller_speed_limit_mode 
=
 
*
speed_limit
;
99
 
}
100
 
CanMessage
::
BatteryCommandState
(
BatteryCommandState 
{
101
 command
,
102
 state
,
103
 estimated_range
,
104
 
})
 
=>
 
{
105
 
self
.
battery_debug 
=
 BatteryDebug 
{
106
 command
:
 
*
command
,
107
 state
:
 
*
state
,
108
 estimated_range
:
 estimated_range
.
truncate
(),
109
 
}
110
 
}
111
 
CanMessage
::
BatteryVoltageCurrent
(
BatteryVoltageCurrent 
{
112
 voltage_mv
,
113
 current_ma
,
114
 
})
 
=>
 
{
115
 
self
.
system_voltage
.
from_battery 
=
 voltage_mv
.
truncate
();
116
 
self
.
battery_current 
=
 current_ma
.
truncate
();
117
 
}
118
 
CanMessage
::
BatteryChargeLevel
(
BatteryChargeLevel 
{
119
 relative_soc
,
120
 absolute_soc_mah
,
121
 
})
 
=>
 
{
122
 
self
.
battery_info
.
relative_soc 
=
 relative_soc
.
truncate
();
123
 
self
.
battery_info
.
absolute_soc 
=
 absolute_soc_mah
.
truncate
();
124
 
}
125
 
CanMessage
::
BatteryStateOfHealth
(
BatteryStateOfHealth 
{
126
 relative_soh
,
127
 absolute_soh_mah
,
128
 
})
 
=>
 
{
129
 
self
.
battery_info
.
relative_soh 
=
 
*
relative_soh
;
130
 
self
.
battery_info
.
absolute_soh 
=
 absolute_soh_mah
.
truncate
();
131
 
}
132
 
CanMessage
::
BatteryCapacityTemp
(
BatteryCapacityTemp 
{
133
 capacity_mah
,
134
 battery_charged
,
135
 battery_charging
,
136
 battery_temp
,
137
 
})
 
=>
 
{
138
 
self
.
battery_info
.
capacity 
=
 
*
capacity_mah
;
139
 
self
.
battery_info
.
charged 
=
 
*
battery_charged
;
140
 
self
.
battery_info
.
charging 
=
 
*
battery_charging
;
141
 
self
.
battery_info
.
temperature 
=
 
*
battery_temp
;
142
 
}
143
 
_
 
=>
 
{}
144
 
}
145
 
}
146
}

#### The ‘Operation state’ task

The main part of my scooter firmware is what I call the ‘operation state’, which is the driving state and all other state which is influenced by the driver. That is: whether the scooter is locked or unlocked, the speed mode the scooter is in, whether the headlight is on, off, or in auto mode, and the speed limit the scooter is configured to.

The state machine receives command such as ‘unlock’ and ‘set speed mode’ from the UI, and handles sending CAN messages to the controller depending on the current operation state and throttle position. The operation state itself is an enum with two states: Locked, and Unlocked. The main data of the operation state is only available within the unlocked state, which should prevent any chance of misbehaviour, such as being able to drive while the scooter is locked.

rust
Copy code
Copy
Copied!
1
#
[
derive
(
PartialEq
,
 Eq
,
 defmt::Format
,
 Clone
,
 Copy
)
]
2
pub
 
enum
 
OperationCommand
 {
3
 Unlock,
4
 Lock,
5
 UnlockSpeedLimit,
6
 LockSpeedLimit,
7
 SetSpeedLimit(
u16
),
8
 SetSpeedMode(SpeedMode),
9
 SetHeadlightMode(HeadlightMode),
10
}
11
12
#
[
derive
(
PartialEq
,
 Eq
,
 defmt::Format
,
 Clone
)
]
13
pub
 
enum
 
OperationState
 {
14
 Locked(
Option
<UnlockCode>),
15
 Active(ActiveState),
16
}
17
18
#
[
derive
(
PartialEq
,
 Eq
,
 defmt::Format
,
 Clone
)
]
19
pub
 
struct
 
ActiveState
 {
20
 
pub
 throttle: Throttle,
21
22
 
///
 Speed limit in km/h * 10, we'll later use this to select the 25/35/45 limit
23
 
///
 sent to the controller
24
 
pub
 speed_limit: 
u16
,
25
26
 
pub
 speed_limit_unlocked: 
bool
,
27
28
 
pub
 speed_mode: SpeedMode,
29
30
 
pub
 walk_mode_counter: 
Option
<NibbleCounter>,
31
32
 
pub
 headlight_mode: HeadlightMode,
33
 
pub
 headlight_config: HeadlightConfig,
34
}
35
36
#
[
embassy_executor
::
task
]
37
async 
fn
 
operation_task
() {
38
 defmt::info
!
(
"
Operation task startup
"
);
39
40
 
let
 
mut
 send_can_messages_ticker 
=
 embassy_time::Ticker::every(Duration::from_millis(
100
));
41
42
 
let
 
mut
 throttle_readings 
=
 
crate
::adc::
THROTTLE_READINGS
.
receiver
().
unwrap
();
43
 
let
 
mut
 ambient_readings 
=
 
crate
::adc::
AMBIENT_READINGS
.
receiver
().
unwrap
();
44
45
 
let
 operation_commands 
=
 
OPERATION_COMMANDS
.
receiver
();
46
47
 
let
 state_updates 
=
 
STATE_UPDATES
.
sender
();
48
49
 
let
 unlock_code 
=
 UnlockCode::get_stored().await;
50
 defmt::info
!
(
"
Loaded unlock code: {}
"
, unlock_code);
51
52
 
update_state
(|s| {
53
 
if
 s.
is_locked
() {
54
 
*
s 
=
 OperationState::Locked(
Some
(unlock_code));
55
 }
56
 });
57
58
 state_updates.
send
(());
59
60
 
loop
 {
61
 
match
 select::select4(
62
 send_can_messages_ticker.
next
(),
63
 throttle_readings
64
 .
changed
()
65
 .
with_timeout
(Duration::from_secs(
1
)),
66
 ambient_readings.
changed
(),
67
 operation_commands.
receive
(),
68
 )
69
 .await
70
 {
71
 select::Either4::First(
_
) 
=>
 {
72
 
send_speed_and_throttle_can_messages
().await;
73
 }
74
 select::Either4::Second(
Ok
(throttle)) 
=>
 {
75
 
update_state
(|s| s.
update_if_active
(|a| a.throttle 
=
 throttle));
76
77
 state_updates.
send
(());
78
 }
79
 select::Either4::Second(
Err
(
_
)) 
=>
 {
80
 
panic!
(
"
Operation task did not receive throttle update in time
"
);
81
 }
82
 select::Either4::Third(ambient) 
=>
 
update_state
(|s| {
83
 s.
update_if_active
(|a| {
84
 
if
 a.headlight_mode 
==
 HeadlightMode::Auto {
85
 
if
 
!
a.headlight_config.auto_on 
&&
 ambient.mapped 
<
 a.headlight_config.low {
86
 a.headlight_config.auto_on 
=
 
true
;
87
 state_updates.
send
(());
88
 } 
else
 
if
 a.headlight_config.auto_on
89
 
&&
 ambient.mapped 
>
 a.headlight_config.high
90
 {
91
 a.headlight_config.auto_on 
=
 
false
;
92
 state_updates.
send
(());
93
 }
94
 }
95
 })
96
 }),
97
 select::Either4::Fourth(op_cmd) 
=>
 {
98
 defmt::info
!
(
"
Handling op command: {}
"
, op_cmd);
99
 
match
 op_cmd {
100
 OperationCommand::Unlock 
=>
 {
101
 
let
 speed_limit 
=
 SpeedLimit::get_stored().await.
get_validated
();
102
 
let
 speed_mode 
=
 SpeedMode::get_stored().await;
103
 
let
 headlight_mode 
=
 HeadlightMode::get_stored().await;
104
105
 
update_state
(|s: 
&
mut
 OperationState| {
106
 
*
s 
=
 OperationState::Active(ActiveState {
107
 throttle: Throttle(
0
),
108
 speed_limit,
109
 speed_limit_unlocked: 
false
,
110
 walk_mode_counter: 
None
,
111
 speed_mode,
112
 headlight_mode,
113
 headlight_config: HeadlightConfig {
114
 low: 
5
,
115
 high: 
13
,
116
 auto_on: 
false
,
117
 },
118
 })
119
 })
120
 }
121
 OperationCommand::Lock 
=>
 {
122
 
let
 unlock_code 
=
 UnlockCode::get_stored().await;
123
 
update_state
(|s| 
*
s 
=
 OperationState::Locked(
Some
(unlock_code)))
124
 }
125
 OperationCommand::SetSpeedLimit(new_limit) 
=>
 {
126
 
let
 validated 
=
 SpeedLimit::new_validated(new_limit);
127
 SpeedLimit::update_stored(validated);
128
 
update_state
(|s| {
129
 s.
update_if_active
(|a| a.speed_limit 
=
 validated.
get_validated
())
130
 })
131
 }
132
 OperationCommand::SetSpeedMode(speed_mode) 
=>
 {
133
 SpeedMode::update_stored(speed_mode);
134
 
update_state
(|s| s.
update_if_active
(|a| a.speed_mode 
=
 speed_mode))
135
 }
136
 OperationCommand::SetHeadlightMode(headlight_mode) 
=>
 {
137
 HeadlightMode::update_stored(headlight_mode);
138
 
update_state
(|s| {
139
 s.
update_if_active
(|a| {
140
 a.headlight_mode 
=
 headlight_mode;
141
 })
142
 })
143
 }
144
 OperationCommand::UnlockSpeedLimit 
=>
 
update_state
(|s| {
145
 s.
update_if_active
(|a| {
146
 a.speed_limit_unlocked 
=
 
true
;
147
 })
148
 }),
149
 OperationCommand::LockSpeedLimit 
=>
 
update_state
(|s| {
150
 s.
update_if_active
(|a| {
151
 a.speed_limit_unlocked 
=
 
false
;
152
 })
153
 }),
154
 }
155
156
 state_updates.
send
(());
157
 }
158
 }
159
 }
160
}
161
rust
Copy code
Copy
Copied!
1
#[derive(PartialEq, Eq, defmt::Format, Clone, Copy)]
2
pub
 
enum
 OperationCommand {
3
 Unlock,
4
 Lock,
5
 UnlockSpeedLimit,
6
 LockSpeedLimit,
7
 SetSpeedLimit(
u16
),
8
 SetSpeedMode(SpeedMode),
9
 SetHeadlightMode(HeadlightMode),
10
}
11
12
#[derive(PartialEq, Eq, defmt::Format, Clone)]
13
pub
 
enum
 OperationState {
14
 Locked(
Option
<UnlockCode>),
15
 Active(ActiveState),
16
}
17
18
#[derive(PartialEq, Eq, defmt::Format, Clone)]
19
pub
 
struct
 ActiveState {
20
 
pub
 throttle: Throttle,
21
22
 
///
 Speed limit in km/h * 10, we'll later use this to select the 25/35/45 limit
23
 
///
 sent to the controller
24
 
pub
 speed_limit: 
u16
,
25
26
 
pub
 speed_limit_unlocked: 
bool
,
27
28
 
pub
 speed_mode: SpeedMode,
29
30
 
pub
 walk_mode_counter: 
Option
<NibbleCounter>,
31
32
 
pub
 headlight_mode: HeadlightMode,
33
 
pub
 headlight_config: HeadlightConfig,
34
}
35
36
#[embassy_executor::task]
37
async 
fn
 
operation_task
()
 
{
38
 
defmt
::
info
!
(
"
Operation task startup
"
);
39
40
 
let
 
mut
 send_can_messages_ticker 
=
 
embassy_time
::
Ticker
::
every
(
Duration
::
from_millis
(
100
));
41
42
 
let
 
mut
 throttle_readings 
=
 
crate
::
adc
::
THROTTLE_READINGS
.
receiver
().
unwrap
();
43
 
let
 
mut
 ambient_readings 
=
 
crate
::
adc
::
AMBIENT_READINGS
.
receiver
().
unwrap
();
44
45
 
let
 operation_commands 
=
 
OPERATION_COMMANDS
.
receiver
();
46
47
 
let
 state_updates 
=
 
STATE_UPDATES
.
sender
();
48
49
 
let
 unlock_code 
=
 
UnlockCode
::
get_stored
().
await
;
50
 
defmt
::
info
!
(
"
Loaded unlock code: {}
"
,
 unlock_code
);
51
52
 
update_state
(|s|
 
{
53
 
if
 s
.
is_locked
()
 
{
54
 
*
s 
=
 
OperationState
::
Locked
(
Some
(
unlock_code
));
55
 
}
56
 
});
57
58
 state_updates
.
send
(());
59
60
 
loop
 
{
61
 
match
 
select
::
select4
(
62
 send_can_messages_ticker
.
next
(),
63
 throttle_readings
64
 
.
changed
()
65
 
.
with_timeout
(
Duration
::
from_secs
(
1
)),
66
 ambient_readings
.
changed
(),
67
 operation_commands
.
receive
(),
68
 
)
69
 
.
await
70
 
{
71
 
select
::
Either4
::
First
(
_
)
 
=>
 
{
72
 
send_speed_and_throttle_can_messages
().
await
;
73
 
}
74
 
select
::
Either4
::
Second
(
Ok
(
throttle
))
 
=>
 
{
75
 
update_state
(|s|
 
s
.
update_if_active
(|a|
 
a
.
throttle 
=
 throttle
));
76
77
 state_updates
.
send
(());
78
 
}
79
 
select
::
Either4
::
Second
(
Err
(
_
))
 
=>
 
{
80
 
panic!
(
"
Operation task did not receive throttle update in time
"
);
81
 
}
82
 
select
::
Either4
::
Third
(
ambient
)
 
=>
 
update_state
(|s|
 
{
83
 s
.
update_if_active
(|a|
 
{
84
 
if
 a
.
headlight_mode 
==
 
HeadlightMode
::
Auto 
{
85
 
if
 
!
a
.
headlight_config
.
auto_on 
&&
 ambient
.
mapped 
<
 a
.
headlight_config
.
low 
{
86
 a
.
headlight_config
.
auto_on 
=
 
true
;
87
 state_updates
.
send
(());
88
 
}
 
else
 
if
 a
.
headlight_config
.
auto_on
89
 
&&
 ambient
.
mapped 
>
 a
.
headlight_config
.
high
90
 
{
91
 a
.
headlight_config
.
auto_on 
=
 
false
;
92
 state_updates
.
send
(());
93
 
}
94
 
}
95
 
})
96
 
}),
97
 
select
::
Either4
::
Fourth
(
op_cmd
)
 
=>
 
{
98
 
defmt
::
info
!
(
"
Handling op command: {}
"
,
 op_cmd
);
99
 
match
 op_cmd 
{
100
 
OperationCommand
::
Unlock 
=>
 
{
101
 
let
 speed_limit 
=
 
SpeedLimit
::
get_stored
().
await
.
get_validated
();
102
 
let
 speed_mode 
=
 
SpeedMode
::
get_stored
().
await
;
103
 
let
 headlight_mode 
=
 
HeadlightMode
::
get_stored
().
await
;
104
105
 
update_state
(|s:
 
&
mut
 OperationState
|
 
{
106
 
*
s 
=
 
OperationState
::
Active
(
ActiveState 
{
107
 throttle
:
 Throttle
(
0
),
108
 speed_limit
,
109
 speed_limit_unlocked
:
 
false
,
110
 walk_mode_counter
:
 
None
,
111
 speed_mode
,
112
 headlight_mode
,
113
 headlight_config
:
 HeadlightConfig 
{
114
 low
:
 
5
,
115
 high
:
 
13
,
116
 auto_on
:
 
false
,
117
 
},
118
 
})
119
 
})
120
 
}
121
 
OperationCommand
::
Lock 
=>
 
{
122
 
let
 unlock_code 
=
 
UnlockCode
::
get_stored
().
await
;
123
 
update_state
(|s|
 
*
s 
=
 
OperationState
::
Locked
(
Some
(
unlock_code
)))
124
 
}
125
 
OperationCommand
::
SetSpeedLimit
(
new_limit
)
 
=>
 
{
126
 
let
 validated 
=
 
SpeedLimit
::
new_validated
(
new_limit
);
127
 
SpeedLimit
::
update_stored
(
validated
);
128
 
update_state
(|s|
 
{
129
 s
.
update_if_active
(|a|
 
a
.
speed_limit 
=
 validated
.
get_validated
())
130
 
})
131
 
}
132
 
OperationCommand
::
SetSpeedMode
(
speed_mode
)
 
=>
 
{
133
 
SpeedMode
::
update_stored
(
speed_mode
);
134
 
update_state
(|s|
 
s
.
update_if_active
(|a|
 
a
.
speed_mode 
=
 speed_mode
))
135
 
}
136
 
OperationCommand
::
SetHeadlightMode
(
headlight_mode
)
 
=>
 
{
137
 
HeadlightMode
::
update_stored
(
headlight_mode
);
138
 
update_state
(|s|
 
{
139
 s
.
update_if_active
(|a|
 
{
140
 a
.
headlight_mode 
=
 headlight_mode
;
141
 
})
142
 
})
143
 
}
144
 
OperationCommand
::
UnlockSpeedLimit 
=>
 
update_state
(|s|
 
{
145
 s
.
update_if_active
(|a|
 
{
146
 a
.
speed_limit_unlocked 
=
 
true
;
147
 
})
148
 
}),
149
 
OperationCommand
::
LockSpeedLimit 
=>
 
update_state
(|s|
 
{
150
 s
.
update_if_active
(|a|
 
{
151
 a
.
speed_limit_unlocked 
=
 
false
;
152
 
})
153
 
}),
154
 
}
155
156
 state_updates
.
send
(());
157
 
}
158
 
}
159
 
}
160
}
161

#### GUI Task

The GUI task handles running the UI, all ‘actions’ in the UI are translated into messages that are sent to the operation state task. The GUI task also runs from a lower priority executor, which allows the other tasks to run in parallel such that long processing times in the GUI thread don’t prevent important tasks from operating.

#### Bluetooth,CAN, andButtontasks

The bluetooth, CAN, and button are simple message forwarders that translate between structured messages and the wire format. There isn’t much to talk about here, they use the encoders and decoders I spoke about inListing 1.

#### Config store task

To be able to remember things like the odometer, last used driving mode, unlock pin, and speed limit, we need a way to persist these values to flash storage. To do this, I use thesequential-storagecrate, which provides a key-value interface on top of flash storage. It’s designed so that writes are wear levelled (by spreading writes over multiple sectors), and to be reliable.

Config entries are declared using a macro, and can be any rust type implementing the required traits:

rust
Copy code
Copy
Copied!
1
#
[
derive
(
defmt::Format
,
 PartialEq
,
 Eq
,
 Copy
,
 Clone
,
 derive_enum_rotate::EnumRotate
,
 Default
,
 serde::Serialize
,
 serde::Deserialize
)
]
2
#
[
rustfmt
::
skip
]
3
pub
 
enum
 
HeadlightMode
 {
4
 
#
[
default
]
5
 Auto,
6
 On,
7
 Off,
8
}
9
10
saved_item!
(
2
, 
HEADLIGHT_MODE
, HeadlightMode, 
10
);
11
12
pub
(
crate
) 
trait
 
Storable
:
13
 Default + PartialEq + Clone + for<'a> sequential_storage::map::Value<'a> + 'static
14
{
15
 
const
 
ID
: 
u8
;
16
17
 
fn
 
take_if_changed_and_timedout
() -> 
Option
<
Self
>;
18
 
fn
 
mark_unchanged
();
19
 
fn
 
update_stored
(val: 
Self
);
20
 async 
fn
 
get_stored
() -> 
Self
;
21
 
fn
 
maybe_get_stored
() -> 
Option
<
Self
>;
22
}
23
24
macro_rules!
 
saved_item
 {
25
 ($id:
expr
, $name:
ident
, $ty:
ty
, $timeout:literal) 
=>
 {
26
 
static
 $name: embassy_sync::blocking_mutex::Mutex<
27
 embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex,
28
 
Option
<($ty, 
bool
, Instant)>,
29
 > 
=
 embassy_sync::blocking_mutex::Mutex::new(
None
);
30
31
 
impl
<
'a
> ::sequential_storage::map::PostcardValue<
'a
> 
for
 $ty {}
32
33
 paste::paste
!
 {
34
 
static
 [
<
WAKER_
 $name
>
]: embassy_sync::waitqueue::AtomicWaker 
=
 embassy_sync::waitqueue::AtomicWaker::new();
35
36
 
impl
 Storable 
for
 $ty {
37
 
const
 
ID
: 
u8
 
=
 $id;
38
39
 
fn
 
take_if_changed_and_timedout
() -> 
Option
<
Self
> {
40
 
let
 now 
=
 Instant::now();
41
 
unsafe
 {
42
 $name.
lock_mut
(|s| {
43
 
let
 (x, v, t) 
=
 s.
as_mut
()
?
;
44
45
 
if
 
*
v 
&&
 (now 
>
 
*
t) {
46
 
*
v 
=
 
false
;
47
 
return
 
Some
(x.
clone
());
48
 }
49
50
 
None
51
 })
52
 }
53
 }
54
55
 
fn
 
mark_unchanged
() {
56
 
unsafe
 {
57
 $name.
lock_mut
(|s| {
58
 
if
 
let
 
Some
((
_
, v, 
_
)) 
=
 s.
as_mut
() {
59
 
*
v 
=
 
false
;
60
 };
61
 })
62
 }
63
 }
64
65
 
fn
 
update_stored
(val: 
Self
) {
66
 
let
 now 
=
 Instant::now();
67
 
let
 t 
=
 now.
saturating_add
(Duration::from_secs($timeout));
68
 
unsafe
 {
69
 $name.
lock_mut
(|s| {
70
 
if
 
let
 
Some
((prev, prev_changed, 
prev_t
)) 
=
 s.
as_mut
() {
71
 
if
 
&
val 
!=
 prev {
72
 
*
prev_changed 
=
 
true
;
73
 
*
prev 
=
 val;
74
 
*
prev_t
 
=
 
if
 
*
prev_t
 
<
 now { t } 
else
 { 
*
prev_t
 };
75
 }
76
 } 
else
 {
77
 
*
s 
=
 
Some
((val, 
true
, t));
78
 }
79
 })
80
 }
81
 [
<
WAKER_
 $name
>
].
wake
();
82
 }
83
84
 async 
fn
 
get_stored
() -> 
Self
 {
85
 core::future::poll_fn(|cx| {
86
 
if
 
let
 
Some
((v, 
_
, 
_
)) 
=
 $name.
lock
(|s| s.
clone
()) {
87
 core::task::Poll::Ready(v)
88
 } 
else
 {
89
 [
<
WAKER_
 $name
>
].
register
(cx.
waker
());
90
 core::task::Poll::Pending
91
 }
92
 })
93
 .await
94
 }
95
96
 
fn
 
maybe_get_stored
() -> 
Option
<
Self
> {
97
 
if
 
let
 
Some
((v, 
_
, 
_
)) 
=
 $name.
lock
(|s| s.
clone
()) {
98
 
Some
(v)
99
 } 
else
 {
100
 
None
101
 }
102
 }
103
 }
104
 }
105
 };
106
}
rust
Copy code
Copy
Copied!
1
#[derive(defmt::Format, PartialEq, Eq, Copy, Clone, derive_enum_rotate::EnumRotate, Default, serde::Serialize, serde::Deserialize)]
2
#[rustfmt::skip]
3
pub
 
enum
 HeadlightMode {
4
 #[default]
5
 Auto,
6
 On,
7
 Off,
8
}
9
10
saved_item!(
2
, HEADLIGHT_MODE, HeadlightMode, 
10
);
11
12
pub
(
crate
) 
trait
 Storable:
13
 Default + PartialEq + Clone + for<'a> sequential_storage::map::Value<'a> + 'static
14
{
15
 
const
 ID: 
u8
;
16
17
 
fn
 
take_if_changed_and_timedout
()
 
->
 
Option
<
Self
>;
18
 
fn
 
mark_unchanged
();
19
 
fn
 
update_stored
(val:
 
Self
);
20
 async 
fn
 
get_stored
()
 
->
 
Self
;
21
 
fn
 
maybe_get_stored
()
 
->
 
Option
<
Self
>;
22
}
23
24
macro_rules!
 saved_item {
25
 ($id:
expr
, $name:
ident
, $ty:
ty
, $timeout:literal) 
=>
 {
26
 
static
 $name: embassy_sync::blocking_mutex::Mutex<
27
 embassy_sync::blocking_mutex::raw::CriticalSectionRawMutex,
28
 
Option
<($ty, 
bool
, Instant)>,
29
 > 
=
 embassy_sync::blocking_mutex::Mutex::new(
None
);
30
31
 
impl
<
'a
> ::sequential_storage::map::PostcardValue<
'a
> 
for
 $ty {}
32
33
 paste::paste
!
 {
34
 
static
 [
<
WAKER_ $name
>
]: embassy_sync::waitqueue::AtomicWaker 
=
 embassy_sync::waitqueue::AtomicWaker::new();
35
36
 
impl
 Storable 
for
 $ty {
37
 
const
 ID: 
u8
 
=
 $id;
38
39
 
fn
 
take_if_changed_and_timedout
()
 
->
 
Option
<
Self
>
 
{
40
 
let
 now 
=
 
Instant
::
now
();
41
 
unsafe
 
{
42
 
$name.
lock_mut
(|s|
 
{
43
 
let
 
(
x
,
 v
,
 t
)
 
=
 s
.
as_mut
()
?
;
44
45
 
if
 
*
v 
&&
 
(
now 
>
 
*
t
)
 
{
46
 
*
v 
=
 
false
;
47
 
return
 
Some
(
x
.
clone
());
48
 
}
49
50
 
None
51
 
})
52
 
}
53
 
}
54
55
 
fn
 
mark_unchanged
()
 
{
56
 
unsafe
 
{
57
 
$name.
lock_mut
(|s|
 
{
58
 
if
 
let
 
Some
((
_
,
 v
,
 
_
))
 
=
 s
.
as_mut
()
 
{
59
 
*
v 
=
 
false
;
60
 
};
61
 
})
62
 
}
63
 
}
64
65
 
fn
 
update_stored
(val:
 
Self
)
 
{
66
 
let
 now 
=
 
Instant
::
now
();
67
 
let
 t 
=
 now
.
saturating_add
(
Duration
::
from_secs
($timeout));
68
 
unsafe
 
{
69
 
$name.
lock_mut
(|s|
 
{
70
 
if
 
let
 
Some
((
prev
,
 prev_changed
,
 
prev_t
))
 
=
 s
.
as_mut
()
 
{
71
 
if
 
&
val 
!=
 prev 
{
72
 
*
prev_changed 
=
 
true
;
73
 
*
prev 
=
 val
;
74
 
*
prev_t
 
=
 
if
 
*
prev_t
 
<
 now 
{
 t 
}
 
else
 
{
 
*
prev_t
 
};
75
 
}
76
 
}
 
else
 
{
77
 
*
s 
=
 
Some
((
val
,
 
true
,
 t
));
78
 
}
79
 
})
80
 
}
81
 
[
<
WAKER_
 
$name
>
].
wake
();
82
 
}
83
84
 async 
fn
 
get_stored
()
 
->
 
Self
 
{
85
 
core
::
future
::
poll_fn
(|cx|
 
{
86
 
if
 
let
 
Some
((
v
,
 
_
,
 
_
))
 
=
 
$name.
lock
(|s|
 
s
.
clone
())
 
{
87
 
core
::
task
::
Poll
::
Ready
(
v
)
88
 
}
 
else
 
{
89
 
[
<
WAKER_
 
$name
>
].
register
(
cx
.
waker
());
90
 
core
::
task
::
Poll
::
Pending
91
 
}
92
 
})
93
 
.
await
94
 
}
95
96
 
fn
 
maybe_get_stored
()
 
->
 
Option
<
Self
>
 
{
97
 
if
 
let
 
Some
((
v
,
 
_
,
 
_
))
 
=
 
$name.
lock
(|s|
 
s
.
clone
())
 
{
98
 
Some
(
v
)
99
 
}
 
else
 
{
100
 
None
101
 
}
102
 
}
103
 }
104
 }
105
 };
106
}

Throughout the codebase, these config values can be read and updated at will:

rust
Copy code
Copy
Copied!
1
//
 read the config entry, this is an async so that this code can
2
//
 wait for the entry to be loaded from flash at startup
3
let
 foo 
=
 HeadlightMode::get_stored().await;
4
5
//
 set value
6
HeadlightMode::update_stored(HeadlightMode::Auto);
rust
Copy code
Copy
Copied!
1
//
 read the config entry, this is an async so that this code can
2
//
 wait for the entry to be loaded from flash at startup
3
let
 foo 
=
 HeadlightMode::get_stored().await;
4
5
//
 set value
6
HeadlightMode::update_stored(HeadlightMode::Auto);

The config store worker is the task that handles loading and persisting these config values to storage.

rust
Copy code
Copy
Copied!
1
pub
 async 
fn
 
worker_
(flash: at32f4xx_hal::pac::FLASH) {
2
 defmt::debug
!
(
3
 
"
FLASH INFO: start: {:x}, end: {:x}, len: {:x}
"
,
4
 
config_start
(),
5
 
config_end
(),
6
 
config_end
() 
-
 
config_start
()
7
 );
8
9
 
let
 
mut
 buffer 
=
 [
0
u8
; 
32
];
10
11
 
let
 
mut
 map_storage 
=
 MapStorage::<
u8
, 
_
, 
_
>::new(
12
 MyFlash(flash),
13
 MapConfig::new(
0
..
8192
),
14
 Cache::new_uncached(),
15
 );
16
17
 init_stored::<SpeedLimit, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
18
 init_stored::<HeadlightMode, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
19
 init_stored::<SpeedMode, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
20
 init_stored::<UnlockCode, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
21
 init_stored::<Odometer, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
22
23
 
loop
 {
24
 Timer::after_secs(
10
).await;
25
26
 write_stored_if_changed::<SpeedLimit, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
27
 write_stored_if_changed::<HeadlightMode, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
28
 write_stored_if_changed::<SpeedMode, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
29
 write_stored_if_changed::<UnlockCode, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
30
 write_stored_if_changed::<Odometer, 
_
, 
_
>(
&
mut
 map_storage, 
&
mut
 buffer);
31
 }
32
}
33
34
fn
 
init_stored
<T: Storable, S: NorFlash, C: CacheImpl<
u8
>>(
35
 map_storage: 
&
mut
 MapStorage<
u8
, S, C>,
36
 buf: 
&
mut
 [
u8
],
37
) {
38
 
match
 embassy_futures::block_on(map_storage.fetch_item::<T>(buf, 
&
T::
ID
)) {
39
 
Ok
(
Some
(v)) 
=>
 {
40
 T::update_stored(v);
41
 
let
 
_
 
=
 T::take_if_changed_and_timedout();
42
 }
43
 r 
=>
 {
44
 
if
 r.
is_err
() {
45
 defmt::warn
!
(
"
Failed to fetch entry for id {}, loading default
"
, T::
ID
);
46
 } 
else
 {
47
 defmt::debug
!
(
"
No stored entry found for id {}, loading default
"
, T::
ID
);
48
 }
49
 T::update_stored(T::default());
50
 T::mark_unchanged();
51
 }
52
 }
53
}
54
55
fn
 
write_stored_if_changed
<T: Storable, S: NorFlash, C: CacheImpl<
u8
>>(
56
 map_storage: 
&
mut
 MapStorage<
u8
, S, C>,
57
 buf: 
&
mut
 [
u8
],
58
) {
59
 
if
 
let
 
Some
(v) 
=
 T::take_if_changed_and_timedout() {
60
 
if
 embassy_futures::block_on(map_storage.
store_item
(buf, 
&
T::
ID
, 
&
v)).
is_ok
() {
61
 defmt::debug
!
(
"
Updated entry for id {}
"
, T::
ID
);
62
 } 
else
 {
63
 defmt::warn
!
(
"
Failed to write changed item for id {}
"
, T::
ID
);
64
 }
65
 }
66
}
rust
Copy code
Copy
Copied!
1
pub
 async 
fn
 
worker_
(flash:
 
at32f4xx_hal
::
pac
::
FLASH
)
 
{
2
 
defmt
::
debug
!
(
3
 
"
FLASH INFO: start: {:x}, end: {:x}, len: {:x}
"
,
4
 
config_start
(),
5
 
config_end
(),
6
 
config_end
()
 
-
 
config_start
()
7
 
);
8
9
 
let
 
mut
 buffer 
=
 
[
0
u8
;
 
32
];
10
11
 
let
 
mut
 map_storage 
=
 
MapStorage
::<
u8
, 
_
, 
_
>::
new
(
12
 MyFlash
(
flash
),
13
 
MapConfig
::
new
(
0
..
8192
),
14
 
Cache
::
new_uncached
(),
15
 
);
16
17
 
init_stored
::<
SpeedLimit, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
18
 
init_stored
::<
HeadlightMode, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
19
 
init_stored
::<
SpeedMode, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
20
 
init_stored
::<
UnlockCode, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
21
 
init_stored
::<
Odometer, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
22
23
 
loop
 
{
24
 
Timer
::
after_secs
(
10
).
await
;
25
26
 
write_stored_if_changed
::<
SpeedLimit, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
27
 
write_stored_if_changed
::<
HeadlightMode, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
28
 
write_stored_if_changed
::<
SpeedMode, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
29
 
write_stored_if_changed
::<
UnlockCode, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
30
 
write_stored_if_changed
::<
Odometer, 
_
, 
_
>(
&
mut
 map_storage
,
 
&
mut
 buffer
);
31
 
}
32
}
33
34
fn
 
init_stored
<T: Storable, S: NorFlash, C: CacheImpl<
u8
>>(
35
 
map_storage:
 
&
mut
 
MapStorage
<
u8
, S, C
>
,
36
 
buf:
 
&
mut
 [
u8
],
37
)
 
{
38
 
match
 
embassy_futures
::
block_on
(
map_storage
.
fetch_item
::<
T
>(
buf
,
 
&
T
::
ID
))
 
{
39
 
Ok
(
Some
(
v
))
 
=>
 
{
40
 
T
::
update_stored
(
v
);
41
 
let
 
_
 
=
 
T
::
take_if_changed_and_timedout
();
42
 
}
43
 r 
=>
 
{
44
 
if
 r
.
is_err
()
 
{
45
 
defmt
::
warn
!
(
"
Failed to fetch entry for id {}, loading default
"
,
 
T
::
ID
);
46
 
}
 
else
 
{
47
 
defmt
::
debug
!
(
"
No stored entry found for id {}, loading default
"
,
 
T
::
ID
);
48
 
}
49
 
T
::
update_stored
(
T
::
default
());
50
 
T
::
mark_unchanged
();
51
 
}
52
 
}
53
}
54
55
fn
 
write_stored_if_changed
<T: Storable, S: NorFlash, C: CacheImpl<
u8
>>(
56
 
map_storage:
 
&
mut
 
MapStorage
<
u8
, S, C
>
,
57
 
buf:
 
&
mut
 [
u8
],
58
)
 
{
59
 
if
 
let
 
Some
(
v
)
 
=
 
T
::
take_if_changed_and_timedout
()
 
{
60
 
if
 
embassy_futures
::
block_on
(
map_storage
.
store_item
(
buf
,
 
&
T
::
ID
,
 
&
v
)).
is_ok
()
 
{
61
 
defmt
::
debug
!
(
"
Updated entry for id {}
"
,
 
T
::
ID
);
62
 
}
 
else
 
{
63
 
defmt
::
warn
!
(
"
Failed to write changed item for id {}
"
,
 
T
::
ID
);
64
 
}
65
 
}
66
}
Listing 3: The config store worker handles writing changed entries. It implements a cooldown system so that frequent changes don’t thrash

### I want the GUI to be pretty too, not just the code

Now for the part of the firmware that I think is actually most novel, the HUD interface. For C projects there are lots of libraries here, including LVGL, SEGGER EmWIN. In Rust we have lots of GUI libraries too (egui, slint, gpui) and some of these are even targeted at embedded systems, but unfortunately all of them either require STD, an allocator, or a framebuffer, all of which I can’t support on a microcontroller with 32k of RAM.

By chance I came acrossBuoyant, which is a rust library providing a SwiftUI-like interface for constructing GUIs, while also requiring no framebuffer, memory allocations or the standard library. It also comes with focus/keyboard navigation support, which is exactly what I need as the scooter has no touchscreen.

I really like the API offered by buoyant, I really didn’t have to fight much to put together a UI that looks quite pretty. For example, here’s the entire code for the pin entry screen:

rust
Copy code
Copy
Copied!
1
#
[
derive
(
PartialEq
,
 Eq
,
 Clone
,
 Copy
,
 defmt::Format
,
 Default
)
]
2
pub
 
struct
 
State
 {
3
 pin: [pin_digit::PinDigit; 4],
4
}
5
6
#
[
must_use
]
7
pub
 
fn
 
view
(state: 
&
state::State) -> impl View<ColorFormat, state::State> 
+
 
use
<
>
 {
8
 VStack::new((
9
 Text::new(
"
Enter PIN
"
, 
&
font::
B612_REGULAR
).
foreground_color
(colour::on_background()),
10
 Lens::new(
pin_entry
(
&
state.locked_state), |s: 
&
mut
 state::State| {
11
 
&
mut
 s.locked_state
12
 }),
13
 Button::new(
14
 |state: 
&
mut
 state::State| {
15
 
if
 state.locked_state.pin
16
 
==
 state
17
 .operation_state
18
 .
as_locked
()
19
 .
and_then
(|x| 
*
x)
20
 .
unwrap_or_default
()
21
 .digits
22
 {
23
 state.locked_state.pin 
=
 
Default
::default();
24
 
let
 
_
 
=
 state.next_operation_commands.
push
(OperationCommand::Unlock);
25
 }
26
 },
27
 |bs| {
28
 Text::new(
"
Confirm
"
, 
&
font::
B612_REGULAR
)
29
 .
padding
(Edges::All, 
4
)
30
 .
foreground_color
(
if
 bs.
is_focused
() {
31
 colour::on_primary()
32
 } 
else
 {
33
 colour::on_primary_fixed()
34
 })
35
 .
background_color
(
36
 
if
 bs.
is_focused
() {
37
 colour::primary()
38
 } 
else
 {
39
 colour::primary_fixed()
40
 },
41
 RoundedRectangle::new(
4
),
42
 )
43
 },
44
 ),
45
 ))
46
 .
with_spacing
(
2
)
47
 .
with_alignment
(HorizontalAlignment::Center)
48
 .
flex_infinite_width
(HorizontalAlignment::Center)
49
 .
with_infinite_max_height
()
50
 .
map_event
(|event, _: 
&
mut
 ()| 
match
 event {
51
 Event::KeyDown(key) 
=>
 
match
 
*
key {
52
 keys::
UP_CLICK
 
=>
 
Some
(FocusAction::Previous.
into_event
(focus::
GROUP_0
)),
53
 keys::
DOWN_CLICK
 
=>
 
Some
(FocusAction::Next.
into_event
(focus::
GROUP_0
)),
54
 keys::
CONFIRM_CLICK
 
=>
 
Some
(FocusAction::Select.
into_event
(focus::
GROUP_0
)),
55
 
_
 
=>
 
None
,
56
 },
57
 Event::KeyUp(
_
) 
=>
 
None
,
58
 
_
 
=>
 
Some
(event.
clone
()),
59
 })
60
}
61
62
fn
 
pin_entry
(state: 
&
State) -> impl View<ColorFormat, State> 
+
 
use
<
>
 {
63
 HStack::new((
64
 Lens::new(
pin_piece
(state.pin[
0
]), |s: 
&
mut
 State| 
&
mut
 s.pin[
0
]),
65
 Lens::new(
pin_piece
(state.pin[
1
]), |s: 
&
mut
 State| 
&
mut
 s.pin[
1
]),
66
 Lens::new(
pin_piece
(state.pin[
2
]), |s: 
&
mut
 State| 
&
mut
 s.pin[
2
]),
67
 Lens::new(
pin_piece
(state.pin[
3
]), |s: 
&
mut
 State| 
&
mut
 s.pin[
3
]),
68
 ))
69
}
70
71
fn
 
pin_piece
(pin: pin_digit::PinDigit) -> impl View<ColorFormat, pin_digit::PinDigit> {
72
 Rotary::new(
73
 |pin: 
&
mut
 pin_digit::PinDigit, event: RotaryEvent| 
match
 event {
74
 RotaryEvent::Next 
=>
 
*
pin 
=
 pin.
prev
(),
75
 RotaryEvent::Previous 
=>
 
*
pin 
=
 pin.
next
(),
76
 RotaryEvent::Select 
|
 RotaryEvent::Exit 
=>
 {}
77
 },
78
 
move
 
|
rotary_state
|
 {
79
 Text::new(pin.
as_str
(), 
&
font::
B612_REGULAR_LARGE_NUMBERS
)
80
 .
padding
(Edges::All, 
4
)
81
 .
foreground_color
(
82
 
match
 rotary_state {
83
 RotaryState::UnFocused 
=>
 colour::on_background(),
84
 RotaryState::Focused 
=>
 colour::on_background(),
85
 RotaryState::Captive 
=>
 colour::on_primary_fixed(),
86
 }
87
 )
88
 .
background
(Alignment::Center,
89
 
match_view!
(rotary_state, {
90
 RotaryState::UnFocused 
=>
 EmptyView,
91
 RotaryState::Focused 
=>
 RoundedRectangle::new(
4
).
stroked
(
2
).
foreground_color
(colour::primary()),
92
 RotaryState::Captive 
=>
 RoundedRectangle::new(
4
).
stroked
(
2
).
foreground_color
(colour::primary_fixed())
93
 })
94
 )
95
 .
content_shape
(Rectangle.
corner_radius
(
4
))
96
 },
97
 )
98
}
rust
Copy code
Copy
Copied!
1
#[derive(PartialEq, Eq, Clone, Copy, defmt::Format, Default)]
2
pub
 
struct
 State {
3
 pin: [pin_digit::PinDigit; 4],
4
}
5
6
#[must_use]
7
pub
 
fn
 
view
(state:
 
&
state
::
State
)
 
->
 impl 
View
<
ColorFormat, 
state
::
State
>
 
+
 
use
<
>
 {
8
 VStack::new((
9
 Text::new(
"
Enter PIN
"
, 
&
font::B612_REGULAR).
foreground_color
(colour::on_background()),
10
 Lens::new(
pin_entry
(
&
state.locked_state), |s:
 
&
mut
 
state
::
State
|
 
{
11
 
&
mut
 s
.
locked_state
12
 
}),
13
 Button::new(
14
 |state:
 
&
mut
 
state
::
State
|
 
{
15
 
if
 state
.
locked_state
.
pin
16
 
==
 state
17
 
.
operation_state
18
 
.
as_locked
()
19
 
.
and_then
(|x|
 
*
x
)
20
 
.
unwrap_or_default
()
21
 
.
digits
22
 
{
23
 state
.
locked_state
.
pin 
=
 
Default
::
default
();
24
 
let
 
_
 
=
 state
.
next_operation_commands
.
push
(
OperationCommand
::
Unlock
);
25
 
}
26
 
},
27
 |bs|
 
{
28
 
Text
::
new
(
"
Confirm
"
,
 
&
font
::
B612_REGULAR
)
29
 
.
padding
(
Edges
::
All
,
 
4
)
30
 
.
foreground_color
(
if
 bs
.
is_focused
()
 
{
31
 
colour
::
on_primary
()
32
 
}
 
else
 
{
33
 
colour
::
on_primary_fixed
()
34
 
})
35
 
.
background_color
(
36
 
if
 bs
.
is_focused
()
 
{
37
 
colour
::
primary
()
38
 
}
 
else
 
{
39
 
colour
::
primary_fixed
()
40
 
},
41
 
RoundedRectangle
::
new
(
4
),
42
 
)
43
 
},
44
 ),
45
 ))
46
 .
with_spacing
(
2
)
47
 .
with_alignment
(HorizontalAlignment::Center)
48
 .
flex_infinite_width
(HorizontalAlignment::Center)
49
 .
with_infinite_max_height
()
50
 .
map_event
(|event,
 _: 
&
mut
 
()|
 
match
 event 
{
51
 
Event
::
KeyDown
(
key
)
 
=>
 
match
 
*
key 
{
52
 
keys
::
UP_CLICK
 
=>
 
Some
(
FocusAction
::
Previous
.
into_event
(
focus
::
GROUP_0
)),
53
 
keys
::
DOWN_CLICK
 
=>
 
Some
(
FocusAction
::
Next
.
into_event
(
focus
::
GROUP_0
)),
54
 
keys
::
CONFIRM_CLICK
 
=>
 
Some
(
FocusAction
::
Select
.
into_event
(
focus
::
GROUP_0
)),
55
 
_
 
=>
 
None
,
56
 
},
57
 
Event
::
KeyUp
(
_
)
 
=>
 
None
,
58
 
_
 
=>
 
Some
(
event
.
clone
()),
59
 
})
60
}
61
62
fn
 
pin_entry
(state:
 
&
State
)
 
->
 impl 
View
<
ColorFormat, State
>
 
+
 
use
<
>
 {
63
 HStack::new((
64
 Lens::new(
pin_piece
(state.pin[
0
]), |s:
 
&
mut
 State
|
 
&
mut
 s
.
pin
[
0
]),
65
 Lens::new(
pin_piece
(state.pin[
1
]), |s:
 
&
mut
 State
|
 
&
mut
 s
.
pin
[
1
]),
66
 Lens::new(
pin_piece
(state.pin[
2
]), |s:
 
&
mut
 State
|
 
&
mut
 s
.
pin
[
2
]),
67
 Lens::new(
pin_piece
(state.pin[
3
]), |s:
 
&
mut
 State
|
 
&
mut
 s
.
pin
[
3
]),
68
 ))
69
}
70
71
fn
 
pin_piece
(pin:
 
pin_digit
::
PinDigit
)
 
->
 impl 
View
<
ColorFormat, 
pin_digit
::
PinDigit
>
 
{
72
 
Rotary
::
new
(
73
 
|pin:
 
&
mut
 
pin_digit
::
PinDigit
,
 
event:
 RotaryEvent
|
 
match
 event 
{
74
 
RotaryEvent
::
Next 
=>
 
*
pin 
=
 pin
.
prev
(),
75
 
RotaryEvent
::
Previous 
=>
 
*
pin 
=
 pin
.
next
(),
76
 
RotaryEvent
::
Select 
|
 
RotaryEvent
::
Exit 
=>
 
{}
77
 
},
78
 
move
 
|
rotary_state
|
 
{
79
 
Text
::
new
(
pin
.
as_str
(),
 
&
font
::
B612_REGULAR_LARGE_NUMBERS
)
80
 
.
padding
(
Edges
::
All
,
 
4
)
81
 
.
foreground_color
(
82
 
match
 rotary_state 
{
83
 
RotaryState
::
UnFocused 
=>
 
colour
::
on_background
(),
84
 
RotaryState
::
Focused 
=>
 
colour
::
on_background
(),
85
 
RotaryState
::
Captive 
=>
 
colour
::
on_primary_fixed
(),
86
 
}
87
 
)
88
 
.
background
(
Alignment
::
Center
,
89
 
match_view!
(
rotary_state
,
 
{
90
 
RotaryState
::
UnFocused 
=>
 EmptyView
,
91
 
RotaryState
::
Focused 
=>
 
RoundedRectangle
::
new
(
4
).
stroked
(
2
).
foreground_color
(
colour
::
primary
()),
92
 
RotaryState
::
Captive 
=>
 
RoundedRectangle
::
new
(
4
).
stroked
(
2
).
foreground_color
(
colour
::
primary_fixed
())
93
 
})
94
 
)
95
 
.
content_shape
(
Rectangle
.
corner_radius
(
4
))
96
 
},
97
 
)
98
}
Figure 18: What the above code renders to
Figure 19: The homescreen view

The flexbox layout made building the homescreen also very easy, I know it’s quite overkill for static content on a fixed size screen, but it saves me having to position elements manually.

There was only one problem with Buoyant: the MCU has only 32k of RAM, which is nowhere near enough for a framebuffer. This means when Buoyant draws a frame it has to draw every single component to the display; the pixels with text on in the above homescreen view would be drawn three times: First the background, then the box, and finally the text. Since we don’t have a framebuffer we also need to send many more repositioning commands to the display. The end result is that the display flickers so much that it is unusable. The solution is to only redraw the components that change, and thankfully rust made updating Buoyant to support this relatively pain free.

A naïve solution to tracking what needs to redraw is to keep track of a bounding rectangle, which starts empty and, when a component is marked dirty, is expanded to surround its previous self and the rectangle containing the dirty component. But this isn’t good if you have two components at opposite ends of the screen that both update on the same frame. My solution to this is to instead insert the bounding boxes of dirtied components into a quadtree^7, which allows the areas that need to be redrawn (and therefore the components that need to redraw) to be tracked more precisely. My solution goes a step further and tracks two quadtrees: one tracks dirty regions and one tracks ‘overdrawn’ regions. A component is marked as changed if a property changes, or its bounding box overlaps with either tree before checking its children, or if its bounding box overlaps with the dirty tree after checking its children. When a component changes, its prior bounding box is added to the dirty tree, and its new bounding box is added to the ‘overdrawn’ tree. When a rectangle is added to the overdrawn tree, any rectangles contained within are removed from the dirty tree. If a node redraws but doesn’t change its bounding box, then any elements behind it don’t need to also redraw, but we do want its children to redraw.

Your browser does not support the video tag

Figure 20: The display partially updating, when the seconds counter updates, it doesn’t force the entire screen to flash.

There’s only one large downside to Buoyant: While it puts in quite some effort to minimise its use of generics, eachStacknode is still parameterised by the types of all the child nodes, which means the fully expanded types start to look like this:

rust
Copy code
Copy
Copied!
1
<
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::match_view::OneOf4<buoyant::view::modifier::map_event::MapEvent<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
2
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
3
buoyant::view::capturing::Lens<buoyant::view::hstack::HStack<(buoyant::view::capturing::Lens<buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
4
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
5
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
6
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
7
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
8
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
9
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
10
scooter_display::ui::view::locked::pin_piece::{closure#1}, scooter_display::ui::view::locked::pin_piece::{closure#0}>,
11
scooter_display::ui::view::locked::pin_entry::{closure#0}>,
12
buoyant::view::capturing::Lens<buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
13
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
14
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
15
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
16
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
17
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
18
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
19
scooter_display::ui::view::locked::pin_piece::{closure#1}, scooter_display::ui::view::locked::pin_piece::{closure#0}>,
20
scooter_display::ui::view::locked::pin_entry::{closure#1}>,
21
buoyant::view::capturing::Lens<buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
22
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
23
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
24
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
25
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
26
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
27
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
28
scooter_display::ui::view::locked::pin_piece::{closure#1}, scooter_display::ui::view::locked::pin_piece::{closure#0}>,
29
scooter_display::ui::view::locked::pin_entry::{closure#2}>,
30
buoyant::view::capturing::Lens<buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
31
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
32
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
33
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
34
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
35
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
36
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
37
scooter_display::ui::view::locked::pin_piece::{closure#1}, scooter_display::ui::view::locked::pin_piece::{closure#0}>,
38
scooter_display::ui::view::locked::pin_entry::{closure#3}>)>, scooter_display::ui::view::locked::view::{closure#0}>,
39
buoyant::view::button::Button<scooter_display::ui::view::locked::view::{closure#2},
40
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
41
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
42
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
43
scooter_display::ui::view::locked::view::{closure#1}>)>>, scooter_display::ui::view::locked::view::{closure#3}, ()>,
44
buoyant::view::modifier::captures_event::CapturesEvent<buoyant::view::vstack::VStack<(buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::hstack::HStack<(buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
45
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>,
46
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>>,
47
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
48
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
49
buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::foreach::ForEachView<3: 
usize
,
50
scooter_display::ui::view::home::TimePieceToShow,
51
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
52
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
3
: 
usize
]>>, glyphr::font::Font>,
53
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>, scooter_display::ui::view::home::header::{closure#3},
54
buoyant::view::foreach::Horizontal>>)>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
55
buoyant::view::shape::rectangle::Rectangle>,
56
buoyant::view::modifier::erase_captures::EraseCaptures<buoyant::view::vstack::VStack<(buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::hstack::HStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
57
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
3
: 
usize
]>>, glyphr::font::Font>,
58
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
59
buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
60
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
2
: 
usize
]>>, glyphr::font::Font>,
61
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
62
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
63
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>)>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
64
buoyant::view::shape::rectangle::Rectangle>>,
65
buoyant::view::modifier::padding::Padding<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::hstack::HStack<(buoyant::view::vstack::VStack<(buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::fixed_frame::FixedFrame<buoyant::view::modifier::padding::Padding<buoyant::view::hstack::HStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
66
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
67
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
68
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
69
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
70
buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
71
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::fixed_frame::FixedFrame<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
72
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
73
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
74
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
75
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
76
buoyant::view::shape::rounded_rectangle::RoundedRectangle>)>,
77
buoyant::view::vstack::VStack<(buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::fixed_frame::FixedFrame<buoyant::view::modifier::padding::Padding<buoyant::view::hstack::HStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
78
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
79
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
80
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
81
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
82
buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
83
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::fixed_frame::FixedFrame<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
84
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
85
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
86
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
87
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
88
buoyant::view::shape::rounded_rectangle::RoundedRectangle>)>)>>>)>>)>,
89
scooter_display::ui::view::home::view::{closure
#
0
}
>
,
90
buoyant::view::modifier::captures_event::CapturesEvent<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::popover::Popover<buoyant::view::scroll_view::ScrollView<buoyant::view::foreach::ForEachView<3:
91
usize
, scooter_display::ui::view::settings::Setting,
92
buoyant::view::match_view::OneOf2<buoyant::view::empty_view::EmptyView,
93
buoyant::view::button::Button<scooter_display::ui::view::settings::setting_entry::{closure#1},
94
buoyant::view::modifier::padding::Padding<buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::padding::Padding<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
95
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
96
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
97
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
98
buoyant::view::shape::rounded_rectangle::RoundedRectangle>>,
99
scooter_display::ui::view::settings::setting_entry::{closure#0}>
>
,
100
scooter_display::ui::view::settings::view::{closure
#
1
}
>
>
,
101
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
102
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>, buoyant::view::spacer::Spacer,
103
buoyant::view::match_view::OneOf2<buoyant::view::vstack::VStack<(buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
104
buoyant::view::hstack::HStack<(buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
105
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
4
: 
usize
]>>, glyphr::font::Font>>,
106
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
107
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
108
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
109
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
110
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
111
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
112
scooter_display::ui::view::settings::number_rotary<scooter_display::ui::view::settings::speed_limit_rotary_handler::{closure#0}>::{closure#1},
113
scooter_display::ui::view::settings::number_rotary<scooter_display::ui::view::settings::speed_limit_rotary_handler::{closure#0}>::{closure#0}>,
114
buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
115
buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
116
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
4
: 
usize
]>>, glyphr::font::Font>>,
117
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
118
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
119
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
120
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
121
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
122
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
123
scooter_display::ui::view::settings::number_rotary<scooter_display::ui::view::settings::speed_limit_rotary_handler::{closure#0}>::{closure#1},
124
scooter_display::ui::view::settings::number_rotary<scooter_display::ui::view::settings::speed_limit_rotary_handler::{closure#0}>::{closure#0}>)>)>,
125
buoyant::view::foreach::ForEachView<4: 
usize
, scooter_display::ui::view::settings::SettingEntry,
126
buoyant::view::button::Button<scooter_display::ui::view::settings::generic_setting_screen::{closure#0}::{closure#1},
127
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
128
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>,
129
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
130
scooter_display::ui::view::settings::generic_setting_screen::{closure#0}::{closure#0}>,
131
scooter_display::ui::view::settings::generic_setting_screen::{closure#0}>>, buoyant::view::spacer::Spacer,
132
buoyant::view::button::Button<scooter_display::ui::view::settings::view::{closure#2}::{closure#1},
133
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
134
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>,
135
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
136
scooter_display::ui::view::settings::view::{closure#2}::{closure#0}>)>>>,
137
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>
>
>
,
138
scooter_display::ui::view::settings::view::{closure
#
3
}
>
,
139
buoyant::view::modifier::captures_event::CapturesEvent<buoyant::view::modifier::padding::Padding<buoyant::view::scroll_view::ScrollView<buoyant::view::foreach::ForEachView<17:
140
usize
, scooter_display::ui::view::info::Info,
141
buoyant::view::button::Button<scooter_display::ui::view::info::info_entry::{closure#1},
142
buoyant::view::modifier::padding::Padding<buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::padding::Padding<buoyant::view::hstack::HStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
143
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
144
buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
145
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
146
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>)>>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
147
buoyant::view::shape::rounded_rectangle::RoundedRectangle>>, scooter_display::ui::view::info::info_entry::{closure#
0
}
>
,
148
scooter_display::ui::view::info::view::{closure
#
0
}
>
>
>
, scooter_display::ui::view::info::view::{closure
#
1
}
>
>
>
,
149
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rectangle::Rectangle
>
 
as
150
buoyant::view::ViewLayout<scooter_display::ui::state::State>
>
::layout::<buoyant::environment::DefaultEnvironment>
rust
Copy code
Copy
Copied!
1
<
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::match_view::OneOf4<buoyant::view::modifier::map_event::MapEvent<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
2
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
3
buoyant::view::capturing::Lens<buoyant::view::hstack::HStack<(buoyant::view::capturing::Lens<buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
4
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
5
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
6
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
7
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
8
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
9
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
10
scooter_display::ui::view::locked::pin_piece::{closure#1}, scooter_display::ui::view::locked::pin_piece::{closure#0}>,
11
scooter_display::ui::view::locked::pin_entry::{closure#0}>,
12
buoyant::view::capturing::Lens<buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
13
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
14
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
15
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
16
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
17
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
18
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
19
scooter_display::ui::view::locked::pin_piece::{closure#1}, scooter_display::ui::view::locked::pin_piece::{closure#0}>,
20
scooter_display::ui::view::locked::pin_entry::{closure#1}>,
21
buoyant::view::capturing::Lens<buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
22
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
23
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
24
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
25
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
26
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
27
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
28
scooter_display::ui::view::locked::pin_piece::{closure#1}, scooter_display::ui::view::locked::pin_piece::{closure#0}>,
29
scooter_display::ui::view::locked::pin_entry::{closure#2}>,
30
buoyant::view::capturing::Lens<buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
31
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
32
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
33
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
34
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
35
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
36
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
37
scooter_display::ui::view::locked::pin_piece::{closure#1}, scooter_display::ui::view::locked::pin_piece::{closure#0}>,
38
scooter_display::ui::view::locked::pin_entry::{closure#3}>)>, scooter_display::ui::view::locked::view::{closure#0}>,
39
buoyant::view::button::Button<scooter_display::ui::view::locked::view::{closure#2},
40
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<
&
str
,
41
glyphr::font::Font>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
42
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
43
scooter_display::ui::view::locked::view::{closure#1}>)>>, scooter_display::ui::view::locked::view::{closure#3}, ()>,
44
buoyant::view::modifier::captures_event::CapturesEvent<buoyant::view::vstack::VStack<(buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::hstack::HStack<(buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
45
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>,
46
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>>,
47
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
48
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
49
buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::foreach::ForEachView<3: 
usize
,
50
scooter_display::ui::view::home::TimePieceToShow,
51
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
52
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
3
: 
usize
]>>, glyphr::font::Font>,
53
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>, scooter_display::ui::view::home::header::{closure#3},
54
buoyant::view::foreach::Horizontal>>)>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
55
buoyant::view::shape::rectangle::Rectangle>,
56
buoyant::view::modifier::erase_captures::EraseCaptures<buoyant::view::vstack::VStack<(buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::hstack::HStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
57
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
3
: 
usize
]>>, glyphr::font::Font>,
58
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
59
buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
60
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
2
: 
usize
]>>, glyphr::font::Font>,
61
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
62
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
63
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>)>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
64
buoyant::view::shape::rectangle::Rectangle>>,
65
buoyant::view::modifier::padding::Padding<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::hstack::HStack<(buoyant::view::vstack::VStack<(buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::fixed_frame::FixedFrame<buoyant::view::modifier::padding::Padding<buoyant::view::hstack::HStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
66
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
67
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
68
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
69
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
70
buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
71
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::fixed_frame::FixedFrame<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
72
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
73
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
74
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
75
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
76
buoyant::view::shape::rounded_rectangle::RoundedRectangle>)>,
77
buoyant::view::vstack::VStack<(buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::fixed_frame::FixedFrame<buoyant::view::modifier::padding::Padding<buoyant::view::hstack::HStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
78
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
79
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
80
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
81
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
82
buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
83
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::fixed_frame::FixedFrame<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
84
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
85
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
86
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
87
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
88
buoyant::view::shape::rounded_rectangle::RoundedRectangle>)>)>>>)>>)>,
89
scooter_display::ui::view::home::view::{closure
#
0
}
>
,
90
buoyant::view::modifier::captures_event::CapturesEvent<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::popover::Popover<buoyant::view::scroll_view::ScrollView<buoyant::view::foreach::ForEachView<3:
91
usize
, scooter_display::ui::view::settings::Setting,
92
buoyant::view::match_view::OneOf2<buoyant::view::empty_view::EmptyView,
93
buoyant::view::button::Button<scooter_display::ui::view::settings::setting_entry::{closure#1},
94
buoyant::view::modifier::padding::Padding<buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::padding::Padding<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
95
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
96
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
97
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>)>>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
98
buoyant::view::shape::rounded_rectangle::RoundedRectangle>>,
99
scooter_display::ui::view::settings::setting_entry::{closure#0}>
>
,
100
scooter_display::ui::view::settings::view::{closure
#
1
}
>
>
,
101
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::vstack::VStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
102
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>, buoyant::view::spacer::Spacer,
103
buoyant::view::match_view::OneOf2<buoyant::view::vstack::VStack<(buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
104
buoyant::view::hstack::HStack<(buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
105
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
4
: 
usize
]>>, glyphr::font::Font>>,
106
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
107
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
108
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
109
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
110
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
111
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
112
scooter_display::ui::view::settings::number_rotary<scooter_display::ui::view::settings::speed_limit_rotary_handler::{closure#0}>::{closure#1},
113
scooter_display::ui::view::settings::number_rotary<scooter_display::ui::view::settings::speed_limit_rotary_handler::{closure#0}>::{closure#0}>,
114
buoyant::view::text::Text<
&
str
, glyphr::font::Font>,
115
buoyant::view::rotary::Rotary<buoyant::view::modifier::content_shape::ContentShape<buoyant::view::modifier::background::BackgroundView<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::modifier::padding::Padding<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
116
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
4
: 
usize
]>>, glyphr::font::Font>>,
117
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
118
buoyant::view::match_view::OneOf3<buoyant::view::empty_view::EmptyView,
119
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
120
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
121
buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::shape::Stroked<buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
122
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
123
scooter_display::ui::view::settings::number_rotary<scooter_display::ui::view::settings::speed_limit_rotary_handler::{closure#0}>::{closure#1},
124
scooter_display::ui::view::settings::number_rotary<scooter_display::ui::view::settings::speed_limit_rotary_handler::{closure#0}>::{closure#0}>)>)>,
125
buoyant::view::foreach::ForEachView<4: 
usize
, scooter_display::ui::view::settings::SettingEntry,
126
buoyant::view::button::Button<scooter_display::ui::view::settings::generic_setting_screen::{closure#0}::{closure#1},
127
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
128
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>,
129
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
130
scooter_display::ui::view::settings::generic_setting_screen::{closure#0}::{closure#0}>,
131
scooter_display::ui::view::settings::generic_setting_screen::{closure#0}>>, buoyant::view::spacer::Spacer,
132
buoyant::view::button::Button<scooter_display::ui::view::settings::view::{closure#2}::{closure#1},
133
buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::padding::Padding<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
134
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>>,
135
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>,
136
scooter_display::ui::view::settings::view::{closure#2}::{closure#0}>)>>>,
137
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rounded_rectangle::RoundedRectangle>
>
>
,
138
scooter_display::ui::view::settings::view::{closure
#
3
}
>
,
139
buoyant::view::modifier::captures_event::CapturesEvent<buoyant::view::modifier::padding::Padding<buoyant::view::scroll_view::ScrollView<buoyant::view::foreach::ForEachView<17:
140
usize
, scooter_display::ui::view::info::Info,
141
buoyant::view::button::Button<scooter_display::ui::view::info::info_entry::{closure#1},
142
buoyant::view::modifier::padding::Padding<buoyant::view::modifier::background_color::BackgroundColor<buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::padding::Padding<buoyant::view::hstack::HStack<(buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<
&
str
,
143
glyphr::font::Font>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565>,
144
buoyant::view::modifier::flex_frame::FlexFrame<buoyant::view::modifier::foreground_color::ForegroundStyle<buoyant::view::text::Text<heapless::string::StringInner<
u8
,
145
heapless::vec::storage::VecStorageInner<[core::mem::maybe_uninit::MaybeUninit<
u8
>; 
8
: 
usize
]>>, glyphr::font::Font>,
146
embedded_graphics_core::pixelcolor::rgb_color::Rgb565>>)>>>, embedded_graphics_core::pixelcolor::rgb_color::Rgb565,
147
buoyant::view::shape::rounded_rectangle::RoundedRectangle>>, scooter_display::ui::view::info::info_entry::{closure#
0
}
>
,
148
scooter_display::ui::view::info::view::{closure
#
0
}
>
>
>
, scooter_display::ui::view::info::view::{closure
#
1
}
>
>
>
,
149
embedded_graphics_core::pixelcolor::rgb_color::Rgb565, buoyant::view::shape::rectangle::Rectangle
>
 
as
150
buoyant::view::ViewLayout<scooter_display::ui::state::State>
>
::layout::<buoyant::environment::DefaultEnvironment>

This of course isn’t ideal as it means we’re going to be generating an absolute ton of code bloat from all the possible instantiations, as a result, the code generated by Buoyant takes up easily 80% of the 190KB size of the binary :/ Currently the code fits, but it’s quite limiting, and I don’t really have space to add any more features. I’ve started working on a new library that I hope should improve on this, but it’s not going to be done any time soon.

### Finally getting this code onto the real thing

So far, all this development has been happening on the cracked open display unit using a debugger, with the application starting from 0x800000 so that no code was running before mine, but when running on a real scooter, the application base is at 0x8008000. This is normally fine; the initialisation code of the application firmware just needs to be configured to configure the interrupt vector base address, so that the bootloader’s interrupts aren’t used instead of yours. It was almost the case that this was all that was needed with my firmware, but for some reason, when the bootloader was allowed to run the CAN bus would no longer receive messages; instead it would repeatedly throw framing errors. After a lot of head bashing and printing of register contents, it dawned on me that the bootloader was enabling some clocks and initialising some peripherals. When a clock is running it becomes impossible to change things like the divisor, this leads to my clock initialisation code not being able to set the correct divisor or clock source for the CAN peripheral, leading to it calculating its timing parameters with the wrong clock frequency…

The solution ends up being this horrible dance that needs to be done:

rust
Copy code
Copy
Copied!
1
 
let
 dp 
=
 
unsafe
 { hal::pac::Peripherals::steal() };
2
 
let
 
mut
 cp 
=
 cortex_m::peripheral::Peripherals::take().
unwrap
();
3
4
 
//
 Bootloader jumps to us with some clocks enabled, so the first thing
5
 
//
 we do is tear everything down.
6
7
 
//
 There might be a better way, and some of these are probably not necessary.
8
 dp.
CRM
.
ctrl
().
reset
();
9
 dp.
CRM
.
cfg
().
reset
();
10
 dp.
CRM
.
clkint
().
reset
();
11
 dp.
CRM
.
pll
().
reset
();
12
 dp.
CRM
.
misc1
().
modify
(|_, w| 
unsafe
 {
13
 w.
clkoutdiv
()
14
 .
bits
(
0
)
15
 .
hickdiv
()
16
 .
bit
(
false
)
17
 .
clkout_sel3
()
18
 .
bit
(
false
)
19
 });
20
21
 dp.
CRM
.
apb2en
().
modify
(|_, w| {
22
 w.
iomux
()
23
 .
bit
(
false
)
24
 .
gpioa
()
25
 .
bit
(
false
)
26
 .
gpiof
()
27
 .
bit
(
false
)
28
 .
spi1
()
29
 .
bit
(
false
)
30
 });
31
 dp.
CRM
.
apb1en
().
modify
(|_, w| w.
can1
().
bit
(
false
));
32
 dp.
CRM
.
ahben
().
modify
(|_, w| w.
dma1
().
bit
(
false
));
33
34
 dp.
CRM
35
 .
ctrl
()
36
 .
modify
(|_, w| w.
pllen
().
clear_bit
().
hexten
().
clear_bit
());
37
38
 dp.
CRM
.
cfg
().
modify
(|_, w| 
unsafe
 {
39
 w.
pllrcs
()
40
 .
clear_bit
()
41
 .
pllmult3_0
()
42
 .
bits
(
0
)
43
 .
pllmult5_4
()
44
 .
bits
(
0
)
45
 });
46
47
 
//
 finally we can now configure our clocks
48
 
let
 crm 
=
 dp.
CRM
.
constrain
();
49
50
 
let
 clocks 
=
 crm
51
 .cfgr
52
 .
use_hext
(
8.
MHz())
53
 .
sclk
(
96.
MHz()) 
//
 can seems to fall over if this is clocked any higher
54
 .
pclk1
(
48.
MHz())
55
 .
pclk2
(
48.
MHz())
56
 .
freeze
();
rust
Copy code
Copy
Copied!
1
 
let
 dp 
=
 
unsafe
 { hal::pac::Peripherals::steal() };
2
 
let
 
mut
 cp 
=
 cortex_m::peripheral::Peripherals::take().
unwrap
();
3
4
 
//
 Bootloader jumps to us with some clocks enabled, so the first thing
5
 
//
 we do is tear everything down.
6
7
 
//
 There might be a better way, and some of these are probably not necessary.
8
 dp.CRM.
ctrl
().
reset
();
9
 dp.CRM.
cfg
().
reset
();
10
 dp.CRM.
clkint
().
reset
();
11
 dp.CRM.
pll
().
reset
();
12
 dp.CRM.
misc1
().
modify
(|
_
,
 
w|
 
unsafe
 
{
13
 w
.
clkoutdiv
()
14
 
.
bits
(
0
)
15
 
.
hickdiv
()
16
 
.
bit
(
false
)
17
 
.
clkout_sel3
()
18
 
.
bit
(
false
)
19
 
});
20
21
 dp.CRM.
apb2en
().
modify
(|
_
,
 
w|
 
{
22
 w
.
iomux
()
23
 
.
bit
(
false
)
24
 
.
gpioa
()
25
 
.
bit
(
false
)
26
 
.
gpiof
()
27
 
.
bit
(
false
)
28
 
.
spi1
()
29
 
.
bit
(
false
)
30
 
});
31
 dp.CRM.
apb1en
().
modify
(|
_
,
 
w|
 
w
.
can1
().
bit
(
false
));
32
 dp.CRM.
ahben
().
modify
(|
_
,
 
w|
 
w
.
dma1
().
bit
(
false
));
33
34
 dp.CRM
35
 .
ctrl
()
36
 .
modify
(|
_
,
 
w|
 
w
.
pllen
().
clear_bit
().
hexten
().
clear_bit
());
37
38
 dp.CRM.
cfg
().
modify
(|
_
,
 
w|
 
unsafe
 
{
39
 w
.
pllrcs
()
40
 
.
clear_bit
()
41
 
.
pllmult3_0
()
42
 
.
bits
(
0
)
43
 
.
pllmult5_4
()
44
 
.
bits
(
0
)
45
 
});
46
47
 
//
 finally we can now configure our clocks
48
 
let
 crm 
=
 dp.CRM.
constrain
();
49
50
 
let
 clocks 
=
 crm
51
 .cfgr
52
 .
use_hext
(
8.
MHz())
53
 .
sclk
(
96.
MHz()) 
//
 can seems to fall over if this is clocked any higher
54
 .
pclk1
(
48.
MHz())
55
 .
pclk2
(
48.
MHz())
56
 .
freeze
();

With this setup code in place, the scooter display unit is now able to correctly boot into the bootloader, which boots the main application, which then reconfigures the clocks appropriately, sets up the required peripherals, and then starts up all the tasks. If you’re interested in the source code, you can find it here:https://github.com/simmsb/scooter-display

Your browser does not support the video tag

Figure 21: The scooter in use. Note the huge range prediction due to the wheels spinning freely

### The future

I’m very happy with how this project went, I was actually quite surprised at how easy it was to build firmware with a nice interface that’s also reliable enough for me to use daily. I think I’m going to work on other things now as I think I’ve been working on this project for over 6 months now. But there’s still lots that I could do, including rewriting the motor controller firmware, and adding some data logging capabilities (it would be nice to see a graph of battery against distance travelled).