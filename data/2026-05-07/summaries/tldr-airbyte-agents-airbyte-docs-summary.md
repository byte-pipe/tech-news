---
title: Airbyte Agents | Airbyte Docs
url: https://docs.airbyte.com/ai-agents/
date: 2026-05-07
site: tldr
model: llama3.2:1b
summarized_at: 2026-05-07T12:33:28.742688
---

# Airbyte Agents | Airbyte Docs

### Airbyte Agents Documentation

Airbyte Agents is a data and context layer for AI agents. It provides real-time access to business data through open-source connectors, managed credentials, and low-latency search.

#### Overview of Airbyte Agents Features

* **Cloud Platform**: Deploy your agent on the Airbyte cloud platform
* **Open-Source Connectors**: Choose from various pre-configured connectors to connect to third-party APIs
* **Type-Safe Connectivity**: Ensure data types are maintained for robust and efficient connections
* **Low-Latency Search**: Faster data retrieval for faster decision-making

### Choosing an Interface

Airbyte Agents offers different interfaces to suit your needs:

#### Web App: Easy Integration with Existing Tools

Develop a custom web app using Airbyte's MCP client
https://mcp.airbyte.ai/mcp

#### MCP Server: Enterprise-Grade Deployment

Easily integrate Airbyte Agents into existing infrastructure using the MCP server
https://mcp.airbyte.ai/

#### Python SDK: Rapid Development for AI Engineers

Use the Python SDK to develop custom agents and connectors
Python SDK available
```python
# Import necessary modules and connect to Airbyte Agents API
import airbyte_sdk

# Create an instance of the Airbyte API client
client = airbyte_sdk.AirbyteClient()

# Connect to the MCP server or perform API calls
data = client.get_data()
```

#### HTTP API: Scalable and Flexible Integration

Perform API requests using the HTTP API and retrieve data from Airbyte Agents
```http
# Send an HTTP request to connect to Airbyte Agents API
import requests

response = requests.post("https://mcp.airbyte.ai/mcp/api/"

# Parse response as JSON and process the data accordingly
data = json.loads(response.text)
```

#### Connectors: Expand Your Capabilities

Browse the catalog of open-source connectors to equipping agents with access to third-party APIs
Agent connectors are available for various use cases, such as cloud connectivity or custom integrations.
```connector-name "Custom Connector"```