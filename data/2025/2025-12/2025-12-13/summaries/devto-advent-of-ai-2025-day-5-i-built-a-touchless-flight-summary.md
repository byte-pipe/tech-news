---
title: Advent of AI 2025 - Day 5: I Built a Touchless Flight Tracker You Control With Hand Gestures - DEV Community
url: https://dev.to/nickytonline/advent-of-ai-2025-day-5-i-built-a-touchless-flight-tracker-you-control-with-hand-gestures-1jn8
date: 2025-12-08
site: devto
model: llama3.2:1b
summarized_at: 2025-12-13T11:07:28.623788
screenshot: devto-advent-of-ai-2025-day-5-i-built-a-touchless-flight.png
---

# Advent of AI 2025 - Day 5: I Built a Touchless Flight Tracker You Control With Hand Gestures - DEV Community

**Introduction to Goose - Automating Development Tasks**

Goose is an open-source, extensible AI agent that offers a range of capabilities beyond code suggestions, enabling developers to automate complex tasks from start to finish. It can build entire projects from scratch, write and execute code, debug failures, orchestrate workflows, and interact with external APIs autonomously.

**Building The Homecoming Board - Gesture-Controlled Flight Display**

The recent project "The Homecoming Board" utilized Goose to create a gesture-controlled flight arrival display that utilizes hand gestures in freezing cold conditions. The app required at least two distinct gestures for navigation (e.g., moving between planes and landing), real-time flight data, and audio feedback for gesture recognition.

**Tech Stack and Benefits**

The project leveraged TanStack Start as the primary framework, combining React and TypeScript with Server-Side Rendering (SSR). MediaPipe was used for gesture recognition, while theOpenSky Network API provided access to real-time flight data. Goose adapted to this workflow seamlessly, handling tasks like building projects, code execution, and testing.

**Gant Laborde's Live Stream on AI and Tensorflow.js**

The demonstration video showcases an even more advanced application, TanStack Start Plus, which integrates with the Pomerium MCP app demo. It provides remote model context protocol servers secured by contextual access policies, demonstrating how developers can build secure applications using Goose and other open-source tools.

**Pre-requisites for Development**

Before attempting to replicate "The Homecoming Board" project or similar applications, make sure a Linux or MacOS host is available as well as Docker and Docker Compose are installed. This setup is necessary when working with Goose and the rest of the TanStack ecosystem.
