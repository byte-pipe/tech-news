---
title: I made my VM think it has a CPU fan | mindless-area
url: https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html
site_name: hackernews
fetched_at: '2025-06-30T07:04:39.831055'
original_url: https://wbenny.github.io/2025/06/29/i-made-my-vm-think-it-has-a-cpu-fan.html
author: Petr Beneš
date: '2025-06-30'
description: '...so the malware would finally shut up and run'
---

## Why bother?

Some malware samples are known to do various checks to determine if they are
running in a virtual machine. One of the common checks is to look for
the presence of certain hardware components that are typically not emulated
in virtualized environments. One such component is theCPU fan.
One of the observed ways malware checks for the presence of a CPU fan is by
looking for theWin32_Fanclass in WMI:

wmic path Win32_Fan get *

And the reason they do this is they want to avoid running
in virtual machines, because they want to complicate the analysis process
for security researchers.

There are plenty of ways for malware to detect if it is running in a VM.
In fact, there are plenty of WMI classes that can reveal the presence of
virtual hardware, such asWin32_CacheMemory,Win32_VoltageProbe, andmany others.

In this post, I will be focusing on the CPU fan. Just because I like the idea
making a virtual machine think it has it. However, the same approach can
be applied to other hardware components and WMI classes as well.

## How the computer knows it has a CPU fan?

The computer knows it has a CPU fan by reading theSMBIOSdata.

How do I know that?By googling.

Win32_Faninstances are provided byWindows\System32\wbem\cimwin32.dll.
If you disassemble it you will see that it reads SMBIOS data (specifically
entries with type 27) to get fan device information.

And indeed, if you disassemblecimwin32.dll, you will find exactly that:

Your first impulse might be to use DLL hooking and patch thecimwin32.
But that’s smol pp way of thinking. We can do better.

## Type 27

The SMBIOS type 27 is defined as“Cooling Device”in theSystem Management BIOS Reference Specification:

We can dump the SMBIOS data using thedmidecodeutility:

root@host:/# dmidecode -t27 -u
# dmidecode 3.3
Getting SMBIOS data from sysfs.
SMBIOS 3.4 present.

Handle 0x1B00, DMI type 27, 15 bytes
 Header and Data:
 1B 0F 00 1B 00 1C 65 00 00 DD 00 00 E0 15 01
 Strings:
 43 50 55 20 46 61 6E 00
 CPU Fan

By default, thedmidecodeutility will interpret the data and display it in a
more human-readable format:

root@host:/# dmidecode -t27
# dmidecode 3.3
Getting SMBIOS data from sysfs.
SMBIOS 3.4 present.

Handle 0x1B00, DMI type 27, 15 bytes
Cooling Device
 Temperature Probe Handle: 0x1C00
 Type: Chip Fan
 Status: OK
 OEM-specific Information: 0x0000DD00
 Nominal Speed: 5600 rpm
 Description: CPU Fan

## Setting custom SMBIOS data in Xen

At the time of writing, the only available resource I found on how to set custom
SMBIOS data in Xen is thisalmost 10 years old mcnewton’s post. I recommend
reading it, as it exactly describes the struggle I had when figuring this out.

In short, you can set custom SMBIOS data in Xen by setting thesmbios_firmwareoption in the domain configuration file to the path to a file containing
the SMBIOS data.

So, let’s create a file namedsmbios.binwith the following byte content:

1B 0F 00 1B 00 1C 65 00 00 DD 00 00 E0 15 01 43
50 55 20 46 61 6E 00
00

Note that the content is same as the output ofdmidecode -t27 -uabove,
but with additional00byte at the end, because the SMBIOS specification
requires it.

In theXen domain configuration file documentation, we can also find this:

Since SMBIOS structures do not present their overall size, each entry in the
file must be preceded by a 32b integer indicating the size of the following
structure.

Our structure is 24 bytes long, so we need to prepend the content with18 00 00 00(24 in little-endian):

18 00 00 00
 1B 0F 00 1B 00 1C 65 00 00 DD 00 00
E0 15 01 43 50 55 20 46 61 6E 00 00

Now we can set thesmbios_firmwareoption in the Xen domain configuration file
to the path to this file:

smbios_firmware

=

"/path/to/smbios.bin"

Let’s save the configuration file and start our Windows domain.

root@host:/# xl create /path/to/windows/domain.cfg

And let’s check if the CPU fan is now present in the Windows VM:

PS C:\> wmic path Win32_Fan get *
No Instance(s) Available.

Oh noes. Something’s wrong.

### The Betrayal

I missed one important detail in the documentation of thesmbios_firmwareoption:

smbios_firmware=”STRING”

Specifies a path to a file that contains extra SMBIOS firmware …Not all predefined structures can be overridden, only the following types:
0, 1, 2, 3, 11, 22, 39. The file can also …

Frankly, I didnotmiss this at first. I just hoped that what I was trying to
do was not“overriding”the predefined structure.

Because Xen (or ratherhvmloader)does not define it.

So, before defining it myself, I tried to find out if there was any other poor
soul who tried to do the same thing before me. And to my disappointment, therewas. Right in thexen-devel patch archive.

Why it was my disappointment, you may ask? Because after reading the response
to the patch, I felt the frustration of the author. But that’s for another story.

Anyway, the patch was rejected, but it’s small and simple, so it’s easy
to apply it to the Xen source code.

### Type 28, too

After applying the patch and recompiling Xen, I was still gettingNo Instance(s) Availableerror when trying to query theWin32_Fanclass.

It didn’t make sense to me, so I dumped the SMBIOS data from the VM, to check
whether the type 27 was present (dmidecodeis available on Windows, too!):

PS C:\> .\dmidecode -t27
# dmidecode 3.5
SMBIOS 2.4 present.

Handle 0x1B00, DMI type 27, 15 bytes
Cooling Device
 Temperature Probe Handle: 0x1C00
 Type: Chip Fan
 Status: OK
 OEM-specific Information: 0x0000DD00
 Nominal Speed: 5600 rpm
 Description: CPU Fan

It was there! But why was it not showing up in WMI? I noticed this line:

 Temperature Probe Handle: 0x1C00

This line indicates that the cooling device (CPU fan) is associated with a
temperature probe, which is another SMBIOS type (type 28). However, the
temperature probe was not defined in the SMBIOS data:

PS C:\> .\dmidecode -t28
# dmidecode 3.5
SMBIOS 2.4 present.

That’s it.

One more table to fake.

So let’s shut down the VM and dump the type 28 data from the host:

root@host:/# dmidecode -t28
# dmidecode 3.3
Getting SMBIOS data from sysfs.
SMBIOS 3.4 present.

Handle 0x1C00, DMI type 28, 22 bytes
Temperature Probe
 Description: CPU Thermal Probe
 Location: Processor
 Status: OK
 Maximum Value: 0.0 deg C
 Minimum Value: 0.0 deg C
 Resolution: 0.000 deg C
 Tolerance: 0.0 deg C
 Accuracy: 0.00%
 OEM-specific Information: 0x0000DC00
 Nominal Value: 0.0 deg C

And again, the byte representation:

root@host:/# dmidecode -t28 -u
# dmidecode 3.3
Getting SMBIOS data from sysfs.
SMBIOS 3.4 present.

Handle 0x1C00, DMI type 28, 22 bytes
 Header and Data:
 1C 16 00 1C 01 63 00 00 00 00 00 00 00 00 00 00
 00 DC 00 00 00 00
 Strings:
 43 50 55 20 54 68 65 72 6D 61 6C 20 50 72 6F 62
 65 00
 CPU Thermal Probe

Therefore, this is the content we need to append to oursmbios.binfile
(again, mind the extra00byte at the end):

1C 16 00 1C 01 63 00 00 00 00 00 00 00 00 00 00
00 DC 00 00 00 00 43 50 55 20 54 68 65 72 6D 61
6C 20 50 72 6F 62 65 00
00

Oh right! We need to prepend the size of the structure, which is 41 bytes this
time (0x29 in hex):

29 00 00 00
 1C 16 00 1C 01 63 00 00 00 00 00 00
00 00 00 00 00 DC 00 00 00 00 43 50 55 20 54 68
65 72 6D 61 6C 20 50 72 6F 62 65 00 00

So, the final content of oursmbios.binfile should look like this:

18 00 00 00
 1B 0F 00 1B 00 1C 65 00 00 DD 00 00
E0 15 01 43 50 55 20 46 61 6E 00 00
29 00 00 00

1C 16 00 1C 01 63 00 00 00 00 00 00 00 00 00 00
00 DC 00 00 00 00 43 50 55 20 54 68 65 72 6D 61
6C 20 50 72 6F 62 65 00 00

### Xth Time’s the Charm

Let’s save the file and start our Windows domain again:

root@host:/# xl create /path/to/windows/domain.cfg

And let’s check if the CPU fan is now present in the Windows VM:

PS C:\> wmic path Win32_Fan get Description,Status
Description Status
Cooling Device OK

Yay! The VM now thinks it has a CPU fan!

If you’re wondering why I didn’t use*in thewmiccommand, it’s because
theWin32_Fanclass has*many*properties, and I wanted to keep the output
short and sweet.wmic path Win32_Fan get *would work just as well.

## Setting custom SMBIOS data in QEMU/KVM

If you’re using QEMU/KVM instead of Xen, your life is much easier. You don’t
need to patch anything. You can set custom SMBIOS data using the-smbiosoption:

qemu-system-x86_64 ...
-smbios

file
=
/path/to/smbios.bin

Or, if you’re using libvirt:


<qemu:commandline>


<qemu:arg

value=
'-smbios'
/>


<qemu:arg

value=
'file=/path/to/smbios.bin'
/>


</qemu:commandline>

However! Remember how Xen required those 32-bit integers indicating the
structure sizes? QEMU does not require them, so you can just use the raw data
without prepending the size:

1B 0F 00 1B 00 1C 65 00 00 DD 00 00 E0 15 01 43
50 55 20 46 61 6E 00 00 1C 16 00 1C 01 63 00 00
00 00 00 00 00 00 00 00 00 DC 00 00 00 00 43 50
55 20 54 68 65 72 6D 61 6C 20 50 72 6F 62 65 00
00

That’s it! QEMU will automatically handle rest of the important SMBIOS entries
for you.

However, if you’re wondering whether you could just take the host’s SMBIOS data
and use it in the VM, the answer isyes. You can try that on your own:

cat
 /sys/firmware/dmi/tables/DMI
>
 /path/to/smbios.bin

## References

* Xen domain configuration file syntax:https://xenbits.xen.org/docs/unstable/man/xl.cfg.5.html
* mcnewton’s notes - Setting custom SMBIOS data in Xen DomUs:https://notes.asd.me.uk/2015/12/04/setting-custom-smbios-data-in-xen-domus/
* [XEN PATCH] tools/firmware/hvmloader/smbios.c: Add new SMBIOS tables (7,8,9,26,27,28):https://old-list-archives.xen.org/archives/html/xen-devel/2022-01/msg00725.html
* System Management BIOS Reference Specification:https://www.dmtf.org/sites/default/files/standards/documents/DSP0134_3.7.1.pdf
* QEMU Anti Detection patches:https://github.com/zhaodice/qemu-anti-detection

Share:

X (Twitter)

Facebook

LinkedIn

* Previous Post
