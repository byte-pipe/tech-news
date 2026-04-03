---
title: GitHub - OpenBB-finance/OpenBB: Financial data platform for analysts, quants and AI agents.
url: https://github.com/OpenBB-finance/OpenBB
date:
site: github
model: llama3.2:1b
summarized_at: 2026-01-03T11:11:55.082290
screenshot: github-github-openbb-finance-openbb-financial-data-platfo.png
---

# GitHub - OpenBB-finance/OpenBB: Financial data platform for analysts, quants and AI agents.

## Financial Data Platform for Analysts, Quants, and AI Agents
=================================================================

### Overview

OpenBB-finance is a public financial data platform designed specifically for analysts, quants, and AI agents. This platform provides a comprehensive set of tools and APIs to simplify the process of creating technical indicators and trading strategies.

### Key Features

* **Financial Data**: Offers real-time and historical financial data, including stock prices, orders, and trades.
* **Technical Indicators**: Includes a wide range of technical indicators, such as chart patterns and trend lines.
* **Quants and AI Development**: Provides pre-built models and APIs for building custom trading strategies and indicators.
* **Real-Time Data Feeds**: Access to real-time market data for stocks, futures, and forex.

### Use Cases

* **Analysts**: Utilize OpenBB-finance to validate hypothesis, analyze chart patterns, and develop predictive models.
* **Quants**: Employ the platform's tools and APIs to create complex trading strategies and algorithmically backtest ideas.
* **AI Agents**: Leverage OpenBB-finance's data and indicators to build intelligent trading systems that respond to market conditions.

### Example Code

```
import pandas as pd
from openbb import data as obd
from openbb.api import *

# Get historical stock prices for a selected symbol
symbol = 'AAPL'
df = obd.get_historical_candles(symbol, date_range='2y')
print(df)

# Create a technical indicator using the Exponential Moving Average (EMA)
em = EMA('100', df['Close'])
print(em)  # prints the EMA line
```
