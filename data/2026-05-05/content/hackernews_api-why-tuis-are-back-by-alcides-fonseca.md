---
title: Why TUIs are back by Alcides Fonseca
url: https://wiki.alcidesfonseca.com/blog/why-tuis-are-back/
site_name: hackernews_api
content_file: hackernews_api-why-tuis-are-back-by-alcides-fonseca
fetched_at: '2026-05-05T00:51:19.020010'
original_url: https://wiki.alcidesfonseca.com/blog/why-tuis-are-back/
author: rickcarlino
date: '2026-05-04'
description: Why TUIs are back
tags:
- hackernews
- trending
---

### Why TUIs are back

Terminal User Interfaces (TUIs) are making a comeback.DHH’sOmarchyis made of three types of user interfaces:TUIs, for immediate feedback and bonus geek points, webapps because 37signals (his company) sellsSAASweb applications and the unavoidable gnome-style native applications that really do not fit well in the style of the distro.

The same pattern occurred around 10 years ago in code editors. We came from the native editors ofBBEdit, Textmate (also promoted byDHH), Notedpad++ and Sublime to Electro-powered apps like Atom,VSCode and all its forks. The hardcore, moved to vim or emacs, trading immediate feedback and higher usability for the steepest learning curve I’ve seen.

#### Windows

The lesson is clear: Native applications are losing. Windows is doing theGUIlibrary standard joke. Because oneAPIdoes not have success, they make up another one, just for that one to fail within the sea of alternatives that exist.

MFC(1992) wrapped Win32 in C++. If Win32 was inelegant,MFCwas Win32 wearing a tuxedo made of other tuxedos. Then cameOLE.COM. ActiveX. None of these were reallyGUIframeworks – they were component architectures – but they infected every corner of Windows development and introduced a level of cognitive complexity that makes Kierkegaard read like Hemingway.

—Jeffrey Snover, inMicrosoft hasn’t had a coherentGUIstrategy since Petzold

Since then, Microsoft has gone through Winforms,WPF, Silverlight, WinUIs,MAUIwithout success. Many enterprise and personal desktop application still rely on Electron Apps, and the last memory of coherent visual integration of the whole OS I have is of Windows 98 or 2000.

It turns out that it’s a lot of work to recreate one’s OS and UIAPIs every few years. Coupled with the intermittent attempts at sandboxing and deprecating “too powerful” functionality, the result is that each new layer has gaps, where you can’t do certain things which were possible in the previous framework.

— Domenic Denicola, inWindows Native App Development Is a Mess

#### Linux

The UI inconsistency in Linux was created by design. Different teams wanted different outcomes and they had the freedom to do it.GTKand Qt became the two reigning frameworks. While Qt is most known for it, both aimed to support cross-platform native development (once upon a time, I successfully compiled gedit on Windows, learning a lot about C compilation, make files and environment variables in the process) but are only widely used in Linux land. Luckily, applications made in the different toolkits can look okay-ish next to each other, something that the different frameworks on Windows fail to achieve. How many engineer-hours does it take to redo the windows Control Panel?

Given the difficulty in testing the million different combinations of distros, desktop environments and hardware in general, most companies do not bother with a native Linux application — they either address it using electron (minting the lock-down), or they let the open-source community solve it self (when they have openAPIs).

#### macOS

Apple used to be a one-book religion. Apple’sHuman Interface Guidelinesused to be cited by every User Interface course over the world. XeroxPARCand Apple were the two institutions that studied what it means to have a good human interface. Fast forward a few decades, and Apple is doing thebestworst it can to break all the guidelines and consistency it was known for.

Now, Apple has beenignoring Fitts’ law,making resizing windows near-impossible(even after trying to fix it) andadding icons to every single menu. MacOS is no longer the safe heaven where designers can work peacefully.

#### Electron

Everyone knows that the user experience of electron apps sucks. The most popular claim is the memory consumption, which to be fair has been decreasing over the last decade, but my main complaint (as I usually drive a 64GBRAMMacBook Pro) is the lack of visual consistency and lack of keyboard-driven workflows. Looking at my dock, I have 8 native apps (text mate and macOS system utilities) and 6 electron apps (Slack, Discord, Mattermost, VScode, Cursor, Plexampp). And that’s from someone who really wishes he could avoid having any electron app at all.

Let us take the example of Cursor (but would be true forVSCode as well). If you are in the agent panel, requesting your next feature, can you move to the agent list on the side panel with just the keyboard? Can you archive it? These are actions that should be the same across every macOS application, and even if there are shortcuts, they are not announced in the menus. And over the last decade, developers have been forgetting to add menus to do the same things that are available in their application (mostly because the application isHTMLwithin its sandbox). For the record, Slack does this better than the others, but it’s not perfect.

#### Restarting from scratch

Together with Dart, Google wanted to design a new operating system, without all the legacy of Android, for new devices. It wanted a fresh UI toolkit (Flutter UI) but Google gave up on the project before a real product was launched. It’s one of those situations where having a monopoly (or a large enough slice of the market) is required to succeed.

Meanwhile,Zeddid the same thing in Rust: they designed their ownGPU-renderer library (GPUI) which is cross-platform. Despite the high-speed, it lacks integration with the host OS on itself, requiring the developers to add the right bindings. Personally, I would rather have a slow renderer that integrated with my OS than the extra speed.

#### TUIs

TUIs are fast, easy to automate (RIPAutomator) and work reasonably well in different operating systems. You can even run them remotely without any headache-inducingX forwarding. When the native UI toolkits fail, we go back to basics. Claude and Codex have been very successful on the command-line: you focus on the interaction and forget about the operating system around you. You can even drive code and apps on cloud machines, or remote into yourGPU-powered machine from your iPad.TUIs are filling the void left by Apple and Microsoft in the post-apocalyptic world where every application looks different. Which is good if you are doing art (including computer games), but not if your goal is to get out of the way of letting the user do their job.

#### What’s next

A checkbox is also part of an interface. You’re using it to interact with a system by inputting data. Interfaces are better the less thinking they require: whether the interface is a steering wheel or an online form, if you have to spend any amount of time figuring out how to use it, that’s bad. As you interact with many things, you want homogeneous interfaces that give you consistent experiences. If you learn that Command + C is the keyboard shortcut for copy, you want that to work everywhere. You don’t want to have to remember to useCTRL+ Shift + C in certain circumstances or right-click → copy in others, that’d be annoying.

—John LoeberinBring Back Idiomatic Design

We need to go back to the basics. Every developer should learn the theory of what makes a good User Interface (software or not!), likeNielsen,NormanorJohnson, and stop treating User Design as a soft skill that does not matter in the Software Engineering Curriculum. In any course, if the UI does not make any sense, the project should be failed. And in theHCIcourse, we should aim for perfect UIs. It takes work, but that work is mostly about understanding what we need. The programming is already being automated.

Operating systems and Toolkits authors should drive this investment. They should focus on making accessible toolkits that developers want to use, and lower the barrier to entry, making those platforms last as long as possible. I do not necessarily argue for cross-platform support, but having one such solution would help reduce the electron andTUIdependency.

			Published:
			

May

03
,
				
2026

			Author: Alcides Fonseca
		

			Language: English
		

			Tags:
			
				
Software Engineering
, 
			
				
User Interfaces