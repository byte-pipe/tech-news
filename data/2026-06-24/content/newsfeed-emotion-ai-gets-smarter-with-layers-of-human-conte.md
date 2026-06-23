---
title: Emotion AI Gets Smarter With Layers of Human Context - IEEE Spectrum
url: https://spectrum.ieee.org/emotion-ai-context
site_name: newsfeed
content_file: newsfeed-emotion-ai-gets-smarter-with-layers-of-human-conte
fetched_at: '2026-06-24T01:02:00.807090'
original_url: https://spectrum.ieee.org/emotion-ai-context
date: '2026-06-23'
published_date: '2026-06-23T12:00:01+00:00'
description: Emotion AI is evolving beyond simple emotion detection. Neurologyca explains how context-aware systems interpret human behavior and intent.
tags:
- ieee-spectrum
- emotions
- affective-computing
- facial-expressions
---

AI
 
Feature
 

# AI Is Learning to Read the Room

 
 

## Emotion-sensing AI systems are becoming aware of context

 
 
 
 
 
Marc Fernandez
 
 
2h
 
10 min read
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

 Josie Norton
 
 

Imagine sitting down atyour desk and logging in for a performance review, with an AI system analyzing the conversation. You’ve been working long hours, balancing deadlines, and your manager asks how you’re doing. You say you’re fine, and maybe even smile, but there’s a hint of hesitation and your voice wavers. As you shift your posture, your shoulders slump.

These are subtle cues that to the human eye might hint at underlying stress. But to an AI model that’s been trained only to categorize emotions as “happy” or “sad,” such nuances are likely lost. It logs the words and a smile and moves on—and unless your human manager intervenes, the fact that you’re tired, unfocused, and maybe a couple of days from burnout never enters the equation.

“Emotion AI,” which estimates how people feel based on facial expressions, voice tone, and behavior, seems to be suddenly everywhere; it’s being used in employee well-being and recruitment interviews, education platforms, and driver-monitoring systems. Technology call-center platforms such asNiCEandGenesysuse AI to detect when a customer sounds frustrated and prompt agents in real time to slow down or respond with more empathy. Giant companies likeMetaand startups such asHume AIare developing more-expressive voice AI systems that can detect emotional cues in the person they’re “talking” to and adjust how they communicate.

What’s more, hundreds of companies already offer virtual AI companionship apps, a fast-growing market that may be worth anestimated US $555 billionby 2035—and robot buddies have also entered the picture. Intuition Robotics’sElliQ, for example, is a small device vaguely resembling a white desk lamp that’s now being used to engage older adults in conversation in hopes of reducing loneliness.

But while the field of emotion AI is advancing at a rapid clip, most existing systems are focused on detecting a limited number of signals to label one specific emotion at a time—which is insufficient if you’re trying to understand the human condition. In the real world, human signals and emotions are contextual, overlapping, and constantly changing. A laugh can signal joy, nervousness, or both; a raised voice might signal enthusiasm just as easily as frustration. To make the job of emotion detection even more difficult, reactions differ greatly from one individual to the next, depending on demographics, cultural background, and countless other variables.

In other words, there’s a gap between what we’re expecting AI to pick up on and what AI can actually deliver. That’s the gap a new field of research—what we call human-context AI—is working to close. Instead of looking at just one input and labeling it, human-context AI increasingly has the capacity to take stock of an individual’s personality and character, and to track emotions in real time while combiningmultiple inputs, including facial dynamics, voice, tone, language, and behavior. Crucially, responses are also evaluated in the context of a specific environment, such as a performance review or professional coaching session. The result? Computers are learning to read the scene, rather than just the screen.

## The Origins of Emotion AI

The story of emotion-sensing AI began almost three decades ago in theMIT Media Lab, where the American electrical engineer and computer scientistRosalind Picardcoined the term “affective computing.” Her work introduced the radical idea that computers could be taught to recognize and respond to human emotions.

Picard’searly experimentsfocused on single modalities: facial expressions, tone of voice, and physiological signals, such as skin conductance orheart rate. The goal was to give machines a window into human feeling, helping them become more empathetic. It was an exciting vision, but back then the science and hardware weren’t ready. Computing power was limited, sensors were crude, and datasets were narrow and biased.

Josie Norton

Over the next decades, researchers and companies got better at measuring the many ways in which humans express themselves. In the 2010s,sentiment analysis—the processing of large volumes of text to suss out emotional undertones—began to reach the mainstream. At the same time, marketing firms, including my company,Neurologyca, began using video andwebcamsto measure and catalogue customer reactions. Biometric devices and activity trackers, such as Fitbits and Apple watches, also became ubiquitous, generating new streams of data about people’s sleep, step counts, stress levels, and more.

Unsurprisingly, scientists soon confirmed that larger volumes of personalized data led to greater accuracy in reading human emotions. In 2019, researchers at Cornell demonstrated thatcombining multiple types of signalsimproves emotion sensing. Their system joined physiological data, such as brain activity measured byelectroencephalography(EEG) and heart rate, with visual cues like facial expression, outperforming systems that relied on just one input. Around the same time, Picard and her team at MIT found that humanoid robotstrained on data unique to a specific personwere substantially better at reading that person’s reactions and feelings than robots acting without personalized data.

More recent studies align with these findings. In 2024,scientists in South Koreashowed that fusing physiological, environmental, and personal data to recognize emotion resulted in a 32 percent error reduction.Another paper, published in 2025, demonstrated that user-specific information significantly enhancesemotion recognitionperformance.

Today, our devices know who we are; our habits and tendencies, likes and dislikes. They’ve also gotten smaller and more efficient. Tiny, low-power cameras and microphones embedded in phones, laptops, and virtual-reality and augmented-reality devices can detect dozens of human signals simultaneously, from eye movements and micro-expressions to breathing rhythms, voice modulation, and posture. Advances in computing have also made it possible to integrate audio, video, biometric, and text data, often without even transmitting raw data to the cloud. And researchers atStanford,Cambridge and MIT, andKyoto University, in Japan, as well asthe Software College of Northeastern Universityin Shenyang, China, are exploring how fusing such inputs can refine the sensitivity and accuracy of human-machine interactions.

And yet, despite so many breakthroughs, machines still can’t reliably interpret emotion or even physical stress. Just last year, a survey published in theJournal of Psychopathology and Clinical Sciencerevealed that stress scores onsmartwatchesrarely, if ever, matched the level of stress that users were experiencing. In fact, a quarter of those surveyed reported feeling the direct opposite of what their smartwatches were reporting.

Why the disconnect? We’ve gotten very good at capturing signals, but not at interpreting them. Afitness trackermight infer from your heart rate that you’re stressed and recommend easing off training, but it doesn’t know if your increased heart rate is due to excitement, tiredness, or an extra cup of coffee. Gauging emotions in real-world settings is even more difficult. To solve this complex problem, machines need context.

## From Neuromarketing to Emotion-Sensing AI

My company, Neurologyca, was founded in Spain in 2015, and started out in neuromarketing. Working with major European brands and conglomerates, our cofounder, Juan Graña, had realized that companies lacked solid data on consumers. At the time, most customer feedback came through surveys, which posed questions such as, “On a scale of 1 to 10, how joyful does this car advertisement make you feel?” or “Which emoji best describes your mood?” Naturally, these overly simplistic tools led to high levels of self-reporting bias, as people often misjudge or misstate their own reactions.

To get around this problem, Neurologyca set up labs, usingneuroscienceandcognitive scienceto more accurately capture human responses to products, logos, advertisements, and experiences. In addition to using biometric tools such as heart monitors, eye trackers, and EEG, we recorded millions of video frames of human reactions, logging each specific context and the resulting facial and bodily movements. To do this, we mapped over 790 points of reference, including corners of the mouth, size of the eyes and pupils, blink rate, and angling of the head. All of this data was collected and stored anonymously under strict European privacy standards.

Next, we paired this information with findings from decades of neuroscience and behavioral science studies on howbiometrics, speech patterns, and human movement are related to emotion—research we continue to gather from academic institutions across Europe. We also created a database of situational contexts—for example, “watching a dog food commercial” or “hearing a new song”—and the human feelings they engendered.

In our work with companies, not only did this approach allow us to recognize nuanced emotions, it also let us identify which reactions indicated positive or negative outcomes. Take, for example, the context of horror-film trailers: Our research helped us figure out that the most successful elicit a very specific mix of emotions, namely a little bit of fear, a little bit of anxiety, but also some joy. With this knowledge, we could quickly rate viewer reactions to help a film company figure out how to tweak its trailer for the desired impact.

Neurologyca

Within a few years, we discovered that a model trained on our database could accurately evaluate emotion using just a webcam. We stopped needing to host focus groups in rooms full of equipment. Instead, we were able to do such things as sending out a new perfume sample to paid participants around the world along with a link. When people opened the link, it turned on their cameras, allowing us to record their faces as they sniffed the perfume for the first time. Suddenly, we had expanded our reach: Rather than using small focus groups in one or two countries, we could quickly assess 1,000 people across the planet, comparing how someone in Japan, India, or Germany might feel about a certain product.

About four years ago, as AI was becoming pervasive, we realized that our models had applications well beyond neuromarketing. Importantly, these models are grounded in directly observed human behavior rather than inferred patterns or loosely labeled open datasets. Looking beyond brands and companies, we established that our model could be integrated into AI systems to help them understand human emotion at a much more granular level. In other words, we could provide a layer of context.

## For Empathetic AI, Context Is Key

When we talk about “a layer of context,” we mean three different types of context. The first is situational or environmental context; for example, a performance review, atelemedicinesession, or a horror-film viewing. The second is personal context, which includes an individual’s specific history, goals, and baseline state. The third is behavioral context, which covers the individual’s reaction over the course of the event or interaction by evaluating real-time changes in attention, confidence, engagement, and cognitive load.

Most systems today focus on only situational context, although some are starting to include personal context. Very few include behavioral context or combine all three in a meaningful way. What we’ve built at Neurologyca is a logic layer that fuses the three and translates them into structured, machine-readable information that allows AI systems and agents to respond more effectively. Our technology is being used to enhance systems in development, as well as some that have already been deployed, including driver-safety apps likeNetradyne, home assistants likeAmazon Alexa, and health-care AI platforms likeSully.ai.

It works as follows: Situational context is determined by the platform or application, be it a professional coaching session, a meditation app, or a driver’s safety monitor. Personal context already lives within each respective platform—or if not, it can be created through sharing of personal data or monitoring via camera. (Most wellness and professional-development apps, for example, contain each user’s profile, history, and prior sessions.) Last but not least, behavioral context is collected and analyzed in real time using our models. In the end, our logic layer fuses these three streams of information.

Our system doesn’t assign fixed weights to the three contexts. Instead, it provides a continuous calibration, with the balance shifting depending on the specific situation. For example, a pause in speech might signal uncertainty in a performance review, but something entirely different in a relaxation setting. If signals are ambiguous or overlapping, our system reflects that uncertainty through lower confidence scores rather than forcing a definitive interpretation.

What’s more, our system can work without ever sending raw data to the cloud, thereby easing privacy concerns. In many cases, video, audio, and biometric signals never leave the device. Instead, our lightweight models extract information locally and share only what’s necessary. Cloud systems, meanwhile, are used for training, pattern analysis, and model improvement. The result is a hybrid architecture: edge-based processing for speed and privacy combined with cloud-based learning for continuous improvement.

The result? By incorporating context, AI systems are beginning to interpret aspects of the human state as interactions unfold, dynamically adapting to emotions rather than reacting after the fact. The range of potential applications is broad and still evolving. Picture a professional-development platform that uses a human avatar to perform a mock interview and then provide feedback and tips on how to appear more confident, likeable, and well-informed. Or a meditation app that knows exactly how well you slept and how anxious you’re feeling, and can recommend an appropriate breathing meditation. Or a humanoid robot teacher that can tell when a student is confused or bored and step in to get them back on track.

## Avoiding Potential Dangers on the Road Ahead

There have long been debates about the ethics of emotion-sensing AI. Some critics question whether systems should attempt to infer human feelings from external signals at all. They argue that reducing people to measurable outputs risks oversimplifying human experience while opening the door to manipulation, surveillance, and unfair judgments in workplaces, schools, and public spaces.

We take those risks extremely seriously. In fact, our technology aims to reduce the dangers of oversimplifying human emotion. Human-context AI is not based on the assumption that a machine can definitively know what someone is feeling. Rather, it is an attempt to move beyond simplistic labels by incorporating situational, personal, and behavioral context, while explicitly representing uncertainty when signals are ambiguous or incomplete.

That said, ethical concerns regarding implementation are real and have shaped the kinds of projects we pursue. We would never, for example, accept military engagements to help with interrogations. Not only for ethical reasons: Emotion AI cannot reliably detect deception, and claiming otherwise would be overstating what the technology can actually do.And while our technology can be used to gauge crowd behavior and predict things like when afootballstadium is at risk of becoming destructively rowdy, we don’t want our technology deployed for surveillance. In short, we believe that using our logic layer on anyone who hasn’t opted in would be intrusive and ethically problematic.

In Europe, our systems are designed to comply with the EU AI Act’s restrictions on emotion recognition in workplaces and schools; as we expand into theUnited States, we apply jurisdiction-specific guidelines while maintaining the same core ethical commitments.

We also don’t advise companies to become overly reliant on our technology. Hiring and firing decisions should not be based on our outputs alone. Instead, our logic layer is designed to support human understanding and surface emotions that might otherwise go unnoticed.

Let’s return to the scenario of the performance review. Never mind basic AI—all humans, and even great managers, miss things during conversations. There’s a lot happening at once, as people process what’s being said, how to respond, and the greater context of the situation. These days, many exchanges also occur virtually or via video, adding more distractions while shared context is stripped away.

While we would never claim that our models understand humans better than their fellow humans, we believe we can offer an added layer to help managers capture and interpret behavioral signals that might otherwise get lost, providing greater visibility into how a conversation is unfolding.

Our model can track patterns moment to moment, picking up, for example, a shift in engagement, an instance when something didn’t land, or a change in how someone is behaving. The model won’t tell the manager what these moments mean or what to do about them; it simply makes them easier to see and follow up.

Human-context AI is at an early stage. The use cases, the adoption patterns, and the actual impact are all still evolving. At the same time, emotion-sensing systems are quickly being incorporated into real products and platforms. And without context—without knowingwhypeople feel the way they do—AI risks misunderstanding us in critical moments.

From Your Site Articles
 
* Visual Language Models Train Robots to Read Human Emotions ›
* Building an AI That Feels ›
* The Rise and Fall of Inflection’s Emotionally Intelligent Chatbot ›
Related Articles Around the Web
 
* Emotion AI, explained | MIT Sloan ›
 
 
 
 
emotions
 
affective computing
 
facial expressions
 
companion robots
 
multimodal ai
 
Machine Learning