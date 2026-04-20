---
title: GitHub - browser-use/browser-use: 🌐 Make websites accessible for AI agents. Automate tasks online with ease. · GitHub
url: https://github.com/browser-use/browser-use
date:
site: github
model: llama3.2:1b
summarized_at: 2026-03-22T11:15:25.855420
---

# GitHub - browser-use/browser-use: 🌐 Make websites accessible for AI agents. Automate tasks online with ease. · GitHub

**Browser-Use: Automatic Website Automation for AI Agents**

**Overview**
--------

** Browser-Use** is an open-source tool for automated web scraping using artificial intelligence (AI) and machine learning (ML). It allows users to bypass website sign-in requirements, automate tasks online, and access static websites. This repository is a landing page providing installation instructions, demo code examples, and a starter setup.

### Key Features

*   Website automation: bypass signs-ins and save time
*   Static content accessibility: focus on ML-based models for image/video description.
*   Code examples: provide templates and use cases to understand how `Browser-Use` works.
*   Documentation: view official documentation with tutorials, guides, and examples.

### Installing Browser-Use

**Setting up a Python environment (Optional)**

```bash
pip install uvx [python-name]==3.11 browser-use
```

**Starter setup**

This creates `Browser-Use_default.py`:

```bash
uvx browser-use init --template default
```

Open the downloaded file in your preferred IDE and explore its contents.

### Example Use Cases

| Task          | Description                          |
|---------------|---------------------------------------|
| Form-Filling    | Fill in a job application                     |
| Grocery-Shopping | Put items into Instacart                        |
| Personal-Assistant| Find parts for a custom PC                     |

**Example Code**

```python
import asyncio
from Browser import Browser, ChatBrowserUse

async def main():
    # Set up the environment and add `browser-use` to your system's PATH.
    await browser.init()

    agent = Bot()

    # Use the chat API in a conversational flow...
    llm=ChatGoogle(model='gemini-3-flash-preview')

    browser = Browser("https://example.com")

    async def run():
        browser.goto(browser_use)
        task=task("The number of stars is 100.")
        llm=ChatBrowserUse(llm=model="ClaudeSonnet6FlashPreview").
        # ... and the rest...

    if __name__=="__main__":
       asyncio.run(run())
```

**Get Started**

Visit our website and follow these steps:

1. Download `Browser-Use_default.py`.
2. Set up your Python environment.
3. Run `uvx browser-use init` to start `Browser-Use`.
4. Import and use `ChatBrowserUse` as a wrapper around ML models (e.g., `ClaudeSonnet6FlashPreview`).
5. Explore the provided examples from our website!
```
### Quickstart Templates

```bash
export VIRTUAL_ENV=env-name .venv activate
source venv-Scripts activating env-python
uvx browser-use init --template default
```
