---
title: Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community
url: https://dev.to/hichamelbsi/breaking-down-the-text-barrier-of-llm-chatbots-with-kendoreact-and-mcp-ui-1ico
date: 2025-09-27
site: devto
model: llama3.2:1b
summarized_at: 2025-09-30T11:13:49.456406
screenshot: devto-breaking-down-the-text-barrier-of-llm-chatbots-wit.png
---

# Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community

## Building a Limitless Language Model Chatbot with KendoReact and MCP-UI

This text describes a novel approach to building a language model chatbot that breaks down the traditional limitations of plain-text answers. The solution combines:

* KendoReact components for a polished, interactive user interface.
* Supabase as the database backend.
* MCP-UI (Model Context Protocol UI) as the glue between the chatbot and UI components.

### Key Features

1.  **Live KendoReact Data**: The system renders live KendoReact Grids and Cards directly in conversations powered by real Supabase queries.
2.  **MCP-UI Server**: An MCP-UI server exposes two tools: `show_grid` for retrieving query results and `show_user_details` for fetching user data along with task counts, creating a seamless interaction experience.

### How it Works

*   On the server side:
    *   A MCP-UI server is created using `mcp-ui/server`, which provides the following features:
        +   Exposes two tools: `show_grid` and `show_user_details`.
        +   Queries tables (tasks, projects, users, user_tasks) for filtering and joins with results.
        +   Returns KendoReact Grids or Cards based on queries and user details.
*   On the client side:
    *   A chatbot UI is built using KendoReact components and `mcp-ui/client` to consume server-side Interactions.
    *   This allows clients to interact directly with UI components, regardless of whether they have a native MCP-compatible host.

### Advantages

This approach offers several advantages:

*   **Interoperability**: MCP hosts can run on the client side using `mcp-ui/client`, ensuring seamless interaction with various chatbot services.
*   **Portability**: Using MCP-UI reduces the effort required to integrate custom UI components due to its native support across different systems.

### Future Directions

The success of this approach inspires potential future directions:

*   **Multimodal Interaction**: Further exploring how interacting with LLMs can be achieved through multimodal interfaces, using data from various sources (e.g., KendoReact widgets).
*   **Decentralized AI Platforms**: Developing decentralized AI platforms that prioritize transparency and security, leveraging MCP-UI and the benefits of KendoReact interactions.

The proposed solution offers a powerful way to unlock new opportunities for language model chatbots. By empowering developers with the capabilities to create immersive interactive interfaces, this approach can drive innovation in conversational AI applications.
