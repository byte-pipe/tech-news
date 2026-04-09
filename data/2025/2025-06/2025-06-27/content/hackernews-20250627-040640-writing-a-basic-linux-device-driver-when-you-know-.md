---
title: Writing a basic Linux device driver when you know nothing about Linux drivers or USB // crescentro.se
url: https://crescentro.se/posts/writing-drivers/
site_name: hackernews
fetched_at: '2025-06-27T04:06:40.870528'
original_url: https://crescentro.se/posts/writing-drivers/
author: sbt567
date: '2025-06-27'
---

A couple of months ago I bought theNanoleaf Pegboard Desk Dock, the latest and greatest in USB-hub-with-RGB-LEDs-and-hooks-for-gadgets technology. This invention unfortunately only supports thereal gameroperating systems of Windows and macOS, which necessitated the development of a Linux driver.

Over the past few posts I’ve set up aWindows VM with USB passthrough, and attempted toreverse-engineer the official drivers, As I was doing that, I also thought I’d message the vendor and ask them if they could share any specifications or docs regarding their protocol. To my surprise, Nanoleaf tech support responded to me within 4 hours, with a full description of the protocol that’s used both by the Desk Dock as well as their RGB strips. The docs mostly confirmed what I had already discovered independently, but there were a couple of other minor features as well (like power and brightness management) that I did not know about, which was helpful.

Today, we’re going to take a crack at writing a driver based on the (reverse-engineered) protocol, while also keepingthe official documentationat hand. One small problem, though: I’ve never written a Linux device driver before, nor interacted with any USB device as anything else but a user.

## Starting from scratch

Most Linux distros ship withlsusb, a simple utility that will enumerate all USB devices connected to the system. Since I had no clue where to start from, I figured I might as well run this to see if the device appears in the listing.

$ lsusb

<snip>

Bus 001 Device 062: ID 37fa:8201 JW25021301515 Nanoleaf Pegboard Desk Dock

Well, good news, it’s definitely there. But, how can the kernel know that what I have plugged in is the “Nanoleaf Pegboard Desk Dock”? The kernel (presumably) has no knowledge of this device’s existence, yet the second I plug it in to my computer it receives power, turns on and gets identified by the kernel.

As it turns out, we actually already have a driver! It’s just a very stupid one. If we runlsusbin verbose mode and request the information just for this specific device, we will get a lot more details about it:

$ lsusb -d 37fa:8201 -v

Bus 001 Device 091: ID 37fa:8201 JW25021301515 Nanoleaf Pegboard Desk Dock
Negotiated speed: Full Speed (12Mbps)
Device Descriptor:
 bLength 18
 bDescriptorType 1
 bcdUSB 1.10
 bDeviceClass 0 [unknown]
 bDeviceSubClass 0 [unknown]
 bDeviceProtocol 0
 bMaxPacketSize0 64
 idVendor 0x37fa JW25021301515
 idProduct 0x8201 Nanoleaf Pegboard Desk Dock
 bcdDevice 1.09
 iManufacturer 1 JW25021301515
 iProduct 2 Nanoleaf Pegboard Desk Dock
 iSerial 3 <snip>
 bNumConfigurations 1
 Configuration Descriptor:
 bLength 9
 bDescriptorType 2
 wTotalLength 0x0029
 bNumInterfaces 1
 bConfigurationValue 1
 iConfiguration 4 Nanoleaf Pegboard Desk Dock
 bmAttributes 0xa0
 (Bus Powered)
 Remote Wakeup
 MaxPower 70mA
 Interface Descriptor:
 bLength 9
 bDescriptorType 4
 bInterfaceNumber 0
 bAlternateSetting 0
 bNumEndpoints 2
 bInterfaceClass 3 Human Interface Device
 bInterfaceSubClass 0 [unknown]
 bInterfaceProtocol 0
 iInterface 5 Nanoleaf Pegboard Desk Dock
 HID Device Descriptor:
 bLength 9
 bDescriptorType 33
 bcdHID 1.00
 bCountryCode 0 Not supported
 bNumDescriptors 1
 bDescriptorType 34 (null)
 wDescriptorLength 34
 Report Descriptors:
 ** UNAVAILABLE **
 Endpoint Descriptor:
 bLength 7
 bDescriptorType 5
 bEndpointAddress 0x82 EP 2 IN
 bmAttributes 3
 Transfer Type Interrupt
 Synch Type None
 Usage Type Data
 wMaxPacketSize 0x0040 1x 64 bytes
 bInterval 1
 Endpoint Descriptor:
 bLength 7
 bDescriptorType 5
 bEndpointAddress 0x02 EP 2 OUT
 bmAttributes 3
 Transfer Type Interrupt
 Synch Type None
 Usage Type Data
 wMaxPacketSize 0x0040 1x 64 bytes
 bInterval 1
Device Status: 0x0000
 (Bus Powered)

This is alotof information, so we need to take a quick USB class.

## A quick USB class

The USB spec is long, complicated and mainly aimed at low-level implementations (think kernel developers, device vendors, and so on). You can, of course, still read it if you enjoy being bored. But, thankfully, a kind soul collected the good parts intoUSB in a NutShell.

To summarize the summary, a USB device can have multipleconfigurations, which usually explain the power requirements for the device. Most devices will have just one.

Each of those configurations can have multipleinterfaces. So for example, a camera might serve as a file storage device as well as a webcam.

Finally, each interface can have multipleendpoints, whcih describe how the data is transferred. Perhaps the camera has an “isochronous” (continuous) transfer for a webcam feed, and a “bulk” transfer for moving image files over.

Going back to our device, we can see that it exposes one interface, which is aHuman Interface Device. HIDs are a class of USB devices that covers things like keyboards, mice or gamepads, and each of those categories is a separatesub-class. The kernel contains a generic driver for USB HIDs -here it isin all of its C glory.

This is why the kernel developers do not need to write specific drivers for each individual keyboard and mouse on the market. Vendors will label their device with one of the well-known HID sub-classes, then use a common protocol to implement the functionality.

Unfortunately there’s no HID specification for an RGB LED… thing (well, there’s an “LED” specification, but it’s mainly for things like status LEDs, not color LEDs) so our device is just a plain old generic HID with an interface sub-class of0. This means that the kernel recognizes it and powers it correctly, but it doesn’t really know what to do with it, so it just lets it sit there.

There are two options that we have at this point:

1. We could write a kernel driver that follows thekernel standardand exposes each individual LED as 3 devices (one per color) under/sys/class/leds. Interacting with the kernel devs sounds scary (yes I realize I’m a grown-ass adult man), but even if it wasn’t, I question the utility of trying to merge drivers for a very niche product into the kernel. Also,/sys/class/ledsfeels like it’s intended for status LEDs and notgamer colorsanyway.
2. We could write a userspace driver throughlibusb, thus defining our own way of controlling LEDs and reducing the quality bar from “Linus Torvalds might send you a strongly worded letter if you fuck up” to “fuck it, we ball”.

Given that I have no idea what I am doing, I’m gonna go for option 2, but if one of you brave souls goes for option 1, please let me know and I will print out a photo of you and frame it on my wall.

### Side quest: udev rules

To do anything fun on Linux, you need to beroot. This is also the case when talking to USB devices. You could always run your drivers asroot, thus sidestepping the problem. But we all know that’s bad form. And if I am to distribute this driver, most people would expect to run it without privilege escalation.

Linux generally relies onudevto manage handlers for hardware events. I will spare you the long story this time and just give you the magic incantation: to make your device accessible to users, you need to create a file at/etc/udev/rules.d/70-pegboard.ruleswith the following contents:

ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", ATTRS{idVendor}=="37fa", ATTRS{idProduct}=="8201", MODE="0770", TAG+="uaccess"

whereATTRS{idVendor}andATTRS{idProduct}are the vendor and product IDs you got fromlsusb, andTAG+="uaccess"is the spell that grants the currently active user permissions to manage the device. Then, unplug your device and plug it back in.

Keep reading if you're using NixOS, and feel free to skip if you go outside sometimes.

You can name the.rulesfile whatever you want, but, obviously, itneeds to come before73alphabetically. This is because fuck you, that’s why. This poses an interesting challenge on NixOS, which, in its eternal wisdom,provide only one way of adding custom rules, which writes to99-local.rules. The solution to that is to make a custom package that defines the rule at the desired location, and then extendservices.udev.packageswith your new package. Thankfully, this is easily doable with thepkgs.writeTextFilehelper, like so:

services
.
udev
.
packages

=

[


(
pkgs
.
writeTextFile

{


name

=

"
pegboard_udev
"
;


text

=

''

 ACTION=="add", SUBSYSTEM=="usb", DRIVERS=="usb", ATTRS{idVendor}=="37fa", ATTRS{idProduct}=="8201", MODE="0770", TAG+="uaccess"


''
;


destination

=

"
/etc/udev/rules.d/70-pegboard.rules
"
;


}
)


]
;

## Writing a basic driver

Okay, enough yapping. Let’s start with a basic Rust binary and immediately add therusbcrate, which will serve as a binding tolibusb.

cargo
 new gamer-driver

cd
 gamer-driver

cargo
 add rusb

To get going, we can try to get a handle on the device and get basic information about it, just likelsusb. This is explained pretty well in the crate readme, so I will not dwell on it too much. We’ll need aContext, which gives us a handyopen_device_with_vid_pidmethod that we can use to get a handle to a device.

use

rusb
::
{
Context
,
 UsbContext
}
;

const

VENDOR
:

u16

=

0x37fa
;

const

DEVICE
:

u16

=

0x8201
;

fn

main
(
)

{


let
 context
=

Context
::
new
(
)
.
expect
(
"
cannot open libusb context
"
)
;


let
 device
=
 context


.
open_device_with_vid_pid
(
VENDOR
,

DEVICE
)


.
expect
(
"
cannot get device
"
)
;


let
 descriptor
=
 device


.
device
(
)


.
device_descriptor
(
)


.
expect
(
"
cannot describe device
"
)
;


println!
(
"
{descriptor:#?}
"
)
;

}

$ cargo run

 Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.02s

 Running `target/debug/gamer-driver`

DeviceDescriptor {

 bLength: 18,

 bDescriptorType: 1,

 bcdUSB: 272,

 bDeviceClass: 0,

 bDeviceSubClass: 0,

 bDeviceProtocol: 0,

 bMaxPacketSize: 64,

 idVendor: 14330,

 idProduct: 33281,

 bcdDevice: 265,

 iManufacturer: 1,

 iProduct: 2,

 iSerialNumber: 3,

 bNumConfigurations: 1,

}

## The joy of debugging

Now that we have access to the device, we want to write a simple payload to it. For that, we first need to claim an interface. Recall that interfaces are essentially capabilities of the device, and throughlsusbwe learned that we only have one interface with the ID (bInterfaceNumber) of0. Thankfully, there’s an obviousclaim_interfacemethod on aDevice.

//
 ...

const

INTERFACE
:

u8

=

0x0
;

fn

main
(
)

{


//
 ...

 device


.
claim_interface
(
INTERFACE
)


.
expect
(
"
unable to claim interface
"
)
;

}

$ cargo run

 Compiling gamer-driver v0.1.0 (/home/ivan/Code/gamer-driver)

 Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.21s

 Running `target/debug/gamer-driver`

thread 'main' panicked at src/main.rs:15:10:

unable to claim interface: Busy

note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Ah.

So, what you just experienced is the joy oflibusberror messages. This message, at 4 characters, is in fact pretty generous - you might be greeted with a message that only saysIo, and good luck debugging that. In general,Busymeans that something is already holding the device open, so you cannot do anything with it. However, you won’t actually be told what is holding it open.

The secret is that the device is, of course, being held open by the kernel. This is the generic driver I talked about earlier. And the secret solution is to release the kernel driver, if it is currently active on the device.

This requires you to have write access to the device, so if you did not do theudevsong and dance from earlier in this article, prepare to prefix all future invocations of your driver withsudo.

fn

main
(
)

{


//
 ...


if
 device


.
kernel_driver_active
(
INTERFACE
)


.
expect
(
"
cannot get kernel driver
"
)


{

 device


.
detach_kernel_driver
(
INTERFACE
)


.
expect
(
"
cannot detach kernel driver
"
)
;


}

 device


.
claim_interface
(
INTERFACE
)


.
expect
(
"
unable to claim interface
"
)
;

}

Note that the kernel driver won’t be reattached automatically, so you might want to calldevice.attach_kernel_driver(INTERFACE)if, for some reason, you need it back.

## Sending data to the device

Surely,nowwe are ready to write out some bytes to a device?

Well, almost! If we try to naively start typing out something likedevice.write, the IDE will helpfully suggest three options:write_bulk,write_controlandwrite_interrupt. This corresponds to three out of four possible types of endpoints that the USB standard supports. Once again,USB in a NutShellcomes in clutch with an explanation of what each of the endpoint types mean. Thankfully, we can mostly skip over the implementation details, as we can once again refer to thelsusbreadout from earlier:

 Endpoint Descriptor:

 bEndpointAddress 0x82 EP 2 IN

 bmAttributes 3

 Transfer Type Interrupt

 Usage Type Data

 wMaxPacketSize 0x0040 1x 64 bytes

 bInterval 1

 Endpoint Descriptor:

 bEndpointAddress 0x02 EP 2 OUT

 bmAttributes 3

 Transfer Type Interrupt

 Usage Type Data

 wMaxPacketSize 0x0040 1x 64 bytes

 bInterval 1

In USB parlance,INis always something that the device sends to the host, andOUTis always something that the host sends to the device. Basically, since this interface has two endpoints, and only one of them is anOUTendpoint, it’s safe to assume we’re looking towrite_interrupton endpoint0x02. The peculiarities of Interrupt endpoints will absolutely come back to bite us in a couple of minutes, but for now we can keep them out of sight and out of mind.

For testing purposes, I want to make the pegboard show a solid red color. According to my earlier investigation, this means that I need to send02 00 c0, followed by 64 repeats of0f ff 0f, to an endpoint at0x02. In addition,rusbonly exposes the blocking API oflibusb, so we will also need to define a timeout after whichlibusbwill give up and error out.

use

std
::
time
::
Duration
;

//
 ...

const

ENDPOINT_OUT
:

u8

=

0x02
;

const

ENDPOINT_IN
:

u8

=

0x82
;

const

TIMEOUT
:
 Duration
=

Duration
::
from_secs
(
1
)
;

fn

main
(
)

{


//
 ...

 device


.
claim_interface
(
INTERFACE
)


.
expect
(
"
unable to claim interface
"
)
;


let
 command
:

[
u8
;

3
]

=

[
0x02
,

0x00
,

0xc0
]
;


let
 color
:

[
u8
;

3
]

=

[
0x0f
,

0xff
,

0x0f
]
;


let
 body
:

Vec
<
u8
>

=
 command


.
into_iter
(
)


.
chain
(
color
.
into_iter
(
)
.
cycle
(
)
.
take
(
192
)
)


.
collect
(
)
;

 device


.
write_interrupt
(
ENDPOINT_OUT
,

&
body
,

TIMEOUT
)


.
expect
(
"
unable to write to device
"
)
;

}

$ cargo run

 Compiling gamer-driver v0.1.0 (/home/ivan/Code/gamer-driver)

 Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.24s

 Running `target/debug/gamer-driver`

And… just like that, the pegboard now shows a solid red color! We didn’t need to worry about manually splitting packets or any of the underlying implementation, just open up a pipe and write to it! It’s that easy.

Let’s run it again to make sure it was not a fluke!

## So, about those interrupts…

Yeah, so if you happen to be following along, and you ran the same binary twice, you’ll notice that the firmware of the pegboard crashes unceremoniously, and shortly after reverts to its default animation. And if I go back to the original packet capture - or the official docs - it’s pretty obvious why: the device sends us back a response, but we never read it.

It turns out that “interrupts” are named as such for a reason, and we should probably handle them as they come in. However, the USB spec defines that thehostmust poll for interrupts. A device cannot interrupt the host by itself.

For our simple “driver”, this means we want to poll the device right after we write to it. Thankfully,rusbgives us aread_interruptmethod, and we have already sneakily defined theENDPOINT_INconstant. Let’s do just that:

fn

main
(
)

{


//
 ...

 device


.
write_interrupt
(
ENDPOINT_OUT
,

&
body
,

TIMEOUT
)


.
expect
(
"
unable to write to device
"
)
;


let

mut
 buf
=

[
0_
u8
;

64
]
;

 device


.
read_interrupt
(
ENDPOINT_IN
,

&
mut
 buf
,

TIMEOUT
)


.
expect
(
"
unable to read from device
"
)
;


dbg!
(
buf
)
;

}

Running this, we see that the contents ofbufare[130, 0, 1, 0...], which corresponds to0x82 0x00 0x01I got from the research. And since we clear the interrupt buffer every time now, we can run this binary many times to define a single solid color on the device. Neat!

## Making this better

Of course, this is… not really what you want. The device may issue more interrupts. For example, there’s a single button on the desk dock, which can be clicked, double-clicked or long-clicked, and each of those will issue a different interrupt. So what wereallywant is a background task of sort that will actively poll the device for interrupts and process them as they come in.

This is where you can get wild with async Rust,tokio, channels, and other fun stuff. That would certainly be theright wayto do it in an actual, serious driver. But to avoid getting into complexities of async Rust, let’s keep it vanilla and usestd::thread::scope.

We’ll also adjust the timeout for reading interrupts to be 1 millisecond, as requested by the device (thebIntervalvalue in thelsusbreadout). This doesn’t mean we will get an interrupt every millisecond, just that the devicecansend one at that rate. If the device sends nothing (i.e., we getErr(Timeout)), we will just continue with the loop.

Put together, that might look something like this:

use

std
::
thread
;

//
 ...

const

WRITE_TIMEOUT
:
 Duration
=

Duration
::
from_secs
(
1
)
;

const

READ_TIMEOUT
:
 Duration
=

Duration
::
from_millis
(
1
)
;

fn

main
(
)

{


//
 ...


thread
::
scope
(
|
s
|

{

 s
.
spawn
(
|
|

{


//
 Do this just once, then end the thread.

 device


.
write_interrupt
(
ENDPOINT_OUT
,

&
body
,

WRITE_TIMEOUT
)


.
expect
(
"
unable to write to device
"
)
;


}
)
;

 s
.
spawn
(
|
|

{


//
 Read interrupts until we hit Ctrl-C.


loop

{


let

mut
 buf
=

[
0_
u8
;

64
]
;


match
 device
.
read_interrupt
(
ENDPOINT_IN
,

&
mut
 buf
,

READ_TIMEOUT
)

{


Ok
(
_
)

=>

println!
(
"
Interrupt:
{}
"
,
 buf
[
0
]
)
,


Err
(
rusb
::
Error
::
Timeout
)

=>

continue
,


Err
(
e
)

=>

panic!
(
"
{e:?}
"
)
,


}


}


}
)
;


}
)
;

}

$ cargo run

 Compiling gamer-driver v0.1.0 (/home/ivan/Code/gamer-driver)

 Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.23s

 Running `target/debug/gamer-driver`

Interrupt: 130

^C

This… works! Of course, we send no more color frames to the device, so we won’t get any more interrupts, but we now have two threads, one which we can use to change the colors shown, and another which we can use to read the interrupts.

There are some quirks with this device: it seems to require a steady stream of color frames, otherwise it reverts to “offline mode” as it does not receive any new frames from the host, and the first frame’s brightness is significantly lower than the brightness of future frames. Not to mention that, despite what the official protocol documentation would have you believe, the colors seem to be in GRB instead of RGB format, and if you make the devicetoo bright, it will just hard-reset after a couple of seconds. That is, I suppose, a part of the joy of coding.

But this small proof of concept shows that writing simple device drivers is not all that hard, and that 50 lines of code can bring you quite far. Over the next few weeks I hope to polish up my proof of concept, make a small GUI for it, pack it up and share it with the two other Linux users who own this dumb thing. And I’m happy to have learned the basics of reverse-engineering a simple USB device driver, and using that as a foundation for writing my own. Even if I could have just asked for the spec earlier and not fussed with it.
