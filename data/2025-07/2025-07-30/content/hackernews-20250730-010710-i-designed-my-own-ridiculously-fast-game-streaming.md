---
title: I designed my own ridiculously fast game streaming video codec – PyroWave – Maister's Graphics Adventures
url: https://themaister.net/blog/2025/06/16/i-designed-my-own-ridiculously-fast-game-streaming-video-codec-pyrowave/
site_name: hackernews
fetched_at: '2025-07-30T01:07:10.666397'
original_url: https://themaister.net/blog/2025/06/16/i-designed-my-own-ridiculously-fast-game-streaming-video-codec-pyrowave/
author: Bogdanp
date: '2025-07-30'
---

Streaming gameplay from one machine to another over a network is a reasonably popular use case these days. These use cases demand very, very low latency. Every millisecond counts here. We need to:

* Send controller input from machine A to B over network
* B renders a frame on the GPU
* B encodes the frame into a bitstream
* B sends the result over a network to A
* A decodes the bitstream
* A displays image on screen
* Dopamine is released in target brain

Every step in this chain adds latency and we want to minimize this as much as possible. The go-to solution here is GPU accelerated video compression using whatever codec you have available, usually H.264, HEVC or if you’re really fancy, AV1. Ideally, we want all of this to complete in roughly ~20 ms.

To make this use case work well, we have to strangle the codecs quite a bit. Modern video codecs love latency since it allows tricks like flexible rate control and B-frames. That is what allows these codecs to operate at ridiculous compression ratios, but we have to throw away most of these tricks now. Since the codec cannot add latency, and we’re working on a fixed bit-rate budget (the ethernet cable or WiFi antenna), we’re left with:

* Hard-capped constant bit rateThere is no buffer that can soak up variable bit rate
* There is no buffer that can soak up variable bit rate
* Infinite GOP P-frames or intra-refreshEither choice deals with packet loss differently
* Either choice deals with packet loss differently

When game streaming, the expectation is that we have a lot of bandwidth available. Streaming locally on a LAN in particular, bandwidth is basically free. Gigabit ethernet is ancient technology and hundreds of megabits over WiFi is no problem either. This shifts priorities a little bit for me at least.

Back in my student days, I designed a very simple low-complexity video codec for my master thesis, and after fiddling with Vulkan video and PyroFling for a while, that old itch was scratched again.I wanted to see what would happen if I designed a codec with laser focus on local streaming with the absolute lowest possible latency, what could go wrong?

### Throwing out motion prediction – intra-only

This is the grug-brained approach to video, but it’s not as silly as it sounds. Bit-rates explode of course, but we gain:

* Excellent error resilienceEven on local WiFi streaming to a handheld device, this does matter quite a lot, at least in my experience
* Even on local WiFi streaming to a handheld device, this does matter quite a lot, at least in my experience
* SimplicityDuh
* Duh
* Consistent qualityWith CBR, video quality is heavily dependent on how good of a job motion estimation can do
* With CBR, video quality is heavily dependent on how good of a job motion estimation can do

Intra-only has use cases in digital cinema (motion JPEG2000) and more professionally oriented applications where these concerns are likely more important than squeezing bandwidth. We’re now working at 100+ Mbits/s instead of ~10-20 Mbit/s, so streaming over the internet is no longer feasible outside of peer-to-peer with fiber links. For reference, raw 1080p60 with 420 chroma subsampling is in the range of 1.5 Gbit/s, and it only gets worse from there.

### Throwing out entropy coding

Entropy coding is an absolute nightmare for parallelization, which means encoding solely on the GPU with compute shaders becomes an extremely painful affair. Let’s just throw that out and see how far we get. Gotta go fast!

There are codecs in this domain too, but it’s getting very specialized at this point. In the professional broadcasting space, there are codecs designed to squeeze more video through existing infrastructure with “zero” lag and minimal hardware cost. My master thesis was about this, for example. A more consumer oriented example is VESA display stream compression (I’m not sure if it does entropy coding, but the compression ratios are small enough I doubt it). There isn’t much readily available software in this domain, it’s generally all implemented in tiny ASICs. If FFmpeg doesn’t support it, it doesn’t exist for mere mortals.

## Discrete Wavelet Transforms

While modern codecs are all block-based Discrete Cosine Transform (DCT) + a million hacks on top to make it good, there is an alternative that tried its best in the 90s to replace DCTs, but kinda failed in the end.https://www.youtube.com/watch?v=UGXeRx0Tic4is a nice video explaining some of the lore. DWT-based compression has a niche today, but only in intra video compression. It’s a shame, because it’s quite elegant.https://en.wikipedia.org/wiki/Discrete_wavelet_transform

A graphics programmer will be familiar with this structure immediately, because this is just good old mip-maps with spice. Effectively, we downsample images, and also compute the “error” between the high-res picture and low-res picture. With signal processing lenses on, we can say it’s a critically sampled filter-bank. After processing N pixels, we obtain N / 2 low-pass and N / 2 high-pass pixels. The filters designed to do this are very particular (I really don’t know or care how they were made), but it’s basically just a basic convolution kernel, nothing too wild. The number of levels can vary but I chose 5 levels of decomposition.

Once the image is filtered into different bands, the values are quantized. Quantizing wavelets is a little tricky since we need to consider that during reconstruction, the filters have different gains. For the CDF 9/7 filter, high-pass is attenuated by 6 dB, and there are other effects when upsampling the lower resolution bands (zero-insertion). Rather than sweating out new graphs, I’ll just copy paste from my thesis. CDF 9/7 has very similar looking spectrum to the 5/3 I used here.

After normalizing the noise power, higher frequency bands can be quantized much harder than low-frequency bands. This exploits human psychovisual effects. This effect is used during rate control, which is another interesting problem. In the end, the higher frequency bands quantize to zero for most of the frame, with bits being allocated to critical regions of the image.

### Classic artifacts of wavelets

The JPEG blocking artifact is infamous. Wavelet’s typical failure mode is that all high-pass information is quantized to 0, even where it shouldn’t be. This leads to a blurring – and if severe – ringing artifact. Given how blurry games these days can be with TAA, maybe this simply isn’t all that noticeable? 😀 Modern problems require modern solutions.

## Packing coefficients into blocks really fast

Fiddling with this part of the codec was the thing that took the longest, but I think I landed on something alright eventually.

The basic block is 32×32 coefficients. This forms a standalone unit of the bitstream that can be decoded independently. If there is packet loss, we can error correct by simply assuming all coefficients are zero. This leads to a tiny blur somewhere random in the frame which is likely not even going to be perceptible.

The 32×32 block is further broken down into 8×8 blocks, which are then broken down into 4×2 blocks. This design is optimized for GPUs hierarchy of threads:

* 1 thread: 4×2 coefficients
* Cluster of threads (subgroup): 8×8 block
* Workgroup: 32×32 block (128 threads)

8 coefficients per thread is deliberately chosen so that we can be byte oriented. Vulkan widely supports 8-bit storage of SSBOs, so I rely on that. We absolutely cannot be in a situation where we do bit fiddling on memory. That makes GPUs sad.

Like most wavelet codecs, I went with bit-plane encoding, but rather than employing a highly complicated (and terribly slow) entropy coding scheme, the bit-planes are just emitted raw as-is. I did this in my master thesis project and I found it surprisingly effective. The number of bits per coefficient are signaled at a 4×2 block level. I did some experiments on these block sizes and 4×2 was the right tradeoff. Using subgroup operations and some light prefix sums across the workgroup, it’s very efficient to decode and encode data this way. For non-zero coefficients, sign bits are tightly packed to the end of the 32×32 block. This was mildly tricky to implement, but not too bad.

The details are in mydraft of the bitstream.

## Accurate and fast rate control

In this style of compression, rate control is extremely important. We have a fixed (but huge) budget we have to meet. Most video codecs struggle with this requirement since the number of bits we get out of entropy coding is not easily knowable before we have actually done the compression. There is usually a lot of slack available to codecs when operating under normal VBR constraints. If a frame overshoots by 30%, we can amortize that over a few frames no problem, but that slack does not exist here since we’re assuming zero buffering latency.

Without entropy coding, we can trivialize the problem. For every 32×32 block, I test what happens if I throw away 1, 2, 3, … bits. I measure psychovisually weighted error (MSE) and bit-cost from that and store it in a buffer for later.

During RD analysis I can loosely sort the decisions to throw away bits by order of least distortion per bit saved. After the required number of bits have been saved through some prefix summing, we have achieved a roughly optimal rate distortion across the entire image in fixed time.

In the final pass, every 32×32 block checks how many bits to throw away and packs out the final bit-stream to a buffer. The result is guaranteed to be within the rate limit we set, usually ~10-20 bytes under the target.

Being able to rate limit like this is a common strength of wavelet codecs. Most of them end up iterating from most significant to least significant bit-plane and can stop encoding when rate limit is met, which is pretty cool, but also horribly slow …

## Gotta go ridiculously fast 😀

So … is it fast? I think so. Here’s a 1080p 4:2:0 encode and decode of Expedition 33, which I found to be on the “brutal” end for image compression. Lots of green foliage and a lot of TAA noise is quite hard to encode.

0.13 ms on a RX 9070 XT on RADV. Decoding is also very fast. Under 100 microseconds. I don’t think anything else even comes close. The DWT pass was quite heavily optimized. It’s one of the few times where I found that packed FP16 math actually helped a lot, even on a beast like RDNA4. The quantizer pass does the most work of all the passes, and it took some effort to optimize too. Doing DWT in FP16 does have a knock-on effect on the maximum quality metrics we can achieve though.

Encoding more “normal” games, the quant + analysis pass has an easier time. 80 microsecond encode is pretty good.

Here’s a 4K 4:2:0 encode of the infamous ParkJoy scene.

0.25 ms, showing that 1080p struggles a bit to keep the GPU fully occupied. An interesting data point is that transferring a 4K RGBA8 image over the PCI-e bus is far slower than compressing it on the GPU like this, followed by copying over the compressed payload. Maybe there is a really cursed use case here …

I think this is an order of magnitude faster than even dedicated hardware codecs on GPUs. This performance improvement translates directly to lower latency (less time to encode and less time to decode), so maybe I’m onto something here.

Power consumption on the Steam Deck when decoding is also barely measurable. Not sure it’s less than the hardware video decoder, but I actually wouldn’t be surprised if it were.

## Quality comparisons

Given how niche and esoteric this codec is, it’s hard to find any actual competing codecs to compare against. Given the domain is game streaming the only real alternative is to test against the GPU vendors’ encoders with H.264/HEVC/AV1 codecs in FFmpeg. NVENC is the obvious one to test here. VAAPI is also an option but at least FFmpeg’s implementation of VAAPI fails to meet CBR targets which is cheating and broken for this particular use case. It’s possible I held it wrong, but I’m not going to try debugging that.

Over 200mbit/s at 60 fps, I find it hard to tell any compression artifacts without side-by-side comparisons + zooming in, which is about 1.5 bpp. For something as simple as this codec, that’s quite neat. For objective metrics, I made use ofhttps://github.com/psy-ex/metrics.

To even begin to compare a trivial codec like this against these codecs is a little silly, but we can level the playing field a bit by putting these codecs under the same harsh restriction that we have in PyroWave:

* Intra-only
* CBR with hard capEncoder is not allowed any slack, which should make the rate control really sweat
* Encoder is not allowed any slack, which should make the rate control really sweat
* Fastest modes (not sure it matters that much to intra-only)

Example command line here:

ffmpeg -y -i input.y4m -b:v 100000k -c:v hevc_nvenc -preset p1 -tune ull -g 1 -rc cbr -bufsize 1667k out.mkv

No one in their right mind would stream like this, but let’s try anyway. 🙂

The video clips from the games are 5s clips I captured myself to raw NV12 video. I don’t think it’s super useful to upload those. My hacked up scripts to generate the graphs can be foundherefor reference.

I ran the NVENC tests on an RTX 4070 on 575 drivers.

### ParkJoy

I included this as a baseline since this sequence has been seared into the mind of every video engineer out there (I think?) … This clip is 50 fps, but since my test script is hard-coded for 1080p60, I hex-edited the .y4m :’)

O_O. One thing to note here is that AV1/HEVC rate control kinda fails in this scenario. It ends up using less than the allotted budget, probably because it has to be conservative to meet the ridiculous hard-capped CBR. The graphs are done using the final encoded size however.

… VMAF, are you drunk?

Back to reality.

The more typical metrics look more like what I would expect. XPSNR is supposed to be a weighted PSNR that takes psychovisual effects into account, but I have no idea if it’s a good objective metric.

### Expedition 33

Quite hard to encode. It was this game that actually gave me the last push to make this codec since even at 50 mbit/s with motion estimation, I recall some sections giving the encoder real trouble. Bumping bit rates just never cleaned things up properly for whatever reason …

I don’t know why, but VMAF really likes PyroWave.

### Stellar Blade

Surprisingly easy to code. Must be the blurred backgrounds in play.

The use of FP16 kinda limits how high the PSNR can go. This is way beyond transparency, so, whatever.

### Street Fighter 6

This scene is arguably a good argument for 4:4:4 …

### FF VII Rebirth

More foliage, which I expected to be kinda hard. The game’s presentation is very soft and it shows in the compression rates 🙂

VMAF really seems like a joke metric for these use cases …

Another example of PSNR flattening off due to lowered internal precision.

## Conclusion

I’m quite happy with this as-is, and having a 100% DIY streaming solution for my own use is fun.
