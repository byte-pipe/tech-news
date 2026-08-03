---
title: 'ssh.place: r/place over SSH'
url: https://ssh.place
site_name: hnrss
content_file: hnrss-sshplace-rplace-over-ssh
fetched_at: '2026-08-03T12:06:57.049885'
original_url: https://ssh.place
date: '2026-08-03'
description: A shared canvas you draw on over SSH. No account, no install. Just run ssh ssh.place
tags:
- hackernews
- hnrss
---

Draw on it:

ssh ssh.place

Any SSH key works. There is nothing to sign up for.

37 online · 9665 of 12000 cells drawn

## How it works

* Move the cursor with thearrow keys,wasdorhjkl
* The canvas is wider than your terminal, soscrollto pan around.shift+←/→jumps a whole screen.
* Pick a color with0to9.tabcycles through all 16.
* spaceputs down a solid block of that color
* Now wait 15 seconds, same as everyone else

This canvas is color only. The server turns down anything with a character in it, so you cannot write text here. Draw something instead.

Your cooldown is tied to your SSH key, so reconnecting will not reset it. This page only reads the canvas. It changes over SSH and nowhere else.