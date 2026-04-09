---
title: Nokia N900 Necromancy
url: https://yaky.dev/2025-12-11-nokia-n900-necromancy/
site_name: hackernews_api
fetched_at: '2025-12-12T19:08:13.706770'
original_url: https://yaky.dev/2025-12-11-nokia-n900-necromancy/
author: Yaky
date: '2025-12-12'
description: Nokia N900 Necromancy
tags:
- hackernews
- trending
---

# Nokia N900 Necromancy

Building a fake battery, adding a USB-C port, booting from SD card, and giving a new life to a classic Linux smartphone.

My friend Dima sent me his old-school classic Nokia N900. The battery is very old, and it does not boot as-is. So naturally, I wanted to see if I can resurrect it.

## Step 0: Is such a thing even possible?

Yes it is! (Unless there are other hardware issues)

I ran a smartphone without a battery a few years ago.

I did look at BL-5J batteries for sale. Many listings say "Genuine" and "OEM", but what does that even mean for a battery for a device that is at least 10 years old? (Some later Nokia Lumia phones used the same battery) And listings with newer-looking batteries do not list the manufacture date. I don't need another old battery or a "spicy pillow".

Also, where's the fun in that?

Cut and soldered a quick prototype to connect instead of the battery. Resistors are to emulate the "normal" temperature by providing expected resistance between the third pin and ground. See link above for details.

Hooked up a large supercapacitor to the battery pins and to a +5V source. If I recall correctly, using a capacitor without additional power did not work.

And it boots!

Now, let's make something that can fit into the battery compartment.

## Step 1: Better "battery"

These supercapacitors are nice, but way too large. After searching on Mouser, I found FM0H473ZF, 47000 mF (0.047F) capacitors in a rectangular case that is only 5mm thick.

Ten of these (~0.5F) is enough to run the smartphone without dying.

Capacitor contraption (TM) arranged (using a 3D-printed template) and soldered together.

And they all fit nicely into the battery compartment. The power is provided by a wire routed through the hole for the carry loop.

Running fine! One noticeable issue is that capacitors are getting pretty warm. Probably my sloppy soldering, but no shorts that I could find.

## ⚠️

This is where I should have stopped. At some point while messing with the "battery" and power, I managed to corrupt the internal partition and the installed OS. Not sure if this was from the sudden battery pull or from supplying +5V instead of the expected +4.2V to the battery pins. Luckily, newer Maemo Leste is intended to run from the SD card anyway, and internal storage still works, so I was able to overwrite it with the bootloader.

Bootloader setup on Maemo Wiki

## Step 2: Consolidating connectors

I thought it might be practical to power the "battery" through the existing USB port. Just run the +5V wire from USB to the "battery", and avoid additional wires. (If you think this is kinda stupid, you are right)

Yooo... What is happening here? Dima says "oh yeah, the USB port was re-soldered. Twice". A quick glance at the forums also confirms that USB port was poorly designed and is prone to breaking.

Just one wire from the +5V pad to the "battery". The ground is the same as the battery pin.

Assembled everything back, routed and soldered the +5V wire, and added a diode to prevent the battery from feeding the USB port, and to drop the voltage to more acceptable ~4.3V.

The setup works, but the smartphone constantly shows either "Charging", or "Device using more power than it is receiving from the PC. Charging with a compatible charger is recommended", with battery gauge going crazy.

And then, the power just cut out.

Yeah, this was not a great idea. Let's see what happened.

USB +5V wire detached itself from the port. I presume this is from either the high current, age, stress, or corrosion.

However, when I opened the smartphone up, I... ripped off the +5V pad. (dark circle in lower right on the photo)

Fuck.

After reading some N900 forums, that +5V pad is a common place to connect the replacement USB port to (which was done here), but... that is the ONLY +5V connection on the board besides the pads under the USB port itself.

FUCK!

## 🪦

RIP Nokia N900. I tried to resurrect you, but instead, I killed your OS and ripped out the USB port wires.

## Step 3: Radical replacements

To be fair, N900 is far from dead. I already flashed u-boot, was able to boot from SD card, and do not plan to use internal storage otherwise. Power can be supplied entirely through the new "battery". So technically, I do not need the USB functionality for the smartphone itself, just to power the "battery". At this point, I might as well replace the port with USB-C. Because why not.

Approximate placement of the new USB port.

The location of the original port is not very convenient. It is sandwiched between the main board and the SD card reader (lower left on the photo). SD card reader is also attached by a permanently-attached ribbon (i.e. nearly irreplaceable).

First, I used a small file to make the micro-USB-shaped hole on the smartphone body fit the USB-C shape. Then, I took a small 6-pin USB-C port, cut and sanded down its plastic parts to make it fit in the original spot. It is still slightly (~0.25mm) taller than the original, but I cannot make it any slimmer.

I tried to attach the USB-C port to the board in the correct place by carefully assembling the board, port and SD card reader into the body, and using small drops of glue to lightly affix the edge of the USB port (that I could reach) to the main board. The intent was to wait for glue to cure, take everything back apart and glue the port in its now-correct position for good. This took several tries but did not really work, as the port got detached while removing the main board every time, and the the superglue I used left lots of residue but did not adhere. Luckily, the tight fit and the shape of the USB-C port hold it in place mechanically quite well.

USB-C with +5V and ground attached.

Originally, I planned to solder all 6 pins and add 5.1 Ohm pull-down resistors to CC1 and CC2 pins (for full power delivery functionality). But there is simply not enough space to route the wires, the narrow valley between the chips (in the lower right of the photo) barely fits 3, and I did not have anything thinner on hand.

Nokia N900 with a USB-C port! Looks pretty nice IMO.

Since I did not solder the pull-down resistors, this USB-C port could only be powered by a "dumb" USB-A-to-USB-C cable, at default 0.5A. Chargers with power delivery functionality cannot identify such USB-C ports, and will not provide power at all. (This is also an issue with some handheld consoles such as RGB30)

The two wires are routed to the battery compartment through a very convenient opening in the metal frame, crimped and inserted into a DuPont connector.

Back to the battery. The capacitor contraption I built before works, but was kind of flimsy, and does not have any more space for a DuPont connector. Also, I would rather use a single capacitor, but it still has to fit. Since the original battery is unusable, I might as well try to salvage it, too.

Take off the sticker (that tells you not to do so :). The top BCM piece is held to the main battery body by two tiny screws (hidden under some crumbly compound) on each end, double-sided sticker, and a single lead in the middle.

Battery Control Module. Interestingly, for this battery, the body is the positive terminal. So the positive lead connects the battery body and the positive pin directly, while the negative lead goes thorough some control circuitry. Attaching a capacitor to these battery terminals should be sufficient.

Since I have a 3D printer, and once you have one, every problem can be solved by printing stuff, I printed the new "battery" to accommodate a large capacitor, diode (for voltage drop), wires, DuPont connectors, and the original battery's BCM.

N900 with a new "battery". Fits really tight, and only 0.25-0.5mm too tall, so the cover still snaps closed.

Boots without problems. Since the attached capacitor is pretty large, it can take a minute or two to charge it to an acceptable level (~4.0V) with a 0.5A current.

Nokia N900 enjoying its new life as an online radio device using Open Media Player.
