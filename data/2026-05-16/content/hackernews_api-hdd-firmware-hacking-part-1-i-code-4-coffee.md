---
title: HDD Firmware Hacking Part 1 – I Code 4 Coffee
url: https://icode4.coffee/?p=1465
site_name: hackernews_api
content_file: hackernews_api-hdd-firmware-hacking-part-1-i-code-4-coffee
fetched_at: '2026-05-16T06:00:17.268040'
original_url: https://icode4.coffee/?p=1465
author: jsploit
date: '2026-05-15'
published_date: '2026-05-14T10:08:20-05:00'
description: HDD Firmware Hacking
tags:
- hackernews
- trending
---

Browse:
 
Home

  /  
 
HDD Firmware Hacking Part 1

## HDD Firmware Hacking Part 1

Ryan Miceli
 / 
May 14, 2026
 / 
7 Comments
 / 
Embedded
, 
Firmware
, 
HDD

Some time last year I was working on an exploit for the Xbox 360 console (which would later turn into the much anticipated softmod) and found myself in need of a way to modify the firmware for a HDD to try and exploit a race condition. This sent me down a rabbit hole of trying to modify the firmware for a few different brands of HDDs and SSDs I had on hand. In this series of blog posts I’ll cover all the work I did including: dumping and analyzing the firmware, live debugging a HDD via JTAG, modifying the drive firmware, and how I used AI to help with analysis and identifying an unknown MCU architecture.

This first post is going to focus on dumping, analyzing, and modifying HDD firmware. Everything in this post was done without the help of AI. In the next post I’ll cover how I used AI to do similar work on other HDDs/SSDs as well as using it to do black box reverse engineering on an unknown ISA, and giving Claude access to debug my hard drive.

### Background

The bug I was trying to exploit was a race condition that occurs when the console is reading data from the HDD. I needed a certain amount of time between when the read request was issued and when the drive replied in order for my exploit to trigger successfully. At the time I didn’t quite understand all the variables at play and was having difficulty exploiting the race condition in the time it took the HDD to respond. One of my initial ideas was to modify the HDD firmware to introduce a delay of a few hundred milliseconds when a specific sector is read from the drive, which would give enough time for the exploit to trigger successfully.

Over the years I had read a few posts/articles about modifying HDD firmware but nothing I could pick up and run with. Regardless, I knew this concept wasn’t new and I just needed to find a drive that was easy to start messing with. At this point in time I just needed one HDD I could use to finish developing the Xbox 360 exploit and then I’d worry about trying to expand the firmware modifications to other makes and models. As it would later turn out I found other ways to dial in my race condition attack and ended up not needing to modify the HDD firmware at all.

The idea of modifying the firmware on a HDD/SSD is very interesting to me especially from attacker and pen-testing points of view. However, I’ve never cared to venture down this rabbit hole until now because embedded devices are typically very complex under the hood and massive time-sucks to reverse engineer. Do you know how a hard drive works? At a high level sure, discs spin at high speed, magnets pull data off them, but do youreallyunderstand how they work at a micro-controller level?

I had no idea how a hard drive worked internally but I knew I had found another bug where failure to exploit it was not an option I was willing to accept. If the only thing standing in my way of exploiting this bug was a hard drive then this hard drive was going down.

## The Test Subjects

For this exploit I just needed any HDD or SSD I could easily obtain, modify, and reflash the firmware on. However, I was primarily focused on the brands of HDDs that were used for the Xbox 360 as anyone using the exploit would most likely already have one on hand. I also grabbed some Western Digital drives as I knew from some past endeavors that they have some backdoor vendor commands which could be used to get low level access to them. And lastly I grabbed a couple Samsung SSDs as I had a few of these on hand. Here are the brave test subjects that would (hopefully) survive whatever experiments I was about to do to them:

Here are the makes and models for anyone interested:

* Samsung HM020GI
* Hitachi HTS545032B9A300
* Western Digital WD3200BEVT
* Samsung PM871a

You may notice one of the drives has been thoroughly shamed and that’s due to some past grief where it was coincidentally used on a failing USB adapter and then on a computer with a failing SATA channel, and you can kinda see where this is going… The drive is in fact fully functional.

### Spinning Up

The first thing I did was research these drive models online to see if I could find firmware dumps and any information from others who’ve been down this path before. I spent quite a bit of time reading through theHDD Guruforums and found a lot of information on Western Digital (WD) drives and the Hitachi drive. I also found ablog series by MalwareTechwhere he tries to modify the firmware on a HDD and one part in particular really resonated with me as I was doing this research:

Before i started hacking I’d decided to read other people’s research to get a good idea of where to start. Resourceful, right? Well it actually turns out that most of the research I’ve based mine on was either wrong or just doesn’t apply to this hard disk.

This was my exact experience, most of the information I found were 15+ year old forum posts that were either incorrect or didn’t apply to the model HDD I had. However, there were lots of “pieces” of information I was gathering that together were starting to form a larger picture. My plan of attack for each drive was as follows:

1. Obtain a firmware dump either by finding the firmware image online or dumping it from the drive myself.
2. Getting the firmware loaded into IDA for analysis, this would also include working around any compression or encryption I encountered. If I couldn’t analyze the firmware there was basically no way I was gonna be able to make modifications for it.
3. Finding a way to flash back modified firmware. This could either be through manually programming a flash chip on the HDD logic board or using standard/backdoor commands. Not being able to write back modified firmware was an immediate show stopper for that drive.
4. Analyze the firmware and try to find the code responsible for handling read requests. The command I’m interested in is the DMA READ EXT command which is what the console uses for read requests. Somewhere in the firmware there’s likely some sort of command handler function table that would get used to handle the various ATA commands the drive supports. Finding this table would either lead me directly to the DMA READ EXT command handler, or give me a starting place to trace around and find it. This would likely be the hardest part of the process.
5. Write some patches to introduce a delay of a few hundred milliseconds when a specific sector is read from the drive.
6. Flash the now modified firmware back to the drive.

## Obtaining the Drive Firmware

One of the things I found on the HDD Guru forums was a section where people uploaded firmware dumps of various HDDs obtained with a PC-3000. If you’re not familiar withPC-3000it’s a professional grade data recovery tool that uses proprietary vendor commands to diagnose and repair HDDs, as well as dump firmware from them. I was able to find a firmware dump for the Western Digital (WD) drive on the forums, and while posting about this on twitter someone reached out and was able to use a PC-3000 they had access to and get a firmware dump of the Samsung HM020GI. I found the firmware for the Samsung PM871a SSD on the Lenovo website as part of a firmware update utility and this actually turned out to be a double whammy. Not only did I get the firmware image but by reverse engineering the update utility I could figure out the commands needed to flash new firmware to the drive. I never found the firmware for the Hitachi drive but I had enough to start with for now.

### Western Digital

Starting with the WD drive, I found a few bits of information on the format the firmware image on the HDD Guru forums, and after looking at it in a hex editor for a few minutes I was able to work out the following:

Structure of the firmware image

The format is very straight forward, essentially just a list of statically based executable/data sections in a flat file starting with the section headers. Additionally, each section header and data block have their own checksum (8-bit summation) to verify data is valid/copied correctly. I wrote a quick IDA loader plugin so I could load the firmware image and start analyzing it and that’s when I realized that all of the sections in this image except for the first one were compressed. Once of the “pieces” of info I found on the forums was that the first section is a loader stub that’s used by the MCU bootloader to decompress and load the remaining sections into memory. However, the poster declined to mention what the compression algorithm was.

At first I ran one of the compressed blocks through some tools to try and identify what the compression algorithm was but this didn’t return any fruitful results. So I loaded the first section into IDA as ARM code and started reverse engineering how it worked. A lot of the MCUs powering HDDs/SSDs are ARM based, and many of them have multiple cores that are responsible for doing different things. Luckily this WD HDD only has one ARM core which makes it a bit easier to work with. After a few minutes of reverse engineering I was able to label most of the section loading loop and identify the function responsible for decompressing data:

Disassembly of section loading function

I spent a bit of time reverse engineering the decompression routine and eventually got a working reimplementation of it. The algorithm is LZHUF but there’s a couple changes made to it which is why I wasn’t able to detect it when I ran one of the compressed blocks through an identification utility. The N constant was changed from 2048 to 4096, and the run length calculation now subtracts THRESHOLD instead of adding it:

Example of modifications to LZHUF algorithm.

After updating my IDA loader script I was able to load the entire firmware image with all the sections at the correct base addresses. The WD firmware was now ready for analysis.

### Samsung PM871a

Next up is the Samsung PM871a which I was able to find the firmware and a firmware update utility for on Lenovo’s website. This actually turned out to be a great strategy, search for firmware update utilities on OEM websites which gets you the firmware and firmware update utility that will:

1. Decrypt/deobfuscate the firmware if it’s protected.
2. Flash it to the HDD.

The firmware for Samsung SSDs are typically encrypted/obfuscated in some way and the firmware update utilities will usually decrypt/deobfuscate the firmware before sending it to the drive for flashing. For the particular SSD I was working with the firmware was obfuscated using some bit fiddling algorithm that I was able to reverse engineer out of the firmware update utility:

C

void DecodeFirmware(unsigned char* pBuffer, unsigned int Length)
{
 // Loop through the entire firmware buffer.
 for (unsigned int i = 0; i < Length; i++)
 {
 // Get the hi nibble for the current byte.
 unsigned char nibbleHi = (pBuffer[i] >> 4) & 0xF;
 
 // Do bit twiddling?
 if ((nibbleHi & 1) != 0)
 nibbleHi >>= 1;
 else
 nibbleHi = 0xF - (nibbleHi >> 1);
 
 // Mask in the new hi nibble value.
 pBuffer[i] = (pBuffer[i] & 0xF) | (nibbleHi << 4);
 }
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18

void
 
DecodeFirmware
(
unsigned
 
char
*
 
pBuffer
,
 
unsigned
 
int
 
Length
)
{
    
// Loop through the entire firmware buffer.
    
for
 
(
unsigned
 
int
 
i
 
=
 
0
;
 
i
 
<
 
Length
;
 
i
++
)
    
{
        
// Get the hi nibble for the current byte.
        
unsigned
 
char
 
nibbleHi
 
=
 
(
pBuffer
[
i
]
 
>>
 
4
)
 
&
 
0xF
;
        
        
// Do bit twiddling?
        
if
 
(
(
nibbleHi
 
&
 
1
)
 
!=
 
0
)
            
nibbleHi
 
>>
=
 
1
;
        
else
            
nibbleHi
 
=
 
0xF
 
-
 
(
nibbleHi
 
>>
 
1
)
;
        
        
// Mask in the new hi nibble value.
        
pBuffer
[
i
]
 
=
 
(
pBuffer
[
i
]
 
&
 
0xF
)
 
|
 
(
nibbleHi
 
<<
 
4
)
;
    
}
}

This particular firmware update utility can be used for a little over 2 dozen different Samsung SSD models (as well as a few dozen different DVD drive models) so harvesting information from these utilities is extremely fruitful when it comes to scaling research endeavors outwards. Next I opened the deobfuscated firmware image in a hex editor to get an idea of what I was working with. The first thing I noticed was some suspicious data in the first few kilobytes of the file that looked like it could be some sort of cryptographic signature (meaning I might not be able to modify the firmware). However, after comparing two firmware files it appeared that other than a few small changes in data/code the only notable difference was some 28 byte run at the very beginning of the file:

Comparing of the two firmware files

While it wasn’t conclusive this was a good indication that the firmware file most likely wasn’t signed with some strong public-key crypto algorithm like RSA or ECDSA. It’s also worth mentioning that the two firmware files are actually the same version but for different form factors of the Samsung PM871a, one for the 2.5″ SATA model and one for the M.2 model. So despite there being a few changes throughout the file it’s still possible some portions of it are in fact signed. The 28 byte run is an odd length for a hash or signature, it could be SHA-224 or truncated SHA-256, but we can worry about that later.

Next step was trying to identify where (if at all) the section headers were located. After loading the file into IDA as a binary file I could immediately tell the file was split into sections with different base addresses so we’ll need to find the section headers to get this loaded properly. The first 8 kilobytes of the file appear to be some meta data blocks and after that we can see this:

Hex dump of the suspected segment descriptors

The bytes in red are most definitely memory addresses for the code/data segments, how do I know? Because I’ve been staring intohex editorsthe abyss for over 20 years now and I’ve gotten incredibly good at picking apart binary file formats. Additionally these addresses line up pretty nicely with the memory map for ARM Cortex-M3 cores:

ARM Cortex-M3 memory map

After a few more minutes of staring into the abyss I was able to work out that the offset and size of each section are in intervals of 16KB blocks, and after writing another IDA loader script I had the firmware fully loaded and ready for analysis.

### Samsung HM020GI

Lastly was the Samsung HM020GI. Looking at the firmware dump for this drive in a hex editor I could clearly see plain text strings and what looked like machine code. However, despite my best attempts I could not find any architecture that this code would disassemble for. One thing that stuck out was that the entire file appear to be word flipped:

Byte flipped firmware data

This was starting to seem like it could be some extremely esoteric ISA or possibly even custom byte code that would get run through a VM baked into the MCU. For now I decided to put this HDD aside, but we’ll come back to it in part 2 so stay tuned!

## Flashing Modified Firmware

From this point on I’m only going to cover my work with the Western Digital HDD as this is the one I spent the most time on. It’s also not very interesting for you as a reader if I’m just repeating the same steps several times over for each drive I worked on. The other drives will make a come back in part 2 where I’ll cover unique research I did on each one but for now we’re going to set them aside.

There’s 3 main ways to write new firmware to a drive:

* Using the DOWNLOAD MICROCODE ATA command, this is the most common way and is supported by most (if not all?) drives.
* Back door vendor commands, typically used as a means of repair/diagnostics or by drives that primarily use service area overlays as a means of patching/updating firmware.
* Through a serial interface exposed on the drive circuit board, typically used as a means of repair/diagnostics.

### DOWNLOAD MICROCODE Command

All HDDs and SSDs communicate with a host device using some version of the ATA specification which outlines all the commands and responses used during communications. These include commands to read and write data, query and set drive information, etc. One such command is the download microcode command which is used to upload new code/firmware to the drive. You’ll typically send the command along with some additional register values to indicate the firmware size, stream the new firmware to the drive (either in chunks or through a DMA transfer), and then the drive will potentially validate the firmware received and write it to non-volatile storage. If the firmware update was successful you can power cycle the drive and you’re done, if it failed then you may have a new paper weight. You can usually recover from this but it requires varying levels of hacking on the drive and is not something a normal user would be able to do.

Most (if not all) drives should support this command and this is how most modern drives do firmware updates. All those firmware update utilities you can find on OEM websites are just streaming the new firmware through this command to the drive.

### Back Door Vendor Commands

Many Western Digital HDDs never received full firmware updates and instead relied on writing new code to the overlay modules located in the service area of the platters. The service area is a special area on the platters that’s normally inaccessible and contains information such as drive configuration data (model/serial info, geometry data, etc), SMART status data, and updated bits of firmware code. These are typically referred to as “modules” or “overlays” and there’s dozens of them located in the service area. Western Digital drives in particular like to use some of these for updated bits of code that get loaded into memory when the drive boots up.

PC-3000 software showing service area modules for a WD HDD

To access these areas there’s some back door commands you can issue to the drive that’ll let you read and sometimes write to these modules. Western Digital uses the SMART READ/WRITE LOG command which is normally used to read (and seldomly write) SMART status values. These commands take a parameter called the log address which is an 8-bit value that indicates which SMART data page you want to read/write. Many of these have predefined purposes per the ATA spec but there’s a range that’s “vendor defined” that can be used to access all sorts of repair and diagnostics commands as we’ll see later on:

ATA specification for log address values.

### Physical Serial Interface

Many HDDs have a physical serial interface that’s exposed via 4 pins next to the SATA connector which you’ve probably seen before. Those pins are for a RS232 serial port that you can connect to and issue repair/diagnostic commands to the drive. Each drive manufacturer/model will have different commands they support, some of which you can find documentation online from other reverse engineers, others you’ll need to actually dig into the firmware to figure out. For now we’re going to ignore this serial port and come back to it in part 2.

HDD serial port connection

### The Western Digital SPI Flash

My plan for reflashing the WD drive was to use the back door vendor commands to write my modified firmware image. I had already prepared a python script that could unpack, patch, and repack the firmware image, now I just needed to write a tool to write the image to the drive. However, my fear was that even if I can write new firmware successfully there’s a good chance I’m going to botch these patches on the first few attempts and could very well put the drive into a state where I couldn’t use the back door commands to reflash and recover. I was really going to need a robust recovery solution or else I could quickly brick a dozen or more drives before I make any real progress.

Luckily the WD drives have two locations where the primary firmware image is stored. The first is in internal MCU flash which is what the WD drive I had was using. The second is a SPI flash chip that’s found on certain models which overrides the internal MCU flash. Even though the model I had didn’t have the SPI flash chip populated the pads for it still existed and could be used by soldering in the SPI flash chip and a couple resistors to signal to the MCU to boot from it instead of the internal flash.

Location of the SPI flash chip.

My plan was to use the SPI flash chip for testing modified firmware and if at any point I flashed something that prevented the drive from booting or being able to reflash new images, I could use an external programmer and reflash it in-circuit. I ordered a couple suitable SPI flash chips and then moved on to analyzing the firmware while I waited for them to arrive.

## Analyzing the Firmware

The next step was going to be the hardest part of this endeavor, finding the code responsible for handling read requests. This firmware is very low level stuff, there’s no strings or useful hints I can derive information from, and it’s split between many different memory segments some of which exist outside of the firmware image. In order to find this bit of code I’m going to have to get very creative here.

### You Ever Debug a Hard Drive Before?

One of the nice things about the WD drives is that most of them expose a JTAG connection in the form of an unpopulated 38-pin MICTOR connector on the board. This means I can easily solder up a few wires and get hardware level debugging access to the MCU running the HDD. Yes you heard me right, we’re going to debug a live HDD.

JTAG wires connected to the HDD circuit board.

Being able to debug the HDD will prove invaluable as I’ll be able to set breakpoints in code, inspect memory, register state, and step through execution while sending the drive commands from a PC. However, there’s a few pain points I’ll have to work through while doing this:

* The HDD needs to be connected to a PC so I can send it ATA commands and see if my breakpoints trigger. Unfortunately I don’t have a USB adapter that supports ATA passthrough so it has to be connected directly to the PC via SATA.
* If the drive doesn’t respond back within some timeout interval Windows thinks the drive is MIA and all subsequent communications will fail until you reboot Windows. On some versions of Windows this will actually cause volmgr to BSOD the machine.
* The HDD is a bit temperamental when being debugged and sometimes you’ll put it into a state where it needs to be power cycled before it’ll function correctly.

This was the first time I ever messed with JTAG debugging so the entire process was a learning experience as I tried to find my way around. After a bit of trial and error getting OpenOCD setup with my FT232 I was able to get connected and break in:

OpenOCD connected to the HDD MCU.

Fwiw I loosely based my tap setup around what MalwareTech found in his experiments but the MCU used on the HDD I’m working with is slightly different. I don’t know if it has multiple ARM cores as I was only ever able to get the first core identified. Regardless, it was time for the next step which was writing a quick tool to send some commands to the drive.

### Vendor Specific Commands

Earlier I briefly mentioned Western Digital drives had some backdoor commands you can access through the SMART READ/WRITE LOG ATA command. These are called vendor specific commands (VSCs) which can do things like read/write firmware, RAM, overlay modules, and other repair/diagnostics related things. The one that’s most interesting right now is the read RAM command. My plan of attack is to set a memory breakpoint on some address, say 0x41414141, then issue the read RAM command with address=0x41414141 which should trigger the breakpoint. From there I can see what function is handling this VSC command (and thus the SMART READ LOG ATA command), and walk up the call stack to hopefully find some common dispatcher that’ll lead me to the function that handles read requests.

To send one of these VSCs you simply setup an ATA passthrough request which is a way to send a low level command directly to the hard drive. You fill out a structure with the values you want programmed into the ATA port registers and the HDD/SSD will attempt to perform that command. You can additionally send some extra data that’s some N sectors large. To issue a VSC we’ll setup the registers to perform a SMART WRITE LOG ATA command with the log page set to 0xBE (which is a vendor defined log page number and what WD drives use for the “backdoor”). Then we provide 1 sector worth of extra data that contains the VSC ID and any additional parameters it takes. For the read RAM command we’ll also provide the memory address and size we want read.

Illustration of an ATA passthrough command.

Here’s the C code for the function I wrote to send this VSC:

C

bool SendVSCAccessKey(HANDLE hDrive, BYTE bVscCmd, bool bWriteAccess, DWORD dwAddress = 0, DWORD dwSize = 0)
{
 DWORD BytesRead = 0;
 DWORD BufferSize = sizeof(ATA_PASS_THROUGH_EX) + 512;
 BYTE abPassthroughData[sizeof(ATA_PASS_THROUGH_EX) + 512] = { 0 };
 ATA_PASS_THROUGH_EX* pAtaPassthrough = (ATA_PASS_THROUGH_EX*)abPassthroughData;
 VSC_COMMAND_DATA* pVscCommand = (VSC_COMMAND_DATA*)(pAtaPassthrough + 1);

 // Setup the passthrough data:
 pAtaPassthrough->Length = sizeof(ATA_PASS_THROUGH_EX);
 pAtaPassthrough->AtaFlags = ATA_FLAGS_DATA_OUT;
 pAtaPassthrough->TimeOutValue = 5;
 pAtaPassthrough->DataTransferLength = 512;
 pAtaPassthrough->DataBufferOffset = sizeof(ATA_PASS_THROUGH_EX);

 // Setup port registers for SMART READ LOG command:
 IDEREGS* pRegs = (IDEREGS*)pAtaPassthrough->CurrentTaskFile;
 pRegs->bCommandReg = ATA_OP_SMART;
 pRegs->bFeaturesReg = SMART_WRITE_LOG;
 pRegs->bSectorCountReg = 1;
 pRegs->bSectorNumberReg = 0xBE; // Special WD log address
 pRegs->bCylLowReg = 0x4F;
 pRegs->bCylHighReg = 0xC2;
 pRegs->bDriveHeadReg = 0xA0;

 // Setup the VSC command data:
 pVscCommand->CommandId = bVscCmd;
 pVscCommand->Mode = bWriteAccess == true ? VSC_MODE_WRITE : VSC_MODE_READ;
 pVscCommand->ReadWriteRam.Address = dwAddress;
 pVscCommand->ReadWriteRam.Length = dwSize;

 // Send the command to the drive.
 if (DeviceIoControl(hDrive, IOCTL_ATA_PASS_THROUGH, pAtaPassthrough, BufferSize, 
 pAtaPassthrough, BufferSize, &BytesRead, nullptr) == FALSE)
 {
 wprintf(L"SendVSCAccessKey failed 0x%08x\n", GetLastError());
 return false;
 }

 // Check for any errors.
 OUT_REGS* pOutRegs = (OUT_REGS*)pAtaPassthrough->CurrentTaskFile;
 if ((pOutRegs->bStatusReg & 1) != 0)
 {
 wprintf(L"SendVSCAccessKey failed drive returned 0x%04x\n", WD_ERROR_CODE(pOutRegs));
 return false;
 }

 return true;
}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49

bool
 
SendVSCAccessKey
(
HANDLE 
hDrive
,
 
BYTE
 
bVscCmd
,
 
bool
 
bWriteAccess
,
 
DWORD 
dwAddress
 
=
 
0
,
 
DWORD 
dwSize
 
=
 
0
)
{
    
DWORD 
BytesRead
 
=
 
0
;
    
DWORD 
BufferSize
 
=
 
sizeof
(
ATA_PASS_THROUGH_EX
)
 
+
 
512
;
    
BYTE
 
abPassthroughData
[
sizeof
(
ATA_PASS_THROUGH_EX
)
 
+
 
512
]
 
=
 
{
 
0
 
}
;
    
ATA_PASS_THROUGH_EX
*
 
pAtaPassthrough
 
=
 
(
ATA_PASS_THROUGH_EX
*
)
abPassthroughData
;
    
VSC_COMMAND_DATA
*
 
pVscCommand
 
=
 
(
VSC_COMMAND_DATA
*
)
(
pAtaPassthrough
 
+
 
1
)
;
 
    
// Setup the passthrough data:
    
pAtaPassthrough
->
Length
 
=
 
sizeof
(
ATA_PASS_THROUGH_EX
)
;
    
pAtaPassthrough
->
AtaFlags
 
=
 
ATA_FLAGS_DATA_OUT
;
    
pAtaPassthrough
->
TimeOutValue
 
=
 
5
;
    
pAtaPassthrough
->
DataTransferLength
 
=
 
512
;
    
pAtaPassthrough
->
DataBufferOffset
 
=
 
sizeof
(
ATA_PASS_THROUGH_EX
)
;
 
    
// Setup port registers for SMART READ LOG command:
    
IDEREGS
*
 
pRegs
 
=
 
(
IDEREGS
*
)
pAtaPassthrough
->
CurrentTaskFile
;
    
pRegs
->
bCommandReg
 
=
 
ATA_OP_SMART
;
    
pRegs
->
bFeaturesReg
 
=
 
SMART_WRITE_LOG
;
    
pRegs
->
bSectorCountReg
 
=
 
1
;
    
pRegs
->
bSectorNumberReg
 
=
 
0xBE
;
     
// Special WD log address
    
pRegs
->
bCylLowReg
 
=
 
0x4F
;
    
pRegs
->
bCylHighReg
 
=
 
0xC2
;
    
pRegs
->
bDriveHeadReg
 
=
 
0xA0
;
 
    
// Setup the VSC command data:
    
pVscCommand
->
CommandId
 
=
 
bVscCmd
;
    
pVscCommand
->
Mode
 
=
 
bWriteAccess
 
==
 
true
 
?
 
VSC_MODE_WRITE
 
:
 
VSC_MODE_READ
;
    
pVscCommand
->
ReadWriteRam
.
Address
 
=
 
dwAddress
;
    
pVscCommand
->
ReadWriteRam
.
Length
 
=
 
dwSize
;
 
    
// Send the command to the drive.
    
if
 
(
DeviceIoControl
(
hDrive
,
 
IOCTL_ATA_PASS_THROUGH
,
 
pAtaPassthrough
,
 
BufferSize
,
 
        
pAtaPassthrough
,
 
BufferSize
,
 
&
BytesRead
,
 
nullptr
)
 
==
 
FALSE
)
    
{
        
wprintf
(
L
"SendVSCAccessKey failed 0x%08x\n"
,
 
GetLastError
(
)
)
;
        
return
 
false
;
    
}
 
    
// Check for any errors.
    
OUT_REGS
*
 
pOutRegs
 
=
 
(
OUT_REGS
*
)
pAtaPassthrough
->
CurrentTaskFile
;
    
if
 
(
(
pOutRegs
->
bStatusReg
 
&
 
1
)
 
!=
 
0
)
    
{
        
wprintf
(
L
"SendVSCAccessKey failed drive returned 0x%04x\n"
,
 
WD_ERROR_CODE
(
pOutRegs
)
)
;
        
return
 
false
;
    
}
 
    
return
 
true
;
}

With everything setup I set a memory access breakpoint for the address0x41414141and then ran my test app to issue the read RAM VSC to the drive. The breakpoint triggered and the debugger broke in:

GDB output from the breakpoint.

Dumping the registers I was able to see the address of the instruction reading from0x41414141was at0xFFE1D780which was inside of the firmware code.

### Into the Belly of the Beast

After a few minutes of poking around the function that triggered the breakpoint I was able to clearly see how it was loading the parameters from the VSC buffer and performing the memory read operation:

Disassembly for the read RAM command handler.

Tracing up the stack I was able to identify a lookup table for the VSCs which contained 67 entries in total, a bit more than I was expecting to see.

Function handler table for VSCs.

While I was debugging the drive I dumped the first 1Kb of stack data so I could use it to walk up the call stack as there were a few indirect calls via function tables. For the next steps I modified my VSC test app and added a new option to read a specific sector from the drive. Then I placed a couple breakpoints in the functions I identified in the call stack to the_vsc_read_write_memoryfunction and ran the read sector test. However, none of my breakpoints were hitting. After a bunch of trial and error I could see the chain of functions leading up to the VSC handler was only triggering breakpoints for the SMART READ LOG, SMART WRITE LOG, and IDENTIFY commands. The DMA READ EXT command from the read sector test was not triggering anything which meant it was being handled elsewhere.

Looking around the functions leading up to the VSC handlers I could see a few memory addresses that were used quite often. They were arrays of data, and searching across the whole firmware image they were used all over the place. I decided to dump these regions of memory to see what was there. I was hoping I’d find data related to the port registers/ATA command being handled which I could use to trace down the code for handling read requests. One of these regions in particular is an array of 40 elements each 16 bytes in size. After poking around the code to see how the fields were laid out I wrote a quick python script to print out each element:

Unknown array data printed out.

After a few minutes of analyzing this data (aka staring into the abyss) and poking at more memory on the drive I was able to determine that the first column is a pointer to some additional data I couldn’t make heads or tails of, and the second column was a function pointer. Looking at each of these function pointers in IDA I could see some of them were in the call stack that leads up to the VSC handler. It seemed like this array was a list of requests to be processed and entries with a valid address in the second column pointed to the function that likely handled the request.

The next step was to see if requests for sector reads used the function pointer field. I ran the read sector test about 2 dozen times to try and “poison” this request table in hopes it would make it obvious which entries were for the read requests, and sure enough we had a winner:

Requests for DMA READ EXT command.

I placed a breakpoint on this function and reran the read sector test and sure enough it was hitting! There was only one problem, this function wasn’t in any of the address ranges for the firmware image, it was somewhere else…

### Where the FSCK is this code?

Earlier I mentioned there’s a special service area of the platters that’s used to store additional data known as overlay modules, and that Western Digital drives like to use them to store additional code. That’s where the code containing this function lives. When the drive boots up it starts in the MCU bootloader which is responsible for copying a special bootstrap section of the firmware into RAM and executing it. The firmware bootstrap then decompresses/copies all remaining sections in the firmware image into RAM at their respective base addresses. At some later point in the bootup process the overlay modules containing more executable code are loaded into memory.

Memory map showing locations of firmware and overlay modules.

These overlay modules can be dumped using some more VSCs but rather than spend time trying to figure that out I decided to just dump the region of RAM containing the code to a file once the drive was fully booted. Later on I did find out that the overlay module containing the code is number 0x11 but that’s not really important. Now for the last step, writing a patch for this code to introduce a small delay when reading a specific sector.

## Patching the Firmware

Since the code I need to patch lives in an overlay module this makes patching it slightly more complicated as it’s more difficult to recover from a bad patch than if it were in external SPI flash. However, now that I could just modify RAM contents using the VSCs my plan was to just hot patch the code in memory until I had working modifications and worry about writing them back to the platter later on.

With the read sector code dumped and loaded into IDA I began analyzing it and planning out how I was going to hook it. Eventually I’d need to figure out what sector(s) the code is trying to read, as I only want to introduce the delay for one specific sector and not every read operation. For now I decided to worry about that detail later and just get the hook written so I could make sure the PoC for the exploit actually worked, otherwise all this was all pointless. After analyzing the code a bit I found a suitable place to hook:

Disassembly of the read sector functions.

Here we can see the main handler functionsub_16A5Eperforms a loop and each iteration callssub_1671Cwhich actually handles the read request. TheSataRequestArrayis the 40 element array from earlier that contained the function pointers for each request. This loop starts with the initial read request entry and will continue processing requests in the array so long as the Unk4 field is not 0xFF. I guess large requests can be split up into multiple smaller requests or something, I’m not entirely sure… As for placing a hook I decided to place it a few instructions intosub_1671Cas it was a little easier than trying to fit it into the loop body. After a bit of trial and error I ended up with the following assembly code:

R

.syntax unified

# Timing related variables to control the delay:
.set F_CPU, 10000000 # CPU frequency
.set MS_DELAY, 200 # 200ms delay

# ============================================================================
# Our code cave
# ============================================================================

 .long 0xFFEAB600
 .long (9f - 0f)
0:
 # Call our hook.
 push {r0-r7, lr}
 blx Hook_SataDmaRead
 pop {r0-r7, lr}
 
 # Replace instructions we overwrote.
 movs r7, r0
 lsls r0, r0, #4
 adds r5, r0, r1
 ldrb r1, [r5, #0xD]
 sub sp, sp, #0x1C
 str r1, [sp, #0xC]
 ldrb r0, [r5, #0xE]
 
 # Trampoline back.
 ldr lr, =0x0001672E+1
 bx lr
 
 Hook_SataDmaRead:
 
 # Setup delay counter.
 ldr r3, =(MS_DELAY * F_CPU / 1000)
 
 Hook_SataDmaRead_loop:
 
 # Spin until the counter is 0.
 sub r3, r3, #1
 bne Hook_SataDmaRead_loop
 
 bx lr
 
 .pool
9:

# ============================================================================
# Hook the sata DMA request handler
# ============================================================================

 .long 0x00016720
 .long (9f - 0f)
0:
 .thumb_func
 ldr r7, =0xFFEAB600
 bx r7
 
 .pool
9:

.long 0xFFFFFFFF

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62

.
syntax 
unified
 
# Timing related variables to control the delay:
.
set 
F_CPU
,
                 
10000000
        
# CPU frequency
.
set 
MS_DELAY
,
              
200
             
# 200ms delay
 
# ============================================================================
# Our code cave
# ============================================================================
 
    
.
long
 
0xFFEAB600
    
.
long
 
(
9f
 
-
 
0f
)
0
:
        
# Call our hook.
        
push
    
{
r0
-
r7
,
 
lr
}
        
blx
     
Hook_SataDmaRead
        
pop
     
{
r0
-
r7
,
 
lr
}
        
        
# Replace instructions we overwrote.
        
movs    
r7
,
 
r0
        
lsls    
r0
,
 
r0
,
 
#4
        
adds    
r5
,
 
r0
,
 
r1
        
ldrb    
r1
,
 
[
r5
,
 
#0xD]
        
sub     
sp
,
 
sp
,
 
#0x1C
        
str     
r1
,
 
[
sp
,
 
#0xC]
        
ldrb    
r0
,
 
[
r5
,
 
#0xE]
        
        
# Trampoline back.
        
ldr     
lr
,
 
=
0x0001672E
+
1
        
bx      
lr
        
    
Hook_SataDmaRead
:
    
        
# Setup delay counter.
        
ldr     
r3
,
 
=
(
MS_DELAY
 
*
 
F_CPU
 
/
 
1000
)
        
    
Hook_SataDmaRead_loop
:
    
        
# Spin until the counter is 0.
        
sub     
r3
,
 
r3
,
 
#1
        
bne     
Hook_SataDmaRead_loop
        
        
bx      
lr
        
        
.
pool
9
:
 
# ============================================================================
# Hook the sata DMA request handler
# ============================================================================
 
    
.
long
 
0x00016720
    
.
long
 
(
9f
 
-
 
0f
)
0
:
        
.
thumb_func
        
ldr     
r7
,
 
=
0xFFEAB600
        
bx      
r7
        
        
.
pool
9
:
 
.
long
 
0xFFFFFFFF

This assembly code inserts a small hook insub_1671Cthat jumps to a code cave I placed in some unused section of RAM, and tries to stall for ~200ms. The delay calculation is based on some guess work math and isn’t scientifically accurate but it’s good enough. With this compiled I modified my test app to perform the following test:

1. Loops 10 times and reads a specific sector, computes the average read time based on the times for each iteration.
2. Writes my patches to RAM thus introducing a ~200ms delay for each read operation.
3. Repeat step 1 and compute new average read time.

After running the app I got the following results:

Output from the test app.

The first thing we notice is that the delay is not ~200ms but more like ~450, like I said the math was guess work and not scientifically accurate… The second thing we can see is all the read times except for the first in the clean test are 0ms. This is likely because we’re hitting cache and thus the drive didn’t need to seek and pull the data off the platter. For the delay test we can see the first iteration the time is also 0ms, I’m not entirely sure why but likely caching behavior as well. The rest of the read test times are all delayed which is exactly what I needed. Now it was time to test this top down with the exploit I was developing and see if the delayed read times would allow it to trigger successfully.

## Task Failed Successfully

After a few minutes of remember how this exploit actually worked and prepping new files my test setup was ready to go. The setup for this test involves a few pieces but is overall quite simple:

* I have a completely unmodified HDD that I’m going to power externally and pre-patch the code in RAM with my delayed read patch. This makes it easier to test without having to worry about writing my patches back to the drive firmware/overlay modules just yet.
* The HDD will be connected to an Xbox 360 via SATA (data cable only). When the console boots up it’ll try to read a specific sector off the HDD. While this happens there’s some “hacking” that’s going on in the background (you’ll find out what this is in a future blog post).
* If the read operation takes long enough my exploit should trigger and the shell code that runs should lite up the console’s ring of light in full orange to indicate it worked.

However, before I did this I wanted to do what any good fake scientist would do and run a control test. That is, boot the console without any modifications to the HDD code to make sure the exploit still failed to trigger. I’d probably run several iterations of booting with no HDD modifications, making sure the exploit failed, then booting with patched HDD code and making sure the exploit triggered. This would help build confidence in how effective the delayed read patches were.

Now imagine my surprise after working 20 hours a day for 7 days straight and having been awake for almost 30 hours at the moment of this test, when I booted the console with no HDD modifications and the exploit triggered successfully. I thought it must have been a fluke, the planets must be aligned right now or something. I power cycled the console several times and the exploit triggered almost every single time despite the HDD running with no modifications applied. I even power cycled the HDD a few times just to make sure. I decided this side quest was over, time to sleep, when I awoke I would research why the exploit suddenly decided to start working.

## Conclusion

In the days following this work I’d come to better understand all the variables surrounding the Xbox 360 exploit and never ended up needing to modify the HDD firmware. I was able to get it to work just fine with every HDD I had on hand, the only exception were SSDs which reply too fast for the exploit to trigger reliably. This was a fun adventure into the depths of embedded devices, I learned a lot and it helped me become more confident in reverse engineering low level embedded devices. Unfortunately I still have no idea how a hard drive works. There’s definitely more I would have liked to look into out of pure curiosity but without any real motivation to do so I shelved all this work. However, while messing around with AI I decided to pick some of it up again and see how well AI would do at block box analysis of embedded devices, so stay tuned for part 2!

Firmware analysis for hard drives is an interesting topic that I’ve only seen talked about once or twice despite many people having done exactly what I did before. There’s quite a bit of information available for older HDDs if you’re willing to scour through decades of vague and incorrect forum posts, but nothing that will paint a complete picture. In particular Travis Goodspeed and Sprite (Jeroen Domburg) have some interesting publications on the subject (I particularly like the anti-forensics work done by Travis). I think the reason you don’t see more information on this topic is because people were afraid it would help bad actors create malware. There’s some merit here but as you’ll see in part 2 when using AI to help with analysis this becomes a pretty moot point. Not to mention that HDD malware already exists (thanks NSA!).

Rather than keep this topic in obscurity I decided to open source the IDA and firmware related scripts I wrote to help others start looking into HDD firmware. I’m interested to see what other people find in these devices and would love to see things like backdoor commands documented, tools to try and fingerprint firmware, and maybe even decompilation of firmware (even though it’s completely pointless and I would never trust it anyway). You can find all my work on myGitHubwhich I’ll update again when part 2 is out.

Tags: 
embedded
, 
firmware
, 
hdd
, 
jtag
, 
reverse engineering
, 
ssd

← Hacking the Xbox 360 Hypervisor Part 2: The Bad Update Exploit