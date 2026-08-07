---
title: How I Smashed a Bug in a Shared Authentication Library - DEV Community
url: https://dev.to/gramli/how-i-smashed-a-bug-in-a-shared-authentication-library-33fm
site_name: devto
content_file: devto-how-i-smashed-a-bug-in-a-shared-authentication-lib
fetched_at: '2026-08-07T19:52:00.430486'
original_url: https://dev.to/gramli/how-i-smashed-a-bug-in-a-shared-authentication-library-33fm
author: Daniel Balcarek
date: '2026-08-05'
description: 'This is a submission for DEV''s Summer Bug Smash: Smash Stories powered by Sentry. This happened a... Tagged with devchallenge, bugsmash, angular, typescript.'
tags: '#devchallenge, #bugsmash, #angular, #typescript'
---

Summer Bug Smash: Smash Stories 🐛🛹

This is a submission forDEV's Summer Bug Smash: Smash Storiespowered bySentry.

This happened a while ago at one of the corporations where I worked.

I was working on a web application as a full-stack developer, so I was responsible for both the frontend and the backend.

Because the corporation was huge, there were several libraries and services shared across multiple teams and maintained by dedicated developers. It was basically open source inside a corporation. 😄

And of course, we used some of those libraries and services, because why reinvent the wheel, right?

So, after we released the first version of our web application, an interesting bug appeared.

When a user opened the application in multiple browser tabs, authentication would sometimes randomly break in one of them. Once that happened, the tab could not recover until the user pressed F5 or closed it completely.

Interesting.

As the senior developer on the team, I took the bug and started investigating.

After some time and a lot of attempts, I found that when the frontend tried to refresh the authentication token, it received a403 ForbiddenHTTP response, and the authentication flow broke completely.

So I played around with session storage and local storage in Chrome and tried changing the authentication configuration. It did not help much, but one thing was clear: the bug appeared to be inside the shared frontend authentication library.

Okay.

I collected all the logs and everything I had learned about the bug and went to the frontend team responsible for maintaining the authentication library.

After an hour-long discussion, they concluded that it was not their fault because the backend team maintaining the authentication service was not supposed to return that particular response code.

Yes, the frontend library and the backend authentication service were maintained by completely different teams.

I was not fully convinced, but there were more of them. 😁

So I collected all the logs again and went to the backend team.

We had another discussion and found that they were returning a valid response code because the frontend authentication library was sending a refresh token that had already been invalidated. The underlying problem was a race condition between multiple tabs. One tab refreshed the token and invalidated the previous refresh token while another tab was still trying to use it.

Okay...

So, once again, I grabbed all the logs and went back to the frontend team.

And in case you are wondering why the two teams did not simply communicate with each other, both teams gave me approximately the same answer:

This is a problem in your application, so your team has to solve it.

Back to the frontend team.

I presented the backend team’s conclusion, but they were still not convinced.

At that point, I was starting to get a little angry, so I created a single ticket, added both teams to it, and included all the logs, requests, responses, timestamps, and everything else I had collected.

Weeks passed.

Conversations continued in the ticket and in chat.

But the bug resolution still looked far, far away.

So I decided to arrange a meeting for everyone involved.

And finally, something happened.

During the meeting, we agreed that the problem was in the frontend authentication library and that the frontend team would fix it.

Success!

Or so I thought.

Two weeks later, while testers and users were getting increasingly angry because the application randomly failed to refresh authentication tokens, the frontend team came back with their final conclusion:

They were unable to reproduce the problem.

And users should not open the application in multiple tabs.

Until that moment, opening multiple tabs had been considered a perfectly normal user flow...

At that moment, I closed the ticket, completely removed the corporate frontend authentication library from our project, and reimplemented the entire client-side authentication flow directly against the existing corporate authentication service.

The main changes were in the Angular HTTP interceptor and the token refresh flow. I updated the interceptor to handle authentication-related responses, including403 Forbidden, without leaving the entire tab stuck in a broken state.

I also reworked how refreshed tokens were handled and stored in session storage. Invalidated tokens and failed refresh attempts were now handled explicitly instead of causing the authentication flow to stop completely.

Yes, it took two days and one night. And yes, I took a few ideas from the corporate authentication library, because otherwise it would have taken much longer. 😄

But I only have one set of nerves.

And you know what?

From that moment on, it worked like a charm. And whenever another bug appeared, it was fixed immediately because, this time, we actually owned the code.

And that is my Bug Smash story where corporate life can sometimes be slightly ridiculous, and fixing one bug can mean rewriting the entire feature.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (43 comments)
 

For further actions, you may consider blocking this person and/orreporting abuse