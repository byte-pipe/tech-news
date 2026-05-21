---
title: Tech specs - Flipper One Documentation
url: https://docs.flipper.net/one/general/tech-specs
date: 2026-05-20
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-05-21T12:08:09.431236
---

# Tech specs - Flipper One Documentation

## Tech Specs

### Overview
The Flipper One is a portable, handheld computer with active development. Its technical specifications are subject to change as the device evolves under the guidance of an experienced researcher.

### Device Details

* **Dimensions**: Width 155mm (6.1 inches), Height 67mm (2.64 inches), Depth 40mm (1.57 inches)
* **Weight**: Tbd grams (tbd ounces); placeholder value.
* **Materials**:
	+ Body: PC/ABS
	+ Buttons and Screen: PC/ABS
	+ Heat Sink: Anodized aluminum
	+ Bracket and Lanyard: Anodized aluminum
	+ Bumpers: Anodized aluminum
	+ Display and Audio Components: TPU monochrome LCD display, 256 x 144 pixels grayscale
* **Compatibility**:
	+ Interface: qSPI
	+ Ports:
		- Front Port
		- Back Port
		- USB C1
		- USB C2 (no clear specifications)
		- HDMI Out
		- Power Delivery (USB C) and charging
	+ MicroSD and SIM Slots

### Connectivity
The Flipper One supports various connectivity options, including:

* **Wi-Fi**: Integrated Wi-Fi module with multiple frequency bands: Wi-Fi 802.11ax, 2.4/5/6 GHz; up to 8 channels.
* **Bluetooth**: Blue-tooth module with Wi-Fi compatibility via MT7921AUN chipset
* **Gigabit Ethernet**: Twin Ethernet ports (1gbit/s) for local connection.

### Performance and Power Management

The Chip is powered by a RP2350 MCU. It features:

* **RISC CPU**: Dual ARM Cortex M33 @ 150 MHz + dual RISC CPU V hazard; up to 2.2 GHz
* **GPU**: Mali G52 MC3, OpenCL 2.1, Vulkan 1.2, NPU for low power efficiency
* **Low Power MCU**: RP2350 MCUs with Dual RISC cores; dual RISCV (16-bit) instruction processing

### Other Features

The Flipper One includes:

* **Touch Display**: HDVI out @ Full-size connector (v2.1)
* **Audio Components**: Stereo audio output through NuVoton Nau8822 speaker
* **PC/ABS Construction**: Build using anodized aluminum plates for structural integrity and durability.

**Technical Specifications** are subject to change based on future developments in the project.

## References

Please note: The technical specifications provided may not be complete or exhaustive. Additional information, such as microSD card support, Wi-Fi encryption method, and charging status, is recommended for a thorough understanding of the Flipper One's capabilities.

| Section | Value |
| --- | --- |
| Dimensions | 155mm (6.1 in), 67mm (2.64 in) - not finalized to be 40mm (1.57in), 67mm (or more, unknown origin) |
| Weight | Tbd grams; placeholder value |
| Materials | Body: PC/ABS Buttons and Screen: PC/ABS Heat Sink Anodized aluminum Bracket Lanyard Plate Bumpers Display Low-power MCU Power Distribution MicroSD Simulation Card Expansion Slot |

Flipper One Technical Details

* Specifications Provided by the original publication on Flipper One Documentation