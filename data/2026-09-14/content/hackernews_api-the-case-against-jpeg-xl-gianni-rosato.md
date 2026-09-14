---
title: The case against JPEG XL | Gianni Rosato
url: https://giannirosato.com/blog/post/case-against-jxl/
site_name: hackernews_api
content_file: hackernews_api-the-case-against-jpeg-xl-gianni-rosato
fetched_at: '2026-09-14T16:47:23.355863'
original_url: https://giannirosato.com/blog/post/case-against-jxl/
author: contact9879
date: '2026-09-14'
description: Investigating JPEG XL's place as a Web image codec.
tags:
- hackernews
- trending
---

Investigating JPEG XL's place as a Web image codec.

## Why?

JPEG XL is a technically impressive image codec; it is a definitive upgrade over
JPEG, more versatile than WebP, and well-equipped to serve use cases beyond the
Web. However, it was famouslyrejected from Chromein 2023. Because this happened to a royalty-free, flexible,
compression-efficient codec from the JPEG Committee that wasreceiving attentionfrom large companies, the decision didn't land well with many.

Recently, aJPEG XL decoder in Rusthas made
its way into Firefox and Chrome in some capacity. The Web's major stakeholders
may therefore be reversing course on JPEG XL given that the new decoder may
protect the Web from reliving2023's WebP vulnerability. Is
this all it took to justify JPEG XL for the Web?

Historically, I've been a big proponent of JPEG XL for all use cases. Iendorsed JPEG XLfor Interop 2024, and I've interacted with Jon Sneyers and Jyrki Alakuijala (two
of the format's primary authors) personally many times. I'm consistently
impressed with their public conduct, level-headedness, technical aptitude, and
passion for the field.

This piece does not seek to discredit the format's authors or their work, nor to
claim any political affiliation relative to the codec's symbolism in free
software. The spirit of this post is educational; I want to offer an empirical
look at the current state of image compression and the Web platform in 2026.
Some inspiration is drawn fromRISC-V: They Should Have Known Betterby Dmitry Grinberg.

## The Web

Ido image compression work, coming from video compression
originally. While working onan AV1 encoder, Julio
Barba and I madesignificant advancements to AVIF, and Ilearned a lotin the
process. When I decided to start buildingmy own encoder, I had to think very hard about which
formats I felt had the highest ceilings, could be effectively optimized, and had
the most present and potential utility. I decided not to work with JPEG XL.

By volume, there are very few use cases on the Web that aren't served by
versatile lossy compression. The average Web consumer doesn't need lossless;
they just need a lossy codec versatile enough to prevent terrible artifacts
(e.g. JPEG on non-photographic content). This rules out JPEG XL's lossless
advantage, which in practice is only roughly11.9% smaller than lossless WebPanyway –
and on an unrealistic test dataset for the Web (157 MP photos, 10 MP
illustrations, and 27 MP books). It cannot be worth bringing a new image codec
to browsers to save 12% on a tiny volume of image content with use cases
inherently less sensitive to bandwidth constraints. I say this because JPEG XL
isn't competitive for lossy, so lossless would be its only real advantage.

## Lossy Compression Efficiency

One of the original arguments for JPEG XL was that its reference encoder was
moreperceptually optimizedthan competing encoders. Now, on both speed and fidelity per bit, other encoders
are stronger.

TheAV1 reference encoderreceived
specialized perceptual tuning based on controlled subjective human trials to
strengthen its efficiency while maintaining a tuning mode optimized for
perceptual metrics.SVT-AV1has
similar tuning modes. There is no compelling argument that modern encoders
aren't tuned for the human eye.

Metrics aren't perfect, but they paint a daunting picture for JPEG XL:

CVVDP
MS-SSIM
SSIMULACRA2

aperture-alphais Halide Compression's upcoming encoder, codenamed Aperture. I
included it to show just how much ground libjxl needs to make up to compete at
the frontier.

Some analysis claims thatJPEG XL underperforms in metricsrelative to its perceptual strength, but I don't see sufficient evidence that
this is to the degree that graphs like the ones I shared could be secretly
completely reversed. CVVDP and SSIMULACRA2 are very strong perceptual metrics,
and definitely tell ussomethingwhen the differences are this great. For
AVIF, libaom's perceptually optimized tune (tune IQ) is only a couple of points
lower than its perceptual-metric-optimized tune (tune SSIMULACRA2). Plus, the
JPEG XL reference encoder has historically suffered fromperceptualissuesthat remain largely
unresolved.

There's no such thing as a codec benchmark, only an encoder benchmark; in
theory, the ceiling for JPEG XL as a format is higher than libjxl is getting.
But how hard would it be to close the gap? As a compression engineer, I believe
it is disadvantaged here. Some reasons:

* JPEG XL doesn't have directional prediction modes. Compressed images are
divided into VarDCT blocks (from 2x2 up to 256x256) and transformed into
frequency representations of their pixels. Other block-based image codecs like
WebP let you predict a block's pixels using surrounding data, subtract this
prediction from the actual pixels, and then do the frequency transform.
Directional prediction modes can result in blur if your encoder isn't
perceptually optimized, but strong mode-decision pipelines can pick the right
mode for the job and save lots of bits. For example, edge preservation is
stronger in codecs with directional pred, while JXL is weaker here.
* The proposed solution for the edge-preservation gap is splines, which are
vastly more difficult to use. The hard part is on the encoder side: you need
an efficient algorithm to figure out which pixels can even be represented as a
spline, then feed every candidate through RDO to decide whether it's worth
coding. There's no existing PoC for using splines for edge preservation, and I
have no reason to believe they'd be better than dir-pred anyway.
* JPEG XL doesn't have deblocking loop filtering (DLF), or any deblocking
filter. It does have two in-loop tools that are sometimes offered as partial
equivalents: gaborish, which is the closest thing JXL has to AV1's loop
restoration filtering, and EPF (edge-preserving filter), whose closest
analogue is AV1's CDEF. Neither is a deblocking filter, and the two together
can't fully replace proper DLF. The DLF can smooth images out, but if your
encoder is smart it will only help you avoid mosquito noise, which JPEG XL
still suffers from.
* JPEG XL's perceptual "XYB" colorspace is based on a lot of intuition, and
doesn't always translate to gains in other formats (like JPEG) even when
metrics like SSIMULACRA2 work in the exact same colorspace. The claimed
efficiency savings from using XYB also aren't as big as originally advertised
because libjxl currently relies on aggressively quantizing the B channel. This
has resulted in subpar color preservation, which new JXL encoder developers
must explicitly undo.
* JXL does poorly with non-photographic images. The proposed solution is using
patches, but they are more difficult to use than AV1's Intra Block Copy.To get a similar range of expressiveness to IntraBC, the encoder has to deal
with additional concepts like layers and blending, which aren't cheap to
represent at the bitstream level.Residual coding is awkward. With AV1, you predict a block, subtract the
prediction from the source, and the transform coefficients naturally
represent the residual. With JXL's construction, you decode a residual frame
and then blend a reference patch, so you need an actual frame or layer whose
decoded pixels represent the residual. That would likely be a Modular frame,
which is interesting because Modular isn't restricted to conventional
unsigned image values the way the final rendered image is.An IntraBC block essentially costs a motion vector plus residual
coefficients, whereas a JXL construction potentially costs a reference
frame, a frame header, a crop, blend information, a patch dictionary entry,
patch coordinates, and a residual frame. That overhead can overwhelm the
savings unless the repeated region is fairly large or reused many times.Patches have to be explicitly enabled in libjxl below effort 7 because they
currently have performance issues.
* To get a similar range of expressiveness to IntraBC, the encoder has to deal
with additional concepts like layers and blending, which aren't cheap to
represent at the bitstream level.
* Residual coding is awkward. With AV1, you predict a block, subtract the
prediction from the source, and the transform coefficients naturally
represent the residual. With JXL's construction, you decode a residual frame
and then blend a reference patch, so you need an actual frame or layer whose
decoded pixels represent the residual. That would likely be a Modular frame,
which is interesting because Modular isn't restricted to conventional
unsigned image values the way the final rendered image is.
* An IntraBC block essentially costs a motion vector plus residual
coefficients, whereas a JXL construction potentially costs a reference
frame, a frame header, a crop, blend information, a patch dictionary entry,
patch coordinates, and a residual frame. That overhead can overwhelm the
savings unless the repeated region is fairly large or reused many times.
* Patches have to be explicitly enabled in libjxl below effort 7 because they
currently have performance issues.

For non-photographic images, the argument that “they should be vector images”
doesn't hold up because many images could be vector images but aren't, and they
can't be vectorized perfectly. “The world should be different” is not a
justifiable defense against optimizing for the way the worldactuallyis.

It is tempting to think these points mean the ceiling is higher than libjxl lets
us reach and that we could do better, but I'm not confident it can eclipse
well-optimized AVIF encoders quickly, given its less intuitive (and potentially
weaker) coding tools.

## Decode Time

JPEG XL has an impressively flexible specification. In addition to its coding
tools, it supports up to 4096 channels, arbitrary color depth, progressive
decode, JPEG recompression, and more. Many of these features are not broadly
useful on the Web; you need 4 channels (RGB/YUV + alpha),reasonablecolor
depth to support HDR (10-bit is fine), and the ability to load quickly.

Progressive rendering (which AVIF supports) decodes a low-fidelity rendition
before the full image arrives. AVIF didn't support progressive rendering for a
while, and during that time I believe it was deeply oversold. Now that libavif
has implemented it (it was always possible), the conversation appears to be
over. I think this is because the results speak for themselves:

This isfrom theJPEG-XL info site,
where AVIF shows a usable image much earlier than JXL at just ~2-3% of the full
image's size. Combined with the fact that the AVIF is smaller overall, this is
an easy win. I've screenshotted the page because the AVIF progressive decode
only works in Chrome, as it is using the browser's native decoder; JPEG XL uses
a polyfill because even in Safari where it is supported, progressive decode
isn't.

JPEG recompression is the ability to losslessly re-encode JPEGs as JXL images
while saving bits; the oft-cited number is 20% savings. However, the user pays
for this in decode time, as recompressed JPEGs take ~33% longer to decode.
Modern consumer devices are powerful, but the argument that the savings come
“for free” is misleading.

On that topic, decode time is not competitive with the best:

In public discourse, AVIF is considered slow to decode; what does that make JXL?
This is also a 10-bit AVIF, and all images were size-matched encodes of the same
source. The JPEG was 2,478,828 bytes, the JPEG XL was 2,599,428, the AVIF
2,649,949, and WebP 2,693,794. WebP is over 90kb larger and still manages to
decode over 10x faster than jxl-rs withwpd.

Due to the codec's expressivity, it is possible to craft images that takeobscenelylong to decode. Takethis example(open with caution) that
computes primes up to 33,599 and takes 17.43s of user time to decode on my M5
Pro with the Rust decoder. Additionally, keep in mind that this is the decoder
making its way into Chrome, Firefox, etc – the prime wall image is just 1,918
bytes, so it's about to become trivially easy to JXL-bomb low-end devices. You
can already ship a couple dozen of these on a Web page and slow Apple devices
down, as they natively support JPEG XL in Safari.

## Conclusion and Opinion

I believe Web codecs should be purpose-built, efficient, and narrowly scoped to
the needs of the Web. I think WebP was a bit too narrowly scoped, but the idea
was there; AVIF's container could be better, and the AV1 spec could be a bit
more specific about handling certain properties of images (e.g. normative 4:2:0
upsampling), but AVIF was always a guaranteed addition to the Web due to AV1 and
benefits from a very mature ecosystem.

Do we need JPEG XL then? It isn't narrowly scoped whatsoever; it is meant to be
everything to everyone, by design. I think a lot of other use cases need this,
but the Web needs to save bandwidth, decode fast, and prevent foot-guns; I don't
see how JPEG XL is even as good a fit as WebP. Not to mention an additional
compatibility headache now exists for anyone just trying to download an image
from the Internet and use it somewhere – it was hard enough to get widespread
WebP adoption, and I don't think it's worth doubling the pain by having to climb
the same hill for AVIFandJPEG XL. Especially when JPEG XL doesn't appear to
add anything to the Web platform.

3½ years ago, I said:

I want a web where both AVIF and JPEG XL can exist, and developers decide
which format to use for its merits. [...] In my opinion, JPEG XL and AVIF have
fundamentally different strengths which lend them to different use cases.

At the time, JPEG XL was a much stronger contender for medium-high fidelity
lossy image compression. AVIF now dominates the entire fidelity range, so JPEG
XL's one real advantage has disappeared.

JPEG XL came from Cloudinary and Google, but I think the codec is discussed in a
way that doesn't make this clear. Also worth mentioning both JPEG XL and AVIF
are royalty-free. Because of the politics around Google's browser market
dominance, AV1 coming from Google, and the controversy around Google's WebP, it
is my opinion that most of the argument for JPEG XL comes from wanting a Web
with more developer choice as opposed to wanting a technologically superior
image codec. I understand this, and I think JPEG XL can still thrive outside the
Web in places AVIF never could. In the same article:

My current optimistic hope is that JXL takes off outside the web among
professionals working with tools like the Adobe suite or alternatives, and
camera manufacturers, smartphone OEMs, and others take notice and begin to
think about JXL more seriously.

JPEG XL isn't useless; it is genuinely compelling technology for use cases
beyond the Web. I'm just not personally convinced we need it in browsers any
time soon.

Software and environment details.