---
title: 'GitHub - alibaba/page-agent: JavaScript in-page GUI agent. Control web interfaces with natural language. · GitHub'
url: https://github.com/alibaba/page-agent
site_name: github
content_file: github-github-alibabapage-agent-javascript-in-page-gui-ag
fetched_at: '2026-03-08T07:24:31.394210'
original_url: https://github.com/alibaba/page-agent
author: alibaba
description: JavaScript in-page GUI agent. Control web interfaces with natural language. - alibaba/page-agent
---

alibaba



/

page-agent

Public

* NotificationsYou must be signed in to change notification settings
* Fork115
* Star1.2k




 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

652 Commits
652 Commits
.github
.github
 
 
.husky
.husky
 
 
.vscode
.vscode
 
 
docs
docs
 
 
packages
packages
 
 
scripts
scripts
 
 
.gitignore
.gitignore
 
 
AGENTS.md
AGENTS.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
eslint.config.js
eslint.config.js
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
tsconfig.base.json
tsconfig.base.json
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# Page Agent






The GUI Agent Living in Your Webpage. Control web interfaces with natural language.

🌐English|中文

👉🚀 Demo|📖 Documentation|📢 Join HN Discussion

page-agent-demo-0227.mp4

## ✨ Features

* 🎯 Easy integrationNo need forbrowser extension/python/headless browser.Just in-page javascript. Everything happens in your web page.The best tool for your agent to control web pages.
* No need forbrowser extension/python/headless browser.
* Just in-page javascript. Everything happens in your web page.
* The best tool for your agent to control web pages.
* 📖 Text-based DOM manipulationNo screenshots. No OCR or multi-modal LLMs needed.No special permissions required.
* No screenshots. No OCR or multi-modal LLMs needed.
* No special permissions required.
* 🧠 Bring your own LLMs
* 🎨 Pretty UI with human-in-the-loop
* 🐙 Optionalchrome extensionfor multi-page tasks.

## 💡 Use Cases

* SaaS AI Copilot— Ship an AI copilot in your product in lines of code. No backend rewrite needed.
* Smart Form Filling— Turn 20-click workflows into one sentence. Perfect for ERP, CRM, and admin systems.
* Accessibility— Make any web app accessible through natural language. Voice commands, screen readers, zero barrier.
* Multi-page Agent— Extend your agent's reach across browser tabs with the optionalchrome extension.

## 🚀 Quick Start

### One-line integration

Fastest way to try PageAgent with our free Demo LLM:

<
script

src
="
{URL}
"
crossorigin
="
true
"
>
</
script
>

Mirrors

URL

Global

https://cdn.jsdelivr.net/npm/page-agent@1.5.2/dist/iife/page-agent.demo.js

China

https://registry.npmmirror.com/page-agent/1.5.2/files/dist/iife/page-agent.demo.js

⚠️For technical evaluation only.This demo CDN uses our freetesting LLM API. By using it, you agree to itsterms.

### NPM Installation

npm install page-agent

import

{

PageAgent

}

from

'page-agent'

const

agent

=

new

PageAgent
(
{


model
:
'qwen3.5-plus'
,


baseURL
:
'https://dashscope.aliyuncs.com/compatible-mode/v1'
,


apiKey
:
'YOUR_API_KEY'
,


language
:
'en-US'
,

}
)

await

agent
.
execute
(
'Click the login button'
)

For more programmatic usage, see📖 Documentations.

## 🤝 Contributing

We welcome contributions from the community! Follow our instructions inCONTRIBUTING.mdfor environment setup and local development.

Please readCode of Conductbefore contributing.

## 👏 Acknowledgments

This project builds upon the excellent work ofbrowser-use.

PageAgentis designed forclient-side web enhancement, not server-side automation.

DOM processing components and prompt are derived from browser-use:

Browser Use
Copyright (c) 2024 Gregor Zunic
Licensed under the MIT License

Original browser-use project: <https://github.com/browser-use/browser-use>

We gratefully acknowledge the browser-use project and its contributors for their
excellent work on web automation and DOM interaction patterns that helped make
this project possible.

Third-party dependencies and their licenses can be found in the package.json
file and in the node_modules directory after installation.

## 📄 License

MIT License

⭐ Star this repo if you find PageAgent helpful!

## About

JavaScript in-page GUI agent. Control web interfaces with natural language.

alibaba.github.io/page-agent/

### Topics

 javascript

 agent

 typescript

 web

 ai

 ui-automation

 browser-automation

 ai-agents

### Resources

 Readme



### License

 MIT license


### Code of conduct

 Code of conduct


### Contributing

 Contributing


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

1.2k

 stars


### Watchers

6

 watching


### Forks

115

 forks


 Report repository



## Releases15

🌟 v1.5.2

 Latest



Mar 5, 2026



+ 14 releases

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors6

## Languages

* TypeScript82.3%
* JavaScript11.0%
* CSS6.2%
* HTML0.5%
