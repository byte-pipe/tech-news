---
title: Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community
url: https://dev.to/hichamelbsi/breaking-down-the-text-barrier-of-llm-chatbots-with-kendoreact-and-mcp-ui-1ico
date: 2025-09-27
site: devto
model: llama3.2:1b
summarized_at: 2025-10-01T11:16:28.700027
screenshot: devto-breaking-down-the-text-barrier-of-llm-chatbots-wit.png
---

# Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community

## Breaking Down the Text Barrier of LLM Chatbots with KendoReact and MCP-UI

This article discusses a system that combines Large Language Model (LLM) chatbots with polished, interactive UI components provided by KendoReact and Supabase. The main goal is to enhance the conversational experience by rendering live KendoReact Grids and Cards within the conversation.

### Key Features of the System:

*   **Server-side Integration**: The system utilizes an MCP-UI server on the backend to expose two tools: `show_grid` which fetches tables with filters and joins, and returns a KendoReact Grid;
*   **Client-side Interactivity**: A chatbot UI is built using KendoReact components and MCP-UI Client.
*   **Portability**: Any host that supports `mcp-ui/client` can consume the server’s interactive Grids and Cards without any custom integration.

### Advantages of this Approach

*   **Improved User Experience**: By rendering live data directly in the conversation, chatbots can provide more engaging and informative experiences for users.
*   **Increased Accessibility**: The system's design promotes interactivity, making it easier for users to explore and manipulate complex datasets.
*   **Futureproofed Applications**: This approach sets a promising foundation for building applications around LLMs that rely on real-time data.

### Future Use Cases

*   **Statistics Dashboards**: Integrating the system with APIs or databases to display ongoing statistics can create a powerful tool for users.
*   **Interactive Workflows**: Enabling multiple MCP servers' result feeds to feed another's UI offers a compelling use case for chatbots that need to manage complex workflows.

### Demo

*   To experience the demo, visit [the Vercel app](https://kendo-ai-bot-mcp-ui.vercel.app/Try), which displays tasks, users, or projects and can interact with dynamic KendoReact x MCP-UI components.
