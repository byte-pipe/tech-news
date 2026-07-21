---
title: Smash Story: The Demo Script That Out-Debugged My Test Suite - DEV Community
url: https://dev.to/gde/smash-story-the-demo-script-that-out-debugged-my-test-suite-430k
date: 2026-07-15
site: devto
model: llama3.2:1b
summarized_at: 2026-07-21T11:39:54.866817
---

# Smash Story: The Demo Script That Out-Debugged My Test Suite - DEV Community

Smash Story: The Demo Script That Out-Debugged My Test Suite - DEV Community

**Introduction**
The article shares an experience where the author, working on a smallMCP server project, encountered a critical bug in their tests that was not present during runtime. They discovered the issue through a demo script called "demo.sh," which showcases four tools: Claude Code, a Google ADK agent, and a Rust CLI.

**The Setup**
The test suite has 10/10 unit tests passing, and the project consists of an SMCP (Model Context Protocol) server that generates images and allows for stateful image editing using four tools. The author confirms using successful deployment and publishing as a Docker image through various AI agents.

**The Smash**
The demo script "demo.sh" introduces a new feature by generating an image, then applying a stateful edit. To save resources, the developer requested only the lowest-quality tier for this server. However, the first test run encountered a runtime error when trying to create an image with minimal thinking levels (1:1), prompting the author to inspect the server's API validation process.

**Insights**
The article highlights several valuable insights into debugging and testing:

* The development team can rely on 10/10 unit tests passing, but these tests were not sufficient during runtime, revealing a crucial bug.
* The server's own validation had already approved images with minimal thinking levels before attempting to execute them.
* The validation layer was validating the API's contract rather than exposing an inherent flaw in the live API.
* A locally-generated allowlist duplicated remote-owned contracts, illustrating how these bugs were not discoverable through testing alone.

**Key Takeaways**

* Debugging and testing can be complex processes that require careful consideration of all aspects.
* Although unit tests may pass, they do not guarantee the behavior of a more complex system like the server described in the article.
* Validation layers must be properly implemented to catch bugs and ensure adherence to contract rules.

This summary retains the author's original meaning while adhering to Markdown formatting guidelines.