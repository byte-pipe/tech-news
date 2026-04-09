---
title: A step-by-step guide to fine-tuning MedGemma for breast tumor classification - DEV Community
url: https://dev.to/googleai/a-step-by-step-guide-to-fine-tuning-medgemma-for-breast-tumor-classification-35af
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-05T11:18:35.772353
screenshot: devto-a-step-by-step-guide-to-fine-tuning-medgemma-for-b.png
---

# A step-by-step guide to fine-tuning MedGemma for breast tumor classification - DEV Community

### Fine-Tuning MedGemma for Breast Tumor Classification

**Disclaimer**: This guide provides information and educational purposes only and is not intended to be a substitute for professional medical advice, diagnosis, or treatment. It highlights the performance benchmarks of MedGemma but does not directly inform clinical diagnosis, patient management decisions, treatment recommendations.

To fine-tune the Gemma 3 variant MedGemma for breast tumor classification, follow these steps:

#### Step 1: Install and Prepare Finetune Notebook
Use the Finetune Notebook to fine-tune the pre-configured MedGemma model. The notebook provides all necessary code and a step-by-step explanation of the process.

### Key Insights

*   Critical choice in data types impacted performance significantly.
*   Quantization used for compute cost reduction.

#### Step 2: Fine-Tune Model
Fine-tune the MedGemma model to optimize its performance for breast tumor classification. This involves adjusting various hyperparameters and training parameters as needed.

**Output (in Markdown format)**

## Setting the Stage
Our goal is to classify microscope images of breast tissue into one of eight categories: four benign (non-cancerous) and four malignant (cancerous). This type of classification represents crucial tasks that pathologists perform in order to make an accurate diagnosis.

### Model Overview
We'll be using MedGemma, a powerful family of open models from Google built on the same research technology as Gemini models. What makes MedGemma special is that it's been specifically tuned for medical applications.

## Fine-Tuning Process

#### Step 1: Prepare Finetune Notebook
Use the Finetune Notebook to fine-tune the pre-configured MedGemma model.

### Key Takeaways

*   The first step in fine-tuning MedGemma involves using the Finetune Notebook.
