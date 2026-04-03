---
title: The Singularity will Occur on a Tuesday - Cam Pedersen
url: https://campedersen.com/singularity
site_name: hnrss
content_file: hnrss-the-singularity-will-occur-on-a-tuesday-cam-peders
fetched_at: '2026-02-10T19:29:28.551295'
original_url: https://campedersen.com/singularity
date: '2026-02-10'
published_date: '[object Object]'
description: src={alwaysHasBeen.src} alt="Always has been astronaut meme" / "Wait, the singularity is just humans freaking out?" "Always has been." Everyone in <span style={
tags:
- hackernews
- hnrss
---

"Wait, the singularity is just humans freaking out?" "Always has been."

Everyone inSan Franciscois talking about the singularity. At dinner parties, at coffee shops, at the OpenClaw meetup where Ashton Kutcher showed up for some reason. The conversations all have the same shape: someone says it's coming, someone says it's hype, and nobody has a number.

This seems like the wrong question. If things are accelerating (and they measurably are) the interesting question isn'twhether. It'swhen. And if it's accelerating, we can calculateexactly when.

I collected five real metrics of AI progress, fit a hyperbolic model to each one independently, and found the one with genuine curvature toward apole. The date hasmillisecond precision. There is a countdown.

(I am aware this isunhinged. We're doing it anyway.)

## The Data

Five metrics, chosen for what I'm calling theiranthropic significance(anthropic here in the Greek sense ("pertaining to humans"), not the company, though they appear in the dataset with suspicious frequency):

1. MMLU scores: the SAT for language models
2. Tokens per dollar: cost collapse of intelligence (log-transformed, because the Gemini Flash outlier spans 150× the range otherwise)
3. Frontier release intervals: shrinking gap between"holy shit"moments
4. arXiv "emergent" papers(trailing 12mo): field excitement, measuredmemetically
5. Copilot code share: fraction of code written by AI

Calibrating instruments...

Each metricnormalizedto[0,1][0, 1][0,1]. Release intervals inverted (shorter = better). Tokens per dollar log-transformed before normalizing (the raw values spanfive orders of magnitude; without the log, Gemini Flash at 2.5M tokens/$ dominates the fit and everything else is noise). Each series keeps its own scale, no merging into a single ensemble.

## Why Hyperbolic

Most people extrapolate AI withexponentials. Wrong move!

An exponentialf(t)=aebtf(t) = ae^{bt}f(t)=aebtapproaches infinity only ast→∞t \to \inftyt→∞. You'd be waiting forever. Literally.

We need a function that hits infinity at afinitetime. That's the whole point of a singularity: a pole, avertical asymptote,the math breaking:

x(t)=kts−t+cx(t) = \frac{k}{t_s - t} + cx(t)=ts​−tk​+c

Ast→ts−t \to t_s^-t→ts−​, the denominator goes to zero.x(t)→∞x(t) \to \inftyx(t)→∞. Not a bug.Thefeature.

Calibrating instruments...

Polynomialgrowth (tnt^ntn) never reaches infinity at finite time. You could wait untilheat deathandt47t^{47}t47would still be finite. Polynomials are for people who think AGI is "decades away."

Exponentialgrowth reaches infinity att=∞t = \inftyt=∞. Technically a singularity, but an infinitely patient one. Moore's Law was exponential. We are no longer on Moore's Law.

Hyperbolicgrowth is what happens when the thing that's growingaccelerates its own growth. Better AI → better AI research tools → better AI → better tools. Positive feedback withsupralinear dynamics. The singularity is real and finite.

## The Fit

The procedure is straightforward, which should concern you.

The model fits a separate hyperbola to each metric:

yi(j)=kjts−ti+cjy_i^{(j)} = \frac{k_j}{t_s - t_i} + c_jyi(j)​=ts​−ti​kj​​+cj​

Each seriesjjjgets its ownscalekjk_jkj​andoffsetcjc_jcj​. The singularity timetst_sts​is shared. MMLU scores and tokens-per-dollar have no business being on the same y-axis, but they can agree on when the pole is.

For each candidatetst_sts​, the per-series fits arelinear inkjk_jkj​andcjc_jcj​. The question is: whichtst_sts​makes the hyperbola fit best?

Here's the thing nobody tells you about fitting singularities: most metrics don't actually have one. If you minimize totalRSSacross all series, the besttst_sts​is always at infinity. A distant hyperboladegeneratesinto a line, and lines fit noisy data just fine. The "singularity date" ends up being whatever you set as the search boundary. You're finding the edge of your search grid, not a singularity.

So instead, we look for the real signal. For each series independently,grid searchtst_sts​and find theR²peak: the date where hyperbolic fitsbetterthan any nearby alternative. If a series genuinely curves toward a pole, its R² will peak at some finitetst_sts​and then decline. If it's really just linear, R² will keep increasing asts→∞t_s \to \inftyts​→∞and never peak. No peak, no signal, no vote!

One series peaks!arXiv "emergent" (the count of AI papers about emergence) has a clear, unambiguous R² maximum. The other four aremonotonicallybetter fit by a line. The singularity date comes from the one metric that's actually going hyperbolic.

This is more honest than forcing five metrics to average out to a date that none of them individually support.

Same inputs → same date.Deterministic. Thestochasticityis in the universe, not the model.

## The Date

Calibrating instruments...

The fitconverged! Each series has its ownR²at the sharedtst_sts​, so you can see exactly which metrics the hyperbola captures well and which it doesn't. arXiv's R² is the one that matters. It's the series that actually peaked.

The 95% confidence interval comes fromprofile likelihoodontst_sts​. We slide the singularity date forward and backward until the fit degrades past anF-threshold.

## The Countdown

Calibrating instruments...

## Sensitivity

How much does the date move if we drop one metric entirely?

Calibrating instruments...

If dropping a single series shiftstst_sts​by years, that series was doing all the work. If the shifts are zero, the dropped series never had a signal in the first place.

The table tells the story plainly: arXiv is doing all the work. Drop it and the date jumps to the search boundary (no remaining series has a finite peak). Drop anything else and nothing moves. They were never contributing to the date, only providing context curves at the sharedtst_sts​.

Note: Copilot has exactly 2 data points and 2 parameters (kkkandccc), so it fits any hyperbola perfectly. Zero RSS, zero influence ontst_sts​. It's along for the ride!

## Whattst_sts​Actually Means

The model saysy→∞y \to \inftyy→∞attst_sts​. But what does "infinity" mean for arXiv papers about emergence? It doesn't mean infinitely many papers get published on a Tuesday in 2034.

It means the model breaks.tst_sts​is the point where the current trajectory's curvature can no longer be sustained. The system either breaks through into something qualitatively new, or it saturates and the hyperbola was wrong. Aphase transition marker, not a physical prediction.

tst_sts​is the moment he looks down.

But here's the part that should unsettle you:the metric that's actually going hyperbolic is human attention, not machine capability.

MMLU, tokens per dollar, release intervals. The actual capability and infrastructure metrics. All linear. No pole. No singularity signal. The only curve pointing at a finite date is the count of papers about emergence. Researchers noticing and naming new behaviors.Field excitement, measured memetically.

The data says: machines are improving at a constant rate. Humans are freaking out about it at an accelerating rate that accelerates its own acceleration.

That's a very different singularity than the one people argue about.

## The Social Singularity

Iftst_sts​marks when the rate of AI surprises exceeds human capacity to process them, the interesting question isn't what happens to the machines. It's what happens to us.

And the uncomfortable answer is:it's already happening.

The labor market isn't adjusting. It's snapping.In 2025,1.1 million layoffs were announced. Only the sixth time that threshold has been breached since 1993. Over55,000 explicitly cited AI. ButHBR foundthat companies are cutting based on AI'spotential, not its performance. The displacement is anticipatory. The curve doesn't need to reach the pole. It just needs tolook like it will.

Institutions can't keep up.The EU AI Act's high-risk rules havealready been delayed to 2027. The USrevoked its own 2023 AI executive orderin January 2025, then issued a new one in December trying to preempt state laws. California and Colorado aregoing their own way anyway. The laws being written today regulate 2023's problems. By the time legislation catches up to GPT-4, we're on GPT-7. When governments visibly can't keep up, trust doesn't erode. Itcollapses. Global trust in AI has dropped to 56%.

Capital is concentrating at dot-com levels.The top 10 S&P 500 stocks (almost all AI-adjacent) hit40.7% of index weightin 2025, surpassing the dot-com peak. Since ChatGPT launched, AI-related stocks have captured75% of S&P 500 returns, 80% of earnings growth, and 90% of capital spending growth. TheShiller CAPEis at39.4. The last time it was this high was1999. The money flooding in doesn't require AI to actually reach superintelligence. It just requires enough people to believe the curve keeps going up.

People are losing the thread.Therapists arereporting a surgein what they're callingFOBO(Fear of Becoming Obsolete). The clinical language is striking: patients describe it as"the universe saying, 'You are no longer needed.'"60% of US workersbelieve AI will cut more jobs than it creates. AI usage is up 13% year-over-year, but confidence in it hasdropped 18%.The more people use it, the less they trust it.

The epistemics are cracking.Less thana third of AI research is reproducible. Under 5% of researchers share their code. Corporate labs are publishing less. The gap between what frontier labs know and what the public knows is growing, and the people making policy are operating on information that'salready obsolete. The experts who testify before Congress contradict each other, because the field is movingfaster than expertise can form.

The politics are realigning.TIMEis writing about populist AI backlash.Foreign Affairspublished "The Coming AI Backlash: How the Anger Economy Will Supercharge Populism."HuffPostsays AI will define the 2026 midterms. MAGA issplittingover whether AI is pro-business or anti-worker. Sanders proposed a data center moratorium. The old left-right axis is buckling under the weight of a question it wasn't built to answer.

All of this is happeningeight years beforetst_sts​. The social singularity isfront-runningthe technical one. The institutional and psychological disruption doesn't wait for capabilities to go vertical. It starts as soon as thetrajectorybecomes legible.

The pole attst_sts​isn't when machines become superintelligent. It's when humans lose the ability to make coherent collective decisions about machines. The actual capabilities are almost beside the point. The social fabric frays at the seams of attention and institutional response time, not at the frontier of model performance.

## Caveats

The date comes from one series.arXiv "emergent" is the only metric with genuine hyperbolic curvature. The other four are better fit by straight lines. The singularity date is really "the date when AI emergence research goes vertical." Whether field excitement is aleading indicatoror alagging oneis the crux of whether this means anything.

The model assumesstationarity.Like assuming the weather will continue to be "changing." The curve will bend, either into alogistic(the hype saturates) or into something the model can't represent (genuine phase transition).tst_sts​marks where the current regime can't continue, not what comes after.

MMLU is hitting its ceiling.Benchmark saturation introduces aleptokurtic compression artifact. MMLU's low R² reflects this. The hyperbola isthe wrong shapefor saturating data.

Tokens per dollar islog-transformed(values span five orders of magnitude)andnon-monotonic(GPT-4 cost more than 3.5; Opus 4.5 costs more than DeepSeek-R1). The cost curve isn't smooth: it'sPareto advancesinterspersed with"we spent more on this one."

Five metrics isn't enough.More series with genuine hyperbolic curvature would make the date less dependent on arXiv alone. A proper study would add SWE-bench, ARC, GPQA, compute purchases, talent salaries. I used five becausefive fits in a table.

Copilot has two data points.Two parameters, two points, zerodegrees of freedom, zero RSS contribution. The sensitivity analysis confirms it doesn't matter.

## Conclusion

Real data. Real model. Real date!

The math found one metric curving toward a pole on a specific day at a specific millisecond: the rate at which humans are discovering emergent AI behaviors. The other four metrics are linear. The machines are improving steadily.We are the ones accelerating!

The social consequences of that acceleration (labor displacement, institutional failure, capital concentration, epistemic collapse, political realignment) are not predictions for 2034. They are descriptions of 2026. The singularity in the data is a singularity in human attention, and it is already exerting gravitational force on everything it touches.

I see no reason to letepistemological humilityinterfere with aperfectly good timer.

See you on the other side!
