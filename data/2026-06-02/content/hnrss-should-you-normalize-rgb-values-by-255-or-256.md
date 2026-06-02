---
title: Should you normalize RGB values by 255 or 256?
url: https://30fps.net/pages/255-vs-256-division/
site_name: hnrss
content_file: hnrss-should-you-normalize-rgb-values-by-255-or-256
fetched_at: '2026-06-02T12:21:42.881232'
original_url: https://30fps.net/pages/255-vs-256-division/
date: '2026-06-01'
description: Should you normalize RGB values by 255 or 256?
tags:
- hackernews
- hnrss
---

30fps.net
 — Computer Graphics & Programming with Pekka Väänänen

Let’s say you’re writing an image processing program.
The program takes in an image, converts it to floating point, does some processing and finally saves the modified pixels to disk as 8-bit colors.
The question today concerns how exactly the integer-to-float conversion should be done.
There are two approaches which, written in Python and NumPy, look like this:

Standard division by 255

Alternative division by 256

pixels 
=
 img 
/
 
255.0

result 
=
 process(pixels)

output 
=
 np.trunc(result 
*
 
255
 
+
 
0.5
)

pixels 
=
 (img 
+
 
0.5
) 
/
 
256.0

result 
=
 process(pixels)

output 
=
 np.trunc(result 
*
 
256
)

I assume that in both cases the output values are clamped before the final typecast:

# Clamp and cast to 8 bits

output_8bit 
=
 output.clip(
0
, 
255
).astype(np.uint8)

The standard approach maps the integer 0 to 0.0 and 255 to 1.0.
It works perfectly fine and ishow GPUs do it.
The alternative adds a 0.5 bias and divides by 256 instead, so the integer 0 gets mapped to0.5/256=0.001953125.
This is inconvenient because your image processing code can’t detect black pixels, for example, without knowing the above constant.
As a consequence, you tie your logic to 8-bit inputs even if you compute in floating point.
With the standard approach, you can always assume black is 0.0.

But some programmers still feel a pull towards the alternative.
What is going on?
What do they see in it?

## The case against 255.0

The standard approach does look quite strange when plotted on the number line.
Below you can see an exaggerated version with 3-bit integers in the range[0..7]being mapped to[0,1]:

On the X-axis we’ve got a number line and the locations of brown circles on it represent the decoded floating-point values.
The numbers inside are the integer inputs.
Each integer has arrows pointing to it; these show a range of floating-point values that round to it.
I’ll call these ranges “bins” in the rest of this article.

### Smaller bins at the extremes

The first issue really apparent in the diagram is how the standard formula’s extreme bins jut beyond the[0,1]range.
Perhaps this visualization is unfair – both approaches clamp their output so the extreme bins could extend infinitely – but it clearly shows how “stretched” the standard range is.
The stretched range is wider than the assumed operating range[0, 1]in image processing.

This means that when converting floating-point values in the[0, 1]range back to integers, the extreme bins have effectively half the width of other bins.
As a consequence, it will be “harder” to output extreme values from your algorithm.
For example, if you generate uniform[0,1]noise and round it using the standard formula, the values 0 and 255 will occur only half as frequently as other integers.

We can verify this claim empirically by generating a million uniform random numbers, plotting them as a histogram, and observing that both the 0 and 255 bins are indeed only half as tall as other bins:

The highlighted crop:

Histogram code

import
 numpy 
as
 np

import
 matplotlib.pyplot 
as
 plt

result 
=
 np.random.uniform(
0
, 
1
, 
1000000
)

final_values 
=
 np.trunc(result 
*
 
255
 
+
 
0.5
).clip(
0
, 
255
).astype(np.uint8)

plt.hist(final_values, bins
=
256
, 
range
=
(
0
, 
255
))

plt.show()

Still, I’m having a hard time coming up with an example situation where the bias away from the extremes would prove problematic.
Sure, the standard approach’s floats are spread over a wider range, but the original image will still round-trip convert losslessly (uint8 → float → uint8).

Also, any result value just beyond 0.0 or 1.0 will still round to the right bin, evening out the output distribution.
An example of what I mean.
Assume your processing subtracts 0.005 from the floating-point colors.
In the standard approach this pushes blacks below zero – outside the[0,1]range – but in the alternative the values stay positive.
In the end both output the integer 0 anyway:

Standard:
trunc(255 * (-0.005) + 0.5) = 0

Alternative:
trunc(256 * (0.5 / 256 - 0.005)) = 0

It didn’t matter that in the standard approach the zero bin was only “half the size”.

### Inexactness

The second issue is that the standard approach’s floating-point values aren’t exact.
For example128/255.0 \approx 0.501961but128/256.0 = 0.5.
Due to this round-off error, the distances between floating-point values vary a tiny bit.
But this isn’t a real problem since the error is trulytiny.
A 32-bit floating-point number has a 23-bit fraction (“significand”).
We are talking about round-off error in its least-significant bit; jitter with the magnitude less than2^{-23}.
Surely a relative error of 0.00001 % is immaterial even in the most sophisticated image processing task.
In this case, inexactness is an aesthetic question, not a technical one.

### Values not in between integers

The alternative approach always places each floating-point value exactly in the middle of two integers.
See how the vertical bars align in the number line diagram above.
The halfway position can be thought of as a compromise; we don’t know what the original quantized value was exactly, and thus the average point between two successive integers is a good guess.

I’m sure there are applications where this property is useful, even though I’m having a hard time coming up with examples myself.
Well, at least dithering is more convenient, argues a 2015 blog post“Converting Color Depth”by Andrew Kesler (known for hisbusiness card raytracer).
The reasoning goes that noise can be added without worrying about edge cases.
In contrast, the standard formula’s awkward extremes requirecareful handlingto keep the noise distribution consistent.

## Two types of quantizers

So far the standard “divide by 255” formula still looks solid, or at least firm enough to still be worth it.
Another way to think about the question is to zoom out a bit and see the two approaches as two differentuniform scalar quantizers.
If we check theWikipedia page on quantization, we’ll quickly learn that there are two main types of quantizers:

Most uniform quantizers for signed input data can be classified as being of one of two types:mid-riserandmid-tread. The terminology is based on what happens in the region around the value 0, and uses the analogy of viewing the input-output function of the quantizer as a stairway. Mid-tread quantizers have a zero-valued reconstruction level (corresponding to a tread of a stairway), while mid-riser quantizers have a zero-valued classification threshold (corresponding to a riser of a stairway).

As a source Wikipedia citesa 1977 paperthat has such an incredible combined title and abstract layout that I must reproduce it here:

“Quantization” by Allen Gresho. IEEE Communications Society Magazine, September 1977.

Anyway.
When plotted on a graph, the mid-riser and mid-tread quantizers differ where they cross zero:

Mid-tread indeed maps zero to zero and mid-riser maps zero to the middle of two integers (sound familiar?).
The notation chosen by Wikipedia represents an input real number withx, its encoded (“classified”) integer value withk, and reconstructed real number withy_k.
The corresponding quantizer formulas look like this:

Type

Classify (encode)

Reconstruct (decode)

Mid-tread staircase quantizer

k = \text{trunc}(x L + 0.5)

y_k=k/L

Mid-riser staircase quantizer

k = \text{trunc}(x L)

y_k=(k+0.5)/L

Lstands for the number of distinct output levels (for example 256).

If we apply these definitions to our two competing approaches, we can call the standard formula a “mid-riser” with L=255 and the alternative a “mid-tread” with L=256.
Actually, I’ll show their code again with the new labels to make the connection to the new formulas above clear.
The code snippets themselves are the same as in the beginning.

Mid-tread quantizer (L=255)

Mid-riser quantizer (L=256)

pixels 
=
 img 
/
 
255.0

result 
=
 process(pixels)

output 
=
 np.trunc(result 
*
 
255
 
+
 
0.5
)

pixels 
=
 (img 
+
 
0.5
) 
/
 
256.0

result 
=
 process(pixels)

output 
=
 np.trunc(result 
*
 
256
)

From this perspective we can say the standard approach is a strange combination of a mid-riser quantizer for unsigned inputs (the quote said “for signed input data”) and a choice ofL=255integer codes.
Clearly this is not optimal for 8-bit inputs.
Again, this is all for the programming convenience of having the extremes map to 0.0 and 1.0.
This leads to the final criticism of the standard formula.

### Higher quantization error but not really

If we were designing a system that receives a uniformly distributed real numberx \in [0,1], encodes it as an 8-bit integerk, and finally reconstructs it as another real numbery_k, the standard formula would waste bandwidth.
Remember how the 0 and 255 bins poked slightly beyond the[0,1]range’s edges?
In the standard approach, the range of representable values is actually[-0.5/255, 255.5/255], meaning the bins are spaced further apart than strictly needed for[0, 1]inputs, leading to a higher reconstruction error.
The increase in error is small, however.
According to StackOverflow userPeter Mudrievskij’s calculation, the mean absolute errors are1/1020and1/1024for 255 and 256 divisors, respectively.
Thus division by 256 is theoretically more precise.

The subtle part is that this kind of reconstruction is not what we’re doing.
The premise was that we are loading 8-bit RGB images, doing processing on them, and saving them again.
We have no control over how they were quantized when saved; all information lost is gone forever.
In other words, if an image’s color were multiplied by 255 and rounded, dividing them by 256 at load time does not bring back any precision.
Only when we control both saving and loading does an appeal to lower reconstruction error make sense.

In fact, using the alternative formula to load other people’s images will introducemore error.
Most likely the images were quantized via the standard formula, so decoding them with the wrong scale factor is incorrect, in theory.
In practice, the colors aren’t absolute measurements (even if the sRGB spec claims so), and all that happens is that we’ll do our processing in a slightly smaller range with a small offset.
End of the subtle part.

Finally, one should never mix the encode and decode steps of the two quantizers.
That’s just broken code.
It’s an easy mistake to make, though.

## Conclusion

To answer the question posed in the title: if you’re processing images given to you by strangers, you should normalize RGB values by 255.
Neither inexact floating-point values nor some abstract feeling of a higher reconstruction error is a good reason to go for the alternative.
But if you control both image saving and loading, don’t need zero to map to zero, and feel OK about tying your processing code to the 8-bit dynamic range, then you can consider division by 256 to eke out a bit more precision.
Just don’t blame me when your colleagues load your images with the standard formula anyway, ruining your master plan.

## Other takes

Jonathan Blow’s2002 articletalks about mid-riser and mid-tread quantizers without mentioning them by name.
I got the diagram idea from there.

The already mentioned2015 blog postby Andrew Kesler advocates for the alternate formula.
Unfortunately the comparison is to the standard formula but without rounding, which invalidates most of the analysis.

I’m writing a book on color reduction algorithms.Sign up hereif you’re interested.

MastodonBlueskyYouTubeFeed

30fps.net