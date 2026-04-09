---
title: Windows 11 to add an AI agent that runs in background with access to personal folders, warns of security risk
url: https://www.windowslatest.com/2025/11/18/windows-11-to-add-an-ai-agent-that-runs-in-background-with-access-to-personal-folders-warns-of-security-risk/
site_name: hackernews_api
fetched_at: '2025-11-18T11:07:09.373356'
original_url: https://www.windowslatest.com/2025/11/18/windows-11-to-add-an-ai-agent-that-runs-in-background-with-access-to-personal-folders-warns-of-security-risk/
author: Mayank Parmar
date: '2025-11-17'
published_date: '2025-11-17T23:44:36+00:00'
description: Windows 11 adds AI agent that runs in background with access to personal folders
tags:
- hackernews
- trending
---

Home


Windows 11

* Windows 11



Microsoft is moving forward with its plans to turn Windows 11 into a full-fledged “AI” operating system amidstCopilot backlash.

The first big move in that direction is an experimental feature called “Agent Workspace,” which gives AI agents access to the most-used folders in your directory, such as Desktop, Music, Pictures, and Videos. It will also allow AI agents to have their own runtime, desktop, user account, and ability to always run in the background if you turn on the feature.

## New agentic features in Windows 11

As soon as I installed Windows 11 Build 26220.7262, Windows Latest noticed a new toggle “Experimental agentic features” inside the “AI Components” page in theSettingsapp >System.

Image Courtesy: WindowsLatest.com

This turns on “Agent Workspace,” but it doesn’t work right now, and if you’re wondering, it’s only available to Windows Insiders in the Dev or Beta Channel.

### What are AI Agents and how do they work?

Agent mode in ChatGPT

If you’ve ever used ChatGPT, you might have come across ‘Agents.’ AI Agents have their own interface, and they navigate just like a human.

Agent mode in GPT opened Azure container, Chromium and Linux to create a presentation | Image Courtesy: WindowsLatest.com

For example, if you ask ChatGPT’s Agent to book a trip, it’ll open Chromium on Linux in an Azure container, search for the query, visit different websites, navigate each page, and book a flight ticket using your saved credentials. An AI Agent tries to behave like a human, and it can perform tasks on your behalf while you sit back and relax (spoiler: you don’t).

That’s the core idea Silicon Valley is trying to sell. However, it doesn’t work as well as companies like OpenAI and Perplexity claim.

Up until now, these Agents have been limited to cloud containers with Chromium and Linux terminal access, but asMicrosoft wants Windows 11 to become an “AI-native” OS, it’s addingAgent Workspace.

## What the hell is Agent Workspace on Windows 11?

Agent workspace is a separate, contained Windows session made just for AI agents, where they get their own account, desktop, and permissions so they can click, type, open apps, and work on your files in the background while you keep using your normal desktop.

This feature is completely optional and is never turned on by default.To test it, I turned on the feature, and Microsoft created an extra “workspace.” It’s very similar to how Windows Sandbox or Workspaces in Microsoft Edge work, but it could be a potential security disaster, as evenMicrosoft is warning about risks.

Image Courtesy: WindowsLatest.com

When Windows spins up this extra workspace, it gives it limited access (like specific folders such as Documents or Desktop) and keeps its actionsisolatedandauditable.

Each agent can have its own workspace and access rules, so what one agent can see or do doesn’t automatically apply to others, and you stay in control of what they’re allowed to touch.

“The creation of the agent workspace where agents can work in parallel with a human user, enabling runtime isolation and scoped authorization,” Microsoftnotedin a support document. “This provides the agent with capabilities like its own desktop while limiting the visibility and accessing the agent has to the user’s desktop activity.”

#### A bit similar to Sandbox?Not technically

You might find the idea of Agent Workspace a bit similar toWindows Sandbox. Microsoft argues that Windows Agent Workspace is more “efficient” than a virtual machine, such as Windows Sandbox, because:

* The agent still has security isolation
* Supports parallel execution
* and gives you control… as you can allow the Agent to access your personal folders even when it’s running in a separate isolated instance. Or you can see the logs.

“The overall experience and security model are actively being refined to support key principles of transparency, safety, and user control,” Microsoft says.

While Agent and Sandbox have similarities like isolation, Sandbox does not have access to your personal files or folders. In Windows Sandbox, Microsoft creates an isolated and hardware-based virtualization, and even a separate kernel to keep the sandbox completely separate.

When you turn off Sandbox, all of its activities are deleted. We can’t say the same for AI agents.

## Windows 11 lets AI agents into your Documents and Desktop folders by default, with read and write access

When you turn on the feature, you’re giving agents access to apps and even local folders, such as Desktop, Music, Pictures, and Videos.

I dug a bit into the implementation, and it looks like Agent Workspace has limited access to your local folder inside (C:\Users\<username>\). When the toggle “Experimental Agent features” is enabled, Windows getsread and writeaccess to the following folders: Downloads, Desktop, Videos, Pictures, and Music.

These folders are called “Known folders,” a feature that Microsoftaddedwith Windows Vista.

Since Agent workspace is using known folders, it can always locate these folders (Documents, Downloads, Desktop, Videos, Pictures, Music) even if you’ve redirected the location elsewhere in the filesystem.

### Why do Agents need access to my personal folders?

To run things for you. Simple.Agent Workspace requires access to apps or private folders to perform actions on your behalf. Microsoft insists that it’s taking care of security implications by giving Agent Workspace its own authorisation (a separate account, similar to your user account), runtime isolation.

Each agent will have its own defined set of dos and don’ts.

The idea is to give Agents their own backyard on your PC, and let them run in the background all the time. You’ll be able to monitor the logs and keep an eye on agent activity.

### Agents also need your apps, not just files or folders

https://www.windowslatest.com/wp-content/uploads/2025/11/Copilot-on-Windows-demo.mp4

While each agent gets its own account, independent of your personal account, an agent wouldstillneed access to your apps.

Now, when you turn on the feature, Microsoft is giving access to all your installed apps that you can use. But you can specifically install apps for your agents. Or you can maintain different user accounts on Windows, and then install apps for those specific users.If this isn’t an unnecessary solution to a problem no one had, then what is…?

### AI Agents may have performance issues

In our tests, Windows Latest observed that the experimental toggle warns of potential performance issues, and it makes sense.

AI agents are going to run in the background all the time and use RAM or CPU, depending agent’s activity. However, Microsoft’s early benchmarks suggest they won’t really drain PCs of their power. Microsoft won’t give us the numbers for obvious reasons.

Microsoft only says AI Agents will use a limited amount of RAM and CPU.

By default, these agents are lightweight, but the catch is that some Agents could be resource-intensive. We’re going to find out later.

## Despite the AI push, Microsoft still insists it deeply cares about power users

Ironically, this new agentic experience has been announced afterMicrosoft’s Windows boss promised to improve Windows for everyone, including developers.

As Windows Latest reported recently, whenMicrosoft’s Windows boss teased an “Agentic” future for Windows, hundreds and thousands of users criticised the leadership. Microsoft’s executive closed the replies/comments on his post to calm the public, but the move backfired as more users started shaming Windows’ Agentic shift.

Later, Microsoft’s Windows boss promised that it would make Windows better for everyone, and it deeply cares about developers.

“We know we have work to do on the experience, both on the everyday usability, from inconsistent dialogs to power user experiences. When we meet as a team, we discuss these paint points and others in detail, because we want developers to choose Windows,”saysPavan Davuluri, who is the boss of Windows and devices at Microsoft.”

“….I’ll boil it down, we care deeply about developers,” he added.

While the Experimental Agents Feature is optional, it makes it quite obvious Microsoft will not stop investing in AI for Windows 11, and Agentic OS is the future, whether you like it or not.

Add as preferred source

Support independent blog

Ask a question (Forum)

WL Newsletter

###### WL Newsletter!

Stay ahead with the latest Windows, IT, and AI updates. Trusted by 50,000+ subscribers.

Name
Email
Join for Free

About The Author

Mayank Parmar

Mayank Parmar is an entrepreneur who founded Windows Latest. He is the Editor-in-Chief and has written on various topics in his seven years of career, but he is mostly known for his well-researched work on Microsoft's Windows. His articles and research works have been referred to by CNN, Business Insiders, Forbes, Fortune, CBS Interactive, Microsoft and many others over the years.

#### RELATED ARTICLESMORE FROM AUTHOR



### Microsoft misses Windows 10 so badly it’s still using it to promote Windows 11







### Fortnite creator & Elon Musk urge Windows 11 to add vertical taskbar, remove MSA amid Copilot AI push







### Windows 11 KB5068861 won’t install, File Explorer SMB search not working on network shares, and other issues







### After Windows 11 AI OS backlash, Microsoft tells angry power users ‘we care deeply about you’







### New Windows 11 Copilot ad accidentally shows AI fumbling a basic text size setting







### Windows 11 25H2 quietly rolls out gaming boost, including for handheld performance
