---
title: Xcode 27 Extends Agent Integration, Revamps UI, and Introduces DeviceHub - InfoQ
url: https://www.infoq.com/news/2026/06/xcode-27-agents-device-hub/
site_name: tldr
content_file: tldr-xcode-27-extends-agent-integration-revamps-ui-and
fetched_at: '2026-06-30T19:38:46.553991'
original_url: https://www.infoq.com/news/2026/06/xcode-27-agents-device-hub/
date: '2026-06-30'
description: At WWDC 2026, Apple introduced Xcode 27, which makes it easy to kick off tasks with coding agents, iterate on new project ideas, and customize the workspace. It also introduces DeviceHub for unified s
tags:
- tldr
---

InfoQ HomepageNewsXcode 27 Extends Agent Integration, Revamps UI, and Introduces DeviceHub

 Mobile
 

From Log Noise to Incident Intelligence: A Maturity Model for AI-Assisted Observability (Webinar Jul 9th) 

# Xcode 27 Extends Agent Integration, Revamps UI, and Introduces DeviceHub

Jun 15, 20262
									min read

by

* Sergio De Simone

#### Follow us on

Youtube
232K Followers

Linkedin
26K Followers

Instagram
New

RSS
19K Readers

X
57.1k Followers

Facebook
21K Likes

Bluesky
New

At WWDC 2026,Apple introduced Xcode 27, which makes it easy to kick off tasks with coding agents, iterate on new project ideas, and customize the workspace. It also introduces DeviceHub for unified simulator and device management, along with enhancements to Organizer and Instruments, among many other improvements.

Xcode 27 extends toolbar and theme customization, introducing a refreshed layout for key controls. Elements such as history navigation and editor controls, previously located in the jump bar, have been moved into the toolbar for quicker access. Most notably, the toolbar is now fully customizable, allowing you to add, remove, and reorder items to suit your workflow.

Theme customization has also been significantly improved, making it easier to configure themes using a richer, more intuitive UI. For example, you can adjust text color intensity and background levels using simple sliders.

Developers can also assign distinct themes to distinct workspaces:

This helps identify at a glance which project is which. So, if you find yourself needing to quickly differentiate projects that are perhaps eerily similar side by side, try giving them unique themes.

Warnings and errors have also been revamped to better integrate with the current theme, adopting a more subtle appearance meant to reduce distraction and help distinguish them from build-time issues.

Xcode 27 introduces a completely redesigned project creation experience, making it faster to start new projects and eliminating the need to name them upfront. Untitled projects allow you to quickly experiment and only assign a name when it becomes necessary. Additionally, when opening an individual Swift file outside of a project—such as one shared by a coworker—Xcode now presents it within a workspace environment, giving you access to features like playground results and UI previews.

Working with coding agents in Xcode 27 is more seamless thanks to a new UI that integrates the conversation transcript directly into the editor pane. The transcript appears as an editor itself, allowing it to work naturally with tabs, split views, and your preferred workspace organization. For example, you can use the /pl (plan) command to outline the details the agent should consider. The agent then gathers the necessary context without making any changes and presents a complete plan for review and feedback.

Another new feature in Xcode 27 is the DeviceHub, which lets you explore and evaluate apps across both simulators and physical devices. It provides a unified interface for common tasks such as taking screenshots, rotating devices, and adjusting accessibility settings like contrast, dynamic type size, and light or dark appearance.

DeviceHub makes it a breeze to work with simulators, but the coolest thing is what I've shared so far works with physical devices as well. If I open the sidebar, I see a combined list of simulators and devices. I have a paired iPad Pro already running my app, and I can see and control it directly in Device Hub.

Xcode 27 also expands support for app localisation, with enhanced AI integration and a redesigned Organiser that highlights the highest-impact issues first. It unifies diagnostics and metrics in a single view and extends support forapp recommendations and sets of goals, such as launch time, hang rate, disc rights, battery, and storage, helping youtrack them.

There is much more to Xcode 27 than can be covered here. Be sure to watch theWWDC session recordingfor a complete overview.*All images courtesy of Apple

 

## About the Author

 

 

 

#### Sergio De Simone

Show more
Show less

### Rate this Article

Adoption

Style

 Author Contacted

#### This content is in theMobiletopic

##### Related Topics:

* Development
* Mobile
* Agents
* Xcode
* Apple
* iOS
* MacOS
* IDE

* #### Related Editorial
* #### Related Sponsors##### Understanding AI Agent Security
* ##### Understanding AI Agent Security
* #### Related SponsorConfidently test, evaluate, and red-team your LLM apps withPromptfoo— catch regressions, benchmark models, and ship high-quality AI features faster; start testing your prompts today.Learn More.

### Related Content

### The InfoQNewsletter

A round-up of last week’s content on InfoQ sent out every Tuesday. Join a community of over 250,000 senior developers.View an example

Enter your e-mail address

Select your country

Select a country

I consent to InfoQ.com handling my data as explained in this 
Privacy Notice
.

We protect your privacy.