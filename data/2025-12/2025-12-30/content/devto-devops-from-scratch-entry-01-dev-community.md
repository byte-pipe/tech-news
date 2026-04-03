---
title: 'DevOps From Scratch: Entry #01 - DEV Community'
url: https://dev.to/maame-codes/devops-from-scratch-entry-01-47pm
site_name: devto
fetched_at: '2025-12-30T11:07:07.793289'
original_url: https://dev.to/maame-codes/devops-from-scratch-entry-01-47pm
author: Maame Afua A. P. Fordjour
date: '2025-12-26'
description: 'Linux Foundation: The "Cockpit" of the Cloud I have used windows all my life, my very... Tagged with devops, linux, learning.'
tags: '#devops, #linux, #learning'
---

## Linux Foundation: The "Cockpit" of the Cloud

I have used windows all my life, my very first computer, was a cream hp with the big 'head'😂. (Will try to find a picture of it and attach it somewhere in this blog.)

👆Ref: Got this picture from a random reddit post on google. It did look similar to this, but it was an HP brand.

At that age, carrying that computer would be a death wish! It was extremely heavy that, it had been at one exact spot in my family house till it stopped working. I started using windows XP, and from then, till this very moment, I have only been a loyal windows user since I ever started using computers. (Never even used the macOS). That's just by the way. This very day, dated 26th, December 2025(Merry Christmas if you read this during Christmas time🎅🎄), is the first time I am learning about the Linux OS, mostly the fundamentals.

If Python is the language we use to build apps, Linux is the language we use to build the world those apps live in. Almost every Docker container, AWS instance, and Kubernetes node runs on Linux.

If you're still clicking icons to move files, you're a passenger. Today, we become the pilot.

Before we get started, I will put down two links which entails most of the things you need to know about Linux.

* [(https://training.linuxfoundation.org/training/introduction-to-linux/)]. This is a60 hoursself paced course that talks about almost everything you need to know about linux. I will be going with this self paced course because of the structure(More beginner friendly in my opinion)
* [(https://www.youtube.com/watch?v=sWbUDq4S6Y8)]. And this is the full course from freecodecamp that is about7 hourslong.

## The Linux File Hierarchy System (FHS)

In Linux, everything is a file. Even your hard drive and your keyboard are represented as files. But unlike Windows, Linux follows a strict "everything has a place" rule called theFilesystem Hierarchy Standard.

📌/bin & /usr/bin: Where the "executable" tools live (like ls, cd, and python).

📌/etc: This is the most important folder for DevOps. It contains configuration files. If you need to change how a web server behaves, you'll find the config here.

📌/var/log: Where the system "screams" when something goes wrong. If your app crashes, your first move is always cd /var/log.

📌/tmp: Temporary files that get wiped on reboot.

Deep dive👉https://www.geeksforgeeks.org/linux-unix/linux-file-hierarchy-structure/]

## Redirection & Pipes (The "Lego" Logic)

The core philosophy of Linux is: "Write programs that do one thing well and work together." We connect them using Pipes (|).

📌>: Redirects output to a file (overwrites it).

📌>>: Appends output to the end of a file.

📌|(The Pipe): Takes the output of one command and shoves it into the next.

If you struggle with ADHD, or any sort of neurodivergence disorder like myself, I have created a webpage called 'FLASHY'. It is a flashcard style of learning to help us remember what we will be learning in this series (Will be updating the webpage to handle the rest of the things we will study along the way). You can try it out here 👉 [https://flashy-memorizer.vercel.app/]. This one entails some of the things learnt from the introduction to Linux course I included in the beginning.

🛣️ The Roadmap Continues...I’m taking the technical "meat" from the Linux Foundation and breaking it down into my diary entries so they actually stick.

Entry #02 will be: Linux Philosophy and Concepts.🚀

(We’ll be looking at why Linux works the way it does—like why everything is a file and why "Small is Beautiful" in software design.) Happy Learning :)

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
