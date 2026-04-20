---
title: 'GitHub - TauricResearch/TradingAgents: TradingAgents: Multi-Agents LLM Financial Trading Framework · GitHub'
url: https://github.com/TauricResearch/TradingAgents
site_name: github
content_file: github-github-tauricresearchtradingagents-tradingagents-m
fetched_at: '2026-03-20T11:14:35.329053'
original_url: https://github.com/TauricResearch/TradingAgents
author: TauricResearch
description: 'TradingAgents: Multi-Agents LLM Financial Trading Framework - TauricResearch/TradingAgents'
---

TauricResearch



/

TradingAgents

Public

* NotificationsYou must be signed in to change notification settings
* Fork6.5k
* Star33.5k




 
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

102 Commits
102 Commits
assets
assets
 
 
cli
cli
 
 
tradingagents
tradingagents
 
 
.env.example
.env.example
 
 
.gitignore
.gitignore
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
main.py
main.py
 
 
pyproject.toml
pyproject.toml
 
 
requirements.txt
requirements.txt
 
 
test.py
test.py
 
 
uv.lock
uv.lock
 
 
View all files

## Repository files navigation

Deutsch
 |

Español
 |

français
 |

日本語
 |

한국어
 |

Português
 |

Русский
 |

中文

# TradingAgents: Multi-Agents LLM Financial Trading Framework

## News

* [2026-03]TradingAgents v0.2.1released with GPT-5.4, Gemini 3.1, Claude 4.6 model coverage and improved system stability.
* [2026-02]TradingAgents v0.2.0released with multi-provider LLM support (GPT-5.x, Gemini 3.x, Claude 4.x, Grok 4.x) and improved system architecture.
* [2026-01]Trading-R1Technical Reportreleased, withTerminalexpected to land soon.

🎉TradingAgentsofficially released! We have received numerous inquiries about the work, and we would like to express our thanks for the enthusiasm in our community.

So we decided to fully open-source the framework. Looking forward to building impactful projects with you!

🚀TradingAgents| ⚡Installation & CLI| 🎬Demo| 📦Package Usage| 🤝Contributing| 📄Citation

## TradingAgents Framework

TradingAgents is a multi-agent trading framework that mirrors the dynamics of real-world trading firms. By deploying specialized LLM-powered agents: from fundamental analysts, sentiment experts, and technical analysts, to trader, risk management team, the platform collaboratively evaluates market conditions and informs trading decisions. Moreover, these agents engage in dynamic discussions to pinpoint the optimal strategy.

TradingAgents framework is designed for research purposes. Trading performance may vary based on many factors, including the chosen backbone language models, model temperature, trading periods, the quality of data, and other non-deterministic factors.It is not intended as financial, investment, or trading advice.

Our framework decomposes complex trading tasks into specialized roles. This ensures the system achieves a robust, scalable approach to market analysis and decision-making.

### Analyst Team

* Fundamentals Analyst: Evaluates company financials and performance metrics, identifying intrinsic values and potential red flags.
* Sentiment Analyst: Analyzes social media and public sentiment using sentiment scoring algorithms to gauge short-term market mood.
* News Analyst: Monitors global news and macroeconomic indicators, interpreting the impact of events on market conditions.
* Technical Analyst: Utilizes technical indicators (like MACD and RSI) to detect trading patterns and forecast price movements.

### Researcher Team

* Comprises both bullish and bearish researchers who critically assess the insights provided by the Analyst Team. Through structured debates, they balance potential gains against inherent risks.

### Trader Agent

* Composes reports from the analysts and researchers to make informed trading decisions. It determines the timing and magnitude of trades based on comprehensive market insights.

### Risk Management and Portfolio Manager

* Continuously evaluates portfolio risk by assessing market volatility, liquidity, and other risk factors. The risk management team evaluates and adjusts trading strategies, providing assessment reports to the Portfolio Manager for final decision.
* The Portfolio Manager approves/rejects the transaction proposal. If approved, the order will be sent to the simulated exchange and executed.

## Installation and CLI

### Installation

Clone TradingAgents:

git clone https://github.com/TauricResearch/TradingAgents.git

cd
 TradingAgents

Create a virtual environment in any of your favorite environment managers:

conda create -n tradingagents python=3.13
conda activate tradingagents

Install dependencies:

pip install -r requirements.txt

### Required APIs

TradingAgents supports multiple LLM providers. Set the API key for your chosen provider:

export
 OPENAI_API_KEY=...
#
 OpenAI (GPT)

export
 GOOGLE_API_KEY=...
#
 Google (Gemini)

export
 ANTHROPIC_API_KEY=...
#
 Anthropic (Claude)

export
 XAI_API_KEY=...
#
 xAI (Grok)

export
 OPENROUTER_API_KEY=...
#
 OpenRouter

export
 ALPHA_VANTAGE_API_KEY=...
#
 Alpha Vantage

For local models, configure Ollama withllm_provider: "ollama"in your config.

Alternatively, copy.env.exampleto.envand fill in your keys:

cp .env.example .env

### CLI Usage

You can also try out the CLI directly by running:

python -m cli.main

You will see a screen where you can select your desired tickers, date, LLMs, research depth, etc.

An interface will appear showing results as they load, letting you track the agent's progress as it runs.

## TradingAgents Package

### Implementation Details

We built TradingAgents with LangGraph to ensure flexibility and modularity. The framework supports multiple LLM providers: OpenAI, Google, Anthropic, xAI, OpenRouter, and Ollama.

### Python Usage

To use TradingAgents inside your code, you can import thetradingagentsmodule and initialize aTradingAgentsGraph()object. The.propagate()function will return a decision. You can runmain.py, here's also a quick example:

from

tradingagents
.
graph
.
trading_graph

import

TradingAgentsGraph

from

tradingagents
.
default_config

import

DEFAULT_CONFIG

ta

=

TradingAgentsGraph
(
debug
=
True
,
config
=
DEFAULT_CONFIG
.
copy
())

# forward propagate

_
,
decision

=

ta
.
propagate
(
"NVDA"
,
"2026-01-15"
)

print
(
decision
)

You can also adjust the default configuration to set your own choice of LLMs, debate rounds, etc.

from

tradingagents
.
graph
.
trading_graph

import

TradingAgentsGraph

from

tradingagents
.
default_config

import

DEFAULT_CONFIG

config

=

DEFAULT_CONFIG
.
copy
()

config
[
"llm_provider"
]
=

"openai"

# openai, google, anthropic, xai, openrouter, ollama

config
[
"deep_think_llm"
]
=

"gpt-5.2"

# Model for complex reasoning

config
[
"quick_think_llm"
]
=

"gpt-5-mini"

# Model for quick tasks

config
[
"max_debate_rounds"
]
=

2

ta

=

TradingAgentsGraph
(
debug
=
True
,
config
=
config
)

_
,
decision

=

ta
.
propagate
(
"NVDA"
,
"2026-01-15"
)

print
(
decision
)

Seetradingagents/default_config.pyfor all configuration options.

## Contributing

We welcome contributions from the community! Whether it's fixing a bug, improving documentation, or suggesting a new feature, your input helps make this project better. If you are interested in this line of research, please consider joining our open-source financial AI research communityTauric Research.

## Citation

Please reference our work if you findTradingAgentsprovides you with some help :)

@misc{xiao2025tradingagentsmultiagentsllmfinancial,
 title={TradingAgents: Multi-Agents LLM Financial Trading Framework},
 author={Yijia Xiao and Edward Sun and Di Luo and Wei Wang},
 year={2025},
 eprint={2412.20138},
 archivePrefix={arXiv},
 primaryClass={q-fin.TR},
 url={https://arxiv.org/abs/2412.20138},
}

## About

TradingAgents: Multi-Agents LLM Financial Trading Framework

arxiv.org/pdf/2412.20138

### Topics

 agent

 finance

 trading

 multiagent

 llm

### Resources

 Readme



### License

 Apache-2.0 license


### Uh oh!

There was an error while loading.Please reload this page.





Activity


Custom properties


### Stars

33.5k

 stars


### Watchers

338

 watching


### Forks

6.5k

 forks


 Report repository



## Releases2

TradingAgents v0.2.1

 Latest



Mar 15, 2026



+ 1 release

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.





## Contributors

### Uh oh!

There was an error while loading.Please reload this page.





## Languages

* Python100.0%
