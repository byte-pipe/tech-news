---
title: Build Your Own GPT from Scratch with C# and TorchSharp (CPU-Only!) - DEV Community
url: https://dev.to/auyeungdavid_2847435260/build-your-own-gpt-from-scratch-with-c-and-torchsharp-cpu-only-3ch5
site_name: devto
fetched_at: '2025-10-02T11:08:24.066182'
original_url: https://dev.to/auyeungdavid_2847435260/build-your-own-gpt-from-scratch-with-c-and-torchsharp-cpu-only-3ch5
author: David Au Yeung
date: '2025-09-30'
description: Introduction Ever wondered what it takes to build a GPT model from scratch? Think it's... Tagged with gpt, ai, torchsharp, csharp.
tags: '#gpt, #ai, #torchsharp, #csharp'
---

## Introduction

Ever wondered what it takes to build a GPT model from scratch? Think it's only possible with Python and expensive GPU clusters? Think again! In this hands-on guide, we'll build a real transformer-based language model usingC#andTorchSharp, and we'll do it all on aCPU.

Yes, the results won't match ChatGPT or Claude, but that's not the point. The goal is to understand how these AI systems work under the hood and prove that you can enter the AI age with tools you already know. Even if your generated text is a bit "strange" or repetitive (the model may not very practical 😜), you'll have built something incredible: your own neural network that learns to predict the next character in a sequence.

So grab your favorite IDE, roll up your sleeves, and let's dive into the fascinating world of transformers together!

## Setting Up Your Environment

Before we start coding, you'll need to set up TorchSharp, the C# binding for PyTorch. Here's what you need:

Step 1: Create a new C# console project

dotnet new console
-n
 MiniGptCs

cd
MiniGptCs

Enter fullscreen mode

Exit fullscreen mode

Step 2: Install TorchSharp packages

dotnet add package TorchSharp
dotnet add package TorchSharp-cpu

Enter fullscreen mode

Exit fullscreen mode

If you're on Windows and want to experiment with CUDA later, you can also install:

dotnet add package TorchSharp-cuda-windows

Enter fullscreen mode

Exit fullscreen mode

For this tutorial, we'll stick with CPU-only training since it's accessible to everyone. Yes, it's slower, but for learning purposes, it works perfectly fine!

## Understanding the Architecture: What Makes a Transformer Tick?

Before we jump into the code, let's understand the key components of our GPT model. A transformer consists of several critical building blocks that work together to process and generate text.

### The Token Embeddings: Teaching the Model About Words

Our model starts by converting characters into numbers (tokens) and then into high-dimensional vectors (embeddings). Think of embeddings as a way to represent each character in a space where similar characters or patterns end up closer together. We use two types of embeddings: token embeddings that represent what character it is, and positional embeddings that represent where in the sequence it appears.

### Multi-Head Self-Attention: The Heart of Understanding Context

This is where the magic happens. Self-attention allows each position in the sequence to "look at" all previous positions and decide which ones are important for predicting the next token. The multi-head part means we do this multiple times in parallel, allowing the model to attend to different types of patterns simultaneously. Some heads might focus on nearby characters, while others capture long-range dependencies.

The key mathematical operation is computing attention scores between queries (Q), keys (K), and values (V). We mask out future positions to ensure the model can only look backward, which is crucial for language modeling. Here's the core attention mechanism in our code:

var

att

=

torch
.
matmul
(
qh
,

kh
.
transpose
(-
2
,

-
1
))

/

MathF
.
Sqrt
(
headDim
);

att

=

att
.
masked_fill
(
maskSlice
.
logical_not
(),

float
.
NegativeInfinity
);

att

=

torch
.
softmax
(
att
,

dim
:

-
1
);

var

y

=

torch
.
matmul
(
att
,

vh
);

Enter fullscreen mode

Exit fullscreen mode

### Feed-Forward Networks: Processing the Attended Information

After attention, we pass the results through a feed-forward network. This is a simple two-layer neural network with a GELU activation function in between. The feed-forward network processes each position independently, transforming the attended information into a more useful representation for the next layer.

### Layer Normalization and Residual Connections

These are the unsung heroes that make deep networks trainable. Layer normalization stabilizes the activations, while residual connections (thex = x + attn.forward(h)pattern) allow gradients to flow directly through the network, preventing the vanishing gradient problem that plagued early deep learning.

## Breaking Down the Key Components

Let's walk through the critical pieces of our implementation:

### The Character Tokenizer

Our tokenizer is deliberately simple - it works at the character level rather than using subword tokenization like modern GPT models. This makes the code easier to understand and the vocabulary size manageable (only unique characters in your corpus):

public

CharTokenizer
(
string

corpus
)

{


var

chars

=

corpus
.
Distinct
().
OrderBy
(
c

=>

c
).
ToArray
();


_stoi

=

new

Dictionary
<
char
,

int
>();


_itos

=

new

Dictionary
<
int
,

char
>();


for

(
int

i

=

0
;

i

<

chars
.
Length
;

i
++)


{


_stoi
[
chars
[
i
]]

=

i
;


_itos
[
i
]

=

chars
[
i
];


}

}

Enter fullscreen mode

Exit fullscreen mode

Each character gets mapped to an integer ID, and we can convert back and forth between text and token sequences.

### The Transformer Block

A transformer block combines self-attention and feed-forward processing with careful normalization. Notice the pre-normalization pattern (LayerNorm before the operation rather than after) and the residual connections:

public

override

Tensor

forward
(
Tensor

x
)

{


var

h

=

ln1
.
forward
(
x
);


x

=

x

+

attn
.
forward
(
h
);

// Residual connection


h

=

ln2
.
forward
(
x
);


x

=

x

+

ffn
.
forward
(
h
);

// Another residual connection


return

x
;

}

Enter fullscreen mode

Exit fullscreen mode

This clean structure is repeated multiple times (we use 4 layers) to build depth into our model.

### The Generation Process: Sampling New Text

Once trained, we generate text by repeatedly predicting the next token and sampling from the probability distribution. We use several techniques to improve generation quality:

Temperature scalingcontrols randomness - lower values make the model more confident and repetitive, higher values introduce more variety but potentially more nonsense.

Top-k samplingonly considers the k most likely next tokens, preventing the model from choosing very unlikely options.

Top-p (nucleus) samplingdynamically chooses how many tokens to consider based on their cumulative probability, which tends to produce more natural text than top-k alone.

## Tuning Your Model: The Parameters That Matter

Getting good results requires understanding which hyperparameters have the biggest impact. Here's what you should focus on:

### Model Architecture Parameters

dModel (128 in our code): This is the embedding dimension - how many numbers we use to represent each token's state. Larger values give the model more capacity to learn complex patterns but require more memory and computation. For CPU training on small datasets, 128-256 works well.

nLayers (4): The number of transformer blocks stacked on top of each other. More layers allow the model to learn more abstract patterns, but they also make training slower. For character-level modeling on limited data, 4-6 layers is a sweet spot.

nHeads (4): The number of attention heads in each layer. This should divide evenly into dModel. More heads let the model attend to different types of patterns, but there are diminishing returns. Four to eight heads typically works well.

contextLen (96): The maximum sequence length the model can process at once. Longer contexts help the model learn long-range dependencies but quadratically increase memory usage due to the attention mechanism. For CPU training, keep this under 128.

### Training Parameters

Learning rate schedule: We use a warmup phase followed by cosine annealing. The warmup prevents the model from making huge updates early in training when gradients are unstable. The cosine annealing gradually reduces the learning rate, allowing the model to fine-tune its weights. Our lrMax of 5e-4 and lrMin of 5e-5 work well for AdamW optimization.

Batch size and gradient accumulation: We use a batch size of 24 with 2 accumulation steps, effectively training on 48 examples per update. Gradient accumulation lets us simulate larger batch sizes without running out of memory. Larger effective batch sizes lead to more stable training but slower convergence.

Dropout (0.15): This randomly zeros out some activations during training, which prevents overfitting. Too much dropout hurts learning, too little causes the model to memorize the training data. Values between 0.1 and 0.2 generally work well.

Gradient clipping (1.0): This prevents exploding gradients by capping the norm of the gradient vector. It's essential for stable training of deep networks.

### Training Progress Analysis from My Results

Looking at the training output, you can see the model is learning:

setstartText = "To be, or not to be";

Using device: CPU
iter 1/2000 | lr 2.50E-006 | train loss 3.9754 | val loss 3.9811
iter 200/2000 | lr 5.00E-004 | train loss 2.1095 | val loss 2.0318
iter 400/2000 | lr 4.86E-004 | train loss 0.9399 | val loss 0.5726
iter 600/2000 | lr 4.47E-004 | train loss 0.4789 | val loss 0.1911
iter 800/2000 | lr 3.88E-004 | train loss 0.3061 | val loss 0.1322
iter 1000/2000 | lr 3.14E-004 | train loss 0.2512 | val loss 0.0998
iter 1200/2000 | lr 2.36E-004 | train loss 0.1993 | val loss 0.0934
iter 1400/2000 | lr 1.63E-004 | train loss 0.1841 | val loss 0.0981
iter 1600/2000 | lr 1.03E-004 | train loss 0.1684 | val loss 0.0802
iter 1800/2000 | lr 6.36E-005 | train loss 0.1759 | val loss 0.0799
iter 2000/2000 | lr 5.00E-005 | train loss 0.1534 | val loss 0.0775
---- Generated ----
To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take Arms against a Sea of troubles,
And by opposing end them: to die, to sleep;
No more; and by a sleep, to say we end
The heart-ache, and the thousand natural shocks
That Fle

Enter fullscreen mode

Exit fullscreen mode

The model started with essentially random predictions (loss ~3.98) and improved dramatically to a final training loss of 0.1534 and validation loss of 0.0775, representing about 96% improvement. The learning rate schedule worked perfectly, warming up from 2.5e-6 to 5e-4 over 200 iterations, then gradually annealing down to 5e-5. The fact that your validation loss (0.0775) is actually lower than training loss is a good sign - it means the model isn't overfitting and can generalize well, likely because dropout makes training harder while validation runs with full model capacity. A loss of 0.0775 translates to the model being roughly 92.5% confident about predicting the next character on average, which is impressive for such a small model (4 layers, 128 dimensions) trained on CPU. The generated text perfectly reproduces Shakespeare's famous soliloquy for several lines before trailing off at "That Fle", which is expected given the limited model size and training corpus - the model successfully learned the patterns, style, and structure of Shakespearean English, it just lacks the capacity and data diversity to continue indefinitely without some repetition or odd endings.

## Tips for Better Results

If you want to improve your model's output, try these approaches:

Expand your training corpus: More diverse data helps the model learn richer patterns. Try downloading the complete works of Shakespeare or other public domain texts.

Train longer: Run for 5000-10000 iterations if you have the patience. The model will continue to improve, though with diminishing returns.

Tune the generation parameters: Experiment with temperature (try 0.7-0.9), top-k (try 30-100), and top-p (try 0.85-0.95) to find the sweet spot for your use case.

Monitor the validation loss: If validation loss starts increasing while training loss decreases, you're overfitting. Increase dropout or reduce model size.

Be patient with CPU training: Each iteration takes a few seconds on CPU. Consider training overnight to get more iterations in.

## The Complete Code

Here's the full implementation you can copy and run:

using

System.Text
;

using

TorchSharp
;

using

TorchSharp.Modules
;

using

static

TorchSharp
.
torch
;

namespace

MiniGptCs

{


// ---------------------------


// Utility: simple char tokenizer


// ---------------------------


public

sealed

class

CharTokenizer


{


private

readonly

Dictionary
<
char
,

int
>

_stoi
;


private

readonly

Dictionary
<
int
,

char
>

_itos
;


public

int

VocabSize

=>

_itos
.
Count
;


public

CharTokenizer
(
string

corpus
)


{


var

chars

=

corpus
.
Distinct
().
OrderBy
(
c

=>

c
).
ToArray
();


_stoi

=

new

Dictionary
<
char
,

int
>();


_itos

=

new

Dictionary
<
int
,

char
>();


for

(
int

i

=

0
;

i

<

chars
.
Length
;

i
++)


{


_stoi
[
chars
[
i
]]

=

i
;


_itos
[
i
]

=

chars
[
i
];


}


}


public

long
[]

Encode
(
string

text
)


{


var

result

=

new

long
[
text
.
Length
];


for

(
int

i

=

0
;

i

<

text
.
Length
;

i
++)


{


if

(!
_stoi
.
TryGetValue
(
text
[
i
],

out

var

id
))


throw

new

Exception
(
$"Unknown char '
{
text
[
i
]}
' for this tokenizer."
);


result
[
i
]

=

id
;


}


return

result
;


}


public

string

Decode
(
IEnumerable
<
long
>

ids
)


{


var

sb

=

new

StringBuilder
();


foreach

(
var

id

in

ids
)


{


if

(!
_itos
.
TryGetValue
((
int
)
id
,

out

var

ch
))


ch

=

'?'
;


sb
.
Append
(
ch
);


}


return

sb
.
ToString
();


}


}


// ---------------------------


// Modules


// ---------------------------


public

class

GELU

:

TorchSharp
.
torch
.
nn
.
Module
<
Tensor
,

Tensor
>


{


public

GELU
()

:

base
(
"gelu"
)

{

}


public

override

Tensor

forward
(
Tensor

input
)


{


var

x

=

input
;


var

c

=

(
float
)
Math
.
Sqrt
(
2.0

/

Math
.
PI
);


return

0.5f

*

x

*

(
1

+

torch
.
tanh
(
c

*

(
x

+

0.044715f

*

torch
.
pow
(
x
,

3
))));


}


}


public

class

MultiHeadSelfAttention

:

TorchSharp
.
torch
.
nn
.
Module
<
Tensor
,

Tensor
>


{


private

readonly

int

nHeads
;


private

readonly

int

dModel
;


private

readonly

int

headDim
;


private

readonly

int

contextLen
;


private

readonly

Linear

qkvProj
;


private

readonly

Linear

outProj
;


private

readonly

Dropout

attnDrop
,

residDrop
;


private

Tensor
?

causalMask
;


public

MultiHeadSelfAttention
(
int

dModel
,

int

nHeads
,

int

contextLen
,

double

attnDropProb

=

0.0
,

double

residDropProb

=

0.0
)


:

base
(
"mhsa"
)


{


if

(
dModel

%

nHeads

!=

0
)

throw

new

ArgumentException
(
"dModel must be divisible by nHeads."
);


this
.
nHeads

=

nHeads
;


this
.
dModel

=

dModel
;


this
.
headDim

=

dModel

/

nHeads
;


this
.
contextLen

=

contextLen
;


qkvProj

=

torch
.
nn
.
Linear
(
dModel
,

dModel

*

3
,

hasBias
:

true
);


outProj

=

torch
.
nn
.
Linear
(
dModel
,

dModel
,

hasBias
:

true
);


attnDrop

=

torch
.
nn
.
Dropout
(
attnDropProb
);


residDrop

=

torch
.
nn
.
Dropout
(
residDropProb
);


RegisterComponents
();


}


public

override

Tensor

forward
(
Tensor

x
)


{


var

B

=

x
.
shape
[
0
];


var

T

=

x
.
shape
[
1
];


var

C

=

x
.
shape
[
2
];


var

qkv

=

qkvProj
.
forward
(
x
);


var

qkvSplit

=

qkv
.
chunk
(
3
,

dim
:

-
1
);


var

q

=

qkvSplit
[
0
];


var

k

=

qkvSplit
[
1
];


var

v

=

qkvSplit
[
2
];


var

qh

=

q
.
view
(
B
,

T
,

nHeads
,

headDim
).
transpose
(
1
,

2
);


var

kh

=

k
.
view
(
B
,

T
,

nHeads
,

headDim
).
transpose
(
1
,

2
);


var

vh

=

v
.
view
(
B
,

T
,

nHeads
,

headDim
).
transpose
(
1
,

2
);


var

att

=

torch
.
matmul
(
qh
,

kh
.
transpose
(-
2
,

-
1
))

/

MathF
.
Sqrt
(
headDim
);


EnsureCausalMask
(
T
,

att
.
device
);


var

maskSlice

=

causalMask
!.
narrow
(
0
,

0
,

T
).
narrow
(
1
,

0
,

T
).
unsqueeze
(
0
).
unsqueeze
(
0
);


att

=

att
.
masked_fill
(
maskSlice
.
logical_not
(),

float
.
NegativeInfinity
);


att

=

torch
.
softmax
(
att
,

dim
:

-
1
);


att

=

attnDrop
.
forward
(
att
);


var

y

=

torch
.
matmul
(
att
,

vh
);


y

=

y
.
transpose
(
1
,

2
).
contiguous
().
view
(
B
,

T
,

C
);


y

=

outProj
.
forward
(
y
);


y

=

residDrop
.
forward
(
y
);


return

y
;


}


private

void

EnsureCausalMask
(
long

T
,

Device

device
)


{


if

(
causalMask

is

not

null

&&


causalMask
.
device

==

device

&&


causalMask
.
shape
[
0
]

>=

T

&&


causalMask
.
shape
[
1
]

>=

T
)


return
;


var

ones

=

torch
.
ones
(
new

long
[]

{

contextLen
,

contextLen

},

dtype
:

ScalarType
.
Bool
,

device
:

device
);


causalMask

=

torch
.
tril
(
ones
);


}


}


public

class

FeedForward

:

TorchSharp
.
torch
.
nn
.
Module
<
Tensor
,

Tensor
>


{


private

readonly

Sequential

seq
;


public

FeedForward
(
int

dModel
,

int

hiddenMult

=

4
,

double

dropout

=

0.0
)

:

base
(
"ffn"
)


{


var

hidden

=

hiddenMult

*

dModel
;


seq

=

torch
.
nn
.
Sequential
(


(
"linear1"
,

torch
.
nn
.
Linear
(
dModel
,

hidden
,

hasBias
:

true
)),


(
"gelu"
,

new

GELU
()),


(
"dropout1"
,

torch
.
nn
.
Dropout
(
dropout
)),


(
"linear2"
,

torch
.
nn
.
Linear
(
hidden
,

dModel
,

hasBias
:

true
)),


(
"dropout2"
,

torch
.
nn
.
Dropout
(
dropout
))


);


RegisterComponents
();


}


public

override

Tensor

forward
(
Tensor

x
)

=>

seq
.
forward
(
x
);


}


public

class

TransformerBlock

:

TorchSharp
.
torch
.
nn
.
Module
<
Tensor
,

Tensor
>


{


private

readonly

LayerNorm

ln1
;


private

readonly

LayerNorm

ln2
;


private

readonly

MultiHeadSelfAttention

attn
;


private

readonly

FeedForward

ffn
;


public

TransformerBlock
(
int

dModel
,

int

nHeads
,

int

contextLen
,

double

dropout

=

0.0
)

:

base
(
"block"
)


{


ln1

=

torch
.
nn
.
LayerNorm
(
new

long
[]

{

dModel

},

eps
:

1e-5
);


ln2

=

torch
.
nn
.
LayerNorm
(
new

long
[]

{

dModel

},

eps
:

1e-5
);


attn

=

new

MultiHeadSelfAttention
(
dModel
,

nHeads
,

contextLen
,

attnDropProb
:

dropout
,

residDropProb
:

dropout
);


ffn

=

new

FeedForward
(
dModel
,

hiddenMult
:

4
,

dropout
:

dropout
);


RegisterComponents
();


}


public

override

Tensor

forward
(
Tensor

x
)


{


var

h

=

ln1
.
forward
(
x
);


x

=

x

+

attn
.
forward
(
h
);


h

=

ln2
.
forward
(
x
);


x

=

x

+

ffn
.
forward
(
h
);


return

x
;


}


}


public

class

GPT

:

TorchSharp
.
torch
.
nn
.
Module
<
Tensor
,

(
Tensor
,

Tensor
?)>


{


private

readonly

int

vocabSize
;


private

readonly

int

contextLen
;


private

readonly

Embedding

tokEmbed
;


private

readonly

Embedding

posEmbed
;


private

readonly

ModuleList
<
TorchSharp
.
torch
.
nn
.
Module
>

blocks
;


private

readonly

LayerNorm

lnF
;


private

readonly

Linear

lmHead
;


private

readonly

Dropout

drop
;


public

GPT
(
int

vocabSize
,

int

contextLen
,

int

nLayers
,

int

nHeads
,

int

dModel
,

double

dropout

=

0.0
)

:

base
(
"gpt"
)


{


this
.
vocabSize

=

vocabSize
;


this
.
contextLen

=

contextLen
;


tokEmbed

=

torch
.
nn
.
Embedding
(
vocabSize
,

dModel
);


posEmbed

=

torch
.
nn
.
Embedding
(
contextLen
,

dModel
);


drop

=

torch
.
nn
.
Dropout
(
dropout
);


blocks

=

new

ModuleList
<
TorchSharp
.
torch
.
nn
.
Module
>();


for

(
int

i

=

0
;

i

<

nLayers
;

i
++)


blocks
.
append
(
new

TransformerBlock
(
dModel
,

nHeads
,

contextLen
,

dropout
));


lnF

=

torch
.
nn
.
LayerNorm
(
new

long
[]

{

dModel

},

eps
:

1e-5
);


lmHead

=

torch
.
nn
.
Linear
(
dModel
,

vocabSize
,

hasBias
:

false
);


RegisterComponents
();


lmHead
.
weight

=

tokEmbed
.
weight
;


InitWeights
();


}


private

void

InitWeights
()


{


torch
.
nn
.
init
.
normal_
(
tokEmbed
.
weight
,

mean
:

0.0
,

std
:

0.02
);


torch
.
nn
.
init
.
normal_
(
posEmbed
.
weight
,

mean
:

0.0
,

std
:

0.02
);


}


public

(
Tensor

logits
,

Tensor
?

loss
)

forward
(
Tensor

idx
,

Tensor
?

targets

=

null
)


{


var

B

=

idx
.
shape
[
0
];


var

T

=

idx
.
shape
[
1
];


if

(
T

>

contextLen
)

throw

new

ArgumentException
(
$"Sequence length
{
T
}
 exceeds context length
{
contextLen
}
"
);


var

tok

=

tokEmbed
.
forward
(
idx
);


var

positions

=

torch
.
arange
(
0
,

T
,

dtype
:

ScalarType
.
Int64
,

device
:

idx
.
device
);


var

pos

=

posEmbed
.
forward
(
positions
).
unsqueeze
(
0
).
expand
(
B
,

T
,

-
1
);


var

x

=

drop
.
forward
(
tok

+

pos
);


foreach

(
var

block

in

blocks
)


x

=

((
TransformerBlock
)
block
).
forward
(
x
);


x

=

lnF
.
forward
(
x
);


var

logits

=

lmHead
.
forward
(
x
);


Tensor
?

loss

=

null
;


if

(
targets

is

not

null
)


{


var

BTV

=

(
int
)(
B

*

T
);


var

logitsFlat

=

logits
.
view
(
BTV
,

vocabSize
);


var

targetsFlat

=

targets
.
view
(
BTV
);


loss

=

torch
.
nn
.
functional
.
cross_entropy
(
logitsFlat
,

targetsFlat
,

reduction
:

torch
.
nn
.
Reduction
.
Mean
);


}


return

(
logits
,

loss
);


}


public

override

(
Tensor
,

Tensor
?)

forward
(
Tensor

input
)

=>

forward
(
input
,

null
);


public

Tensor

Generate
(
Tensor

idx
,

int

maxNewTokens
,

double

temperature

=

1.0
,

int
?

topK

=

null
,

double
?

topP

=

null
)


{


using

var

noGrad

=

torch
.
no_grad
();


var

device

=

idx
.
device
;


var

seq

=

idx
.
clone
();


for

(
int

step

=

0
;

step

<

maxNewTokens
;

step
++)


{


var

Tcur

=

seq
.
shape
[
1
];


var

input

=

Tcur

<=

contextLen

?

seq

:

seq
.
narrow
(
1
,

Tcur

-

contextLen
,

contextLen
);


var

(
logits
,

_
)

=

forward
(
input
);


var

nextLogits

=

logits
.
narrow
(
1
,

logits
.
shape
[
1
]

-

1
,

1
).
squeeze
(
1
);


nextLogits

=

nextLogits

/

(
float
)
temperature
;


if

(
topK
.
HasValue
)


nextLogits

=

TopKFilter
(
nextLogits
,

topK
.
Value
);


if

(
topP
.
HasValue
)


nextLogits

=

TopPFilter
(
nextLogits
,

topP
.
Value
);


var

probs

=

torch
.
softmax
(
nextLogits
,

dim
:

-
1
);


var

nextToken

=

torch
.
multinomial
(
probs
,

num_samples
:

1
);


seq

=

torch
.
cat
(
new

Tensor
[]

{

seq
,

nextToken

},

dim
:

1
);


}


return

seq
;


}


private

static

Tensor

TopKFilter
(
Tensor

logits
,

int

k
)


{


int

V

=

(
int
)
logits
.
shape
[^
1
];


if

(
k

<

1
)

k

=

1
;


if

(
k

>

V
)

k

=

V
;


if

(
logits
.
dtype

!=

ScalarType
.
Float32

&&

logits
.
dtype

!=

ScalarType
.
Float64
)


logits

=

logits
.
to_type
(
ScalarType
.
Float32
);


var

(
topkVals
,

topkIdx
)

=

torch
.
topk
(
logits
,

k
,

dim
:

-
1
);


var

negInf

=

torch
.
full_like
(
logits
,

float
.
NegativeInfinity
);


var

filtered

=

negInf
.
clone
();


filtered

=

filtered
.
scatter
(
dim
:

-
1
,

index
:

topkIdx
,

src
:

topkVals
);


return

filtered
;


}


private

static

Tensor

TopPFilter
(
Tensor

logits
,

double

topP
)


{


var

(
sortedLogits
,

sortedIdx
)

=

logits
.
sort
(
dim
:

-
1
,

descending
:

true
);


var

probs

=

torch
.
softmax
(
sortedLogits
,

-
1
);


var

cum

=

torch
.
cumsum
(
probs
,

-
1
);


var

remove

=

cum

>

topP
;


var

keepFirst

=

torch
.
zeros_like
(
remove
);


var

zeroIdx

=

torch
.
tensor
(
new

long
[]

{

0

},

dtype
:

ScalarType
.
Int64
,

device
:

logits
.
device
);


keepFirst

=

keepFirst
.
index_fill
(-
1
,

zeroIdx
,

1
);


remove

=

torch
.
logical_and
(
remove
,

torch
.
logical_not
(
keepFirst
.
to_type
(
ScalarType
.
Bool
)));


var

negInf

=

torch
.
full_like
(
sortedLogits
,

float
.
NegativeInfinity
);


var

filteredSorted

=

torch
.
where
(
remove
,

negInf
,

sortedLogits
);


var

baseline

=

torch
.
full_like
(
logits
,

float
.
NegativeInfinity
);


var

result

=

baseline
.
scatter
(-
1
,

sortedIdx
,

filteredSorted
);


return

result
;


}


}


public

static

class

DataUtils


{


public

static

(
Tensor

X
,

Tensor

Y
)

MakeBatches
(
long
[]

data
,

int

batchSize
,

int

blockSize
,

Device

device
,

Random

rnd
)


{


var

X

=

torch
.
empty
(
new

long
[]

{

batchSize
,

blockSize

},

dtype
:

ScalarType
.
Int64
,

device
:

device
);


var

Y

=

torch
.
empty
(
new

long
[]

{

batchSize
,

blockSize

},

dtype
:

ScalarType
.
Int64
,

device
:

device
);


int

maxStart

=

Math
.
Max
(
0
,

data
.
Length

-

blockSize

-

1
);


if

(
maxStart

==

0

&&

data
.
Length

<

blockSize

+

1
)


throw

new

Exception
(
$"Corpus too small for blockSize=
{
blockSize
}
. Data length=
{
data
.
Length
}
"
);


for

(
int

b

=

0
;

b

<

batchSize
;

b
++)


{


int

start

=

rnd
.
Next
(
0
,

Math
.
Max
(
1
,

maxStart
));


var

sliceX

=

data
.
Skip
(
start
).
Take
(
blockSize
).
ToArray
();


var

sliceY

=

data
.
Skip
(
start

+

1
).
Take
(
blockSize
).
ToArray
();


X
[
b
]

=

torch
.
tensor
(
sliceX
,

dtype
:

ScalarType
.
Int64
,

device
:

device
);


Y
[
b
]

=

torch
.
tensor
(
sliceY
,

dtype
:

ScalarType
.
Int64
,

device
:

device
);


}


return

(
X
,

Y
);


}


}


public

static

class

Schedulers


{


public

static

double

CosineAnneal
(
double

t
,

double

tTotal
,

double

lrMin
,

double

lrMax
)


{


if

(
tTotal

<=

0
)

return

lrMin
;


var

cos

=

(
1.0

+

Math
.
Cos
(
Math
.
PI

*

Math
.
Clamp
(
t

/

tTotal
,

0.0
,

1.0
)))

/

2.0
;


return

lrMin

+

(
lrMax

-

lrMin
)

*

cos
;


}


}


class

Program


{


static

void

Main
(
string
[]

args
)


{


torch
.
random
.
manual_seed
(
1337
);


var

device

=

torch
.
CPU
;


Console
.
WriteLine
(
$"Using device:
{
device
.
type
}
"
);


int

contextLen

=

96
;


int

nLayers

=

4
;


int

nHeads

=

4
;


int

dModel

=

128
;


double

dropout

=

0.15
;


int

batchSize

=

24
;


int

accumSteps

=

2
;


int

maxIters

=

2000
;


int

evalInterval

=

200
;


double

lrMax

=

5e-4
;


double

lrMin

=

5e-5
;


int

warmupIters

=

200
;


double

gradClip

=

1.0
;


string

corpus

=

LoadCorpus
();


var

tokenizer

=

new

CharTokenizer
(
corpus
);


var

data

=

tokenizer
.
Encode
(
corpus
);


int

nTrain

=

(
int
)(
data
.
Length

*

0.9
);


var

trainData

=

data
.
Take
(
nTrain
).
ToArray
();


var

valData

=

data
.
Skip
(
nTrain
).
ToArray
();


var

gpt

=

new

GPT
(
tokenizer
.
VocabSize
,

contextLen
,

nLayers
,

nHeads
,

dModel
,

dropout
).
to
(
device
);


gpt
.
train
();


var

optimizer

=

torch
.
optim
.
AdamW
(
gpt
.
parameters
(),

lr
:

lrMax
,

weight_decay
:

0.1
);


var

rnd

=

new

Random
(
1337
);


for

(
int

iter

=

1
;

iter

<=

maxIters
;

iter
++)


{


gpt
.
train
();


double

lr
;


if

(
iter

<=

warmupIters
)


lr

=

lrMax

*

iter

/

Math
.
Max
(
1
,

warmupIters
);


else


lr

=

Schedulers
.
CosineAnneal
(
iter

-

warmupIters
,

maxIters

-

warmupIters
,

lrMin
,

lrMax
);


foreach

(
var

group

in

optimizer
.
ParamGroups
)

group
.
LearningRate

=

lr
;


Tensor
?

accumLoss

=

null
;


for

(
int

accStep

=

0
;

accStep

<

accumSteps
;

accStep
++)


{


var

(
xb
,

yb
)

=

DataUtils
.
MakeBatches
(
trainData
,

batchSize
,

contextLen
,

device
,

rnd
);


var

(
logits
,

loss
)

=

gpt
.
forward
(
xb
,

yb
);


var

scaledLoss

=

loss
!

/

accumSteps
;


scaledLoss
.
backward
();


if

((
accumLoss

is

null
))


accumLoss

=

loss
!.
detach
();


else


accumLoss

=

accumLoss

+

loss
!.
detach
();


}


torch
.
nn
.
utils
.
clip_grad_norm_
(
gpt
.
parameters
(),

max_norm
:

gradClip
);


optimizer
.
step
();


optimizer
.
zero_grad
();


if

(
iter

%

evalInterval

==

0

||

iter

==

1
)


{


gpt
.
eval
();


var

(
xVal
,

yVal
)

=

DataUtils
.
MakeBatches
(
valData
,

batchSize
,

contextLen
,

device
,

rnd
);


var

(
_
,

valLoss
)

=

gpt
.
forward
(
xVal
,

yVal
);


Console
.
WriteLine
(
$"iter
{
iter
}
/
{
maxIters
}
 | lr
{
lr
:
E2
}
 | train loss
{(
accumLoss
!.
item
<
float
>()

/

accumSteps
):
F4
}
 | val loss
{
valLoss
!.
item
<
float
>():
F4
}
"
);


}


}


gpt
.
eval
();


var

startText

=

"To be, or not to be"
;


var

startIds

=

tokenizer
.
Encode
(
startText
);


var

input

=

torch
.
tensor
(
startIds
,

dtype
:

ScalarType
.
Int64
,

device
:

device
).
unsqueeze
(
0
);


var

sampled

=

gpt
.
Generate
(
input
,

maxNewTokens
:

300
,

temperature
:

0.8
,

topK
:

50
,

topP
:

0.9
);


var

sampledIds

=

sampled
.
squeeze
(
0
).
cpu
().
data
<
long
>().
ToArray
();


var

generated

=

tokenizer
.
Decode
(
sampledIds
);


Console
.
WriteLine
(
"---- Generated ----"
);


Console
.
WriteLine
(
generated
);


}


private

static

string

LoadCorpus
()


{


var

texts

=

new
[]


{


@"To be, or not to be, that is the question:
 Whether 'tis nobler in the mind to suffer
 The slings and arrows of outrageous fortune,
 Or to take Arms against a Sea of troubles,
 And by opposing end them: to die, to sleep;
 No more; and by a sleep, to say we end
 The heart-ache, and the thousand natural shocks
 That Flesh is heir to? 'Tis a consummation
 Devoutly to be wish'd. To die, to sleep,
 To sleep, perchance to Dream; aye, there's the rub,
 For in that sleep of death, what dreams may come,
 When we have shuffled off this mortal coil,
 Must give us pause."
,


@"All the world's a stage,
 And all the men and women merely players;
 They have their exits and their entrances,
 And one man in his time plays many parts,
 His acts being seven ages. At first, the infant,
 Mewling and puking in the nurse's arms.
 Then the whining schoolboy, with his satchel
 And shining morning face, creeping like snail
 Unwillingly to school."
,


@"Friends, Romans, countrymen, lend me your ears;
 I come to bury Caesar, not to praise him.
 The evil that men do lives after them;
 The good is oft interred with their bones;
 So let it be with Caesar. The noble Brutus
 Hath told you Caesar was ambitious:
 If it were so, it was a grievous fault,
 And grievously hath Caesar answer'd it."
,


@"Shall I compare thee to a summer's day?
 Thou art more lovely and more temperate:
 Rough winds do shake the darling buds of May,
 And summer's lease hath all too short a date:
 Sometime too hot the eye of heaven shines,
 And often is his gold complexion dimm'd;
 And every fair from fair sometime declines,
 By chance or nature's changing course untrimm'd;
 But thy eternal summer shall not fade
 Nor lose possession of that fair thou owest;
 Nor shall Death brag thou wander'st in his shade,
 When in eternal lines to time thou growest:
 So long as men can breathe or eyes can see,
 So long lives this and this gives life to thee."


};


return

string
.
Join
(
"\n\n"
,

texts
.
SelectMany
(
t

=>

Enumerable
.
Repeat
(
t
,

100
)));


}


}

}

Enter fullscreen mode

Exit fullscreen mode

## Conclusion

You've just built a GPT-style transformer from scratch in C#! Sure, it won't replace ChatGPT, but that was never the goal. You now understand how attention mechanisms work, how transformers are structured, and how to train neural networks with gradient descent.

This knowledge is valuable whether you're planning to work with large language models professionally or you're just curious about how AI works. The principles you've learned here - attention, embeddings, backpropagation (each iteration performs backpropagation), regularization (like Dropout) - apply to all modern deep learning systems.

The AI age isn't limited to Python developers with massive GPU clusters. With tools like TorchSharp, C# developers can explore, learn, and build real AI systems too. So keep experimenting, keep learning, and most importantly, have fun with it!

## References

* TorchSharp
* Transformer模型详解
* Layer Normalisation & Residual Connection
* Unleashing the Power of Gelu Activation
* Learning Rate in Neural Network
* Training and Validation Loss in Deep Learning

Love C# & AI!

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
