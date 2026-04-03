---
title: x86CSS
url: https://lyra.horse/x86css/
date: 2026-02-25
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-25T06:01:09.658224
---

# x86CSS

# x86 CPU made in CSS

x86CSS is a functional x86 CPU emulator written entirely in Cascading Style Sheets (CSS), requiring no JavaScript. It's implemented as a C program compiled with GCC that runs within the CSS environment.

## Key Features and Concepts
- **CSS-only Implementation:** The entire CPU is built using CSS, demonstrating the capabilities of the technology.
- **C Compilation:** A C program is compiled using GCC into native 8086 machine code, which is then executed within the CSS.
- **No JavaScript Required:** The functionality relies solely on CSS features, including animations and style queries, for a fully functional program.
- **Compatibility:** The project implements most of the x86 architecture, focusing on the original 16-bit 8086 instruction set. Some instructions and behaviors are simplified or missing.
- **Customizable Memory and I/O:** The emulator has a default memory size of 1.5kB, which can be adjusted. Custom I/O addresses are available for interaction.
- **Self-Contained:** The project includes a Python script (`build_css.py`) to compile C code into an executable that runs within the CSS.

## Functionality
- **Program Execution:** Users can write and compile 8086 assembly or C code to run within the emulator.
- **Customizable Input/Output:** The emulator provides custom I/O addresses for interacting with the running program.
- **Clock Implementation:** A CSS clock is included for timing purposes, utilizing animations and style container queries for zero user input operation.

## Technical Details
- **Browser Compatibility:** Currently, it primarily works in Chromium-based browsers due to the use of specific CSS features.
- **Preprocessor:** The CSS code is hand-written, with a Python script used for repetitive parts.
- **No AI/LLM Used:** The project was built manually without the assistance of AI models.

## Credits
The project acknowledges contributions from Jane Ori, Soo-Young Lee, mlsite.net, crtc-demos && tkchia, polly, cohosters, and others for inspiration and resources.
