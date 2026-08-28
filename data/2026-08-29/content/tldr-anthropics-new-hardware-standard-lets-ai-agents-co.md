---
title: Anthropic's new hardware standard lets AI agents control the physical world - Ars Technica
url: https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/
site_name: tldr
content_file: tldr-anthropics-new-hardware-standard-lets-ai-agents-co
fetched_at: '2026-08-29T01:31:01.652939'
original_url: https://arstechnica.com/ai/2026/08/anthropics-new-hardware-standard-lets-ai-agents-control-the-physical-world/
date: '2026-08-29'
published_date: '2026-08-27T22:15:43+00:00'
description: Standardized driver interface aims to let devices talk to AI and each other.
tags:
- tldr
---

Text
 settings

For all theinterest inanduptakeofagentic AI systemsoverthe past year or so, the world of automated AI has thus far been primarily limited to text, images, code, and other data and actions that take place inside a computer. Anthropic is now aiming to change that somewhat with what it’s callingthe Model Hardware Standard(MHS), a set of standardized drivers designed to let AI agents easily interface with and control arbitrary devices.

For now, the “research preview” of the MHS effort is being sold mainly as a way to help scientists streamline the arduous process of creating the custom software integrations that are often needed to get disparate components of an experiment working in concert. MHS can provide a common interface and common format for data sharing between these devices, Anthropic says, allowing them to talk to each other across a network “without needing a bespoke ‘translator’ program in between.” The standardized system could reduce weeks or months of exacting experimental setup down to “hours or minutes,” Anthropic writes.

 An Anthropic graphic illustrating how MHS serves as a “translation” layer between AI agents and multiple types of devices.
 

 Credit:
 
Anthropic

 An Anthropic graphic illustrating how MHS serves as a “translation” layer between AI agents and multiple types of devices.

 

 Credit:

 

 
 Anthropic

 

Ina video posted alongside the announcement, Anthropic Technical Staffer Alek Kemeny says the MHS effort was inspired by observing neuroscientist Arco Bast work through an experiment on memory formation in the brain atthe HHMI Janelia Research Campusin Ashburn, Virginia. Kemeny said Bast had worked out an interface to get the rotating laser beams, microscopes, cameras, and myriad other components of the experiment to coordinate through a common interface. “This idea could be used to have AI run any science experiment in the world,” Kemeny recalls thinking at the time.

## Your new robotic lab assistant?

There’s nothing about a common machine interface language that requires the use of AI models, of course. And Anthropic says MHS devices can be controlled directly in real time via command-line prompts and API code files. But integrating an MHS system with an AI model through the Model Context Protocol lets scientists interact with devices using natural language and lets models “reason through each step in an experiment, update parameters in real time, and, in some cases, recover from hardware errors without intervention,” Anthropic writes.

Anthropic gave the example of a model like Claude adjusting a laser, checking the results via a separate camera, then repeating the process to automatically calibrate the whole system. MHS could also allow an AI model to focus a microscope, analyze the results, decide what part needs more observation, then automatically move the microscope to the relevant section to continue the experiment.

In a video, Anthropic also showed Claude reasoning how to get a robotic arm to pick up an aluminum can even though it had not been specifically trained on the required steps. And rather than reasoning through each step each time, Anthropic says MHS-enabled models can sequence steps across instruments by writing API scripts and adjusting them as conditions require.

 Anthropic introduces MHS in a promo video.

 

Anthropic says MHS also includes a standardized tagging system to describe hardware’s real-world constraints for models that may have been trained more in the virtual world. That includes encoded information about the hardware’s physical characteristics (e.g., the weight and range of a robot arm) as well as its adjustable parameters, measurement options, and enforced safety limits. These tags can then be integrated into a reference file that can quickly provide an AI model with crucial information about a device it has no previous training experience with.

For now, Anthropic says it is working with “a first group of scientific research labs and advanced manufacturers” during an MHS preview period, including Amazon Web Services (Strands Robots), Hugging Face (LeRobot), Raspberry Pi, Automata, and Universal Robots. These partners will help Anthropic “build safety evaluations and develop best practices for AI systems operating physical equipment,” the company writes. After that, the plan is for MHS to eventually become an open source and “agent agnostic” standard for integrating AI and physical systems.

In early testing with scientific partners over the past year, Anthropic says it “saw MHS reduce the time it took to integrate devices, mak[ing] it possible to iterate faster in a variety of experimental settings.”

“If you can test hypotheses faster, you could create general technologies faster,” Kemeny said ina promo videoalongside the announcement. “This is how a century of progress can condense into a decade.”

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland
 

Senior Gaming Editor

 Kyle Orland has been the Senior Gaming Editor at Ars Technica since 2012, writing primarily about the business, tech, and culture behind video games. He has journalism and computer science degrees from University of Maryland. He once 
wrote a whole book about 
Minesweeper
.
 

1. 1.New Twitter launches, says Musk's X gave up the name
2. 2.Claude, Codex, and Hermes installed unowned code inside corporate networks
3. 3.Elon Musk’s xAI used child porn to train Grok models, lawsuit says
4. 4.AI industry says Trump plans to tax chips in the “single dumbest way imaginable”
5. 5.RFK Jr. goes full anti-vaccine bananas over two measles deaths—one was a newborn

Customize