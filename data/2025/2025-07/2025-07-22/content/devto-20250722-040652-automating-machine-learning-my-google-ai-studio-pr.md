---
title: 'Automating Machine Learning: My Google AI Studio Project for Code Generation & Model Training - DEV Community'
url: https://dev.to/dthiwanka/automating-machine-learning-my-google-ai-studio-project-for-code-generation-model-training-5a8e
site_name: devto
fetched_at: '2025-07-22T04:06:52.209391'
original_url: https://dev.to/dthiwanka/automating-machine-learning-my-google-ai-studio-project-for-code-generation-model-training-5a8e
author: Dulaj Thiwanka
date: '2025-07-15'
description: 'This post is my submission for DEV Education Track: Build Apps with Google AI Studio. ... Tagged with deved, learngoogleaistudio, ai, gemini.'
tags: '#deved, #learngoogleaistudio, #ai, #gemini'
---

## This post is my submission forDEV Education Track: Build Apps with Google AI Studio.

## What I Built

I set out to build a full-featured Machine Learning Web App that enables users to upload CSV data, perform data exploration, advanced preprocessing, model selection (classification or regression), hyperparameter tuning, evaluation, and auto-generate Python code for deployment also generate components covering CSV upload, target selection, data exploration, preprocessing (outlier handling, datetime extraction, text handling), model and algorithm selectors, hyperparameter tuning, train-test split options, model persistence, evaluation metrics and visualizations, and final code generation.

## Demo

## Screenshot 1 – CSV Upload Section

Users can upload their dataset (CSV) easily with drag-and-drop or file picker, initiating the ML workflow seamlessly.

## Screenshot 2 – Select Target Variable & Column to Predict

Choose the target (dependent) variable for prediction tasks, clearly distinguishing between features and labels for supervised learning.

## Screenshot 3 – Data Exploration Panel

Includes:Dataset Preview (first few rows)

* Summary Statistics (mean, median, standard deviation, min, max)
* Missing Value Detection & Visualization
* Correlation Analysis between numeric variables

## Screenshot 4 – Advanced Preprocessing Options

✔️ Outlier Detection & Handling✔️ Column Type Overrides (force categorical/numeric)✔️ Datetime Feature Extraction (year, month, day, hour splits)✔️ Text Column Handling (basic NLP pre-processing options)✔️ Target Variable Transformation (e.g. log transformation for regression targets)

## Screenshot 5 – Model Type Selector

🔘 Classification🔘 Regression

## Screenshot 6 – Specific Algorithm Selector

* Logistic Regression
* Random Forest Classifier
* Support Vector Machine (SVM)
* Gradient Boosting Classifier
* K-Nearest Neighbours (KNN)
* XGBoost Classifier

## Screenshot 7 – Hyperparameter Tuning Panel

Interactive inputs to grid search or Random Search hyperparameters for the chosen algorithm to improve performance.

## Screenshot 8 – Train/Test Split Options

✔️ Specify Train/Test Split Ratio✔️ Enable Stratified Split (for balanced target class distribution in classification tasks)

## Screenshot 9 – Model Persistence

Option to save the trained model for later inference or deployment.

## Screenshot 10 – Evaluation Options Selector

✔️ Select Classification Metrics (Accuracy, Precision, Recall, F1-Score, AUC, etc.)✔️ Choose Classification Visualizations (Confusion Matrix, ROC Curve, Precision-Recall Curve)

## Screenshot 11 – Auto-generated Python Code

Displays complete, ready-to-run Python code based on all chosen parameters and configurations, enabling:

* Reproducibility
* Deployment readiness
* Educational insight for new ML engineers

🔗Sample Generated Code:View Full Code Snippet

🌐Live Demo:Try the App Here

💻GitHub Repository:csv-to-python-model-generator

⭐Contribute & Improve:Fork the repo, open issues, or start a discussion to enhance this project together!

## 💡Connect with Me

👨‍💻LinkedIn:Dulaj Thiwanka Jayawardena

✉️Email:dulthiwanka2015@gmail.com

## 🚀My Experience

I developed the entire project usingGoogle AI Studio, gaining hands-on experience in Python, machine learning workflows, and integrating multiple advanced data processing features efficiently.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
