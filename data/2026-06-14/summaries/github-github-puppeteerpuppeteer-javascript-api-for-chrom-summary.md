---
title: GitHub - puppeteer/puppeteer: JavaScript API for Chrome and Firefox · GitHub
url: https://github.com/puppeteer/puppeteer
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-06-14T11:52:49.711939
---

# GitHub - puppeteer/puppeteer: JavaScript API for Chrome and Firefox · GitHub

**Puppeteer Library Overview**

Puppeteer is a popular JavaScript library for controlling Chrome or Firefox over theDevTools Protocol WebDriver bi-directional (BiDi). It provides a high-level API to interact with both browsers in the headless mode, allowing users to execute automation tests and applications.

**Main Features and Capabilities**

* High-level API for customizing browser interactions
* Emulates the DevTools protocol for seamless interaction with both Chrome and Firefox
* Supports headless mode (no visible UI)
* Enables execution of automation tests and applications

**Installation and Setup**

To install Puppeteer, run the following command:

`npm i puppeteer`

Alternatively, you can install it as a library without downloading Chrome:

```bash
 npm i puppeteer-core
```

Or configure your package manager to allow the installation script to run.

**MCP Integration**

Puppeteer provides an MCP (Browser Management Control Point) server for browser automation and debugging. It supports two experimental APIs: WebMCPAPI

* Launches a Chromium DevTools Proxy server in headless mode
* Allows for debugging, inspection, and testing of Chrome applications
* Supports keyboard navigation and other edge cases

**Example Usage**

Here's an example of using Puppeteer to launch the browser, navigate to a URL, and interact with the browser:

```javascript
import { puppeteer } from 'puppeteer';

(async () => {
    // Launch the browser in headless mode
    const browser = await puppeteer.launch({
        args: ['--headless', '--no-sandbox'],
    });

    // Create a new page object
    const page = await browser.newPage();

    // Navigate to a URL
    await page.goto('https://developer.chrome.com/docs/devtools/');

    // Set the screen size
    await page.setViewport({
        width: 1080,
        height: 1024,
    });

    // Perform some assertions
    await page.waitForSelector('#my-element');
})();
```