---
title: Activity-Focused Design | IxDF
url: https://ixdf.org/literature/article/activity-focused-design
site_name: tldr
content_file: tldr-activity-focused-design-ixdf
fetched_at: '2026-05-22T06:00:34.069495'
original_url: https://ixdf.org/literature/article/activity-focused-design
date: '2026-05-22'
description: Task Analysis is one of many activity-focused approaches to UX design, that centers on the actions people need or want to take in order to reach a goal.
tags:
- tldr
---

# Activity-Focused Design

byChristian Briggs•1 week ago• 10 min read

 644 Shares
 

Share this Article

Cite this Article

Save

 Cite This article
 

Activity-focused design centers on the actions people need or want to take in order to reach a goal. For example, if you are designing a home lighting control app, an activity-focused approach will help you to identify and design the steps a user must take to connect their lights or switch them on and off.

There are many activity-focused approaches toUX design, includingtask analysis,jobs to be done,activity theoryandactivity-based design. Each provides a different way of looking at problems, yields different insights and may result in different design decisions, but all of them have one thing in common: The core unit of analysis isactivity— what people do and how they do it to achieve a goal.

© 
Interaction Design
 Foundation, CC BY-SA 4.0

Here we will introducetask analysis, but please remember that it is onlyoneactivity-focused approach. Please also remember that activity-focused approaches are notreplacementsfor things likehuman-centered design. Rather, they arecomplementary. For example, in the research phase of ahuman-centered design process, you might use task analysis to discover the steps a user takes to solve a problem. You might also use it later in the process to ensure that designs andprototypessupport important user activities.

Before we dive into how to do task analysis, let’s define a few terms to avoid confusion. Please note that the following are working definitions for our present context, and may have slightly different names elsewhere.

First, agoalis an end state that a person intends to achieve, such as “lightbulb is connected to the mobile app” or “light is turned on.” Anactivityis a series of tasks that a person will do to help achieve a goal, such as “connect the lightbulb to the app” and “turn on the light.” Ataskis a single unit of action or work, such as “open the app” or “click on the button with the lightbulbicon” or “plug in the lightbulb.”

When doing task analysis, there will be times where you will have to use your best judgment. For example, you will have tochoose the level of specificitythat will be most useful for your design goals. For example, “move finger” or “look at the lightbulb” might be too specific to be useful, while “use the app” or “light the room” might be too general.

You will also need to choose the types of tasks to analyze. If you aredesigning something brand-new, youmay want to avoid mentioning specificuser interfaceelementssuch as “click theonbutton” or “select the bulb from the menu.” Instead, you could write them in an interface-independent way such as “turn the lightbulb on” or “select the bulb.” This will provide more flexibility in the design phase to consider multiple ways that the interface can support the task. On the other hand, if you areanalyzing an existing app or system, youmay want to include tasks that describe the existing interfacesuch as “use thesearch boxto find the device.” There are no correct or incorrect choices here — only choices that are more or less helpful for your own design process.

## Task Analysis: The Process

There are many variations of task analysis — and you may eventually develop your own! — but the focus is always on understanding thegoala person is trying to achieve and thetasksthat will or will not help them to achieve it. Here we will walk through a basic version of task analysis that you can start using right away in your own design work.

Imagine that as in the previous section, you were asked to design an app to control lightbulbs from your mobile device.

Thefirst stepin task analysis is to determine the most importantgoalor goals of a person who uses the app. Do they want to simply turn the lights on and off? Control them automatically based on the time of day? Connect them to a motion sensor?

Thesecond stepis to determine thetasksthat a person would have to perform to reach those goals. To set the lightbulb to “on” (goal), this might include plugging in the bulb (task), turning on the mobile device’s Bluetooth (task), connecting the bulb to the app (task) and turning on the lightbulb in the app (task).

There are many ways to determine these goals and tasks, including conductingthink-aloud interviews, where a person expresses what they are thinking while working toward a goal, andcontextual inquiry, where you observe users working on something in their usual environment. If the design problem is simple and you are very short on time, you can even work toward the goal yourself and keep track of the tasks you have to do.

With your data in hand, thethird stepis to document the goals and tasks in a way that helps you and your team to identify gaps or opportunities to design improvements. This might take the form of a simpletask analysis diagram(shown below), ahierarchical task diagram,sequence diagram,flowchartor any other format that works for you and your team.

© Interaction Design Foundation, CC BY-SA 4.0

At this point you will have a pretty good understanding of the steps to consider in your app design, and anartifactthat will help you and otherstakeholdersto take thefourth and final step, which is to look for unnecessary, inefficient or counterproductive tasks that could be removed or improved in your design. If your users will be using devices that are always connected via Bluetooth, for example, the task of turning it on could be removed.

© Interaction Design Foundation, CC BY-SA 4.0

Occasionally you will find that more insights are needed and add another approach. For example, if your task analysis reveals that a certain task makes people anxious, ausersurveymight show the prevalence of the problem, andsemi-structured interviewsmight reveal theroot cause.

## Task Analysis: Strengths and Weaknesses

Every design approach has its strengths and weaknesses — where it sharpens our insights and where it may create blind spots. Here are some general thoughts about task analysis.

### Strengths

* When the success of a design solution depends on users completing a series of tasks — especially if thosetasks must be accomplished in a particular order— task analysis will help to reveal gaps and optimization opportunities.
* The focus on discrete taskstranslates quite naturally to the design of a digital experience. If your task analysis reveals that in order to turn on a lightbulb a user must locate the lightbulb’s icon, choose a brightness level and click the “on” button, then the design will be straightforward.

### Weaknesses

* Because it focuses so heavily on tasks and goals, task analysis does not automatically lead to insights aboutnon-task-relatedaspects like the emotional state of users, social pressures or norms of use. For example, a strict task analysis for the light control app may not reveal how users feel about its effect on their energy use, or if they feel awkward using a phone to turn on lights in front of their friends.
* Task analysis can be prone tobackward-looking design. For example, it could be difficult to imagine and design a new method of controlling lights if your information came from an analysis of people’s current light-controlling tasks.

## The Take Away

In activity-focused design, the core unit of analysis is activity — what people do and how they do it to achieve a goal. Task analysis is one of many activity-focused approaches. It includes four main steps:

1. Determine the goalof a person.
2. Determine the tasksthat a person would have to perform to reach those goals.
3. Documentthe goals and tasks.
4. Analyzethe goals and tasks for ways to improve outcomes.

Every design approach has strengths and weaknesses. One strength of task analysis is its ability to reveal patterns in situations where a design solution depends on the completion of tasks. Another is that its focus on tasks translates easily to the design of a user experience.

One weakness of task analysis is that it does not automatically reveal other important factors like emotional state, social pressures, norms, etc. Another weakness is that its focus on current goals and tasks can lead to backward-looking design.

## References and Where to Learn More

You can find a more detailed article on task analysis here with helpful ideas for identifying goals and tasks and ways to analyze more complex situations:How to improve your UX designs with Task Analysis

## Images

© Interaction Design Foundation, CC BY-SA 4.0

## Learn More in This Course:

AI for Designers

Closes in:

2 days

84

%

booked

View Course

## Learn Design From the Best

Get one powerful email each week, like 318,816 others.

Next email in:

5

days

16

hrs

17

mins

12

secs

 

Name
 

 Your email 

 Go
 

Please enter a valid email address.

## What You ShouldRead Next

* Read full article## 6 Insights to Achieve Agile UX ExcellenceAgile methods boost UX design teams' adaptability. The shift from traditional to agile methods occurred because the former fell short. Agile nurtures a dynamic environment where innovation thrives—it promotes early and frequent testing to minimize risks through short, iterative cycles while teams coSocial shares484Published4 days agoRead Article

* Read full article## Top Tips to Create Effective Journey MapsA low conversion rate (below 2%) usually means a website struggles to keep visitors interested. Journey mapping helps identify why visitors leave quickly and tracks every step of a user's interaction with a website. The goal is simple—to create a smooth, enjoyable journey to make users return. LearnSocial shares589Published1 week agoRead Article

* Read full article## What If Your Users Lie? How Personas Help You Get to the TruthPeople often describe what they think they want, but that doesn’t always match what will actually solve their problem. Most of the time, they’re describing symptoms, not the root cause. That’s where you come in. Your job is to dig deeper, ask better questions, and help them uncover what they reallySocial shares424Published1 week agoRead Article

* Read full article## Why User Experience?Abraham Maslow's hierarchy of needs asserts that when we fulfill unconscious goals such as food, shelter and approval, we improve our quality of life. The improvement of technology has also been driven by the fulfillment of human needs; that’s why the shift to service orientation in the digital worlSocial shares474Published1 week agoRead Article

* Read full article## The Psychology Behind Personas: Why They Work in Any Job, Any IndustryWhen you think of personas, your mind might jump to UX design or marketing. But the truth is, personas are far more versatile than most people realize. Whether you work on mobile apps, train staff, manage patients, or in human resources, personas help you make better, more human-centered decisions.Social shares493Published1 week agoRead Article

* Read full article## The Hollywood Guide to UX Personas: Storytelling That Drives Better DesignHave you ever teared up watching a Pixar film? Felt the thrill when a superhero overcame impossible odds? Cheered for a villain’s redemption? That’s the power of great storytelling—and it's exactly the emotional clarity and focus that UX designers can bring into persona creation.How do we make our pSocial shares450Published1 week agoRead Article

* Read full article## How to Elevate Your Mobile UX StrategyMobile makes up over 54% of global website traffic—a far different world from how users used to get online. Exceptional mobile user experiences are a prime necessity in our digital-first world, and the quality of a mobile user experience can mean the difference between a product that thrives and oneSocial shares451Published2 weeks agoRead Article

* Read full article## The Secret to Success? Understanding People—How to Use Personas to Get AheadWhat makes some professionals consistently stand out—regardless of their role, industry, or resources? It’s not just talent or tenacity. The real differentiator is this: they understand the people they’re trying to serve. Whether you're designing a product, launching a campaign, leading a team, or sSocial shares472Published2 weeks agoRead Article

* Read full article## Convergence – How to Be Creative Through Analytical Thinking[[video:89]]
In this video, you’ll learn the different roles that divergent and convergent thinking play in creating innovative and useful solutions. It’s the interplay of exploratory divergence and analytic convergent activities that allows us to build a map of our design space and hence identifySocial shares527Published2 weeks agoRead Article

* Read full article## The Nature of ExperienceThe four threads of experience and six processes of sense-making outlined by McCarthy and Wright in their "Technology as Experience" apply to both digital and non-digital experiences. Here we’ll learn how they can be used to design more meaningful and impactful experiences.In this short clip, HCI PrSocial shares465Published2 weeks agoRead Article

## Top Articles

* Read full article## The 5 Stages in the Design Thinking Process2k shares
* Read full article## What is Design Thinking and Why Is It So Popular?1.6k shares
* Read full article## Personas – A Simple Introduction1.6k shares
* Read full article## Bad Design vs. Good Design: 5 Examples We Can Learn From1.5k shares
* Read full article## What is Interaction Design?1.5k shares

## Top Topic Definitions

* Read full topic### Design Thinking51 articles10 videos
* Read full topic### User Experience Design157 articles8 videos
* Read full topic### Graphic Design19 articles3 videos
* Read full topic### Color Theory7 articles5 videos
* Read full topic### User Interface (UI) Design65 articles8 videos

## 39% of Today's Skills Will Change by 2030

The World Economic Forum expects 39% of today's skills to be transformed or become outdated by 2030.

The good news is that jobs in UX / UI design and AI are among the fastest-growing professions globally.

 See How Design Skills Turn Into Job Options