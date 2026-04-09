---
title: Line scan camera image processing
url: https://daniel.lawrence.lu/blog/y2025m09d21/
site_name: hackernews_api
fetched_at: '2025-08-24T22:01:44.582376'
original_url: https://daniel.lawrence.lu/blog/y2025m09d21/
author: Daniel Lawrence Lu
date: '2025-08-24'
description: I use my line scan camera to take cool pictures of trains and other stuff.
tags:
- hackernews
- trending
---

I use my line scan camera to take cool pictures of trains and other stuff.

But there’s a lot that goes into properly processing the images.

FIGURE 1
 A cool tram.
FIGURE 2
 A cool train, the Renfe AVE Class 102, nicknamed
Pato
 because of its duck bill-like appearance.
FIGURE 3
 Cool diesel locomotive.
FIGURE 4
 Nice CRH6A intercity electric multiple unit.
FIGURE 5
 Awesome CR400AF. Super fast.

# 1Principle of operation

The way it works is that the camera has a single column of pixels (or in this case, two columns), that scans at a super high speed.
The camaera is stationary, but as a train moves past it, it gets scanned.

This is essentially also how aphoto finish cameraworks.

Since the background is static, it gets repeated for every column of the image, giving it its distinctive striped look.

FIGURE 6
 Principle of operation of a line scan camera, which produces an image where the horizontal dimension is time rather than space.
source: cmglee on Wikimedia Commons
FIGURE 7
 A 1953 photo finish.
source

Line scan cameras are very suitable for capturing trains, since I can capture the full length of the train with minimal perspective distortion.
This is super nice for train nerds who want to make models of the trains.
Also, as you keep the camera running, you can get incredibly high resolution photos that span over 100,000 pixels wide.

By the way, film photo finish cameras and strip cameras behave almost the same as line scan cameras but with one subtle distinction, which is that you have to pull the film across a strip that’s somewhat wider than a single column of pixels.
This is because film is less sensitive than modern digital image sensors.
However, you’ll need to know the approximate speed of the subject and pull the film across at roughly the right speed.

# 2About the camera

I’m using anAlkeria Necta N4K2-7C.
It has a 4096×2Bayer arrayimage sensor.
I’m saving its raw data in 16 bit binary arrays.

FIGURE 8
 My camera.
FIGURE 9
 Waiting for a subway train to roll by in Brooklyn, New York.

# 3Detecting the region of interest

Sometimes, I keep the line scan camera running for a while, and it generates tons of boring data of the background.
To detect moving things, I compute an “energy function” that’s defined as

1


whereis the maximum pixel value of the image, and the partial derivative are theimage gradient.

FIGURE 10
 Example energy image.

This is because, for a static background, it will be full of horizontal stripes.
By weighing the-direction (time direction) gradient against the total gradient norm, we can find areas where it’s a more vertical-ish structure rather than a horizontal structure.
However, doing this by itself risks noisy gradients in empty (but noisy) areas where the gradient direction is completely random.
The maximum pixel value term ensures that whatever gradient we see is salient.

The image is divided into chunks and the score of a chunk is the 99th percentile energy.

Finally, chunks containing moving objects are defined to be ones where the score is at least 1.5× that of the minimum score.

This heuristic took me longer than I would like to admit to figure out.
Previously, I came up with heuristics that worked well on one capture but couldn’t generalize well to other captures.
Sometimes, the background will contain slowly moving foliage waving in the wind, that would screw up other methods of detection.
That resulted in a lot of wasted time because time spent processing empty regions seriously slows down iteration speed when developing the later steps.

# 4Speed estimation

The most common question I get is, how do I estimate the speed of the subject?
If I don’t do it properly, it will appear stretched out, squished, or flipped.

Typically, I just set the camera to scan as fast as possible while maintaining a decent exposure, so the scan rate is independent of the subject.
Faster subjects will appear squished, and slower subjects will appear stretched out.

For most of my earlier works, I just eyeballed it. A good rule of thumb is to look for round things such as the wheels and “no smoking” signs.
But now I have a fully automated technique that works fairly robustly.

The key idea is to exploit the fact that the line scan camera actually has two lines in aBayer array, where one line is red, green, red, green, and the second line is green, blue, green blue.
By comparing the two green channels, we are able to figure out how fast stuff is moving.

The problem is that the data is very noisy, and salient features are sparse.
Here’s the general approach:

* Divide image into chunks.
* Compute the absolute difference between the 2 green channels of each chunk for various small shifts (from -7 to +7). This gives us a cost array for each chunk.
* Perform subpixel peak interpolation in the cost array using an iteratively reweighted Gaussian,mean shiftstyle. This gives us a shift estimate per chunk.
* Fit a robust spline to the shift estimates.
FIGURE 11
 Interpolating to find the peak using mean shift.
FIGURE 12
 Sample spacing and fitted spline.

As you can see, the data is noisy, but we have surprisingly decent granularity for this very subpixel case where we were scanning slower than needed so the spacing is like 0.5.

The value of the spline is actually thesample spacing. It tells us how close together or far apart the sample points in the original time series we should be using.
This leads us to the next section.

FIGURE 13
 Uncorrected left end. It’s squished!!!
FIGURE 14
 Uncorrected right end. It’s slightly squished but not nearly as much.
FIGURE 15
 Left end of New York subway train.
FIGURE 16
 Right end of New York subway train.

Hmm, I think my speed estimation still isn’t perfect. It could be off by about 10%.
For future work, I think I might be able to extract features correspondences such as SIFT or LightGlue. Trains are full of repeating elements that are supposed to be evenly spaced. I can detect those, and add a cost function to evenly space them, and optimize.
Another idea is to use a circle Hough transform to find circles.

# 5Resampling

From the spline that gives us the sample spacing, we can basically generate the samples as such:

samples

=

[]

sample_position

=

0.0

while

sample_position

<

raw_width
:


samples
.
append
(
sample_position
)


sample_position

+=

spline
(
sample_position
)

However, there are a few gotchas:

* If the spline is negative-valued, it means the subject is going the other way, i.e. the image is flipped. In this case, I start withsample_positionset toraw_widthand go from right to left.
* If the spline goes to zero, we are doomed because the while loop will never terminate. I clamp the steps to at least 0.1 and throw an error if the spline has both positive and negative values.
* This is sort of a naive integration compared to the trapezoidal rule or something. However, given that the spline moves very slowly, it is fine.

Now, for each sample position, we also store the sample width, which is the value of the spline.
If we were to simply extract a single column from the raw data, we would be throwing away a lot of data, and the result wouldn’t be antialiased.
Instead, it is better to pick a window of width proportional to the sample spacing.
I chose aHann window.

FIGURE 17
 Naively selecting columns instead of using a windowing function.
FIGURE 18
 Using a rectangular window.

Not only is the first image very grainy, but the rapidly blinking LED display showing the characters for 筲箕灣 is completely illegible without proper sampling.

FIGURE 19
 Upsampling using a rectangular window.
FIGURE 20
 Upsampling using a Hann window.

As you can see, the rectangular window performs very poorly when upsampling and introduces horrible jagged artifacts. The Hann window does better. Some other windows like the Sinc are even better supposedly.

# 6Demosaicing

Recall that the camera has two lines forming a Bayer array.

If we simply create an image of half resolution (i.e. 2048 pixels tall instead of 4096), by grouping each RGGB group into one pixel, we would have some nasty fringing problems since the red and blue pixels are offset.

FIGURE 21
 Fringing due to bad demosaicing.
FIGURE 22
 Better.

Instead we should write out the image with careful attention to offsets, interpolating as necessary.
Note that the horizontal offsets must be doneafterspeed estimation, because, before speed estimation, the-axis is time, and after speed estimation, the-axis is space.
But the 2-pixel wide Bayer array is physically aspatialoffset.

I implemented a basic interpolation scheme that uses bilinear interpolation.
This fixes most of the fringing, although we can do even better. That will be left for future work.

Unlike a traditional Bayer array, here we have the possibility that the green channels cover 100% of the pixels, so we can potentially do better than traditional demosaicing algorithms.
But there’s currently an annoying problem, which is that the two green channels on my line scan camera don’t match.

# 7Getting rid of the vertical stripes

Vertical stripes in the image are common and are due to two main reasons:

* Clock jitter. The exposure time of each column may be randomly slightly off for some reason.
* I’ve noticed that when a dark object shows up, like the coupling between train cars, the whole slice of the image there is brighter.

To fix this, I use linear regression to fit a basic model of the form:

2


where,, andare scalar parameters of the model,is a 2048-element vector containing the luminance value of the column (mean over the 4 channels), andis the row index (aka the 2048-element vector of.

You can compose models as such:

3


This gives us a new modelwith parameters:

4


The associative property of the composition operator is left as an exercise for the reader.

There is also the identity model, i.e. one that does nothing, which is

5


and there’s also the inverse:

6


so the set of these models forms a mathematical group.

I fit a model to each consecutive pair of columns using weighted least squares, where we assign each row element a weight based on a Gaussian.
The weight would be:

7


In other words, the residual would be

8


After fitting this model, we redo the steps again several times, where thevector is recalculated each time.
This is known asiteratively-reweighted least squaresand is pretty good at rejecting outliers.

FIGURE 23
 The first plot shows the current column’s luminance and previous column’s luminance, as well as the previous column corrected by the model. The second plot shows the weight. The third plot shows the weighted initial and final error.

This all gives usrelativemodels between the previous column and the current column, but we wantglobalmodels that tell us how to correct each column overall.
We could set the global models by just composing them forever, but they would soon start to drift arbitrarily far away from the identity model.

You could prevent them from drifting away by solving a band-diagonal linear system where you have residuals of two types:

* prior residual, penalizing the difference between each model from the identity
* relative model residual, penalizing the difference between the delta between adjacent models and the relative model we computed

This can be solved in. However, it is a bit of work to implement. In practice, you can mitigate most high frequency stripes by just doingexponential smoothing, which basically acts as a high-pass filter

9


for some small, in this case hardcoded to be 0.02.

FIGURE 24
 Before. You can see rather subtle stripes in the dark area.
FIGURE 25
 After.

Previously, I also had some success by directly fitting the model to line up each column with the first column. However, it doesn’t work for captures where the background isn’t static (e.g. rotating line scan panoramas, and pointing the line scan camera out of a moving train).

By the way, I should point out that vertical stripes getting rid of should be donebeforespeed estimation, since it happens in the time domain at capture time.
If a train were speeding up, it would appear stretched out at first, and squished at the end, and the striping would affect the end a lot more than the start.

# 8Denoising

I implemented a patch-based denoiser, also known asblock matching.
It works by making the observation that you often have repeated textures in a line scan photo of a train.
Technically, you also have lots of self-similarity in general photos, so patch-based denoising is a common method for denoising in general.
However, one important distinction is that most denoisers only look in a small neighborhood around the current patch, but mine looks along the entire row.

What I do is, for each row, we process it independently.
From each 3×3 pixel patch, we can construct afeature vectorof size 27 (9 times 3 channels, RGB).
Then, we collect all these features and sort them by mean value.
Now, for each position along the row, we search in the window of size 128 in the sorted vector.
The sorted vector will have similar-looking patches nearby, but we further weigh them by Gaussian similarity to the current patch.
Then, we compute the weighted average of the center pixel of each of those patches.

Another trick is to realize that the noise is Poisson-distributed which has a standard deviation that scales with the square root of the signal.
But if I just square root the input data first, then we just need to compare it to a constant.

This works decently, but is incredibly slow.
Let me know if you think of any faster ways to do it. A KD tree in feature space would die from the curse of dimensionality. Perhaps a hash table? To keep things lightweight, we can limit the population in each cell.

FIGURE 26
 Noisy watch.
FIGURE 27
 Denoised watch.
FIGURE 28
 Noisy passenger.
FIGURE 29
 Denoised passenger.

The good thing about the patch-based denoiser is that unique features like this passenger remain virtually unchanged.

Previously, I also tried using atotal variation denoiser, processing each row and column independently.
It worked decently but would often destroy fine detail in textures.

# 9Skew correction

If the camera isn’t perfectly upright, the resulting image may be slightly skewed.
I’m planning on implementing automatic skew correction.
But here are two caveats:

* skew detection must be done after speed estimation
* proper sampling should happen after skew detection, since the skew transformation introduces generation loss and we can sample directly from the raw data instead.

So basically we’d need to generate a quick, poorly sampled version, run skew detection on it, and then sample it properly afterwards.
We can implement skew detection using aHough transform.
Generally, I do a decent job of keeping the camera upright, so we just need to correct for very small skews, so a Hough transform is suitable (since the complexity scales with the number of bins of the histogram).
We can also use the energy function from the region of interest detector to primarily care about vertical structures.

# 10Color calibration

I kinda just eyeballed this color calibration matrix.

10


But to be honest it looks fairly decent.

FIGURE 30
 People’s skin tones look fine to me.

# 11Implementation details

The code is implemented in Python using numpy.

the code

Due to the large size of the data (4096 rows and hundreds of thousands of columns), it is sometimes impossible to fit all of it in memory, so the code takes several passes and outputs in chunks.
Actually, it is probably okay to fit it in a few gigabytes of RAM, but you’d have to chunk up the storage (there’s no way a contiguous numpy array of 4096 by 100,000 could be allocated).

## 11.1Vibe coding experience

I tried using AI to help with a lot of the implementation. However, the results were mixed.

AI would often accidentally make things quadratic for no reason when a linear time algorithm would suffice. For example, when trying to implement spline-based resampling, ChatGPT 5 came up with horribly slow (but vectorized) code that constructed a giant tensor with a mask across the entire width of the image forevery single sample. Since there are 100,000 samples, and each mask was 100,000 columns wide, you can imagine it would take millennia to run. I ended up reimplementing it from scratch by hand. Then Grok 4 implemented weighted least squares regression by materializing the entire weight vector withnp.diaginstead of simply pre-multiplying each row ofAandxwith the square root of the weight before doingnp.linalg.solve(A, x). Again, with 100,000 elements, making the square matrix withnp.diagwould have instantly run out of memory.

Both Grok 4 Expert and ChatGPT 5 Thinking also completely failed to implement the band-diagonal least squares to my vertical stripes strategy, but as mentioned, the exponential smoothing trick works okay for now.

However, for some other stuff, AI was quite helpful.
It created a class that dynamically loads chunks from disk but provides the API to index and slice it.
That was neat.
AI was also incredibly good at helping with Matplotlib’s arcane syntax.

# 12Other people’s line scan photography of trains

## 12.1Adam Magyar

Adam Magyaruses a black and white digital line scan camera for his “Stainless” project, and another derived from a scanner for his “Urban Flow” project.

His camera must have much better sensitivity than mine since he managed to capture fairly clean images even for underground trains (whereas I generally require sunlight for mine).
Apparently, he had to scout out many subway stations to find ones where the lights don’t flicker at 60 Hz.

## 12.2KR64’s blog

Atkr64.seesaa.netyou can find a mind boggling collection of high quality line scan photos of trains from all across Japan.

They probably do this full time as the variety of trains is far greater than I can ever hope to achieve.
I believe they use a film slit scan camera.

Unfortunately, their website has a bunch of technical issues and often goes down. I would be happy to help them out but my Japanese is very poor and I don’t see any way to contact them.
