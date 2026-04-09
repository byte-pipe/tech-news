---
title: 5 Terminal Commands That Saved Me Hours of Clicking - DEV Community
url: https://dev.to/maame-codes/5-terminal-commands-that-saved-me-hours-of-clicking-4mfn
site_name: devto
fetched_at: '2025-12-21T19:06:42.216883'
original_url: https://dev.to/maame-codes/5-terminal-commands-that-saved-me-hours-of-clicking-4mfn
author: Maame Afua A. P. Fordjour
date: '2025-12-19'
description: When I first started coding, I was terrified of the terminal. That blank black screen with the... Tagged with terminal, webdev, programming.
tags: '#terminal, #webdev, #programming'
---

When I first started coding, I was terrified of the terminal.

That blank black screen with the blinking green cursor? It looked like something out of The Matrix, something only "senior engineers" with grey beards knew how to use. Me? I loved my mouse. I loved my GUI. I was a professional at dragging and dropping files and right-clicking to create new folders.

But as I started building projects and diving into more complex tools, the GUI started feeling... slow.

I found myself clicking through ten layers of nested folders just to find one file. My wrist was actually starting to hurt from all the double-clicking. I realized that if I wanted to be fast, efficient, and actually understand what the computer was doing, I had to ditch the mouse and embrace the command line.

It was awkward at first. My muscle memory fought me every step of the way. But once I got past the initial learning curve, I realized I could do things in seconds that used to take minutes.

Here are the 5 basic commands that finally convinced me to switch sides. 👇

## 1. The Teleporter: cd (plus Tab Completion)

The Old Way (GUI): Open file explorer. Double-click "Documents". Double-click "Coding". Double-click "Python". Double-click "Projects". Realize I clicked the wrong one. Go back. Double-click "Web-App".

The Terminal Way:

cd ~/Doc[TAB]/Cod[TAB]/Py[TAB]/Proj[TAB]/Web[TAB]

Enter fullscreen mode

Exit fullscreen mode

Why I love it:cd stands for "Change Directory." It’s simple, but when you combine it with the Tab key, it’s a superpower. You just type the first few letters of a folder, hit Tab, and the terminal autocompletes the name for you.

It feels less like walking through a maze of folders and more like teleporting directly to where you need to be.⚡️

## 2. The Instant Architect: mkdir -p

The Old Way (GUI): I need to set up a new project structure. Right-click -> New Folder -> type "my-app". Open folder. Right-click -> New Folder -> type "src". Open folder. Right-click -> New Folder -> type "components". Go back up. Right-click -> New Folder -> type "assets".

So. Much. Clicking. 😫

The Terminal Way:

mkdir -p my-app/{src/components,assets,tests}

Enter fullscreen mode

Exit fullscreen mode

Why I love it:mkdir means "Make Directory." But the magic here is the -p flag (parent) and those curly braces {}. This single line creates my main folder AND all the subfolders inside it instantly. It’s like snapping your fingers and having a building appear.

## 3. The "Safety Net": cp -r

The Old Way (GUI): I'm about to try a completely reckless refactor of my code that might break everything. I need a backup. I go to the parent folder, right-click my project folder, click "Copy," right-click blank space, click "Paste." Wait for the computer to calculate file sizes... wait for the copy bar to finish... rename the new folder to "project-backup".

The Terminal Way:

cp -r my-cool-project my-cool-project-BACKUP

Enter fullscreen mode

Exit fullscreen mode

Why I love it:cp is Copy. The -r stands for "recursive," which just means "copy the folder and every single thing inside it." It’s blazing fast. Before I try anything stupid with my code, I run this command in one second, and I have instant peace of mind. 😌

## 4. The Mass Cleaner: The Wildcard *

The Old Way (GUI): My Downloads folder is a disaster zone of PDFs, images, and chaotic zip files. I want to move just the images to my Pictures folder. I have to scroll through, hold down Ctrl (or Cmd), and gingerly click every single .jpg and .png file, hoping I don't accidentally let go of the key and have to start over. Then drag them all over.

The Terminal Way:

mv ~/Downloads/*.jpg ~/Pictures/
mv ~/Downloads/*.png ~/Pictures/

Enter fullscreen mode

Exit fullscreen mode

Why I love it:Okay, the asterisk * isn't technically a command, it's a wildcard. But combined with mv (Move), it changed my life. The * basically means "everything." So *.jpg means "everything that ends in .jpg".

It makes organizing messy folders unbelievably satisfying. 🧹

## 5. The Detective: grep -r

The Old Way (GUI): My code is throwing an error related to a variable named api_key_v2. I have no idea where I defined that variable. I open VS Code, open 15 different tabs, and start doing Ctrl+F in every single file trying to find it.

The Terminal Way:

grep -r "api_key_v2" .

Enter fullscreen mode

Exit fullscreen mode

Why I love it:grep is basically a search-and-rescue dog for text. The -r flag tells it to look "recursively" through the current folder (.) and every folder underneath it.

It instantly spits out the exact file and line number where that text exists. It makes debugging giant codebases feel way less overwhelming.

## Just Try It for a Week

Look, I still use VS Code. I still use a browser. GUIs aren't evil.

But getting comfortable with these basics changed my relationship with my computer. I stopped feeling like a "user" navigating a system someone else built, and started feeling like an "engineer" controlling the system directly.

If you're scared of the black screen, try forcing yourself to use it for just these five tasks for one week. Your mouse hand will thank you. 🙏

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (14 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
