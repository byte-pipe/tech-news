---
title: Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community
url: https://dev.to/hichamelbsi/breaking-down-the-text-barrier-of-llm-chatbots-with-kendoreact-and-mcp-ui-1ico
date: 2025-09-27
site: devto
model: llama3.2:1b
summarized_at: 2025-10-02T11:13:32.533837
screenshot: devto-breaking-down-the-text-barrier-of-llm-chatbots-wit.png
---

# Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community

## Building a Multi-Component LLM Chatbot with KendoReact and MCP-UI

This article discusses the development of an LLM-based chatbot that utilizes KendoReact for interactive UI components, Supabase as the database backend, and MCP-UI (Model Context Protocol UI) as the glue between the chatbot and UI components. The system can render live KendoReact Grids and Cards directly in conversation without relying on text-only answers.

### Key Components

*   **MCP-UI Server**: Exposes two tools: show_grid for querying tables with filters and joins, and returns a KendoReact Grid; and show_user_details for fetching user profiles plus task counts (todo, in_progress, done) and returning a KendoReact Card.
*   **Client-side UI**: Built using KendoReact components integrated with MCP-UI's portability feature. The chatbot can receive UI messages from the server and render them inside the conversation.

### Benefits of Using MCP-UI

*   Portability: Any MCP host that supports mcp-ui/client can consume the server's interactive Grids and Cards without custom integration.
*   Scalability: The system can handle multiple users and conversations simultaneously, making it suitable for large-scale applications.

### Future Potential

*   **Statistics Dashboard**: Integrate with ongoing conversation to display real-time statistics.
*   **Interactive Workflows**: Enable one MCP server's results feed another's UI to facilitate collaborative decision-making processes.

## Demo

The demo URL can be found in the article, providing hands-on experience with displaying tasks, users, or projects and interacting with dynamic KendoReact x MCP-UI components. The application will run temporarily on an Anthropic API key, but an temporary Supabase API key is needed for local setup.

*   **Video Demo**: A video recording of the custom-powered chatbot provided to demonstrate its capabilities.
*   **Screenshot**: A screenshot that showcases the same system running inside LibreChat.
