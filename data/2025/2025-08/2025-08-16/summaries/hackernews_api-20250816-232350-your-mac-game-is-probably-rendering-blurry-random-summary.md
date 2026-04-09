---
title: Your Mac Game Is Probably Rendering Blurry – Random Thoughts
url: https://www.colincornaby.me/2025/08/your-mac-game-is-probably-rendering-blurry/
date: 2025-08-15
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-08-16T23:23:50.228114
---

# Your Mac Game Is Probably Rendering Blurry – Random Thoughts

**Problem or Opportunity**

The article discusses a common problem faced by game developers who create full-screen games for Macs with notched displays: rendering blurry frames due to incorrect resolution selection. The author, Colin Cornaby, submits an issue on Apple's Feedback section (FB13375033) and provides technical insights into how this bug affects both macOS users and app developers building full-screen games using AppKit.

**Market Indicators**

The article notes that:

* Over 9,000 feedback requests have been submitted for macOS issues since September 2023.
* The issue is open on the Feedback platform, indicating a significant number of user requests.
* CGDisplayCopyAllDisplayModes returns resolutions from both full area and under-menu-bar regions, which can lead to incorrect rendering.

**Technical Feasibility**

As a solo developer, technical feasibility is essential. The article mentions that:

* Most games default to the first resolution on the list (disregarding the notch region).
* A game may not account for the 3:2 aspect ratio of Mac computers with notched displays.
* CGDisplayCopyAllDisplayModes requires specific permissions and capabilities from Apple's Graphics Services library.

Regarding time investment, the article does not provide any direct estimates. However, it is essential to consider that developing games with complex graphics requires significant expertise in game development, rendering, and display-related issues.

**Business Viability Signals**

Several signals indicate business viability:

* Apple pays a fee for submitting feedback requests through their Feedback platform (FB13375033).
* The problem has been open on the Feedback platform since September 2023, indicating a steady stream of interest.
* A significant number of user requests have been submitted.

**Actionable Insights for Building a Profitable Solo Developer Business**

Based on the article's findings, I extract the following insights:

1. **Highlight game developers who cater to Mac users**: Specializing in developing games that are optimized for Mac with notched displays can provide an opportunity to create more revenue.
2. **Offer comprehensive display-related features and support**: Developing resources (e.g., tutorials, documentation) that explain display configurations and recommendations can attract customers.
3. **Target app developers building full-screen games**: Catering to them with improved support, debugging tools, or optimizing frameworks for Mac's unique displays could increase revenue potential.

To mitigate potential risks:

1. **Conduct thorough research on your target audience**: Understand the needs and pain points of both game developers and Mac users with notched displays.
2. **Develop a deep understanding of Apple's Graphics Services library**: Ensure you are well-versed in the required permissions, capabilities, and limitations.

By understanding this problem, recognizing its opportunities, and addressing technical challenges, solo game developers can create a more profitable business focused on creating games that cater to Mac users with notched displays.
