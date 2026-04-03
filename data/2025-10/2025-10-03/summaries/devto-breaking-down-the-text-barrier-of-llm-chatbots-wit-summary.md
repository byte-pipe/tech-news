---
title: Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community
url: https://dev.to/hichamelbsi/breaking-down-the-text-barrier-of-llm-chatbots-with-kendoreact-and-mcp-ui-1ico
date: 2025-09-27
site: devto
model: llama3.2:1b
summarized_at: 2025-10-03T11:16:22.920336
screenshot: devto-breaking-down-the-text-barrier-of-llm-chatbots-wit.png
---

# Breaking down the text barrier of LLM chatbots with KendoReact and MCP-UI - DEV Community

## Breaking Down the Text Barrier of LLM Chatbots with KendoReact and MCP-UI
===========================================================

This article presents a solution to overcome the limitations of existing Large Language Model (LLM) chatbots by integrating polished, interactive UI components using KendoReact, Supabase as the database backend, and MCP-UI as the glue between the chatbot and UI components.

### Key Points

* **Combines KendoReact and MCP-UI for a dynamic conversation experience**: Creates live KendoReact Grids and Cards that render directly in conversations.
* **Exposes two tools through MCP-UI**: `show_grid` queries tables with filters and joins, returning a KendoReact Grid; `show_user_details`: fetches a user profile plus task counts (todo, in_progress, done), and returns a KendoReact Card.

### Implementation Details

* **MCP-UI Server**:
	+ Exposes two tools through an API: `show_grid` queries tables with filters and joins.
	+ Returns a KendoReact Grid displaying the results.
* **KendoReact Components**: Built a chatbot UI using these components, which can receive UI Request messages from the server.
* **Client-Side Integration**:
	+ Consumes the interactive Grids and Cards API through MCP-UI Client.
* **Prototype of Future LLM Applications**: Explores use cases that leverage interactiveness, such as statistics dashboards tied to ongoing conversations, workflow management, and exploration tools.

### Technical Insights

* **Portability**: Use any MCP host (e.g., LibreChat) that supports MCP-UI/client can consume the server’s active Grids and Cards without custom integration.
* **MCP-UI’s battle-tested components**: Enhances Kendo UI's usability for various development partners, including Shopify experiment with "agentic commerce" using similar patterns.

### Conclusion

This challenge demonstrates how integrating KendoReact, MCP-UI, and Supabase can enhance the user experience of LLM chatbots by providing advanced conversational interaction capabilities.
