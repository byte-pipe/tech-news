---
title: Build a Frontend for your ADK Agents with AG-UI - DEV Community
url: https://dev.to/copilotkit/build-a-frontend-for-your-adk-agents-with-ag-ui-2alo
date: 2025-09-25
site: devto
model: llama3.2:1b
summarized_at: 2025-10-02T11:16:43.492136
screenshot: devto-build-a-frontend-for-your-adk-agents-with-ag-ui-de.png
---

# Build a Frontend for your ADK Agents with AG-UI - DEV Community

# Building a Frontend for your ADK Agents using AG-UI - DEV Community

## TL;DR

This guide will show you how to build a frontend for your Agent Development Kit (ADK) agents using AG-UI Protocol and CopilotKit. It is essentially a quickstart guide to help you get started fast.

## What is the Agent Development Kit (ADK)?

* The ADK is an open-source framework designed to simplify the process of building complex and production-ready AI agents.
* Equips your AI agents with planning, tool use, and state management features out of the box.

## Setting up an ADK + AG-UI + CopilotKit agent using CLI

### Setting up the Backend (Ag-UI Protocol)

1. Install Node.js if you haven't already
2. Set up a new project directory for your ADK agent
3. Run the following command to set up the backend:
```
git clone https://github.com/adk-projects/AgentDevelopmentKit.git
cd AgentDevelopmentKit
npm install
npm link ag-ui-protocol
```

### Setting up the Frontend (CopilotKit)

1. Install Node.js if you haven't already
2. Set up a new project directory for your ADK agent
3. Run the following command to set up the frontend:
```
git clone https://github.com/adk-projects/CopilotKit.git
cd CopilotKit
npm install
npx copilotkit-init --adapter=opendialog-protocol # Select AG-UI adapter
```

## Integrating your ADK agent with AG-UI protocol in the backend

1. Set up the AG-UI server to handle incoming requests from your agent.
2. Your agent should have an API endpoint exposed for receiving data.

### Running the Frontend using CopilotKit

To run the frontend, navigate to the `CopilotInit` directory and start the server:
```
npx copilotkit-init start
```

## Building a frontend for your ADK + AG-UI agent using CopilotKit

You can use the CopilotKit CLI tool to build your frontend. The latest version has built-in support for various programming languages, including JavaScript, and frameworks like React.

Here is an example of how you can create a simple web page with a button in front end:
```bash
npx copilotkit init my-app
cd my-app
git add .
git commit -m "Initial commit"
git push origin main
```
To open the app, open `index.html` in your web browser.

### Integrating ADK agent with AG-UI protocol in frontend

1. Your ADK agent should have an API endpoint that exposes data to the frontend.
2. Use the AG-UI adapter in CopilotKit to connect to this data source and update it in real-time.

## Prerequisites

* Basic understanding of React or Next.js
* Python installed on your computer; use the `gemini` model for ADK agent development
* AG-UI Protocol implemented as an open-source platform; check out their GitHub repository
* CopilotKit open-source copilot framework; explore their documentation
