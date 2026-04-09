---
title: Introducing the Gemini 2.5 Computer Use model
url: https://blog.google/technology/google-deepmind/gemini-computer-use-model/
date: 2025-10-07
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-08T11:20:58.759336
screenshot: hackernews_api-introducing-the-gemini-2-5-computer-use-model.png
---

# Introducing the Gemini 2.5 Computer Use model

# Introducing the Gemini 2.5 Computer Use Model

• Available in preview via Google AI Studio and Vertex AI
• Enables developers to build agents that can interact with user interfaces (UIs)

## Key Features

- Outperforms leading alternatives on multiple web and mobile control benchmarks
- Supports lower latency than other models
- Can be accessed through the Gemini API

## How it Works

1.  **Input Processing**: The `computer_use` tool receives the following inputs:
    - User request: a description of the task to be performed
    - Screenshot of the environment: a representation of the current screen layout and user inputs
    - History of recent actions: a record of previous tasks completed by the agent
2.  **Analysis**: The input is analyzed to determine the required action for completion of the task.

## Interaction Flow

1.  **Action Generation**: Based on the analysis, a response is generated that represents one of the supported UI actions (e.g., clicking or typing).
2.  **Request Generation**: A request will be included in the response to confirm with the user prior to execution.
3.  **Execution**: The client-side code executes the received action and sends a new screenshot back to the agent as a function response.

## Primary Optimization

The Gemini 2.5 Computer Use model is primarily optimized for web browsers but also showcases proficiency in strong-parsing techniques that handle interactive elements and dropdowns.
