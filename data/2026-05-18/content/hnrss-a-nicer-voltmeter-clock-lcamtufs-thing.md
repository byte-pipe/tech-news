---
title: A nicer voltmeter clock - lcamtuf’s thing
url: https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock
site_name: hnrss
content_file: hnrss-a-nicer-voltmeter-clock-lcamtufs-thing
fetched_at: '2026-05-18T06:00:47.633778'
original_url: https://lcamtuf.substack.com/p/a-nicer-voltmeter-clock
author: lcamtuf
date: '2026-05-16'
description: Sometimes, electronic circuit design is mostly about wood
tags:
- hackernews
- hnrss
---

# A nicer voltmeter clock

### Sometimes, electronic circuit design is mostly about wood

May 16, 2026
23
11
3
Share

Back in 2019, I built a simple voltmeter clock:

The clock, version 1. Cherry enclosure.

As the name implies, these clocks use analog panel voltmeters instead of traditional clock faces to display time. I didn’t come up with the idea, so I never really blogged about the design; I just built one and kept it on my office desk.

The idea endures, but most of the designs I see on the internet are needlessly complicated and not all that pretty, so when I decided to build a revised design, I figured it might be good to document it better. The process started with a rough mockup in a 3D design program:

A mockup of the new design in Rhino3D.

For this version of the meter clock, I opted to use three generic, 90° panel voltmeters from Amazon (link, about $9). I disassembled them, took careful measurements of the faces, and then printed replacement decals on adhesive paper. Printable PDF templates can be foundhere.

Customizing 5 V panel meters.

Note that the new hour gauge has 13 divisions, from 0 to 12, while the minute and second templates have 61 divisions, from 00 to 60. This is because I wanted to implement continuous motion for each hand; this meant that at 11:30, the hour dial couldn’t be just stuck at 11; it needed to be moving toward the twelfth division, even if it was never to reach it.

In addition to a host of other problems, the cheap “Baomain 65C5” meters I’m using have a rather hideous plastic flange. I decided to hide this flange from view and use a recessed decorative pattern to keep the front panel interesting. This made it more expedient to cut the front and back on a CNC mill instead of building the enclosure by hand (as I did for version 1). The stock material is maple lumber resawn, squared, and planed in my workshop:

Machined front and back faces.

The rounded side wall posed a different challenge. For a seamless appearance, I needed to do bend a flat piece of wood using a shaped template. To pull this off without a steam bending jig, I had to cut a series of internal notches on the side wall. This allowed the wood to flex more easily:

Manually bending side walls using an internal template.

The wood had to be moistened, clamped, and then allowed to dry. After a couple of days, I glued the curved side wall to the front and back faces, relying on another template cut out of scrap plywood to get a precise fit without any more gymnastics with clamps and ratchet straps:

Gluing up clock body using an external template (plywood).

Anyway — here’s the assembled piece after sanding and a coat of nitrocellulose lacquer:

Initial fitting.

Not bad, right?

The circuit is far less interesting and took just an hour or so: I grabbed the venerableAVR128DB28MCU, powered it off a wall wart, interfaced it to an 8 MHz crystal (ECS-80-18-4X-CKM). A 32.768 kHz crystal would also do. The panels are connected to three digital output pins (PC0, PC1, PC2). Finally, two input pins (PD6, PD7) are interfaced to two small pushbuttons mounted on the back and used to set time.

Note that the circuit doesn’t required digital-to-analog converters or any other additional components to drive the meters; instead, I’m just using a relatively high-frequency, 1-bit digital pulse train. The inertia of the meter (and the inductance of the coil inside the meter) does the rest, settling in an intermediate position depending on the software-controlled signal duty cycle.

The code can be viewedhere; it’s short and well-commented. The basic idea is to advance a 10 Hz counter using a timer interrupt synchronized with the crystal. With this out of the way, the main event loop computes the appropriate duty cycle and then manually toggles the output pins. Although the chip has a hardware PWM module, the application is simple enough that using the PWM circuitry wouldn’t really buy us anything.

Here’s the obligatory “rollover” video captured around 11:59:59:

Peace out.

If you’re new here, you might enjoy some of my other articles:

#### Notched sticks to calculators: the history of counting machines

lcamtuf
·
August 26, 2023
Read full story

#### See it with your lying ears

lcamtuf
·
Jan 10
Read full story

#### A breakthrough in C/C++ dependency management

lcamtuf
·
Apr 25
Read full story

#### How has mathematics gotten so abstract?

lcamtuf
·
September 27, 2025
Read full story
Subscribe
23
11
3
Share