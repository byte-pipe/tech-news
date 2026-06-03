---
title: Pluto 1.0 release! - Package Announcements - Julia Programming Language
url: https://discourse.julialang.org/t/pluto-1-0-release/137296
site_name: hackernews_api
content_file: hackernews_api-pluto-10-release-package-announcements-julia-progr
fetched_at: '2026-06-04T06:55:11.810418'
original_url: https://discourse.julialang.org/t/pluto-1-0-release/137296
author: fons-p
date: '2026-06-03'
published_date: '2026-05-27T15:18:03+00:00'
description: After six years, it’s time to release Pluto version 1.0! With this release, I want to celebrate all the progress over the past years, and to symbolise that Pluto is ready. I am proud of what we have achieved, and I hope &hellip;
tags:
- hackernews
- trending
---

# Pluto 1.0 release!

Package Announcements

pluto
, 
 
notebooks

fonsp

 May 27, 2026, 3:18pm
 

1

After six years, it’s time to release Pluto version 1.0! With this release, I want to celebrate all the progress over the past years, and to symbolise that Pluto isready. I am proud of what we have achieved, and I hope you enjoy it!

This is a long post, so I will give a table of contents.This post will take 10 minutes to read. It will take longer if you click on links with additional information.

* Wait… what is Pluto?
* Okay! And what’s new in Pluto?(1/10) Reproducibility & reliability(2/10) Sharing your work(3/10) Reactivity(4/10) Interactivity(5/10) Accessibility and localization(6/10) Education(7/10) AI tools(8/10) Documentation(9/10) Editor tools(10/10) Ecosystem
* (1/10) Reproducibility & reliability
* (2/10) Sharing your work
* (3/10) Reactivity
* (4/10) Interactivity
* (5/10) Accessibility and localization
* (6/10) Education
* (7/10) AI tools
* (8/10) Documentation
* (9/10) Editor tools
* (10/10) Ecosystem
* Thank you!

 

# Wait… what is Pluto?

Pluto is aninteractive environment for notebook programmingin Julia. Our goal is to make scientific computing moreaccessibleandfun! You can use Pluto to experiment with code in a safe and friendly environment, and you can use it to write interactive articles, lecture notes and presentations (literate programming).

What’s special about Pluto is:

* Interactive: cells arereactive(like a spreadsheet) and it’s very easy to addbuttons and slidersto control your code.
* Reproducible: From package management to execution order, Pluto goes to great lengths to make sure that someone else will be able to run your notebook when you’re done!
* Accessible: We designed Pluto to teach our own course:Computational Thinking at MIT. The result is a programming environment that prioritizes beginners over advanced users!

And Pluto is popular! It’s used by people all around the world (like these online courses) and Pluto has been the#1starred Julia package on GitHub since 2021.

### Try Pluto

Pluto is free and open source, written in Julia and JavaScript. Pluto is supereasy to installusing Julia’s package manager. Start Julia, and run:

import Pluto
Pluto.run()

Want to know more?Check out our website →

hand drawing of 3 characters playing with the "Pluto" letters2000×640 79.3 KB

# Okay! And what’s new in Pluto?

Well… the1.0.0releaseitself is a bit unspectacular (just one PR:“removed deprecations”), but in this post I want to give an overview ofhighlights from the past years. If you tried Pluto before, then now might be a good time to check it out again!

## (1/10) Reproducibility & reliability

Pluto 1.0 is very reliable! Courses of 100+ students often report that everyone was able to install Pluto and run course notebooks without problems.

This is the result of countless design choices, bug fixes, testing, built-in strategies to automatically recover from broken states, and care. We have ~2500 automatic test cases, including tests that use web browsers to test Pluto by clicking and typing in the UI.

### Automatic Pkg management

Every notebook has an isolated Pkg environment, and packages are automatically added and removed when needed. When you open a notebook from someone else, the same versions of packages will be used.

We developed GracefulPkg.jl to improve reproducibility when mixing Julia versions. And there is also a newProject.toml editor, which gives precise control over which versions are used. You can use the new Julia[sources]feature to use packages from github in a reproducible way.

screenshot of a code snippet that imports the Plots package, with a dynamic inline popup that tells the user that "Plots version 1.41.6 will be installed in the notebook when you run this cell. Installation can take 3 minutes, afterwards it loads in 4 seconds."1000×362 24.5 KB

## (2/10) Sharing your work

Pluto notebooks can be exported directly to Julia, PDF and HTML. The HTML format is special: it is a self-contained file that renders your notebook exactly as it looked when you exported. It also contains the Julia source code and package environment, which means that if you can read it, you can run it. Here is anexample. Since 2025, the Pluto web assets are also self-contained, which means you can open HTML export files without internet.Read more about exporting →

### Make a website

You can usestatic-export-templateto automatically generate a website from a repository of notebooks, and with PlutoSliderServer.jl you can serve Pluto-based websites that are instantly interactive.

We also launchedpluto.land, a free web service to easily share Pluto HTML exports. It’s like a pastebin, but only for Pluto notebooks.

## (3/10) Reactivity

Pluto notebooks are reactive. Changing one cellinstantly shows effectson all other cells, giving you a fast and fun way to experiment with your model. There are new ways to control reactivity, which helps when you havelong-running cells.

### Disable cells

Pluto allows you todisable a cell, which means that it will not get executed with reactivity. When one of the dependencies of a disabled cell changes, the disabled cell willnotget executed as usual.

The cell disabling feature isreactive– any cells that depend on a disabled cell willalso be disabled. This is a really powerful feature, because you can easily disable a large number of cells at once, by disabling a core cell that is used in all of them.Learn more →

### Confirm before long runtimes

A new feature in Pluto willask for confirmationwhen you trigger a reactive chain of cells that might take a long time to run (based on previous runtimes). This gives the option to cancel the run, make more changes, and run everything in a single reactive batch.

screenshot of a popup that says: "This cell and its dependency might take 3 minutes to run. Confirm? No (Escape key), Yes (Enter key). Tip: You can use the disable cell feature to control which cells run reactively."992×560 33.7 KB

## (4/10) Interactivity

Pluto issuper interactivesince day 1! What’s new: more interactive elements in PlutoUI.jl and new APIs for designing your own widgets.

### New in PlutoUI.jl

ThePlutoUI.jlpackage contains lots of new input widgets. You have sliders, switches, buttons, dropdowns, multiselects, textfields, you name it! And it also has a click-for-more widget, a reading-time-calculator, an extra wide Pluto cell, a cell in the side margin, advanced tools for 2D layout, and tools for composing multiple widgets into one!Check out the complete showcase →

There is alsoPlutoTeachingTools.jl, co-developed with other teachers who use Pluto. It contains everything you need to write interactive lectures, and live homeworks that react to student input.

screenshot of various plutoUI widgets aligned in a grid. there are several sliders, a switch toggle, checkbox select items for "linear" and "quadratic", a dropdown with the sine function selected, a color picker with the color pink selected, a button that says "Recalculate", and a large text input box.1450×262 9.67 KB

### Advanced: Widgets API

We have gradually rolled out lots of API that lets you write your own widgets, using a high level of integration into the Pluto engine. We expose aJavaScript runtime, Pluto’s high-performanceJulia-JS connection, ourdisplay system, andmore. With this API, you can easily add Pluto-specific widgets to an existing package (without adding a Pluto dependency), or write a new package. PlutoUI.jl is also built using this API.Read an overview →

## (5/10) Accessibility and localization

Pluto is more accessible than ever! We have worked hard to improvekeyboard-only, mouse-only and touch-only use,visual accessibilityandscreen readersupport.Learn more →

Also new: Pluto can be used in16 different languages: Chinese (Chinese)(by@Fromduststar), Dansk (Danish)(by@gwr-de), Deutsch (German)(by@kellertuer), Ελληνικά (Greek)(by@pankgeorg), English, Español Latinoamericano (Latin American Spanish)(by@gruumsh1), Français (French)(by@Pangorawand@gdalle), Čeština (Czech)(by@kunzaatko), Italiano (Italian)(by@disberd), Japanese (Japanese)(by@Itou-Kouki), Nederlands (Dutch)(by@fonsp), Norsk Bokmål (Norwegian)(by@kellertuer), فارسی (Persian)(by@shosseinib), Polski (Polish)(by@s-zymon), Português (Portugal) (Portuguese Portuguese)(by@rgouveiamendes)and Suomi (Finnish)(by@eteppo).

Are you interested to contribute to Pluto’s localization?Check out our documentation →

## (6/10) Education

Inspiration for Pluto comes from my experience teaching Julia. (I currently work on Pluto alongside the courseBayesian MLat TU Eindhoven, check it out!)

### Error messages

Getting an error message can be scary and demotivating for new programmers, so we did our best to improve the error experience in Pluto. Using web design and Julia heuristics, we try to present the error message and stack trace the way we would explain it to someone else.

Features include:

* Mini preview for your own code
* Explaining what the stack trace is
* Fade-out of internal Julia functions in the stack trace
* Click-to-show the stack trace if the error comes from the cell itself
* Click-to-show stack frames that happened before your own code
* Click-to-show long type annotations

screenshot of an error message in pluto, showcasing the features described previously.1330×1126 71.9 KB

### Course Website Template

We developedcomputational-thinking-template, a repository template for buildingawesome looking course websites! It features a sidebar, a colorful homepage, built-in search, GitHub Actions, “Edit this Page” links, run with Binder, and much more! This template is based on the successful online courseComputational Thinking at MIT. The technology behind this course is open source (developed by the Pluto team), and now available as a standalone template.Read more about the template, or you canexplore all publishing options →

cropped screenshot of the computational thinking course template default website. there is a sidebar, a colorful header and a search bar. The course still has placeholder name, authors, etc.2410×933 372 KB

### PlutoTurtles

PlutoTurtles.jlis a fun way to get started with Julia programming. You can move a little turtle with simple commands to draw lines in any color you want – you make a drawing with code. With Pluto, you can make the drawingsinteractive, by controlling variables with sliders, and Pluto canhighlight lines of codewhile the turtle takes steps.

We have aprogramming tutorial based on PlutoTurtles.jl, and ashowcase of some simple turtle art.

## (7/10) AI tools

Pluto is not a vibe coding tool, and we are not planning to make it one! We think that AI code generation is useful, but right now, Pluto should still be a tool that helps people get better at writing Julia code.

At the moment, we have one AI-powered feature, which canautomatically fix syntax errors(like a missingendor"), but no other types of errors. We hope that this will help you with what you are trying to do, without taking over your creativity.

There are multiple ways to disable AI features if it’s not what you want. Check out ourdocumentation about AI editor features →

## (8/10) Documentation

Also new! We have a collection of40 featured notebooks, which showcase the exciting things you can do with Julia and Pluto. You can read and interact with the featured notebooks directly from the Pluto main menu, or from our website.

And we have a shiny new website –plutojl.org! The website shows what Pluto can do, and it has lots of documentation to explain how to best use Pluto. Oh, and the website is built withPlutoPages.jl, a new SSG package.

cropped screenshot of the plutojl website showing the documentation navigation sidebar and a search bar2406×1216 340 KB

## (9/10) Editor tools

The Pluto editor has lots of improvements.Sergio Vargaswrote a new parser for Julia that runs in CodeMirror 6, the new code editing system that we use. The new parser is very detailed and performant, which allowed us to (re)write lots of functionality based on syntax-pattern-matching.

### Autocomplete

Pluto has a carefully crafted autocomplete system, which gives code suggestions while you type. It combines static code analysis (from the JS parser) with scope analysis and Julia REPL autocomplete results – an experience optimized for Julia notebooks. I believe it’s good enough to enable automatically while you type, but you can also disable this in the settings.

screenshot of the autocomplete system – the user typed the letter c inside a function, and it autocompletes the argument name correctly along with other functions that start with c.1490×496 42.7 KB

### More features

We implemented a jump-to-definition plugin, more keyboard shortcuts, a mixed language parser (when using Python/SQL/HTML inside Julia), tabs/spaces setting, copy-link-to-header, and much more.

Pluto also got support for Logging (like@info), retro terminal streams (likeprintln) and ANSI color rendering. And we improved our rich object viewer, with high-performance displays for HTML, LaTeX, SVG, PNG, and our interactive tree viewer for vector, tuple and dictionary data structures.

## (10/10) Ecosystem

Along the way, we have contributed several packages to the Julia ecosystem: Malt.jl, HypertextLiteral.jl, GracefulPkg.jl, MIMEs.jl, ExpressionExplorer.jl, PlutoDependencyExplorer.jl and contributions to base Julia and the Julia web ecosystem. These packages are also used in projects unrelated to Pluto!

We now have a formalgovernance structure,architecture overview, and I transfered the repository to a collectiveJuliaPlutoorganisation.

# Thank you!

Pluto has been a collaborative effort. You can read some highlights abouthow Pluto works and who designed it. Open source software development is challenging, but I’m very grateful for people I met along the way. Thank you for supporting me in difficult times, for teaching me new ways of thinking, and for your contributions to the project. It means a lot to me!

If you have used Pluto and you enjoy it, I’m happy! Please reach out and share your experience, I would love to hear from you. You can contact me here on discourse, or emailfons-at-plutojl-dot-org.

orlando_mendez

 May 27, 2026, 8:33pm
 

2

Congrats,@fonsp, on this release, and may we have moreplutoversions in the future!

bvdmitri

 May 28, 2026, 9:38am
 

3

I remember usingearly versions of Plutoback in 2021! What a nice journey! Great project that inspired many people to try out Julia, congratulations with the firststablerelease

csvance

 May 28, 2026, 1:10pm
 

4

Congratulations on 1.0! Pluto is a lot of things to a lot of people, but for me one of its biggest strengths is how well it works for communicating results interactively.

Mikhail_Kagalenko

 June 3, 2026, 3:00pm
 

5

Unless I’m missing something, there does not seem to be a way to disable AI features from a notebook itself, instead a suggested solution is to supply a named parameter to Plluto.run(). Can this parameter be set from within the notebook?

johnh

 June 3, 2026, 3:31pm
 

6

Woohoo! Pluto is 1 !

### Related topics

Topic

Replies

Views

Activity

Hosting interactive pluto notebook on web/Github

New to Julia

pluto

29

10796

 March 23, 2022
 

(Not-So-)Crazy idea: Make the julia docs a Pluto notebook

Community

documentation

 , 
 
pluto

41

5246

 September 30, 2021
 

Announcing Neptune.jl (now updated to multi-line cells!)

Package Announcements

notebooks

98

14669

 January 25, 2022
 

Pluto's running script with Julia shipping bundle

Tooling

3

721

 August 15, 2020
 

Pluto noobie questions

General Usage

pluto

9

421

 September 8, 2022