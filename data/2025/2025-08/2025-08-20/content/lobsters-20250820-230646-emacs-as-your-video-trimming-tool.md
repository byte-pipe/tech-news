---
title: Emacs as your video-trimming tool
url: https://xenodium.com/emacs-as-your-video-trimming-tool
site_name: lobsters
fetched_at: '2025-08-20T23:06:46.825216'
original_url: https://xenodium.com/emacs-as-your-video-trimming-tool
date: '2025-08-20'
tags: emacs, lisp
---

xenodium.com

 ██ ██ ███████ ███ ██ ██████ ██████ ██ ██ ██ ███ ███
 ██ ██ ██ ████ ██ ██ ██ ██ ██ ██ ██ ██ ████ ████
 ███ █████ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ████ ██
 ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██
 ██ ██ ███████ ██ ████ ██████ ██████ ██ ██████ ██ ██

August 19, 2025

# Emacs as your video-trimming tool

Marcin ‘mbork’ Borkowski has a nice post showing us how hetrims video clips from our beloved editor. Trimming clips is something I do from time to time, specially when posting a screencast of sorts. Since I don't need much, I typically resort to QuickTime Player's trimming functionality that ships with macOS. While it does the job, ever since Iadded a "graphical" seeker to Ready Player Mode, I had been meaning to build a simple video trimming tool of sorts. Marcin's post was just about the right nudge I needed to also give this a go, yieldingvideo-trimmer-mode.

The solution relies onffmpegto do the heavy lifting and is roughly 300 lines of code. I was going to share the entire snippet in this post, though may as well point you to itslocation in my Emacs config repo. I'm likely to tweak it, so you may as well take a look at its latest incarnation.

## Make it all sustainable

Findvideo-trimmer-modeuseful? Want me to publish toMELPA? Enjoying thisblogormy projects? I am an 👉 indie dev 👈. Help make my work sustainable by ✨sponsoring✨

Need a blog?I can help with that. Maybe buy mymacOS/iOS appstoo ;)

powered byLMNO.lol

privacy policy·terms of service
