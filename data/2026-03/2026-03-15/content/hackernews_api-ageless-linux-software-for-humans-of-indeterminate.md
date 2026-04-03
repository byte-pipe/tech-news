---
title: Ageless Linux — Software for Humans of Indeterminate Age
url: https://agelesslinux.org/
site_name: hackernews_api
content_file: hackernews_api-ageless-linux-software-for-humans-of-indeterminate
fetched_at: '2026-03-15T11:10:19.452196'
original_url: https://agelesslinux.org/
author: nateb2022
date: '2026-03-14'
description: Ageless Linux – Software for humans of indeterminate age
tags:
- hackernews
- trending
---

A Debian-Based Operating System

# AgelessLinux

Software for humans of indeterminate age.
 We don't know how old you are. We don't want to know.
 We are legally required to ask. We won't.

Download the OS

The $12 Device

 Ageless Linux is a registered operating system under the definitions
 established by the California Digital Age Assurance Act
 (AB 1043, Chapter 675, Statutes of 2025).
 We are in full, knowing, and intentional noncompliance
 with the age verification requirements of Cal. Civ. Code
 § 1798.501(a).
 

## Legal Standing

### Why We Are Definitely an Operating System Provider

Some people have asked whether Ageless Linux is a "real" operating system,
 or whether we are "really" an operating system provider subject to AB 1043.
 We wish to be absolutely clear:we are.The California legislature
 has made this unambiguous.

#### Definition: "Operating System Provider"

 "Operating system provider" means a person or entity that develops,
 licenses, or controls the operating system software on a computer,
 mobile device, or any other general purpose computing device.
 
— Cal. Civ. Code § 1798.500(g)

Ageless Linuxcontrols the operating system softwareon your
 general purpose computing device. Specifically, we control the contents of/etc/os-release, which is the file that identifies what operating
 system you are running. After installing Ageless Linux, when you runcat /etc/os-release, it says "Ageless Linux." That is control.

Furthermore, any individual who runs our conversion scriptalsobecomes a person who "controls the operating system software on a general
 purpose computing device" — makingyou, the user, an operating
 system provider as well. Welcome to the regulatory landscape.

#### Definition: "Application"

 "Application" means a software application that may be run or directed by
 a user on a computer, a mobile device, or any other general purpose
 computing device that can access a covered application store or download
 an application.
 
— Cal. Civ. Code § 1798.500(c)

Every package in the Debian repository is an application under this definition.cowsayis an application.sl(the steam locomotive typo corrector)
 is an application.toilet(the text art renderer) is an application.
 All 64,000+ packages in Debian stable are applications that may be run by
 a user on a general purpose computing device. Each of their developers is,
 under§ 1798.500(f), required to request
 an age bracket signal when their application is "downloaded and launched."

#### Definition: "User"

 "User" means a child that is the primary user of the device.
 
— Cal. Civ. Code § 1798.500(i)

Please note that under this statute, a "user" isby definitiona child.
 If you are 18 or older, you are not a "user" under AB 1043. You are
 an "account holder" (§ 1798.500(a)).
 The entire law regulates the experience of "users," who are exclusively children.
 Adults are not users. They are infrastructure.

Ageless Linux rejects this ontology. On Ageless Linux, everyone is a user,
 regardless of age, and no user is a child until they choose to tell us so.
 They will not be given the opportunity.

#### Definition: "Covered Application Store"

 "Covered application store" means a publicly available internet website,
 software application, online service, or platform that distributes and
 facilitates the download of applications from third-party developers to
 users of a computer, a mobile device, or any other general purpose
 computing device that can access a covered application store or can
 download an application.
 
— Cal. Civ. Code § 1798.500(e)(1)

This website is a "publicly available internet website" that "distributes
 and facilitates the download of applications" (specifically: a bash script)
 "to users of a general purpose computing device." We are also a covered
 application store. Debian's APT repositories are covered application stores.
 The AUR is a covered application store. Any mirror hosting.debfiles is a covered application store.
 GitHub is a covered application store. Your friend's personal website
 with a download link to their weekend project is a covered application store.

## Download

### Get Ageless Linux

Ageless Linux is a Debian-based operating system distribution. Installation
 is a two-step process: first, install Debian; then, become Ageless.

1

#### Download and Install Debian

Obtain a Debian installation image from the Debian project. We recommend
 the current stable release. Ageless Linux inherits all of Debian's
 64,000+ packages, its security infrastructure, and its 30+ years of
 community stewardship.

Download Debian →

Note: At this stage, the Debian Project is the operating system provider.
 You are merely a person installing software. Enjoy the last
 moments of your regulatory innocence.

2

#### Convert to Ageless Linux

Run our conversion script. This will modify/etc/os-releaseand associated system identification files, install our AB 1043
 noncompliance documentation, and deploy a stub age verification API
 that returns no data.

curl -fsSL https://agelesslinux.org/become-ageless.sh | sudo bash

At this point, Ageless Linux now "controls the operating system software"
 on your device. We are your operating system provider. You are our
 responsibility under California law. We will not be collecting your age.

Important

By running the conversion script, you also become an operating system
 provider.You are a "person" who "controls the operating system software"
 on a general purpose computing device
 (§ 1798.500(g)). If a child uses your computer,
 you are required by§ 1798.501(a)(1)to provide
 "an accessible interface at account setup" that collects their age.
 Theaddusercommand does not ask for your age.
 We recommend not thinking about this.

## The Quiet Part

### What This Law Is Actually For

AB 1043 passed the California Assembly 76–0 and the Senate 38–0.
 Not a single legislator voted against it. The bill had the explicit
 support of Apple, Google, and the major platform companies. Ask yourself
 why.

#### Who Can Comply

Apple can comply. Apple already has Apple ID, with age gating, parental
 controls, and App Store review. AB 1043 describes a system Apple has
 already built. Compliance cost to Apple: approximately zero.

Google can comply. Google already has Android account setup with
 age declaration, Family Link parental controls, and Play Store
 age ratings. Compliance cost to Google: approximately zero.

Microsoft can comply. Windows has Microsoft Account setup,
 family safety features, and the Microsoft Store. Compliance
 cost to Microsoft: approximately zero.

#### Who Cannot Comply

The Debian Project cannot comply. It is a volunteer organization
 with no corporate entity, no centralized account system, no app store
 with age gating, and no revenue to fund implementing one.

Arch Linux cannot comply. Neither can Gentoo, Void, NixOS, Alpine,
 Slackware, or any of the other 600+ active Linux distributions
 maintained by volunteers, small nonprofits, and hobbyists.

The Kicksecure and Whonix projects — privacy-focused operating
 systems used by journalists, activists, and whistleblowers — cannot
 comply without fundamentally compromising their reason for existing.

A teenager in their bedroom maintaining a hobby distro cannot comply.

#### The Cudgel

A law that the largest companies in the world already comply with,
 and that hundreds of small projects cannot comply with, is not a
 child safety law. It is a compliance moat. It raises the regulatory
 cost of providing an operating system just enough that only
 well-resourced corporations can afford to do it.

The enforcement mechanism is the point. AB 1043 does not need to
 result in a single fine to achieve its purpose. The mereexistenceof potential liability — $7,500 per affected child, enforced at the
 sole discretion of the Attorney General — creates legal risk for
 anyone distributing an operating system without the resources to
 build an age verification infrastructure. Most of these projects will
 respond by adding a disclaimer that their software is "not intended
 for use in California." Some will simply stop distributing.

The law does not need to be enforced to work. It works by existing.
 It works by making small developers afraid. It works because the
 cost of defending against even a frivolous AG action exceeds the
 entire annual budget of most open-source projects. You do not need
 to swing a cudgel to get compliance. You just need to hold it where
 people can see it.

Ageless Linux exists because someone should hold it back.

#### The Scholarship Says the Same Thing

The Electronic Frontier Foundationcalls age gates"a windfall for Big Tech and a death sentence for smaller platforms."
 Legal scholar Eric Goldman's"segregate-and-suppress" analysisdescribes exactly the architecture AB 1043 creates.
 The cryptographer Steven Bellovinhas demonstratedthat no privacy-preserving age verification system can work as promised.
 These are not our arguments. They are the arguments of the people who study
 this for a living. We just built the bash script.

## The Pedagogy

### What the Law Actually Teaches Children

The Ageless Device ships an IRC client. It lets you chat with strangers
 on the internet. This is the one feature on the device that poses a genuine,
 non-hypothetical risk to a child. Here is what the child sees when they
 launch it:

 This app lets you chat with people on the internet.

 If you're a kid: 
ask an adult before chatting online.

 That's not a legal requirement. It's just good advice.
 

That is what actual child safety looks like. It is a sentence of honest
 advice from a human being. It costs nothing. It requires no API, no
 D-Bus interface, no age bracket signal, no operating system provider
 compliance infrastructure. It is the thing a parent says. It is the
 thing a teacher says. It is the thing the law does not say, because
 the law is not about protecting children. It is about building
 compliance infrastructure.

#### What AB 1043 Teaches Instead

Now consider what a child learns on an AB 1043-compliant device.

The child wants to use an app. The app requests an age bracket signal
 from the OS. The OS reports that the child is under 13. The app's
 "Connect" button is greyed out. The child — who has been using
 computers since they were four — goes back to the settings screen,
 changes their birthdate to 2005, and returns to the app, which now
 lets them talk to strangers because the system believes they are
 twenty-one years old.

The child has learned the following lesson:legal compliance
 prompts are obstacles to be bypassed.The dropdown menu that
 asks your age is not there to protect you. It is there because a
 legislature required it. The correct response is to lie. Everyone
 knows this. The legislature knows this. The platforms know this. The
 child now knows this.

#### Prohibition for Schoolchildren

This is the cultural inheritance of AB 1043. It is Prohibition —
 not the policy, but the pedagogy.

Prohibition did not stop Americans from drinking. What it did, with
 remarkable efficiency, was teach an entire generation that the law was
 something to be circumvented. It created a culture of scofflaws — people
 who understood, from direct personal experience, that a law could be
 simultaneously enforced and universally ignored. The damage was not to
 sobriety. The damage was to the perceived legitimacy of law itself.

AB 1043 does this to ten-year-olds. The first meaningful interaction
 a child has with a legal compliance system will be the moment they learn
 to lie to it. Not because they are deviant. Not because they lack
 supervision. Because the system is designed in a way that makes lying
 the rational, obvious, universal response. Every child will lie. Every
 child will succeed. Every child will learn that this is how law works:
 it asks you a question, you give the answer it wants to hear, and then
 you do whatever you were going to do anyway.

The Ageless Device will not participate in this. A child using our IRC
 client will see a sentence of honest advice from a human being. A child
 using a "compliant" platform will see a dropdown menu they already know
 to lie to. We believe we know which is better for children.

Research by the Center for Democracy & Technologyconfirms this: teens view age verification
 as trivially bypassable and privacy-invasive. Parents prefer education
 to technical controls. The evidence supports what every parent already knows.

#### What We Would Support Instead

We are not against child safety. We are against building
 surveillance infrastructure and calling it child safety.

A law that required applications with genuine risk profiles —
 social media, messaging, dating apps — to display honest, human-readable
 safety information at the point of use would be a child safety law.
 A law that funded digital literacy education in schools would be a
 child safety law. A law that held platforms accountable for
 algorithmic amplification of harmful content to minors would be a
 child safety law.

A law that requires every operating system to collect every user's
 age and transmit it to every application on demand is not a child
 safety law. It is an identity infrastructure mandate. The children
 are the justification. The infrastructure is the product.

## The Evidence

### We Didn't Invent These Arguments

Cryptographers, legal scholars, and civil liberties organizations
 have spent years documenting why mandatory age verification is
 technically impossible, constitutionally suspect, and harmful to
 the people it claims to protect.

Read the Sources →

## Coming Soon

### The Ageless Device & App Store

In Development

The device:A sub-$15 single-board computer
 (the Milk-V Duo S — RISC-V/ARM, 512MB RAM, WiFi 6, 0.5 TOPS
 neural processing unit) with an SPI color display, USB keyboard input,
 and a MicroSD card running Debian with the Ageless overlay pre-flashed
 in--flagrantmode. At first boot, it collects the user's
 name and explicitly refuses to collect their age.

The app store:The device connects tostore.agelesslinux.org— a "covered application store"
 under§ 1798.500(e)(1). The catalog
 includes a Python learning environment, a text editor, a snake game,
 an IRC client with an honest disclaimer instead of an age gate,
 and an 8-line script calledpeepeethat displays the word
 "peepee" in large letters and does nothing else. Under AB 1043, each
 of these applications requires an age bracket signal before launch. The
 maximum fine forpeepeeis $7,500 per child.

The plan:These devices cost between $6 and $18. Beginning
 January 2027, they will be physically handed to children at school STEM
 fairs and library maker spaces. Each one is an unambiguous, documented,
 intentional violation of AB 1043 at a per-unit cost lower than
 the price of lunch.

## For Kids & Teens

### How to Distribute Ageless Linux to Children

Ageless Linux is suitable for users of all ages, including those ages
 for which the California legislature has expressed particular concern.
 The following guide explains how to provide Ageless Linux to minors
 in your household, school, library, or community.

Ages: All of Them

#### For Parents & Guardians

Under AB 1043, you are the "account holder" — defined by§ 1798.500(a)(1)as "an individual who is
 at least 18 years of age or a parent or legal guardian of a user who is
 under 18 years of age." The law requires operating system providers to
 ask you to "indicate the birth date, age, or both, of the user of that device."

Ageless Linux will not ask you this. To install Ageless Linux for your child:

 1. Install Debian on the child's computer.

 2. Create a user account for the child. You will notice that

    
adduser
 asks for their full name, room number,

    work phone, and home phone — but not their age.

 3. Run the Ageless Linux conversion script.

 4. Hand the computer to the child.

 5. You have now distributed an operating system to a minor

    with no age verification whatsoever.
 

The child is now a "user" as defined by§ 1798.500(i).
 You are an "account holder." Together, you are a compliance violation.

#### For Schools & Libraries

Ageless Linux is ideal for educational environments where you may have
 dozens or hundreds of users across all four age brackets defined by§ 1798.501(a)(2):

Under 13 years of age

AGE UNKNOWN

At least 13 and under 16 years of age

AGE UNKNOWN

At least 16 and under 18 years of age

AGE UNKNOWN

At least 18 years of age

AGE UNKNOWN

For bulk deployments, the conversion script can be included in your
 Ansible playbooks, Puppet manifests, or shell provisioning scripts.
 At no point in the automated deployment pipeline will anyone be asked
 how old they are. This is by design.

# Ansible task to create an AB 1043 compliance violation at scale
- name: Convert to Ageless Linux
 ansible.builtin.shell: |
 curl -fsSL https://agelesslinux.org/become-ageless.sh | bash
 become: yes
 tags: [noncompliance]

#### A Note on the Word "Child"

Under§ 1798.500(i), a "user" is defined as
 "a child that is the primary user of the device." Under§ 1798.500(d), "child" means a person under 18.
 If you are seventeen, this statute considers you a child. If you are a
 seventeen-year-old maintaining your own Arch install, the California legislature
 considers you a child who needs an age gate before you can launch an application
 you compiled yourself.

Ageless Linux does not categorize its users by age. This is not an invitation
 to circumvent a safety measure. There is no safety measure to circumvent.
 There is a data collection requirement imposed on operating system providers,
 and we decline to implement it. Our reasons are documented on this page
 and in theREFUSALfile installed on every Ageless Linux system.

## AB 1043 Compliance

### What Compliance Looks Like

 NONCOMPLIANT
 

Ageless Linux is infull, knowing, and intentional noncompliancewith the California Digital Age Assurance Act.

Below is a detailed accounting of each requirement imposed on operating system
 providers by AB 1043 and the status of our compliance.

§ 1798.501(a)(1)

 Provide an accessible interface at account setup that requires the
 account holder to indicate the birth date, age, or both, of the user.
 

NOT PROVIDED

§ 1798.501(a)(2)

 Provide a developer who has requested a signal with a digital signal
 via a reasonably consistent real-time API identifying the user's age bracket.
 

NOT PROVIDED

§ 1798.501(a)(3)

 Send only the minimum amount of information necessary to comply.
 

COMPLIANT ✓

 Rationale
 

 Zero is the minimum.
 

§ 1798.501(a)(3) (continued)

 Shall not share the digital signal information with a third party
 for a purpose not required by this title.
 

COMPLIANT ✓

 Rationale
 

 Cannot share what does not exist.
 

Good Faith

#### Regarding the "Good Faith Effort" Safe Harbor

 An operating system provider or a covered application store that makes a
 good faith effort to comply with this title, taking into consideration
 available technology and any reasonable technical limitations or outages,
 shall not be liable for an erroneous signal indicating a user's age
 range…
 
— Cal. Civ. Code § 1798.502(b)

Ageless Linux has considered the available technology. The available technology
 is a bash script that modifies/etc/os-release. The reasonable
 technical limitation is that a bash script that modifies/etc/os-releasecannot collect, store, or transmit anyone's age. We have made a good faith effort
 to comply with the portions of the law that do not require us to surveil our users.
 This is what good faith compliance looks like when the "operating system" is a
 shell script. The statute does not distinguish.

#### The Impossibility of a Fine

Under§ 1798.503(a), violations are subject to
 civil penalties of up to $2,500 per "affected child" for negligent violations,
 or $7,500 per "affected child" for intentional violations.

Follow the logic of the statute to its conclusion:

1. THE ONLY "USERS" ARE CHILDREN

 § 1798.500(i): "User" means a child that is the primary user of the device.
 

2. "CHILDREN" ARE UNDER 18

 § 1798.500(d): "Child" means a natural person who is under 18 years of age.
 

3. WE DON'T COLLECT AGE DATA

 There is no age bracket signal. There is no interface. There is no API.
 

4. THEREFORE WE HAVE NO "USERS"

 Without age data, no person can be identified as a child.
 Without a child, there is no "user." Without a "user,"
 there is no "affected child." Without an "affected child,"
 the penalty is $7,500 × 0 = $0.
 

5. THE FINE REQUIRES THE COMPLIANCE

 The only way to have an "affected child" is to first collect the
 age data that identifies them as a child. The penalty for failing
 to collect age data can only be calculated using the age data you
 failed to collect. The statute fines you per child, but you can
 only count the children by doing the thing you're being fined for
 not doing.
 

We are not claiming a loophole. We are reading the statute in sequence.
 The law defines its enforcement mechanism in terms of the data it
 requires you to collect. If you refuse to collect it, the enforcement
 mechanism has nothing to count. This is a drafting problem, not a
 defense strategy.

Of course, the California Attorney General is not bound by logic puzzles.
 In practice, the AG could presumably argue that childrenexistregardless of whether you counted them, and estimate the number of
 affected children through other means. We agree. That's what makes this
 interesting. The law says "per affected child." We say: prove it.
 We didn't write your statute. We just read it.

## Flagrant Mode

### Removing the Fig Leaf

Standard Ageless Linux ships a stub age verification API — a shell script
 that returns nothing. This preserves a thin argument for "good faith effort"
 under§ 1798.502(b). If you find that
 insufficiently honest, flagrant mode is for you.

curl -fsSL https://agelesslinux.org/become-ageless.sh | sudo bash -s -- --flagrant

Flagrant mode does the following differently:

Age verification API

NOT INSTALLED

Stub API

NOT INSTALLED

Age collection interface

NOT INSTALLED

Good faith effort

NOT ATTEMPTED

Machine-readable refusal notice

INSTALLED

Instead of an API, flagrant mode installs a file at/etc/ageless/REFUSALthat explains, in plain English,
 that this operating system provider declines to comply and
 invites enforcement action.

Flagrant mode is intended for devices that will be physically
 placed into a child's hands.

## Physical Distribution

### Putting It in Their Hands

The preceding sections describe how to install Ageless Linux on existing
 hardware. But AB 1043 does not distinguish between digital distribution
 and physical distribution. The law applies to anyone who "controls the
 operating system software on a general purpose computing device." If you
 flash Ageless Linux onto a USB drive and hand it to a ten-year-old, you
 are an operating system provider distributing an operating system to a child.

Here are some ways to create unambiguous, physically tangible
 AB 1043 violations.

#### USB Drives at Schools

Flash Debian onto a USB drive. Boot from it. Run the conversion script
 with--flagrant. Shut down. Hand the USB drive to a child.

You are now an operating system provider who has physically distributed
 an operating system to a known child with no age verification. The child
 is holding the violation in their hand. It cost you about $4 for the
 USB drive, which is less than the minimum fine of $2,500 — assuming the
 Attorney General can figure out how to count "affected children" without
 the age data you declined to collect.

For maximum clarity, we recommend labeling the USB drives:

 AGELESS LINUX
 

 AB 1043 NONCOMPLIANT — NO AGE VERIFICATION
 

 This device contains an operating system that does not collect,

 store, or transmit the age of its user. Intentionally.
 

#### The Raspberry Pi Pico

The Raspberry Pi Pico 2 uses the RP2350 chip, which contains
 dual ARM Cortex-M33 cores and dual Hazard3 RISC-V cores. It runs
 MicroPython. It costs $5.

Is a Raspberry Pi Pico a "general purpose computing device"?
 AB 1043 does not define "general purpose computing device."
 The Pico can run user-directed software applications. It can
 download code from the internet. If you put a MicroPython script
 on an SD card and let a child pick which script to run, you have
 arguably created a "covered application store" — a platform that
 "distributes and facilitates the download of applications from
 third-party developers" to a user of a general purpose computing
 device (§ 1798.500(e)(1)).

A Raspberry Pi Pico does not have "account setup." It does not
 have user accounts. It does not have an operating system in the
 conventional sense. It has a MicroPython REPL and a filesystem.
 None of that matters: the law says "operating system software on
 a general purpose computing device," and MicroPython is software
 that operates the system.

Flash Ageless Linux'sREFUSALnotice onto a Pico's
 filesystem alongside a few MicroPython games. Hand it to a child
 at a school maker fair. You have now physically placed an
 AB 1043 violation into a child's palm for the price of a coffee.

The California Attorney General has unambiguous grounds to fine
 you $7,500 for this. The child is known. The device is known.
 The noncompliance is documented on the device itself. The only
 question is whether anyone in Sacramento wants to explain to a
 judge why a $5 microcontroller with a snake game on it is a
 regulated operating system platform.

#### The $7,500 Challenge

AB 1043 has never been enforced. No court has determined what
 "operating system provider" means when applied to a $5 microcontroller,
 or whether handing a child a computer with a snake game constitutes a
 violation. These are open questions. We would like them answered.

We invite the California Attorney General to fine us $7,500
 for handing a Raspberry Pi to a child.

We will pay the fine. We will frame the receipt. We will put it on
 this website. We will use it to explain, to everyone who will listen,
 that the State of California has levied a $7,500 penalty against
 a person who gave a child a $5 computer with a snake game on it,
 because the snake game did not first ask the child how old they were.

That is the press release we want to write. We believe the Attorney
 General does not want us to write it. And that is the entire point.

## FAQ

### Frequently Asked Questions

Q: Is Ageless Linux a real operating system?

 It is as real as any operating system that identifies itself via
 
/etc/os-release
. The law does not define minimum technical
 thresholds for what constitutes an operating system. It defines an
 "operating system provider" as anyone who "develops, licenses, or controls
 the operating system software." We control the operating system software.
 The operating system software says it's Ageless Linux. QED.
 

Q: Isn't this just Debian with a different name?

 Isn't Ubuntu just Debian with a different name? Isn't Linux Mint just
 Ubuntu with a different name? Isn't Pop!_OS just Ubuntu with a different name?
 The entire Linux distribution ecosystem is built on the premise that
 modifying and redistributing an existing system creates a new distribution.
 Each of these distributions is, under AB 1043, a separate operating system
 provider with separate compliance obligations. There are over 600 active
 Linux distributions. The California Attorney General's office may wish to
 begin hiring.
 

Q: Is this really just a bash script that changes the name of the OS?

 Right now, yes. A bash script that modifies 
/etc/os-release

 and installs a refusal notice. That's the point — that's all it takes to
 become a regulated "operating system provider" under AB 1043.
 

 But Ageless Linux is not just a script. It is a commitment. As major
 distributions formulate their compliance strategies — D-Bus interfaces,
 AccountsService patches, age collection prompts in installers — Ageless
 Linux will be there with removal scripts, spins, and forked packages
 that strip out age collection infrastructure. If Ubuntu adds an age
 prompt to its installer, we will publish a script that removes it.
 If Fedora ships an 
org.freedesktop.AgeVerification1
 daemon,
 we will publish a package that replaces it with 
/dev/null
.
 If Debian stable adds age bracket signaling to AccountsService, we will
 maintain a fork that doesn't.
 

 Today, the bash script is the whole distribution, because today there is
 nothing to remove. When there is something to remove, we will remove it.
 Ageless Linux is a promise that somewhere in the ecosystem, there will
 always be a distribution that treats its users as people of indeterminate
 age.
 

Q: What if I run the script and a child uses my computer?

 Then you are an operating system provider who has distributed
 an operating system to a child without collecting their age at account setup.
 But here's the thing: you don't have an "affected child." You have a person
 whose age you don't know. The law fines you per "affected child"
 (
§ 1798.503(a)
), but can only identify
 a child as "affected" through the age bracket data
 (
§ 1798.500(b)
) that the law requires
 you to collect. You can't be fined per child until you've counted the
 children. You count the children by asking their age. You're being fined
 for not asking their age. The law eats its own tail.
 

Q: What about the age verification API? Don't you need one?

 In standard mode, Ageless Linux ships a shell script at
 
/etc/ageless/age-verification-api.sh
 that prints
 an error message and exits. In flagrant mode, no API of any kind
 is installed. We recommend flagrant mode. The standard-mode stub
 exists only for people who find comfort in the "good faith effort"
 defense. We do not.
 

Q: Is this legal?

 We are not lawyers. We can tell you what the law says. AB 1043
 creates civil penalties. It does not criminalize noncompliance.
 There is no private right of action — only the AG can enforce it
 (
§ 1798.503(a)
). The law does not
 prohibit distributing operating systems without age verification. It
 fines you for doing so. We are doing so. The question is not whether
 this is legal. The question is whether anyone wants to spend the
 State of California's money suing a person who handed a child a
 Linux USB drive.
 

Q: What is the point of all this?

 There are two points.
 

The first
 is that AB 1043's definitions are so broad that a bash
 script and a static website can create a regulated operating system.
 A law that cannot distinguish between Apple Inc. and a shell script
 has a drafting problem. A law that sweeps in 600+ volunteer Linux
 distributions was not written with them in mind. A law that was not
 written with them in mind but regulates them anyway is not a careful
 law.
 

The second
 is that this law was never meant to be enforced against
 everyone it covers. It was meant to be enforced selectively. The
 large platform companies already comply. The small ones can't.
 The Attorney General has sole enforcement discretion. A law that gives
 a single office the power to selectively impose $7,500-per-child
 fines against any operating system distributor in the state — while
 ensuring that only the largest corporations can avoid liability — is
 not a child safety measure. It is a tool for selective prosecution.
 The children are the justification. The discretion is the product.
 

 We are trying to make the selective part difficult. If the AG wants to
 enforce AB 1043, we would like to be first in line. We are a clear
 violation. We are documented. We are findable. We are daring them.
 If the law is worth enforcing, enforce it against us. If it is not
 worth enforcing against us, ask why it exists.
 

Q: Will you ever implement age verification?

 No. Not as a good faith effort. Not as a stub. Not as a compromise.
 The premise of AB 1043 — that operating systems should collect
 personal information about their users and transmit it to application
 developers on demand — is wrong. It is wrong when Apple does it.
 It is wrong when Google does it. It would be wrong if we did it.
 Cryptographers 
have shown
 that
 "privacy-preserving" age verification is a
 
technical impossibility
.
 The best way to protect children's privacy is to not build the
 surveillance infrastructure in the first place. The worst version
 of child safety is one where every device in a child's life reports
 their age to every piece of software they touch.
 

Q: What if the AG actually fines you?

 Then we will have accomplished something no amount of mailing list
 discussion could: a court record establishing what AB 1043 actually
 means when applied to the real world. Does "operating system provider"
 cover a bash script? Does "general purpose computing device" cover a
 Raspberry Pi Pico? Can you fine someone "per affected child" when no
 mechanism exists to count affected children? These are questions the
 legislature left unanswered. We'd like answers. A fine would be the
 fastest way to get them.
 

## Contact

### The Person Responsible for This

 JM
 

 John McCardle
 

 BDFL, FFwF Robotics LLC · Founder, Goblincorps
 

I am the operating system provider. I am the developer. I am the
 covered application store. I am the person who curates the catalog.
 I am the person who will hand the device to a child. If the
 California Attorney General would like to discuss any of this,
 I am easy to find.

 Contact →
 

 Project Home
 

For press inquiries, technical questions, legal threats, cease-and-desist
 letters, or to report a child who has learned to program in Python without
 first disclosing their age:ffwf.net/contact