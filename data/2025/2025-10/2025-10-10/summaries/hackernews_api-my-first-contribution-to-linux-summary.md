---
title: My First Contribution to Linux
url: https://vkoskiv.com/first-linux-patch/
date: 2025-10-06
site: hackernews_api
model: llama3.2:1b
summarized_at: 2025-10-10T11:11:03.387377
screenshot: hackernews_api-my-first-contribution-to-linux.png
---

# My First Contribution to Linux

**Context**

The author has been studying Linux source code to gain deeper understanding of how computers work and decided to contribute a patch to build on this newfound knowledge.

## How do the keys work?

* The problem lies in the "Application" toggle key, which is supposed to select between two modes (like the old Fujitsu keyboard's Application/Player mode). This key seems to be just a hardware toggle button without any functional behavior.
* Another possible bug: when pressing this keyboard key under i3 (the 2008 version of the display manager), it doesn't do anything on its own. The events are not bound to anything by default.

## How to verify keys?

To see how special keys like this ones are handled in Linux, the author looked up `KeyPress` and `KeyRelease` event handlers under X11, which seems to be a good way to get information about what is happening with keyboard input. After using it, they bound events to specific commands.

## Study of Fujitsu-laptop driver

The author also analyzed the Fujitsu-laptop driver as part of their research on Linux kernel development process.

## Modifying the driver

In order to test changes and make contributions, the author decided to upstream the changes.

## Testing my changes

The author used `bindsym` to bind specific keys to arbitrary commands in their custom `i3-sensible-terminal` configuration file. With this setup, when they pressed the now key under i3 (which was previously supposed to be a "modes" toggle), it opened a new terminal window.

## Upstreaming

Although the author made some changes based on their research, these were not directly upstreamed. However, they did contribute patches to build upon.

## Project Timeline

As part of this project, the author worked on various aspects such as adding support for Fujitsu-laptops and modifying a kernel module related to keyboard functionality.

## Conclusion

By following these steps, the author was able to gain insight into how Linux handles special keys like those found in old laptops. Their efforts have not led to direct upstream contributions of code yet but provide valuable learning experience on how to contribute to open-source projects and build upon existing ones.
