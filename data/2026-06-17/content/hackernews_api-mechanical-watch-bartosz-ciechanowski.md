---
title: Mechanical Watch – Bartosz Ciechanowski
url: https://ciechanow.ski/mechanical-watch/
site_name: hackernews_api
content_file: hackernews_api-mechanical-watch-bartosz-ciechanowski
fetched_at: '2026-06-17T06:00:16.962389'
original_url: https://ciechanow.ski/mechanical-watch/
author: Bartosz Ciechanowski
date: '2026-06-16'
description: Mechanical Watch (2022)
tags:
- hackernews
- trending
---

May 4, 2022

# Mechanical Watch

In the world of modern portable devices, it may be hard to believe that merely a few decades ago the most convenient way to keep track of time was a mechanical watch. Unlike their quartz and smart siblings, mechanical watches can run without using any batteries or other electronic components.

Over the course of this article I’ll explain the workings of the mechanism seen in the demonstration below. You can drag the device around to change your viewing angle, and you can use the slider to peek at what’s going on inside:

What you see here is known as themovement– the inner part of a mechanical watch that’s usually enclosed in a metal case. In this article I’m focusing on a watch movement itself, since beautiful watch cases merely hide the intricate mechanisms which are the real stars of the show.

The entire watch movement has a lot of parts, and in this blog post I’ll explain the purpose of each one. The world of watchmaking is jargon-heavy, so many of the components may have unfamiliar names, but you shouldn’t feel pressured to remember them – the names and parts will becolor-codedfor easy reference.

In a functioning watch many parts are in constant motion. By default all animations in this article areenabled, but if you find them distracting, or if you want to save power, you canglobally pauseall the following demonstrations.disabled, but if you prefer to have things moving as you read you canglobally unpausethem and have animations running.

While the entire watch movement has many parts, the timekeeping system, which forms the core function of any watch, consists of just seven major elements which we can lay out in a straight line:

It may not look like much, but these parts still have a lot of interesting details about them that contribute to thesecond handrotating at a correct pace. We’ll start exploring these details by focusing on the source of power for this entire contraption.

# Power

Purely mechanical devices have a few different ways to power themselves, but one of the simplest methods to store energy is to use a spring. Most springs we see in daily life arecoilsprings. In the demonstration below, you can move themassattached to this type ofspringto see it bounce:

When aspringlike this is compressed, it stores some energy that is then released when the compressing tension is removed. Mechanical watches typically use a different kind of spring – a spiraltorsionspring. This type ofspringis loaded when it’s twisted. When let go, thespringunwinds in the opposite direction to eventually settle in its natural state:

In a mechanical watch, we ultimately want to show rotating hands, so a spinning motion that a torsion spring provides is particularly useful. Aspringin a typical mechanical watch has a slightly more complicated shape – you can see it below in its relaxed state. By dragging theslideryou can try to wind it midair, but as soon as you let go, it will snap back to its original shape:

As you can see, thisspringis quite strong and it wants to expand very rapidly. To contain thespringwe have to put it in a casing known as abarrel:

Once in thebarrel, thespringstill wants to expand to its original state, but thebarrel’swall keep it in place. Thisspringis the storage of energy for the watch and its name, themainspring, reflects its importance.

Unfortunately, we can’t really get any useful work from themainspringin this state – it has already expanded to the largest possible size. To store more energy in it we need to wind it tightly using thearborthat we’ll first attach on the inner side of themainspring:

If you look closely, themainspringhas a little hole near its end – you can see it in the center of the demonstration. Thearborhas a little hook that grabs onto that hole:

When thearboris turned, it pulls themainspringwith it, causing it to wind. In the demonstration below, we’re holding thebarreltight, and you can turn thearborby dragging the slider:

Notice that as soon as you let go of thearborby releasing the slider, themainspringwill turn thearborright back. This is less than desired – we want thebarrelto turn instead, so that it can power the other parts of the watch. To get some useful work from themainspring, we’ll have to keep holding on to thearborand instead let thebarrelgo when we want to use the stored energy:

We’ll soon see how this is accomplished in practice, but for now we’ll assume that thearboris held tight and themainspringends up rotating thebarrel, just like in the demonstration above. Before we finish up with themainspringand thebarrel, let’s discuss two other details that make this mechanism more reliable. Let me bring up the relaxed spring one more time:

Themetal stripattached to themainspringprovides additional tension to its outer part. Thatmetal stripreally wants to snap back to its straight shape, so it pushes against the wall of thebarrel, creating a lot of friction that keeps the mainspring in place:

This locks the outer end of themainspringwhen thearbormoves the inner. If we were to keep winding thespringpast its maximum capacity, we’d overpower that friction letting themainspringslip inside – this acts as a safety mechanism to prevent the parts from breaking.

As we’ve seen, in its relaxed state, themainspringforms an S-shape with varied curvature throughout. This helps to balance the tension inmainspring’sdifferent sections when it is inside thebarrel. Notice that the inner sections of the wound spring have a much smaller radius than the outer parts. If the relaxed spring was just a straight piece of metal, then after winding, the inner parts would be bent much more than the outer parts. With the S-shaped spring the outer sections of the spring are also under a similar tension because they want to get back to their curve that is bent in the opposite direction.

To secure themainspringand prevent dust from getting in we close thebarrelwith a lid that snaps into its place:

We’ve managed to make some parts rotate and one could naively think that we could just attach awatch handto thebarrelto make it track time. Unfortunately, that won’t really work – you can witness this in the demonstration below. You can see how this “watch” behaves after you wind themainspringwith the slider and let it go:

We clearly have some work to do – thehandspins way too fast and it only does a few rotations before themainspringinside thebarrelruns out of the stored energy. Clearly, this contraption won’t let us track time in any reliable way.

If we wanted our watch to run continuously for around 40 hours on a single wind, we’d need the minute hand to complete 40 rotations in that time. Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations in that time. We need to find a way to convert a small number of revolutions of thebarrelinto a large number of revolutions of the hands. This is where gears come in.

# Gears

I’vetalked about gearson this blog before, so let me just recap things very briefly. Gears can be used to change the speed of rotation between two different axes. In the demonstration below, you can witness that by observing little dots I put on each gear – theyellow gear, which is powered by the biggerred gear, takes much less time to finish a single revolution:

An important aspect of two matching gears is their number of teeth. Each tooth in one gear meets with a space between teeth in the other gear, so within a unit of time both gears rotate by the same number of teeth. If the number of teeth in two gears is different, those gears can take a different amount of time to complete a single rotation. In the demonstration below, you can change theratioof the number of teeth between the drivingred gearand the drivenyellow gearto see how it affects the speed of rotation of thatyellow gear:

These gears are intended to work with each other so the ratio of teeth is equivalent to the ratio of the gear radii. When thedriving gearhasmore teeththan thedriven gear, thedriven gearmakes more rotations than thedriving gear. We can use this behavior to make the second hand of a watch rotate many times on a single rotation of the barrel.

Let’s consider how much of a speed increase we have to do here. The barrel can rotate close to 7 times on a single wind, but we want the second hand to complete around 2400 revolutions in the same time. We need the ratio of teeth, or the ratio of radii, to be around 343:1. Let’s see how that would look in practice. In the demonstration below, you can use the slider to look at the two gears from further away:

As you can see, these proportions are ridiculous – to make thered gearfit in any reasonably sized watch, theyellow gearwould have to be absolutely tiny and both gears would have to have very fragile, microscopic teeth.

Instead, mechanical watches use atrainof gears with multiple gears working in pairs – each pair increases the speed to some extent. In the demonstration below, you can see the four wheels participating in this reduction. Notice that there are two gears on most axes of rotation. You can control the speed of rotation of this gear train using the slider:

Thebarrelacts as thefirst wheel, it drives thesecond wheel, which drives thethird wheel, which finally drives thefourth wheel. Notice that each big gear drives a smaller gear called apinion. A pinion is mounted on the same shaft as the next big gear so we’re able to keep increasing the speed on each axis. This approach has significant advantages – we’re able to make the overall mechanism much smaller and we’ll soon use one of the intermediate wheels that rotates at a slower rate to drive minute and hour hands.

Before we finish up with gears, let me quickly mention the shape of their teeth. While many bigger machines use aninvolute shapefor the profile of their gear teeth, mechanical watches commonly usecycloidalprofiles which are obtained byrolling a circle on the surface of another circle.

Let’s see how the so-calledgoing trainthat we’ve assembled works when we wind themainspringthrough thearborand let the watch run:

We’ve certainly achieved the goal of thesecond handrotating many times on a single rotation of thebarrel, but the speed of revolution of thathandis still completely untamed. We need to find a way to control the rate of release of the energy stored in themainspring– we’ll do this with theescapement.

# Escapement

Let’s start by looking at the two components that create the escapement – theescape wheeland thepallet fork:

Notice the unusual shape of the teeth of theescape wheel– it’s very different than the gears we’ve seen before. Its top part hosts a regularly shaped gear that can be used to turn thatwheel.

Thepallet forkitself is made of metal, but notice the twopinkishtransparent parts at its end. These arejewelsmade from syntheticruby. That compound is not only very hard, which prevents its wear, but it also has a low coefficient of friction with steel. Let’s see why these properties are important by observing how these two components interact with each other:

Theescape wheelwants to rotate as indicated by thered arrow. Thepallet forkprevents that motion, but as we pivot thatpallet forkback and forth we let theescape wheelbrieflyescapefrom that jail only to be stopped again.

We’ll see the details of that interaction in a few paragraphs, but right now this mechanism lets us control the rotation of theescape wheelby simply moving thepallet forkfrom one side to another. Let’s see how these pieces fit into the rest of the assembly. In the demonstration below, I’ve wound the spring for you so thebarrel, through the gear train, ends up trying to rotate theescape wheel. Using the two buttons you can switch the position of thepallet fork:

The mainspring wants to unwind by rotating theescape wheel, but thepallet forkonly allows this to happen for a brief period of time. Because of the gear reduction, the rotation of thebarrelis pretty much invisible. However, if you observe thehandattached to thefourth wheel, you can see it gently rotate as you swing thepallet forkback and forth.

The little time keeping mechanism is almost fully functional now. The last remaining piece here is a device that will automatically tick thepallet forkback and forth. However, for the watch to track time correctly that ticking action has to happen at an appropriate cadence. This is where thebalancecomes in – it forms the beating heart of a watch.

# Balance

Let’s bring up the first torsion spring we saw before – recall that once you twist it from its original position, it will oscillate back and forth, only to settle after a while:

We can control the rate of this periodic motion by adjusting two parameters. The first one is thestiffnessof the spring, which primarily depends on its height, thickness, and length, as well as the type of material from which it’s made. The second one is the mass and its distribution, or, more precisely, themoment of inertiaof the object that the spring rotates. Moment of inertia increases when more mass is put further away from the axis of rotation. In the demonstration below, you can tweak both thestiffnessof the spring andmoment of inertiaof the attached mass to see how these parameters affect the period of rotation:

By carefully tuning these parameters, we can make this system oscillate at a desired rate. This idea of using a torsion spring with attached mass is exactly what mechanical watches use as their source of precise time tracking. The balance is formed by thebalance wheelattached to thebalance spring. In this watch thebalance wheeloscillates back and forth at a fairly high frequency:

At thebottom sideof the balance wheel you’ll find another pinkish transparent jewel calledjewel roller. While small, this part is very important – thisjewelhits the other end of thepallet forkas thebalance wheelrotates, which in turn pushes thepallet forkback and forth. Let’s first look at an overview of how thebalance wheelinteracts with the other parts. In the demonstration below, you can slow things down with the slider:

Let’s look at this interaction up close, as it deserves a closer attention. In the demonstration below, you can scrub back and forth in time to see all the action as it happens:

balance wheelis swinging backjewel rollerstrikes thepallet fork, knocking it out of positionescape wheelunlocks and pushes thejewelof thepallet forkpallet forkpushes thejewel rollerand thebalance wheelescape wheellocks againbalance wheelcontinues its swing

As thebalance wheelswings, thejewel rollerstrikes thepallet fork, which unlocks theescape wheel. Once unlocked, theescape wheelpowered by the mainspring pushes on thepallet forkwhich, through thejewel roller, pushes on thebalance wheelitself. This causes thebalance wheelto gain some energy, which prevents it from stopping after a while – it’s equivalent to giving a push to a person swinging on a swing. When thebalance wheelcomes back, it performs the same action, just in the other direction.

You may also have noticed a subtle dance between thelittle hornat the end of thepallet forkand thenotched diskon thebalance wheel. Those parts make sure that thepallet forkcan switch sides only at the appropriate time – it’s a safety mechanism that prevents the watch from locking up when the watch is shaken or dropped:

Once thepallet forkunlocks theescape wheel, that wheel has to start spinning very quickly. This is why gears in the gear train have holes in them – it reduces their moment of inertia so that thebarrelcan accelerate them more quickly.

It’s also important to mention that the gear train not only increases the speed of the gears, but it also reduces the forces acting on the balance. Thebarrelitself turns quite forcefully but at theescape wheelthetorqueis greatly reduced, which prevents theescape wheelfrom pushing thepallet forkand thus thebalance wheelwith too much vigor.

Let’s look at the entirety of what we’ve built so far one last time. I’m now running the mechanism at its normal speed:

In this watch movement thebalance wheeldoes a full back and forth swing four times per second, hitting thepallet forktwice during each cycle, for a total of 8beatsper second or 28,800 beats per hour. While different watches may have different rates, they all do a tiny turn of thesecond handmany times per second, which gives mechanical watches the illusion of a very smooth hand motion.

In principle, all the pieces we have here are sufficient for the watch to run, but we’re still missing a few details. More importantly, we’ve just been hanging the parts in the air, so it’s time we started a proper assembly of the complete watch movement.

# Mainplate

We’ll start with themainplate, which forms the main body of the movement:

Notice that it hasa lotof different openings – we’ll fill them in by the end of this article. The pink elements are yet againruby jewels. They form bearings in which the axes of various components can rotate. Let’s look at a simple jewel up close:

Notice that ajewelhas a small basin in it. To even further reduce energy losses of the rotating components, a small amount of special oil is placed in that cavity. That oil sticks to thejeweland a shaft that rotates inside it to further decrease the friction, which lets the watch run longer on a single wind, while also reducing wear on the delicate mechanical parts.

The first two components we will mount onto the mainplate are theescape wheeland thepallet fork:

Thepallet forkitself is then topped with thepallet fork bridge. Thatbridgeholds the other end of thepallet fork’saxis, and it is attached to the mainplate withtwo screws:

Notice that in this watch the side-to-side movement of thepallet forkis limited by the shape of the two knobs in the central part of thepallet fork bridge:

This ensures that theescape wheelcan only push thepallet forkso far before the motion is physically stopped by these knobs.

Next, we can put the rest of the gear train in. All four wheels are cleverly arranged so that they occupy only a small amount of space:

Notice that thefourth wheelgoes directly through the center of the watch – you can see its axis poking on the other side. By the end of our assembly we’ll attach a second hand on the end of that long axis. To secure all elements in place, we cap them with atrain wheel bridge, which provides the setting for the other ends of the shafts for all rotating parts. Thatbridgeisscrewedto the mainplate to hold everything in place:

The only remaining part from the initial mechanism that we haven’t yet mounted is the balance, which forms its own little assembly. Let’s build it up first by attaching all the parts to thebalance bridge:

Notice that thebalance springis very delicate and thebalance wheelends up stretching it out. Because of its thinness, thebalance springis often referred to ashairspring. Theyellowandtealcomponents both regulate the behavior of the balance. Let’s see how they work in action:

Theyellow componentsare firmly attached to thebalance spring, and by turning them, we can adjust the resting position of thebalance wheeland itsjewel roller. This ensures that both the “tick” and “tock” phases of thebalance wheelswing take the same amount of time.

Theteal componentscan freely slide on thehairspring, but they reduce or increase its effective length as they prevent the tail section of thehairspringfrom oscillating freely. By adjusting position of theseteal componentswe can modify the duration of a single beat and make the watch run slightly faster or slower. That speed regulation can also be fine-tuned using thescrewin the top part – its head is not centered, so when turned it will gently rotate the littleteal fork.

Thehairspringis made from special alloys likeNivaroxthat keep the spring’s stiffness invariant to temperature differences, which improves the overall timekeeping accuracy.

The final portion of the balance assembly is the shock protector mechanism, which consists of thecasing,two jewels, and atiny springthat keeps everything in place:

This mechanism protects the fragile tips of thebalance shaftfrom breaking when the watch experiences a sudden jerk. Let’s see how these pieces act together when thebalance shaftis jolted around:

When the watch is shaken, the motion of theshaftis absorbed by thespring, similarly to the suspension system in a car. If the jerk is very strong, then the much thicker and stronger part ofbalance shaftcarries the load through thecase, which protects the fragile tip from breaking.

Let’s attach the entire balance assembly to the rest of the movement we’ve built so far. Notice that the other end of thebalance wheel’saxis also rests on the shock protection jewels embedded in the mainplate:

With that last step, we’ve actually finished recreating the core of the watch mechanism that we’ve previously seen floating in the air. However, you may remember that I’ve glanced over the little detail of how to make sure that themainspringstays wound. Let’s see what happens if we actually try to wind the watch using thearbor. For the sake of clarity I also cut a hole in the top part of thebarrelso that you can see thespringinside:

As long as thearboris held, themainspringcan power the rest of the watch – you can see the rotation of thesecond handattached to thefourth wheelon the other side of the watch. However, as we let thearborgo themainspringfinds an easy way to release its tension by just turning thearborback – thespringquickly losses all its stored energy and the watch stops.

To prevent themainspringfrom unwinding on its own, we need to restrain thearborfrom turning counterclockwise, while still allowing theclockwiserotation so that we can wind thespring. This seemingly complicated problem is solved with a very simple mechanism known as theclick– let’s see how it works.

# Click

To continue developing our assembly, we firstly need to put a solid foundation in the form of thebarrel bridge– it holds thebarrelin place and provides structure for other parts. Since thisbridgewill make some areas inaccessible, we’re also going to attach alittle leverthat we will get back to at a later point:

Then, we’llscrewin theratchet wheelonto thearbor. Notice that theratchet wheelhas a square opening, which matches the square shape of the top part of thearbor:

Those matching square shapes will cause thearborto turn when theratchet wheelis turned. I temporarily removed thescrewto make things easier to see:

Here come the three critical pieces of the puzzle. Firstly, we put the littleclickin the opening on top of thebarrel bridge:

Within its limited range theclickcan rotate back and forth on its little axis:

The second piece of the puzzle is aclick spring. This little piece of metal is very springy. When wesqueezeit, it wants to pop back:

We compress thatclick springa little and we also put it into thebarrel bridge:

Notice that when we try to rotate theclick, theclick springwill push it back in place as soon as we let go:

The final piece of the puzzle is thecrown wheel, which also lands on thebarrel bridge. It’s secured in a place with ascrewwith a left-handed thread – unlike most regular screws this one is fastened when turned in thecounterclockwisedirection:

Notice how the teeth of thecrown wheelinteract with theratchet wheel. While it looks as if thecrown wheelwas missing every other tooth, the two gears can still mesh and function together. The gaps in thecrown wheelallow the little post on theclickto fall between thecrown wheel’steeth.

If weturnthecrown wheelcounterclockwise, it will mesh with theratchet wheeland wind the spring. Notice how the teeth of thecrown wheelend up pushing theclickaway, but it snaps back as soon as there is some space:

When theclicksnaps back and hits thecrown wheel, it makes aclickingsound, which explains its name.

The counterclockwise turn of thecrown wheelallows us to wind the mainspring, so let’s see what happens when we try toturnit in the opposite direction. In the simulation below, notice how thecrown wheel’steeth jam with theclick, preventing thecrown wheel’srotation:

This simple mechanism allows us to wind the mainspring by turning thecrown wheel, which you can do in the demonstration below. Theclickalso prevents the mainspring from unwinding on its own – that’s why you can’t drag back the slider without restarting the entire simulation:

Thesecond handon the other side of the watch shows how the seconds are tracked, but a functional watch should show minutes and hours as well. Let’s see how this watch movement accomplishes these goals with a set of gears that form the so-calledmotion works.

# Motion Works

In our movement, the second hand is cleverly mounted on the fourth wheel of the power train since that wheel rotates once per minute with high precision. For the minute hand to turn at the correct pace, we needsomeaxis to rotate 60 times slower than that. Thankfully, the designers of this watch movement used an ingenious way to harness some of that speed reduction from the other gears.

If you look closely, you can see that the small gear of thethird wheelfrom the other side of the watch is exposed through a little opening. We can mount acannon pinionwith itsdriving wheelonto the center of the watch and have thatdriving wheelmesh with thesmall gear:

When thatthird wheelrotates, it turns thedriving wheeland thus thecannon pinion. By mounting the minute hand on thatcannon pinionwe can keep track of passing minutes – the number of teeth in all the involved gears is carefully calculated to achieve the desired 60 times speed reduction compared to the second hand.

Let’s see the functional second hand and minute hand in the demonstration below. The slider lets you control the speed of flowing time so that you don’t have to wait too patiently to see hands change their position:

The hour hand itself needs to rotate 12 times slower than the minute hand, but we can easily achieve that using two additional gears. The intermediateminute wheelmeshes with thecannon pinion, and thehour wheelmeshes with the pinion of thatminute wheel:

Thehour wheelcan loosely rotate on thecannon pinionso that they can both turn independently of each other. By putting the hour hand on thathour wheel, we can finish assembling the mechanism that drives the hands of the watch. I’ve also attached adialthat has each of the twelve hours marked – it actually lets us read the time that the hands are showing:

Time keeping is the fundamental function of every watch, but many devices go beyond that by adding various additional features known ascomplications. While our movement is not very sophisticated, it still has a nice complication that shows the current day of the month right in the little window on the right side of the dial. Let’s see how this feature is implemented.

# Date

The date mechanism in this watch consists of four major parts – thejumper spring, theindicator gear, thedate jumper platewith itsgear, and the big date ring itself with all possible 31 days imprinted on it:

To explain how this mechanism works I’ll first hide all the unrelated parts. I’ll also remove the cover from theindicator gear, which reveals asmall torsion springhidden inside it. Let’s see how these pieces work together when thehour wheelrotates. You can go back and forth in time using the slider:

As thehour wheelturns, it rotates thegearin thedate jumper plate. The other side of thatgearthen turns theindicator gearand thetorsion springattached to it. Thatspringsnags onto a tooth on the date ring and gets flexed, but at some point it starts to push the date ring forward. When the ring rotates enough thejumper springrapidly snaps the ring to the next position.

You may wonder why we need this complicated mechanism in the first place. One could naively assume that we could directly tie the rotation of the date ring to the rotation of thehour wheel, similarly to how we rotated thehour wheelin sync with minutes, albeit at slower pace. Unfortunately, this would cause the current date tocontinuouslyrotate under the little window in the dial, making it hard to read. You can see that behavior on the left side in the demonstration below:

On the right side you can see the date indicator as operated by the mechanism that we’ve just built – the date only changes around midnight. You may have realized that the date tracking in our movement is not particularly smart. This watch always counts 31 days every month, so we have to change the date a day after a shorter month occurs. Moreover, if the watch hasn’t been running for a while, the time itself may be incorrectly set. We need to find a way to adjust date and time on our watch.

Thankfully, gears driving the minute hand, the hour hand, and the date indicator are all connected, so we can adjust everything by turning asingle gear. I’ll briefly hide thehour wheelto make things visible:

Notice that when we turn theminute wheelonly thecannon pinionturns. Thatpinionfits tightly inside itsdriving gear– it usually turns with thatgear. However, when thedriving gearcan’t rotate because it’s blocked by the rest of the gear train, thecannon pinioncan overpower the friction of that tight fit and rotate on its own. This lets us set time without interfering with the gear train, which could break the delicate parts.

With thehour wheelin place, rotation of theminute wheelalso sets the hour, and, if we turn thatgearlong enough, the date:

With every step our watch is becoming more complete, but we still have a few inconveniences in our way. To change the time and to wind the mainspring, we have to turn the internal gears of the movement, which normally are safely hidden inside the watch case.

Moreover, on every month that lasts less than 31 days, we currently have to tweak the time setting, as that’s the only way to adjust the date. Ideally, we’d find a way to set the date separately from the time.

To fix these problems we’ll assemble thekeyless workswhich is a mechanism that will let us resolve all these issues.

# Keyless Works

Firstly, let’s look at thecrown, which is the main interface for operating the watch, and thestemthat is attached to that crown:

The crown sits freely on the outside of the watch and is directly touched by the user. Notice that part of the stem has a square cross section. The stem carries two additional components – thewinding pinionand thesliding pinion. First, let’s slide them on to see how they fit:

Thewinding pinionhas a circular opening so it can rotate on thestemeasily. However, thesliding pinionhas asquareopening which aligns with the section of thestemthat has a square shape. That square interlocking causes thesliding pinionto rotate with thestemas thecrown turns:

Let’s put these pieces into the main assembly. I temporarily removed the date ring so that it doesn’t get in our way:

Notice that thewinding pinionmeshes with thecrown wheelon the other side of the watch. To actually turn thewinding pinionwe first have to move thesliding pinionall the way towards it – I symbolize this pushing force with theblue arrowbelow. If we nowturn the crownthe matching shape of the neighboring surfaces on thewinding pinionand thesliding pinioncauses them to interlock. We’re ultimately able to turn thecrown wheeland the rest of the mainspring-winding machinery byturning the crownclockwise:

However, if werotatethe crown in theotherdirection, the shape of the neighboring surfaces will push thesliding pinionaway, because thecrown wheel, and therfore thewinding pinion, can’t rotate in the opposite direction. This safety mechanism ensures that any forceful rotation of the crown in the “wrong” direction won’t break the movement.

It seems that we’ve achieved our goal of being able to wind the spring by simplyturning the crown. Unfortunately, we still have a small problem to solve – we need something to actually exert the force that pushes thesliding piniontowards thewinding pinion.

Moreover, in some cases we want therotation of the crownto serve different purposes. Other than winding the mainspring, in our watch we want to be able to adjust the date, and, separately, the time. We’ll choose each of those three actions by pulling the crown in and out.

Let’s build a mechanism that will solve these problems. Firstly, we’ll put thecorrector leverand thesetting leverin place:

If we nowpull the crownin and out, these parts will rotate on their little pivots with a fairly complex interaction between them:

With the other parts in the way it may be hard to see what’s going on, so let’s look at these components on their own. Notice the intricate interlocking that happens when wepull the crownin and out with the slider:

A groove in thestemends up locking with asmall postin thesetting lever, causing it to rotate as thecrown is pulled. Theother poston thesetting leverends up pushing and hooking with thecorrector lever, making it rotate as well.

So far the mechanism doesn’t do anything interesting, so let’s put thesetting wheelon top of thecorrector lever:

Thatwheelcan move freely on its post. If we nowpull the crownin and out we can see that thesetting wheelengages with the minute works:

By turning thatsetting wheelwe’ll be able to set time on the watch, but to turn thatwheelwe need to slide thesliding piniontowards it so that therotation of the crownand the attachedsliding pinionrotates thesetting wheel:

This poses a challenge – we need to control the position of thesliding pinionto, depending on the mode, engage thewinding pinionto wind the mainspring, or thesetting wheelto set the time. This is where theyokecomes in:

In the close-up down below you can observe thatyokefits into the groove on thesliding pinion, so as theyokerotates on its pivot, it will push thesliding pinionin and out, causing it toslide. Additionally, theyokeitself is pushed by thesetting leveras wepull the crown:

We’re almost done with this little mechanism, we just need to finish the little details. Firstly, we want to keep all the fragile pieces in place – right now nothing prevents them from falling off their careful placement. Secondly, when wepull the crown, there are no distinctive stops in its movement – by turning the crown we may accidentally change the current mode. Finally, when wepush the crownall the way in to switch back to the winding mode, we want theyoketo reliably return to its initial position. This is where thesetting lever jumpercomes in – it serves all three of these purposes:

That part isscrewedto the mainplate, which prevents the other parts from falling out. Its various arms and legs also help to keep the things pressed down. Let’s see how thesetting lever jumperhelps us with other two problems. Notice the three small grooves that I’m pointing out with thegray arrows:

As wepull the crownin and out, thesmall postin thesetting leverends up snapping into one of those three places. To jump between the grooves, thatsmall posthas to bend the long arm of thejumper, which creates tension that pushes thatsmall postinto the closest groove. We end up with three distinct positions that all the pieces can rest in – once locked we can reliably turn the crown without risk of accidentally changing the current mode.

Finally, on the other end of thesetting lever jumperwe also have a thin section that is kept under tension against theyoke– I’m pointing its location with agray arrow:

As theyokerotates, that springy piece of metal wants to rotate theyokeback. When the crown is in the date or time setting mode, thesetting leverprevents theyokefrom coming back, but once we return to the winding mode, that spring in thejumperwill rotate theyokeback causing thesliding pinionto move back as well.

There is actually one additional clever bit that’s been hiding in plain sight. If you recall, we put a smallleverright on the mainplate before we started working on the winding mechanism. The short end of thatleverfits in the groove of thesliding pinion. When wepull the crownand move thesliding pinion, thatleverrotates:

When turned all the way, thatleverrubs against thebalance wheelpreventing it from moving – this stops the watch. As a result, when wepull the crownall the way out to enter the time setting mode, thatstop leverblocks thebalance wheel, which stops the watch in an action known ashacking. This lets us set the time without the second hand changing on its own at the same time, aiding with more precise time adjustment.

Let’s look at the functions of this entire mechanism one more time with all the participating pieces in place. When the crown is full pushed in, itsrotationwill rotate thesliding pinion, which turns thewinding pinion, and then thecrown wheel, and finally theratchet wheelto wind the mainspring:

When the crown is pulled all the way out, itsrotationturns thesliding pinion, thesetting wheel, and then theminute wheel, thehour wheel, and the hiddencannon pinionwhich allows us to set the time:

Finally, when the crown is pushed roughly halfway through, we enter date setting mode, but to see it work we still need to attach an additionaldate correctorthat fits into the small groove on the mainplate:

Notice that thedate correctorcan freely slide up and down in that groove. If we now pull the crown out mid way andturnit, we end up rotating thatdate corrector, which then can engage with the teeth on the inside of the date ring. Thedate jumper springmakes sure that we lock the date ring at a valid position:

Personally, I think this entire mechanism known as thekeyless worksis a real mechanical marvel. The intricate interactions are so well balanced and each part serves many different roles. Older pocket watches were wound by a separate key, with the crown being used only to set the time, but modern watches get away with not having a winding key, which explains thekeylessname. With just a few carefully shaped pieces and a single crown, we can control various settings of the watch. Before we move on, let’s secure the remaining pieces with theminute train bridge:

We’re almost done building the watch movement. The final component that we’ll assemble will make the watch automatically wind itself as we roam around.

# Automatic Winding

When the person wearing a watch moves arms throughout the day, the orientation of that watch in space changes quite a lot. Even during a leisurely walk, the watch swings slightly relative to the ground. Normally, all the energy used to move the watch goes to waste, but an automatic winding mechanism manages to capture some of it to wind the mainspring.

Let’s first try to understand the main idea by attaching the complete automatic winding mechanism to the watch. Its primary part is theweightthat can rotate freely around the center. When thatweightrotates it drives abunch of gears, with thelast oneconnecting to theratchet wheelthat is used to wind the mainspring hidden inside thebarrel:

The fact that theweightcan rotate freely is critical here. In the demonstration below, you can witness what happens to theweightas you rotate the watch in space by dragging it around. The gravity works towards the bottom of this website – it always pulls theweightdown, which makes it turn relative to the rest of the watch:

If you recall our discussion of watch winding, you may remember that theratchet wheelcan only turn in one direction with the click preventing the mainspring from just unwinding on its own. However, theweightcan swing back and forth, which would normally imply that any gear system that is connected to thatweightwould also rotate in both directions.

If you look at the automatic winding mechanism on its own, you can witness something unusual – as you turn theweightback and forth with the slider, theoutput gearturns only inonedirection. I put a littleblack doton thatgearto make it easier to see:

To understand how this happens let’s first look at all the parts involved in the mechanism:

Thegreen gearis attached directly to the bottom of theweight, so when theweightrotates, thatgearturns thetwo bluegears on the underside of theyellow gears. Most of this composition is similar to things we’ve seen before with gears kept in place by bridges. However, you may have guessed that the doubled-up pairs ofyellowandbluegears are responsible for the magic here. Let’s see how they’re constructed:

Theblue gearcan rotate freely on theyellow gear, and the fish-likeleverscan also rotate around their axis through the holes in theblue gear. Notice that the inner part of theyellow gearhas a particular shape. In the demonstration below, I removed most of the central part of theblue gearso that you can see what’s going on inside. You can rotate thatgearback and forth using the slider to see how the parts interact:

Notice that when you rotate theblue gearcounterclockwise, theleversjust slide through the internals of theyellow gear. However, when you rotate theblue gearclockwise, one of theleversgets stuck and it starts to turn theyellow gearwith it. This clever mechanism transfers power from theblue gearto theyellow gearonly in one direction.

The autowinding assembly containstwosuch gears – one will drive theoutput gearwhen turned clockwise, and one that turns thatgearwhen turned counterclockwise. In the demonstration below, you can witness what happens when you rotate thegearattached to the weight. To make things easier to see I removed all of the non functional parts:

Notice that I’m highlighting a pair ofyellowandbluegears only when they’reactivelytransferring power directly from theweight gearto theoutput gear. Only one such pair is active at a time – the other either spins idly, or acts as an intermediate to change the direction of rotation to make sure theoutput gearalways winds the spring.

Notice that theoutput gearrotates very little relative to thegearattached to the weight, so it takes a lot of arm swinging to fully wind the mainspring. However, over the course of a day the automatic winding mechanism can usually ensure that the mainspring stays wound.

# The Size of it All

In all the examples so far we had the comfort of looking at the parts at a fairly large magnification, but in this last demonstration down below you can finally see how tiny all the components are. By dragging the slider you can change the viewing size:

That rounded rectangle surrounding the watch corresponds to the size of a credit card – if you have one handy you can put it on screen and drag the slider until the card fits in that outline. Hopefully, this really puts in perspective how small all the parts we’ve talked about are.

# Further Watching and Reading

There are many YouTube channels dedicated to mechanical watches, but I particularly likeWristwatch Revival, which is dedicated to fixing broken watches, which very often involves a complete dissection of a movement, and a repair or replacement of broken parts. Although the creator is not a professional watchmaker, the videos are packed with information and are very enjoyable to watch.

Watchmakingby George Daniels is a book dedicated to the process of actuallymakingwatches from scratch. While few will endeavor this journey, the publication also explains many of the considerations required when designing a watch movement and its parts. Many of the book’s pages are accompanied by pretty technical illustrations that help to explain the concepts.

# Final Words

In the 1970s mechanical watches started to be dethroned by quartz models, which track time by electronically counting vibrations of a quartz crystal. As technology progressed, typical watches only increased their reliance on digital circuits. Modern smart reincarnations resemble their archetypes only in shape and placement on wrists.

Mechanical watches are not as accurate as digital ones. They require maintenance and are more fragile. Despite all these drawbacks, these devices show atruemastery of engineering. With creative use of miniature gears, levers, and springs, a mechanical watch rises from its dormant components to become truly alive.