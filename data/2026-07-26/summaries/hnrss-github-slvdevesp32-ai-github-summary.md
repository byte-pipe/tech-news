---
title: GitHub - slvDev/esp32-ai · GitHub
url: https://github.com/slvDev/esp32-ai
date: 2026-07-25
site: hnrss
model: llama3.2:1b
summarized_at: 2026-07-26T11:37:43.978037
---

# GitHub - slvDev/esp32-ai · GitHub

**Overview of the Tech: ESP32-S3 28M Parameter Language Model**

* A public repository for a high-performance language model built on an ESP32-S3 microcontroller.
* The model runs locally within the chip's memory, saving significant energy and reducing communication with external devices.

**Key Features:**

* High computational power and speed due to using an embedded processing core instead of being stored in SRAM (Flash) or RAM
* Ability to scale to millions of parameters while minimizing memory requirements
* Implemented using Google's Per-Layer Embeddings from Gemma 3n and Gemma 4

**Performance:**

* Approximately **9.5 tokens per second** end-to-end speed due to pure compute processing on the chip
* Uses a small screen to render text, showing the performance in real-time

**Technical Details:**

* Chip specifications:
	+ ESP32-S3 (microcontroller)
	+ 512KB SRAM
	+ 8MB PSRAM and 16MB flash memory
* Model size and capacity:
	+ Approximately **14.9MB at a 4-bit resolution**
* Trainings and datasets:
	+ Used the TinyStories dataset for its simplicity and coherence

**Comparison and Limitations:**

* Has higher computational power than many earlier models on chips like this, but at the cost of significant memory usage
* Unable to answer questions or follow instructions due to limited input scope