---
title: MicroGPT explained interactively | growingSWE
url: https://growingswe.com/blog/microgpt
site_name: hackernews_api
content_file: hackernews_api-microgpt-explained-interactively-growingswe
fetched_at: '2026-03-02T11:17:46.534250'
original_url: https://growingswe.com/blog/microgpt
author: growingswe
date: '2026-03-01'
published_date: '2026-03-01'
description: Walk through Karpathy's 200-line GPT from scratch. Tokenize names into integers, watch softmax convert scores to probabilities, step through backpropagation on a computation graph, explore attention heatmaps, and see a tiny model learn to generate plausible names.
tags:
- hackernews
- trending
---

# MicroGPT explained interactively

Trying my best to visualize it. I'm a n00b at machine learning though

Andrej Karpathy wrote a 200-line Python script that trains and runs a GPT from scratch, with no libraries or dependencies, just pure Python. The script contains the algorithm that powers LLMs like ChatGPT.

Let's walk through it piece by piece and watch each part work.Andrej did a walkthrough on his blog, but here I take a more visual approach, tailored for beginners.

## The dataset

The model trains on 32,000 human names, one per line: emma, olivia, ava, isabella, sophia... Each name is a document. The model's job is to learn the statistical patterns in these names and generate plausible new ones that sound like they could be real.

By the end of training, the model produces names like "kamon", "karai", "anna", and "anton".The model has learned which characters tend to follow which, which sounds are common at the start vs. the end, and how long a typical name runs. From ChatGPT's perspective, your conversation is just a document. When you type a prompt, the model's response is a statistical document completion.

## Numbers, not letters

Neural networks work with numbers, not characters. So we need a way to convert text into a sequence of integers and back. The simplest possible tokenizer assigns one integer to each unique character in the dataset. The 26 lowercase letters get ids 0 through 25, and we add one special token called BOS (Beginning of Sequence) with id 26 that marks where a name starts and ends.

Type a name below and watch it get tokenized. Each character maps to its integer id, and BOS tokens wrap both ends:

Tokenizer
BOS
26
e
4
m
12
m
12
a
0
BOS
26
char
token
vocab size
27
sequence length
6
unique chars
a-z + BOS
Name

The integer values themselves have no meaning. Token 4 isn't "more" than token 2. Each token is just a distinct symbol, like assigning a different color to each letter. Production tokenizers like tiktoken (used by GPT-4) work on chunks of characters for efficiency, giving a vocabulary of ~100,000 tokens, but the principle is the same.

## The prediction game

Here's the core task: given the tokens we've seen so far, predict what comes next. We slide through the sequence one position at a time. At position 0, the model sees only BOS and must predict the first letter. At position 1, it sees BOS and the first letter and must predict the second letter. And so on.

Step through the sequence below and watch the context grow while the target shifts forward:

Next-token prediction
sequence
BOS
input
e
target
m
m
a
BOS
Given [BOS] → predict "e"
Given [BOS, e] → predict "m"
Given [BOS, e, m] → predict "m"
Given [BOS, e, m, m] → predict "a"
Given [BOS, e, m, m, a] → predict "BOS"
1
 / 
5

Each step produces one training example: the context on the left is the input, the green token on the right is what the model should predict. For the name "emma", that's five input-target pairs. This sliding window is how all language models train, including ChatGPT.

## From scores to probabilities

At each position, the model outputs 27 raw numbers, one per possible next token. These numbers (calledLogits) can be anything: positive, negative, large, small. We need to convert them into probabilities that are positive and sum to 1.Softmaxdoes this by exponentiating each score and dividing by the total.

Adjust the logits below and watch the probability distribution change. Notice how one large logit dominates, and the exponential amplifies differences.

Softmax
a
22.1
%
b
8.1
%
c
4.9
%
d
1.8
%
e
60.0
%
other
3.0
%
probability
a
:
2.0
b
:
1.0
c
:
0.5
d
:
-0.5
e
:
3.0
other
:
0.0

Here's the actual softmax code from microgpt. Step through it to see the intermediate values at each line:

Softmax step-through
PYTHON
1
def
 
softmax
(
logits
)
:
2
 
max_val
 
=
 
max
(
val
.
data
 
for
 
val
 
in
 
logits
)
3
 
exps
 
=
 
[
(
val
 
-
 
max_val
)
.
exp
(
)
4
 
for
 
val
 
in
 
logits
]
5
 
total
 
=
 
sum
(
exps
)
6
 
return
 
[
e
 
/
 
total
 
for
 
e
 
in
 
exps
]
VALUES
a
1.200
e
2.800
m
0.500
n
1.800
BOS
-0.300
softmax([1.2, 2.8, 0.5, 1.8, -0.3])
max_val = 2.8
exps = [exp(logit - 2.8) for each logit]
total = sum(exps) = 1.715
probs = [e / 1.715 for each e]
1
 / 
5

The subtraction of the max value before exponentiating doesn't change the result mathematically (dividing numerator and denominator by the same constant cancels out) but prevents overflow. Without it,exp(100)would produce infinity.

## Measuring surprise

How wrong was the prediction? We need a single number that captures "the model thought the correct answer was unlikely." If the model assigns probability 0.9 to the correct next token, the loss is low (0.1). If it assigns probability 0.01, the loss is high (4.6). The formula is−log⁡(p)-\log(p)−log(p)wherepppis the probability the model assigned to the correct token. This is calledcross-entropy loss.

Drag the slider to adjust the probability of the correct token and watch the loss change:

Cross-entropy loss
0
1
2
3
4
5
0
0.25
0.5
0.75
1
probability of correct token
loss
1.20
P(correct)
30%

The curve has two properties that make it useful. First, it's zero when the model is perfectly confident in the right answer (p=1p = 1p=1). Second, it goes to infinity as the model assigns near-zero probability to the truth (p→0p \to 0p→0), which punishes confident wrong answers severely. Training minimizes this number.

## Tracking every calculation

To improve, the model needs to answer: "for each of my 4,192parameters, if I nudge it up by a tiny amount, does the loss go up or down, and by how much?"Backpropagationcomputes this by walking the computation backward, applying thechain ruleat each step.

Every mathematical operation (add, multiply, exp, log) is a node in a graph. Each node remembers its inputs and knows its local derivative. The backward pass starts at the loss (where theGradientis trivially 1.0) and multiplies local derivatives along every path back to the inputs.

Step through the forward pass, then the backward pass for a small example whereL=a⋅b+aL = a \cdot b + aL=a⋅b+awitha=2,b=3a = 2, b = 3a=2,b=3:

Computation graph
FORWARD
|
BACKWARD
a
2.0
b
c
L
*
+
Input a = 2.0
Input b = 3.0
c = a * b = 2.0 * 3.0 = 6.0
L = c + a = 6.0 + 2.0 = 8.0
Start: dL/dL = 1.0
dL/dc = 1 * 1.0 = 1.0 (addition passes gradient through)
dL/da += 1 * 1.0 = 1.0 (from the + path)
dL/da += b * dL/dc = 3.0 * 1.0 = 3.0 (total: 4.0)
dL/db = a * dL/dc = 2.0 * 1.0 = 2.0
1
 / 
9

Now step through the actualValueclass code. Watch how each operation records its children and local gradients, then howbackward()walks the graph in reverse, accumulating gradients:

Value class and backward()
PYTHON
1
class
 
Value
:
2
 
def
 
__init__
(
self
,
 
data
,
 
children
=
(
)
,
 
local_grads
=
(
)
)
:
3
 
self
.
data
 
=
 
data
4
 
self
.
grad
 
=
 
0
5
 
self
.
_children
 
=
 
children
6
 
self
.
_local_grads
 
=
 
local_grads
7
 
8
 
def
 
__add__
(
self
,
 
other
)
:
9
 
return
 
Value
(
self
.
data
 
+
 
other
.
data
,
10
 
(
self
,
 
other
)
,
 
(
1
,
 
1
)
)
11
 
12
 
def
 
__mul__
(
self
,
 
other
)
:
13
 
return
 
Value
(
self
.
data
 
*
 
other
.
data
,
14
 
(
self
,
 
other
)
,
 
(
other
.
data
,
 
self
.
data
)
)
15
 
16
 
def
 
backward
(
self
)
:
17
 
# topological sort
18
 
topo
 
=
 
[
]
19
 
visited
 
=
 
set
(
)
20
 
def
 
build_topo
(
v
)
:
21
 
if
 
v
 
not
 
in
 
visited
:
22
 
visited
.
add
(
v
)
23
 
for
 
child
 
in
 
v
.
_children
:
24
 
build_topo
(
child
)
25
 
topo
.
append
(
v
)
26
 
build_topo
(
self
)
27
 
self
.
grad
 
=
 
1
28
 
for
 
v
 
in
 
reversed
(
topo
)
:
29
 
for
 
child
,
 
lg
 
in
 
zip
(
v
.
_children
,
 
v
.
_local_grads
)
:
30
 
child
.
grad
 
+
=
 
lg
 
*
 
v
.
grad
STATE
creating values
VAR
DATA
GRAD
a
2.0
0
a = Value(2.0)
b = Value(3.0)
c = a * b → data=6.0, local_grads=(b.data=3, a.data=2)
L = c + a → data=8.0, local_grads=(1, 1)
Topological sort: [a, b, c, L] (dependencies before dependents)
L.grad = 1 (dL/dL = 1)
Process L: children=(c, a), local_grads=(1, 1)
Process c: children=(a, b), local_grads=(3, 2)
1
 / 
8

Notice thataaahas a gradient of 4.0, not 3.0. That's becauseaaais used in two places: once in the multiplication (∂(a⋅b)/∂a=b=3\partial(a \cdot b)/\partial a = b = 3∂(a⋅b)/∂a=b=3) and once in the addition (∂(c+a)/∂a=1\partial(c + a)/\partial a = 1∂(c+a)/∂a=1). The gradients from both paths sum up:3+1=43 + 1 = 43+1=4. This is the multivariable chain rule in action. If a value contributes to the loss through multiple paths, the total derivative is the sum of contributions from each path.

This is the same algorithm that PyTorch'sloss.backward()runs, operating on scalars instead of tensors.

## From IDs to meaning

We know how to measure error and how to trace that error back to every parameter. Now let's build the model itself, starting with how it represents tokens.

A raw token id like 4 is just an index. The model can't do math with a bare integer. So each token looks up a learned vector (a list of 16 numbers) from anEmbeddingtable. Think of it as each token having a 16-dimensional "personality" that the model can adjust during training.

Position matters too. The letter "a" at position 0 plays a different role than "a" at position 4. So there's a second embedding table indexed by position. The token embedding and position embedding are added together to form the input to the rest of the network.

Click a token below to see its embedding vectors and how they combine:

Embedding lookup
BOS
e
m
m
a
token emb
-0.08
0.04
-0.01
0.06
-0.03
0.07
-0.05
0.02
+
pos emb
-0.01
0.06
-0.03
0.02
-0.05
0.04
-0.07
0.01
=
combined
-0.09
0.10
-0.04
0.08
-0.08
0.11
-0.12
0.03
d
0
d
1
d
2
d
3
d
4
d
5
d
6
d
7
showing 8 of 16 dimensions

The embedding values start as small random numbers and get tuned during training. After training, tokens that behave similarly (like vowels) tend to end up with similar embedding vectors. The model learns these representations from scratch, with no prior knowledge of what a vowel is.

## How tokens talk to each other

This is howtransformerswork. At each position, the model needs to gather information from previous positions. It does this throughAttention: each token produces three vectors from its embedding.

AQuery("what am I looking for?"), aKey("what do I contain?"), and aValue("what information do I offer if selected?"). The query at the current position is compared against all keys from previous positions viadot product. High dot product means high relevance. Softmax converts these scores into attention weights, and the weighted sum of values is the output.

Explore the attention weights below. Each cell shows how much one position attends to another. Switch between the four attention heads to see different patterns:

Attention weights
BOS
e
m
m
a
BOS
BOS
e
m
m
a
BOS
key position
query
100
35
65
15
30
55
8
12
35
45
5
10
15
30
40
4
8
12
18
28
30
Head 
1
Head 
2
Head 
3
Head 
4

The gray region in the upper-right is the causal mask. Position 2 can't attend to position 4 because position 4 hasn't happened yet. This is what makes the modelAutoregressive: each position only sees the past.

Different heads learn different patterns. One head might attend strongly to the most recent token. Another might focus on the BOS token (to remember "we're generating a name"). A third might look for vowels. The four heads run in parallel, each operating on a 4-dimensional slice of the 16-dimensional embedding, and their outputs are concatenated and projected back to 16 dimensions.

## The full picture

The model pipes each token through: embed, normalize, attend, addresidual, normalize, MLP, add residual, project to output logits. TheMLP(multilayer perceptron) is a two-layer feed-forward network: project up to 64 dimensions, applyReLU(zero out negatives), project back to 16. If attention is how tokens communicate, the MLP is where each position thinks independently.

Step through the pipeline for one token and watch data flow through each stage:

GPT forward pass
Token
Token
Embed
Pos
Embed
Add
RMS
Norm
Attn
Add
RMS
Norm
MLP
Add
Output
Logits
vector dimension: 16 (except output: 27)
Input token: "e" (id=4)
Look up token embedding (row 4 of wte)
Look up position embedding (row 1 of wpe)
Add token + position embeddings
Normalize: scale to unit root-mean-square
Multi-head attention: Q·K → weights → weighted V
Residual connection: add attention output to input
Normalize before MLP
Linear → ReLU → Linear (per-position thinking)
Residual connection: add MLP output to input
27 scores, one per possible next token
1
 / 
11

Here's the actualgpt()function from microgpt. Step through to see the code executing line by line, with the intermediate vector at each stage:

GPT forward pass
PYTHON
1
def
 
gpt
(
token_id
,
 
pos_id
,
 
keys
,
 
values
)
:
2
 
tok_emb
 
=
 
state_dict
[
"wte"
]
[
token_id
]
3
 
pos_emb
 
=
 
state_dict
[
"wpe"
]
[
pos_id
]
4
 
x
 
=
 
[
t
 
+
 
p
 
for
 
t
,
 
p
 
in
 
zip
(
tok_emb
,
 
pos_emb
)
]
5
 
x
 
=
 
rmsnorm
(
x
)
6
 
7
 
for
 
li
 
in
 
range
(
n_layer
)
:
8
 
x_residual
 
=
 
x
9
 
x
 
=
 
rmsnorm
(
x
)
10
 
q
 
=
 
linear
(
x
,
 
attn_wq
)
11
 
k
 
=
 
linear
(
x
,
 
attn_wk
)
12
 
v
 
=
 
linear
(
x
,
 
attn_wv
)
13
 
keys
[
li
]
.
append
(
k
)
14
 
values
[
li
]
.
append
(
v
)
15
 
# multi-head attention
16
 
for
 
h
 
in
 
range
(
n_head
)
:
17
 
attn_logits
 
=
 
[
q_h
 
.
 
k_h
[
t
]
 
/
 
sqrt
(
d
)
18
 
for
 
t
 
in
 
range
(
len
(
k_h
)
)
]
19
 
attn_weights
 
=
 
softmax
(
attn_logits
)
20
 
head_out
 
=
 
weighted_sum
(
attn_weights
,
 
v_h
)
21
 
x
 
=
 
linear
(
x_attn
,
 
attn_wo
)
22
 
x
 
=
 
[
a
 
+
 
b
 
for
 
a
,
 
b
 
in
 
zip
(
x
,
 
x_residual
)
]
23
 
24
 
x_residual
 
=
 
x
25
 
x
 
=
 
rmsnorm
(
x
)
26
 
x
 
=
 
linear
(
x
,
 
mlp_fc1
)
27
 
x
 
=
 
[
xi
.
relu
(
)
 
for
 
xi
 
in
 
x
]
28
 
x
 
=
 
linear
(
x
,
 
mlp_fc2
)
29
 
x
 
=
 
[
a
 
+
 
b
 
for
 
a
,
 
b
 
in
 
zip
(
x
,
 
x_residual
)
]
30
 
31
 
logits
 
=
 
linear
(
x
,
 
lm_head
)
32
 
return
 
logits
VECTOR
processing...
gpt(token_id=4, pos_id=1, ...) — processing "e" at position 1
Look up token embedding: row 4 (for "e") from wte table
Look up position embedding: row 1 from wpe table
Add token + position embeddings element-wise
RMSNorm: scale x to unit root-mean-square
Enter layer 0. Save x_residual, normalize x again
Project x into Query, Key, Value vectors (3 matrix multiplies)
Append K and V to the KV cache for future positions to see
Multi-head attention: 4 heads each compute Q·K scores, softmax, weighted V sum
Project concatenated head outputs through output projection (attn_wo)
Residual connection: add attention output back to the saved input
MLP: save residual, normalize, project up to 64 dimensions
ReLU: zero out all negative values
Project back down to 16 dimensions
Residual connection: add MLP output back to its input
Final projection: multiply by lm_head to get 27 logits (one per token)
1
 / 
16

The residual connections (the "Add" steps) are load-bearing. Without them, gradients would shrink to near-zero by the time they reach the early layers, and training would stall. The residual connection gives gradients a shortcut, which is why deep networks can train at all.

RMSNorm (root-mean-square normalization) rescales each vector to have unit root-mean-square. This prevents activations from growing or shrinking as they pass through the network, which stabilizes training. GPT-2 used LayerNorm; RMSNorm is simpler and works just as well.

## Learning

The training loop repeats 1,000 times: pick a name, tokenize it, run the model forward over every position, compute the cross-entropy loss at each position, average the losses, backpropagate to get gradients for every parameter, and update the parameters to make the loss a bit lower.

The optimizer is Adam, which is smarter than naive gradient descent. It maintains a running average of each parameter's recent gradients (momentum) and a running average of the squared gradients (adaptivelearning rate). Parameters that have been getting consistent gradients take larger steps. Parameters that have been oscillating take smaller ones.

Watch the loss decrease over 1,000 training steps. The model starts at ~3.3 (random guessing among 27 tokens:−log⁡(1/27)≈3.3-\log(1/27) \approx 3.3−log(1/27)≈3.3) and settles around 2.37. The generated names evolve from gibberish to plausible:

Training
2.5
3.0
3.5
random guessing
training step
generated names
xqbzjf
mwplkt
gvrcnx
step
0
loss
3.37
1
 / 
100

Step through the code for one complete training iteration. Watch it pick a name, run the forward pass at each position, compute the loss, run backward, and update the parameters:

One training step
PYTHON
1
# Pick a document and tokenize it
2
doc
 
=
 
docs
[
step
 
%
 
len
(
docs
)
]
3
tokens
 
=
 
[
BOS
]
 
+
 
[
uchars
.
index
(
ch
)
 
for
 
ch
 
in
 
doc
]
 
+
 
[
BOS
]
4
 
5
# Forward pass: predict each next token
6
keys
,
 
values
 
=
 
[
[
]
 
for
 
_
 
in
 
range
(
n_layer
)
]
,
 
[
.
.
.
]
7
losses
 
=
 
[
]
8
for
 
pos_id
 
in
 
range
(
n
)
:
9
 
token_id
 
=
 
tokens
[
pos_id
]
10
 
target_id
 
=
 
tokens
[
pos_id
 
+
 
1
]
11
 
logits
 
=
 
gpt
(
token_id
,
 
pos_id
,
 
keys
,
 
values
)
12
 
probs
 
=
 
softmax
(
logits
)
13
 
loss_t
 
=
 
-
probs
[
target_id
]
.
log
(
)
14
 
losses
.
append
(
loss_t
)
15
loss
 
=
 
(
1
/
n
)
 
*
 
sum
(
losses
)
16
 
17
# Backward pass
18
loss
.
backward
(
)
19
 
20
# Adam optimizer update
21
for
 
i
,
 
p
 
in
 
enumerate
(
params
)
:
22
 
m
[
i
]
 
=
 
beta1
 
*
 
m
[
i
]
 
+
 
(
1
 
-
 
beta1
)
 
*
 
p
.
grad
23
 
v
[
i
]
 
=
 
beta2
 
*
 
v
[
i
]
 
+
 
(
1
 
-
 
beta2
)
 
*
 
p
.
grad
*
*
2
24
 
m_hat
 
=
 
m
[
i
]
 
/
 
(
1
 
-
 
beta1
 
*
*
 
(
step
+
1
)
)
25
 
v_hat
 
=
 
v
[
i
]
 
/
 
(
1
 
-
 
beta2
 
*
*
 
(
step
+
1
)
)
26
 
p
.
data
 
-
=
 
lr
 
*
 
m_hat
 
/
 
(
v_hat
*
*
0.5
 
+
 
eps
)
27
 
p
.
grad
 
=
 
0
STATE
load data
emma
Pick document: "emma"
Tokenize: [BOS, e, m, m, a, BOS] (length 6)
Initialize empty KV cache and loss list
Position 0: input="BOS" → predict "e", loss=3.30
Position 1: input="e" → predict "m", loss=3.15
Position 2: input="m" → predict "m", loss=3.42
Position 3: input="m" → predict "a", loss=3.28
Position 4: input="a" → predict "BOS", loss=2.95
Average loss = 3.220
loss.backward() — compute gradient for all 4,192 parameters
Adam update: nudge each parameter using its gradient, momentum, and adaptive learning rate
1
 / 
11

## Making things up

Once training is done,Inferenceis straightforward. Start with BOS, run the forward pass, get 27 probabilities, randomly sample one token, feed it back in, and repeat until the model outputs BOS again (meaning "I'm done") or we hit the maximum length.

Temperature controls how we sample. Before softmax, we divide the logits by the temperature. A temperature of 1.0 samples directly from the learned distribution. Lower temperatures sharpen the distribution (the model picks its top choices more often). Higher temperatures flatten it (more diverse but potentially less coherent output).

Adjust the temperature and watch the probability distribution change:

Temperature sampling
original distribution from the model
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
28
%
temperature
1.0
entropy
3.64
top token
e
Temperature
1.0

Step through the inference loop to see a name being generated character by character. At each step, the model runs forward, produces probabilities, and samples the next token:

Generating a name
PYTHON
1
temperature
 
=
 
0.5
2
keys
,
 
values
 
=
 
[
[
]
 
for
 
_
 
in
 
range
(
n_layer
)
]
,
 
[
.
.
.
]
3
token_id
 
=
 
BOS
4
sample
 
=
 
[
]
5
 
6
for
 
pos_id
 
in
 
range
(
block_size
)
:
7
 
logits
 
=
 
gpt
(
token_id
,
 
pos_id
,
 
keys
,
 
values
)
8
 
probs
 
=
 
softmax
(
[
l
 
/
 
temperature
 
for
 
l
 
in
 
logits
]
)
9
 
token_id
 
=
 
random
.
choices
(
10
 
range
(
vocab_size
)
,
11
 
weights
=
[
p
.
data
 
for
 
p
 
in
 
probs
]
)
[
0
]
12
 
if
 
token_id
 
=
=
 
BOS
:
13
 
break
14
 
sample
.
append
(
uchars
[
token_id
]
)
15
 
16
print
(
""
.
join
(
sample
)
)
OUTPUT
generated
(empty)
Initialize: temperature=0.5, start with BOS token
Position 0: run gpt(BOS, 0, ...)
Softmax with temperature=0.5, sample → "k"
"k" is not BOS → append to sample: "k"
Position 1: run gpt("k", 1, ...)
Softmax with temperature=0.5, sample → "a"
"a" is not BOS → append to sample: "ka"
Position 2: run gpt("a", 2, ...)
Softmax with temperature=0.5, sample → "r"
"r" is not BOS → append to sample: "kar"
Position 3: run gpt("r", 3, ...)
Softmax with temperature=0.5, sample → "a"
"a" is not BOS → append to sample: "kara"
Position 4: run gpt("a", 4, ...)
Softmax with temperature=0.5, sample → "i"
"i" is not BOS → append to sample: "karai"
Sampled BOS → break out of loop
Output: "karai"
1
 / 
18

A temperature approaching 0 would always pick the highest-probability token (greedy decoding). This produces the most "average" output. A temperature of 1.0 matches what the model actually learned. Values above 1.0 inject extra randomness, which can produce creative outputs but also nonsense. The sweet spot for names is around 0.5.

## Everything else is efficiency

This 200-line script contains the complete algorithm. Between this and ChatGPT, litte changes conceptually. The differences are things like: trillions of tokens instead of 32,000 names. Subword tokenization (100K vocabulary) instead of characters. Tensors on GPUs instead of scalarValueobjects in Python. Hundreds of billions of parameters instead of 4,192. Hundreds of layers instead of one. Training across thousands of GPUs for months.

But the loop is the same. Tokenize, embed, attend, compute, predict the next token, measure surprise, walk the gradients backward, nudge the parameters. Repeat.