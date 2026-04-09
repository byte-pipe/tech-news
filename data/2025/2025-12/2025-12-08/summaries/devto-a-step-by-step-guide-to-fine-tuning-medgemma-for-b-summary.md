---
title: A step-by-step guide to fine-tuning MedGemma for breast tumor classification - DEV Community
url: https://dev.to/googleai/a-step-by-step-guide-to-fine-tuning-medgemma-for-breast-tumor-classification-35af
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-08T11:16:56.674093
screenshot: devto-a-step-by-step-guide-to-fine-tuning-medgemma-for-b.png
---

# A step-by-step guide to fine-tuning MedGemma for breast tumor classification - DEV Community

**Fine-tuning MedGemma for Breast Tumor Classification**
======================================================

**Introduction**
---------------

This guide will walk you through the first step in fine-tuning Google's MedGemma model for breast tumor classification. MedGemma is a powerful family of open models developed by Google, used for classifying microscope images of breast tissue into one of eight categories: four benign (non-cancerous) and four malignant (cancerous).

**Step-by-Step Fine-tuning Process**
-----------------------------------

### 1. Setting the stage

* We'll use MedGemma's full precision model to achieve optimal performance.
* Quantizing the model may be a more cost-effective approach if compute costs are a concern.

### 2. Loading and Preparing Data

* Load your dataset of microscope images of breast tissue into Python.
* Prepare the data by resizing and normalizing it.

### 3. Configuring Fine-tuning Environment

* Create a new notebook for fine-tuning using Finetune Notebook (available at [www.medgemma.dev](http://www.medgemma.dev)).
* Install required libraries and setup necessary environment variables.

```bash
!pip install -u medgemma pytorch torchvision sklearn
```

### 4. Fine-tuning Model

* Use the Finetune Notebook provided by MedGemma to fine-tune your model.
* Integrate key insights from the walkthrough, including data type choices that contributed to improved performance.

**Key Takeaways:**
- Fine-tuning requires experimentation and patience during the development process.
- Understanding the strengths and limitations of MedGemma models is essential for optimal performance.
- Keep an eye on monitor progress while modifying fine-tune parameters and consider utilizing different approaches, such as model pruning or knowledge distillation.

Note that the guide proceeds to suggest moving towards a production-ready environment using Cloud Run jobs in the next step:

**Next Steps**
---------------

In our future post, we'll showcase how to scale up this workflow to a production-ready environment with Cloud Run.
