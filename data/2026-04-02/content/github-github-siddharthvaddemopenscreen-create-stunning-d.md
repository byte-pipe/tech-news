---
title: 'GitHub - siddharthvaddem/openscreen: Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio. · GitHub'
url: https://github.com/siddharthvaddem/openscreen
site_name: github
content_file: github-github-siddharthvaddemopenscreen-create-stunning-d
fetched_at: '2026-04-02T19:24:39.383956'
original_url: https://github.com/siddharthvaddem/openscreen
author: siddharthvaddem
description: 'Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio. - GitHub - siddharthvaddem/openscreen: Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio.'
---

siddharthvaddem

 

/

openscreen

Public

* NotificationsYou must be signed in to change notification settings
* Fork1.1k
* Star15.3k

 
 
 
 
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

385 Commits
385 Commits
.github
.github
 
 
.husky
.husky
 
 
electron
electron
 
 
icons/
icons
icons/
icons
 
 
public
public
 
 
scripts
scripts
 
 
src
src
 
 
tests
tests
 
 
.editorconfig
.editorconfig
 
 
.gitignore
.gitignore
 
 
.nvmrc
.nvmrc
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
biome.json
biome.json
 
 
components.json
components.json
 
 
electron-builder.json5
electron-builder.json5
 
 
index.html
index.html
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
postcss.config.cjs
postcss.config.cjs
 
 
tailwind.config.cjs
tailwind.config.cjs
 
 
tsconfig.json
tsconfig.json
 
 
tsconfig.node.json
tsconfig.node.json
 
 
vite.config.ts
vite.config.ts
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

Warning

This is very much in beta and might be buggy here and there (but hope you have a good experience!).

# OpenScreen

OpenScreen is your free, open-source alternative to Screen Studio (sort of).

If you don't want to pay $29/month for Screen Studio but want a much simpler version that does what most people seem to need, making beautiful product demos and walkthroughs, here's a free-to-use app for you. OpenScreen does not offer all Screen Studio features, but covers the basics well!

Screen Studio is an awesome product and this is definitely not a 1:1 clone. OpenScreen is a much simpler take, just the basics for folks who want control and don't want to pay. If you need all the fancy features, your best bet is to support Screen Studio (they really do a great job, haha). But if you just want something free (no gotchas) and open, this project does the job!

OpenScreen is 100% free for personal and commercial use. Use it, modify it, distribute it. (Just be cool 😁 and give a shoutout if you feel like it !)

## Core Features

* Record your whole screen or specific windows.
* Add Automatic zooms or manual zooms (customizable depth levels).
* Record microphone audio and system audio capture.
* Customize the duration and position of zooms however you please.
* Crop video recordings to hide parts.
* Choose between wallpapers, solid colors, gradients or a custom background.
* Motion blur for smoother pan and zoom effects.
* Add annotations (text, arrows, images).
* Trim sections of the clip.
* Customize speed at different segments.
* Export in different aspect ratios and resolutions.

## Installation

Download the latest installer for your platform from theGitHub Releasespage.

### macOS

If you encounter issues with macOS Gatekeeper blocking the app (since it does not come with a developer certificate), you can bypass this by running the following command in your terminal after installation:

xattr -rd com.apple.quarantine /Applications/Openscreen.app

Note: Give your terminal Full Disk Access inSystem Settings > Privacy & Securityto grant you access and then run the above command.

After running this command, proceed toSystem Preferences > Security & Privacyto grant the necessary permissions for "screen recording" and "accessibility". Once permissions are granted, you can launch the app.

### Linux

Download the.AppImagefile from the releases page. Make it executable and run:

chmod +x Openscreen-Linux-
*
.AppImage
./Openscreen-Linux-
*
.AppImage

You may need to grant screen recording permissions depending on your desktop environment.

Note:If the app fails to launch due to a "sandbox" error, run it with --no-sandbox:

./Openscreen-Linux-
*
.AppImage --no-sandbox

### Limitations

System audio capture relies on Electron'sdesktopCapturerand has some platform-specific quirks:

* macOS: Requires macOS 13+. On macOS 14.2+ you'll be prompted to grant audio capture permission. macOS 12 and below does not support system audio (mic still work).
* Windows: Works out of the box.
* Linux: Needs PipeWire (default on Ubuntu 22.04+, Fedora 34+). Older PulseAudio-only setups may not support system audio (mic should still works).

## Built with

* Electron
* React
* TypeScript
* Vite
* PixiJS
* dnd-timeline

I'm new to open source, idk what I'm doing lol. If something is wrong please raise an issue 🙏

## Contributing

Contributions are welcome! If you’d like to help out or see what’s currently being worked on, take a look at the open issues and theproject roadmapto understand the current direction of the project and find ways to contribute.

## License

This project is licensed under theMIT License. By using this software, you agree that the authors are not liable for any issues, damages, or claims arising from its use.

## About

Create stunning demos for free. Open-source, no subscriptions, no watermarks, and free for commercial use. An alternative to Screen Studio.

openscreen.vercel.app

### Topics

 electron

 open-source

 screen-recorder

 screen-capture

 pixijs

### Resources

 Readme

 

### License

 MIT license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

15.3k

 stars
 

### Watchers

32

 watching
 

### Forks

1.1k

 forks
 

 Report repository

 

## Releases11

v1.3.0

 Latest

 

Apr 2, 2026

 

+ 10 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript97.5%
* CSS1.6%
* Other0.9%