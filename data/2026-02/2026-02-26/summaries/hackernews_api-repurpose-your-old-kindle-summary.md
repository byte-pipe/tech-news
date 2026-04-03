---
title: Repurpose your old Kindle
url: https://www.mariannefeng.com/portfolio/kindle/
date: 2026-02-25
site: hackernews_api
model: gemma3n:latest
summarized_at: 2026-02-26T06:01:11.541918
---

# Repurpose your old Kindle

# Repurpose your old Kindle

This article details how to repurpose an old Kindle (specifically Kindle Touch 4th Generation/K5/KT) into a live bus arrival feed, offering a cost-effective alternative to commercial solutions. The process involves jailbreaking the Kindle, installing necessary software, setting up SSH, running a server to generate a displayable image, and creating a custom KUAL app to control the dashboard's display.

## Key Steps:

*   **Jailbreaking:** The first step is to jailbreak the Kindle using a specific tar file and following instructions from the Kindle hacking community.
*   **Software Installation:** Install KUAL (a custom app launcher) and MRPI (for installing custom apps) on the jailbroken Kindle, potentially requiring a hotfix guide beforehand. OTA updates are disabled.
*   **SSH Setup:** Establish an SSH connection to the Kindle using a KUAL extension (USBNetwork) and further configured via a blog post, enabling remote access.
*   **Server Setup:** Create a server that fetches bus arrival data (using the NJ Transit GraphQL API as an example), formats it into an HTML image, and generates a PNG image every 3 minutes using `wkhtmltoimage`. The server serves this image via a dedicated endpoint.
*   **KUAL App Creation:** Develop a custom KUAL app with a menu item to start the dashboard. This involves a script (`start.sh`) that handles signals to prevent premature termination.

## Detailed Breakdown:

*   **Jailbreaking & Software:** The article directs readers to the Kindle hacking bible for jailbreaking instructions and the Kindle modding wiki for installing KUAL and MRPI, noting potential difficulties and the need for specific steps.
*   **SSH:** SSH is set up using a KUAL extension and further configured using a blog post, focusing on running the extension and the `wkhtmltoimage` command via USB.
*   **Data Acquisition & Server:** The author uses the NJ Transit GraphQL API to retrieve bus arrival times. A server is created using Node.js, utilizing `wkhtmltoimage` to generate a PNG image from HTML content fetched from the API. The server serves the generated image through specific endpoints.
*   **Image Resolution & Display:** The Kindle's screen resolution (600x800) is crucial, and the image generation process involves rotation and translation to align the bus times correctly on the screen.
*   **KUAL Dashboard Control:** A custom KUAL app is created with a "Start dashboard" menu item that executes a script to initiate the dashboard display, handling signals to prevent the script from exiting prematurely.
