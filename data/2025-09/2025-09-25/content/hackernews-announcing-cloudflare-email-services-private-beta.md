---
title: Announcing Cloudflare Email Service’s private beta
url: https://blog.cloudflare.com/email-service/
site_name: hackernews
fetched_at: '2025-09-25T19:07:45.448878'
original_url: https://blog.cloudflare.com/email-service/
author: tosh
date: '2025-09-25'
published_date: 2025-09-25T14:00+00:00
description: Today, we’re launching Cloudflare Email Service. Send and receive email directly from your Workers with native bindings—no API keys needed. We're unifying email sending and routing into a single service built for developers. Sign up for the private beta.
---

# Announcing Cloudflare Email Service’s private beta

2025-09-25

* Thomas Gauvin
* Celso Martinho
4 min read

If you are building an application, you rely on email to communicate with your users. You validate their signup, notify them about events, and send them invoices through email. The service continues to find new purpose with agentic workflows and other AI-powered tools that rely on a simple email as an input or output.

And it is a pain for developers to manage. It’s frequently the most annoying burden for most teams. Developers deserve a solution that is simple, reliable, and deeply integrated into their workflow.

Today, we're excited to announce just that: the private beta of Email Sending, a new capability that allows you to send transactional emails directly from Cloudflare Workers. Email Sending joins and expands our popularEmail Routingproduct, and together they form the new Cloudflare Email Service — a single, unified developer experience for all your email needs.

With Cloudflare Email Service, we’re distilling our years of experiencesecuringandroutingemails, and combining it with the power of the developer platform. Now, sending an email is as easy as adding a binding to a Worker and callingsend:

export default {
 async fetch(request, env, ctx) {

 await env.SEND_EMAIL.send({
 to: [{ email: "
[email protected]
" }],
 from: { email: "
[email protected]
", name: "Your App" },
 subject: "Hello World",
 text: "Hello World!"
 });

 return new Response(`Successfully sent email!`);
 },
};

### Email experience is user experience

Email is a core tenet of your user experience. It’s how you stay in touch with your users when they are outside your applications. Users rely on email to inform them when they need to take actions such as password resets, purchase receipts, magic login links, and onboarding flows. When they fail, your application fails.

That means it’s crucial that emails need to land in your users’ inboxes, both reliably and quickly. A magic link that arrives ten minutes late is a lost user. An email delivered to a spam folder breaks user flows and can erode trust in your product. That’s why we’re focusing on deliverability and time-to-inbox with Cloudflare Email Service.

To do this, we’re tightly integrating with DNS to automatically configure the necessary DNS records — like SPF, DKIM and DMARC — such that email providers can verify your sending domain and trust your emails. Plus, in true Cloudflare fashion, Email Service is a global service. That means that we can deliver your emails with low latency anywhere in the world, without the complexity of managing servers across regions.

### Simple and flexible for developers

Treating email as a core piece of your application also means building for every touchpoint in your development workflow. We’re building Email Service as part of the Cloudflare stack to make developing with email feels as natural as writing a Worker.

In practice, that means solving for every part of the transactional email workflow:

* Starting with Email Service is easy. Instead of managing API keys and secrets, you can use theEmailbinding to yourwrangler.jsoncand send emails securely and with no risk of leaked credentials.
* You can use Workers to process incoming mail, store attachments in R2, and add tasks to Queues to get email sending off the hot path of your application. And you can usewranglerto emulate Email Sending locally, allowing you to test your user journeys without jumping between tools and environments.
* In production, you have clear observability over your emails with bounce rates and delivery events. And, when a user reports a missing email, you can quickly dive into the delivery status to debug issues quickly and help get your user back on track.

We’re also making sure Email Service seamlessly fits into your existing applications. If you need to send emails from external services, you can do so using either REST APIs or SMTP. Likewise, if you’ve been leaning on existing email frameworks (likeReact Email) to send rich, HTML-rendered emails to users, you can continue to use them with Email Service. Import the library, render your template, and pass it to the `send` method just as you would elsewhere.

import { render, pretty, toPlainText } from '@react-email/render';
import { SignupConfirmation } from './templates';

export default {
 async fetch(request, env, ctx) {

 // Convert React Email template to html
 const html = await pretty(await render(<SignupConfirmation url="https://your-domain.com/confirmation-id"/>));

 // Use the Email Sending binding to send emails
 await env.SEND_EMAIL.send({
 to: [{ email: "
[email protected]
" }],
 from: { email: "
[email protected]
", name: "Welcome" },
 subject: "Signup Confirmation",
 html,
 text: toPlainText(html)
 });

 return new Response(`Successfully sent email!`);
 }
};

### Email Routing and Email Sending: Better together

Sending email is only half the story. Applications often need to receive and parse emails to create powerful workflows. By combining Email Sending with our existingEmail Routingcapabilities, we're providing a complete, end-to-end solution for all your application's email needs.

Email Routing allows you to create custom email addresses on your domain and handle incoming messages programmatically with a Worker, which can enable powerful application flows such as:

* UsingWorkers AIto parse, summarize and even label incoming emails: flagging security events from customers, early signs of a bug or incident, and/or generating automatic responses based on those incoming emails.
* Creating support tickets in systems like JIRA or Linear from emails sent to[email protected].
* Processing invoices sent to[email protected]and storing attachments in R2.

To use Email Routing, add theemailhandler to your Worker application and process it as needed:

export default {
 // Create an email handler to process emails delivered to your Worker
 async email(message, env, ctx) {

 // Classify incoming emails using Workers AI
 const { score, label } = env.AI.run("@cf/huggingface/distilbert-sst-2-int8", { text: message.raw" })

 env.PROCESSED_EMAILS.send({score, label, message});
 },
};

When you combine inbound routing with outbound sending, you can close the loop entirely within Cloudflare. Imagine a user emails your support address. A Worker can receive the email, parse its content, call a third-party API to create a ticket, and then use the Email Sending binding to send an immediate confirmation back to the user with their ticket number. That’s the power of a unified Email Service.

Email Sending will require a paid Workers subscription, and we'll be charging based on messages sent. We're still finalizing the packaging, and we'll update our documentation,changelog, and notify users as soon as we have final pricing and long before we start charging. Email Routing limits will remain unchanged.

### What’s next

Email is core to your application today, and it's becoming essential for the next generation of AI agents, background tasks, and automated workflows. We built the Cloudflare Email Service to be the engine for this new era of applications, we’ll be making it available in private beta this November.

* Interested in Email Sending?Sign up to the waitlist here.
* Want to start processing inbound emails? Get started withEmail Routing, which is available now, remains free and will be folded into the new email sending APIs coming.

We’re excited to be adding Email Service to our Developer Platform, and we’re looking forward to seeing how you reimagine user experiences that increasingly rely on emails!

Cloudflare's connectivity cloud protects
entire corporate networks
, helps customers build
Internet-scale applications efficiently
, accelerates any
website or Internet application
,
wards off DDoS attacks
, keeps
hackers at bay
, and can help you on
your journey to Zero Trust
.
Visit
1.1.1.1
 from any device to get started with our free app that makes your Internet faster and safer.
To learn more about our mission to help build a better Internet,
start here
. If you're looking for a new career direction, check out
our open positions
.


Birthday Week
Cloudflare Email Service
