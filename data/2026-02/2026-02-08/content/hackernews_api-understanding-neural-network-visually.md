---
title: Understanding Neural Network, Visually
url: https://visualrambling.space/neural-network/
site_name: hackernews_api
content_file: hackernews_api-understanding-neural-network-visually
fetched_at: '2026-02-08T15:30:56.806468'
original_url: https://visualrambling.space/neural-network/
author: surprisetalk
date: '2026-02-04'
published_date: '2025-07-10T00:00:00+00:00'
description: Understanding Neural Network, Visually
tags:
- hackernews
- trending
---

visualrambling.space

# UNDERSTANDING NEURAL NETWORK, VISUALLY

Loading assets, please wait...

# Understanding Neural Network, Visually

An interactive visualization to understand how neural networks work

tap/click the right side of the screen to go forward →

I’ve always been curious about how AI works.

But with the constant news and updates, I often feel overwhelmed trying to keep up with it all.

So I decided to go back to the basics and start learning from the beginning, with neural networks.

When I'm learning, I find it easier to understand how things work when I can visualize them in my mind.

So I made this visualization, and I'm sharing it now.

I'm just hoping it can also be useful for those of you who are curious about AI and want to learn from the basics.

But a quick disclaimer: I’m not an expert, and I might get things wrong here and there.

If you spot anything off, just let me know. I’d love to learn from you too!

So, what exactly is a neural network?

A neural network is inspired by the structure and functions of biological neural networks.

It works by taking some data as input and processing it through a network of neurons.

Inside each neuron, there’s a rule that decides whether it should be activated.

When that happens, it means the neuron found a pattern in the data that it has learned to recognize.

This process repeats as the data moves through the layers of the network.

The pattern of activation in the final layer represents the output of the task.

Let’s start with a simple use case for a neural network: recognizing a handwritten number.

In this case, the input is an image of a number, and we want the neural network to tell us what number it is.

The output is determined by which neurons in the last layer get activated.

Each one corresponds to a number, and the one with the highest activation tells us the network’s prediction.

To do this, first we need to turn the image into data that the neural network can understand.

In this example, the data will be the brightness value of each pixel in the image.

The neuron will receive a value depending on how bright or dark that part of the image is.

The darker an area (which means there is something written there), the more value a neuron will have.

Once this process is finished, the input neurons will now have values that resemble the input image.

These input values are then passed on to the next layer of neurons to process.

But here’s the key part: before being passed, each value is multiplied by a certain weight.

These weights will be varied for each connection.

It might be positive, negative, less than 1, or more than 1.

The receiving neuron will then sum up all the weighted values it gets.

Then comes the rule we mentioned earlier — usually called an activation function.

There are actually different types of activation functions, but let's use a simple rule for now:

If the total value is greater than a threshold, the neuron activates. Otherwise, it keeps inactive.

If the neuron gets activated, it means it recognized something in the image. Maybe a line, a curve, or a part of a number.

Now imagine we have to do these same operations for every neuron in the next layer.

Each neuron has its own weight and threshold value, so it will react differently to the same input image.

To put it differently, each neuron is looking for a different pattern in the image.

This process repeats layer by layer until we reach the final layer.

At each layer, the neurons process the patterns detected by the previous layer, building on them to recognize more complex patterns.

Until finally, in the last layer, the network has enough information to deduce what number is in the image.

So that’s basically how a neural network works in a nutshell.

It’s a series of simple math operations that process input data to produce an output.

With the right combination of weights and thresholds, the network can learn to map inputs to the right outputs.

In this case, it’s used to map an image of a handwritten number to the correct number.

I’ll stop here for now.

So far, we’ve looked at what a neural network is, how it reads input, performs calculations, and gives an output.

But we haven’t answered the important question:

How do we find the right weights and right thresholds, so that the correct neuron is activated?

That part’s a little tricky — I’m still trying to wrap my head around it and find a good way to visualize it.

So I won’t go into it just yet.

But for now, I hope this gives you a basic understanding of how neural networks work.

See you in the next one 👋

about this project →

visualrambling.space is a personal project by Damar, someone who loves to learn about different topics and rambling about them visually.

If you also love this kind of stuff, feel free to follow me. I'll try to post more content like this in the future!

__________________

https://twitter.com/damarberlari

_blank
