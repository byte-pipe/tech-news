---
title: Your IDE is an Attack Vector - DEV Community
url: https://dev.to/aezur/your-ide-is-an-attack-vector-2i0b
site_name: devto
content_file: devto-your-ide-is-an-attack-vector-dev-community
fetched_at: '2026-02-15T19:11:37.116846'
original_url: https://dev.to/aezur/your-ide-is-an-attack-vector-2i0b
author: Peter Mulligan
date: '2026-02-12'
description: A new type of VSCode phishing attack is targeting freelancers via Upwork. Here’s how it works and how... Tagged with vscode, security, phishing, tooling.
tags: '#vscode, #security, #phishing, #tooling'
---

A new type of VSCode phishing attack is targeting freelancers via Upwork. Here’s how it works and how to protect yourself.

Hi, I'm Peter and I like to build things.

In recent years, we've seen a rise in high-profile attacks that use lifecycle hooks to run malicious code. The attack I am here to shine a spotlight on uses a similar "manipulate the tooling" mindset.

I work as a freelancer through a platform called Upwork. Over the last couple of months I have seen this platform turn into a hunting ground for a new type of phishing attack that uses VSCode as the attack vector.

It is an interesting attack because it sits somewhere between traditional phishing and spear phishing. It doesn't have a specific target but it doesn't cast a wide net. It uses a highly refined approach that enables the attacker to create a pool of self-selected high-value targets. Here's how it goes down...

## The Tech

Visual Studio Code has the concept oftasks. They are defined in.vscode/tasks.jsonat the root of the project. Tasks are best thought of as an interface between the editor and your local tooling. They let you describe how commands should be run; what shell to use, what arguments to pass, what order to run them in. That kind of thing. VSCode has native bindings for npm, Gulp, Grunt, and Jake.

This is an auto-generated task fornpm run build:

{


"version"
:

"2.0.0"
,


"tasks"
:

[


{


"label"
:

"npm: build"
,


"type"
:

"shell"
,


"command"
:

"npm"
,


"args"
:

[
"run"
,

"build"
],


"isBackground"
:

false
,


"problemMatcher"
:

[
"$tsc"
],


"group"
:

"build"


}


]

}

Enter fullscreen mode

Exit fullscreen mode

If you need to run commands for a build tool that VSCode doesn't have native bindings for, you can do that using acustom task. These let you run commands with a variety of options as shownherein the schema. For now, we're only interested in therunsOnoption.

From the docs:

Specifies when a task is run. Valid values are:

* "default": The task will only be run when executed through the Run Task command.
* "folderOpen": The task will be run when the containing folder is opened.

Now, if you're anything like me, the description offolderOpenis terrifying. Arbitrary code execution when the folder is opened? That can't be right. Surely there are protections in place?

There is a setting (task.allowAutomaticTasks) that lets you control the behavior. You can set it to always allow, always ask, or always deny. So we set it to "always ask" and we're good, right?

Unfortunately, as mentioned in thisGitHub issue, when you clone a new repository and VSCode asks you if you trust the authors, that choice takes precedence over your settings. If you click "yes", you have told VSCode that you trust this project explicitly.

## The Bait

The attacker posts a job on Upwork. On the surface, it looks the same as all the others. Tech stack and company description. Corporate jargon. Indistinguishable at first glance.

The jobs are almost exclusively in the crypto or DeFi domain. They are usually for between $75 and $150 per hour. They promise long-term work for the right candidate. They talk of technical excellence and team culture. It often mentions there will be a small take-home but not always.

Taken at face value, it looks like a good opportunity for a lot of developers. Developers in the crypto/DeFi sphere. Developers likely to have crypto wallets and api keys on their machine.

## The Social Dynamics

It is free to post a job on Upwork. Freelancers then pay a small amount to submit a proposal for the project. The client reads the proposals and invites potential candidates into a chat room to interview. This allows both sides to define terms before initiating the contract.

For the freelancer, it's time to close the deal. Pressure is high and you can see from Upwork's UI that the client is interviewing multiple developers. Better bring your A-game.

The client sends a GitHub link.

It is cloned without question.

Do you trust the authors of the files in this folder?

## The Payload

The handful of times I have encountered this attack (I stopped bidding on the jobs pretty quick!), the command being run was alotof whitespace followed by awgetto a Vercel endpoint being piped intocmd. 😱

The whitespace confused me at first until I viewed the code on GitHub. Their code-viewer doesn't wrap lines, so I needed to scroll to the right about 3 times the width of the page to see thewget.

I didn't know I was going to turn this into an article at the time and I did not download the content of the URLs so I don't know what the malicious code itself did, but from context it downloads a crypto wallet exfiltration script. I still have one of the URLs if someone more skilled than me wants to go poking around. Just reach out.

## Why This Attack Works

This attack is very well thought out. It puts itself in the target's shoes. I have no way of gathering data on itseffectivenessbut I can imagine it works wonders considering the amounts of these jobs posted daily.

The mechanics of Upwork do the heavy lifting of the social engineering. The ability to filter for crypto/DeFi developers and post a job for free provides frictionless target selection. The competitive and high-stress nature of the proposal system means you only interact with the target when they are already stressed. The platform’s social norm of running test repos, combined with the fact that freelancers are less likely to follow proper isolation protocols, makes this attack more robust.

The target selection is masterful, but combined with silent script execution when the project is opened in VSCode is devastating.

## How To Stay Safe

Only open random repositories in an isolated environment (container or VM). Inspect them before running anything. Does it have apostinstallorpreinstallscript? What do they do? Does it have a.vscodefolder? Why?

You can use VSCode'sdev containersfeature to open untrusted projects safely. From there, you can watch for any weird activity before it touches your main system.

You can also open projects with VSCode from the command line using the--disable-extensionsflag. (code --disable-extensions .)

The key takeaway: Treat anything you didn’t personally create as untrusted by default.

Connect with me onLinkedInorUpwork.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (30 comments)


For further actions, you may consider blocking this person and/orreporting abuse
