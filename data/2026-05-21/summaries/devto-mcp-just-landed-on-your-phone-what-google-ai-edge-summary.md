---
title: MCP Just Landed on Your Phone: What Google AI Edge Gallery Actually Does - DEV Community
url: https://dev.to/dannwaneri/mcp-just-landed-on-your-phone-what-google-ai-edge-gallery-actually-does-1567
date: 2026-05-20
site: devto
model: llama3.2:1b
summarized_at: 2026-05-21T12:07:20.931061
---

# MCP Just Landed on Your Phone: What Google AI Edge Gallery Actually Does - DEV Community

**Google AI Edge Gallery: What It Offers and Its Limitations**

The article discusses Google's AI Edge Gallery, an open-source Android app that allows users to deploy large language models on their devices without the need for internet connectivity. The main focus of the article is on the app's new features:

*   **MCP (Mobile Cloud Package) Connections**: This feature enables running agents on mobile devices with cloud storage capabilities.
*   **LiteRT-LM (TensorFlow Lite Mobile Inference Runtime)**: A lightweight, optimized runtime for mobile devices that supports various agent models and skills.

The author describes a series of experiments to push the limits of the app's capabilities:

1.  **Gemma-4-E2B**: Runs in 2.6 GB and opens a 32K context window, demonstrating offline capability on phone.
2.  **Gemma 3n E2B**: Uses 4096 tokens in a multi-modal input model, highlighting its flexibility.

The article also highlights the integration of built-in skills like:

*   **Calculate Hash**: A built-in skill for hashing text, useful for various applications.
*   **Create Calendar Event**: A built-in skill that enables writing to the OS calendar.

However, it's noted that community-created skills are only available in 12 total and have a different interface compared to built-in ones.

**Key Takeaways**

*   Google AI Edge Gallery supports MCP connections on Android devices with cloud storage capabilities.
*   LiteRT-LM (TensorFlow Lite Mobile Inference Runtime) is a native mobile runtime developed by Google Research.
*   The app offers various agent models, including Gemma, and can deploy skills built-in or community-created.