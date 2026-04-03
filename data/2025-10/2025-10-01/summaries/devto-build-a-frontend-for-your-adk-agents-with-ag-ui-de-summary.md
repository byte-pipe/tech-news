---
title: Build a Frontend for your ADK Agents with AG-UI - DEV Community
url: https://dev.to/copilotkit/build-a-frontend-for-your-adk-agents-with-ag-ui-2alo
date: 2025-09-25
site: devto
model: llama3.2:1b
summarized_at: 2025-10-01T11:18:18.407655
screenshot: devto-build-a-frontend-for-your-adk-agents-with-ag-ui-de.png
---

# Build a Frontend for your ADK Agents with AG-UI - DEV Community

Here's a concise and informative summary of the article:

## Introduction to Agent Development Kit (ADK)
The Agent Development Kit (ADK) is an open-source framework that simplifies building complex AI agents. It equips your AI agents with planning, tool use, and state management features.

## What is ADK?
ADK provides a foundation for creating production-ready AI agents with hours of development time. You can go from idea to prototype with complete flexibility.

## Prerequisites
To build full-stack ADK agents, you need:

* Basic understanding of React or Next.js
* Python installed on your computer
* AG-UI Protocol (CopilotKit) used for frontend interactions

## Setup Full-Streak_ADK Agent using CLI
Set up a full-stacked ADK agent with AG-UI Protocol and CopilotKit backend by running the following CLI command:

### Step 1: Set up Adk Backend
Run the CLI command below to set up your ADK agent's backend:
```
adk setup <ADK-version>
```

This will guide you through setting up your full-stack ADK agent using AG-UI Protocol and CopilotKit.

## Integration with AG-UI and CopilotKit Frontend
You'll learn how to integrate your ADK agent with AG-UI protocol in the backend and build a frontend for it using CopilotKit in this article.

### Step 2: Integrate with AG-UI Backend
Explore the integration of your ADK agent with AG-UI Protocol by following the provided guide.
```
# Adk Setup & Integrations

## Prerequisites:
* You can check what requirements do for yourself to get started fast using the getting starts guideline at https
* Python installed on your computer.


If you want to implement a full-stack AI Agent using Python, here is how you could achieve it in 30 days if following copilot kit docs guide:

```python
import os
from flask import Flask

# Load data and config from files named “config.py” and “data.json”
app = Flask(__name__)

@app.route('/')
def index():
return ‘<h1>FullStackAI Agent</h1>“

if __name__ == '__main__':
  app.run()
```

Note: You will need to create a new AI engine using AGUI protocol following your setup procedure in getting started guide.

```python
import os
from flask import Flask, request

app = Flask(__name__)

# Load data and config from files named “config.py” and “data.json”
@app.route('/testinput', methods=['POST'])
def handle_input():
    data = request.get_json()
    response = {'message': 'processed successfully'}
    return jsonify(response)

if __name__ == '__main__':
  app.run(port=5000)
```


### Step 3: Build Frontend with CopilotKit

Use the provided guide to build your full stacks agui frontend that implements AI logic for an AGP engine using Agui Protocol. You're just a few hours away from it!

Note: This is not an exhaustive guide, you may need more information about AG-UI and CopilotKit's functionality which can also be found on their official documentation.

### Step 4: Integrate Frontend with Backend
Integrate your frontend built using CopilotKit with the backend setup through API calls to communicate with each other. Ensure that there are valid HTTP headers, request body as described in ADK guidelines for an example of what's allowed and invalid

## Conclusion
