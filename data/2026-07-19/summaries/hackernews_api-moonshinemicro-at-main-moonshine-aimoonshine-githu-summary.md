---
title: moonshine/micro at main · moonshine-ai/moonshine · GitHub
url: https://github.com/moonshine-ai/moonshine/tree/main/micro
date: 2026-07-14
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-07-19T11:30:07.067156
---

# moonshine/micro at main · moonshine-ai/moonshine · GitHub

**Moonshine Micro - Overview**

* Moonshine is an open-source AI toolkit for building real-time voice agents and applications
* Designed specifically for embedded system processors like microcontrollers and DSPs, such as Raspberry Pi RP2350
* Uses the RP2350 as its reference platform and provides voice-activity detection, command recognition, and neural speech synthesis

**Architecture**

* Voice-activity detection, command recognition, and neural speech synthesis are integrated into a single framework
* Can run in as little as 470 KB of RAM on microcontrollers with limited resources

**Components**

* **Flash**: used for storing firmware and data ( approximately 89 KiB)
* **SRAM (arena peak)**: provides additional memory for cached data and computations (approximately 36 KiB)
* **Compute**: includes VAD, STT, TTS, and other components running sequentially to optimize performance
* **TensorFlow Lite Microlite speech synthesis library**

**System Requirements**

* Microcontroller with limited resources (e.g. Raspberry Pi RP2350 with 80 cents retail price)
* Dedicated RAM of at least 470 KB

**Code Structure**

* Code is released under the MIT License
* Emitted as a single executable file for each microcontroller setup using voice on an RP2350 MCU example code
* Includes TensorFlow Lite Microlite speech synthesis library