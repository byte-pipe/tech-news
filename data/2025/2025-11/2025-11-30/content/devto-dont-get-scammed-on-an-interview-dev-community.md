---
title: Don't get scammed on an interview. - DEV Community
url: https://dev.to/ackvf/dont-get-scammed-on-an-interview-4f92
site_name: devto
fetched_at: '2025-11-30T11:06:32.293266'
original_url: https://dev.to/ackvf/dont-get-scammed-on-an-interview-4f92
author: Qwerty
date: '2025-11-26'
description: A practical, experience-based guide on how to identify interview scams targeting developers and how to safely inspect unknown code using GitHub Codespaces. Tagged with software, interview, scam, guide.
tags: '#software, #interview, #scam, #guide'
---

### Don't get scammed on an interview.

So… I just went through two “interviews” that turned out to be scams. Both followed the same playbook:they gave me a repo link, told me to share my screen, and asked me to install + run the project during the call.

On afirstinterview.

That alone feels off, right? But these scammers have gotten smarter. They’ll do the whole friendly intro, talk about the company, show you a project, ask about your past work — the whole thing feels legit until suddenly you’re the one walkingthemthrough a repo on your machine.

Luckily, I had a gut feeling something wasn’t right. I isolated everything, sandboxed the repo, and ended up finding a bunch of red flags… including a hidden script or a fake MetaMask popup that lookedexactlylike the real extension.

The worst thing is that while I already knew this was a scam, I heardanother scammerin the background doing the same thing to another poor dev. I even saw their cursor moving in a shared Figma file. However, it was hilarious to watch the panic after I wrote this:

Anyway, this wasn't my first experience either, but seeing how profitable these scams must be, I finally decided to write about it to help other devs avoid getting burned.Take this as advice from a friend who just dodged a bullet.

## tl;dr

If you are interest in knowing how tospotthese scams, read on, otherwise skip directly to theHow to protect yourselfsection for a detailed guide, or skip all the way to thestep-by-step screenshot guide, or just remember these key points:

If you are in a rush to open unknown repos, useGitHub Codespacesorcodesandboxwith Copilot or another AI integration to analyze the repo for malicious intent and to run it in a safe environment.

GitHubcodespaceis a VSCode in the browser atgithub.devthat gives everyone60 hr freecompute time every month - ideal also for scoped home assignments.

Alternatively, you can self-host full VSCode IDE in a docker withcode-server, or just use VSCode Server in a docker and connectremotelywith any VSCode. You can also tryDev Containersfor free and completely local, that do all that, batteries included.

Btw,what is the difference between github.dev and vscode.dev?

## Why listen to me?

I am a software developer with 10 years of experience interviewing at real companies. As a remote contractor, I've worked on 20 projects ranging from few months to couple years and the number of interviews done is significantly higher(20 just this year). Here are the red flags I noticed.

## The red flags

Flags hidden in plain sight.You saw the crimson early.The tears weren’t yours.

### Different ways to get scammed and the First Red Flags

There are multiple ways how these scammers try to invade your system or steal your credentials.

* some try to scam you right away via fake conferencing apps
* some will let you try a demo project even before the interview and ask you to provide"feedback and suggestions for improvement"
* some will ask you to clone and run a repo on your machine with the same agenda either as ahomeworkor during an interview
* and others try to build trust first by actually conducting a full interview

#### 🟥 Never use unknown conferencing apps

Insist on using Zoom, Google Meet, Microsoft Teams, Telegram or other mainstream apps.They are available on desktop, mobile as well as in abrowser, so you shouldn’t have any issues joining without installing anything. If it was legitimate, they would agree without any problems, especially if e.g. teams don't work for you, so you ask to use another.

Be wary of links like meet.google.com.join.1bc-23e-h4j.com or zoom.us.joinsession.com and similar. Those are legitimately looking malicious sites, the important bit is the domain name before .com (or other TLD) - that’s the actual site you are visiting.

If you are curious, before you open any links, use incognito browser mode without any sensitive cookies or extensions enabled to avoid leaking your credentials.

#### 🟥 If they want you to install software, it's a scam

Never install unknown software on your machine. I have never experienced a real interview that required installing anything beyond mainstream conferencing apps.

#### 🟥 If they give you access to their full repo, it's a scam

If they ask you to inspect their full repo or Figma design document and give feedback, it’s absolutely a scam. No real company would give away their intellectual property like that.

Though, sometimes you are required to do a home assignment, but that’s different. In that case, you get a limited repo or a coding challenge designed specifically for interviews - and this is what this post is about and how to detect this, because you can absolutely get scammed even during these assignments.

#### 🟥 If the offer sounds too good to be true, it probably is

... too good to be true.

These scammers always have multiple “open positions” they’re trying to fill, regardless of your actual skills or experience. Full time, part time, freelance, junior, senior — they’ll claim to have something for everyone. They will promise you a high salary, or claim to have a position that perfectly matches your skills.

#### 🟥 Do a background check on their profile

I was once contacted on LinkedIn by a 72 year old "senior web3 recruiter" who was previously a certified hypnotherapist of 40 years.

The plot twist?

Thereal guy, an actual hypnotherapist, died 2 years prior which I found after reverse-image searching his profile picture.

### 🟥 The second Red Flag: The way They talk to you

If you get past the initial obvious signs mentioned above, there are more subtle red flags to watch out for.

One thing I didn’t expect is how predictable thecommunication styleof these scammers is.If you pay attention, you can spot them before you ever touch a repo.

Here are the patterns I noticed — and once you see them, you can’t unsee them.

#### They sound surprisingly unprofessional

You’d expect an experienced recruiter or a senior engineer to speak clearly, guide the discussion, explain the agenda, and set expectations.

With scammers, it’s the opposite:

* no real structure
* unclear questions
* unclear instructions
* often poor English and vague phrasing
* awkward pauses
* jumping between topics without transitions
* not really going into depth on anything
* proceeding with their script regardless of what you say or fails you make
* noisy/bussy room

#### They’re often inexperienced or too “casual”

Young,impatient, and not used to real hiring processes.They don’t probe deeply into your experience.They don’t ask follow-ups.They don’t explore your reasoning.

It feels like someone trying topretendthey’re running an interview rather than someone who actually does this for a living.

#### They rush the introduction phase

The intro is usually the weakest part of the whole act, because scammers:

* don’t understand the actual product
* can’t answer deep questions
* aren’t trained in interview structure
* don’t want to waste time

#### They don’t actually care about your career or fit

They don't care about:

* how you think
* how you solve difficult challenges
* how you collaborate
* what kind of developer you are
* whether you’re someone they want to hire

Real interviewers are curious about you, your story, your skills and thought process.

#### They have a short fuse

If you hesitate, ask questions, or try to clarify anything, they get impatient or even annoyed. Real interviewers arepatient and willing to explain things clearly. You can try it by simply playing dumb on purpose for a bit and see how they react - it's really fun actually :-).

#### They overpraise you excessively

Another thing I noticed: when I showed my portfolio, the reactions were overly enthusiastic to the point of feeling fake — constant “wow, amazing, man!” every few seconds. Experienced interviewers might acknowledge good work, but they don’t oversell it like that. Excessive praise is just anothersocial engineeringtactic to build quick trust and rush you past your instincts.

In a real interview, you should feel like you’re having a professional conversation with someone who knows what they’re doing and is genuinelyinterested in the detailsyou share.

If it feels off, it probably is.

#### Disabled camera or filters are a red flag too

If they don’t turn on their camera, that’s a big warning sign. Real interviewers and developers always show their face and expect the same from you at any stage of the interview. I can’t stress this enough: in my ~50+ interviews, I have never had a single call where at least one person didn’t already have their camera on when I joined. While this isn’t a hard rule, it’s a very strong convention in tech interviews.

And if theydoturn it on, pay attention to their background, lighting, and overall professionalism. A messy or odd setup can be a sign they’re not who they claim to be. Even recruiters working from home make an effort to look presentable.

Also be wary of AI filters or avatars— they’re terrifyingly good now. Watch for subtle glitches: unnatural blinking, strange eye contact, stiff facial expressions, lips not syncing to speech, or weird distortions when they move and turn their head. If something feels off visually, trust that feeling.

### 🟥 The last Red Flag: They make You share Your screen

Real companies don’t ask you to share your screenin the first interview- be it to show your portfolio (they usually want portfolio ahead of time, with your CV), run code, or anything else.Real companies don’t ask you to clone and run their repo in the first 45 minutes of meeting you.They especially don’t sit back and watch your screen like it’s a Twitch stream.

In any normal code-review-style interview, it's usually asecond or third roundand the interviewer sets up a shared multi-user coding environment using codesandbox or the likes and only then maybe ask you to share your screen, or just connect to a session. You don’t open unknown software on your machine while strangers watch your desktop icons, extensions, file paths, and environment variables.

If someone insists on you running their repo early in the process: that’s your warning.

## How to protect yourself

Even in completely legitimate situations, if you find yourself in a situation where you’re being asked to run unknown code, here are the steps to protect yourself:

You can skip this section if you only want to see thestep-by-step guide.

### Use isolated coding environment

There are multiple ways to do this, depending on your needs, resources andtime.

#### Dev Containers - VSCode extension

You can exploreDev Containersthat come with a VSCode extension, it runs locally in Docker or in cloud, batteries included.

#### Linux in Docker

Another option is to set up a Docker image yourself with a prebuilt image or clean Linux. Experience very similar to just using WSL for development. You will connect "remotely" from your local VSCode over SSH, which triggers the installation of VSCode Server. From there you can install node and other dependencies, and clone and run the repo; fully isolated.

#### Self-hosted VSCode in Docker

As we move to the cloud, you can self-host full VSCode IDE in a docker withcode-server. This will give you web-based VSCode that you can access from any browser, any device, anywhere. Great for occasional development from a tablet.

#### GitHub Codespaces or codesandbox

Some might argue that Docker is not 100% secure, so that leaves us with Virtual Machines or 3rd party cloud providers, such asGitHub Codespacesorcodesandbox.

GitHub Codespacesprovides 60 hours offree compute timeevery month, which is more than enough for scoped home assignments or interviews. It’s a full VSCode in the browser atgithub.devorvscode.dev.

What is the difference between github.dev and vscode.dev?Difference between the two is that github.dev is more integrated with github: automatic login, and some github related extensions, including Github Copilot and the github visual theme. It can load any github repo from the command prompt, or by pressing.on a keyboard while on any github page, or just by replacing thegithub.comwithgithub.devin the URL.vscode.dev requires you to log in if you want to synchronize your settings and extensions and it can load github and azure repos in a similar way by appending the full urlvscode.dev/dev.azure.com/myRepo.

However, in my experience it is much faster to just usegithub.devfor any repositories even outside of github such as bitbucket or gitlab, because a Codespace requires you to start from a repo on github or to create a new one, andhttps://github.com/github/devis such a minimalistic repo that loads with github.dev by default.

### Analyze the repo with AI tools

Before you run any unknown code, use AI tools to analyze it for malicious intent. You can use GitHub Copilot, ChatGPT, or other AI assistants to review the codebase quickly. All of them are available as extensions in VSCode, so you can use them directly in your isolated coding environment. GitHub Copilot is also availablefor freein GitHub Codespaces.

* UseAgent modeto scan the whole codebaseA simple prompt"Analyze this codebase for any malicious scripts, hidden backdoors, or suspicious behavior. Summarize your findings."should do.
* A simple prompt"Analyze this codebase for any malicious scripts, hidden backdoors, or suspicious behavior. Summarize your findings."should do.
* Ask specific questions about dependency files, configuration scripts, or parts of the code that seem suspicious.

Tip: Watch for unknown dependencies, suspiciously large files and obfuscated code. The following is a pretty common code injection. A normally lookingtailwind.config.jsfile, but there was a malicious one-line code inserted after at least a thousand spaces, completely unnoticeable to a naked eye.

## Step-by-step guide that is completely free and instant

This guide uses GitHub Codespaces. It's free and instant to start. You get a full VSCode IDE in the browser with terminal access, extensions, GitHub Copilot, and everything you need to inspect and run the code safely.

* docs:Codespaces: Free quota
* docs:Codespaces: Free unit consumption multiplier and pricing
* docs:GitHub Copilot Free
* account:Billing / Usage dashboard

#### 1. Open the repo link in your browser

* If it is a github repo, while browsing it, hit.on the keyboard or replacegithub.comwithgithub.devin the URL, which will launch the repo in github.dev browser VSCode.
* If not, copy the clone command (URL).

#### 2. Start a Codespace on github.dev

If the TERMINAL button doesn't appear, open Command Palette and find

Codespaces: Continue working in New Codespace

Choose2 coresfor 60 hours of free computing time every month. Double the CPU halves the free hours.

#### 3. Clone the repo in the Codespace terminal(optional)

If it was not a github repo, clone it in the terminal:

git clone <REPO_URL>

cd
 <REPO_NAME>

Enter fullscreen mode

Exit fullscreen mode

#### 4. Analyze the code with GitHub Copilot

Open Command Palette and find

Chat: Open Chat

Switch toAgent mode. and ask it to analyze the codebase for malicious intent:

Analyze this codebase for any malicious scripts, hidden backdoors, or suspicious behavior. Summarize your findings.

Enter fullscreen mode

Exit fullscreen mode

If you find something, then that's your cue. You can use deobfuscation utilities to get more sense of the code or ask AI, if you are curious, but you should exit the interview.

* beautifier.io- online code beautifier

#### 5. Run the code safely

Follow the project’s README instructions to install dependencies and run the project. Since you’re in an isolated Codespace, any malicious code will be contained within this environment. But still be cautious before you enable access to any extensions.My suggestion would be to run it in a separate Browser profile orIncognito windowwithout any sensitive cookies or extensions enabled to avoid leaking your credentials, such as Metamask or other web3 wallets.

You will see a link in the terminal to open the running project in a new browser tab if it is a web application.

#### 6. Clean up

When you are done, stop the Codespace to avoid consuming more hours anddeletethe codespace from your GitHub account as it consumes GB-hours. (You get 15 GB for a month for free.) The codespace gets deleted automatically after 30 days of inactivity, too, if you forget.

Check the usage in thedashboard.

If you have already closed the Codespace tab, you can find it athttps://github.com/codespaces.

## Final thoughts

I don't want to waste any more of your time. This already blew beyond few simple screenshots into a more detailed guide, but I think it was worth it.

Thank you for reading and please,do share it with your junior developer friendsto help them avoid getting scammed. The scammers keep improving and move into organized operations, so it must be profitable for them, and with the rise of AI, they will get even more sophisticated.

Cheers! 🥂😎

Qwerty, signing out.

VeniVidiAbii

Vici

(I came; I saw; I left; I won)

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
