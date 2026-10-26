---
title: Overgrown, when plants invade your abandoned tabs | Charlie Gerard | Senior research engineer & Creative Technologist Charlie Gerard | Senior research...
url: https://charliegerard.dev/blog/overgrown-extension/
date: 2026-10-22
site: hackernews_api
model: llama3.2:1b
summarized_at: 2026-10-26T17:25:41.079188
---

# Overgrown, when plants invade your abandoned tabs | Charlie Gerard | Senior research engineer & Creative Technologist Charlie Gerard | Senior research...

## Overgrown: A Chrome Extension Where Plants Invade Your Abandoned Tabs

### Key Points:

* A Chrome extension that simulates an overgrown state where plants invade abandoned tabs
* The extension has a neglect clock on each tab that runs while the tab is out of view, causing plants to grow over the tab
* When a tab is neglected for too long, the page behind the vines is walled off, preventing access
* Users can slash through the vines by dragging across them to free the tab

### Demo:

[Link to repository]

### The Idea:

* Every tab has a "neglect clock" that runs while the tab is not displayed and stops while it is visible
* As the tab is neglected, plants grow over it with time passing
* Once a tab is more than 5% overgrown, the page behind the vines is wallowed, and users can only access the tab after slashing through the vines
* Users can choose from three "weapons" (machete, chainsaw, and flamethrower) to use to clear the vines

### The Extension:

* The code is divided into three main components: background worker, content script, and popup folder
* The background worker starts the simulation on each open tab and forgets it when it closes
* The content script displays the plants and animation on the tabs and handles the UI
* The popup folder contains widgets for the time setting, weapon choice, tab list, and current state display

### Features and Fun Mechanics:

* Users can pick their preferred weapon of choice for clear-cutting vines
* The jungle grows back over time, requiring more frequent clearing
* A new tab will only be considered finished after being cleared and freed from the jungle
* For fun, users can see the time it takes to clear a particularly difficult-to-reach tab.