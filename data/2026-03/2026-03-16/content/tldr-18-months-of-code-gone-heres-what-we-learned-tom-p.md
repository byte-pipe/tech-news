---
title: 18 Months of Code, Gone. Here's What We Learned. | Tom Piaggio
url: https://tompiagg.io/posts/we-threw-away-1-5-years-of-code
site_name: tldr
content_file: tldr-18-months-of-code-gone-heres-what-we-learned-tom-p
fetched_at: '2026-03-16T19:26:54.322216'
original_url: https://tompiagg.io/posts/we-threw-away-1-5-years-of-code
author: Tom Piaggio
date: '2026-03-16'
published_date: '2026-03-10T12:00:00.000Z'
description: We developed this product for over 1.5 years, closed clients left right and center, and now we're throwing everything away. Here's why, what we learned, and what we chose instead.
tags:
- tldr
---

# 18 Months of Code, Gone. Here's What We Learned.

Share:
Twitter
Copy Link
March	10, 2026

We developed this product for over 1.5 years, closed clients left right and center, and now we're throwing everything away.

In case you don't know me (orAutonoma), we're no strangers to pivots. Funnily enough, we pivoted like 4 times already (enterprise search, documentation generation, coding agent, QA testing platform). The reasons are beyond the scope of this article. In all cases, we knew bugs were painful, we just didn't know what was the best way of solving the problem.

On our last pivot, we actually started getting customers and raised a round from one of the biggest names in the industry. We hired a team of 14 (as I'm writing this article) and started closing clients left right and center. So why would we take such a drastic decision over something that's working for many customers? Well, many reasons. That's why I'm writing this article.

## The No-Tests Era (and Why I Regret It)

In my past, I've been guilty of overengineering (as many of you probably also did, and if you say you didn't you're lying). I was Uncle Bob-Pilled but I've been burnt so hard with this that in this startup, I went 180 deg in the opposite direction: TypeScript monorepo, no strict, no tests. Just ship and that's all that matters.

That worked great for our early customers when there were only two of us writing code and each of us owned a huge portion of it and knew everything. After we started hiring, it became a disaster. Bugs were appearing everywhere out of the blue. The codebase was a huge mess of nulls, undefined behaviour, bad error handling. It was so bad that we actually lost a client over this.

For the longest time, I would NOT allow people to write tests because I thought that culturally, we need to have a culture of shipping fast and we should be dogfooding our own product and that should be enough. At some point, I realized that I was affecting the quality of our product and productivity and I changed my mind. In some ways, it was too late. That's why now that we're rewriting everything, we started with tests from the ground up and the most strict TypeScript mode.

## Why a Rewrite and Not a Refactor

Initially, when we set out to build this product, we wanted a fully agentic solution. At the time, the tech wasn't there. It was GPT-4 era (not 4o, just 4). The models were so bad that we needed to build huge guardrails and give them very accurate information in order for them to kind of work. We built huge Playwright and Appium wrappers that would do very complex inspections over the code and extract a bunch of information. I'm proud to say that none of the open source solutions I've seen come close to the level of sophistication and replicability we built. We had like 7 clicking strategies that would self-heal on the fly if something changed, for example. That made running tests super fast and reliable.

Now, models have actually advanced so much that the sophisticated inspection is not necessary anymore. And we'd be bringing a huge codebase, with crippling tech debt and vestiges of a worse past of unstrict TypeScript, with not much to gain. We discussed it with the team and decided the best way moving forward was to rewrite the whole thing (bringing the agentic stuff over).

## Dropping Next.js and Server Actions

Some of the tech decisions we made were to actually change technologies. And I think this is interesting.

We were super invested in Next.js and Server Actions. We didn't do fetches of any kind. Server Actions is a great idea with a subpar execution IMHO. The idea of having functions that you could use on the frontend is amazing. They have some very bad caveats that make them a bad solution in almost all cases.

They're async.This might sound like a weird take, but remember we're using this mainly on React. Having async functions fetching data potentially means auseEffectblock (or have that data be SSR), or async functions and having to handle the changing state manually.

They're hard to test.When you implement a function like this:

export async function getUserById(id: string): Promise<User> {
 return prisma.user.findFirst({
		where: {id}
 })
}

You either have to create a Prisma object with an in-memory db, apply migrations, etc; or mock the Prisma object. It gives you no flexibility. It's impossible to do dependency injection because that'd mean passing the db from the frontend to the backend and that clearly makes no sense. The feeling of defining a Server Action and calling it from the frontend is magical but that's where the magic ends.

They execute sequentially. GLOBALLY.WTF is that decision. It's like a manufactured Python Global Interpreter Lock but in TypeScript. I understand that the reasoning is to have some kind of idempotency and not have renders be out of order... but WTF. That makes them either unusable in any project or you have to develop FOR Server Actions. And when you have to accommodate your practices to a framework and not the other way around, it's a sign that it's a bad tech.

They're not observable.This was really bad. We use Sentry and for many technologies they have automatic instrumentation. I'm a hater of manual instrumentation. I think these things should not clutter the code. The problem with Server Actions is that they all become a single POST. So in Sentry, you'd see every Server Action as a single POST to/with garbage unreadable data. They can't be traced. You can't add headers to them. Just a pain.

They're a security footgun.You could argue this is a skill issue. If you're like me and start using a technology before fully reading the documentation, you might easily miss this. Server Actionsbecomean endpoint in practice. If you don't structure the action right, you could expose yourself to very obvious security vulnerabilities that are not apparent when writing the code. For example, the function that I wrote before is actually unsafe. This would let anyone get any user if they have the ID:

export async function getUserById(id: string): Promise<User> {
 return prisma.user.findFirst({
		where: {id}
 })
}

This would be the correct implementation:

export async function getUserById(id: string): Promise<User> {
	const cookieStore = await cookies()
	if (cookieStore.orgId == null) {
		return null
	}

 return prisma.user.findFirst({
		where: {id, orgId: cookieStore.orgId}
 })
}

The problem this has is that if you code this way, you can't share the code with the API. So what you actually have to do is have aprivatedirectory where you have the implementations, and the Server Actions are a wrapper of those implementations but with the auth check, and those same private functions can be used by the API.

/private/users.ts

export async function privateGetUserById(id: string, orgId: string): Promise<User> {
 return prisma.user.findFirst({
		where: {id, orgId}
 })
}

/lib/users-actions.ts

export async function getUserById(id: string): Promise<User> {
	const cookieStore = await cookies()
	if (cookieStore.orgId == null) {
		return null
	}

 return privateGetUserById(id, cookieStore.orgId)
}

/api/users.ts

import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(
 req: NextApiRequest,
 res: NextApiResponse
) {
 // validate headers and body for auth

 const result = await privateGetUserById(id, cookieStore.orgId)

 return NextResponse.json(result)
}

They use errors as flow control.It would be weird to blame Next.js for the fact that errors in JavaScript (and TypeScript) are bad. JavaScript errors are just bad and everybody knows that. I usually prefer returning errors as values so I know when something throws and know what to do about it without having to go to the implementation. That worksmostlyfor Next.js, except that Next.js uses errors as flow control. This is one of the worst practices in coding ever IMO. Especially in JavaScript where errors are not apparent when they're thrown. Stuff like redirects are exceptions of typeredirect. So something like this won't work:

// Broken: the redirect gets caught
async function myAction() {
 try {
 await doSomething();
 redirect('/dashboard');
 } catch (e) {
 // This catches the redirect "error" too
 console.error(e);
 }
}

So I'm forced to do something ugly like this:

async function myAction() {
 let shouldRedirect = false;
 try {
 await doSomething();
 shouldRedirect = true;
 } catch (e) {
 // handle real errors
 }
 if (shouldRedirect) redirect('/dashboard');
}

Or, I'm forced to do try/catches on every line if I need to handle errors differently for each function:

async function myAction() {
 try {
 await doSomething();
 } catch (e) {
 console.error(e);
 return
 }

 try {
 await doSomethingElse();
 } catch (e) {
 await undoSomething()
 console.error(e);
 return
 }

 redirect('/dashboard');
}

In all my years of software development I have never had such a slow framework in all senses. Slow to build. Slow to develop. Slow to startup. Slow Server Actions. I swear Angular 2 was faster in all senses. I was so broken by this that when we changed to just React, I thought the server was not reloading because it was so fast.

## What We Chose Instead (and How We Went From 8GB to Basically Free)

We went for React with tRPC (basically TanStack Start) and a Hono backend. I have to say I miss having everything packaged into a single package, but it just makes more sense given our deployment.

We have everything mostly deployed in Kubernetes (we can discuss this but we have very complex stateful workflows that we need to expose as temporary machines that are very easily deployed on Kubernetes, and very hard on other platforms). We actually had the Next.js project running in a container. Literally, the container took like 8GB RAM per instance. It was the biggest we had. With React we just compile into static files and serve them from a CDN (basically free). And the Hono backend is like < 100MB RAM.

## The Orchestration Problem

If you think Server Actions were painful, wait until you hear about orchestration.

We considered useworkflow.dev (which I love the ergonomics of), but it was impossible to merge with the use cases we had for our jobs and it would just create points of failure that I didn't need. Eg:

// pseudocode
export async function startMobileJob(){
	"use step"

	// this action is async and doesn't wait for the job to finish, just for it to be created on Kubernetes
	await k8s.spawnJob()

	// i could poll for the result?
	await pollForJob()

	// i could use the webhook primitive and wait for the response?
	await webhook()
}

In both cases I'll be adding custom code that could fail. The webhook needs a sidecar container that checks if the job finishes and sends a fetch request. You might say "well that sounds pretty easy" and it is. Until for some reason it fails because some dependency was missing or the Kubernetes JSON was incorrectly formatted or a multiplicity of reasons and you get a job that never ends on the UI. The polling is the same. Jobs can end in multiple different states and you have to account for all of them.

I tried many solutions in the past that seem simple but hide complexities much bigger (like building asmallorchestrator in TypeScript that would listen for job changes). It's impossible to reconcile the information in a quick and dirty implementation. Also, very hard to test.

In the end we went with the technology we know and love, with its quirks and ugly UI: Argo. It's Kubernetes native. Each step is a job and you're guaranteed that it runs in the order that you need. It scales pretty well to the thousands of tests we need to run reliably. And you can merge many workflows together into a single one so we can easily send a message at the end. Again, this is very hard to test but we have already built abstractions to do this.

Before you mention Temporal: it has the same problem useworkflow has. It can't wait for a job to finish without breaking the workflow abstraction.

## "But Why Do You Need a Kubernetes Job?"

The reason is that the jobs have stateful parts, and in many cases, we need to deploy stuff alongside the job. For example, for our mobile jobs, we need to acquire a lease for the device (a whole different implementation that's again, outside the scope of this blogpost), create the job, install the app, connect to the device, etc. All of those take time and the Appium connection + install is costly to setup. So we can't have a stateless process be passing around information and recreating all this every time.

Itcouldbe a step in one of these workflow technologies, but that'd mean having a HUGE image with both dependencies from iOS, Android, web, and any other workflow I need into a single image making it super huge. Thatcouldbe a solution. I'm not saying it would be a bad one, but we just thought we'd go with the devil that we know.

## Wrapping Up

I'm open if you know better solutions to any of this. I'd love to know if you agree with these decisions or if you'd do something different. It's been a very exciting journey for us and we'll be announcing this new product in a few weeks. We're just testing with some design partners right now. If you want early access or want to break it before we launch, DM me onTwitter. We'll have a "one more thing" in a couple of weeks as well, so stay tuned.

### Want more of this?

Subscribe to get notified when I write something new. No spam, just occasional thoughts on AI, startups, and things I'm probably doing wrong.

Subscribe
