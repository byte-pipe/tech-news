---
title: Build Your Own AI Butler - A Scheduled Agent That Runs Itself! - DEV Community
url: https://dev.to/aws/build-your-own-ai-butler-a-scheduled-agent-that-runs-itself-3dmk
date: 2026-05-06
site: devto
model: llama3.2:1b
summarized_at: 2026-05-07T12:37:22.780354
---

# Build Your Own AI Butler - A Scheduled Agent That Runs Itself! - DEV Community

**Jarsvia: A Customizable AI Butler and Long-Running News Agent**

### Overview

Jarsvia is a bespoke, custom-made artificial intelligence (AI) agent designed to cater to individual needs. It offers unparalleled functionality, reliability, and flexibility. The solution aims to provide an equivalent of Jarvis, the fictional AI character from the Marvel Cinematic Universe, serving as a trusted butler for users.

### Key Features

* **Built-in news delivery**: Receive breaking news updates and trending stories via a scheduled news digest agent called "The Pulse."
* **Chat functionality**: Engage in conversations with Jarsvia using natural language processing (NLP) capabilities.
* **Advice and guidance**: Offer advice based on your preferences, experiences, or interests.
* **User interface customization**: Leverage Telegram as the primary messaging channel for seamless communication.
* **Expansion and upgradeable**: Expand its offerings through future updates, plugins, and integrations.

### System Architecture

1. **Configuration Management**: Define the Jarsvia configuration in a custom JSON file (e.g., `agentcore.json`).
2. **Deployment**: Schedule the agent using EventBridge Scheduler with Lambda triggers.
3. **Memory Management**: Retain contextual information across runs utilizing AWS AgentCore's memory capacity.

### Usage and Integration

1. **Initiation**: Run Telegram with Jarsvia as the user interface to start engaging in conversations.
2. **Message-based interaction**: Respond to messages from Jarsvia, prompting her for advice or engaging in discussions about specific topics.
3. **Scheduled news input**: Use an RSS feed (or other source) to periodically update The Pulse with new news content.

### Code Implementation

The provided code serves as a starting point for building your own Jarvis-like AI agent. It demonstrates:

* AgentCore managed harness integration
* EventBridge Scheduler scheduling via a Lambda trigger
* Customizable configuration management

Customize and expand this foundation through adding features, plugins (e.g., advice models), or integrations with external systems.

### Conclusion

Jarsvia is an innovative solution for individuals seeking customized AI assistance. With its robust capabilities and flexibility, it can become a trusted companion in various aspects of daily life.