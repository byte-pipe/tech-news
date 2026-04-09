---
title: Build Your Own GPT from Scratch with C# and TorchSharp (CPU-Only!) - DEV Community
url: https://dev.to/auyeungdavid_2847435260/build-your-own-gpt-from-scratch-with-c-and-torchsharp-cpu-only-3ch5
date: 2025-09-30
site: devto
model: llama3.2:1b
summarized_at: 2025-10-01T11:21:15.969713
screenshot: devto-build-your-own-gpt-from-scratch-with-c-and-torchsh.png
---

# Build Your Own GPT from Scratch with C# and TorchSharp (CPU-Only!) - DEV Community

## Building a GPT Model from Scratch with C# and TorchSharp - DEV Community

### Introduction

*   Describe the objective of building a real transformer-based language model using C# and TorchSharp on a CPU.
*   Explain why ChatGPT and Claude are not involved in this process.
*   Highlight the benefits of creating an AI system from scratch, even if it's not practical.

### Setting Up TorchSharp

```csharp
// Create a new C# console project
dotnet new console
--n
--miniGptCs
cd
MiniGptCs

// Enter fullscreen mode
exitfullscreenmode

// Install TorchSharp packages
dotnet add package TorchSharp
dotnet add package TorchSharp-cpu
```

### Understanding the Transformer Architecture

*   Describe the key components of a transformer, including token embeddings and positional embeddings.
*   Explain how self-attention allows each position in the sequence to "look at" all previous positions.

### Implementing Multi-Head Self-Attention for Contextual Understanding

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadSelfAttention(nn.Module):
    def __init__(self, d_model, n_head=8):
        super(MultiHeadSelfAttention, self).__init__()
        self.num_angles = n_head
        self.d_model = d_model
        self.temperature = 1 / math.sqrt(d_model)

    def forward(self, query, key, value):
        q = torch.matmul(query, key.transpose(-2, -1)) / self.temperature
        attention_scores = F.softmax(q, dim=-1)
        values = torch.matmul(attention_scores, value)
        return torch.mean(values, dim=1), attention_scores

def generate_token_embeddings(text, embedding_dim):
    """
    Generate token embeddings for a given text.

    Parameters:
    text (str): The input text.
    embedding_dim (int): The dimensionality of the embedding space.

    Returns:
    Embeddings (list): A list of token embeddings corresponding to each word in the text.
    """

    # Convert text into tokens
    tokens = [token for char in str(text) for token in char if len(str(token)) > 1]

    # Initialize an empty list to store the embeddings
    embeddings = []

    # Generate token embeddings using a simple approach (one-hot encoding)
    embedding_dim = int(embedding_dim ** 0.5)

    weights = np.zeros((len(tokens), embedding_dim))
    for i, token in enumerate(tokens):
        if len(token) == 1:
            continue
        weights[i] = np.random.rand(embedding_dim)


    # Use a simple linear function to predict the next character in a sequence
    def rffn(weights, i):
        return nn.Linear(len(embeddings), embedding_dim)(weights[i])

    embeddings.extend(rffn([np.random.random((embedding_dim,)) for _ in range(100)], i))

    return embeddings

token_embeddings = generate_token_embeddings('Hello World', 256)
print(token_embeddings)

# Initialize input embeddings to zeros
input_embeddings = [0] * len(tokens)

# Update embeddings by calculating the similarity between each pair of tokens and the embedding corresponding to that token

def update_embeddings(token_embeddings, inputs):
    """
    Update embeddings based on the similarity between tokens and their corresponding input values.

    Parameters:
    token_embeddings (list): A list of token embeddings derived from words in a dataset.
    inputs (list): A list of input values corresponding to each word.

    Returns:
    Updated token embeddings
    """

    # Calculate similarities between token embeddings
    similarities = np.dot(token_embeddings, inputs)

    # Use a simple approach (mean subtraction) for updating the embedding weights
    updates = [0.5] * len(tokens)

    return token_embeddings + updates

# Update embeddings based on word similarity with each other and input value
updated_token_embeddings = update_embeddings(token_embeddings, inputs)

print(updated_token_embeddings)

```

### Creating a Simple Model Using the Updated Token_embeddings

```python
class SimpleModel(nn.Module):
    def __init__(self, embedding_dim, num_layers=2, num_classes=3):
        super(SimpleModel, self).__init__()
        self.embeddings = nn.LadderLayer(embedding_dim)
        self.conv_layers = []
        for i in range(num_layers):
            conv_layers.append(nn.Conv1d(embedding_dim, embedding_dim // 2, kernel_size=5, stride=2))
            embedding_dim //= 2

    def forward(self, inputs):
        embedded_inputs = [self.embeddings(inputs)]
        outputs = [embedded_inputs[0]]
        for layer in self.conv_layers:
            output = torch.nn.functional.relu(layer(outputs[-1].reshape(-1, 64, 5)))
            outputs.append(output)

        return outputs[-1]

model = SimpleModel(input_dim=3, hidden_dim=64)
```

### Evaluating and Training the Model

```python
import os
from sklearn.metrics import accuracy_score, f1_score

# Train model and evaluate its performance on a test dataset...
train_dataset = ...
test_dataset = ...

# Initialize training and evaluation metrics
train_loss_tracker = TrainingCounter()
test_loss_tracker = TestLossTracker()

for epoch in range(10):
    model.train()
    for batch in train_dataset:
        # Zero the gradients, move to the next batch
        optimizer.zero_grad()

        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)

        with torch.no_grad():
            outputs = model(input_ids)

        loss, _ = criterion(outputs, inputs_batch)

        train_loss_tracker.update(loss.item(), epoch * len(batch))
    model.eval()

    test_loss_tracker.clear()
    total_correct, total_incorrect = 0
    for batch in test_dataset:
        # Zero the gradients, move to the next batch
        optimizer.zero_grad()

        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)

        with torch.no_grad():
            outputs = model(input_ids)

        loss, _ = criterion(outputs, inputs_batch)

        test_loss_tracker.update(loss.item(), epoch * len(batch))
    total_correct, total_incorrect = accuracy_score(test_dataset['input_ids'], test_dataset['output_labels']), \
                                      f1_score(test_dataset['input_ids'], test_dataset['output_labels'])

# Print final results
print(f'Test Accuracy: {total_correct / (len(test_dataset) - 0)}', ', ', f'Test F1 Score: {total_correct / len(test_dataset)},',
      f'Accuracy = {accuracy_score(test_dataset['input_ids'], test_dataset['output_labels'])} ')
```

Finally, train the model using a loop that iterates over multiple training mini-batches and updates its weights based on their losses.
