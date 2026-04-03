---
title: Blue light filters don’t work - by Patrick Mineault
url: https://www.neuroai.science/p/blue-light-filters-dont-work
site_name: hnrss
content_file: hnrss-blue-light-filters-dont-work-by-patrick-mineault
fetched_at: '2026-02-21T11:08:56.496932'
original_url: https://www.neuroai.science/p/blue-light-filters-dont-work
author: Patrick Mineault
date: '2026-02-20'
description: Why controlling total luminance is a better bet
tags:
- hackernews
- hnrss
---

# Blue light filters don’t work

### Why controlling total luminance is a better bet

Patrick Mineault
Feb 20, 2026
9
2
Share

Everybody wants better sleep, but getting better sleep is hard.

I was trading New Year’s resolutions with a circle of friends a few weeks ago, and someone mentioned a big one: sleeping better. I’m a visual neuroscientist by training, so whenever the topic pops up it inevitably leads to talking about the dreaded blue light from monitors, blue light filters, and whether they do anything. My short answer isno, blue light filters don’t work, but there are many more useful things that someone can do to control their light intake to improve their sleep—and minimize jet lag when they’re travelling.

My longer answer is usually a half-hour rant about why they don’t work, covering everything from a tiny nucleus of cells above the optic chiasm, to people living in caves without direct access to sunlight, to neuropeptides, the different cones, how monitors work, gamma curves, what I learned running ismy.blue, corn bulbs, melatonin, finally sharing my Apple Watch & WHOOP stats. What follows is slightly more than you needed to know about blue light filters and more effective ways to control your circadian rhythm. Spoiler: the real lever is total luminance, not color.

## The premise

Right above the optic chiasm lies a nucleus called the suprachiasmatic nucleus (SCN). This is where the brain’s master circadian clock lives. There are a lot of phenomena in the body, whether alertness, body temperature, or hunger, that are at least partially dependent on our body’s sense of time. There’s a set of neurons that are part of the hypothalamus that autonomously track time, by a fascinating set of transcription-translation feedback loops involving proteins that ultimately shut down their own translation in a cycle that lasts about 24 hours. The cells in the SCN also synchronize with each other through neuropeptides, and diffuse the master clock signal throughout the body; melatonin from the pineal gland, but also via secondary regulation of the HPA (stress axis), and a neuropeptide called AVP.

The intrinsic clock is not very precise, with a cycle that typically lasts a little more than 24 hours, something which was first verified in people living deep underground in abandoned mines (for science!). One factor that ultimately resets the clock is input from a set of neurons inside the retina that project to this nucleus. Those cells are called intrinsically photosensitive retinal ganglion cells (ipRGCs). Breaking this down:

* Aretinal ganglion cellis a cell in the retina (the back of the eye) that ultimately projects to the brain
* Intrinsically photosensitivemeans these cells don’t rely on signals from cones or rods to get light information; the cells directly express a light-sensing molecule, an opsin, called melanopsin.
The ipRGC-SCN-pineal circuit, from
Introduction to Behavioral Neuroscience

ipRGCs are not image-forming, and they don’t project to visual cortex; they’re just there to track ambient light, relaying information to the SCN. Crucially, melanopsin isoften said to be sensitive to blue. Therein lies the premise of blue light filters: if you cut the blue out of your display at night, you will help your body’s clock synchronize, and fall asleep more easily; or at the very least, it will stop your brain’s internal clock from getting delayed.

## A flawed premise

Is that premise correct? No. The premise is revealed as obviously flawed the minute you look at the absorption spectra of the different opsins. Compare melanopsin’s sensitivity to different wavelengths with those of the three cones: its peak sensitivity is right between that of the S (short wavelength, aka blue) cone and that of the M cone (medium wavelength, aka green). It also has a pretty broad bandwidth.It’s not sensitive to blue, it’s sensitive to cyan (and blue and green).

Unless your strategy is to create a photo-lab-like screen in pure black and red, or wear deep-red-tinted glasses, it’s unlikely that a pure colorshift strategy will cut out that big of a chunk of the spectrum.

## What night shift does

What does blue light blocking software like f.lux and Apple’s Night Shift do? We can measure their effect by presenting different colors on a monitor with or without the filter on and measuring the output light with a spectrometer. Ideally, I would have access to a precision spectrometer as I used in grad school, but that seemed excessive and very expensive; I used a cheap colorimeter instead, the SpyderX, to find out. This device can measure the (simulated) response of the L, M, and S cones to a patch of constant luminance on the screen (LMS responses).The PsyCalibrator paper’s appendixassures me that the device is remarkably linear within the range that I used it in, saving me from browsing eBay for several weeks for a calibrated precision spectrometer that would cost less than a 2014 Nissan Altima in good condition.

The SpyderX, an affordable colorimeter used to measure colors on a screen

I tested this with Apple’s Night Shift on my M1 Macbook Air. I was surprised to find that the mapping function is very simple: LMS responses can be mapped linearly via matrix multiplication between standard and night-shifted colors (R^2 = .997). This is surprising because Night Shift could do all sorts of complicated things, like a nonlinear look-up table (LUT). As luck would have it, the transformation is linear, and more than that, almost diagonal, facilitating analysis.

Here’s the matrix:

 L M S
L [ +0.979 -0.116 +0.013 ]
M [ +0.162 +0.636 -0.022 ]
S [ +0.140 -0.102 +0.384 ]

Reading off the diagonal, to a good approximation, it tells us that:

* Night Shift maintains L (red) luminance
* Night Shift decreases M (green) luminance by about 40%
* Night Shift decreases S (blue) luminance by about 60%

You can’t directly tell from these numbers how ipRGCs will react to Night Shift, because ofcolor metamerism: you also need to know theemissionspectrum. You can, however, guess that if the emission spectrum is not pathological, the ipRGC change in response will probably lie somewhere in between the M cone and the S cone, that is, about 50%.

Indeed, I used a reference spectrum for this class of monitor, guessing the emissions of the individual primaries by splitting the spectrum by eye, and calculated that ipRGC cells would see 52% less light during night shift mode, which is within the same ballpark as that implied byNagaro et al (2019). Broadly, software blue light filters cuts abouthalfof light relevant to ipRGCs.

## Is half a lot?

No. Human light perception works on a log scale, allowing us to maintain useful vision over6 orders of magnitude of luminance, from the sun at noon to moonless nights, whereas halving is .3 orders of magnitude1. In relative terms, halving light is a tiny blip of the dynamic range of vision.Phillips et al. (2019)measured the concentration of melatonin in the saliva of subjects in response to different light-exposure levels. That gives a dose-response curve: luminance on the x axis, and melatonin suppression (disruption of the circadian rhythm) on the y axis.

They found that the curve is quite shallow. Halving the luminance, at best (around 20 lux baseline) might get you from 50% to 25% melatonin suppression.

Average and individual dose response curves from Phillips et al. (2019)

That’s not nothing, but the odds that you’ll realize these gains are pretty slim. One, you have to be lucky enough to be within the right range—if your room is too bright or too dim, it will have no effect. Second, the advantage will be offset immediately if you increase your screen brightness to compensate for the color shift. Doubling the screen brightness is, unfortunately, only a few keystrokes away, as we’ll see very soon. It’s possible that Night Shift does something, butthe biggest study I could find of Night Shift mode (still a pretty small study) found little effect on sleep, so if there’s an effect, it must be tiny.

Wouldn’t zeroing out all blue emission (i.e. mapping (r, g, b) → (r, g, 0)) remove even more of the cyan culprit? Yes, but it would make it very hard to use the computer. Software blue light filters are a compromise between maintaining usability and cutting outsomecyan light.

## Are people actually using Night Shift?

Aggravatingly, yes. I have seen survey numbers thrown around from 10% to 80% of users using blue light filters at night. I don’t know where these numbers are coming from, frankly. However, as it turns out, my viral websiteismy.bluecan get us some real numbers. Recall thatismy.blue is a website I made to settle an argument with my wife, an ophthalmologist, about the true color of a blue-green blanket (I lost this argument; it was blue). People chose whether a particular shade of cyan should be called blue or green, and could compare their color boundary with that of the broader population.

Blue light filters interfere with ismy.blue, moving the boundary to the right

Blue light filters mess with a computer’s colors, and so shouldradicallyshift a person’s apparent blue-green boundary. Now, most people running a blue light filter at night are unaware, and there’s no way from the website’s end to know a person’s monitor settings, so some people took the test at night with blue-light filters on. The linear transformation matrix model for Night Shift predicts that people’s blue-green boundary should shift in hue by about 15 degrees, which is huge—an effect size of multiple standard deviations compared to the daytime distribution of blue-green boundaries.

You can see this in aggregate in the mean thresholds as a function of solar time. Solar time is a standardized time basis where midnight corresponds to solar midnight, noon to solar noon, 6AM to sunrise, 6PM to sunset. Thresholds are stable during the day, but jump around at night, in the direction that you would expect (they rise, especially on platforms with built-in filtering like Mac & iPhone).

So I did something a little cheeky: I fit a mixture model for the threshold with two bumps: one for regular users, and one for blue-filter users 15 degrees to the right. Importantly, I fit different mixture weights depending on solar time. Perhaps I could have used a mixture of t-distributions instead, there are mix shifts I haven’t fully thought about, etc. Still, it’s an interesting data point.

As you can see, the proportion of blue-light filter users in my sample is quite large; at its peak during the night, 25% of iPhone users and 33% of Mac users were on Night Shift. I’ll note that the proportion of estimated blue filter never goes to exactly 0 during the day, so some putative blue light filter users might have true idiosyncratic thresholds on monitors with normal colors, or wildly miscalibrated or broken screens. On the other hand, the proportion at night is likely an undercount, since some would have (wisely, as instructed) turned off their blue light filters prior to taking the test. My guess is it probably comes out as a wash.

Overall, it means that blue light filters are quite commonly used, especially on platforms that them built in (e.g. Mac).

## What works instead?

Who can blame the people for thinking these blue light filters do something?! Everyone fromIvy League institutionstohealth influencersare telling us that blue light is bad. So what works instead?

To be clear, lightdoesaffect sleep onset and quality through the ipRGC-SCN-pineal-gland-melatonin connection. Controlling light is effective for certain kinds of sleep disturbances. For instance, an issue I’ve had over the years is a phase-delay pattern; I would get to bed later and later every night, which pushed my rise time forward, until it interfered with daytime activities (i.e. a job). Tightly controlling light to better control sleep can work here. However, the amount of cyan light change is far larger than that afforded by a blue light filter. Here are four things that can help.

Disclaimer: I’m not an MD, nor a sleep specialist, this is not medical advice. Talk to your MD.

### Use dark mode

Dark mode is distinct from night shift (blue filter) mode; it instructs websites and apps to display light text on a dark background as opposed to the daytime dark text on a light background. I took a sample of 4 websites/apps (Google, X, Github, and VSCode) with the SpyderX colorimeter + a diffuser to average over a larger area of the screen, and found reductions in luminance ranging from92% to 98%! That’s huge.

If it feels like it’s almost too much (e.g. the backgrounds are typically shifted to dark gray rather than pure black), remember that light perception is logarithmic, and that raw RGB values are translated to screen luminance via a gamma function whose exponent on Mac is 2.2. That means that dark grays can have far less light in absolute terms than the number implied by a linear scale. For instance, the dark gray #101010 has a relative luminance of (1/16)^2.2 compared to white #ffffff; about ~450 times darker.

That’s all great, but there are websites that still don’t have dark modes. It doesn’t make any sense in 2026 that Gmail doesn’t have a dark mode. If the activity you’re doing most at night is reading email, you might consider an alternative email client.

### Decrease your screen brightness at night

The screen brightness control on Mac has 17 notches, with the lowest corresponding to completely black. Here’s how much light I measured from the SpyderX with a dark grey uniform stimulus as a function of this setting. The first half of the scale is approximately exponential, the second half linear. You can decrease the amount of light coming from your screen by more than half simply by dimming the screen by several notches. Just make sure, if you use a laptop/second screen combo like I do, that the brightness of the second screen is synced to your primary screen; I set up the free MonitorControl app recently to do this.

### Increase light during the day

The ipRGC-SCN connection is not just modulated by night-time light; it’s modulated by day-time light.Research in rodentssupports the idea that the amplitude of diurnal oscillations in the SCN is affected by daytime brightness. The usual advice is to go outside and touch grass during the day—indeed, the sun is very bright, even under dark clouds. It’s also the case, however, that offices—and especially home offices—are frequently overly dim.LED light is incredibly cheap these days; you can get a ridiculously bright 100W LED lightbulb—not 100W “incandescent equivalent” light, 100 real Watts in the visible spectrum—for a few tens of dollars. You can then diffuse that light over a relatively large home office.

### Take melatonin

If you stack the three previous advice sections together, you could gain as much as 2-3 order of magnitude peak-to-trough luminance throughout your day. That might be enough to support your circadian rhythm health. If that’s not enough, however, recall that one of the ultimate outputs of the SCN is through the pineal gland, which releases of melatonin. Partly, it’s the inhibition of circulating melatonin that is causally responsible for sleep phase shift. It’s possible to remedy that by taking exogenous melatonin an hour before bed to facilitate the onset of sleep.

However, most melatonin supplements have far too high doses.Be very wary of melatonin dose. As explained in this excellently researchedSlate Star Codex post, over-the-counter melatonin supplements can contain anywhere between10 to 30 timesas much melatonin as is optimal to maintain circadian hygiene. If you have ever taken melatonin and got immediately knocked out cold, had weird dreams and woke up in the middle of the night sweaty or shivering, you likely took too much—which, to be clear, is not your fault, it’s the default in the US and Canada. The mega-doses in stores serve as hypnotics (punches you to sleep), but wreck sleep architecture. The right dose is 0.3 mg, which is hard to find in pharmacies but can be found online. This dose will not knock you out (feels more like chamomile tea than Ambien).

## Conclusion

I’ve been meaning to write about blue light for a long time—a perfect topic for a visual neuroscientist! The blue light filter story has just the right level of anchoring in reality—the entrainment of circadian rhythms by ipRGCs—to feel like a tantalizingone simple trickto fix your sleep. Simple but ineffective on its own, there is a kernel of truth behind the idea of blue light filters that can be used to come up with a better policy: use dark mode; dim your screen; touch grass; if all fails, consider melatonin.

1

For you camera aficionados, we maintain vision over about 20 stops–whereas halving light corresponds to one stop.

9
2
Share
