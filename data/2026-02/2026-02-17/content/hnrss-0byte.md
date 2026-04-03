---
title: 0byte
url: https://0byte.io/articles/pytorch_introduction.html
site_name: hnrss
content_file: hnrss-0byte
fetched_at: '2026-02-17T11:20:12.474258'
original_url: https://0byte.io/articles/pytorch_introduction.html
date: '2026-02-13'
description: AI/ML Blog
tags:
- hackernews
- hnrss
---

# Intro to PyTorch

## Easy to follow, visual introduction.

10th FEBRUARY, 2026

Table of Contents:

* what is PyTorch
* tensors basics
* autograd for automatic differentiation
* autograd in practice
* building a simple neural network
* YouTube

### what is PyTorch?

PyTorchis currently one of the most popular deep learning frameworks. It is an open-source library built upon theTorch Library(it's no longer in active development), and it was developed by Meta AI (previously Facebook AI). It is now part of theLinux Foundation.

### tensor basics

Machine Learning (ML) is all about numbers. Tensor is a specialised container for those numbers.
				You might know tensors frommathsor physics, but in machine learning, a tensor is simply PyTorch's data type for storing numbers. Think of it like a more powerful version of a list or array. Tensors hold your training data and theweightsWeights are numbers that determine how important each input is to the final decision.your model learns.What makes tensors special is that they come packed with useful functions. When you create a new tensor, you need to fill it with starting values. PyTorch offers manyinitialisation functions:torch.rand(),torch.randn(),torch.ones(), the list goes on.But what's the difference between them? If they give you random numbers, which random numbers? And why there are so many ways to initialise it?The best way to understand is to see it.If we create thousands of random values using each function and plot them as a histogram, we can see exactly what to expect:

import torch
rand_sample = torch.rand(10000)
randn_sample = torch.randn(10000)
zeros_sample = torch.zeros(10)
ones_sample = torch.ones(10)
arange_sample = torch.arange(0, 10)
linspace_sample = torch.linspace(0, 10, steps=5)
eye_sample = torch.eye(5)
empty_sample = torch.empty(10)

Seeing it as a histogram paints a very clear picture.torch.rand()initialises tensor with random values between 0 and 1.torch.randn()with values that are mostly clustering around 0 andtorch.eye()gives anidentity matrix, andtorch.empty()is... wait. Not empty? In theory is not empty. It allocates memory but does not initialise it, so the tensor contains whatever values happened to already be in that memory. If you see zeros, that’s just coincidence.torch.zeros()explicitly fills the tensor with zeros, whereastorch.empty()makes no guarantees at all - you should always write to it before reading from it."Hey! What about own my data?"I've got you. Initialising tensors with random noise can be helpful, but ultimately, you want your own data for training. Let's start with a simple example, you have data structure as follows:BedroomsSize (m²)Age (years)Price (£k)265152853958425412025380388422955180367525850245

# Each row is one house: [bedrooms, bathrooms, size, age, price]
houses = torch.tensor([
 [2, 65, 15, 285],
 [3, 95, 8, 425],
 [4, 120, 25, 380],
 [3, 88, 42, 295],
 [5, 180, 3, 675],
 [2, 58, 50, 245]
], dtype=torch.float32)

You might be wondering, not all data is numbers. Sometimes we have words, images, or even 3D mesh data. If that's the case, we need a step in between. We need to find a way to map our input data to numbers. With proprietary data types, this can be a challenging step that a Data Scientist would have to solve.Wordsget mapped to numbers. The simplest approach is to assign each word a unique ID. So the sentencehello worldbecomes[0, 1]- just numbers that PyTorch can work with.

"hello" → 0
"world" → 1

Images- are nothing more than a grid of pixels, each containing colour information (RGB - Red, Green, Blue) with values ranging from0to255. A 28×28 pixel greyscale image? That's a tensor of shape[28, 28]. A colour image? Shape[3, 28, 28]for the three colour channels. You can checkHello ML!where we built super simple image classifier.3D Mesh- We're used to seeing 3D objects in games where they appear to be solid shapes. Sometimes we see wireframes. But for machine learning, we're most interested in vertices. The points that define the shape. Each vertex has coordinates:x,y, andzvalues. A 3D model with 1000 vertices? That's a tensor of shape[1000, 3].As you can see, there's always a way to find a numerical representation of your input data.

### Tensor Mathematical Operations

Tensors also come with plenty of operations. In fact, there are over 100 pre-defined operations. These operations are described in the officialdocumentationof PyTorch. Here are a few:Basic Arithmetic Operations:

import torch

x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([4.0, 5.0, 6.0])

# BASIC ARITHMETIC
print(x + y) # Addition
print(x * y) # Element-wise multiplication
print(x @ y) # Dot product (matrix multiplication for 1D)

# AGGREGATIONS
print(x.sum()) # Sum all elements
print(x.mean()) # Average
print(x.max()) # Maximum value

Activation Functions:

import torch
import torch.nn.functional as F

x = torch.tensor([-2.0, -1.0, 0.0, 1.0, 2.0])

# RELU (MOST POPULAR) - SETS NEGATIVE VALUES TO 0
print(F.relu(x)) # tensor([0., 0., 0., 1., 2.])

# SIGMOID - NORMALISE VALUES BETWEEN 0 and 1
print(torch.sigmoid(x)) # tensor([0.12, 0.27, 0.50, 0.73, 0.88])

# TANH - NORMALISE VALUES BETWEEN -1 and 1
print(torch.tanh(x)) # tensor([-0.96, -0.76, 0.00, 0.76, 0.96])

### autograd for automatic differentiation

You'll often see the phrase "Autograd is the engine of Neural Networks." Sure, you don't need to know how an engine works to drive a car, but it's a good idea to at least peek below the bonnet.If you already know what a function derivative is, feel free to skip tothe next chapter.Differentiation is a big deal. It's a fundamental mathematical operation that underpins much of science and engineering. Differentiation is used to describe how a function changes with respect to a specific variable. Differential equations are common throughout science and engineering; from modeling the evolution of bacteria to calculating rocket thrust over time to predictive machine learning algorithms, the ability to rapidly compute accurate differential equations is of great interest."-autograd.readthedocs.io

### DERIVATIVE - HOW STEEP IN ONE DIRECTION?

f(x) = x²

Move along the curve (x position):0.00

						Position (x):
0.00


 				Function value f(x) = x²:

0.00

 				Derivative f'(x) = 2x:
0.00


						The dashed line shows the slope (derivative) at that point. Notice how the slope gets steeper as you move away from x = 0. At x = 2, our function is changing at a rate of 4.


Now, that's interesting. But even our simple apartment example from the beggining has more than one variable. In fact we have 4! Bedrooms, Bathrooms, Square Footage and Age. (Price is the target value - what we want to predict.

### GRADIENT - HOW STEEP IN ALL DIRECTIONS?

f(x) = x² + y²

X position:1.00

Y position:1.00

Position: (

0.00
,

0.00
)
Function value f(x, y) = 0.2x² + 0.2y²:

0.00
Gradient ∇f = [0.3x, 0.3y] = [

0.00
,
0.00

]
The yellow arrow shows the gradient - always points in the direction of steepest increase.

The gradient is just a collection of derivatives - one for each variable. It shows us the slope in every direction at once. We can visualise a function with two variables,xandy, because we still have that third dimensionzto show height. But here's the kicker: we've already hit our visualisation limit. Any network with more than two parameters is near impossible to visualise. Real neural networks have millions.That's why we need autograd. It handles all the derivative calculations automatically. And with the help of a GPU, this can be done at speeds hard to imagine.We just trust the maths at this point.

### GRADIENT DESCENT - FOLLOWING THE SLOPE DOWNHILL

Autograd gives us the gradient. As you saw on the chart, the arrow points uphill in the direction of steepest increase. And what's up there? Higher loss - further away from the truth. Based on that information we can make adjustmets. Gradient Descent is the algorithm that finds our way down, to the valley where loss is lowest.It's not the only algorithm that does that. The one worth mentionig isAdam- one of the most popular optimisers, also included in PyTorch's library.The training loop becomes: calculate derivatives to get the gradient → use the optimiser (gradient descent, Adam, etc.) to make adjustments → repeat that hundreds or thousands of times.

### autograd in practice

Let's now explore how we can calculate derivatives in PyTorch.

# DEFINE SINGLE VALUE TENSOR
# NOTICE WE ARE ENABLING GRADIENT TRACKING
x = torch.tensor(2.0, requires_grad=True)

# DEFINE FUNCTION f(x) = x²
f = x ** 2

# TO CALCULATE GRADIENT WE CAN CALL .backward() function
f.backward()

# WE CAN NOW CHECK THE GRADIENT (DERIVATIVE) AT OUR POINT x
print(x.grad) # 4.0

Let's try something more complex.

# DEFINE THREE TENSORS WITH GRADIENT TRACKING
x = torch.tensor(1.0, requires_grad=True)
y = torch.tensor(2.0, requires_grad=True)
z = torch.tensor(0.5, requires_grad=True)

# DEFINE FUNCTION f(x,y,z) = sin(x)·y² + e^z
f = torch.sin(x) * y**2 + torch.exp(z)

# CALCULATE GRADIENTS
f.backward()

# CHECK DERIVATIVES
print(x.grad) # cos(1) * 4 ≈ 2.16
print(y.grad) # sin(1) * 2*2 ≈ 3.37
print(z.grad) # e^0.5 ≈ 1.65

This is getting tedious. But here's the thing: when training a neural network, you don't write out these functions manually. The network architecture itself is the complex function with millions of parameters and operations. PyTorch tracks everything automatically. You just define your model, run it, calculate loss, and call.backward(). PyTorch handles all the maths behind the scenes.

### building a simple neural network

As an intro, it's fitting to create a simple classifier or regression model. You've probably seen the classicTitanic tabular dataset? Well, this property price estimator is in the same boat. :)We're usingtabular dataTabular data is information arranged in rows and columns, like a spreadsheet. Each row represents one record, and each column represents a specific piece of information about it.here because it lets us focus on learning PyTorch's core concepts - the training loop, backpropagation, and model building. In practice, neural nets really shine on unstructured data like images and text. Because this is a simple intro, we'd like to avoid convolutional layers (CNNs).If you have tabular data, it's often a good idea to tryXGBoostorLightGBMbefore jumping to building a custom neural network, which might be less accurate.

### IMPORTING LIBRARIES



import torch
import torch.nn as nn
# CONTAINS ACTIVATION FUNCTIONS
import torch.nn.functional as F
# PANDAS FOR LOADING CSV DATA
import pandas as pd
# POPULAR LIBRARY FOR SPLITTING DATA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
# OPTIONAL. FOR VISUALISATION
import matplotlib.pyplot as plt

### DATA PREP

DATASET: london_houses_transformed.csv

In Machine Learning, data is king - but it needs to be in the right format. The typical workflow:1.Separate features from the target- We drop the 'price' columnx = data_raw.drop('price', axis = 1)to get feature setx. Price will go toy. This is our target.2.Data Split- Often you would do a TRAIN/VALIDATE/TEST split, but we'll keep it simple with just TRAIN/TEST usingtest_size=0.2- we essentially save 20% of dataset aside for testing while preserving 80% for training. Therandom_state=42parameter ensures the split is reproducible.3.Normalise- Some values are large and can disproportionately influence training. We scale to zero mean and unit variance usingStandardScaler. Fitted on training data only to avoid data leakage.4.Tensor- Convert our data to PyTorch tensors — the data type required for training.

data_raw = pd.read_csv('./london_houses_transformed.csv')
# SEPARATE FEATURES FROM THE TARGET
x = data_raw.drop('price', axis = 1)
y = data_raw['price']

# DATA SPLIT 80/20
X_train_raw, X_test_raw, Y_train_raw, Y_test_raw = train_test_split(
 x.values, y.values, test_size=0.2, random_state=15
)

# NORMALISE
scaler_X = StandardScaler().fit(X_train_raw)
scaler_Y = StandardScaler().fit(Y_train_raw.reshape(-1, 1))

# SAVING THIS FOR DE-NORMALISATION LATER
price_mean = scaler_Y.mean_[0]
price_std = scaler_Y.scale_[0]

# TENSOR
X_train = torch.FloatTensor(scaler_X.transform(X_train_raw))
X_test = torch.FloatTensor(scaler_X.transform(X_test_raw))
Y_train = torch.FloatTensor(scaler_Y.transform(Y_train_raw.reshape(-1, 1)))
Y_test = torch.FloatTensor(scaler_Y.transform(Y_test_raw.reshape(-1, 1)))

### DEFINE THE MODEL

It's time to define our model object. No magic here. FollowingPyTorch official documentation. The difference is that we're specifying the amount of input features87(our data has 88 columns - 87 Features and 1 Target). Hidden layers:h1with 64 neurons,h2with 32 neurons, and1output feature (price). Using ReLU for activation function.

class Model(nn.Module):
 def __init__(self, in_features=87, h1=64, h2=32, output_features=1):
 super().__init__()
 self.fc1 = nn.Linear(in_features, h1)
 self.fc2 = nn.Linear(h1, h2)
 self.out = nn.Linear(h2, output_features)

 def forward(self, x):
 x = F.relu(self.fc1(x))
 x = F.relu(self.fc2(x))
 x = self.out(x)

 return x

model = Model()

### TRAINING LOOP

Time to send our model to school! The training loop is where the model actually learns. Each iteration through the entire dataset is called an epoch. Here's what happens in each epoch:

1. Forward Pass- Send training data through the model and get predictions:model.forward(X_train).
2. Calculate Loss- We measure how wrong the predictions are usingMSELoss().
3. Backpropagation-loss.backward()calculates how much each weight contributed to the error.
4. Update Weights-optimiser.step()adjusts the weights to reduce the error. We use theAdamoptimiser, which adapts the learning rate for each parameter automatically.
5. Clear Gradients-optimiser.zero_grad()resets the gradients so they don't accumulate into the next epoch.

We repeat this process 100 times at a 0.01 learning rate. With each epoch, the loss should decrease as the model gets better at predicting prices.

epochs = 100
learning_rate = 0.01
torch.manual_seed(15)
# EACH TRAINING LOOP, WE'LL STORE THE LOSS
# THIS IS OPTIONAL, USED FOR VISUALISING LOSS GRAPH
losses = []

optimiser = torch.optim.Adam(model.parameters(), learning_rate)
loss_func = nn.MSELoss()

for i in range(epochs):
 optimiser.zero_grad()

 y_pred = model.forward(X_train)

 # MEASURE THE LOSS/ERROR
 loss = loss_func(y_pred, Y_train)

 # (OPTIONAL) ADDING LOSS FROM THE CURRENT EPOCH
 losses.append(loss.detach().numpy())

 # (OPTIONAL) PRINTING LOSS EVERY 500th EPOCH
 if i % 500 == 0:
 print(f'Epoch: {i} loss: {loss}')

 # CLEAR GRADIENTS FROM PREVIOUS STEP
 optimiser.zero_grad()
 # BACKPROPAGATION
 loss.backward()
 # UPDATE WEIGHTS
 optimiser.step()

# SAVE OUR FINAL MODEL
torch.save(model.state_dict(), 'model.pth')

### (OPTIONAL) VISUALISING LOSS FUNCTION

plt.figure(figsize=(10, 6))
plt.plot(losses, linewidth=2, color='#e74c3c')
plt.xlabel('EPOCH', fontsize=12)
plt.ylabel('MSE Loss (normalised)', fontsize=12)
plt.title('Training Progress: Loss Approaching Zero', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.ylim(bottom=0)
plt.tight_layout()
plt.show()

### TESTING OUR MODEL

We test the model with the cases we put aside. With data that the model hasn't seen yet, we check the results against the actual target data. Then we collect the results to calculate:- MAE - Mean Absolute Error- MAPE - Mean Absolute Percentage Error

# TELLS PYTORCH WE ARE IN INFERENCE MODE
model.eval()
with torch.no_grad():
 predictions = model(X_test)

 # DENORMALISE BACK TO REAL PRICES:
 predictions_real = predictions * price_std + price_mean
 Y_test_real = Y_test * price_std + price_mean

 print("\nTEST PREDICTIONS (UNSEEN DATA):")
 mae = mean_absolute_error(Y_test_real, predictions_real)
 mape = mean_absolute_percentage_error(Y_test_real, predictions_real) * 100

 # CALCULATE PERCENTAGE ERRORS
 pct_errors = torch.abs((Y_test_real - predictions_real) / Y_test_real) * 100

 within_10 = (pct_errors <= 10).sum().item()
 within_20 = (pct_errors <= 20).sum().item()
 total = len(Y_test_real)

print(f"\nOverall performance:")
print(f" MAE: £{mae:,.0f}")
print(f" MAPE: {mape:.1f}%")
print(f" Within 10%: {within_10}/{total} ({within_10/total*100:.0f}%)")
print(f" Within 20%: {within_20}/{total} ({within_20/total*100:.0f}%)")

The results are in:Overall performance:MAE: £329,798MAPE: 18.6%Within 10%: 257/689 (37%)Within 20%: 447/689 (65%)We've built a complete ML pipeline from scratch - data prep, training, backpropagation, evaluation - all working together. The results show us exactly where the real challenge lies: not in the model, but in the features. Property prices are all about location, and our current features can't capture that granularity. This is the reality of ML: great models can't compensate for missing information. Next time? Start with better features, or reach forXGBoostwhen working with tabular data.

### YouTube Video

recording... :)

### Like the content? Subscribe to the newsletter!
