---
title: MNT Reform
url: http://mnt.stanleylieber.com/reform/
site_name: hackernews_api
content_file: hackernews_api-mnt-reform
fetched_at: '2026-04-21T20:02:30.613406'
original_url: http://mnt.stanleylieber.com/reform/
author: speckx
date: '2026-04-20'
description: MNT Reform is an open hardware laptop, designed and assembled in Germany
tags:
- hackernews
- trending
---

# MNT Reform

MNT Reformis an open hardware laptop, designed and assembled in Berlin, Germany.

2021.10.08: orderedmnt reform.

2021.12.27: received mnt reform#000120.

2023.04.17: mnt reform #000120 is now being offered as aloanerbysdf.org.

2023.06.02: ordered mnt reform (2023 refresh).

2023.06.29: bought used mnt reform on ebay.

2023.07.03: received used mnt reform#000158.

2024.11.05: sold mnt reform #000158.

2025.02.24: bought used mnt reform on ebay.

2025.03.05: received used mnt reformdiy.

## screen

The trackball can press against the screen when the lid is closed, causing asmall mark to appear on the screen.

## case

Lid, screen bezel, keyboard frame, and wrist rest are made from milled aluminium. Side panels and transparent bottom panel are made from acrylic.

Screws in the LCD bezel are not covered, and over time the one in the center can start to rub the paint off of the wrist rest.

fabricate new side panels- forum thread

My friend kindly sent me a pair of metal replacement side panels. First I tried painting them with a paint brush and a bottle ofVanta Black. This flaked off easily, so I sanded them down and repainted them with black spraypaint (satin finish). Managed to chip that as well during installation. I don’t know what I’m doing.

2022.03.03 Update: MNT has now made availablesteel replacement side panels.

## accessories

usb-c pd adapter (female)- bought one,it works

usb-c pd adaptor (male, non-amazon)- reported to work

lifepo4 replacement batteries (affordable, out of stock)

lifepo4 replacement batteries (expensive, in stock)

lifepo4 external charger- for recovering depleted cells (2-bay)

lifepo4 external charger- for recovering more depleted cells (8-bay)

laird wifi antenna-improved reception

2022.04.27 Update: I ended up just stretching the original molex antenna down under the trackball, which improved reception even more than buying an expensive new antenna. Because of its shape and the orientation of its cables, the Laird antenna wouldn’t quite reach.

iogear gwu637 ethernet to wifi n adapter- for operating systems where wifi doesn’t (yet) work

piñatex sleeve- note: pull tabs broke off in the first week

2022.02.22 Update: MNT sent me a replacement sleeve with new, all-metal zipper pulls that are now standard equipment on the sleeve.

2022.07.16 Update: One of the all-metal zipper pulls shattered as I tried to unzip the sleeve.

mbk-colors: 1u and 1.5u homing-replacement key caps, some with raised edges to help with acclimating to the non-standard keyboard layout

## operating systems

9front-howto,sdcard image,sysinfo

alpine linux-
fully functional (howto pending)

void linux-sdcard image(does not boot on my machine)

debian linux-
pre-installed

## keyboard

http://mnt.stanleylieber.com/keyboard/

## audio in linux

fix for speakers too quiet:

 By default, the speaker output of MNT Reform is a bit quiet, and
 changing the volume with PulseAudio won’t dramatically change it.
 There’s one more knob you can turn up that is only accessible via
 ALSA.

 Open a Terminal and type alsamixer. Then press F6 and select
 the wm8960-audio card. Navigate with Cursor keys to the Playback
 slider and turn it up

Well, there is nowm8960-audiolisted on my system, only(default). AndMasteris already cranked to 100. Investigating, I noticed:

 sl@reform:~$ dmesg | grep 8960
 [ 3.613559] wm8960 2-001a: Failed to issue reset

edgineersays:

 Usually a reboot gets the audio going for me if I see failed to issue
 reset (happens on booting from power off). Lukas speculates on a fix
 here[1] and another person[2] provided this line in order to rebind the
 device without a reboot:

 echo 2-001a > /sys/bus/i2c/drivers/wm8960/bind

 I was able to replicate the issue and test the above line out just
 now. I had to “sudo su” first. Then the audio device showed up in
 alsamixer again just fine.

[1][2]

This worked for me, as well.

Update 2022.06.20: After numerous updates, sound no longer works for me in Alpine Linux.

## leds in linux

turn off wifi led:

 echo 0 > /sys/class/leds/ath9k-phy0/brightness # needs root permissions

## files

foot -foot.ini(sl)

rofi -mnt-reform.rasi

sway -config(default),config(sl)

vga -font(download page)

waybar -config,style.css

## doc

operator handbook -buy,pdf

diy assembly manual -pdf

interactive system diagram and interactive PCBs -html

sources (kicad, etc.) -repository

external usb keyboard manual -pdf

## reviews

arstechnica

## links

buy,community,faq,ifixit,reform school