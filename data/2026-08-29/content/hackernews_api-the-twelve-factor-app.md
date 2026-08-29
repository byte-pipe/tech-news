---
title: The Twelve-Factor App
url: https://12factor.net/
site_name: hackernews_api
content_file: hackernews_api-the-twelve-factor-app
fetched_at: '2026-08-29T15:28:56.832818'
original_url: https://12factor.net/
author: Adam Wiggins
date: '2026-08-27'
description: A methodology for building modern, scalable, maintainable software-as-a-service apps.
tags:
- hackernews
- trending
---

# Introduction

In the modern era, software is commonly delivered as a service: calledweb apps, orsoftware-as-a-service. The twelve-factor app is a methodology for building software-as-a-service apps that:

* Usedeclarativeformats for setup automation, to minimize time and cost for new developers joining the project;
* Have aclean contractwith the underlying operating system, offeringmaximum portabilitybetween execution environments;
* Are suitable fordeploymenton moderncloud platforms, obviating the need for servers and systems administration;
* Minimize divergencebetween development and production, enablingcontinuous deploymentfor maximum agility;
* And canscale upwithout significant changes to tooling, architecture, or development practices.

The twelve-factor methodology can be applied to apps written in any programming language, and which use any combination of backing services (database, queue, memory cache, etc).