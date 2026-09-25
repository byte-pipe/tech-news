---
title: GitHub - shy3130/tick-stock-panel: TSP自托管、零运维的 A 股「选股 + 监控 + 回测」量化工作台 | LLM能力驱使策略定制+个股分析+复盘 | 自由接入第三方数据源与个性化扩展数据 | 个人开源 · GitHub
url: https://github.com/shy3130/tick-stock-panel
date: 
site: github
model: llama3.2:1b
summarized_at: 2026-09-25T15:49:20.958756
---

# GitHub - shy3130/tick-stock-panel: TSP自托管、零运维的 A 股「选股 + 监控 + 回测」量化工作台 | LLM能力驱使策略定制+个股分析+复盘 | 自由接入第三方数据源与个性化扩展数据 | 个人开源 · GitHub

# GitHub Repository -.shy3130/tick-stock-panel

## Purpose
The purpose of this repository is to provide a self-hosted, Zero-ops TSP (Stock Prediction System) workbench for high-frequency quantitative trading.

## Features

* **Self-hosted**: A self-hosted version of the repository allows administrators to manage and configure the project without relying on a cloud-based service.
* **Multi-data-source routing**: Supports the routing of 6 different data sources, allowing for dynamic and flexible data analysis.
* **Real-time monitoring**: Monitors market events and adjusts the trading strategy accordingly.
* **AI-powered chat assistant**: Provides real-time answers to questions based on the latest market data.
* **Automated data imports**: Supports the import of data from various sources, including proprietary data feeds and open-source data sources.
* **Customizable**: Allows for customization of the trading strategy and data analysis.

## Key Features

* **TSP Engine**: A proprietary trading engine that uses a combination of machine learning algorithms and expert knowledge to analyze the markets.
* **Risk management**: Built-in risk management features, including position sizing, stop-loss, and maximum drawdown limits.
* **Trade execution**: Automatic trade execution based on the trading strategy and risk management parameters.
* **Trade execution analytics**: Provides detailed analytics and insights into trade performance, including trade execution time, risk, and profit.

## Technical Details

* **Language**: Python 3.x
* **Framework**: Flask
* **Database**: PostgreSQL
* **Containerization**: Docker
* **API**: RESTful API

## Project Structure

* `workflows`: Directory containing workflow definitions for tasks such as data loading, risk management, and trade execution.
* `github`: Directory containing the main project repository.
* `backend`: Directory containing the Python code for the main application logic.
* `backend/docs`: Directory containing documentation for the main application logic.

## Usage

1. Clone the repository using `git clone https://github.com/shy3130/tick-stock-panel.git`.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Configure the project using the `config.json` file.
4. Run the application using `python app.py`.

## Project Requirements

* Python 3.7+
* Flask 2.0+
* PostgreSQL 9.5+
* Docker 1.13+
* Apache Kafka 2.3+

## Project Guidelines

* The repository should be maintained in GitHub.
* The main application code should be located in the `backend` directory.
* Documentation should be generated using Jupyter Notebook.
* Code should be well-organized and following the standard Python style guide.