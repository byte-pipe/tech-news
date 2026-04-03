---
title: Build a Frontend for your ADK Agents with AG-UI - DEV Community
url: https://dev.to/copilotkit/build-a-frontend-for-your-adk-agents-with-ag-ui-2alo
date: 2025-09-25
site: devto
model: llama3.2:1b
summarized_at: 2025-09-28T10:20:42.108026
screenshot: devto-build-a-frontend-for-your-adk-agents-with-ag-ui-de.png
---

# Build a Frontend for your ADK Agents with AG-UI - DEV Community

## Building a Frontend for your ADK Agents with AG-UI - DEV Community

### TL;DR

This guide will help you build a full-stack Agent Development Kit (ADK) agent using AG-UI Protocol and CopilotKit. You'll learn how to integrate your ADK agent with AG-UI protocol in the backend and establish a frontend that communicates with the backend through CopilotKit.

### Introduction

Before we begin, give shoutouts to Mark FogleandSyed Fakherfor initially building theADK/AG-UI integration. To get started, you'll need to set up an ADK agent using CLI or install Python if it's not already installed on your computer. For a full-stack ADK agent, integrate the backend with AG-UI protocol and front-end development kit CopilotKit.

### What is the Agent Development Kit (ADK)?

Agent Development Kit (ADK) is an open-source framework designed to simplify the process of building complex AI agents with multi-step reasoning and execution. With ADK, you can build a working prototype within hours.

### Main Components

#### Backend

The backend component powers the AI agent backend using AG-UI Protocol.
It facilitates event-based interaction between frontend and backend, enabling real-time communication.
```python
# Import required libraries
import agui  # Assuming Python-AG-UI library is installed
from agui.agui import AgentInterface  # Use AG-UI API

class ExampleBackend:
    def __init__(self):
        self.agent_interface = Agui(AgentInterface())

    def process_input(self, input_data):
        # Process user input here
        return agui.get_current_state()

def main():
    backend = ExampleBackend()
    print(backend.process_input("Hello "))
```
#### Frontend

The frontend component is built using CopilotKit to facilitate easy integration and real-time communication with the backend.
```javascript
// Import required libraries
import copilotkit  # Assuming Copyit framework is installed
from copilotkit AGUI import AGUI  # Use AG-UI API

class ExampleAGUI:
    def __init__(self):
        self_agui = AGUI()

    def process_event(self, event_data):
        # Process user input here
        return "Hello "

def main():
    agui = ExampleAGUI()
    print(agui.process_event("Hello "))
```
### Setting Up Your Full-Stack ADK Agent

Follow these steps to set up your full-stack ADK agent:

1. **Setup the back-end**: Install Python and AG-UI library, create a backend class with process_input method.
2. **Integrate the frontend with CopilotKit**: Setup an instance of the AG-UI protocol in your front-end application.
3. **Push the modified AG-UI protocol to the source code repository**
