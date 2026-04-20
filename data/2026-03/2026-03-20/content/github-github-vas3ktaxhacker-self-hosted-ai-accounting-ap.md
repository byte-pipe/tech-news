---
title: 'GitHub - vas3k/TaxHacker: Self-hosted AI accounting app. LLM analyzer for receipts, invoices, transactions with custom prompts and categories · GitHub'
url: https://github.com/vas3k/TaxHacker
site_name: github
content_file: github-github-vas3ktaxhacker-self-hosted-ai-accounting-ap
fetched_at: '2026-03-20T11:14:36.516233'
original_url: https://github.com/vas3k/TaxHacker
author: vas3k
description: Self-hosted AI accounting app. LLM analyzer for receipts, invoices, transactions with custom prompts and categories - vas3k/TaxHacker
---

vas3k



/

TaxHacker

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork235
* Star1.6k




 
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

142 Commits
142 Commits
.github
.github
 
 
ai
ai
 
 
app
app
 
 
components
components
 
 
docs
docs
 
 
etc/
nginx
etc/
nginx
 
 
forms
forms
 
 
hooks
hooks
 
 
lib
lib
 
 
models
models
 
 
prisma
prisma
 
 
public
public
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
.prettierrc
.prettierrc
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
components.json
components.json
 
 
docker-compose.build.yml
docker-compose.build.yml
 
 
docker-compose.production.yml
docker-compose.production.yml
 
 
docker-compose.yml
docker-compose.yml
 
 
docker-entrypoint.sh
docker-entrypoint.sh
 
 
eslint.config.mjs
eslint.config.mjs
 
 
instrumentation-client.ts
instrumentation-client.ts
 
 
instrumentation.ts
instrumentation.ts
 
 
middleware.ts
middleware.ts
 
 
next.config.ts
next.config.ts
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
postcss.config.mjs
postcss.config.mjs
 
 
sentry.edge.config.ts
sentry.edge.config.ts
 
 
sentry.server.config.ts
sentry.server.config.ts
 
 
tailwind.config.ts
tailwind.config.ts
 
 
tsconfig.json
tsconfig.json
 
 
View all files

## Repository files navigation

# TaxHacker — self-hosted AI accountant

TaxHacker is a self-hosted accounting app designed for freelancers, indie hackers, and small businesses who want to save time and automate expense and income tracking using the power of modern AI.

Upload photos of receipts, invoices, or PDFs, and TaxHacker will automatically recognize and extract all the important data you need for accounting: product names, amounts, items, dates, merchants, taxes, and save it into a structured Excel-like database. You can even create custom fields with your own AI prompts to extract any specific information you need.

The app features automatic currency conversion (including crypto!) based on historical exchange rates from the transaction date. With built-in filtering, multi-project support, import/export capabilities, and custom categories, TaxHacker simplifies reporting and makes tax filing a bit easier.

🎥Watch demo video

Important

This project is still in early development. Use at your own risk!Star usto get notified about new features and bugfixes ⭐️

## ✨ Features

### 1Analyze photos and invoices with AI

Snap a photo of any receipt or upload an invoice PDF, and TaxHacker will automatically recognize, extract, categorize, and store all the information in a structured database.

* Upload and organize your docs: Store multiple documents in "unsorted" until you're ready to process them manually or with AI assistance
* AI data extraction: Use AI to automatically pull key information like dates, amounts, vendors, and line items
* Auto-categorization: Transactions are automatically sorted into relevant categories based on their content
* Item splitting: Extract individual items from invoices and split them into separate transactions when needed
* Structured storage: Everything gets saved in an organized database for easy filtering and retrieval
* Customizable AI providers: Choose from OpenAI, Google Gemini, or Mistral (local LLM support coming soon)

TaxHacker works with a wide variety of documents, including store receipts, restaurant bills, invoices, bank statements, letters, even handwritten receipts. It handles any language and any currency with ease.

### 2Multi-currency support with automatic conversion (even crypto!)

TaxHacker automatically detects currencies in your documents and converts them to your base currency using historical exchange rates.

* Foreight currency detection: Automatically identify the currency used in any document
* Historical rates: Get conversion rates from the actual transaction date
* All-world coverage: Support for 170+ world currencies and 14 popular cryptocurrencies (BTC, ETH, LTC, DOT, and more)
* Flexible input: Manual entry is always available when you need more control

### 3Organize your transactions using fully customizable categories, projects and fields

Adapt TaxHacker to your unique needs with unlimited customization options. Create custom fields, projects, and categories that better suit your specific needs, idustry standards or country.

* Custom categories and projecst: Create your own categories and projects to group your transactions in any convenient way
* Custom fields: You can create unlimited number of custom fields to extraxt more information from your invoices (it's like creating extra columns in Excel)
* Full-text search: Search through the actual content of recognized documents
* Advanced filtering: Find exactly what you need with search and filter options
* AI-powered extraction: Write your own prompts to extract any custom information from documents
* Bulk operations: Process multiple documents or transactions at once

### 4Customize any LLM prompt. Even system ones

Take full control of how TaxHacker's AI processes your documents. Write custom AI prompts for fields, categories, and projects, or modify the built-in ones to match your specific needs.

* Customizable system prompts: Modify the general prompt template in settings to suit your business
* Field or project-specific prompts: Create custom extraction rules for your industry-specific documents
* Full control: Adjust field extraction priorities and naming conventions to match your workflow
* Industry optimization: Fine-tune the AI to understand your specific type of business documents
* Full transparency: Every aspect of the AI extraction process is under your control and can be changed right in settings

TaxHacker is 100% adaptable and tunable to your unique requirements — whether you need to extract emails, addresses, project codes, or any other custom information from your documents.

### 5Flexible data filtering and export

Once your documents are processed, easily view, filter, and export your complete transaction history exactly how you need it.

* Advanced filtering: Filter by date ranges, categories, projects, amounts, and any custom fields
* Flexible exports: Export filtered transactions to CSV with all attached documents included
* Tax-ready reports: Generate comprehensive reports for your accountant or tax advisor
* Data portability: Download complete data archives to migrate to other services—your data stays yours

### 6Self-hosted mode for data privacy

Keep complete control over your financial data with local storage and self-hosting options. TaxHacker respects your privacy and gives you full ownership of your information.

* Home server ready: Host on your own infrastructure for maximum privacy and control
* Docker native: Simple setup with provided Docker containers and compose files
* Data ownership: Your financial documents never leaves your control
* No vendor lock-in: Export everything and migrate whenever you want
* Transparent operations: Full access to source code and complete operational transparency

## 🛳 Deployment and Self-hosting

TaxHacker can be easily self-hosted on your own infrastructure for complete control over your data and application environment. We provide aDocker imageandDocker Composesetup that makes deployment simple:

curl -O https://raw.githubusercontent.com/vas3k/TaxHacker/main/docker-compose.yml

docker compose up

The Docker Compose setup includes:

* TaxHacker application container
* PostgreSQL 17 database (or connect to your existing database)
* Automatic database migrations on startup
* Volume mounts for persistent data storage
* Production-ready configuration

New Docker images are automatically built and published with every release. You can use specific version tags (e.g.,v1.0.0) orlatestfor the most recent version.

For advanced setups, you can customize the Docker Compose configuration to fit your infrastructure. The default configuration uses the pre-built image from GitHub Container Registry, but you can also build locally using the providedDockerfile.

Example custom configuration:

services
:

app
:

image
:
ghcr.io/vas3k/taxhacker:latest


ports
:
 -
"
7331:7331
"


environment
:
 -
SELF_HOSTED_MODE=true

 -
UPLOAD_PATH=/app/data/uploads

 -
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/taxhacker


volumes
:
 -
./data:/app/data


restart
:
unless-stopped

### Environment Variables

Configure TaxHacker for your specific needs with these environment variables:

Variable

Required

Description

Example

UPLOAD_PATH

Yes

Local directory for file uploads and storage

./data/uploads

DATABASE_URL

Yes

PostgreSQL connection string

postgresql://user@localhost:5432/taxhacker

PORT

No

Port to run the application on

7331
 (default)

BASE_URL

No

Base URL for the application

http://localhost:7331

SELF_HOSTED_MODE

No

Set to "true" for self-hosting: enables auto-login, custom API keys, and additional features

true

DISABLE_SIGNUP

No

Disable new user registration on your instance

false

BETTER_AUTH_SECRET

Yes

Secret key for authentication (minimum 16 characters)

your-secure-random-key

You can also configure LLM provider settings in the application or via environment variables:

* OpenAI:OPENAI_MODEL_NAMEandOPENAI_API_KEY
* Google Gemini:GOOGLE_MODEL_NAMEandGOOGLE_API_KEY
* Mistral:MISTRAL_MODEL_NAMEandMISTRAL_API_KEY

## ⌨️ Local Development

We use:

* Next.js 15+for the frontend and API
* Prismafor database models and migrations
* PostgreSQLas the database (PostgreSQL 17+ recommended)
* Ghostscript and GraphicsMagickfor PDF processing (install on macOS viabrew install gs graphicsmagick)

Set up your local development environment:

#
 Clone the repository

git clone https://github.com/vas3k/TaxHacker.git

cd
 TaxHacker

#
 Install dependencies

npm install

#
 Set up environment variables

cp .env.example .env

#
 Edit .env with your configuration

#
 Make sure to set DATABASE_URL to your PostgreSQL connection string

#
 Example: postgresql://user@localhost:5432/taxhacker

#
 Initialize the database

npx prisma generate
&&
 npx prisma migrate dev

#
 Start the development server

npm run dev

Visithttp://localhost:7331to see your local TaxHacker instance in action.

For a production build, instead ofnpm run devuse the following commands:

#
 Build the application

npm run build

#
 Start the production server

npm run start

## 🤝 Contributing

We welcome contributions to TaxHacker! Here's how you can help make it even better:

* 🐛 Bug Reports: File detailed issues when you encounter problems
* 💡 Feature Requests: Share your ideas for new features and improvements
* 🔧 Code Contributions: Submit pull requests to improve the application
* 📚 Documentation: Help improve documentation and guides
* 🎥 Content Creation: Videos, tutorials, and reviews help us reach more users!

All development happens on GitHub through issues and pull requests. We appreciate any help.

## ❤️ Support the Project

If TaxHacker has helped you save time or manage your finances better, consider supporting its continued development! Your donations help us maintain the project, add new features, and keep it free and open source. Every contribution helps ensure we can keep improving and maintaining this tool for the community.

## 📄 License

TaxHacker is licensed under theMIT License.

## About

Self-hosted AI accounting app. LLM analyzer for receipts, invoices, transactions with custom prompts and categories

taxhacker.app

### Topics

 invoices

 accounting

 self-hosted

 expenses

 taxes

 currency-exchange

 llm

 llm-apps

 ai-analysis

### Resources

 Readme



### License

 MIT license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

1.6k

 stars


### Watchers

24

 watching


### Forks

235

 forks


 Report repository



## Releases10

v0.6.1

 Latest



Mar 12, 2026



+ 9 releases

## Sponsor this project

### Uh oh!

There was an error while loading.Please reload this page.






* ko-fi.com/vas3k
* https://vas3k.com/donate/
* https://paypal.me/vas3kcom

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors4

* vas3kVasily Zubarev
* H1DArtem Sushchev
* danfimovDmitrii Anfimov
* dependabot[bot]

## Languages

* TypeScript99.2%
* Other0.8%
