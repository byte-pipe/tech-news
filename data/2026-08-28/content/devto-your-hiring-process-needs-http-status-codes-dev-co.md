---
title: Your Hiring Process Needs HTTP Status Codes - DEV Community
url: https://dev.to/kenwalger/your-hiring-process-needs-http-status-codes-png
site_name: devto
content_file: devto-your-hiring-process-needs-http-status-codes-dev-co
fetched_at: '2026-08-28T12:25:22.104247'
original_url: https://dev.to/kenwalger/your-hiring-process-needs-http-status-codes-png
author: Ken W Alger
date: '2026-08-26'
description: Because "we'll be in touch" is not an observable state. I submitted a job application recently. It... Tagged with career, discuss, humor, programming.
tags: '#discuss, #career, #humor, #programming'
---

Compares ATS black holes to broken APIs

Because "we'll be in touch" is not an observable state.

I submitted a job application recently.

It was one of those applications where you actually put in the effort. I read the job description carefully, tailored the resume, wrote a cover letter specifically for the organization, and answered the optional questions rather than pretending they were optional.

Then I clickedSubmitand got... nothing.

No confirmation email. No "we received your application." No indication that a candidate record had been created. Just a browser page telling me the submission had succeeded and the vague hope that somewhere, deep inside an applicant tracking system, my carefully assembled application had not been written directly to/dev/null.

As a developer, I find this troubling. Not because I expect an interview, or because I think every recruiter owes me personalized feedback. I just want a status code.

And I think that's a smaller ask than it sounds like, for a reason I'll come back to at the end: the states already exist. Somewhere in that ATS, my application is in one. The decision not to show me which one is a product decision, not a privacy constraint.

## The Web Solved This Problem Decades Ago

When software sends a request to another system, we generally consider it useful for the receiving system to say what happened. Did it work? Is it still processing? Was the request malformed? Is the resource gone? Did something catch fire on the server?

HTTP gives us an entire vocabulary for this.

Hiring systems, meanwhile, have developed their own protocol:

POST /careers/applications

[no observable response]

Enter fullscreen mode

Exit fullscreen mode

This is sometimes followed, anywhere from three minutes to six months later, by:

After careful consideration...

Enter fullscreen mode

Exit fullscreen mode

Instead of inventing vague candidate statuses like "Under Consideration," perhaps hiring systems could adopt something developers already understand.

## The 2xx Family: Success, Allegedly

### 200 OK

A human being has reviewed your application.

Nothing else is implied.

Honestly, this alone would be revolutionary.

### 202 Accepted

Your application has been received and accepted for processing.

This is the most important status code in the entire hiring protocol. The candidate does not need the hiring manager's notes or a walkthrough of the internal workflow. They need:

202 APPLICATION_ACCEPTED

Enter fullscreen mode

Exit fullscreen mode

Now we know the thing exists.

### 204 No Content

Your application was successfully received.

We have chosen not to acknowledge this in any way.

## The 3xx Family: You Have Been Redirected

### 302 Found

We found an internal candidate.

Thanks for playing.

### 304 Not Modified

Your application has been "Under Review" for 47 days.

There has been no change since the last time you checked, or the 23 times before that. There will be no change the next time either. Please consider caching this response locally.

### 410 Gone

The position existed when you applied. It no longer exists. No additional information is available.

At least410would be useful. The current discovery mechanism is noticing that your bookmarked job posting has started redirecting to the careers homepage.

## The 4xx Family: This One's On You

### 401 Unauthorized

You must create an account before applying.

Your password must contain at least 14 characters, uppercase and lowercase letters, a number, a symbol, and one ancient Sumerian glyph. It cannot match any password you have used since 1997.

You will then manually enter every field from the resume you just uploaded.

You will never use this account again.

### 403 Forbidden

You have the required experience and qualifications.

Unfortunately, you live 37 miles outside the geographic boundary within which we have determined this Zoom meeting can occur.

### 404 Not Found

Hiring manager not found. Recruiter not found. Job posting not found.

Nobody knows who owns this requisition.

### 408 Request Timeout

After seven weeks without communication, the candidate has accepted another position.

The hiring team will contact them tomorrow to schedule the second interview.

### 409 Conflict

The position requires 12 years of production experience with a technology introduced six years ago.

The conflict cannot be resolved.

### 417 Expectation Failed

You expected the phrase "we'll be in touch" to imply future communication.

It did not.

### 422 Unprocessable Content

Your experience is relevant, but your career path does not fit cleanly into the predefined boxes in our applicant tracking system.

Human intervention may be required.

Human intervention is unavailable.

### 425 Too Early

You applied 14 minutes after the job was posted.

LinkedIn reports 612 applicants.

We have questions too.

### 451 Unavailable For Legal Reasons

Your qualifications are not the issue.

The issue is a background check vendor, a non-compete of uncertain enforceability, or a sponsorship question nobody wants to be the one to ask about.

## The 5xx Family: It Was Never You

### 500 Internal Server Error

Something has gone wrong internally. Your recruiter left, the headcount was frozen, the hiring manager changed, Finance reconsidered the budget, the organization restructured, or the position was posted by accident.

We will communicate all of these possibilities using the same message:

We have decided to move forward with other candidates.

### 502 Bad Gateway

The recruiter says they are waiting for the hiring manager.

The hiring manager says recruiting owns the next step.

Your request cannot be routed.

### 503 Service Unavailable

Your recruiter is no longer with the company.

Their calendar link remains active.

### 504 Gateway Timeout

"We expect to have a decision by Friday."

Friday has passed. The specification does not define which Friday was intended.

## Candidates Don't Need Distributed Tracing

There's a serious point hiding under all of this. Hiring has an observability problem, and it's usually mistaken for a communication problem.

Companies understandably cannot expose everything happening inside a recruiting process. Candidate evaluations are private. Interview feedback may be sensitive. Hiring managers need room to compare people and make decisions.

That's fine. Nobody is asking for:

GET /hiring-manager/private-thoughts/about-me

Enter fullscreen mode

Exit fullscreen mode

But there is an enormous amount of territory between exposing confidential deliberations and providing no information at all.

A hiring pipeline already has states. An application was received. It entered review. Someone reviewed it. An interview was requested. The requisition was paused. The position was filled. The position was canceled. The candidate was declined.

Those state transitions already exist in the system. They are already recorded, timestamped, and reportable, because that's how recruiting teams measure their own funnel. The candidate is the one participant in the process who cannot see the record they're in.

## Give Us the Boring Version

Imagine an applicant portal that reported nothing more than this:

202 APPLICATION_RECEIVED Mar 04
200 REVIEWED Mar 19
304 NO_CHANGE Apr 02
304 NO_CHANGE Apr 30
410 POSITION_CLOSED May 12

Enter fullscreen mode

Exit fullscreen mode

That's not radical transparency. It's barely transparency at all. But it tells you the system is functioning.

It removes the need to wonder whether an application disappeared. It reduces pointless portal refreshing. And it prevents candidates from reading silence as information, when silence might mean anything from "the hiring manager is on vacation" to "the requisition was canceled two weeks ago."

Mostly, it treats applicants like participants in a process rather than packets transmitted into an undocumented endpoint.

## 200 OK

I don't expect every application to result in an interview. I've submitted enough of them to have considerable empirical evidence supporting that position.

I don't expect detailed rejection feedback either. I understand why companies are reluctant to provide it. I don't even particularly mind403 REQUIREMENTS_NOT_METor410 POSITION_FILLED. Those are answers.

What makes modern hiring uniquely frustrating isn't rejection. It's uncertainty about whether anything is happening at all.

Software engineers have spent decades building systems around a simple principle: when one system asks another to do something, the response should carry enough information to understand what happened.

Candidates aren't asking for distributed tracing of your recruiting infrastructure.

We'd settle for a status code.

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse