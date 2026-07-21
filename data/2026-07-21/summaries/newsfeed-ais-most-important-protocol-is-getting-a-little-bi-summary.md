---
title: "AI's most important protocol is getting a little bit easier to use | TechCrunch"
url: https://techcrunch.com/2026/07/20/ais-most-important-protocol-is-getting-a-little-bit-easier-to-use/
date: 2026-07-20
site: newsfeed
model: llama3.2:1b
summarized_at: 2026-07-21T11:50:24.511395
---

# AI's most important protocol is getting a little bit easier to use | TechCrunch

**The Model Context Protocol (MCP) Update: Improving AI Interoperability**

The Model Context Protocol (MCP) is a critical building block for AI interoperability. It enables AI models to securely access external data sources and services, reducing the need for custom infrastructure from engineers.

**Key Changes in the MCP Update**

* **New session ID approach**: The MCP update will use a "stateless" approach to session IDs on the server side, similar to how most ordinary websites work.
* **Session ID management**: Under the new system, servers will issue session IDs each time an AI client connects. This eliminates the need for servers to keep track of previous conversations and reduces maintenance efforts.

**Background: MCP's Existing Challenges**

MCP currently relies on a "hello" message from clients asking what capabilities they have. Servers then reply with their capabilities and hand back an initial session ID.
However, this setup can lead to issues when multiple machines are used in load balancing scenarios:
* Each machine must keep track of the "same conversation" IDs that have been issued already.
* This extra work can be time-consuming and costly, especially for large-scale deployments.

**Impact on the AI Ecosystem**

The MCP update is expected to improve AI interoperability by reducing infrastructure complexities. According to Arcade founder Nate Barbettini:
"The first thing we did was try and change how machines interact with each other because the existing session IDs were only ever the same at a certain point... 

By using a "stateless" approach, MCP will become easier to maintain and less expensive to operate as it scales."

The next step for MCP is gaining clarity on changes made in this update.