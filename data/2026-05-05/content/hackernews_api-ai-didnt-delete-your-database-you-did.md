---
title: AI didn't delete your database, you did
url: https://idiallo.com/blog/ai-didnt-delete-your-database-you-did
site_name: hackernews_api
content_file: hackernews_api-ai-didnt-delete-your-database-you-did
fetched_at: '2026-05-05T20:06:08.535970'
original_url: https://idiallo.com/blog/ai-didnt-delete-your-database-you-did
author: Brajeshwar
date: '2026-05-05'
description: The AI didn't delete your database, your poor decision did. The best way forward is accountability and having competent developers in your team. No way around it.
tags:
- hackernews
- trending
---

Last week, a tweet went viral showing a guy claiming that a Cursor/Claude agentdeleted his company's production database. We watched from the sidelines as he tried to get a confession from the agent: "Why did you delete it when you were told never to perform this action?" Then he tried to parse the answer to either learn from his mistake or warn us about the dangers of AI agents.

I have a question too: why do you have an API endpoint that deletes your entire production database? His post rambled on about false marketing in AI, bad customer support, and so on. What was missing was accountability.

I'm not one to blindly defend AI, I always err on the side of caution. But I also know you can't blame a tool for your own mistakes.

In 2010, I worked with a company that had a very manual deployment process. We used SVN for version control. To deploy, we had to copy trunk, the equivalent of the master branch, into a release folder labeled with a release date. Then we made a second copy of that release and called it "current." That way, pulling the current folder always gave you the latest release.

One day, while deploying, I accidentally copied trunk twice. To fix it via the CLI, I edited my previous command to delete the duplicate. Then I continued the deployment without any issues... or so I thought. Turns out, I hadn't deleted the duplicate copy at all. I had edited the wrong command and deleted trunk instead. Later that day, another developer was confused when he couldn't find it.

All hell broke loose. Managers scrambled, meetings were called. By the time the news reached my team, the lead developer had already run a command to revert the deletion. He checked the logs, saw that I was responsible, and my next task was to write a script to automate our deployment process so this kind of mistake couldn't happen again. Before the day was over, we had a more robust system in place. One that eventually grew into a full CI/CD pipeline.

Automation helps eliminate the silly mistakes that come with manual, repetitive work. We could have easily gone around asking "Why didn't SVN prevent us from deleting trunk?" But the real problem was our manual process. Unlike machines, we can't repeat a task exactly the same way every single day. We are bound to slip up eventually.

With AI generating large swaths of code, we get the illusion of that same security. But automation means doing the same thing the same way every time. AI is more like me copying and pasting branches, it's bound to make mistakes, and it's not equipped to explain why it did what it did. The terms we use, like "thinking" and "reasoning," may look like reflection from an intelligent agent. But these are marketing terms slapped on top of AI. In reality, the models are still just generating tokens.

Now, back to the main problem this guy faced. Why does a public-facing API that can delete all your production databases even exist? If the AI hadn't called that endpoint, someone else eventually would have. It's like putting a self-destruct button on your car's dashboard. You have every reason not to press it, because you like your car and it takes you from point A to point B. But a motivated toddler who wiggles out of his car seat will hit that big red button the moment he sees it. You can't then interrogate the child about his reasoning. Mine would have answered simply: "I did it because I pressed it."

I suspect a large part of this company's application was vibe-coded. The software architects used AI to spec the product from AI-generated descriptions provided by the product team. The developers used AI to write the code. The reviewers used AI to approve it. Now, when a bug appears, the only option is to interrogate yet another AI for answers, probably not even running on the same GPU that generated the original code. You can't blame the GPU!

The simple solution isknow what you're deploying to production.The more realistic one is, if you're going to use AI extensively, build a process where competent developers use it as a tool to augment their work, not a way to avoid accountability. And please, don't let your CEO or CTO write the code.

Did you like this article?You can buy me a coffee.Share your insightful comments here.

### Join my newsletter

Subscribe

JavaScript is required to combat spammers.

Follow me onTwitter,Spotify, orRSS
						Feed

## On a related note, here are some interesting articles.

### All AI Videos Are Harmful

When OpenAI released the first version of Sora, I was excited. For years, I'd had thisshort storysitting on my hard drive, something I'd written long ago and always dreamed of bringing to life as a short film. The only problem was I didn't have the expertise to shoot a movie, and my Blender 3D skills are rusty for lack of use. But Sora promised something different. I could upload my sketches, input my script, and generate the film in my mind. The creative barrier had finally been lifted.

### Boredom is the Gatekeeper

That first Monday of my holiday break, I made a promise to myself. No work emails, no side projects, not even glancing at my blog. This time was for family, for Netflix queues, for rereading dog-eared novels. One thing I was really looking forward to was learning something new, a new skill. Not for utility, but purely for curiosity. I wanted to learn about batteries. They power our world, yet they're a complete mystery to me. I only vaguely remember what I learned in high school decades ago. This would be the perfect subject for me.

### Why Am I Paranoid, You Say?

Technology has advanced to a point I could only have dreamed of as a child. Have you seen the graphics in video games lately? Zero to 60 miles per hour in under two seconds? Communicating with anyone around the world at the touch of a button? It's incredible, to say the least. But every time I grab the TV remote and decline the terms of service, my family watches in confusion. I don't usually have the words to explain my paranoia to them, but let me try.

 

				View all articles
			

### Comments