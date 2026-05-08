---
title: 'AI vs Non-AI: Building the Same Project Twice - DEV Community'
url: https://dev.to/nandofm/ai-vs-non-ai-building-the-same-project-twice-4073
site_name: devto
content_file: devto-ai-vs-non-ai-building-the-same-project-twice-dev-c
fetched_at: '2026-05-08T12:08:32.835149'
original_url: https://dev.to/nandofm/ai-vs-non-ai-building-the-same-project-twice-4073
author: Fernando Fornieles
date: '2026-05-06'
description: 'When I was implementing my weather station system, I asked myself: what if I built it again but this... Tagged with ai, softwareengineering, discuss, programming.'
tags: '#discuss, #ai, #softwareengineering, #programming'
---

When I was implementing my weather station system, I asked myself: what if I built it again but this time using AI?

The idea I had in mind was to compare the same project implemented with both approaches. Is AI development as fast as the hype claims? What about code quality? Will I face the same challenges when using AI? As a developer, will I feel better or worse?

In this article I will try to explain how was building my Weather Monitoring System again using AI and how I felt, being as honest as possible.

## Experiment Context

The Components

* Sensor Reader: A Python program that reads weather data from the sensor, displays the current readings and sends the data to the Web app
* Web App: Dashboard & API: a PHP + Symfony web application that receives the data from the weather station and display it in a dashboard.

AI SetupI didn't want to spend money using AI, so I tried the free plan ofGemini,OpenRouterand alsoOllamalocally. But with the Gemini and OpenRouter I ran out of tokens too fast and using Ollama in my own PC didn't work properly.

So, following a colleague recommendation, I ended up usingOpenCodeand its default model: Big Pickle.

I have to say that, regardless of the final result, it worked quite well.

Source CodeYou can check the source code for both approaches here:

* Sensor ReaderHorrameteoHorrameteo AI
* Horrameteo
* Horrameteo AI
* WebappHorrameteo WebHorrameteo Web AI
* Horrameteo Web
* Horrameteo Web AI

Rewrite approachIt is true that when rebuilding a project you don't have to experiment, you know exactly what you want. To compensate this advantageI triedto act as if the "handmade" projects didn't exist and also acting as a "vibe coder", that means, I only wanted it to work without writing a single line of code and without caring about how it is built.

## Time Spent

I measured the time spent by assigning 2 hours per each day I committed code.

Project

non-AI

AI

Sensor Reader

42h

14h

Webapp

28h

12h

"Wow!! Four times faster using AI!!"

But the reality isthat during the development, without AI, I had to learn Python and how the Pimoroni library works. Also, I didn't have a clear idea of how to structure the code. I refactored it several times as I learned about how to apply best programming practices in Python.

Another factor to take into account is how I used the version control system with both approaches. Using AI I made less commits than without it because:

* Without AI I commit each small step I consider ok.
* With AI I made fewer but larger commits as I waited until a complete functionality was working.

Regarding the Webapp project, I had it finished in around 16h. The rest of the time, until 28h, I was iterating to see what kind of statistical weather data I wanted to see together with current values and also how to display the information. Using AI I applied directly the solution I finally decided for the non-AI approach.

Taking this into account and the fact that, as a vibe coder, I didn't spend time reviewing the code, my "spider-sense" warns me thatmaybe the numbers are not as impressive as they seem.

## Code Quality

I have used Sonarqube to obtain some metrics about code quality like maintainability, security, reliability or code duplication. Is it better using AI or not? Let's see.

Sensor ReaderThe non-AI project had 45 maintainability issues for not following thesnake_caseconvention. My decision was to follow theCamel Case, maybe because I am mainly a Java & PHP developer. For me this was not an issue and so I marked them as false positives.

I also removed some issues from theWeather Hat display classas it is just a wrapped copy of the Pimoroni's example. I only made a few changes to make it an implementation of theDisplayInterface.

Taking this into account, this is the result without AI:

And this is the result with AI:

The non-reliability issue from the AI project is for a useless assignment in thefactory.pyfile.

In my opinion, the quality seems better without AI, but it is true that there is no big difference.

Regarding complexity and technical debt, these are the result.

non-AI

AI

Cyclomatic complexity

72

87

Cognitive complexity

19

87

Technical debt

50min

7min

AI code is more difficult to understand (87 vs 19) but the technical debt is higher with the non-AI project due to my lack of knowledge with Python. The concept of interfaces doesn't exist in Python andI didn't approach it correctly.

WebappThe results are quite similar but the AI approach has a 3.6% of duplicated code

The complexity and technical debt results are as follows:

non-AI

AI

Cyclomatic complexity

70

72

Cognitive complexity

10

16

Technical debt

30min

1h 43 min

AI is clearly worse in these metrics, with more than three times of technical debt, and a code a bit more difficult to understand.

## Development Experience

I had mixed feelings using AI. On one hand I was amazed about what you can accomplish with a simple set of requirements. On the other hand I felt overwhelmed and quite distrustful of the final result.

AI struggled in several important points and, in the end, I had to finally explain where the problem was as it was unable to find the solution.

In theSensor Readerproject, AI was applying the temperature offset incorrectly. Instead of indicating the offset value to the Pimoroni's library, before reading the sensor, AI applied it after the temperature was read. Due to this, the relative humidity values were wrong. After several iterations where I told the AI that the result was wrong and asked it to read to Pimoroni's documentation, I had to explain the AI how to fix the issue.

In the Web app I had several problems with authentication:

* In the first run, the user auth didn't work. AI had to fix several issues, one after another: 404 and 500 errors, infinite loop accessing the login form, etc. In one of these iterations, AI recommended me to remove the CSRF token in the login form!
* Once authentication was solved, logout didn't work and I had to implement it by myself as AI was unable to make it work.
* When introducing the JWT authentication AI removed the user session-based authentication!
* AI was unable to make JWT authentication work together with session-based authentication. It insisted several times that the problem was with the Apache web server configuration. But it was just how the project needs to be configured to be executed on the Apache web server. Again, I had to make it work by myself.

It was very frustrating and I ended up quite angry several times.

The SDD (Spec-Driven Development) experience was also frustrating.

Natural language is imprecise by nature. A real developer can fill the gaps of a specification document applying their own judgment and knowledge about the domain. AI will just hallucinate. To avoid this as much as possible, you have to be extremely precise writing the specification. And, IMHO, this is far more complex than coding.

I ended up using the AI to do the things step by step instead of telling it to use the specification file.

## Conclusion

AI is helpful for solving limited tasks and problems like finding a bug, implementing an interface or connecting to an endpoint. Building an entire project from a specification document is another story. With limited tasks it is easy to review the code and feel more or less accountable of the result. Having tones of code to review I feel less in control of the final result.

Don't get me wrong, AI is a good tool, an amazing one, but you still need to know how to write code. And the only way I know to get better at using AI is to continue facing problems by ourselves.

The key point is to find what kind of problems we should solved ourselves and which ones can be delegated to the AI.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse