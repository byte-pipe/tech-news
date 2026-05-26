---
title: 'GitHub - Open-Dev-Society/OpenStock: OpenStock is an open-source alternative to expensive market platforms. Track real-time prices, set personalized alerts, and explore detailed company insights — built openly, for everyone, forever free. · GitHub'
url: https://github.com/Open-Dev-Society/OpenStock
site_name: github
content_file: github-github-open-dev-societyopenstock-openstock-is-an-o
fetched_at: '2026-05-26T19:41:28.138921'
original_url: https://github.com/Open-Dev-Society/OpenStock
author: Open-Dev-Society
description: OpenStock is an open-source alternative to expensive market platforms. Track real-time prices, set personalized alerts, and explore detailed company insights — built openly, for everyone, forever free. - Open-Dev-Society/OpenStock
---

Open-Dev-Society

 

/

OpenStock

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork1.6k
* Star12k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

124 Commits
124 Commits
.github
.github
 
 
.idea
.idea
 
 
__tests__
__tests__
 
 
app
app
 
 
components
components
 
 
database
database
 
 
hooks
hooks
 
 
lib
lib
 
 
middleware
middleware
 
 
public/
assets
public/
assets
 
 
scripts
scripts
 
 
types
types
 
 
.gitignore
.gitignore
 
 
API_DOCS.md
API_DOCS.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
components.json
components.json
 
 
docker-compose.yml
docker-compose.yml
 
 
eslint.config.mjs
eslint.config.mjs
 
 
next.config.ts
next.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
postcss.config.mjs
postcss.config.mjs
 
 
tsconfig.json
tsconfig.json
 
 
vitest.config.ts
vitest.config.ts
 
 
View all files

## Repository files navigation

 Checkout new amazing projects also, 
OpenReadme 
 is live

 © Open Dev Society. This project is licensed under AGPL-3.0; if you modify, redistribute, or deploy it (including as a web service), you must release your source code under the same license and credit the original authors.
 

# OpenStock

OpenStock is an open-source alternative to expensive market platforms. Track real-time prices, set personalized alerts, and explore detailed company insights — built openly, for everyone, forever free.

Note: OpenStock is community-built and not a brokerage. Market data may be delayed based on provider rules and your configuration. Nothing here is financial advice.

## 📋 Table of Contents

1. ✨Introduction
2. 🌍Open Dev Society Manifesto
3. ⚙️Tech Stack
4. 🔋Features
5. 🤸Quick Start
6. 🐳Docker Setup
7. 🔐Environment Variables
8. 🧱Project Structure
9. 📡Data & Integrations
10. 🧪Scripts & Tooling
11. 🤝Contributing
12. 🛡️Security
13. 📜License
14. 🙏Acknowledgements

## ✨ Introduction

OpenStock is a modern stock market app powered by Next.js (App Router), shadcn/ui and Tailwind CSS, Better Auth for authentication, MongoDB for persistence, Finnhub for market data, and TradingView widgets for charts and market views.

## 🌍 Open Dev Society Manifesto

We live in a world where knowledge is hidden behind paywalls. Where tools are locked in subscriptions. Where information is twisted by bias. Where newcomers are told they’re not “good enough” to build.

We believe there’s a better way.

* Our Belief: Technology should belong to everyone. Knowledge should be open, free, and accessible. Communities should welcome newcomers with trust, not gatekeeping.
* Our Mission: Build free, open-source projects that make a real difference:Tools that professionals and students can use without barriers.Knowledge platforms where learning is free, forever.Communities where every beginner is guided, not judged.Resources that run on trust, not profit.
* Tools that professionals and students can use without barriers.
* Knowledge platforms where learning is free, forever.
* Communities where every beginner is guided, not judged.
* Resources that run on trust, not profit.
* Our Promise: We will never lock knowledge. We will never charge for access. We will never trade trust for money. We run on transparency, donations, and the strength of our community.
* Our Call: If you’ve ever felt you didn’t belong, struggled to find free resources, or wanted to build something meaningful — you belong here.

Because the future belongs to those who build it openly.

## ⚙️ Tech Stack

Core

* Next.js 15 (App Router), React 19
* TypeScript
* Tailwind CSS v4 (via @tailwindcss/postcss)
* shadcn/ui + Radix UI primitives
* Lucide icons

Auth & Data

* Better Auth (email/password) with MongoDB adapter
* MongoDB + Mongoose
* Finnhub API for symbols, profiles, and market news
* TradingView embeddable widgets

Automation & Comms

* Inngest (events, cron, AI inference via Gemini)
* Nodemailer (Gmail transport)
* next-themes, cmdk (command palette), react-hook-form

Language composition

* TypeScript (~93.4%), CSS (~6%), JavaScript (~0.6%)

## 🔋 Features

* AuthenticationEmail/password auth with Better Auth + MongoDB adapterProtected routes enforced via Next.js middleware
* Email/password auth with Better Auth + MongoDB adapter
* Protected routes enforced via Next.js middleware
* Global search and Command + K paletteFast stock search backed by FinnhubPopular stocks when idle; debounced querying
* Fast stock search backed by Finnhub
* Popular stocks when idle; debounced querying
* WatchlistPer-user watchlist stored in MongoDB (unique symbol per user)
* Per-user watchlist stored in MongoDB (unique symbol per user)
* Stock detailsTradingView symbol info, candlestick/advanced charts, baseline, technicalsCompany profile and financials widgetsOptional cross-source sentiment insights for Reddit, X.com, news, and Polymarket
* TradingView symbol info, candlestick/advanced charts, baseline, technicals
* Company profile and financials widgets
* Optional cross-source sentiment insights for Reddit, X.com, news, and Polymarket
* Market overviewHeatmap, quotes, and top stories (TradingView widgets)
* Heatmap, quotes, and top stories (TradingView widgets)
* Personalized onboardingCollects country, investment goals, risk tolerance, preferred industry
* Collects country, investment goals, risk tolerance, preferred industry
* Email & automationAI-personalized welcome email (Gemini via Inngest)Daily news summary emails (cron) personalized using user watchlists
* AI-personalized welcome email (Gemini via Inngest)
* Daily news summary emails (cron) personalized using user watchlists
* Polished UIshadcn/ui components, Radix primitives, Tailwind v4 design tokensDark theme by default
* shadcn/ui components, Radix primitives, Tailwind v4 design tokens
* Dark theme by default
* Keyboard shortcutCmd/Ctrl + K for quick actions/search
* Cmd/Ctrl + K for quick actions/search

## 🤸 Quick Start

Prerequisites

* Node.js 20+ and pnpm or npm
* MongoDB connection string (MongoDB Atlas or local via Docker Compose)
* Finnhub API key (free tier supported; real-time may require paid)
* Gmail account for email (or update Nodemailer transport)
* Optional: Google Gemini API key (for AI-generated welcome intros)

Clone and install

git clone https://github.com/Open-Dev-Society/OpenStock.git

cd
 OpenStock

#
 choose one:

pnpm install

#
 or

npm install

Configure environment

* Create a.envfile (seeEnvironment Variables).
* Verify DB connectivity:

pnpm test:db

#
 or

npm run test:db

Run development

#
 Next.js dev (Turbopack)

pnpm dev

#
 or

npm run dev

Run Inngest locally (workflows, cron, AI)

npx inngest-cli@latest dev

Build & start (production)

pnpm build 
&&
 pnpm start

#
 or

npm run build 
&&
 npm start

Openhttp://localhost:3000to view the app.

## 🐳 Docker Setup

You can run OpenStock and MongoDB easily with Docker Compose.

1. Ensure Docker and Docker Compose are installed.
2. docker-compose.yml includes two services:

* openstock (this app)
* mongodb (MongoDB database with a persistent volume)

1. Create your.env(see examples below). For the Docker setup, use a local connection string like:

MONGODB_URI
=
mongodb://root:example@mongodb:27017/openstock?authSource=admin

1. Start the stack:

#
 from the repository root

docker compose up -d mongodb 
&&
 docker compose up -d --build

1. Access the app:

* App:http://localhost:3000
* MongoDB is available inside the Docker network at host mongodb:27017

Notes

* The app service depends_on the mongodb service.
* Credentials are defined in Compose for the MongoDB root user; authSource=admin is required on the connection string for root.
* Data persists across restarts via the docker volume.

Optional: Example MongoDB service definition used in this project:

services
:
 
mongodb
:
 
image
: 
mongo:7

 
container_name
: 
mongodb

 
restart
: 
unless-stopped

 
environment
:
 
MONGO_INITDB_ROOT_USERNAME
: 
root

 
MONGO_INITDB_ROOT_PASSWORD
: 
example

 
ports
:
 - 
"
27017:27017
"

 
volumes
:
 - 
mongo-data:/data/db

 
healthcheck
:
 
test
: 
["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]

 
interval
: 
10s

 
timeout
: 
5s

 
retries
: 
5

volumes
:
 
mongo-data
:

## 🔐 Environment Variables

Create.envat the project root. Choose either a hosted MongoDB (Atlas) URI or the local Docker URI.

Hosted (MongoDB Atlas):

#
 Core

NODE_ENV
=
development

#
 Database (Atlas)

MONGODB_URI
=
mongodb+srv://<user>:<pass>@<cluster>/<db>?retryWrites=true&w=majority

#
 Better Auth

BETTER_AUTH_SECRET
=
your_better_auth_secret

BETTER_AUTH_URL
=
http://localhost:3000

#
 Finnhub

#
 Note: NEXT_PUBLIC_FINNHUB_API_KEY is required for Vercel deployment

NEXT_PUBLIC_FINNHUB_API_KEY
=
your_finnhub_key

FINNHUB_BASE_URL
=
https://finnhub.io/api/v1

#
 Sentiment insights (optional)

ADANOS_API_KEY
=
your_adanos_api_key

#
 ADANOS_API_BASE_URL=https://api.adanos.org

#
 AI Provider (optional, default: "gemini")

#
 Supported: "gemini", "minimax", "siray"

#
 AI_PROVIDER=gemini

#
 Gemini

GEMINI_API_KEY
=
your_gemini_api_key

#
 MiniMax (optional, used when AI_PROVIDER=minimax or as fallback)

#
 Get your key at https://platform.minimaxi.com

#
 MINIMAX_API_KEY=your_minimax_api_key

#
 Inngest Signing Key (required for Vercel deployment)

#
 Get this from your Inngest dashboard: https://app.inngest.com/env/settings/keys

INNGEST_SIGNING_KEY
=
your_inngest_signing_key

#
 Email (Nodemailer via Gmail; consider App Passwords if 2FA)

NODEMAILER_EMAIL
=
youraddress@gmail.com

NODEMAILER_PASSWORD
=
your_gmail_app_password

Local (Docker Compose) MongoDB:

#
 Core

NODE_ENV
=
development

#
 Database (Docker)

MONGODB_URI
=
mongodb://root:example@mongodb:27017/openstock?authSource=admin

#
 Better Auth

BETTER_AUTH_SECRET
=
your_better_auth_secret

BETTER_AUTH_URL
=
http://localhost:3000

#
 Finnhub

#
 Note: NEXT_PUBLIC_FINNHUB_API_KEY is required for Vercel deployment

NEXT_PUBLIC_FINNHUB_API_KEY
=
your_finnhub_key

FINNHUB_BASE_URL
=
https://finnhub.io/api/v1

#
 Sentiment insights (optional)

ADANOS_API_KEY
=
your_adanos_api_key

#
 ADANOS_API_BASE_URL=https://api.adanos.org

#
 AI Provider (optional, default: "gemini")

#
 Supported: "gemini", "minimax", "siray"

#
 AI_PROVIDER=gemini

#
 Gemini

GEMINI_API_KEY
=
your_gemini_api_key

#
 MiniMax (optional, used when AI_PROVIDER=minimax or as fallback)

#
 Get your key at https://platform.minimaxi.com

#
 MINIMAX_API_KEY=your_minimax_api_key

#
 Inngest Signing Key (required for Vercel deployment)

#
 Get this from your Inngest dashboard: https://app.inngest.com/env/settings/keys

INNGEST_SIGNING_KEY
=
your_inngest_signing_key

#
 Email (Nodemailer via Gmail; consider App Passwords if 2FA)

NODEMAILER_EMAIL
=
youraddress@gmail.com

NODEMAILER_PASSWORD
=
your_gmail_app_password

Notes

* Keep private keys server-side whenever possible.
* If usingNEXT_PUBLIC_variables, remember they are exposed to the browser.
* In production, prefer a dedicated SMTP provider over a personal Gmail.
* Do not hardcode secrets in the Dockerfile; use.envand Compose.

## 🧱 Project Structure

app/
 (auth)/
 layout.tsx
 sign-in/page.tsx
 sign-up/page.tsx
 (root)/
 layout.tsx
 page.tsx
 help/page.tsx
 stocks/[symbol]/page.tsx
 api/inngest/route.ts
 globals.css
 layout.tsx
components/
 ui/… # shadcn/radix primitives (button, dialog, command, input, etc.)
 forms/… # InputField, SelectField, CountrySelectField, FooterLink
 Header.tsx, Footer.tsx, SearchCommand.tsx, WatchlistButton.tsx, …
database/
 models/watchlist.model.ts
 mongoose.ts
lib/
 actions/… # server actions (auth, finnhub, user, watchlist)
 better-auth/…
 inngest/… # client, functions, prompts
 nodemailer/… # transporter, email templates
 constants.ts, utils.ts
scripts/
 test-db.mjs
types/
 global.d.ts
next.config.ts # i.ibb.co image domain allowlist
postcss.config.mjs # Tailwind v4 postcss setup
components.json # shadcn config
public/assets/images/ # logos and screenshots

## 📡 Data & Integrations

* FinnhubStock search, company profiles, and market news.SetNEXT_PUBLIC_FINNHUB_API_KEYandFINNHUB_BASE_URL(default:https://finnhub.io/api/v1).Free tiers may return delayed quotes; respect rate limits and terms.
* Stock search, company profiles, and market news.
* SetNEXT_PUBLIC_FINNHUB_API_KEYandFINNHUB_BASE_URL(default:https://finnhub.io/api/v1).
* Free tiers may return delayed quotes; respect rate limits and terms.
* Adanos sentiment insights (optional)Structured stock sentiment snapshots across Reddit, X.com, news, and Polymarket.SetADANOS_API_KEY; optionally override the API host withADANOS_API_BASE_URL.Used only for the stock detail sentiment card and does not replace Finnhub or TradingView.
* Structured stock sentiment snapshots across Reddit, X.com, news, and Polymarket.
* SetADANOS_API_KEY; optionally override the API host withADANOS_API_BASE_URL.
* Used only for the stock detail sentiment card and does not replace Finnhub or TradingView.
* TradingViewEmbeddable widgets used for charts, heatmap, quotes, and timelines.External images fromi.ibb.coare allowlisted innext.config.ts.
* Embeddable widgets used for charts, heatmap, quotes, and timelines.
* External images fromi.ibb.coare allowlisted innext.config.ts.
* Better Auth + MongoDBEmail/password with MongoDB adapter.Session validation via middleware; most routes are protected, with public exceptions forsign-in,sign-up, assets and Next internals.
* Email/password with MongoDB adapter.
* Session validation via middleware; most routes are protected, with public exceptions forsign-in,sign-up, assets and Next internals.
* InngestWorkflows:app/user.created→ AI-personalized Welcome EmailCron0 12 * * *→ Daily News Summary per userLocal dev:npx inngest-cli@latest dev.
* Workflows:app/user.created→ AI-personalized Welcome EmailCron0 12 * * *→ Daily News Summary per user
* app/user.created→ AI-personalized Welcome Email
* Cron0 12 * * *→ Daily News Summary per user
* Local dev:npx inngest-cli@latest dev.
* Email (Nodemailer)Gmail transport. Update credentials or switch to your SMTP provider.Templates for welcome and news summary emails.
* Gmail transport. Update credentials or switch to your SMTP provider.
* Templates for welcome and news summary emails.

## 🧪 Scripts & Tooling

Package scripts

* dev: Next.js dev server with Turbopack
* build: Production build (Turbopack)
* start: Run production server
* lint: ESLint
* test:db: Validate DB connectivity

Developer experience

* TypeScript strict mode
* Tailwind CSS v4 (no separate tailwind.config needed)
* shadcn/ui components with Radix primitives
* cmdk command palette, next-themes, lucide-react icons

## 🤝 Contributing

You belong here. Whether you’re a student, a self-taught dev, or a seasoned engineer — contributions are welcome.

* Open an issue to discuss ideas and bugs
* Look for “good first issue” or “help wanted”
* Keep PRs focused; add screenshots for UI changes
* Be kind, guide beginners, no gatekeeping — that’s the ODS way

## 🛡️ Security

If you discover a vulnerability:

* Do not open a public issue
* Email:opendevsociety@cc.cc
* We'll coordinate responsible disclosure and patch swiftly

## 📜 License

OpenStock is and will remain free and open for everyone. This project is licensed under the AGPL-3.0 License - see the LICENSE file for details.

## 🙏 Acknowledgements

* Finnhub for accessible market data
* TradingView for embeddable market widgets
* shadcn/ui, Radix UI, Tailwind CSS, Next.js community
* Inngest for dependable background jobs and workflows
* Better Auth for simple and secure authentication
* All contributors who make open tools possible

— Built openly, for everyone, forever free. Open Dev Society.

© Open Dev Society. This project is licensed under AGPL-3.0; if you modify, redistribute, or deploy it (including as a web service), you must release your source code under the same license and credit the original authors.

## Our Honourable Contributors

* ravixalgorithm- Developed the entire application from the ground up, including authentication, UI design, API and AI integration, and deployment.
* Priyanshuu00007- Created the official OpenStock logo and contributed to the project’s visual identity.
* chinnsenn- Set up Docker configuration for the repository, ensuring a smooth development and deployment process.
* koevoet1221- Resolved MongoDB Docker build issues, improving the project’s overall stability and reliability.
* ettoreciolli1- updated Readme

## ❤️ Partners & Backers

Siray.ai— The robust AI infrastructure backing OpenStock. Siray.ai ensures our market insights never sleep.

## Special thanks

Huge thanks toAdrian Hajdin (JavaScript Mastery)— his excellent Stock Market App tutorial was instrumental in building OpenStock for the open-source community under the Open Dev Society.

GitHub:adrianhajdinYouTube tutorial:Stock Market App TutorialYouTube channel:JavaScript Mastery

## About

OpenStock is an open-source alternative to expensive market platforms. Track real-time prices, set personalized alerts, and explore detailed company insights — built openly, for everyone, forever free.

openstock-ods.vercel.app

### Topics

 nextjs

 stock-market

 tailwindcss

 inngest

 shadcn-ui

 coderabbit

### Resources

 Readme

 

### License

 AGPL-3.0 license
 

### Contributing

 Contributing
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

12k

 stars
 

### Watchers

78

 watching
 

### Forks

1.6k

 forks
 

 Report repository

 

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 
* buymeacoffee.com/ravixalgorithm

Learn more about GitHub Sponsors

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript91.7%
* JavaScript4.5%
* CSS3.6%
* Dockerfile0.2%