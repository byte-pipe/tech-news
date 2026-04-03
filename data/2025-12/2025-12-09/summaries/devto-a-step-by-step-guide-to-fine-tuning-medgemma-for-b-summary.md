---
title: A step-by-step guide to fine-tuning MedGemma for breast tumor classification - DEV Community
url: https://dev.to/googleai/a-step-by-step-guide-to-fine-tuning-medgemma-for-breast-tumor-classification-35af
date: 2025-12-02
site: devto
model: llama3.2:1b
summarized_at: 2025-12-09T11:17:51.996343
screenshot: devto-a-step-by-step-guide-to-fine-tuning-medgemma-for-b.png
---

# A step-by-step guide to fine-tuning MedGemma for breast tumor classification - DEV Community

**Fine-tuning MedGemma for Breast Cancer Classification**

**Introduction**

This guide is to outline the process of fine-tuning Google's MedGemma model to classify breast cancer histopathology images. MedGemma is an Open Model that can be used for medical tasks such as diagnosing breast cancer.

**Objective**

The goal of this tutorial is to improve the performance of MedGemma on breast cancer classification, specifically to four benign and four malignant categories, by fine-tuning the model in a notebook environment.

**Setting up the Project**

Before we dive into the code, let's set up our project. We will be using the Finetune Notebook to prepare our data for fine-tuning and create an executable Docker image for production-ready environments such as Cloud Run jobs.

### Step 1: Import Libraries and Load Data

Get started by importing essential libraries and loading breast cancer classification datasets from the `sklearn.datasets` module:
```python
import numpy as np
from sklearn.datasets import load_iris, load_breast_cancer
from finetune import make_dataloader

# Load breast cancer dataset
X, y = load_breast_cancer(target_size=10)
```
### Step 2: Preprocess Data

Prepare the data for fine-tuning by scaling features and encoding categorical variables:
```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

preprocessor = StandardScaler()
categorical_transformer = OneHotEncoder dtype=int32, categorical=False)

data = np.array([X])
target = y

# Split data into training and validation sets
train_data, val_data, train_target, val_target = train_test_split(data, target, test_size=0.2, random_state=42)
```

### Step 3: Create a Finetune Model Architecture

Define a MedGemma-based model architecture using PyTorch:
```python
from finetune import MedGemma

# Initialize MedGemma model
model = MedGemma(
    base="path/to/medgememma/model.pt",
    feature_types=["float32", "int32"],
    output_features=[8]  # Number of final outputs (benign/malignant categories)
)

# Define a custom data loader for training and validation sets
dataloader_type = "dask"
batch_size = 16
train_loader, val_loader = dataloader(type=dataloader_type, batch_size=batch_size, dtype=np.float32, dtype_str="float32")

# Freeze the model
model.freeze()
```

### Step 4: Fine-tune the Model

Begin fine-tuning the MedGemma model by iterating over training data and updating model weights:
```python
for epoch in range(10):
    for batch_idx, (data_t, target_t) in enumerate(train_loader):
        # Zero the gradients and start training
        optimizer = torch.optim.Adam(model.parameters(), lr=4e-5)

        model.train()
        for data_batch in data_t:
            with torch.autograd.set_grad_enabled(True):
                output = model(data_batch.target_type, target_t, **data_batch.to_tensor())
                loss = output.mean().mean()  # Calculate mean squared error (MSE) between predicted and actual values

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}, Loss: {loss.item:.4f}")
```
### Step 5: Deploy the Model to Cloud Run

Use a Docker image container to package and deploy the fine-tuned model:
```markdown
## Deployment Steps

* Create a Dockerfile in the project root
* Build a Docker image and save it as `medgemma-breed-1.0` (optional)
* Push the image to your preferred registry, e.g., GCR or Docker Hub
* Configure Cloud Run by creating a Deployment resource with default settings:
  - Service name: `medgemma-breed`
  - Image identifier: `medgemma-breed-1.0`
  - Tiered service role: `AppServiceAdmin`
* Save the updated Deployment ID to the desired secret

# Update deployment.yaml
image:
  image: medgemma-breed-1.0
  containers:
    - name: medgemma
      command: /bin/sh -c "source deploy.sh;"
          stdout: 'porecho $PATH"
          stderr: 'porecho $PATH'
          stdin: null

# Deploy to Cloud Run
```

**Key Takeaway(s)**

* Integrate the MedGemma model into your workflow for breast cancer classification.
* Use a finetuning process, including data shaping and model pre-processing, to improve performance on complex tasks like pathologic tissue analysis.

This guide demonstrates how to fine-tune Google's MedGemma model on breast cancer histopathology images in a step-by-step manner. By following these directions, you can develop and deploy your own high-performance medical AI models for various tasks, from classifying disease patterns to identifying potential malignancy based on microscopic tissue features.
