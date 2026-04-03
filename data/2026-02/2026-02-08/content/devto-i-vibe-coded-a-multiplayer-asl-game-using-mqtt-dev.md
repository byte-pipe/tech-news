---
title: I Vibe Coded a Multiplayer ASL Game using MQTT! 🌐 - DEV Community
url: https://dev.to/francistrdev/i-vibe-coded-a-multiplayer-asl-game-using-mqtt-480
site_name: devto
content_file: devto-i-vibe-coded-a-multiplayer-asl-game-using-mqtt-dev
fetched_at: '2026-02-08T15:31:01.014653'
original_url: https://dev.to/francistrdev/i-vibe-coded-a-multiplayer-asl-game-using-mqtt-480
author: 👾 FrancisTRDev 👾
date: '2026-02-03'
description: Last year (2 months ago), I created a game using p5.js and ml5.js that uses Machine Learning to... Tagged with mqtt, webdev, discuss, showdev.
tags: '#discuss, #mqtt, #webdev, #showdev'
---

Last year (2 months ago), I created a game usingp5.js and ml5.jsthat uses Machine Learning to detect the ASL alphabet. I made this project for my course "IoT with Machine Learning" at my University and it taught me a lot about the process and how IoT is shaping the world!

One of the things that I utilize in this project is using MQTT (Message Queuing Telemetry Transport). It is different from Web Sockets because of how it is use for IoT specifically since it is designed for constrained devices such as Arduino, which I used for this project.

But I want to use MQTT forjustthe multiplayer functionality. I had some practice with Web Sockets, but thought to myself..."How far can I go with MQTT"?

# Overview of the Project

This project is a desktop application. It is a simple game where your goal is to spell out as many words as you can in ASL. You can play either Single player or Multiplayer. It utilizes Machine Learning to perform Pose Estimation on the user's hand points usingml5.js. You can learn more about iton their documentation.

# Technologies I Used

To make the desktop application, I usedTauriwhich is framework to create your own desktop/mobile app. It is very nice since you can do Web Development stuff inside of Tauri such as React, Vue, or just Vanilla HTML, CSS, and JavaScript. For this project, I stick to Vanilla HTML, CSS, and JavaScript. I also usedp5.js and ml5.jsfor my libraries as I mentioned earlier. I also used SupaBase to store high scores of the words they accomplished.

# ASL Machine Learning Model

This rough flow diagram shows the following of the game functionality. When you do ASL, it detects your hand points and the gesture you are doing. It then feeds the data points into the Machine Learning Model and it predicts which alphabet you are gesturing in real-time. Once the game is done, it uploads your data to the database of your score and coins you have received.

The Arduino part is an extension that shows you data, such as your "Letters per second" and your username, on an LCD which is shown here:

# MQTT Multiplayer Functionality

To accomplished this, I useMosquittoas my broker. This diagram shows the flow of how the Multiplayer game works:

In short, you can create a room and it will provide you a code to share with other users to join the room. In the lobby, when everyone clicks "Ready" the game starts. Demo is shown here below:

# Challenges I Faced

There are are few big things I faced when creating this project.

### 1. MQTT setup

I had the idea of how it works, but it is hard to implement in practice since I am not really using an IoT device to communicate to the broker (Unless you count the camera as an IoT device). Since it was vibe coded, I had to take the time to understand the flow and how data is being pass/received.

### 2. Creating my own Model

I started with Image Classification. But the problem is that it captures the WHOLE image in addition to your hands. Meaning if I use the model in a different setting, it would not predict it accurately. I then learn about Hand pose in ml5.js documentation and I start building my own model. I had to create a separate vibe coded project that is design to create your own Hand pose Model.

### 3. Training problems

For context, I trained letters from A-Z ("J" and "Z" are excluded). For each letter, it captures around 2000 Post Estimation data. After training is complete, it forgets the last last two letters, which are "X" and "Y". The solution I came up with is that during data collecting, if I reach either "X" or "Y", collect more than 2000 Post Estimation data. In this case, "X" will get 4000 and "Y" gets 6000 (Just to be safe).If anyone knows why this is the case, please let me know!

# Summary

It was a fun project! I learned a lot about not only how to connect the Arduino to the web, but also how to use MQTT to the limit (to my knowledge). If you are interested more about this project, check out theGitHub Repository here!

Any questions, or comments? I would love to hear from you!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (13 comments)


For further actions, you may consider blocking this person and/orreporting abuse
