---
title: GitHub - zilliztech/claude-context: Code search MCP for Claude Code. Make entire codebase the context for any coding agent. · GitHub
url: https://github.com/zilliztech/claude-context
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-04-21T12:09:55.615469
---

# GitHub - zilliztech/claude-context: Code search MCP for Claude Code. Make entire codebase the context for any coding agent. · GitHub

**Public Overview of Claude Context**

CLAUSE-CONTEXT is a Memory-Centralized Programming (MCP) plugin for Claude Code, an AI-powered programming assistant. It provides a semantic code search system that retrieves all relevant code from millions of lines, offering long-term context to AI agents.

**Key Features and Benefits**

*   Stores entire codebase in a vector database
*   Efficiently loads only related code for each request
*   Cost-effective for large codebases (avoiding multi-round discovery)
*   Seamlessly integrates with Claude Code and other AI coding assistants

**Getting Started**

1.  **Sign In Required**: To access the configuration examples, use your OpenAI API key to provide:
    *   `OPENAI_API_KEY`: Replace `sk-your-openai-api-key` in the command line interface.
2.  **System Requirements**: Ensure Node.js (>= 20.0.0 and < 24.0.0).
3.  **MCP Server Configuration**:

    ```
    Claude Context is not compatible with Node.js 24.0.0, downgrade to first if your node version is greater or equal to 24
    npm install @zilliz/claude-context-mcp@latest
    claude mcp add claude-context \
      -e OPENAI_API_KEY=sk-your-openai-api-key \
      -e MILVUS_TOKEN=your-zilliz-cloud-api-key \
      -- npx @zilliz/claude-context-mcp@latest
    ```

**Using Claude Context with Claude Code**

*   Install the `CLAUSE-CONTEXT` and `OpenAI` dependencies
*   Import `klaudeContext` in your codebase
*   Use the MCP server to manage sessions

By following these steps, you can harness the power of CLAUSE-CTX to enhance your AI coding experience.