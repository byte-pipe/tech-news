---
title: "Anthropic's new hardware standard lets AI agents control the physical world - Ars Technica"
url: https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/
date: 2026-08-29
site: tldr
model: gpt-oss:120b-cloud
summarized_at: 2026-08-29T01:32:45.249155
---

# Anthropic's new hardware standard lets AI agents control the physical world - Ars Technica

# Anthropic’s Model Hardware Standard (MHS) Enables AI Agents to Control Physical Devices

## Overview
- Anthropic introduced the Model Hardware Standard (MHS), a set of standardized drivers that let AI agents interface with and control arbitrary hardware.
- The current “research preview” targets scientific labs, aiming to replace custom integration code with a common interface for data sharing across devices.
- Anthropic claims MHS can cut experimental setup time from weeks or months to hours or minutes.

## How MHS Works
- MHS provides a translation layer between AI models and hardware, allowing real‑time control via command‑line prompts, API calls, or natural‑language interaction through the Model Context Protocol.
- Devices are described with standardized tags that encode physical constraints (weight, range, safety limits, etc.) and adjustable parameters, giving models necessary context even without prior training on the specific hardware.

## Demonstrations
- In a promotional video, Claude (Anthropic’s model) adjusted a laser, evaluated camera feedback, and iteratively calibrated the system.
- Claude also focused a microscope, analyzed images, and repositioned it for further observation.
- Another demo showed Claude reasoning how to operate a robotic arm to pick up an aluminum can despite lacking explicit training on the task, using generated API scripts that adapt to changing conditions.

## Partnerships and Preview Phase
- Anthropic is collaborating with early partners such as AWS (Strands Robots), Hugging Face (LeRobot), Raspberry Pi, Automata, and Universal Robots.
- These partners assist in safety evaluations, best‑practice development, and testing of MHS in scientific and advanced manufacturing settings.
- The goal is to eventually release MHS as an open‑source, agent‑agnostic standard.

## Potential Impact
- Faster integration of hardware reduces iteration cycles, enabling quicker hypothesis testing and accelerated technological progress.
- By providing AI models with reliable, real‑world hardware interfaces, MHS could broaden the scope of autonomous scientific experimentation and industrial automation.