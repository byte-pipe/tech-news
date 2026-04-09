---
title: A step-by-step guide to fine-tuning MedGemma for breast tumor classification - DEV Community
url: https://dev.to/googleai/a-step-by-step-guide-to-fine-tuning-medgemma-for-breast-tumor-classification-35af
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-04T11:19:19.770427
screenshot: devto-a-step-by-step-guide-to-fine-tuning-medgemma-for-b.png
---

# A step-by-step guide to fine-tuning MedGemma for breast tumor classification - DEV Community

**Fine-Tuning MedGemma for Breast Tumor Classification**

**Introduction**
MedGemma is an open-source family of AI models developed by Google, specifically designed for medical applications such as breast cancer histopathology image classification. This guide aims to walk through the process of fine-tuning a MedGemma model using the Gemma 3 variant, which can achieve high performance in clinical tasks.

**Prerequisites**
This guide assumes that you have:

* A basic understanding of AI and machine learning concepts
* Familiarity with the necessary tools and environments (e.g., Python, Jupyter Notebook)

**Setup Required**

1. Create a new project directory for your code.
2. Install the pre-configured fine-tuning notebook using pip: `pip install -U gendem-finetune-nn`.
3. Clone the MedGemma repository to your project directory.

**Step 1: Finetune Notebook**
The finest tuning notebook provides an exhaustive guide through the process, including code snippets and explanations.
```markdown
# Step 1: Import necessary modules and load pre-trained model
import mediagemma as mg
from finetuning_notebook import MedGemmaFinetuneNode
model = mg.DNNMedGemmaFinetuneNode()
# Load your dataset for classification purposes (e.g., image files)
# ...

# Train model using a custom dataset or loading the pre-trained model (if applicable)
# ...
```
**Step 2: Optimize Model Performance**
To fine-tune the MedGemma model, you may need to experiment on data types and performance settings.
```markdown
# Step 2: Attempt data type optimization (e.g., quantization)
# ...

# Optional: Run in a Cloud Run job for scalability
```
**Step 3: Refine Model Architecture**
Based on the insights from previous steps, identify key decisions that made an optimization possible (e.g., choosing between two options).
```markdown
# Step 3: Implement critical optimization decisions based on prior findings
# ...
```

Note: The above code and instructions are provided as a starting point. It is essential to consult additional resources and official MedGemma documentation for the exact steps, as well as any specific requirements or recommendations for fine-tuning your model.
