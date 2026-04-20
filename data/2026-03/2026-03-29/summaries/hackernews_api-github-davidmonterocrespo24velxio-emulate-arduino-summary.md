---
title: GitHub - davidmonterocrespo24/velxio: Emulate Arduino, ESP32 & Raspberry Pi. in your browser. Write code, compile, and run on 19 real boards — Arduino...
url: https://github.com/davidmonterocrespo24/velxio
date: 2026-03-28
site: hackernews_api
model: gpt-oss:120b-cloud
summarized_at: 2026-03-29T01:03:36.845416
---

# GitHub - davidmonterocrespo24/velxio: Emulate Arduino, ESP32 & Raspberry Pi. in your browser. Write code, compile, and run on 19 real boards — Arduino...

# Velxio: Arduino & Embedded Board Emulator

## Overview
- Fully local, open‑source multi‑board emulator that runs entirely in the browser.
- Write Arduino C++ or Python, compile, and simulate with real CPU emulation and more than 48 interactive electronic components.
- Supports 19 boards across five CPU architectures: AVR8, ARM Cortex‑M0+, RISC‑V RV32IMC/EC, Xtensa LX6/LX7, and ARM Cortex‑A53.

## Access & Deployment
- Live demo: https://velxio.dev (no installation required).
- Self‑host with Docker: `docker run -d -p 3080:80 ghcr.io/davidmonterocrespo24/velxio:master` then open http://localhost:3080.

## Funding
- Project is free and open‑source.
- Sponsorship via GitHub Sponsors (preferred) or PayPal helps cover server costs, library maintenance, and further development.

## Screenshots (described)
- Raspberry Pi Pico ADC test with two potentiometers, Serial Monitor output, and compilation console.
- Arduino Uno driving an ILI9341 240×320 TFT display via SPI, rendering real‑time graphics.
- Library Manager loading the full Arduino library index for browsing and installation.
- Component Picker showing 48 available components with visual previews and filters.
- Multi‑board simulation of Raspberry Pi 3 and Arduino running simultaneously, connected via serial.
- ESP32 simulation with an HC‑SR04 ultrasonic sensor using real Xtensa emulation via QEMU.

## Supported Boards
- **AVR8 (browser)** – Arduino Uno, Nano, Mega 2560, ATtiny85, Leonardo, Pro Mini (avr8js, C++).
- **RP2040 (browser)** – Raspberry Pi Pico, Pico W (rp2040js, C++).
- **Xtensa (QEMU backend)** – ESP32 DevKit C, ESP32‑S3, ESP32‑CAM, Seeed XIAO ESP32‑S3, Arduino Nano ESP32 (QEMU, C++).
- **RISC‑V (browser)** – ESP32‑C3 DevKit, Seeed XIAO ESP32‑C3, ESP32‑C3 SuperMini, CH32V003 (RiscVCore.ts, C++).
- **ARM Cortex‑A53 (QEMU backend)** – Raspberry Pi 3B (QEMU, Python).

## Key Features

### Code Editing
- Monaco editor with syntax highlighting, autocomplete, minimap, and dark theme.
- Multi‑file workspace supporting .ino, .h, .cpp, and .py files.
- Arduino compilation via arduino‑cli backend, producing .hex/.bin files.
- Toolbar buttons for compile, run, stop, and reset with status messages.
- Resizable compilation console displaying full compiler output, warnings, and errors.

### Multi‑Board Simulation

#### AVR8 (Arduino Uno, Nano, Mega, ATtiny85, Leonardo, Pro Mini)
- Native‑speed ATmega/ATtiny emulation via avr8js (~60 FPS).
- Full GPIO, timers, USART, ADC, SPI, and I2C support.
- Functions such as `millis()`, `delay()`, `analogRead()`, `analogWrite()`, and serial communication work as on real hardware.

#### RP2040 (Raspberry Pi Pico, Pico W)
- 133 MHz ARM Cortex‑M0+ emulation via rp2040js.
- 30 GPIO pins, dual UARTs, 12‑bit ADC (including temperature sensor), two I2C buses, two SPI buses, PWM on any pin.
- WFI optimization skips idle time; oscilloscope provides ~8 ns resolution timestamps.

#### ESP32 / ESP32‑S3 (Xtensa QEMU)
- Dual‑core Xtensa LX6/LX7 emulation via QEMU lcgamboa.
- 40 GPIO pins, three UARTs, 12‑bit ADC, I2C, SPI, RMT/NeoPixel decoder, 16‑channel LEDC/PWM, Wi‑Fi emulation (SLIRP NAT).
- Requires Arduino‑ESP32 2.0.17 (IDF 4.4.x) for compatibility.

#### ESP32‑C3 / XIAO‑C3 / SuperMini / CH32V003 (RISC‑V)
- Browser‑based RISC‑V RV32IMC/EC emulation via RiscVCore.ts.
- Full GPIO, UART, ADC, I2C, SPI, PWM, and Wi‑Fi support.

#### Raspberry Pi 3B (ARM Cortex‑A53 QEMU)
- Full Linux environment emulated with QEMU, supporting Python development.

## Documentation
- Detailed technical notes are available in the `docs/` folder (e.g., `RP2040_EMULATION.md`, `ESP32_EMULATION.md`).

## Repository Structure
- Organized into `backend`, `frontend`, `scripts`, `test`, `tools`, `wokwi-libs`, Docker configuration files, and supporting documentation.
