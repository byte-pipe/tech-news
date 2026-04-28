---
title: 'GitHub - iamgio/quarkdown: 🪐 Markdown with superpowers: from ideas to papers, presentations, websites, books, and knowledge bases. · GitHub'
url: https://github.com/iamgio/quarkdown
site_name: github
content_file: github-github-iamgioquarkdown-markdown-with-superpowers-f
fetched_at: '2026-04-28T12:26:12.538278'
original_url: https://github.com/iamgio/quarkdown
author: iamgio
description: '🪐 Markdown with superpowers: from ideas to papers, presentations, websites, books, and knowledge bases. - iamgio/quarkdown'
---

iamgio

 

/

quarkdown

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork303
* Star11.4k

 
 
 
 
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

3,318 Commits
3,318 Commits
.github
.github
 
 
.run
.run
 
 
demo
demo
 
 
docs
docs
 
 
gradle/
wrapper
gradle/
wrapper
 
 
mock
mock
 
 
quarkdown-cli
quarkdown-cli
 
 
quarkdown-core
quarkdown-core
 
 
quarkdown-html
quarkdown-html
 
 
quarkdown-install-layout-navigator
quarkdown-install-layout-navigator
 
 
quarkdown-interaction
quarkdown-interaction
 
 
quarkdown-libs
quarkdown-libs
 
 
quarkdown-lsp
quarkdown-lsp
 
 
quarkdown-plaintext
quarkdown-plaintext
 
 
quarkdown-quarkdoc-reader
quarkdown-quarkdoc-reader
 
 
quarkdown-quarkdoc
quarkdown-quarkdoc
 
 
quarkdown-server
quarkdown-server
 
 
quarkdown-stdlib
quarkdown-stdlib
 
 
quarkdown-test
quarkdown-test
 
 
scripts
scripts
 
 
.dockerignore
.dockerignore
 
 
.gitignore
.gitignore
 
 
CHANGELOG.md
CHANGELOG.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
build.gradle.kts
build.gradle.kts
 
 
gradle.properties
gradle.properties
 
 
gradlew
gradlew
 
 
gradlew.bat
gradlew.bat
 
 
settings.gradle.kts
settings.gradle.kts
 
 
version.txt
version.txt
 
 
View all files

## Repository files navigation

ReleasesLatest|Stable

# Table of contents

1. About
2. Demo
3. Targets
4. Comparison
5. Getting startedInstallationQuickstartCreating a projectCompiling
6. Installation
7. Quickstart
8. Creating a project
9. Compiling
10. Mock document
11. Contributing
12. Sponsors
13. Concept
14. License

 

# About

Quarkdown is a modern Markdown-based typesetting system designed forversatility. It allows a single project to compile seamlessly into a print-ready book, academic paper, knowledge base, or interactive presentation.
All through an incredibly powerful Turing-complete extension of Markdown, ensuring your ideas flow automatically into paper.

 

Original credits:Attention Is All You Need

Born as an extension of CommonMark and GFM, the Quarkdown Flavor bringsfunctionsto Markdown, along with many other syntax extensions.

This is a function call:

.somefunction {arg1} {arg2}
 Body argument

Possibilities are unlimitedthanks to an ever-expandingstandard library,
which offers layout builders, I/O, math, conditional statements and loops.

Not enough?You can still define your own functions and variables, all within Markdown.
You can even create awesome libraries for everyone to use.

.function {greet}
 to from:
 **Hello, .to** from .from!

.greet {world} from:{iamgio}

Result:Hello, worldfrom iamgio!

This out-of-the-box scripting support opens doors to complex and dynamic content that would be otherwise impossible
to achieve with vanilla Markdown.

Combined with live preview, ⚡ fast compilation speed and a powerfulVS Code extension, Quarkdown simply gets the work done,
whether it's an academic paper, book, knowledge base or interactive presentation.

 

 

## Looking for something?

Check out thewikito get started and learn more about the language and its features!

 

## As simple as you expect...

Inspired by:X-ray flashes from a nearby supermassive black hole accelerate mysteriously

 

## ...as complex as you need.

# Targets

* HTMLPlainContinuous flow like Notion/Obsidian, perfect for static websites and knowledge management - check out the author'spersonal website.Pagedviapaged.jsPerfect for papers, articles and books - check out thedemo document.Slidesviareveal.jsPerfect for interactive presentations.DocsPerfect for wikis, technical documentation and large knowledge bases - check outQuarkdown's wiki.
* PlainContinuous flow like Notion/Obsidian, perfect for static websites and knowledge management - check out the author'spersonal website.
* Pagedviapaged.jsPerfect for papers, articles and books - check out thedemo document.
* Slidesviareveal.jsPerfect for interactive presentations.
* DocsPerfect for wikis, technical documentation and large knowledge bases - check outQuarkdown's wiki.
* PDFAll document types and features supported by HTML are also supported when exporting to PDF.
* All document types and features supported by HTML are also supported when exporting to PDF.
* Plain text

The desired document type can be set by calling the.doctypefunctionwithin the source itself:

* .doctype {plain}(default)
* .doctype {paged}
* .doctype {slides}
* .doctype {docs}

# Comparison

Quarkdown

LaTeX

Typst

AsciiDoc

MDX

Concise and readable

✅

❌

✅

✅

✅

Full document control
1

✅

✅

✅

❌

❌

Scripting

✅

Partial

✅

❌

✅

Book/article export

✅

✅

✅

✅

Third-party

Presentation export

✅

✅

✅

✅

Third-party

Static site export

✅

❌

Experimental

✅

✅

Docs/wiki export

✅

❌

❌

✅

✅

Learning curve

🟢

🔴

🟠

🟢

🟢

Targets

HTML, PDF, TXT

PDF, PostScript

HTML, PDF

HTML, PDF, ePub

HTML

LaTeX

Quarkdown

\tableofcontents

\section
{
Section
}

\subsection
{
Subsection
}

\begin
{
enumerate
}
 
\item
 
\textbf
{
First
} item
 
\item
 
\textbf
{
Second
} item

\end
{itemize}

\begin
{
center
}
 This text is 
\textit
{
centered
}.

\end
{
center
}

\begin
{
figure
}[!h]
 
\centering

 
\begin
{
subfigure
}[b]
 
\includegraphics
[width=0.3
\linewidth
]{img1.png}
 
\end
{
subfigure
}
 
\begin
{
subfigure
}[b]
 
\includegraphics
[width=0.3
\linewidth
]{img2.png}
 
\end
{
subfigure
}
 
\begin
{
subfigure
}[b]
 
\includegraphics
[width=0.3
\linewidth
]{img3.png}
 
\end
{
subfigure
}

\end
{
figure
}

.tableofcontents

# 
Section

## 
Subsection

1
.
 
**
First
**
 item

2
.
 
**
Second
**
 item

.center
 This text is 
_
centered
_
.

.row alignment:{spacebetween}
 
![
Image 1
]
(
img1.png
)

 
![Image 2](img2.png)

 
 
![Image 3](img3.png)

 

# Getting started

## Installation

### Install script (Linux/macOS)

curl -fsSL https://raw.githubusercontent.com/quarkdown-labs/get-quarkdown/refs/heads/main/install.sh 
|
 sudo env 
"
PATH=
$PATH
"
 bash

Root privileges let the script install Quarkdown into/opt/quarkdownand its wrapper script into/usr/local/bin/quarkdown.If missing, Java 17, Node.js and npm will be installed automatically using the system's package manager.

For more installation options, check outget-quarkdown.

### Homebrew (Linux/macOS)

brew install quarkdown-labs/quarkdown/quarkdown

### Install script (Windows)

irm https:
//
raw.githubusercontent.com
/
quarkdown
-
labs
/
get-quarkdown
/
refs
/
heads
/
main
/
install.ps1 
|
 iex

### Scoop (Windows)

scoop bucket add java
scoop bucket add quarkdown https://github.com/quarkdown-labs/scoop-quarkdown
scoop install quarkdown

### GitHub Actions

Seesetup-quarkdownto easily integrate Quarkdown into your GitHub Actions workflows.

### Manual installation

Instructions for manual installation

Downloadquarkdown.zipfrom thelatest stable releaseand unzip it,
or build it withgradlew installDist.

Optionally, adding<install_dir>/binto yourPATHallows you easier access Quarkdown.

Requirements:

* Java 17 or higher
* (Only for PDF export) Node.js, npm, Puppeteer. SeePDF exportfor details.

 

## Quickstart 🆕

New user? You'll findeverything you needin theQuickstart guideto bring life to your first document!

 

## Creating a project

quarkdown create [directory]will launch the prompt-based project wizard, making it quicker than ever
to set up a new Quarkdown project, with allmetadataand initial content already present.

For more information about the project creator, check out itswiki page.

Alternatively, you may manually create a.qdsource file and start from there.

 

## Compiling

Runningquarkdown c file.qdwill compile the given file and save the output to file.

If the project is composed by multiple source files, the target file must be the root one, i.e. the one that includes the other files.

* How to include other files?

If you would like to familiarize yourself with Quarkdown instead,quarkdown repllets you play with an interactive REPL mode.

#### Options

The most commonly used options are:

* -por--preview: enables automatic content reloading after compiling.
* -wor--watch: recompiles the source every time a file from the source directory is changed.

Tip

Combine-p -wto achievelive preview!

* --pdf: produces a PDF file. Learn more in the wiki'sPDF exportpage.

For the full list of options, check out theCLI optionswiki page.

 

 

## Mock document

 

Mock, written in Quarkdown, is a comprehensive collection of visual elements offered by the language,
making it ideal for exploring and understanding its key features — all while playing and experimenting hands-on with a concrete outcome in the form of pages or slides.

* The document's source files are available in themockdirectory, and can be compiled viaquarkdown c mock/main.qd -p.
* The PDF artifacts generated for all possible theme combinations are available and can be viewed in thegeneratedrepo.

## Contributing

Contributions are welcome! Please checkCONTRIBUTING.mdto know how contribute via issues or pull requests.

## Sponsors

A special thanks to all the sponsors whosupported this project!

 
 

## Concept

The logo resembles the originalMarkdown icon, with focus on Quarkdown's completeness,
richness of features and customization options, emphasized by the revolving arrow all around the sphere.

What could be mistaken for a planet is actually aquarkor, more specifically, adown quark,
an elementary particle that is a major constituent of matter: they give life to every complex structure we know of,
while also being one of the lightest objects in existence.

This is, indeed, the conceptQuarkdownis built upon.

## License

By default, Quarkdown and its modules are licensed underGNU GPLv3, except for modules that include their ownLICENSEfile:
the CLI (quarkdown-cli) and Language Server (quarkdown-lsp) modules and binaries are licensed under GNU AGPLv3.

## Footnotes

## Footnotes

1. The ability to customize the properties of the document and of its output artifact through the language itself.↩

## About

🪐 Markdown with superpowers: from ideas to papers, presentations, websites, books, and knowledge bases.

quarkdown.com

### Topics

 markdown

 static-site-generator

 pdf

 documentation

 compiler

 wiki

 markup

 paper

 slides

 typesetting

 scripting-language

 presentations

 markup-language

 knowledge-management

 typesetting-system

### Resources

 Readme

 

### License

 GPL-3.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

11.4k

 stars
 

### Watchers

33

 watching
 

### Forks

303

 forks
 

 Report repository

 

## Releases33

v2.0.0

 Latest

 

Apr 23, 2026

 

+ 32 releases

## Sponsor this project

 

 

 Sponsor

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 

Learn more about GitHub Sponsors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* Kotlin74.8%
* TypeScript12.2%
* SCSS6.1%
* HTML5.8%
* Java0.5%
* TeX0.3%
* Other0.3%