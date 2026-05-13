---
title: 'React is Overkill: Why Python + HTMX is Dominating in 2026 - DEV Community'
url: https://dev.to/syedahmershah/react-is-overkill-why-python-htmx-is-dominating-in-2026-17ib
site_name: devto
content_file: devto-react-is-overkill-why-python-htmx-is-dominating-in
fetched_at: '2026-05-13T19:36:40.875110'
original_url: https://dev.to/syedahmershah/react-is-overkill-why-python-htmx-is-dominating-in-2026-17ib
author: Syed Ahmer Shah
date: '2026-05-13'
description: Last year I spent forty minutes setting up a React project for an internal admin dashboard. Just the... Tagged with python, react, javascript, discuss.
tags: '#discuss, #python, #react, #javascript'
---

Boilerplate fatigue and performance gains

Last year I spent forty minutes setting up a React project for an internal admin dashboard. Just the boilerplate. Vite config, ESLint setup, Tailwind integration, React Router, TanStack Query because someone on Twitter said it was the right way to handle server state now. I hadn't written a single line of actual application logic yet and I already had twelve files open.

The dashboard needed to list records from a database, let you filter them, and update a status field. Three things. That's it.

I've been thinking about that moment a lot since then. Not because React was wrong exactly, but because the whole experience made me ask a question I probably should've asked earlier: what problem am I actually solving, and does my stack match that problem?

HTMX has been around since 2020, technically. Carson Gross built it on older ideas — intercooler.js, hypermedia, REST as it was supposed to work. But it's only in the last eighteen months or so that it's started showing up seriously in production codebases beyond hobby projects and blog posts. TheHTMX GitHub repocrossed 40k stars. TheState of JS 2024 surveyshowed a weird but real pattern: developers were increasingly marking "would not use again" next to React while usage stayed high. People are still using it, but the love is clearly cooling at the edges.

What HTMX actually does is conceptually simple enough to explain in one sentence: it lets HTML elements make HTTP requests and swap parts of the page based on the response. That's it. No virtual DOM, no component lifecycle, no client-side routing, no state management library to argue about. You writehx-get="/search"on an input andhx-trigger="keyup changed delay:300ms"and the results div updates. The HTML is the state. The server renders the HTML. You're done.

For a lot of use cases — the boring ones, the productive ones — that's genuinely enough.

Where Python comes in is almost too natural. Django and FastAPI are both excellent at rendering HTML fragments quickly. Django's template engine is underrated. FastAPI with Jinja2 is fast enough that you genuinely don't need to think about it for most traffic levels a small team will ever hit. You return an HTML fragment from your endpoint, HTMX drops it into the DOM, and the user sees something happen. No JSON serialization, no client-side deserialization, no React re-render cycle. The server does what servers are supposed to do: handle the data, decide what the UI should look like, send it down.

Miguel Grinberg wrote a good piece about this pattern inhis Flask-HTMX tutorialsand the core insight is something almost boring: web applications were server-rendered for a decade and a half and it worked fine. The SPA era solved real problems — but it also introduced an enormous amount of accidental complexity for cases that didn't need it.

I want to be fair here because the React discourse tends to go off the rails. React is not bad. React is very good at what it was built for. When you need rich client-side interactivity — collaborative editing, complex real-time interfaces, something like Figma or Notion — the component model, unidirectional data flow, and the client-side rendering approach make sense. The ecosystem is genuinely impressive. Next.js solved real deployment problems. React Server Components, once you get past the initial confusion about what they even are, are a real architectural idea worth understanding.

But most applications aren't Figma. Most applications are CRUD with some filtering. Most internal tools are forms, tables, and dashboards. Most freelance projects are e-commerce sites and appointment booking systems. And for all of those, the React stack asks you to carry a lot of weight that delivers nothing to your end users.

The JavaScript fatigue conversation has been happening for a long time —this 2016 post by Jose Aguinagawas funny eight years ago because it was accurate. The irony is it's somehow still accurate in 2026, just with different library names. Bundlers changed. State management evolved from Redux to Zustand to Jotai to whatever came after that. Server components got added to React in a way that made half the existing tutorials wrong. The amount of meta-knowledge required to set up a React project correctly — not even write application logic, just set it up — is genuinely unreasonable for a lot of teams.

Here's where I want to talk about something that doesn't get said enough in these discussions, which is the South Asian developer context specifically.

A lot of the conversation about frontend frameworks happens in the frame of a US/European developer with fast internet, a high-spec machine, and a client who doesn't care about performance as long as it looks modern. That context shapes the defaults. When Vercel or Netlify blog posts talk about bundle sizes and Core Web Vitals, they're often writing for an audience where a 300kb JS bundle is a minor annoyance. In Pakistan — Karachi, Lahore, Hyderabad, smaller cities — that's not a minor annoyance. Users on mobile data in Tier-2 cities are waiting for your SPA to hydrate and it shows.

Freelancers here mostly work on Upwork and Fiverr. A lot of the gigs are admin dashboards for small businesses, HR tools for local companies, basic inventory management systems. The budgets are not large. The timelines are tight. When a Pakistani developer can ship a fully functional admin panel with Django + HTMX in two or three days because there's no API layer to design, no client-side state to manage, no authentication token flow to wire up separately — that is a real, material productivity advantage.

I've talked to a few people doing final year university projects at HITEC, COMSATS, and similar universities around Sindh and Punjab. The React stack honestly overwhelms students who are still figuring out async/await. Watching someone understand HTMX in an afternoon and ship something that works by evening — that's not a small thing. There's something to be said for a technology that removes barriers to entry without sacrificing capability.

The local SaaS mindset here is also different. When someone in Karachi is building their first B2B software product, they're thinking about getting to paying customers fast, not about whether their architecture will scale to ten million users. Python with Django gives you ORM, admin panel, authentication, and a templating system in one package. Adding HTMX on top means you get reactive UI without the separate frontend deployment, the CORS configuration, the API versioning headache. For a solo founder or a two-person team, that simplicity is worth a lot.

The cases where I'd genuinely choose Python + HTMX are becoming clearer to me over time.

Internal tools are the obvious one. Any time a company needs a dashboard that only ten people use, building a full React SPA is an organizational tax, not a feature. The JavaScript bundle has to be maintained, the frontend dev has to know the API contract, someone has to manage the deployment pipeline. With server-rendered HTML and HTMX, it's just one application. One deploy. The developer who built the data model builds the UI. That's not unsophisticated, that's economical.

Small startups at the idea validation stage. If you're not sure whether your product has legs yet, spending three months building a polished React frontend before you talk to users is a bet you probably shouldn't be making. Django + HTMX lets a Python developer ship something users can click through in days. That's not a forever architecture, but it doesn't need to be.

Content-heavy sites with some interactivity. A blog that has a comment section, a search bar, a newsletter signup. HTMX handles those interactions cleanly. You're not pulling in a frontend framework for three interactive elements.

Where it gets harder is when you actually need rich client-side state. An application where the UI is the product — design tools, real-time collaboration, complex data visualization with local filtering and sorting that needs to feel instant. React and its ecosystem are genuinely better there. That's not a grudging admission, it's just accurate.

There's also the team dynamic angle that people underplay. A lot of teams have backend developers who know Python well and frontend skills that are functional but not deep. The React ecosystem requires either genuine frontend expertise or a willingness to do a lot of cargo-culting patterns from Stack Overflow. Server-side rendering with HTMX plays to Python developers' strengths and doesn't require a separate specialist. In markets where fullstack Python devs are easier to find and cheaper to hire than React developers, that matters organizationally.

Adam Johnson's work on Django + HTMX patternsand theHTMX documentation's own essayson hypermedia are worth reading if you want to understand the philosophy here rather than just the mechanics. The argument isn't "SPAs were a mistake." The argument is closer to: the web platform extended HTML to support interactivity through JavaScript, but maybe it should have extended HTML itself instead. HTMX is a bet on that idea. It's a small, focused library — around 14kb unminified — and it's deliberately unambitious in scope. It does one thing and expects HTML and HTTP to do the rest.

I keep coming back to something that's hard to articulate but feels important. There's a certain developer experience that React optimizes for — the experience of a developer inside the component, thinking in terms of state and props and effects. It's a powerful mental model once you internalize it. But it's a mental model you have to fully commit to, and it pulls a lot of complexity in with it.

HTMX optimizes for a different experience — the experience of building something where the server is in control and the browser is just displaying what the server says. That's a much older model. It maps onto how people actually think about data and business logic, which lives on the server. For a lot of developers, particularly those whose real expertise is in data, backend systems, and APIs, that model is more natural and requires less context-switching.

Neither of these is objectively better. They're suited to different problems, different teams, and different moments in a product's life.

What feels true in 2026, though, is that HTMX has earned its place in the conversation as a serious option for production work. It's not a protest against modern tooling. It's not nostalgia for PHP spaghetti. It's a genuine approach to building web interfaces that works well for a specific, large, and underserved category of application. The category that most of us are actually building most of the time.

I rebuilt that admin dashboard eventually. Three days with FastAPI, Jinja2 templates, and HTMX. No build step. No node_modules folder the size of a small country. Every developer on the backend team could read and modify the templates without learning a new paradigm.

It's still running. Nobody has asked me to rewrite it in React.

If you want to dig into the actual mechanics, theHTMX documentationis genuinely well-written and surprisingly short. For the Python side,full-stack-fastapi-templateis a good starting point even if you swap out the React frontend for Jinja2. Andthis talk by Carson Gross at DjangoCon 2022is the most coherent thirty minutes you'll spend understanding what HTMX is actually trying to do.

## Connect With the Author

Platform

Link

✍️ Medium

@syedahmershah

💬 Dev.to

@syedahmershah

🧠 Hashnode

@syedahmershah

💻 GitHub

@ahmershahdev

🔗 LinkedIn

Syed Ahmer Shah

🧭 Beacons

Syed Ahmer Shah

🌐 Portfolio

ahmershah.dev

 Create template
 

Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (44 comments)
 

Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse