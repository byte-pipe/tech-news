---
title: Build a Frontend for your ADK Agents with AG-UI - DEV Community
url: https://dev.to/copilotkit/build-a-frontend-for-your-adk-agents-with-ag-ui-2alo
date: 2025-09-25
site: devto
model: llama3.2:1b
summarized_at: 2025-09-29T11:19:05.020064
screenshot: devto-build-a-frontend-for-your-adk-agents-with-ag-ui-de.png
---

# Build a Frontend for your ADK Agents with AG-UI - DEV Community

## TL;DR
This guide will help you build a frontend for your Agent Development Kit (ADK) agents using AG-UI Protocol and CopilotKit.

**What is the Agent Development Kit (ADK)?**

* An open-source framework for building complex AI agents.
* Equips your AI agents with planning, tool use, and state management out of the box.

**Setting up an ADK agent using CLI**

* Set up a full-stack ADK agent quickly by running a CLI command to set up the backend with AG-UI protocol and frontend with CopilotKit.

## Prerequisites

* A basic understanding of React or Next.js.
* Python installation on your computer.
* Familiarity with AG-UI Protocol and CopilotKit.

## How it Works

### Step 1: Run CLI command to set up the backend

Run the following CLI command:
```bash
cd path/to/ADK/agent
npm install -g @agui/proto/cli
ag-ui init <your-project-name>
```
Choose a project name, and the command will set up your ADK agent quickly.

### Step 2: Integrate the frontend with CopilotKit

Run the following CLI command:
```bash
cd path/to/ADK/agent
npm install @copilotkit/http
ag-ui copy <your-project-name>
```
This will integrate your ADK agent with AG-UI Protocol and start building a full-stack ADK agent.

## Full Stack ADK Agent using CLI

The setup flow is covered in the Getting Started guide within the CopilotKit docs.

### Example Use Case:

With this setup, you can now integrate your ADK agents with AG-UI Protocol's frontend to create seamless real-time interactions between the backend and frontend.
