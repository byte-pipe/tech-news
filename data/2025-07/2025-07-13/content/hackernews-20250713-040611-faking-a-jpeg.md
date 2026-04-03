---
title: Faking a JPEG
url: https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/
site_name: hackernews
fetched_at: '2025-07-13T04:06:11.512926'
original_url: https://www.ty-penguin.org.uk/~auj/blog/2025/03/25/fake-jpeg/
author: todsacerdoti
date: '2025-07-13'
---

# 25th March 2025: Faking a JPEG

×⇩Click to expand

I've beenwitteringonaboutSpigot for a while.
It's smallweb applicationwhich generates a
fake hierarchy of web pages, on the fly, using a Markov
Chain to make gibberish content for aggressive web crawlers
to ingest.

Spigot has been sitting there, doing its thing, for a few
months now, serving over a million pages per day. I've
not really been keeping track of what it's up to, but every now
and then I look at its logs to see what crawlers are hitting it.

Sadly, two of the hardest-hitting crawlers go to extreme lengths
to hide their identity, generating random, and unlikely, browser
signatures (e.g. Firefox version 134.0, 64 bit, on Windows 98!) and
accessing from random addresses. It seems quite likely that this
is being done via a botnet - illegally abusing thousands of people's
devices. Sigh.

Where I can identify a heavy hitter, I add it to the list on
Spigot's front page so I can track crawler behaviour over time.

Anyway... a couple of weeks ago, I noticed a new heavy hitter,
"ImageSiftBot". None of Spigot's output contained images, but
ImageSiftBot was busily hitting it with thousands of requests
per hour, desperately looking for images to ingest. I felt sorry
for its thankless quest and started thinking about how I could
please it.

My primary aim, for Spigot, is that it should sit there, doing its
thing, without eating excessive CPU on my server. Generating images
on the fly isn't trivial, in terms of CPU load. If I want to create
a bunch of pixels, in a form that a crawler would believe, I pretty
much have to supply compressed data. And compressing on the fly is
CPU intensive. That's not going to be great for Spigot, and is a
complete waste when we're just generating throw-away garbage in any
case.

I got to thinking: compression tends to increase the entropy of
a bit stream. If a file doesn't look to have random content then
it's compressible, and an optimally compressed set of data would
be more or less indistinguishable from random data. JPEGs are
pretty well compressed. So the compressed data in a JPEG will
look random, right?

If I had a template for a JPEG file, which contained the "structured"
parts (info on size, colour depth, etc) and tags indicating where
highly compressed data goes, I could construct something that looks
like a JPEG by just filling out the "compressed" areas with random
data. That's a very low-CPU operation. The recipient would see
something that looks like a JPEG and would treat the random data
as something to decompress.

I read up a bit on the structure of JPEG files and discovered they
can be quite complex. But that doesn't matter much. A JPEG file is
made up of chunks. Each chunk has a marker and a length (sometimes
implicitly zero, sometimes only determined by reading the chunk's
content, looking for the next marker). So, parsing a JPEG is
relatively simple. And I've got loads of JPEGs. So: what if I
scan a bunch of existing files, discarding the "comment" chunks,
noting just the length of the "pixel data" chunks and keeping the
rest? How big would the result be?

I've currently got 514 JPEGs on my web site, totalling about 150MBytes
of data. If I scan all of them, keeping just the "structured" chunks
and noting the "pixel" chunk lengths, the resulting data set is under
500KBytes - a drop in the ocean. That gives me 514 realistic templates, of
various sizes, colour depths, etc.

Generating a JPEG would come down to:

template

=

random
.
choice
(
template_list
)

for

chunk

in

template
.
chunks
:


if

chunk
.
type

is

pixel_data
:


output
(
random
.
randbytes
(
chunk
.
length
))


else
:


output
(
chunk
.
data
)

And that it!

So I knocked together some test code. And discovered it's not quite
as simple as that. Real pixel data isn't quite random - it's Huffman
coded, and there's a bit of structure there. If I fill out the pixel
chunks with purely random data, the decoder notices places where the
data is incorrect. I'm sure someone with more brains/time/inclination
than me would be able to parse the other chunks in the template to
determine exactly what Huffman codes can be inserted into the pixel
chunks, still without needing to actuallydocompression.

But that's where I bowed out. Because... every JPEG viewer I've tried
accepts my garbage data and displays an image. Even though the decoder
notes issues, it still emits pixel data. And that might just be good
enough to inconvenience web crawlers. I bet most of them don't care
about errors, so long as they don't result in a broken image. Even if
theydocare about errors, they still have to grab the data and try
to decode it before they can tell it's broken. And that's increasing
their costs, which is fine by me.

The image at the top of this page is an example, generated on the fly by
from the code. Your browser will probably display it, despite it being a
faulty JPEG.

Back to efficiency: How quickly can I generated these garbage images? As I
said, I'm using templates based on images from my site. I usually optimise
images for the web, resulting in JPEGs having a range of sizes, but mostly
around 1280x960 pixels and 200-300KBytes. A quick test shows I can generate
around 900 such images per second on my web server using this method (in
Python). That's around 190MBytes/second and very substantially faster than
my web server's connection to the Internet. Nice!

I've wired the above into Spigot and around 60% of Spigot-generated
pages will now have a garbage JPEG in them. As with Spigot, I seed the
random number generator for an image with a value derived from the URL.
So, while the above image was generated on the fly, if you reload it,
you'll get the same image.

ImageSiftBot isveryhappy with this and grabbed around 15,000 garbage
images today. I expect it'll ramp its rate up over the next few days as it
finds more links. Meta's bot, AmazonBot, and GPTBot are also getting
excited!

I need to tidy up the Python class that does this, but will release it
in due course. It's under 100 lines of code (but could do with more
comments!).

[2025-03-26]Now released onGitHub

[2025-03-28]After thinking a lot about Huffman codes, I've added a bit
mask against the generated pixel data. "AND"-ing every generated byte with
0x6D ensures that no strings of three or more 1's appear in the bit stream.
This massively reduces the probability (from > 90% to < 4%) of generating a
JPEG that has invalid Huffman codes, without requiring a lot more CPU.

The focus is to make generating the garbage as cheap as possible for me
and as expensive as possible for the abusive web crawler. After examining
how JPEG uses Huffman codes, itwouldn'tbe excessively difficult to
generate perfectly valid Huffman streams. But it would eat a lot more CPU
for very little gain.

## Leave a comment

Name:

Email:

Web site:

Anti-Spam:
