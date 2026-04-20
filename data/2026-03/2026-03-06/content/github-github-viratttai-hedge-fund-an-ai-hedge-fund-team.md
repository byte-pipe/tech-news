---
title: 'GitHub - virattt/ai-hedge-fund: An AI Hedge Fund Team · GitHub'
url: https://github.com/virattt/ai-hedge-fund
site_name: github
content_file: github-github-viratttai-hedge-fund-an-ai-hedge-fund-team
fetched_at: '2026-03-06T11:12:22.581682'
original_url: https://github.com/virattt/ai-hedge-fund
author: virattt
description: An AI Hedge Fund Team. Contribute to virattt/ai-hedge-fund development by creating an account on GitHub.
---

virattt



/

ai-hedge-fund

Public

* NotificationsYou must be signed in to change notification settings
* Fork8.1k
* Star46.2k




 
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

799 Commits
799 Commits
.github/
ISSUE_TEMPLATE
.github/
ISSUE_TEMPLATE
 
 
app
app
 
 
docker
docker
 
 
src
src
 
 
tests
tests
 
 
.dockerignore
.dockerignore
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
poetry.lock
poetry.lock
 
 
pyproject.toml
pyproject.toml
 
 
View all files

## Repository files navigation

# AI Hedge Fund

This is a proof of concept for an AI-powered hedge fund. The goal of this project is to explore the use of AI to make trading decisions. This project is foreducationalpurposes only and is not intended for real trading or investment.

This system employs several agents working together:

1. Aswath Damodaran Agent - The Dean of Valuation, focuses on story, numbers, and disciplined valuation
2. Ben Graham Agent - The godfather of value investing, only buys hidden gems with a margin of safety
3. Bill Ackman Agent - An activist investor, takes bold positions and pushes for change
4. Cathie Wood Agent - The queen of growth investing, believes in the power of innovation and disruption
5. Charlie Munger Agent - Warren Buffett's partner, only buys wonderful businesses at fair prices
6. Michael Burry Agent - The Big Short contrarian who hunts for deep value
7. Mohnish Pabrai Agent - The Dhandho investor, who looks for doubles at low risk
8. Peter Lynch Agent - Practical investor who seeks "ten-baggers" in everyday businesses
9. Phil Fisher Agent - Meticulous growth investor who uses deep "scuttlebutt" research
10. Rakesh Jhunjhunwala Agent - The Big Bull of India
11. Stanley Druckenmiller Agent - Macro legend who hunts for asymmetric opportunities with growth potential
12. Warren Buffett Agent - The oracle of Omaha, seeks wonderful companies at a fair price
13. Valuation Agent - Calculates the intrinsic value of a stock and generates trading signals
14. Sentiment Agent - Analyzes market sentiment and generates trading signals
15. Fundamentals Agent - Analyzes fundamental data and generates trading signals
16. Technicals Agent - Analyzes technical indicators and generates trading signals
17. Risk Manager - Calculates risk metrics and sets position limits
18. Portfolio Manager - Makes final trading decisions and generates orders

Note: the system does not actually make any trades.

## Disclaimer

This project is foreducational and research purposes only.

* Not intended for real trading or investment
* No investment advice or guarantees provided
* Creator assumes no liability for financial losses
* Consult a financial advisor for investment decisions
* Past performance does not indicate future results

By using this software, you agree to use it solely for learning purposes.

## Table of Contents

* How to Install
* How to Run⌨️ Command Line Interface🖥️ Web Application
* ⌨️ Command Line Interface
* 🖥️ Web Application
* How to Contribute
* Feature Requests
* License

## How to Install

Before you can run the AI Hedge Fund, you'll need to install it and set up your API keys. These steps are common to both the full-stack web application and command line interface.

### 1. Clone the Repository

git clone https://github.com/virattt/ai-hedge-fund.git

cd
 ai-hedge-fund

### 2. Set up API keys

Create a.envfile for your API keys:

#
 Create .env file for your API keys (in the root directory)

cp .env.example .env

Open and edit the.envfile to add your API keys:

#
 For running LLMs hosted by openai (gpt-4o, gpt-4o-mini, etc.)

OPENAI_API_KEY=your-openai-api-key

#
 For getting financial data to power the hedge fund

FINANCIAL_DATASETS_API_KEY=your-financial-datasets-api-key

Important: You must set at least one LLM API key (e.g.OPENAI_API_KEY,GROQ_API_KEY,ANTHROPIC_API_KEY, orDEEPSEEK_API_KEY) for the hedge fund to work.

Financial Data: Data for AAPL, GOOGL, MSFT, NVDA, and TSLA is free and does not require an API key. For any other ticker, you will need to set theFINANCIAL_DATASETS_API_KEYin the .env file.

## How to Run

### ⌨️ Command Line Interface

You can run the AI Hedge Fund directly via terminal. This approach offers more granular control and is useful for automation, scripting, and integration purposes.

#### Quick Start

1. Install Poetry (if not already installed):

curl -sSL https://install.python-poetry.org
|
 python3 -

1. Install dependencies:

poetry install

#### Run the AI Hedge Fund

poetry run python src/main.py --ticker AAPL,MSFT,NVDA

You can also specify a--ollamaflag to run the AI hedge fund using local LLMs.

poetry run python src/main.py --ticker AAPL,MSFT,NVDA --ollama

You can optionally specify the start and end dates to make decisions over a specific time period.

poetry run python src/main.py --ticker AAPL,MSFT,NVDA --start-date 2024-01-01 --end-date 2024-03-01

#### Run the Backtester

poetry run python src/backtester.py --ticker AAPL,MSFT,NVDA

Example Output:

Note: The--ollama,--start-date, and--end-dateflags work for the backtester, as well!

### 🖥️ Web Application

The new way to run the AI Hedge Fund is through our web application that provides a user-friendly interface. This is recommended for users who prefer visual interfaces over command line tools.

Please see detailed instructions on how to install and run the web applicationhere.

## How to Contribute

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

Important: Please keep your pull requests small and focused. This will make it easier to review and merge.

## Feature Requests

If you have a feature request, please open anissueand make sure it is tagged withenhancement.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## About

An AI Hedge Fund Team

### Resources

 Readme



### Uh oh!

There was an error while loading.Please reload this page.





Activity


### Stars

46.2k

 stars


### Watchers

574

 watching


### Forks

8.1k

 forks


 Report repository



## Releases

No releases published

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python58.1%
* TypeScript37.7%
* Shell1.8%
* Batchfile1.6%
* CSS0.7%
* Mako0.1%
