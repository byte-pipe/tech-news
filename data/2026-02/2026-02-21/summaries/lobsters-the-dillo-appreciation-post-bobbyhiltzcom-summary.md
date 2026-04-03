---
title: The Dillo Appreciation Post | BobbyHiltz.com
url: https://bobbyhiltz.com/posts/2026/02/dillo-appreciation/
date: 2026-02-21
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-21T06:03:30.508347
---

# The Dillo Appreciation Post | BobbyHiltz.com

# The Dillo Apprreciation Post

This post details the author's continued appreciation for the Dillo web browser and highlights several custom scripts and page actions they've created to enhance its functionality.

## Page Actions
### Webmentions
The author has created Bash scripts to streamline the process of saving web pages as "mentions" (like bookmarks with extra information). These scripts automatically copy the URL and title to the clipboard, which are then formatted into a specific HTML structure for use with a custom feed parser.
### Sharing to other services
Two page actions are described for sharing pages to external services: Wallabag (a read-it-later service) and Linkhut (a social bookmarking site). These actions pre-fill submission pages with the page's URL and title.

## Browsing YouTube and Wallabag
### YouTube (dillPype?)
The author developed a Python script called dillPype to manage a list of YouTube videos. Inspired by Philip Wattamore's RSS feeds page, the script fetches video entries from YouTube channel RSS feeds, sorts them by date, and outputs an HTML file. This allows for viewing a list of videos in Dillo, with a link to open each video in an external player like mpv.
### Wallabag (dillBag?)
A Python script is used to fetch and display unread articles from a Wallabag feed. The script retrieves the title and link of articles and outputs them to an HTML file. This enables the author to access saved articles from Wallabag within Dillo, particularly useful on mobile devices.

## Key Points
- The author actively uses Dillo and has developed custom scripts and page actions to improve its usability.
- These enhancements include simplified bookmarking, sharing to other services, and managing YouTube and Wallabag content.
- The author provides the code for the Python scripts, encouraging others to utilize and adapt them.
- The post acknowledges the work of others in the community, specifically mentioning a post by MacKeenzie regarding YouTube RSS feeds.
