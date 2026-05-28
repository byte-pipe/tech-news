---
title: 'A 100% Private, Local AI Resume Optimizer with Google Gemma 4: How I Built ResuMate! - DEV Community'
url: https://dev.to/deeptej/i-built-resumate-a-100-private-local-ai-resume-optimizer-with-google-gemma-4-699
site_name: devto
content_file: devto-a-100-private-local-ai-resume-optimizer-with-googl
fetched_at: '2026-05-28T12:11:38.231021'
original_url: https://dev.to/deeptej/i-built-resumate-a-100-private-local-ai-resume-optimizer-with-google-gemma-4-699
author: deeptej (⁠^⁠.⁠_⁠.⁠^⁠)⁠ﾉ
date: '2026-05-24'
description: 'This is a submission for the Gemma 4 Challenge: Build with Gemma 4 See why I chose the Gemma 4 E2B... Tagged with devchallenge, gemmachallenge, gemma, discuss.'
tags: '#discuss, #devchallenge, #gemmachallenge, #gemma'
---

Gemma 4 Challenge: Build With Gemma 4 Submission

This is a submission for theGemma 4 Challenge: Build with Gemma 4

See why I chose the Gemma 4 E2B model

I was recently preparing for my internship applications and like everyone else I wanted my resume to be as good as it could possibly be. So I uploaded my entire education history to a website that claimed to rate and improve my resume. I entered every project, every achievement, my phone number, my email, links to my GitHub and LinkedIn, hit enter and waited...

But somewhere between hitting enter and reading the response, a thought crept in:where did all of that personal information just, go?

A resume isNOTa casual document. It has my address on it, my education history, the names of professors and mentors I listed as references. And I had just handed all of it to a server I knew nothing about, owned by a company whose privacy policy I have definitely never read.

I couldn't shake that feeling off.So I built something to FIX IT!!

## What I Built

ResuMateis aprivacy-firstresume tailoring tool that runs ENTIRELY on your local machine, thanks toGemma 4!. Your resume and YOUR personal information never leaves your laptop. Not a single character!

You upload your resume once. Then for every job you're interested in, you paste the job description and ResuMate doessix things:

* ATS match analysis:Scores your resume against the job description from 0 to 100. Shows you exactly which keywords are present, which are missing, andgives you specific, actionable suggestions to improve your scorewithout fabricating experience you don't have.

* Drafts a cover letter:The modelfirst reads the tone of the job description, asks itself, is this a corporate law firm or a startup? and drafts a cover letter best suited for that world. Most importantly, it usesYOURactual achievements, thanks toGemma 4's context window of up to 256K token!

* Job Description Decoder:This one is my personal favorite. A lot of times companies use a lot of corporate jargon and I'm just steppin' out of college :) ResuMate reads the job description and translates corporate lingo into plain english (phew, now that's better)."Operationalize strategic pillars to achieve sustainable, scalable leverage"???? like whaa? The decoder effectively surfaces what the company is trying to say, all while also using the context that the entire job description provides.

* Red Flag Detector:ResuMate looks for patterns in the job description that may be something you might want to know before applying or is worth asking during the interview. Each flag comes with severity rating and specific questions you can ask during the interview as well! Now that's convenient~

* Interview Prep:This one is another one of my favorites! and it also comes from a personal experience!

Whenever I look at job descriptions that I might seem fit for, I immediately start thinking about the type of questions that might be asked for such a role and the topics that I might want to prep for the role, I built this feature to tackle just that!

ResuMate generatesquestions tailored to both the role requirement and your specific background. **This does not include generic"Tell me your weaknesses and strengths"type questions. Each question also comes with an explaination of what the interviewer is actually testing and how to approach a strong answer using your real experience. ResuMate also **recommends a few topics that you might want to brush up before the interview based on the keywords it picks up from the job description.Pretty cool right?

* Generate a tailored resume:Gemma reorganizes and emphasizes on your existing experience and structure it to match the priorities of the job description. It incorporates missing keywords if the user already has the experience but not the specific keywords. Once done the user can directly export the tailored resume to a PDF. And the best part, every job page has its own tailored version of resume, so you don't need to download and store multiple versions, they'll always stay under the job card.

Every job you analyse is saved locally so you can have a cup of tea or go for a walk and everything is stays exactly where you left it!No re-running, no re-uploading.The dashboard shows your full history with ATS scores for every job at a glance. This not only saves time but also gives you a birds eye view of every job you've looked at!

The thing that makes ResuMate different from every other AI resume tools isn't just any single feature. It's the direction the analysis runs in.

Most tools are one directional. They optimise you for the job.ResuMate is bidirectional.It optimises your application and it analyses the job on your behalf.The job description decoder and red flag detector exist becausea job application is not just you auditioning for a company, it's also the company auditioning for you.You should go into that interview having done your homework on both sides.

## Demo

## Code

Find the source code for ResuMate and how you can download and run it on your machine on GitHub:ResuMate on GitHub

### Why Gemma 4 E2B

The inputs are text, and both models handle text identically.

ResuMate relies on two text documents as input- a resume and a job description.Both Gemma 4 E2B and Gemma 4 E4B share the same context window of 128K tokens and the same 262K vocabulary. For a task like resume analysis, these were the numbers that mattered to me. A resume and a job description rarely exceed a few thousand tokens. E2B handles this without breaking a sweat and E4B would handle it the same way, so there wasn't really a capability gap to close by going bigger.

### My own hardware told me who my users are

This is the reason I feel the most strongly about. When I tried running E4B locally during development, it would not even initialise on my machine. I have 4GB of total RAM, with perhaps 1 to 2GB realistically available after everything else running. E4B needs more than that to load, let alone run inference. E2B initialised, ran, and was fast.

This made me realise about who ResuMate is actually for. The target audience is students and fresh graduates, people who are actively looking for their first job or first internship. That group, is usually not running high-end hardware. They are on a similar kind of laptop I was on. If the tool that is supposed to help them with their job search cannot even start on their machine, it has already failed them before they typed a single word.

E2B runs on modest hardware.It has the same context length and vocabulary as E4B.It is faster on constrained resources. This was enough for me to single out which model I am going to go with.

### Speed makes or breaks the entire user experience

LocalHire runs six sequential prompts every time you analyze a job. This means six round trips to the model before you see a complete analysis. If each prompt takes noticeably longer due to a heavier model, that slowdown really adds up across the entire session.

And job seekers aren't just going to do a single analysis. They might be looking at tens of roles eveyr week. I wanted every analysis to feel as fast as possible, not something you start and come back to, later. E2B generates tokens faster on the same hardware, and across six prompts per-job that difference is something users would really feel.

## How I Used Gemma 4

There are a total of six resume tasks that are run per job. Gemma 4 runs these, each with its own carefully designed prompt.

You can check out the prompts here:ResuMate/blob/main/core/ollama.py#L76

* TheATS analysisasks the model to read two documents simultaneously, identify semantic relationships between the terms rather than just extracting keywords, produce a numeric score, categorize the keywords into two lists i.e. found and missing and generate suggestions to improve the score- all in a structured markdown format that the website can parse and render.
* Thejob description decoderwhich for me was one of the hardest prompts to get right. Corpo lingo carries meaning that depends a lot of context. Getting Gemma to decode phrases honestly, required multiple attempts to get right. And I can finally understand what"Operationalize strategic pillars to achieve sustainable, scalable leverage"means 😭
* Thecover letter generatordoes multiple things- detect the tone of the JD, match it in the response, avoid certain types of opening statements like "I am writing..." and referencing only real experience for the user's resume and not hallucinating all whilst staying within three paras. Gemma 4 handles this really well provided the instructions are explicit enough, and I got to pick up a bit of prompt engineering along the way!
* Theinterview prepfeature required Gemma 4 to cross-reference the two documents viz. the resume and the job description, and figure out the gap between them to suggest questions that help fill that gap, instead of generic interview questions, which made this even more personal.

Each of these prompts streams back to the browser token by token usingServer-Sent Events. Django keeps a persistent connection open and forwards each token from Ollama as it arrives.

## What I learnt

* Prompt engineering is harder than it looks.I assumed writing a prompt was just... asking nicely 😭 boy was I wrong. It isnt. Getting Gemma to produce output in a consistent, parseable format took more tries than I expected. Early versions of my prompts produced beautifully written responses that my code could not parse at all. The minute I started telling it, here is exactly what I want, here is exactly how I want it formatted, here is an example, everything got more reliable.
* Thinking about constraintsBecause I was running everything on my own machine I had to constantly think about RAM limits, inference speeds etc. These are constraints that disappear when you use cloud API. Building locally helped me think in constraints.

## What worked well

* Finally build my first project with a local LLMI hadn't incorporated a locally running LLM with a project before and I finally got a chance to do it, so that's pretty cool!
* Gotta love DjangoFile uploads, streaming HTTP responses, SQLite db, template rendering, everything just worked. No fighting with the framework.

## What I Plan to Improve

* Browser extension for automatic JD importRight now users paste job descriptions manually. The real workflow is: see a job on LinkedIn or Naukri or Indeed, click a button, have the JD extracted automatically. Perhaps a small browser extension that reads the page content and sends it to the local Django server would eliminate the only friction that remains in the core workflow. This is the next feature I want to build.

## Conclusion

Every technical decision while building ResuMate traced back to one very important thing:the model has to run on your machine, privately, on hardware you actually own.That constraint ruled out cloud APIs, ruled out the larger models, and helped me go with Gemma 4 E2B as my model of choice. The constraints did not limit the project, but they defined it!

Thanks for reading so far!! I hope we all get the role we're dreaming of! ✨🌸 See y'all in another post!! 👋🏻

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse