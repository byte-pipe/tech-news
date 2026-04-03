---
title: Notes on clarifying man pages
url: https://jvns.ca/blog/2026/02/18/man-pages/
date: 2026-02-20
site: lobsters
model: gemma3n:latest
summarized_at: 2026-02-20T06:02:47.311883
---

# Notes on clarifying man pages

# Notes on Clarifying Man Pages

This article explores ways to improve the usability of man pages, drawing on experiences with cheat sheets and feedback from users. The author suggests that man pages themselves could benefit from incorporating elements of cheat sheets, better organization, and more examples.

## Key Ideas for Improving Man Pages:

* **Options Summary:** Similar to the `rsync` man page, a concise summary of each option could be beneficial, especially for long lists of options.
* **Categorized Options:** Organizing options by category (e.g., "General," "Startup," "Tracing") instead of alphabetically could improve discoverability.
* **Cheat Sheet Section:** Including a condensed, ASCII-art style cheat sheet at the beginning of a man page, as seen in Perl man pages, could provide quick reference.
* **Examples:** Incorporating examples, like those found in the OpenBSD man pages and the `curl` man page, is highly valued by users and helps illustrate how to use the command.
* **Table of Contents and Internal Links:** Adding a table of contents (especially in HTML versions) and internal hyperlinks between sections would make navigation easier.
* **Data in Tables:** Presenting information, like ASCII character codes in the `ascii` man page, in a table format can improve readability and scanning.
* **GNU Approach vs. OpenBSD:** The GNU coreutils man pages often lack examples compared to OpenBSD's, suggesting a potential area for improvement in the GNU project.
* **External Tools:** Tools like `fish` (for tab completion), `tldr.sh` (for community-driven examples), and DashMac (a docs browser with a man page viewer) offer alternative and helpful ways to access man page information.

## Challenges and Considerations:

* **Maintaining a Different Format:** Implementing improvements like tables of contents and hyperlinks requires a toolchain (like Git's AsciiDoc system) to manage the documentation.
* **Universal Option Lookup:** A system for easily looking up the function of a specific option (e.g., "what does -a do?") would be highly desirable.
* **Political Aspects:** The author notes the potentially sensitive nature of the GNU vs. OpenBSD documentation approach.

## Overall Perspective:

The author believes that man pages are becoming increasingly difficult to navigate as software becomes more complex. Incorporating elements from cheat sheets, better organization, and more examples could significantly enhance their usability.
