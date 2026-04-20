---
title: Microsoft Hasn’t Had a Coherent GUI Strategy Since Petzold | Jeffrey Snover's blog
url: https://www.jsnover.com/blog/2026/03/13/microsoft-hasnt-had-a-coherent-gui-strategy-since-petzold/
site_name: hackernews_api
content_file: hackernews_api-microsoft-hasnt-had-a-coherent-gui-strategy-since
fetched_at: '2026-04-06T11:21:48.891467'
original_url: https://www.jsnover.com/blog/2026/03/13/microsoft-hasnt-had-a-coherent-gui-strategy-since-petzold/
author: naves
date: '2026-04-05'
published_date: '2026-03-13T10:50:16+00:00'
description: 'A few years ago I was in a meeting with developers and someone asked a simple question: "What''s the right framework for a new Windows desktop app?" Dead silence. One person suggested WPF. Another said WinUI 3. A third asked if they should just use Electron. The meeting went sideways and we never did answer…'
tags:
- hackernews
- trending
---

A few years ago I was in a meeting with developers and someone asked a simple question: “What’s the right framework for a new Windows desktop app?”

Dead silence. One person suggested WPF. Another said WinUI 3. A third asked if they should just use Electron. The meeting went sideways and we never did answer the question.

That silence is the story. And the story goes back thirty-plus years.

When a platform can’t answer “how should I build a UI?” in under ten seconds, it has failed its developers. Full stop.

## The Last Time Windows Had a Clear Answer

In 1988, Charles Petzold publishedProgramming Windows. 852 pages. Win16 API in C. And for all its bulk, it represented something remarkable: a single, coherent, authoritative answer to how you write a Windows application. In the business, we call that a ‘strategy’.

Win32 that followed was bigger but still coherent. Message loops. Window procedures. GDI. The mental model was a bit whacky, but it wasonemental model. Petzold explained it. It was the F=MA of Windows. Simple. Powerful. You learned it. You used it. You were successful.

Clarity is your friend! One OS, one API, one language, one book. There was no committee debating managed-code alternatives. There was just Win32 and Petzold, and it worked. This was Physics not Chemistry (this works but only for this slice of the period table. And only under these pressures.  And only within this temperature. And only if the Moon is in the 7th house of Jupiter).

What happened next is a masterclass in how a company with brilliant people and enormous resources can produce a thirty-year boof-a-rama by optimizing for the wrong things.  AKABrillant people doing stupid things.

## The Object-Oriented Fever Dream (1992–2000)

Win32 had real limitations, so Microsoft did what Microsoft does: it shipped something new for the developer conference. Several somethings.

MFC (1992) wrapped Win32 in C++. If Win32 was inelegant, MFC was Win32 wearing a tuxedo made of other tuxedos. Then came OLE. COM. ActiveX. None of these were really GUI frameworks – they were component architectures – but they infected every corner of Windows development and introduced a level of cognitive complexity that makes Kierkegaard read like Hemingway.

I sat through a conference session in the late nineties trying to understand the difference between an OLE document, a COM object, and an ActiveX control. I looked at the presenter like they had a rat’s tail hanging out of his mouth for the entire hour.

Microsoft wasn’t selling a coherent story. It was selling technology primitives and telling developers to figure out the story themselves. That’s the Conference Keynote Cluster***k – Microsoft optimized for an executive impressing people with their keynote and not the success of the users or developers.

## PDC 2003 and the Vision That Ate Itself

At PDC 2003, Microsoft unveiled Longhorn – genuinely one of the most compelling technical visions the company had ever put in front of developers. Three pillars: WinFS (a relational file system), Indigo (unified communications), and Avalon – later WPF – a GPU-accelerated, vector-based UI subsystem driven by a declarative XML language called XAML. Developers saw the Avalon demos and wentnuts. It was the right vision.

It was also, in the words of Jim Allchin’s internal memo from January 2004, “a pig.”

By August 2004, Microsoft announced a complete development reset. Scrapped. Start over from the Server 2003 codebase. And after the reset, leadership issued a quiet directive: no f***ing managed code in Windows. All new code in C++. WPF would ship alongside Vista, but the shell itself would not use it.

The Windows team’s bitterness toward .NET never healed. From their perspective, gambling on a new managed-code framework had produced the most embarrassing failure in the company’s history. That bitterness created a thirteen-year institutional civil war between the Windows team and the .NET team that would ultimately orphan WPF, kill Silverlight, doom UWP, and give us the GUI ecosystem boof-a-rama we have today.

## Silverlight: The Pattern Established (2007–2010)

WPF shipped in late 2006. It was remarkable – XAML, hardware-accelerated rendering, real data binding. If Microsoft had made it the definitive answer and invested relentlessly, the story might have ended differently. Instead, in 2007, they launched Silverlight: a stripped-down browser plugin to compete with Flash, cross-platform, elegant, and the foundation for Windows Phone. Around 2010 it looked like the rich client future.

Then at MIX 2010, a Microsoft executive said in a Q&A that Silverlight was not a cross-platform strategy – it was about Windows Phone. HTML5 was now policy. The Silverlight team was not told this was coming. Developers who had bet their LOB applications on Silverlight found out from a conference Q&A.

Silverlight wasn’t killed by technical failure. The technology was fine. It was killed by a business strategy decision, and developers were the last to know.

Remember that pattern. We’ll see it again.

## The Metro Panic and the Two-Team War (2012)

Apple had sold 200 million iPhones. The iPad was eating into PC sales. Microsoft’s answer was Windows 8 and Metro – a touch-first runtime called WinRT that was deliberatelynotbuilt on .NET. Remember the Windows team’s bitterness? Here it manifests. WinRT was a native C++ runtime. Clean break from WPF, WinForms, and a decade of developer investment in .NET.

There were actually two stories being told simultaneously inside Microsoft. The Windows team was building WinRT. The .NET team was still evangelizing WPF. Different buildings, different VPs, different road maps.

What developers heard at //Build 2012: the future is WinRT, and also HTML+JS is first-class, and also .NET still works, and also C++ is back, and also you should write Metro apps, and also your WPF code still runs fine. That is not a strategy. That is a Hunger Games stage where six teams are fighting for your attention.

Enterprise developers took one look at UWP’s sandboxing, its Store deployment requirement, and its missing Win32 APIs, and walked away. The framework designed to win them into the modern era had been optimized for a tablet app store that never materialized.

## UWP and the WinUI Sprawl (2015–Present)

Windows 10 brought Universal Windows Platform – write once, run on PC, phone, Xbox, HoloLens. Compelling on paper. The problem: Windows Phone was dying, and Microsoft’s own flagship apps – Office, Visual Studio, the shell itself – weren’t using UWP. The message was clear even if no one said it out loud.

When UWP stalled, the official answer becameit depends. Use UWP for new apps, keep WPF for existing ones, add modern APIs via XAML Islands, wait for WinUI 3, but also WinUI 2 exists for UWP specifically, and Project Reunion will fix everything, except we’re renaming it Windows App SDK and it still doesn’t fully replace UWP and…

Brilliant people doing stupid things. Technological Brownian motion.

Project Reunion / WinUI 3 represents genuine progress. But ask yourself why the problem existed at all. UWP’s controls were tied to the OS because the Windows team owned them. The .NET team didn’t. The developer tools team didn’t. Project Reunion was an organizational workaround dressed up as a technical solution.

One developer’s summary, written in 2024: “I’ve been following Microsoft’s constant changes: UAP, UWP, C++/CX replaced by C++/WinRT without tool support, XAML Islands, XAML Direct, Project Reunion, the restart of WinAppSDK, the chaotic switch between WinUI 2.0 and 3.0…” Fourteen years. Fourteen pivots. That person deserves a medal and an apology, in that order.

## The Zoo Without a Zookeeper

Here is every GUI technology actually shipping on Windows today:

Microsoft native frameworks:

* Win32(1985) – Still here. Still used. Petzold’s book still applies.
* MFC(1992) – C++ wrapper on Win32. Maintenance mode. Lives in enterprise and CAD.
* WinForms(2002) – .NET wrapper on Win32. “Available but discouraged.” Still fastest for data-entry forms.
* WPF(2006) – XAML, DirectX-rendered, open source. No new Microsoft investment.
* WinUI 3 / Windows App SDK(2021) – The “modern” answer. Uncertain roadmap.
* MAUI(2022) – Cross-platform successor to Xamarin.Forms. The .NET team’s current bet.

Microsoft web-hybrid:

* Blazor Hybrid– .NET Razor components in a native WebView.
* WebView2– Embed Chromium in a Win32/WinForms/WPF app.

Third-party:

* Electron– Chromium + Node.js. VS Code, Slack, Discord. The most widely deployed desktop GUI technology on Windows right now – and Microsoft had nothing to do with it.
* Flutter(Google) – Dart, custom renderer, cross-platform.
* Tauri– Rust backend, lightweight Electron alternative.
* Qt– C++/Python/JavaScript. The serious cross-platform option.
* React Native for Windows– Microsoft-backed port of Facebook’s mobile framework.
* Avalonia– Open source WPF spiritual successor. Used by JetBrains, GitHub, Unity – developers who stopped waiting for Microsoft.
* Uno Platform– WinUI APIs on every platform. More committed to WinUI than Microsoft is.
* Delphi / RAD Studio– Still alive. Still fast. Still in vertical market software.
* Java Swing / JavaFX– Yes, still in production. The enterprise never forgets.

Seventeen approaches. Five programming languages. Three rendering philosophies. That is not a platform. I might not have a dictionary definition for the term boof-a-rama but I know one when I see it.

## The Lesson

Every failed GUI initiative traces back to one of three causes: internal team politics (Windows vs. .NET), a developer conference announcement driving a premature platform bet (Metro, UWP), or a business strategy pivot that orphaned developers without warning (Silverlight). None of these are technical failures. The technology was often genuinely good – WPF was good, Silverlight was good, XAML is good. The organizational failure was the product.

You either have a Plausible Theory of Success that covers the full lifecycle – adoption, investment, maintenance, and migration – or you have a developer conference keynote.

One is a strategy. The other is a thirty-year boof-a-rama.

Charles Petzold wrote six editions ofProgramming Windowstrying to keep up with each new thing Microsoft announced. He stopped after the sixth, which covered WinRT for Windows 8. That was 2012.

I don’t blame him.

### Share this:

* Share on X (Opens in new window)X
* Share on LinkedIn (Opens in new window)LinkedIn
* Share on Facebook (Opens in new window)Facebook
* Email a link to a friend (Opens in new window)Email
