---
title: 'blog.smartere » Floppy Disks: the best TV remote for kids'
url: https://blog.smartere.dk/2026/01/floppy-disks-the-best-tv-remote-for-kids/
site_name: hackernews
fetched_at: '2026-01-13T11:07:44.213846'
original_url: https://blog.smartere.dk/2026/01/floppy-disks-the-best-tv-remote-for-kids/
author: mchro
date: '2026-01-13'
---

# Floppy Disks: the best TV remote for kids

Posted on
mandag, januar 12, 2026
 in
Hal9k
,
Planet Ubuntu-DK
,
Planets

Modern TVs are very poorly suited for kids. They require using complicated remotes or mobile phones, and navigating apps that continually try to lure you into watching something else than you intended to. The usual scenario ends up with the kid feeling disempowered and asking an adult to put something on. That something ends up on auto-play because then the adult is free to do other things and the kid ends up stranded powerless and comatose in front of the TV.

Instead I wanted to build something for my 3-year old son that he could understand and use independently. It should empower him to make his own choices. It should be physical and tangible, i.e. it should be something he could touch and feel. It should also have some illusion that the actual media content was stored physically and not un-understandably in “the cloud”, meaning it should e.g. be destroyable — if you break the media there should be consequences. And there should be no auto-play: interactonceand getonevideo.

## Floppy disks are awesome!

And then I remembered the sound of a floppy disk. The mechanical click as you insert it, the whirr of the disk spinning, and the sound of the read-head moving. Floppy disks are the best storage media ever invented! Why else would the “save-icon” still be a floppy disk? Who hasn’t turned in a paper on a broken floppy disk, with the excuse ready that the floppy must have broken when the teacher asks a few days later? But kids these days have never used nor even seen a floppy disk, and I believe they deserve this experience!

Building on the experience from theBig Red Fantus-Button, I already had a framework for controlling a Chromecast, and because of thenetcat | bashshenanigans it was easily extendable.

My first idea for datastorage was to use the shell of a floppy disk and floppy drive, and put in an RFID tag; this has been done a couple of times on the internet, such asRFIDiskor thisRaspberryPi based RFID readeror thisvideo covering how to embed an RFID tag in a floppy disk. But getting the floppy disk apart to put in an RFID tag and getting it back together was kinda wonky.

When working on the project inHal9ksomeone remarked: “Datastorage? The floppy disk can store data!”, and a quick prototype later this worked really,really, well. Formatting the disk and storing a single small file, “autoexec.sh”, means that all the data ends up in track 0 and is read more or less immediately. It also has the benefit that everything can be checked and edited with a USB floppy disk drive; and the major benefit that all the sounds are completely authentic: click, whirrr, brrr brrr.

## Autorun for floppy disks is not really a thing.

The next problem to tackle was how to detect that a disk is inserted. The concept ofAutoRunfrom Windows 95 was a beauty: insert a CD-ROM and it would automatically start whatever was on the media. Great for convenience, quite questionably for security. Whilein theoryfloppy disks are supported for AutoRun, it turns out that floppy drives basically don’t know if a disk is inserted until the operating system tries to access it! There is apin 34 “Disk Change” that is supposed to give this information, but this is basically a lie. None of the drives in my possession had that pin connected to anything, and the internet mostly concurs. In the end I slightly modified the drive and added a simple rolling switch, that would engage when a disk was inserted.

## A floppy disk walks into a drive; the microcontroller says “hello!”

The next challenge was to read the data on a microcontroller. Helpfully, there is theArduino FDC Floppy libraryby dhansel, which I must say ismostexcellent. Overall, this meant that the part of the project that involved reading a file from the floppy disk FAT filesystem was basically the easiest part of all!

A combined ATMega + ESP8266 UNO-like board. Not really recommended, but can be made to work.

However, theArduino FDC Floppylibrary isonlycompatible with the AVR-based Arduinos, not the ESP-based ones, because it needs to control the timing very precisely and therefore uses a healthy amount of inline assembler. This meant that I would need one AVR-based Arduino to control the floppy disk, but another ESP-based one to do the WiFi communication. Such combined boards do exist, and I ended up using such a board, but I’m not sure I would recommend it: the usage is really finagly, as you need to set the jumpers differently for programming the ATmega, or programming the ESP, or connecting the two boards serial ports together.

## A remote should be battery-powered

A remote control should be portable, and this means battery-powered. Driving a floppy disk of of lithium batteries was interesting. There is a large spike in current draw when the disk needs to spin up of several amperes, while the power draw afterwards is more modest, a couple of hundred milliamperes. I wanted the batteries to be 18650s, because I have those in abundance. This meant a battery voltage of 3.7V nominally, up to 4.2V for a fully charged battery; 5V is needed to spin the floppy around, so a boost DC-DC converter was needed. I used an off the shelf XL6009 step-up converter board. At this point a lot of head-scratching occurred: that initial spin-up power draw would cause the microcontroller to reset. In the end a 1000uF capacitor at the microcontroller side seemed to help but not eliminate the problem.

One crucial finding was that the ground side of the interface cable should absolutelynotbe connected to any grounds on the microcontroller side. I was using a relatively simple logic-level MOSFET, theIRLZ34N, to turn off the drive by disconnecting the ground side. If any ground is connected, the disk won’t turn off. But also: if any logic pin was being pulled to ground by the ATmega, that would also provide a path to ground. But since the ATmega cannot sink that much current this would lead to spurious resets! Obvious after the fact, but this took quite some headscratching.Setting all the logic pins to input, and thus high impedance, finally fixed the stability issues.

After fixing the stability, the next challenge was how to makebothof the microcontrollers sleep. Because the ATmega sleep modes are quite a lot easier to deal with, and because the initial trigger would be the floppy inserting, I decided to make the ATmega in charge overall. Then the ESP has a very simple function: when awoken, read serial in, when a newline is found then send off that complete line via WiFi, and after 30 seconds signal to the ATmega that we’re sleeping, and go back to sleep.

The overall flow for the ATmega is then:

1. A disk is inserted, this triggers a interrupt on the ATmega that wakes up.
2. The ATmega resets the ESP, waking it from deep sleep.
3. The ATmega sends a “diskin” message over serial to the ESP; the ESP transmits this over WiFi when available.
4. The ATmega turns on the drive itself, and reads the disk contents, and just sends it over serial to the ESP.
5. Spin down the disk, go to sleep.
6. When the disk is ejected, send a “diskout” message over serial, resetting the ESP if needed.
7. Go back to 1.

The box itself is just lasercut from MDF-board. For full details see theFloppyDiskCast Git repository.

## Server-side handlers

Responding to those commands is still thenetcat | bashfrom theBig Red Fantus-Button, which was simply extended with a few more commands and capabilities.

A few different disks to chose from, with custom printed labels.

diskinalways sends a “play” command to the Chromecast.diskoutalways sends a “pause” command to the Chromecast.Other commands likedad-musicare handled in one of two ways:

* Play a random video from a set, if a video from that set is not already playing: e.g.dad-musicwill randomly play one of dad’s music tracks – gotta influence the youth!
* Play the next video from a list, if a video from the list is not already playing: e.g.fantus-maskinernewill play the next episode, and only the next episode.

Common for both is that they should be idempotent actions, and thediskinshortcut will make the media resume without having to wait for the disk contents itself to be read and processed. This means that the “play/pause” disk just contains an empty file to work.

## Questionable idea meets real-world 3 year old user

The little guy quickly caught on to the idea! Much fun was had just pausing and resuming music and his Fantus TV shows. He explored and prodded, and some diskswereharmed in the process. One problem that I did solve was that the read head stayed on track 0 after having read everything: this means that when the remote with disk inside it is tumbled around, the disk gets damaged at track 0. To compensate for this, I move the head to track 20 after reading has finished: any damage is then done there, where we don’t store any data. As a bonus it also plays a little more mechanic melody.

## Bring on the comments

1. Tamara Raetzsiger:12. januar 2026 kl. 17:29That was a lot of work to go to so that you could delay or avoid both negative and positive interactions with your son. When you engage face to face you could be teaching him qualities like patience and obedience and encouragement; you could be showing him frequently that you enjoy his company, that he is a likeable person worth your time and attention. Technology is not supposed to replace parenting, friend.Reply to this Comment
2. Theronsiger:12. januar 2026 kl. 19:00Awesome. I’ve wanted to do something with mini disks myself for a while.Did you consider just using the disks as a carrier and putting a RFC tag under the sticker or something? Would dramatically lower power consumption.Reply to this Comment

### Leave a Reply

Klik her for at annullere svar.

Name (required)

Mail (will not be published) (required)

Website

Δ
