---
title: 👾 Server Access Logs with GoAccess - DEV Community
url: https://dev.to/annavi11arrea1/server-access-logs-with-goaccess-333d
site_name: devto
content_file: devto-server-access-logs-with-goaccess-dev-community
fetched_at: '2026-06-23T10:19:44.571150'
original_url: https://dev.to/annavi11arrea1/server-access-logs-with-goaccess-333d
author: Anna Villarreal
date: '2026-06-21'
description: 'Part 1: Self-hosting on Jetson Orin Nano 👽 Jetson Orin Nano Web Server Follow-up... Tagged with security, webdev, learning, linux.'
tags: '#security, #webdev, #learning, #linux'
---

Live HTML dashboards and bot detection

Part 1:Self-hosting on Jetson Orin Nano

### 👽 Jetson Orin Nano Web Server Follow-up 👽

Cool! Now that the mini web server is up and running, how can I see web traffic easily? I discovered GoAccess recently, which is a free and open source tool for checking out server logs in real time. There are two way to view it. At first I was happy to just see nicely-parsed server logs in the terminal. Ahhhh, organization! It gives you a bunch of interesting stuff to look at.

Here is what the terminal view looks like:

Dats cool

You know, inviting traffic to a webserver invokes anxiety. Having half an idea of what is happening helps ease tension for sure. I was really excited to find this tool. You can open go access in the terminal to display different information with different views. I will leave the explaining to the official documentation found here:GoAccess Docs

But the web developer in me was super excited to find a very human-readable html version readily available. Using a reverse proxy through nginx, you can view all the stats on a web page locally. It also allows you to pick a theme and customize how the information is displayed. Be sure to check out the settings and chart options!

Here is what the html view produces:

Stats for silly hoomins.

Idk about you, but this is my super exciting find for the day.

I think my next step is to connect an agent that reads the logs and alerts me on set parameters.

I'm interested to hear what tools all of you use to enhance web server monitoring?

What's the best agent for web analytics, in your opinion?

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse