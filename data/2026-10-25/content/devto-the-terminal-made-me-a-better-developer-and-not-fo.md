---
title: The Terminal Made Me a Better Developer (And Not for the Reasons I Expected) - DEV Community
url: https://dev.to/sizzlebop/the-terminal-made-me-a-better-developer-and-not-for-the-reasons-i-expected-nn6
site_name: devto
content_file: devto-the-terminal-made-me-a-better-developer-and-not-fo
fetched_at: '2026-10-25T14:49:16.423389'
original_url: https://dev.to/sizzlebop/the-terminal-made-me-a-better-developer-and-not-for-the-reasons-i-expected-nn6
author: Jessica Doering
date: '2026-10-19'
description: When I first started using the terminal, sure, it was useful. I could navigate around directories,... Tagged with productivity, linux, beginners, terminal.
tags: '#productivity, #linux, #beginners, #terminal'
---

Curiosity beats memorizing commands

When I first started using the terminal, sure, it was useful. I could navigate around directories, install packages, run a dev server, do some Git stuff. But most of those things could also be done by clicking a few buttons.

And clicking buttons seemed perfectly reasonable to me.

I wasn't really sure about being one of those people who does absolutely everything from a terminal just because I can.

But the more I got into development, and especially the more time I spent working with Linux, the more I found myself using it.

Sometimes because it was faster. Sometimes because whatever I was trying to do didn't have a convenient graphical option. And sometimes because I was following instructions and had absolutely no idea what half the commands were doing.

Eventually, I started getting curious about that last part.

What was that command actually doing? Why did it work? Why did it fail? And why was I running it in the first place?

Somewhere along the way, I realized I was learning a lot more than how to use a command line.

I was starting to understand how things worked underneath all the nice interfaces I'd gotten used to.

And that's been far more useful than learning to type commands quickly.

## I started paying more attention to the filesystem

I've always understood files and folders. I think most of us have been moving things around in file managers for years without giving it much thought.

But working in the terminal made me pay attention to things I normally wouldn't have noticed.

For example:

pwd
ls
 
-la

cd
 ..

Enter fullscreen mode

Exit fullscreen mode

Nothing exciting there, right?

But when you're working in the terminal, knowing where you are actually matters.

I've lost count of how many times I've tried running something only to discover I wasn't in the directory I thought I was.

Or wondered why a configuration file wasn't showing up, only to remember it was hidden.

Or had something fail because I used a relative path without thinking about what it was relativeto.

These are pretty basic things, but they're also things I could get away with not thinking about when I was just clicking through folders.

I started paying more attention to hidden files, symbolic links, absolute versus relative paths, and where applications store their configuration.

And suddenly, a bunch of little things that used to confuse me started making more sense.

Not because the terminal magically made me smarter. I just had to understand what I was doing instead of relying on an interface to handle it for me.

## I finally started understanding processes

This was a big one for me.

When you open an application normally, you click an icon and it opens. When you're finished, you close it.

Simple enough.

But there's a lot going on behind that, and I didn't always give it much thought.

Running things from the terminal made processes a lot more visible.

Especially when working on web apps.

If you've spent any time developing with Vite, you've probably encountered the dreaded port-already-in-use situation.

You try to start your dev server, and something is already sitting on the port you wanted.

Sometimes it's another instance of your app that you forgot was still running. Ask me how I know.

Instead of just closing random terminal windows and hoping for the best, I started learning how to see what was actually running.

ps aux
pgrep 
-af
 node
ss 
-ltnp

Enter fullscreen mode

Exit fullscreen mode

And if I specifically want to know what's listening on port 5173:

ss 
-ltnp
 | 
grep
 
':5173'

Enter fullscreen mode

Exit fullscreen mode

These commands let me investigate the processes and listening sockets on my system. Depending on permissions, I might not be able to see every process associated with a socket, but it's a useful place to start.

It seems like a small thing, but understanding the relationship between a running application, its process, and the port it's using helped a lot of other concepts click for me.

Before, I knew my dev server was running because the browser showed my app.

Now I had a better idea of whatrunningactually meant.

## Permissions started making a lot more sense

Linux permissions were another one of those things I sort of understood in theory.

Read, write, execute. Got it.

Except apparently I didn't always get it, because I'd still run into situations where I couldn't modify a file or execute a script and wonder what the hell was going on.

The terminal made it easier to actually look at what was happening.

ls
 
-l
 script.sh

stat 
script.sh

Enter fullscreen mode

Exit fullscreen mode

Instead of just getting a permission-denied message and being annoyed about it, I could check who owned the file and what permissions it had.

I started understanding why a file might be readable but not writable, or why a script wouldn't execute even though it was sitting right there.

I also learned that execute permission on a directory doesn't mean quite the same thing as execute permission on a file. On a directory, it's about being able to traverse it.

That's one of those little Linux details that seems weird until you understand it.

And then there'ssudo.

I think it's pretty easy when you're learning Linux to see a permission error and think, well, I'll just stick sudo in front of it.

Problem solved!

Except maybe not.

You might get the command to work, but you still don't know why it needed elevated permissions. And depending on what you're doing, you might end up creating files owned by root that really shouldn't be.

I've learned that getting something to work and understanding why it wasn't working are two very different things.

That lesson has come up quite a bit in development, actually.

## Networking became a little less mysterious

Networking is one of those subjects where I understood the general concepts long before I felt comfortable troubleshooting anything.

I knew what DNS was. I knew what ports were. I understood that applications communicate over networks.

Great.

But when something wouldn't connect, that knowledge didn't necessarily tell me where to start.

Was the hostname resolving? Was the server actually responding? Was my application even listening on the port I thought it was?

Or had I somehow managed to break something entirely unrelated?

The terminal gave me a way to start narrowing those things down.

dig example.com
curl 
-I
 https://example.com
ss 
-ltn

Enter fullscreen mode

Exit fullscreen mode

These commands look at different pieces of the puzzle.

diglets me check DNS resolution.

curllets me make an HTTP request and inspect the response.

Andsslets me see which TCP ports are listening on my own system.

None of these commands will magically explain every network problem, obviously. But they give me somewhere to start.

And I think that's what made the biggest difference.

I stopped treating every connection failure as one big mysterious problem and started trying to figure out which part was actually failing.

Because "my app can't connect" could mean quite a few different things.

And knowing which one you're dealing with makes troubleshooting a whole lot easier.

## I got better at actually reading errors

This might sound ridiculous, but I think one of the most useful things I've learned from working in the terminal is to actually read what my tools are telling me.

Not just glance at the error, decide something is broken, and immediately start trying things until it works.

I meanreallyread it.

When you're working in the terminal, you see a lot of output.

Compiler errors, dependency warnings, stack traces, server logs, and sometimes an absolutely ridiculous wall of text because one little thing went wrong.

At first, all that output can be overwhelming.

And sometimes it still is.

But the more I worked with it, the more I started recognizing what was worth paying attention to.

A missing environment variable isn't the same thing as a network request failing.

A dependency conflict isn't a syntax error.

And an application that crashes immediately is a very different problem from one that's running perfectly fine but not responding the way you expected.

I still have plenty of moments where I stare at an error wondering what on earth it's trying to tell me.

But I'm much more likely now to investigate the actual error instead of immediately throwing another possible solution at it.

And when I do have to look something up, I usually have a much better idea ofwhatI need to look up.

That's made a pretty big difference.

## The real benefit has been learning how to investigate things

I think this is the part I didn't expect when I started using the terminal more.

I thought I'd learn some useful commands. Maybe speed up a few workflows.

What I didn't expect was how much it would change the way I approached problems.

Now, when something doesn't work, I'm more likely to start asking questions.

Where is this command actually running?

What process is using that port?

Who owns this file?

Is the server responding at all?

What does the error message actually say?

And I don't mean that I always know how to figure these things out.

Far from it.

Half the time I'm still looking up commands, reading documentation, or finding out that the thing IthoughtI understood works a little differently than I expected.

But that's kind of the point.

I don't think being comfortable with the terminal means memorizing hundreds of commands or being able to type some ridiculous one-liner from memory.

It means knowing that there's probably a way to investigate what's happening, and being willing to figure out how.

Sometimes that means using a command I already know.

Sometimes it means spending twenty minutes reading documentation to figure out why that command didn't do what I expected.

Both are useful.

## A few things worth experimenting with

If you're relatively new to the terminal, or you've mostly been using it to install packages and start development servers, here are a few little exercises worth trying.

These examples are mostly aimed at Linux, since that's what I use. Some commands will be different on macOS or Windows.

The goal isn't to memorize them. It's to look at what they show you and try to understand why that information matters.

### 1. Take a closer look at a project directory

Open a terminal inside one of your projects and try:

pwd
ls
 
-la

find 
.
 
-maxdepth
 2 
-type
 f

Enter fullscreen mode

Exit fullscreen mode

Look at where you are, which files are hidden, and how things are organized.

Try running the commands from different directories and see what changes.

Pay particular attention to relative paths. They're simple until they're the reason something isn't working.

### 2. Find your development server

Start a development server like you normally would.

Then open another terminal and run:

pgrep 
-af
 node
ss 
-ltnp

Enter fullscreen mode

Exit fullscreen mode

If you're using a Node-based development server on Linux, see if you can find its process and the port it's listening on.

If you can't see the process information you expected, look into why. It might be a permissions issue, or your server might be running through a different executable.

The investigation is the exercise.

### 3. Look at file permissions

Pick a file in your project and run:

ls
 
-l
 package.json

stat 
package.json

Enter fullscreen mode

Exit fullscreen mode

What do all those permission bits mean?

Who owns the file?

What can the owner do that other users might not be able to?

You don't need to go changing permissions just to experiment. In fact, I'd recommend understanding what you're looking at before doing that.

### 4. See what happens during an HTTP request

Try:

curl 
-v
 https://example.com

Enter fullscreen mode

Exit fullscreen mode

There's quite a bit of information in that output.

Look at the connection details, TLS negotiation, request headers, and response headers.

You don't need to understand every line right away.

Pick something unfamiliar and look it up.

That's literally how I've learned a lot of this stuff.

### 5. Experiment with pipes

Here's a tiny one:

printf
 
'apple\nbanana\napricot\n'
 | 
grep
 
'^a'

Enter fullscreen mode

Exit fullscreen mode

You should see:

apple
apricot

Enter fullscreen mode

Exit fullscreen mode

That little|sends the output of one command into another command.

It's such a simple idea, but it's also one of the things that makes Unix-like command-line environments so useful.

Instead of needing one giant tool that does everything, you can connect smaller tools together.

Once that concept clicks, a lot of terminal workflows start making more sense.

And it's worth experimenting with beyond this little example.

## You don't have to do everything in the terminal

I should probably mention this because I know how these conversations sometimes go.

I am not suggesting everyone should abandon graphical applications and spend the rest of their lives staring at a terminal window.

I use graphical applications all the time.

There are plenty of things I'd rather do with a good interface, and I'm not going to make my life unnecessarily complicated just to prove I can do something from the command line.

I also don't think using a terminal automatically makes someone a better developer.

You can copy and paste commands all day without understanding a single thing about what they do. Just like you can click around a graphical interface without really knowing what's happening.

The difference, at least for me, has been curiosity.

When I started paying attention to what commands were doing, why they were working, and why they occasionally failed spectacularly, I started learning a lot more.

The terminal just makes it particularly easy to see some of the things that graphical interfaces usually handle for you.

## It's not really about typing faster

I started using the terminal because it was useful.

And sure, I've gotten faster at certain things. There are plenty of tasks where opening a terminal and typing a command is easier than clicking through a bunch of menus.

But that hasn't been the most valuable part.

What's really changed is how I see the software I'm working with.

An application isn't just something that opens when I click an icon anymore. There are processes running, files being accessed, permissions being checked, network connections being made, and all kinds of smaller things happening behind the scenes.

And when something goes wrong, I have a much better idea of where to start looking.

I still have a ridiculous amount to learn. I look things up constantly, experiment with things I don't fully understand yet, and occasionally break something because I was a little too confident.

But I'm getting better at figuring things out.

And that's what working in the terminal has really helped me with.

Not becoming some command-line expert.

Just becoming a better investigator.

Which, the more I learn about development, the more I realize is a pretty important skill.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse