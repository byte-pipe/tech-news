---
title: USB for Software Developers | WerWolv
url: https://werwolv.net/posts/usb_for_sw_devs/
date: 2026-04-09
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-04-10T06:02:17.912152
---

# USB for Software Developers | WerWolv

# USB for Software Developers – Summary

## Introduction
- Writing a USB driver is comparable to writing a socket‑based application, not a complex kernel task.
- The guide offers a high‑level introduction for developers with limited hardware background.
- Deeper resources exist (e.g., *USB in a Nutshell*), but this article focuses on approachability.

## The USB Device
- Uses an Android phone in Bootloader (fastboot) mode as the target device.
- Chosen because it is easy to obtain, has a simple documented protocol, and usually lacks pre‑installed drivers.
- Enter bootloader by holding a specific button combination (e.g., volume‑down while powering on).

## Enumerating the Device by Hand
- **Enumeration**: host queries the device for its descriptors; the OS normally selects a driver based on class or VID/PID.
- Vendor‑specific devices often have no driver loaded, leaving them available for custom handling.

### Basic Information
- The device is recognized as a USB device even without a driver, per the USB specification.
- `lsusb` output (Linux) shows:
  - Bus and Device numbers (physical port identifiers).
  - VID `18d1` (Google) and PID `4ee0` (Nexus/Pixel fastboot).
- VID is assigned by USB‑IF; PID is assigned by the manufacturer.

### Class and Driver Information
- `lsusb -t` displays the USB device tree:
  - Class = “Vendor Specific Class”.
  - Driver = `[none]`, indicating no kernel driver is attached.
- This situation is ideal for writing a user‑space driver.
- On Windows, similar details can be obtained via Device Manager or USB Device Tree Viewer.

## Enumerating the Device with libusb
- libusb provides a user‑space API to detect and communicate with USB devices.
- Example program workflow:
  - Initialize a libusb context.
  - Register a hot‑plug callback for VID `0x18d1` / PID `0x4ee0`.
  - Enter an event‑handling loop; on device arrival, print “Device plugged in!”.
  - Clean up by deregistering the callback and exiting libusb.
- Compiling and running the program confirms detection without any kernel code.

### Platform Notes
- **Linux**: the process works out of the box; if a driver is unexpectedly loaded, `libusb_detach_kernel_driver()` can detach it.
- **Windows**:
  - If the device presents a Microsoft OS descriptor, Windows may load `Winusb.sys`, which libusb can use directly.
  - If no driver is loaded (device shows a warning icon), tools like Zadig can replace the driver with `Winusb.sys` to enable libusb communication.
