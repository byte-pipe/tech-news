---
title: A Docker Trick I Wish I Knew Sooner - DEV Community
url: https://dev.to/joybtw/a-docker-trick-i-wish-i-knew-sooner-23of
date: 2025-10-16
site: devto
model: llama3.2:1b
summarized_at: 2025-10-22T11:22:24.313838
screenshot: devto-a-docker-trick-i-wish-i-knew-sooner-dev-community.png
---

# A Docker Trick I Wish I Knew Sooner - DEV Community

## A Cleaner Docker Download Method Revealed - DEV Community

**The Old Way: Installing Curl**

When building a Docker image using `curl`, it's easy to install the command-line tool inside the container. However, this approach adds unnecessary bloat by installing `curl` just for downloading files.

*   Installing `curl` and then invoking it as many times as required is inefficient and increases the size of the Docker image.
*   This method requires managing a separate package, which can slow down development process and complicate production environments.

## The Better Way: Using Docker's ADD Instruction

Docker provides an easy way to download remote files without requiring additional packages. The `ADD` instruction allows pulling files from URLs directly into the container at build time.
*   **Benefits**:
    *   Smaller image size reduces costs and enhances performance in production or constrained environments.
    *   Fewer dependencies means fewer potential security vulnerabilities and a simpler dependency tree.
    *   Cleaned up Dockerfile makes it more readable, idiomatic, and easier to understand.

## When to Use Each Approach

*   Use `ADD` when:
    +   You need to download single files from URLs
    +   The file doesn't require authentication or other advanced features
    +   The goal is minimal Docker image size
*   Stick with `curl` for workflow that requires more control over the downloaded content or multiple files.

**Quick Tips and Considerations**

*   Templates can help answer frequently asked questions (FAQs) or store snippets for future use.
*   You might want to consider sharing your tricks, but don't hesitate to block abusive users who ask unnecessary questions.

### Conclusion

Using `ADD` in Docker provides a cleaner, more efficient way to handle file downloads. It reduces the size of your image while maintaining readability and simplicity. When deciding whether to use `curl` or `ADD`, think about what you need: minimal Docker images or advanced workflow control?
