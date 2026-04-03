---
title: Writing a good CLAUDE.md | HumanLayer Blog
url: https://www.humanlayer.dev/blog/writing-a-good-claude-md
date: 2025-11-30
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-12-01T11:09:05.367041
screenshot: hackernews_api-writing-a-good-claude-md-humanlayer-blog.png
---

# Writing a good CLAUDE.md | HumanLayer Blog

## Onboarding Agent HLLM Models with CLAUDE.md Files
---------------------------------------------

### Overview
Stateless LLMs like OpenCode and Zed require explicit management of agent memory. In contrast, agents like Claude for human-AI collaborations need to onboard the human developer's codebase upon initial use.

### Key Points

*   **Initial State:** Coding agents have no context knowledge about a developer's codebase at startup.
*   **Information Needed:** Agents must be informed of the developer's tech stack, project structure, and dependencies on each new session.
*   **Contextual Knowledge:** Onboarding through CLAUDE.md files helps clarify purpose, function, and verification of changes.

### Structured Output (Markdown)

*   **Principle 1: Stateless Models**
    *   LLMs are mostly stateless: their weights are frozen before use.
    *   Claude models do not learn over time; they only retain global knowledge from the agent's previous sessions.
*   **Principle 2: Explicit Management**
    *   Agents require explicit management of agent memory across multiple sessions.
*   **Principle 3: Preferred Method**
    *   CLAUDE.md is the preferred method for onboarding agents into a developer's codebase.

### High-Level CLAUDE Model Configuration
--------------------------------------------

#### Data Requirements

*   **What:** Provide global context about your project structure, apps, shared packages, and code dependencies.
*   **Why:** Inform agent of purpose and function of different parts of the project.
*   **How:** Detail local steps involved in the development process.

#### Structure

*   Onboarding Process
    *   Include:
        *   App descriptions
        *   Shared package information
        *   Project structure description
      *   Purpose and functionality of different components
    *   Use clear and concise language that leverages agent-specific instructions.
    *   Maintain original perspective as per the CLAUDE.md format.

### Case Study: Onboarding Claude Model with CLAUDE.md

*   **Development Context:** A team wants to onboard their AI model, Claude, for human-AI collaboration tasks. They need accurate contextual information about the developer's codebase.
*   **Solution:** Develop a well-structured and informative CLAUDE.md file that leverages essential details provided by the agent during initial setup.

By following these guidelines and best practices, developers can effectively onboard their AI models, Claude, ensuring reliable and meaningful interactions.
