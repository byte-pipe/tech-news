---
title: 'GitHub - Ademking/MD-This-Page: Convert any web page to clean, readable Markdown with just one click. · GitHub'
url: https://github.com/Ademking/MD-This-Page
site_name: tldr
content_file: tldr-github-ademkingmd-this-page-convert-any-web-page-t
fetched_at: '2026-06-20T11:42:28.359697'
original_url: https://github.com/Ademking/MD-This-Page
date: '2026-06-20'
description: Convert any web page to clean, readable Markdown with just one click. - Ademking/MD-This-Page
tags:
- tldr
---

Ademking

 

/

MD-This-Page

Public

* NotificationsYou must be signed in to change notification settings
* Fork75
* Star864

 
 
 
 
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

17 Commits
17 Commits
.github/
workflows
.github/
workflows
 
 
assets
assets
 
 
tabs
tabs
 
 
.gitignore
.gitignore
 
 
.prettierrc.mjs
.prettierrc.mjs
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
background.ts
background.ts
 
 
content.ts
content.ts
 
 
package.json
package.json
 
 
pnpm-lock.yaml
pnpm-lock.yaml
 
 
postcss.config.js
postcss.config.js
 
 
screenshot.png
screenshot.png
 
 
tailwind.config.js
tailwind.config.js
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# .MD this page

Turn any webpage into clean, LLM-ready Markdown in one click.Strip the browser, keep the structure, then copy or download instantly.

### How it works

1. Open any webpage
2. Right-click → ".MD this page" (or pressAlt+M)
3. Get clean Markdown instantly

## Why Markdown (and why it matters for LLMs)

Modern LLMs perform significantly better when content is provided in clean, structured Markdown instead of raw HTML or cluttered webpage data.

HTML pages include navigation bars, scripts, ads, and deeply nested DOM structures that add noise and consume context window without adding meaning. This extension solves that by converting pages into a simplified, structured format that is easier to process and reason about.

Benefits for LLM workflows:

* Less noise, more signal:Removes ads, UI elements, and boilerplate content that distract from the main text.
* Better structure understanding:Headings, lists, and sections are preserved in a format LLMs naturally interpret well.
* Token efficiency:Markdown is significantly more compact than HTML, helping fit more useful content into limited context windows.
* Improved reasoning quality:Clean hierarchical formatting makes it easier for models to summarize, extract, and answer questions accurately.
* Reliable parsing:Unlike raw HTML, Markdown avoids deeply nested or inconsistent DOM structures that can confuse extraction pipelines.

In short:this extension turns “web pages” into “LLM-ready documents.”

## Features

* One-Click Conversion:Use the context menu (right-click) or the keyboard shortcut (Alt+M) to instantly convert the current page.
* Smart Extraction:Powered by Mozilla's Readability library to isolate the main content and ignore ads, navbars, and unnecessary elements.
* Dedicated Preview Tab:Opens a clean interface where you can view and refine the extracted Markdown.
* Customizable Output:Toggle various elements to tailor the Markdown to your needs:Remove/Keep ImagesRemove/Keep LinksShow/Hide Metadata (Title, Author, Date)Show/Hide Source URLGenerate a Document Structure / Page Map
* Remove/Keep Images
* Remove/Keep Links
* Show/Hide Metadata (Title, Author, Date)
* Show/Hide Source URL
* Generate a Document Structure / Page Map
* Export Options:Copy to clipboardDownload as a.mdfileCopy as a prompt (useful for AI workflows)
* Copy to clipboard
* Download as a.mdfile
* Copy as a prompt (useful for AI workflows)

## Try it out!

Or you can install the extension fromreleasesor build it from source (see instructions below). Once installed, simply right-click on any webpage and select ".MD this page" to see the magic happen.

## Getting Started

This extension is built withPlasmoand React.

### Prerequisites

* Node.js
* pnpm (or npm, yarn)

### Installation & Development

1. Clone the repository and navigate to the project directory:cdmd-this-page
2. Install dependencies:pnpm install
3. Run the development server:pnpm devThis will run the Plasmo dev server and generate abuild/chrome-mv3-devdirectory.
4. Load the extension in Chrome:* Go tochrome://extensions/
* EnableDeveloper mode
* ClickLoad unpacked
* Select thebuild/chrome-mv3-devdirectory from this project.

### Building for Production

To create a production build of the extension:

pnpm build

This will output the production-ready extension intobuild/chrome-mv3-prod.

## Built With

* Plasmo- Browser Extension Framework
* React- UI Library
* Tailwind CSS- Styling
* @mozilla/readability- Content extraction
* Turndown- HTML to Markdown conversion

## License

MIT License

## Credits

Adem Kouki -GitHub

## About

Convert any web page to clean, readable Markdown with just one click.

### Topics

 chrome-extension

 markdown

 firefox-extension

### Resources

 Readme

 

### License

 MIT license
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

864

 stars
 

### Watchers

6

 watching
 

### Forks

75

 forks
 

 Report repository

 

## Releases1

Version 1.0.0

 Latest

 

Apr 17, 2026

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript92.8%
* JavaScript3.6%
* CSS3.6%