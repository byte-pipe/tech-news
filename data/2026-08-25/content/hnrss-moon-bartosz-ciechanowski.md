---
title: Moon – Bartosz Ciechanowski
url: https://ciechanow.ski/moon/
site_name: hnrss
content_file: hnrss-moon-bartosz-ciechanowski
fetched_at: '2026-08-25T11:25:17.417545'
original_url: https://ciechanow.ski/moon/
author: Bartosz Ciechanowski
date: '2026-08-24'
description: Moon (2024)
tags:
- hackernews
- hnrss
---

December 17, 2024

# Moon

In the vastness of empty space surrounding Earth, the Moon is our closest celestial neighbor.
Its face, periodically filled with light and devoured by darkness, has an ever-changing, but dependable presence in our skies.

In this article, we’ll learn about the Moon and its path around our planet, but to experience that journey first-hand, we have to enter the cosmos itself.

Let’s take a look at the Moon as seen from space in all its sunlit glory. You can drag it around to change your point of view, and you can also use the slider to control thedate and time:

In this convenient view, we can freely pan the camera around to see the Moon and its marvelous craters and mountains from various angles. Unfortunately, we don’t have that freedom of motion in our daily experience – the Moon wanders on its own path across the daily and nightly skies.

We can simulate these travels below, where you can see the current position of the Moon in the sky. You can drag that panorama around to adjust your viewing direction – this lets you see the breadth of the sky both above and below the horizon. By dragging the sliders you can witness how the position of the Moon changes in the sky acrossdaysandhoursof your local time. As the Moon’s placement in the sky shifts, the little arrow will guide you to its position.

You can also drag the littlefigurineon the globe in the bottom-right corner to see how the sky looks at that location on Earth. If your browser allows it,clickingtappingthebutton will automatically put thefigurineat your current location. This may all feel quite overwhelming at the moment, but we’ll eventually see how all these pieces fit together:

Over the course ofone day, the Moon travels on an arc in the skyalmostcompleting a loop around the Earth. As thedayspass, the Moon’s illumination also visibly changes.

You’ll probably admit that it’s a little hard to focus on the tiny Moon as it shifts its position in the sky. To make things easier to see, I’ll zoom in the camera and lock its position on the Moon:

Notice that across asingle daythe Moon seems to rotate, and overmany daysit quite visibly wobbles. These wobbly variations let us occasionally see some hidden parts on the “edges” of the Moon, but our neighbor ultimately shows us only one of its sides. In our space-floating demo we could easily see the Moon from all sides, but on Earth we can never see most of thefar sideof the Moon.

Over the course ofdays, the lighting on the Moon also changes dramatically. The line between the lit and unlit parts of the Moon, known as theterminator, sweeps across the Moon, revealing the details of its surface. Although the Moon has a spherical shape, the fully lit Moon looks more like a flat disk.

In this article I’ll explain all the effects we’ve just seen, and we’ll also learn about gravity, ocean tides, and eclipses. Let’s begin by exploring how celestial bodies move through space and how their mere presence influences the motion of their neighbors.

# Motion in Space

Let me introduce a little cosmic playground in which we’ll do our experiments. Inside it, I put a littleplanetthat floats freely in space. You can drag theplanetaround to change its position. The arrow symbolizes the initial velocity of thisbody– you can tweak this velocity by dragging thedashed outlineat the end of the arrow. To get things going, you can press thebutton in the bottom-left corner:

Notice that I’m drawing a ghost trail behind the movingplanet, making it easier to track its motion. As you can see, once you let theplanetgo, it travels through space in a straight line, only to eventually get out of visible bounds.

Let’s complicate things a little by addinganother bodyto this sandbox. You can tweak the positions and velocities ofbothbodiesto see how their mutual presence impacts one another. I’m also marking the thin lines of trajectories that the bodies will take evenbeforeyou let things go, making it easier to plan their motion:

The motion we see now isn’t as straightforward as before. Insome scenarios, thetwobodiestravel past each other after tweaking their initial trajectories. Inother configurations,bothobjectsroam through space together, permanently locked in a swinging dance.

You may have also managed to make thetwobodiesrun intoeach other. We’ll eventually see a more realistic visualization of that scenario, but in this simplified simulation when two objects collide, they just stick together and continue their coupled journey.

What’s responsible for all these effects is the force ofgravityacting on the objects. Let’s explore that interaction up close. As before, you can drag thetwobodiesaround, and you can also change their masses using the sliders below:

Thearrowsrepresent the force of gravity acting on thetwobodies– the longer the arrow, the larger theforce. For completeness, I’m displaying the values andunitsof masses and distances, but the numbers aren’t particularly important here. What matters is that when we increase either the mass of the first bodym1or the mass of the second bodym2, theforce of gravitygrows too.

Moreover, the magnitude ofgravityalso depends on the distancerbetween the objects. As bodies move farther apart, thegravityweakens. Notice how theforcesacting on each body have the same magnitude, but they point towards the other body, which indicates anattractiveforce.

If you paid close attention to the lengths of the arrows, you might have noticed that theforcedecreases quite rapidly withdistance. We can visualize this with a plot, in which thewhiteline shows the magnitude ofgravityas a function ofdistance. More precisely, it shows thatgravityis inversely proportional to thesquareof thatdistance:

Let’s take a very brief mathematical interlude to describe what we’ve seen in more detail. All these dependencies are captured in the following equation for theforceof gravityF, betweentwoobjectswith massesm1andm2separated by distancer:

F
 = 
G
 × 

m
1
 × 
m
2

/

r
2

Thegravitational constantGseen in front of the right-hand side of the equation is incredibly small, making gravity a very weak force. We have no issues lifting everyday objects despite the might of the mass of the entire Earth pulling them down.

While the strength of gravity between any two bodies is equal, the resulting change in motion is not. You may recall from elementary physics classes that forceFis equal to massmtimes accelerationa. We can encapsulate this idea in a pair of simple formulas that tie these values for thefirstandsecondbody:

F
 = 
m
1
 × 
a
1

F
 = 
m
2
 × 
a
2

By plugging in the equation for the force of gravityFand reducing the masses, we end up with a set of two equations foraccelerationsof the bodies:

a
1
 = 
G
 × 

m
2

/

r
2

a
2
 = 
G
 × 

m
1

/

r
2

Notice that the acceleration of the first bodya1depends on the mass of thesecondbodym2. Similarly, the acceleration of the second bodya2depends on the mass of the first bodym1. Let’s see this in practice in the demonstration below, where I’m temporarily making thebig bodytwentytimes more massive than thesmall body:

Notice that the body withsmaller massdrastically changes its course, while the motion of thelarger bodyis only marginally affected. This tracks with our day-to-day experience, where every item left hanging in the air very visibly accelerates towards the staggeringly massive Earth, but our planet doesn’t jump out of its way to meet the falling object.

Now that we understand that it’s the force of gravity that makes the bodies move towards each other, let’s do a better job of tracking the motions of these objects over time. Right now our camera is fixed in space, so thetwobodiesoften fly out of visible bounds. Thankfully, we can easily fix this by moving the camerawiththe bodies.

In the demonstration below, I’m presentingthe samescenario from two different vantage points. On the left, I’m showing the scene from the familiar point of view that’s fixed in space – you can plan the trajectories of thetwobodieson that side.

On the right, you can see this simulation from the point of view of the camera that’s tied to the motion of thetheseobjects. I’m marking the position of that camera with a white doton the thin line joining the bodies. By dragging the slider you canmove the camerabetween them:

With the camera following the bodies we can now track their motion forever. More importantly, we can also see therelativemotion of the two objects. When you make the bodiesmove together, you can witness how from theperspectiveof theteal body, it’s theyellow bodythat orbits around theteal body, but from theperspectiveof theyellow body, it’s the other way around.

Better yet, if we position the camerahalfway, or evenanywhere elsebetween thetwobodies,bothobjects seem to orbit the camera. The perception of relative motion depends on the point of view, but there is one point that’s particularly useful for observation. In this next demonstration, I’ve added a little white trail to the camera itself. Watch how the path of the camera in space changes as youreposition itwith the slider:

In general, the cameratraverses some squiggly path in space. However, there is onespecial positionbetween thetwobodiesfor which the camera travels in a perfectly straight line. This point is known as thebarycenter, and it’s located at thecenter of massoftheseobjects.

Let’s explore the concept of the barycenter a little closer. In the demonstration below, you can once again drag the bodies around to change the distance between them, and you can also use the sliders to tweak their masses. The center of mass of thesetwobodiesis marked with a black and whitesymbol:

The equation in the bottom part explains the placement of the center of massof these two objects – it is located at a point where its distance from the first bodyr1multiplied by that body’s massm1, equals that point’s distance from the second bodyr2multiplied by its massm2.

This simple rule becomes slightly more complicated when more than two bodies are involved. In those scenarios, the position of the center of mass is theweighted averageof the positions of all the bodies, where the masses of these bodies serve, very appropriately, as weights.

We’ll only be interested in the center of mass of two bodies, so the demonstration we’ve just seen fits our needs well. Notice that as the bodies move farther away, the barycenter also migrates to stay in the constant proportion of the distance separating the objects. Moreover, if one of the bodies is much more massive than the other, the center of mass could lie inside that larger body.

In our space simulator, the mass of theteal bodyis three times the mass of theyellow body, so the barycenterof this system lies three-quarters of the way between theyellowandtealobjects:

The motion of the barycentershows usthat the tangled dance of two celestial bodies hides a much simpler linear motion through spaceandsome additional motion of thetwobodiesaround that barycenter.

Let’s try to see that other motion more clearly by making one more modification to the right side of the demonstrations we’ve seen. Notice that the trails left by the bodies linger in space, but ideally, we’d also want to see the paths taken by the bodies relative to the moving camera.

To make this work we can attach a little drawing plane to the camera itself – I’m outlining that plane below with athin rectangle. Then, as the bodies move around, they can trace their trails on thatplaneas well:

With this new method we can see the paths the bodies tookrelativeto the moving camera. When seen from this perspective, we can finally reveal that, in most practical scenarios, the two orbiting bodies trace ellipses relative to each other.

Depending on the initial conditions, some of those ellipses arelarger, and some aresmaller. Some arealmost circular, and some arequite elongated. Changing theposition of the camerawith the slider changes the relative sizes of these two ellipses, but they maintain their overall proportions. The ellipse of motion of one body seen from the perspective of the other isthe sameforbothbodies, it just shifts in space.

As youmay have seenon this blog before, an ellipse can be more formally characterized by itseccentricityand the size of itssemi-major axis, which you can control using the sliders below:

Eccentricityspecifies how elongated an ellipse is. It can be defined as the ratio of the length of thedark pink segmentto the length of thesemi-major axis. Thatsegmentspans the distance between the center of the ellipse and one of the twofocus points, which are also jointly known asfoci. When we watch orbital motion from the perspective of theorbited body, thatbodyis always in one of thefocus pointsof the orbital ellipse of theorbiting body.

I’ve also marked two special points on the orbital ellipse. Atapoapsis, theorbiting bodyis at its farthest distance from theorbited body, and atperiapsistheorbiting bodyis closest to thatbody. These two points are collectively known asapsides, and the line joining them is known as theline of apsides. The simple rule for remembering which apsis is which is thatapoapsisis the one that’s fartherawayfrom theorbited body.

We’ve just described the orbital ellipse and its apsides as seen from the point of view of the larger body, but in our cosmic playground we’ve seen how moving the camera around with a slider can change the perception of motion:

With a two-body system like this one we actually have some flexibility in describing which body orbits which. We typically say that it’s theless massive objectthat orbits themore massive one, but the observer on thesmaller bodywouldjust seethe motion of thelarger neighboraround it.

For us, it will be often useful to describe things from thepoint of viewof the barycenter– we’ve seen earlier how that special point lets us decompose the motion of two solitary bodies into the movement on a straight line and the orbiting motion around that barycenter.

That particular viewpoint also lets us explain another irregular motion we can see in these elliptical orbits. Notice that as the two bodies are close to each other, they swing across their trajectories much faster.

You can see it best when looking at thedashed segmentsI’ve drawn on the elliptical orbits – traversal of each brighter or darker section takes the same amount of time. These lines are visibly longer when the bodies are close, which reflects their faster motion as they travel longer distance over the same period.

This non-uniform motion can also be seen in the angular velocity of the orbital motion, which describes how many degrees per second an orbiting body sweeps through. In this next demonstration theblue linerotates with constant angular velocity, so in every second it goes across the same number of degrees. As you can see, theorange linejoining two bodies rotates with varying speed:

Notice how theorange lineis sometimes ahead of and sometimes behind theblue line, which shows that the orbital motion doesn’t have a constant angular velocity.

This unusual behavior is more easily explained with the following contraption, where I put thetwobodieson agiant barthat spins around on an axis placed right at the center of massof the two bodies. Using the slider you can change thedistancebetween these objects:

As the bodiesget closer, the rotation speeds up. Conversely, as the bodies movefarther apart, the rotation slows down. You can easily recreate a version of this experiment by holding heavy items in your hands and spinning on a desk chair with your arms spread out. As you pull them towards your torso, your rotation will speed up.

These are examples ofconservation of angular momentumin which the speed of revolution and the mass distribution of a system are inherently tied together. Broadly speaking, when we double the distance from the axis of rotation, the angular velocity becomesfourtimes smaller.

The space playgrounds we’ve looked at earlier work just like the demonstration with the bar, but instead of a slider, it’s the force of gravity that determines the distance between the bodies. Gravity pulls the objects closer together, increasing the speeds at which they swing by each other. As the bodies move past their closest distance, that increased speed shoots them out away from each other and the cycle continues.

The details on how this action creates elliptical paths are beautifully covered inthe video on Feynman’s Lost Lecture, but for our needs it will be enough to just witness once more how all the initial values of masses, positions, and velocities of thetwobodiesdecide everything about their motion:

With a firmer grasp on orbital motion in space, we can finally see how everything we’ve learned affects movement of our planet and its closest celestial neighbor.

# Moon and Earth

Let’s first look at the Moon and Earth side by side to compare their masses and sizes inimperial unitsmetric units:

Moon
Earth

mass
0.01619
0.07346
1.317
5.972
× 10
25
 lb
24
 kg

mean radius
1079.6
1737.4
3958.8
6371.0
mi
km

volume
0.5270
2.1968
25.9876
108.321
× 10
10
 
mi
km
3

mean density
208.8
3344
344.2
5513
lb/ft
3
kg/m
3

The Earth’s mean radius is only around 3.67 times larger than that of the Moon. Since the volume of a sphere grows with the third power of its radius, and the Earth is on average much denser, our planet’s mass ends up being around 81.3 times larger than the Moon’s.

Let’s try to replicate this table in our space simulator, where I addedtwobodieswith sizes and masses matching those of theEarthand theMoon. Let’s see how these values affect the motion of the two objects:

With oursimulated Earthbeing so massive, we can quite easily make thisMoonorbit theEarthwith various ellipses. Unfortunately, while this simulation correctly mimics the relative sizes of the real Earth and Moon, it doesn’t reflect the cosmic scale of the distance between these two bodies.

Let’s see how far away the Moon really is. In the demonstration below, you can use the slider tozoom awayfrom the Earth until the Moon’s position becomes visible:

If you drag the slider all the wayto the right, you’ll notice that I’m actually markingthreedistances between the centers of the Earth and the Moon. The orbit of the Moon doesn’t form a perfect circle, so the separating distance varies as the Moon gets closest to the Earth at periapsis, and farthest away at apoapsis. The values shown here inmileskilometersare the predictedmaximum,mean, andminimumof that distance in the 21stcentury.

Let’s see the orbit of the Moon in more detail. The following demonstration shows the motion of our neighbor from the perspective of the Earth itself. You can drag around the following demonstration to change the viewing angle. The slider lets you control thespeed of time:

With all the sizes and distances replicated realistically, it may be hard to see these tiny bodies. To make things more legible, you can press thebutton in the bottom right corner to toggle between the real andtentimes larger artificial sizing of these bodies.

With this three dimensional view we can now see that the Moon’s motion lies in theorbital planethat I’m marking with afaint gray disc. To help us orient ourselves in space, I’ve also added alinethat marks a fixed reference direction pointing at some very distant stars.

On average, it takes the Moon27.322 days27 days, 7 hours, and 44 minutesto complete the whole orbit, as measured by crossings of thereference line. That period is known as thesidereal month, wheresiderealmeans “with respect to stars”. This is only one of the four different types oflunar monthsthat we’ll explore in this article.

As the Moon orbits the Earth, it traces the familiar elliptical shape. We can quite clearly see how the elliptical eccentricity shifts the Moon’s path relative to the perfect circle of the visualization of theorbital planethat I’ve drawn above.

Let’s take a closer look at some of the parameters of the Moon’s orbit. In this next demonstration I’m using the current position and velocity of the Moon to calculate an ellipse that best describes the Moon’s orbit atthatmoment of time. I’m drawing this ellipse with adashed line, while thesolid trailshows the actual path the Moon took:

Since we’re making theellipsefit the current orbital motion, thisidealized ellipsematches theactual trailvery well in the vicinity of the orbiting Moon. However, farther away from the Moon this best-fittingellipsedivergesfrom thepaththe Moon actually took. This shows us that while it’s pretty close, the Moon’s trajectory doesn’t form a perfect ellipse.

As we see in the labels, both eccentricity and the length of the semi-major axis of this “currently best-fitting” ellipse vary over time. Measured over a long period, the eccentricity of the Moon’s orbit has the average value of 0.0549, while the semi-major axis has the average length of239,071 mi384,748 km.

Moreover, the fitted orbitalellipsenot only changes its shape, but also its orientation. Theline of apsidesof the ellipse which joins theapoapsisand theperiapsiswobbles over time in a quite chaotic manner.

These effects happen because the Earth and the Moon aren’t the sole bodies in space – they’re both part of the Solar System. True to its name, the Solar System is dominated by the Sun itself, and it’s primarily the effects of the Sun’s gravity that cause all theseperturbationsof the Moon’s orbit.

We’ll soon explore the influence of the Sun in more detail, but for now let’s focus on the changes of the positions ofapoapsisandperiapsis. In the demonstration below, I’ve made time flow even faster than before. Additionally, every time the Moon is at its closest to the Earth, that is when it’s at theperiapsis, I’m leaving a littlemarkeron the orbital plane:

Notice how theline of apsideswobbles back and forth, but across many months it overall makes steady progress rotating, whenseen from above, in the counter-clockwise direction. Averaged over long time, thisline of apsidesmakes a full rotation in8.85 years8 years and 310 days, which defines the period of the Moon’sapsidal precession.

Themarkersthat I drop when the Moon crosses theperiapsismeasure theanomalistic month. Notice that the lengths of anomalistic months vary a lot as they happen on different parts of the orbit. Sometimes it takes the Moon less than 25 days to get closest to the Earth again, but sometimes it takes it over 28 days to reachperiapsisagain. Over long time the anomalistic month has ameanlength of27.554 days27 days, 13 hours, and 3 minutes.

This period is a bit longer than the27.322 days27 days, 7 hours, and 44 minutesof the sidereal month, which is tracked by the crossings of thereference line. When averaged over time, theline of apsidesrotates steadily in the same direction as the Moon’s orbital motion, so it takes the Moon a bit more time to catch up toperiapsis.

All the demonstrations we’ve seen also show one more effect that we didn’t account for in our simple playground simulations – both the Earth and the Moon spin around their axes. You can see this more clearly in the demonstration below where I glued ablue arrowto the surface of the Earth, and agray arrowto the surface of the Moon:

When viewedfrom the side, we can see that the axes of rotations of these two bodies aren’t neatly perpendicular to theorbital plane, and they also spin at very different rates. Our planet takes roughly23.93 hours23 hours and 56 minutesoralmostone day to complete a full revolution and point towards thereference directionagain. The Moon rotates much slower, taking27.322 days27 days, 7 hours, and 44 minutesto revolve just once and align withthat directionagain.

From abovewe can see that thegray arrowfixed to the Moon’s surface generally points towards the Earth, as indicated by the thin line joining the two bodies. If you pay close attention, you’ll notice that thisarrowis sometimes pointing a bit ahead of that direction and sometimes a bit behind that direction.

This is a consequence of the Moon’s non-circular orbit – we’ve seen earlier how the angular velocity of an orbiting body changes as it sweeps through its orbital ellipse. The Moon rotates around its axis with more or less constant speed, but the Moon’s angular position relative to the Earth doesn’t advance at a constant rate. As a result, the two rotating motions don’t always perfectly cancel each other out.

In a close-up view of the bodies you might have also noticed that the rotation axis of the Moon is tilted relative to itsorbital plane. Similarly, the axis of rotation of our planet is also tilted relative to thatplane. Let’s briefly switch our point of view to align ourselves straight-up with the Earth’s rotation axis:

From this perspective we can see that the Moon’sorbital planeisinclinedto our planet. Notice how the Moon’s position relative to the Earth changes during its orbital motion – it is sometimes “above” and sometimes “below” our planet, revealing the truly three dimensional aspects of the Moon’s motion.

All the orbital observations we’ve made will help to explain some of the effects we’ve seen at the beginning of this article, where we looked at the Moon through the eyes of an observer on the ground. Before we investigate these effects, we need to build a bit more intuition on how objects in space look to someone viewing them from the surface of Earth.

# Eyes on the Heavens

Let’s first place ourselves on Earth and look at the sky in which I artificially put threecolorfulcelestialbodies. You can drag the demonstration around to change which part of the sky you’re looking at. If you lose track of these bodies, the little arrows will guide you back to their area of the sky:

Although the markers of the compass directions are of some help, it may be quite hard to grasp how this view from the Earth’s surface corresponds to the more external view from space we’ve gotten used to.

Let me clarify things in the next demonstration, where the left side shows the same view we’ve just seen, and the right side shows the same scene, butas seen from space. I’ve also outlined the sky view on the left withthefourcoloredlines– as you pan around the landscape on the left, you can see that square outline reflected on the right. I’ve also added afigurinethat represents avastlyenlarged observer standing on the ground. Thefigurine’sbody and itsrighthand always point in the current direction of observation:

With that external view, we can see how the observer on the ground can’t see the sky ineverypossible direction. Half of it is obscured by the Earth itself, with the horizon clipping the whole breadth of the surrounding sky to only the visible hemisphere.

Moreover, notice how the actual size of an object doesn’t match its size seen in the Earthly observer’s sky. For example, bothyellowandtealbodies are of the samephysicalsize, but thelatterlooks smaller in the sky. Similarly, thepinkbody is physically larger than theyellowone, but they share similar size from the observer’s point of view.

We can understand these sizing effects with the help of cones that shoot out from the position of the observer towards the bodies in space. Note that these cones start on the ground here, because the actual observer is much smaller than the gigantic illustrativefigurine.

The size of the intersection of those cones with the hemisphere of the sky, or the size of theprojected area, determines thevisiblesize. Intuitively, the farther away the object, the smaller it appears. If the projection occupies a larger fraction of the total hemisphere, the object will look larger as well.

We can conveniently describe the size of objects in the sky by measuring theanglespanned by the visible cone. In the demonstration below, I’m showing a flat side view of thiscone. You can drag theyellow bodyaround to change its distance from theobserver. You can also use the slider to change the size of thatbody:

The closer the object is to theobserver, or the larger the body, the greater theangleof the visible cone. Thatangleis known as theangular diameterorangular sizeof the observed object.

Having experienced how objects in the night sky may look at a fixed moment in time, let’s see how the Earth’s rotation affects observations done from the ground. In the demonstration below, you canscrub through timewith the slider to witness the effects of the spin of our planet:

This scene may seem a bit contrived, becausethethreeobjectsare just magically floating in space at fixed positions. Fortunately, it’s a decent representation of how all the stars in the night sky appear to Earthly observers – they’re distant enough that over the course of a day they essentially don’t move relative to the Earth’s center. As our planet spins,thesethreeobjectsseem to rise over the horizon, travel across the visible sky, and then set below the horizon again.

You’ll probably agree that it’s a little annoying to have to manually keep panning through the night sky to look at these objects, so on the left side of this next demonstration I’m automatically adjusting the viewing angle to track thetealbody. On the right side, I’m locking the camera on thefigurineitself. Don’t be misled by what you see here – the Earth is still rotating around its axis, the camera just rotates with it:

As seen through the observer’s eyes on the left side, theotherobjectsnow seem to rotate around thetealone, but this is purely a consequence of theobserverturning on the ground to keep facing thetealbody.

You may have experienced something similar when watching an airplane flying over your head. As the plane is approaching, its front is closer to you and its tail is in the back, but after the plane has passed over, you see the plane’s tail as being closer to you, and its front is more distant. In your eyes the plane has rotated, but in fact the plane has kept its course the entire time, and it wasyouwho turned to keep an eye on it.

When these celestial bodies disappear beneath the horizon, it becomes impossible to track them, but thankfully in these computer simulations I can make the Earth transparent, giving us an unobstructed view of the full sphere of the surrounding space:

With this approach we can now see the entire trajectory ofthethreeobjectsas an observer on Earth sees them. Because these objects don’t move relative to the center of our planet, they travel on closed paths, returning to where they came from after the Earth completes one revolution around its axis over the course of23.93 hours23 hours and 56 minutes.

Let’s bring back the Moon into the picture. In the simulation below, we can see the Moon in the starry sky as seen from the surface of the Earth. Note that I removed all the visual effects related to sunlight, including the daytime blue sky and any illumination changes on the surface of the Moon itself.

We’ll bring in those effects later on, but for now we’ll just look at theartificiallylit Moon over the course of the next 24 hours – you canscrub through this timewith the slider. You can now also drag the littlefigurinearound the globe to change the observer’s location, orclicktapthe buttonin the corner to jump to your location:

Notice how small the Moon actually is in the sky – it only spans around 0.5° of the viewing angle. Just like our colorful objects did, the Moon also travels across the sky as the Earth rotates. However, because the Moonmovesrelative to the center of our planet, it doesn’t quite close up its path. This is easily observable from space:

Notice that over the course of 24 hours the Moon moves ahead on its orbit, so a bit more time has to pass for the Earth to rotate to have our neighbor be over roughly the same spot on the Earth again. Moreover, the inclinedorbital planeshifts the Moon to be a little lower or higher relative to the Earth, so its arc in the sky shifts too.

Let’s go back to observing the Moon from Earth. To see our neighbor more clearly I’ll increase the zoom level of the camera, and I’ll lock it on the Moon:

When viewed this way, the Moon seems to rotate over the course of one day, but this effect is purely a consequence of theobserverturning around to face the Moon – we’ve already seen this behavior with colorful objects seemingly rotating in space.

The observer stands up vertically on the ground, so as the Earth rotates, theobserver’s“up” and “towards the Moon” directions change in space. How much these directions change depends on thelatitudeof theobserver’slocation. When seen from theequator, the Moon “rotates” quite rapidly as it passes over theobserver’shead. On theNorthandSouthPoles, the “up” direction is fixed in space, which removes that daily rotation. Notice that even on the poles the Moon still visibly turns a little over the course of a day.

To investigate these subtler aspects of the Moon’s motion in the sky we have to give ourselves a bit more time for observations. In the demonstration below, you can track the Moon over the next 30 days. You can still drag thefigurineto some other location, but the observer’s Moon-facing rotation can make things pretty nauseating outside of the poles, so you can alwaysget backto that stationary location:

Notice that over the course of a month the Moon wobbles visibly, and it also changes its size. The oscillations we see here are caused by the Moon’s orbital motion.

Let’s see this more clearly from space by drawing the cone of visibility of the Moon for the observer on the surface of the Earth. Unlike in previous examples, where I’ve aligned the rotation of the camera to thereference line, this time I’ve synchronized our perspective with the orbital motion of the Moon, giving us an unchanging perspective on that body:

As we’ve discussed earlier, the Moon’s orbit around the Earth isn’t perfectly circular. The Moon changes its distance to our planet, which affects how large it looks in the sky. Below you can see a side-by-side comparison of the Moon’s visible size when it’s atapoapsisandperiapsis:

The Moon’s orbital motion is also responsible for the periodic wobbles, which we can see clearly by once more gluing an arrow to its surface:

We can seefrom abovethat the Moon appears to wobble from side to side, because the angular speed with which it sweeps the orbit varies over time, while its angular speed with which it rotates around its axis is almost constant. Similarly, in aside viewwe can see that the axis of rotation of the Moon is tilted relative to its orbital plane, so we sometimes see more of the Moon’s top, and sometimes more of its bottom.

All the effects we’ve seen here are known aslibrations. Over the course of many days, librations make it possible to see around 59% of the Moon’s surface. However, because of the Moon’s synchronized spin and orbital motion, a large part of the Moon’s surface is never visible from Earth. It’s finally time to investigate how the Moon got locked into that motion by taking a more detailed look at gravity and the structure of celestial bodies.

# Gravity at Scale

So far we’ve only been experimenting with gravitational interactions between two objects, but it’s time we vastly increased the number of participating entities. In the demonstration below, I randomly distributed over1200 bodies– they all gravitationally attract each other:

We’re watching this scene from afar, so the individualbodieswe see here are very big – each on the order of dozens ofmileskilometersacross. Initially, theseobjectsmove very slowly, but the mutual gravitational forces consistently accelerate them towards each other, increasing their speed and kinetic energy.

This simple simulation doesn’t reflect this, but once thesebodiescollide, this energy gets released by heating up the matter constituting theobjects. When hot enough, the matter loses its solid form and starts to behave more like a fluid that can relatively easily change its shape. The pushing pressure from the surrounding neighbors and the heat from the decay of radioactive isotopes also help to maintain that liquid form.

When in this state, this mass of matter can’t really maintain any rigid shape, and after wobbling for a while, it reaches an equilibrium forming a sphere. When no other forces are involved, this liquid spherical shape balances itself perfectly – any mountain that stands out gets gravitationally pulled towards the center, and any valley gets squeezed out by the surrounding matter trying to fill the empty space.

In the simulation we’ve just seen, all thebodiesstarted frozen in space. Let’s see what happens when we give theseobjectssome initial random velocity:

After a while we end up with the similar spherical shape, but this time this blob rotates. What we’re witnessing here is another example of the conservation of angular momentum in action.

From our previous examples you may associate angular momentum with some kind of spinning or orbital motion, but even the simplest movement on a straight line contains a rotational component when seen from an appropriate point. Below you’ll find a replica of the very first space simulation we’ve played with in this article, but this time I’m also drawing an additionaldashed linespanned between theyellow planetand the centralblue point:

Thatdashed lineturns as thebodymoves in a straight line, revealing the rotational motion relative to theblue point. Even in this scenario the angular momentum of the system is maintained.

Through all the collisions in our complex system the velocity and the angular momentum of each of the hundreds of bodies constantly change, but, relative to some fixed point, thesumof the angular momenta of all the bodies remains constant. Whatever original value of angular momentum this system had, persists forever.

In the initially chaotic motion of all the bodies there is some average amount of rotational motion. Once all these bodies get closer to each other, the angular velocity grows high enough to be visible. This is the exact equivalent of two planets orbiting each other more quickly as the distance between them decreases, but it happens here at much larger scale.

There is one more aspect of these self-aggregating blobs that we should explore. In this next demonstration, one fourth of the objects iscolored blue. Thesebodiesare much denser than theothers, therefore, each is also more massive:

Notice that in the final liquefied planet thesedenser objectshave a tendency to aggregate at the center of the body. We’re basically observingbuoyancyin action, where thisdenser materialsinks to the “bottom” of the planetary blob and thelighter onefloats to the surface.

These accumulation, oraccretionprocesses that I’ve crudely simulated with a small number of bodies, happened on an absolutely massive scale during the formation of Earth and other planets. The wholefascinating historyof the early Solar System is beyond the scope of our discussions, but the simple simulations we’ve seen highlight the origins of the Earth’s rotation, and illustrate why it’sdifferentiatedwith a heavy iron core in the middle.

A few different theories have been suggested to explain the origin of the Moon itself. These days the leading one is thegiant impact hypothesis, in which a large body hit the early Earth around 4.5 billion years ago.

Scientific opinions differ not only on the size, speed, and composition of the impacting body, but also on the subsequent process of formation of the Moon from the resulting debris.

Someearlier papersassume the Moon simply formed from the matter scattered into space after the collision. Other authorssuggestthat the energy released during impact created a huge, partially vaporized cloud of matter from which small moonlets condensed and accreted to create the Moon. Some otherrecent researchshows withbeautiful computer simulationsthat the proto-Moon may have formed immediately after the impact.

Any theory of the Moon’s origin has to end up with a similar state as the Earth and the Moon are in right now. For example, if we estimate that during the collision only a small amount of matter got ejected out of reach of the Moon’s and Earth’s gravity, the total mass of the two bodies before and after the impact should be more or less the same.

Moreover, the Moon is on average much less dense than Earth, because the Moon’s iron core is comparativelymuch smallerthan that of Earth’s. If we assume that the colliding body and proto-Earth formed in the same area of the Solar System and therefore had similar composition, then this implies that a large part of the impacting object’s iron core must have transferred to our planet.

The Moon and Earth also share very similar ratios of isotopes of some elements, suggesting that the ejected material that formed the Moon was a mix of the proto-Earth and the other proto-planet.

Let’s try to recreate some simple collision scenarios using our rudimentary simulations. In the demonstration below, you can drag the impacting body around and change its initial velocity, similarly to how we did this in the introductory orbital simulations:

We don’t know what the initial conditions of this collision actually were, but when everything finally settled, we most likely ended up with the Moon orbiting Earth and both bodies spinning around their axes.

The simulation below gives a rough overview of this situation. Note that it doesn’t try to accurately reflect the distances, speeds, or surface details involved in those early stages, but it will be enough to help us explore the other details of gravitational effects between theEarthand theMoon:

Let’s try to first understand what forces the Earth imposed on this early Moon when we incorporate the more fine-grained scale of gravitational interactions we’ve been playing with. In the demonstration below, I putthreesmallbodiesfar away from theEarth. Initially,thesethreeobjectsare evenly spaced, but notice what happens to the distances between them over time:

Thedashedcirclesshow the original positions of thepinkandtealobjects relative to the centralyellowbody. Quite clearly, the three bodies seem to drift apart.

Recall that the force of gravity is proportional to the inverse of the square of distance between the objects. When an object is close to itsmassive neighbor, it’s also close to each tiny parcel of matter that makes up thatneighbor. We can visualize this with a plot and arrows that show the Earth’sgravitational forcesacting on theseequallyspacedobjectsplaced at a varying offset – you can control it with the slider below:

Thepink bodyis closest toEarth, so it experiences the strongestforceand the strongest acceleration. Conversely, theteal bodyis the most distant, so it feels the weakestforceand it doesn’t increase its velocity as fast as thecloserbodies. It’s thisvariationinforcesthat increased the distance separating the objects in the previous simulation.

Even thoughallthreebodieswere moving towards the planet, from the perspective of thecentral bodyboth its neighbors movedawayfrom it. It’s easiest to understand this effect by calculating thedifferencebetween theforcesacting on thatcentral bodyand its neighbors. I’m drawing these force differences withyellow arrowsthat have been scaled up to be more legible:

Theseyellow arrowsshow actual forces on thepinkandtealbodyrelativeto theyellow body. As seen by theyellow body, itstwoneighborsare pulled away by these so-calledtidal forces, which arise from differences in gravity experienced by the bodies.

Our early Moon isn’t immune to these effects either. Because of its orbital motion it doesn’t crash into our planet, but its parts closest to the Earth feel a stronger pull than the Moon’s central sections. Those central parts are in turn pulled more forcefully than the Moon’s parts most distant from the Earth. We can visualize these forces by putting thegravity arrowson small sections of the Moon:

If we then calculate the difference between theforceacting on each of those small sections and theforceacting on the center of mass of the Moon, we can visualize thetidal forcesacting on the Moon itself. For clarity, I’m drawing the arrows much larger than the gravity differences actually are:

As you can see, thetidal forcesare trying to flatten and stretch the Moon both towards and away from the Earth. Thankfully, the self-gravity of the Moon is strong enough and the Moon isfar away enoughthat these differences in the Earth’s gravity don’t pull the Moon’s body apart. However, the Moon does stretch a little, forming an elongated shape.

In the demonstration below, you can visualize thisstretchingwith the second slider, but be aware that the distortion you’re playing with here isvastlyexaggerated:

As this early Moon keeps spinning around its axis, its different parts get closer and farther away from the proto-Earth. The elongation travels across the Moon’s surface, continuously morphing its shape. As you can imagine, it takes a lot of energy to deform a celestial body, and some of this energy inevitably gets lost due to friction.

These losses introduce a delay to the entire deformation process, and the maximum elongation is reached a littleafterthat area of the Moon has been closest to the Earth. As a result, the elongated bulge doesn’t point directlyatthe Earth, but it’s carried ahead by the spin of the Moon – the elongated shape is a bitoff-axis. In the demonstration below, you can play with an overemphasized degree of thisdelay:

Let’s pause here for a minute to understand what effect thetidal forcesmay have on this stretched and skewed body. In the demonstration below, I’m drawing along barthat gets pulled bytwo ropesattached to its ends. Using the slider you can scrub through time to see how this contraption would behave when pulled by theseforces:

Notice that initially thebaris rotated, so it’s a little off-axis with the directions of thepulling forces. This gives theropessome leverage, and thepulling forcesrotate the entirebarclockwise until it’s alignedwiththoseforces.

This is very similar to what happens to our spinning early Moon deformed bytidal forces. Since the elongation is slightly off-axis, thetidal forcesrotate the Moon clockwise, which gently decreases the Moon’s existing counterclockwise spin!

The actual elongation and the off-axis skew of the early Moon were much smaller than what I’ve depicted here, and its non-circular orbit complicated things even more, but the net result oftidal forceswas to slow down the Moon’s spin until it was synchronized with the Moon’s average orbital motion.

In this whole process the angular momentum of the Moon had to be conserved, so as the Moon’s spinning motion slowed down, its distance from the Earth increased. This kept the overall balance of how quickly all the matter rotated and how far from the center of rotation it all was.

In the last few paragraphs we’ve only focused on the effects of Earth’s gravity on the Moon, but everything we’ve discussed also manifests in the influence of the Moon’s gravity on Earth. The Moon also creates a slightly elongating bulge on Earth thattravels acrossour planet as Earth rotates.

Earth also used to rotate faster, but tidal forces slowed down its rotation, transferring some of the angular momentum from the rotational motion to the joint orbital motion. This has also increased the distance between the two bodies.

Even today, Earth is very gently slowing its rotation, with the average day getting longer by about 2 milliseconds per century. As a result, the Moon is also moving away from our planet at the rate of around1.5 inches3.8 centimetersper year. Part of the present-day energy dissipation is caused by the deformation of Earth itself, but most of the energy gets lost in the oceans in the form oftides.

The forces driving the ocean tides have the very same nature as the ones we’ve just discussed. To understand how they work, let’s look at afictional planetcompletely covered with a deep layer of water and orbited by asmaller neighbor. Thewhite arrowssymbolize theneighbor’sgravity forces acting on the water at that location. The slider lets you control thespeed of time:

Water closer to theorange bodyexperiences a stronger pull than the water farther away. The solid part of the water-coveredplanetalso gets gravitationally pulled by theneighborwith some force. Like before, we can calculate the difference between theforceacting on each parcel of water and theforceacting on the center of the solid body, which will show us thetidal forcesacting on the water:

Subject to thesetidal forcesthe surface of the water will deform until it reaches a new balance with the gravitational forces of theplanetitself. It’s actually pretty hard fortidal forcesto just raise the water against the force of gravity of theplanet. The tidal deformation is primarily caused by “sliding” the water away from the regions where thetidal forcesact tangentially to the surface.

Here we’ll make an idealized assumption that, on thisplanet, water can very quickly travel and deform under the influence of gravity. It’s not super realistic, but this simplification will help illustrate some fundamentals of tidal motions. The demonstration below shows an exaggerated view of that tidally deformed ocean. I’ve also added a littlefigurinethat you can drag around to more easily see the water level at that location:

The plot below shows the water level over time at theobserver’slocation. As theplanetspins, different areas of the ocean are directly in line with theorbiting body, so the water level oscillates over time. Notice that the tidal forces createtwobulges, so during a single rotation of the planet theobserverexperiences twohigh tidesand twolow tides.

In this perfectly aligned system thesmaller planetorbits thebigger oneright around the equator and that’s where the water bulges have theirhighest amplitude, creating the largest difference between low and high tides. As you drag theobserverto the regionwherethe bulges aren’t as pronounced, the tides become weaker.

Let’s disturb this equatorial symmetry by making the orbit of thesmall bodyinclined relative to thebig planet:

Notice that we still experience two bulges, but they no longer happen at the same latitude. In most areas the two high and low tides are no longer even, because theobservermay be closer or farther away from the nearby bulge. This creates some additional once-per-day variation on top of the regular twice-per-day oscillation. Moreover, thebody’smotion on the inclined orbit now also moves the bulges up and down the globe, adding once-per-month variation to these tidal amplitudes.

Any additional body present in the system would also exert its tidal forces, creating another pair of bulges. As the relative positions of these bodies change, their bulges could line up to create tides of greater amplitude. These bulges could also be shifted relative to each other with a low tide caused by one body partially cancelling out the high tide from the other.

What we’ve explored here is only a simplified model of what would happen on a planet fully covered with water. For example, we didn’t account for tidal deformation of the crust itself, or any latency in the water displacement caused by energy dissipation. However, the underlying principles roughly match the system that drives the tidal forces on Earth. The Moon, and to a lesser extent the Sun, bothimposetidal forces on the bodies of water on Earth.

How the water on Earthreactsto these forces is very heavily influenced by geography of the land itself. The size and placement of the continents and islands, the shape of coastlines, gulfs, bays, and straits, the depth of the sea floor, they all significantly affect the actual amplitude and frequencies of tides observed at any given location.

Insome areasof the world the mean difference between a high and low tide can reach over38 feet11 meters, but insome seasthe tides can be barely perceptible. Aglobal viewon the tidal motions reveals complicated patterns that clearly don’t neatly fall into the simple bulge model, but the local changes in tide levels can still be broken down into cycles that follow the relative motions of the Moon, the Earth, and the Sun.

We’ve already seen some other glimpses of the influence of the Sun, like how it affected the Moon’s orbit by changing its eccentricity and semi-major axis. To understand the full impact of the Sun on the Moon’s trajectory we have to finally properly introduce our home star.

# Moon, Earth, and Sun

Let’s put the three celestial bodies side by side to compare their statistics inimperial unitsmetric units:

Moon
Earth
Sun

mass
0.01619
0.07346
1.317
5.972
438,470
1,988,500
× 
25
 lb
24
 kg

mean radius
1079.6
1737.4
3958.8
6371.0
432,300
695,700
mi
km

volume
0.5270
2.1968
25.9876
108.321
33,810,247
140,927,257
× 10
10
 
mi
km
3

mean density
208.8
3344
344.2
5513
87.9
1408
lb/ft
3
kg/m
3

With a mass that’s 332,950 times larger than that of the Earth, the Sun completely dwarfs the other two bodies. Even though the Sun has much lower density, its radius is still over 109 times larger than our planet’s.

At normal zoom scale, you may barely be able to see the speck of the Earth, and the Moon will most likely be almost completely invisible. To remedy this, you can use the slider tozoom inon all three bodies letting you witness how absolutely massive the Sun is.

The distance to the Sun is even more staggering. In the demonstration below, you canzoom awayfrom the Earth-Moon system until our star is seen:

The seemingly largedistancebetween the Earth and the Moon almost completely disappears when put in this perspective, and the smallness of those two bodies makes them vanish into the darkness. The values shown here inmileskilometersare themaximum,mean, andminimumdistance between the Sun and the barycenterof the Earth-Moon system in the 21stcentury.

While the distances and sizes we’ve just seen are correct, the positions and motions of the Earth and the Moon relative to the Sun are a little more involved. In the demonstration below, you can see a three dimensional simulation of the Earth and the Moon on their joint path around the Sun. You can drag it around to change the viewing angle, use the first slider tozoom inon these bodies, or tweak thespeed of timewith the second slider:

With these three bodies involved, we can no longer describe the entirety of the motion of the Earth and the Moon in a simple, two dimensional manner. Let’s dissect what’s going on by first focusing on the path of the Earth-Moon barycenteraround the Sun:

From atop down view, we can clearly see the familiar elliptical shape. When observedfrom the sidewe see that the motion of the barycenter lies in a flat plane, which I’m highlighting withblue color. This plane is known as theecliptic.

Traditionally, theecliptichas been defined as the plane of motion of the Earth around the Sun, but themodern definitionis based on the average motion of thebarycenterof the Earth-Moon system. If youzoom inon the barycenterup close, you can see how the Moon and, to amuchlesser extent, the Earth, bob up and down through thisplaneas they orbit around the Sun. In some sensebothbodies orbit the Sun, and the Moon also orbits the Earth at the same time.

With the Sun present, the barycenterno longer travels on a straight line like it did in our simple two-body space simulations. In general, the gravitational motion ofthree bodiescan get very chaotic, but, luckily for us, the Moon and the Earth have settled into a balanced and predictable system.

The Earth-Moon barycenteris located inside the body of our planet, so the barycenter’s motion around the Sun very closely matches the familiar yearly motion that we experience on Earth. You can read more about the Earth’s journey in myearlier article, but for our needs here it will be enough to assume that it takes the Earth-Moon system roughly one year to orbit the Sun.

Let’s take a closer look at the motions of the Earth and the Moon around their barycenter. We’ve already discussed how the motion of the Moon around the Earth forms the Moon’sorbital plane– I’m marking it with afaint gray discin the demonstration below:

Theorbital planeof the Moon doesn’t lie flat in theecliptic, but it is instead inclined to it at anangle. Thisinclination anglevaries a bit over time, reaching an average value of 5.145°.

Theinclination anglelets us specify one aspect of the orientation of the Moon’sorbital plane, but there is also another angle we need to consider. Notice that the intersection of the inclinedorbital planewith theeclipticforms a straight line called theline of nodes:

Thislinegets crossed by the Moon in two places: on its waybelowandabovetheecliptic. Thesetwopointsare known asorbital nodes. Thered pointis thedescending nodebecause the Moon submerges, ordescendsunder theecliptic. Similarly, thegreen pointis theascending nodebecause the Moon rises, orascendsabove theecliptic.

To orient theline of nodesin space, we have to bring in ourreference direction. Theanglebetween thatreference directionand theascending nodedirection of theline of nodesis known as thelongitude of the ascending node:

Even when running this simulation200,000 times fasterthan real life, thelongitude of the ascending nodeseems to fluctuate only a little, keeping theline of nodesrelatively stable in space. However, when we speed things up even more, we begin to notice some predictable movement:

Theline of nodesconsistently rotates over time, which we can see reflected in the angle very slowly looping through all 360 degrees. This effect is known asnodal precessionand it is primarily caused by the gravitational force of the Sun disturbing the Moon’s path.

Whenseen from above, theorbital planeof the Moon rotates clockwise, which is theoppositedirection of the Moon’s orbit around the Earth. It takes around18.61 years18 years and 223 daysfor theorbital planeto complete one rotation.

The period between passages of the Moon through theascending nodeis known as thedraconic month. Because of the nodal precession, it takes the Moon a little less time to get back to theascending nodethan it takes it to cross thereference line, so a draconic month averages at27.212 days27 days, 5 hours, and 5 minutes.

The nodal precession has two other consequences for the relative motion of the Earth and the Moon, but to see them, we first have to visualize the spinning motion of these two bodies in more detail. Below I’ve markedtwoanglesbetween the axes of rotation of theEarthand theMoon, and the direction perpendicular to theecliptic plane. This measures theaxial tiltof these bodies relative to theecliptic:

The Earth’saxis of rotationholds steadily in space, with the current value of itsaxial tiltat around 23.44°. Right now this value very gently decreases at the rate of roughly 0.013° per century.

On the other hand, the Moon’saxis of rotationis almost exactly perpendicular to theecliptic plane. The Moon’saxial tiltmeasures on average only 1.543°, with small fluctuations similar to the inclination changes itsorbital planeexperiences.

Let’s take a top-down view of these axes of rotation. In this next demonstration, I’m marking thetwoanglesbetween thereference directionand the two planes that contain the axes of rotation of theEarthand theMoon, and are also perpendicular to theecliptic:

This rotating motion of the axis of rotation of a celestial body is known asaxial precession. The Earth’s axisrotatesvery slowly, completing a full cycle in roughly 26,000 years.

Compared to the Earth’s, the Moon’s axisrotatesmuch more rapidly, finishing one turn in18.61 years18 years and 223 days. You may recall that this is the exact same duration as the Moon’s nodal precession, where theline of nodesrotates over time. In fact, the orientation of the Moon’s axis of rotation is strictly controlled by the orientation of the Moon’sorbital plane.

This dependence is reflected in the demonstration below, where I’m drawing ablue linethat’s perpendicular to theecliptic plane, adark gray linethat’s perpendicular to the Moon’sorbital plane, and thewhite lineof the Moon’s rotation axis:

Thesethreelinesalways lie flat in the same plane. This relation is summarized inCassini’s third law, which states that the Moon’srotational axisstays in the plane formed by theothertwolines. As the Moon’sorbital planerotates in nodal precession, so does the Moon’saxis of rotation.

The final aspect of nodal precession that we need to consider deals with its impact on observers on Earth. As the Moon’sorbital planerotates, it can be aligned with the Earth’s axis of rotation to a higher or lower degree.

In the simulation below, I rotated the camera’s “up” direction to match the Earth’saxis of rotationand I also keep rotating the viewing angle with the Moon’sorbital plane, giving us an unchanging outlook on these elements. I then mark theanglebetween the Earth’saxisand thedirection perpendicularto the Moon’sorbital plane:

Notice that thisangleoscillates over a long period of time, reaching a minimum of around 18.13° and a maximum of around 28.72° – I’m marking these extremes with fainter lines. Over the course of18.61 years18 years and 223 days, the orbital plane goes through its entire tilting cycle.

Depending on thatrelative angleof the Moon’s orbital plane, observers on Earth can see the Moon sweeping through the sky in a broader or narrower band. In the demonstration below, the trail we see marks 30 days of the Moon’s path in the sky. The slider lets you jump through time over the whole period of the next18.61 years18 years and 223 days:

Notice that the width of the “band” of the Moon’s position gets thinner and thicker over the years, in correlation with changes between the relative orientation of the Moon’s orbital plane and the Earth’s axis of rotation.

It’s primarily the Sun’s gravity that disturbs the Moon’s orbit from the pristine elliptical path. As the Moon orbits around Earth and those two bodies orbit around the Sun, the distance between the Sun and the Moon varies. This changes the strength of those gravitational interactions, causing the precessing effects.

What I’ve discussed here were only the major and most visible components of the Moon’s motion through space. Historically, the science oflunar theorytries to decompose the motion of the Moon into various cyclical elements that depend on the relative position of the Moon, the Earth, and the Sun. Many of these effects even have theirown names.

Themodern developmentsin prediction of the Moon’s position rely on direct computer simulation of the motion of all the planets, their moons, and hundreds of other small bodies in the Solar System. These calculations also account for other effects like non-spherical shape of the bodies or more complicated gravitational interactions arising fromgeneral relativity.

For us, it’s time to stop observing merely the gravitational influences of the Sun. We’re finally ready to cast some light on the visual aspects of its presence.

# Sunlight

Let’s see how the Earth and the Moon actually look in space. To make it easier to find the Sun when you’rezoomed in, theyellow linesindicate the “towards the Sun” direction for the two bodies:

Since the Sun is so far away, at any given time the sunlight splits the Moon and the Earth into pretty much even halves of lit and unlit parts. As these bodies spin around their axes, they experience their respectivesolardays. In the demonstration below, I added the familiar arrows glued to the surface of these bodies, letting us track their orientation more precisely:

For our planet, it takes, on average, 24 hours for the same location on the ground to pointat the Sunagain. The Moon rotates much more slowly, so the equivalent cycle of one solar Moon day lasts29.530 days29 days, 12 hours, and 44 minutesof Earth time.

These periods are longer than a single spin around the axes of rotation, as measured by crossings of thereference direction. These bodies keep moving on their orbit around the Earth and the“towards the Sun”direction keeps advancing too, requiring more body rotation for the arrows to line up withthat directionagain.

Let’s jump back onto the surface of Earth to see how the sunlight affects what we see in the sky. You can use the sliders below to independently changedateandtime:

Notice that the sunlightscattersthrough Earth’s atmosphere, giving the sky the familiar blue color during daytime, and a yellowish and reddish tint at sunrise and sunset. I’m once more making Earth transparent, letting you look below the horizon where I’m hiding any atmospheric effects.

Notice that we can often see the Moon visible in the daily blue sky, because the sunlight reflected from the Moon’s surface contributes additional light to the light coming from the sky itself. The dark part of the Moon doesn’t reflect any light, so we only see the bare blue shade of the sky in that unlit area.

Most importantly for us, over the course ofmany days, the lighting on the Moon changes too, but to see it better we have to zoom in and lock the camera on the Moon’s lit surface:

As time passes, the Moon goes through itsphases, progressing between being fully lit and not lit at all. Traditionally, these phases have particular names, which you canscrubthrough in the demonstration below:

To see the progress of light with minimal distraction, I’m showing these phases as seen from the North or South Pole and with all the atmospheric effects removed. As we’ve seen earlier, a more typical observer will see the Moon go through its phases embedded in the dark or bright skies, and the Moon will rotate as the observer shifts around to keep it in view.

The Moon phases are caused by changes in relative position of the Moon, the Earth, and the Sun. In the demonstration below, you can see the space view of these bodies, with the cone of visibility showing what an observer on Earth sees astime passes. For clarity, you can change the size of the objects with the buttonin the bottom right corner:

The Sun always lights up roughly half of the Moon, and the phases seen from Earth change because we see different portions of the Moon’s lit surface.

The period between occurrences of the same phase is known as thesynodic month– this period averages at29.530 days29 days, 12 hours, and 44 minutes. The average synodic month has the same duration as the average Moon solar day, because the locked spin and orbital motions keep them even.

The synodic month is the longest of the four lunar months we looked at. As the Moon and the Earth progress on their path around the Sun, it takes the Moon a bit more time to be in the same relative position to the Earth and the Sun. The length of a calendar month is based on the synodic month, but the length of each of the twelve months has been adjusted to make them all fit neatly into a whole calendar year.

When we look at the new or full moon from above the ecliptic plane, the Sun, the Moon, and the Earth are all aligned. However, because of the inclination of the Moon’s orbital plane, the three bodies typically don’t form a straight line, and the side view shows that the Moon is a little below or above the ecliptic.

We can see this best when we look at shadows cast in space by the Earth and the Moon. To make the dark cones of the shadows cast by the two bodies visible, I’m filling the entire space with the Sun’s light:

When the Moon, the Earth, and the Sun align, and either the Earth or the Moon are in their neighbor’s shadow, we get to experience truly breathtaking astronomical events – eclipses. To grasp the details of eclipses let’s first try to understand the conical shapes of the shadows we’ve just seen and what impact they have on the observers.

The demonstration below shows an illustrative example of theSun, somecelestial body, and anobserverlooking at theSun. The right side shows how theobserver, wearing darkening equipment, sees theSun. You can drag thatcelestial bodyaround to see how its placement affects the visuals for theobserver:

Notice that the sunlight forms three distinct zones. Inside theblue zone, theobserverdoesn’t see theSunat all – it’scompletely obscuredby theplanet. In theorange zonetheobserversees theSunpartially occluded, with theSungetting more exposed as theobserveris closer to the outer border of theorange zone. Outside of theorange zonethe observer always seesthe entireSun.

When the Moon obscures the Sun, causing Earth to be in the Moon’s shadow, asolareclipse occurs. These conditions can only be met around a new moon, but a new moon doesn’t guarantee that a solar eclipse will occur.

In the previous simulation, it was easy for us to just drag theplanetaround to hide theSunfrom theobserverfloating somewhere in space. Unfortunately, the Moon’s inclined orbit makes it much harder for its shadow to land in the right spot to occlude the Sun for observers on Earth.

We can see it more clearly in the Earthly skies by tracking the position of the new moon over the course of several synodic months – you canflip through themwith the slider. I’m drawing the outline of the Moon with adark pink line:

Coincidentally, notice that the Moon during a new moon is never visible to the naked eye because the sunlight hits the Moon’s surface almost entirely on its opposite side. The Moon is also either placed in the blazingly bright skies nearby the Sun, or it’s hidden under the horizon in the night sky. However, if the Moon’s position relative to the ecliptic is fortunate enough, the fringe of its lit new moon surface can be justbarely visiblein carefully taken telescope photography.

For the Sun and the Moon to visually overlap, the Moon has to be very close to theecliptic plane. For this to happen, theline of nodesthat joins the locations at which the Moonsinks underorrises abovetheeclipticneeds to more or less pointtowards the Sun.

You can experience this below byscrubbing through timewith the second slider to arrive at the conditions leading to the solar eclipse that passed across North America onApril 8, 2024:

Let’s analyze the shadow cast on the Earth on that day in more detail. In the demonstration below, the right side shows the observer on the sunlit Earth with the visible Moon’s shadow sweeping across the Earth. The left side shows the zoomed-in view of the Sun, as seen by that observer through eclipse glasses:

Notice theblueandorangecurves on the Earth. They match the shadow zones we’ve seen before, and they divide the surface of our planet into three distinct regions. Outside of theorangeshape the Sun isn’t occluded by the Moon, so these areas of the Earth don’t experience any effects of the eclipse.

On theinsideof theorangeshape, the Sun is partially occluded by the Moon – these areas experiencepartialsolar eclipse. The closer the observer is to theblueshape, the more obscured the Sun is, and the darker the area on the ground.

Finally, inside theblue regionthe Sun iscompletely occludedby the Moon and atotalsolar eclipse occurs. Below you’ll find a re-enactment of this event, showing visibleSun’s coronaandprominencesshooting out from the Sun’s surface:

Although the Sun is very big, it’s also very far away, so it ends up having almost the same size as the Moon in the visible sky, making total solar eclipses possible. Recall, however, that the Moon traverses a non-circular orbit, so its visible size in the sky changes over time. When the Moon is farther away from Earth it may never completely cover the Sun. This happened during the solar eclipse ofOctober 14, 2023:

Thistype of eclipse is known as anannulareclipse, and when it happens, the criticalblue regionof totality ceases to exist, because some parts of the Sun are always visible.

When it’s Earth that casts its shadow onto the Moon, alunareclipse occurs. A lunar eclipse occurs only around a full moon. In the demonstration below, you can see the total lunar eclipse that occurred onNovember 8, 2022. Theorangeandblueshapes yet again define the regions where, from the perspective of the Moon, the Sun ispartiallyorfullyoccluded. Note that, to reflect the perceptual effects of this event, I’m adjusting the camera’s brightness setting as the Moon gets obscured:

During the totality, the dim red light on the fully occluded areas of the Moon is revealed. This red tint happens because the sunlight scatters and refracts through Earth’s atmosphere – the surface of the Moon “sees” the red ring of sunset and sunrise all around our planet with the Sun hidden right behind the horizon of the entire globe.

Eclipses are so rare because many orbital motions, each with a different period, need to align for them to happen. If the Moon’s orbit wasn’t inclined, somewhere on Earth we’d experience a solar eclipse during every new moon and a lunar eclipse during every full moon.

There is one more sunlight-related effect you might have observed in the night sky. When looking at a crescent Moon, you’ll sometimes see that even the part that isn’t sunlit is still somewhat visible. I’m simulating this event here:

What lights up the dark part of the Moon is actually the sunlight reflected from Earth in an effect aptly known asearthshine. The intensity of earthshine depends on the cloud coverage on Earth and the relative positions of the three bodies.

At this point we’ll once more leave the surface of Earth to venture back into space, giving us the full freedom of motion to explore the interaction of sunlight with the surface of the Moon:

As we look at the lit Moon, its surface features become distinguishable only by the variation in color as well as the shadows cast near the terminator area where the light hits the surface at an oblique angle – you might have noticed the edges of all the craters and mountains. Let’s explore the details of lunar surface up close.

# Lunar Surface

Although a realistic view of the Moon gives us an impression of its surface, we can get a much better look at its shape with the help of two visual tweaks. First, I’ll color the elevation – thebrighter the color, the higher the altitude of that area. The Moon has no sea level to speak of, so the altitude equal to the Moon’s mean radius is typically designated as the baseline of0 feet0 meters. Second, I’ll make the height differences in the 3D modelten timesas large as they actually are, making the elevation changes much more prominent:

This mode reveals the enormous variation on the Moon’s surface. Thehighest pointon the Moon rises35,387 feet10,786 metersover the Moon’s mean radius, while thelowest pointsinks30,112 feet9,178 metersbelow that average value.

Large swaths of the Moon are covered withimpact craters, and many of them have even more craters inside them. These craters formed when variousimpactorslike meteoroids and asteroids hit the Moon’s surface.

Depending on the size and speed of the impactor, different types of craters can develop. Smaller impacting projectiles formsimple craterswith bowl-like shapes and raised rims. Larger objects hitting the surface formcomplex craters. In complex craters, the area under impact can spring back up to form a central rebound – a mountain peak formed in the middle of the crater. The most energetic impacts createmulti-ring basinswith concentric ridges surrounding the central site of impact. If you look closely, you can see all these types of craters on the surface of the Moon.

Notice that all craters share a circular shape. Impactors hit the Moon with extremely fast velocity, on the order of12 to 45 miles20 to 70 kilometerspersecond. When a colliding body slams into the ground, it creates a strong compressive shockwave, which hemi-spherically expands in the ground in all directions.

The propagation of this explosion-like shockwave is responsible for the rounded shape of the crater, even when the impacting body itself isn’t spherical or when it strikes the Moon at an angle. In fact, an impactor ismost likelyto hit the surface of a planet at a 45° angle and only very oblique strikes createelongated craters.

This shockwave excavates the ground matter, ejecting it all around the crater. As the debris falls, it often forms smaller secondary craters. The material ejected during impact can also cover much greater distances, creatingray systems. You can see them as streaks on the surface of the Moon. In the demonstration below, the little draggable indicator pinpoints the same location on both views, letting you see theelevationof the features visible in regular sunlight:

You may have noticed that many of the largest basins have relatively smooth, crater-less bottoms – these arelunar maria. Maria is a plural form of Latin wordmare, which stands for asea. These impact basins were flooded by lava around three billion years ago, erasing the history of any existing craters in that area.

Because of the different chemical composition of that lava, the maria are darker, which we can easily see on the Moon’s surface. Maria are readily visible with the naked eye from Earth, forming the Moon’s unique splotches.

The early solar system was a violent place, but the Moon continues to be struck by meteoroids even in the present day. While the accumulated effects of all larger and smaller impacts are immediately visible in the forms of craters, many micro impactors also affected the Moon’s surface. The Moon has a virtually nonexistent atmosphere, so even the tiniest pieces of space dust can hit the Moon’s surface without burning up in the air, as they do on Earth.

Over the billions of years since the Moon’s formation, each impact has continued to break the surface rocks spreading them across a larger area. All of these impacting processes covered the Moon’s surface with a layer oflunar regolith, which consists of minuscule pieces of rock, often bonded with melted glass formed during impact. The powdery nature of lunar regolith is perhaps best captured by the iconic photograph ofBuzz Aldrin’sfootprint from theApollo 11mission:

The very fine-grained form of lunar regolith is also responsible for the unusual brightness of the full moon, so let’s explore that phenomenon in the last section of this article.

# Lunar Brightness

Let’s establish the baseline for how common objects behave when lit by light. Below I’m showing you a simple sphere covered with matte gray paint. I’m illuminating this sphere with a distant Sun-like light source coming from the direction indicated by theyellow arrow. You can use the slider to tweak thatlight directionand you can drag the sphere around to change your viewing angle:

For the sake of clarity, I’m only drawing onelight arrow, but every place on this sphere is hit by light coming from that direction. The brightness of each part of this matte sphere depends only on the angle at which the light strikes it. Moreover, the brightness of each area doesn’t change as we pan the camera around. You can see this in thesmall circleunder the demonstration – its brightness matches the brightness of the placemarkedon the sphere, at least as long as we can see that spot.

Most importantly, when the observer is positionedstraight onwith the direction of theincoming light, the sides of the sphere are visibly darker, giving it a familiar three-dimensional appearance.

This matches our daily experience with how many matte surfaces look, and perhaps you already had a chance toexplore the detailsof these effects. However, if I were to cover this sphere with lunar soil, its appearance would change – you can experience this below:

Notice that when you pan the camera around, the brightness of themarked patchchanges subtly. Moreover, as your viewing angle approaches the angle of theincoming light, the surface getsbrighterandbrighterand it also becomes increasingly uniformly shaded. When viewedstraight onwith theincoming light, a sphere covered in lunar soil looks more like a flat disc than a three dimensional object. For the samepatchof surface, the amount of light reaching the observer now also depends on the relative position of the observer.

Let’s try to understand these view-dependent interactions. In the left side of the next demonstration, we’re once more seeing a sphere covered in lunar soil with amarked patchon it. On the right side, I’m visualizing the samemarked patch, thedirection of lighthitting it, and theviewing directionfrom which we’re looking at that patch on theleftside. I symbolically draw thatviewing directionon the left side with just one arrow that always pointsintothe screen, but every part of the sphere shares pretty much the same viewing direction since we’re watching it from afar.

As you drag the camera on the left-side, you’ll see thatviewing directionchanging on the right. This gives you a different perspective of thesetwodirections, letting you see how they change relative to thespot:

Notice theanglemarked between thelight directionand theviewing direction. This angle is known as thephase angle, and its value strongly affects the brightness of each section of this sphere. As we decrease thephase angleby aligning theviewing directionwith thelight direction, the surface covered with lunar soil becomes brighter.

In the demonstration below, we can compare the visuals of a classic matte sphere on the left, with a lunar soil sphere on the right. The plots below track the dependence between thephase angleand thetotalamount of reflected light reaching you from the surfaces of each sphere:

As you drag the view around, yourphase anglechanges. This obscures or reveals a larger fraction of the lit surface, affecting how much light we see. As expected, for amaximumphase angleboth surfaces get completely dark because the light illuminates the hidden halves of the spheres.

However, when thephase angleisvery smalland we’re looking at the lunar sphere from a similar direction as theincoming light, the brightness of the lunar sphere rapidly increases with the effect known asopposition surge. You may have noticed this when watching the night sky – the Moon is significantly brighter during a full moon than even a few days before or after that phase.

On Earth, we have borderline no control over thephase angle– the position of our planet, the Moon, and the Sun predetermine thelight direction, theviewing directionand the resultingphase anglefor us:

These interactions between the lunar soil and light aren’t just visible from Earth, but also directly on the surface of the Moon. Below you can find a photograph from the Apollo 11 mission showing a brighter halo right where the camera’s viewing direction is very close to the direction of the sunlight hitting the surface:

To understand how opposition surge arises, we have to investigate the interactions between the grains of lunar regolith and the light shining on them. Let’s first take a look at some simple models of grains of Moon dust casting shadows on agray disc. You can change thedirection of the lightwith the slider:

As you change thedirectionof the incoming light, the shadows also move around to be on the opposite side of the light. When you thenlook at the scenefrom thedirection of the light, you’ll notice that all the darkness of the shadows disappears – they’re hidden behind the grains themselves. Naturally, the shadows are still there, they’re just not visible from that specific angle.

Even in this simple scene, we already witness how a few shadow-casting grains can visibly affect the perceived darkness, so let’s scale things up by viewing a large collection of grains from a bit farther away. You can once more control thedirectionof the incoming light with the slider:

All the randomly oriented grains cast shadows on each other, and when viewedfrom the side, these shadows make the surface look visibly dark. However, when we glance at the surface fromroughly the same angleas theincoming light, the surface becomes much brighter. This happens even when the light hits the surface at avery shallow angle.

These conditions are met almost exactly during a full moon, or in the center of the astronaut’s camera pointed at the ground – the phase angle is small because the viewing direction is very strongly aligned with the incoming sunlight.

The effect we’ve just seen is known asshadow hiding. It was originally believed that shadow hiding is the principal cause of the opposition surge, but in the 1990s another effect started to gain traction as the possible explanation of this phenomenon.

This other effect is slightly more complicated, and it requires looking at the wave nature of light. I’vebriefly discussedthese concepts before, but to recap, light is an electromagnetic wave that travels through space with its electric and magnetic components oscillating with a set frequency.

In the demonstration below, I’m drawing a simple,pulsatingsphericalsourcethat emits light in every direction. The light emitted from thissourcespreads out spherically, but if I drew the emitted waves as a set of overlapping spheres it would be quite difficult to grasp how the electric field varies over time. Instead, I’m showing the changing amplitude of just oneslicethrough this field, and I’m using two colors to distinguishpositiveandnegativevalues. The slider below lets you control thewavelengthof this light, which determines the distance between two consequentpeaksorvalleys:

Notice that the amplitude, or “height”, of the wave decreases with distance, which we can also see in the decreasing intensity of theredandbluecolors.

Let’s take a closer look at how these waves spread over a longer distance. On the left side of the next demonstration we can see a top-down view of asourceemitting light, while on the right side we see how this wave looks to anobserverthatlooks atthissourcefrom far away. You can drag thesourcearound to change its position:

Far away from thesource, the radii of spheres of propagating waves become very large, so the arcs of individualpeaksorvalleyslook like straight lines.

An electromagnetic wave like this could travel through the vacuum of space completely uninterrupted. However, any tiny object put in the light’s path will scatter it to some extent, creating a new wave.

In the demonstration below, I put a smallgrainof lunar regolith in the path of the incoming light – you can drag thisspeckaround to change its position. You can also control thedirectionof this light with the second slider. This littledust speckscatters the incoming light and acts like a new light source emitting waves that eventually reach theobserver:

In general, the amplitude of this newly scattered wave can vary with direction, but for simplicity I’m showing it here as a simple spherical wave that spreads uniformly in all directions.

Let’s add one morelunar grainto our scene. The light will now scatter from bothparticles, and the resulting waves willinterferewith each other – where twopeaksor twovalleysoverlap perfectly their amplitude doubles, but when apeakmeets avalleythey cancel each other out, creating dark areas:

As you drag thewavelengthslider, or you change thedirectionof the incoming light,oryou move thegrainsaround, you’ll see that the interference patterns of light reaching theobserverchange drastically.

So far we’ve only looked at the scattering of the directly incoming light, but the light scattered by each grain interacts with theothergrains as well. Those grains scatter the originally scattered light, which can then be scattered by other grains, and so on.

Let’s take a closer look at the light interactions acrosstwoscattering events, that is whenincoming lightscatters from the first grain, then scatters from the second grain, and then reaches theobserver,orwhen theincoming lightscatters from the second grain, then scatters from the first grain, to finally reach theobserver:

Now it’s really hard to see what’s going on, so I’m going to make two changes. First, I’ll split all the light into the incoming, scattered once, and scattered twice components – you can choose between them in the next demonstration. Second, I’ll make the source lightcontinuouslyemit light, letting us see the resulting interference patterns in more detail:

We can now easily how thesingly scattered lightreaching theobserveris very sensitive to the placement of the grains, thewavelengthand thedirectionof the incoming light.

If a rough surface is lit with a light of a single frequency, e.g. created by a laser, one could indeed see aspeckleof these constructive and destructive interference regions hitting the observer from various elements of the surface. Thankfully, sunlight contains a whole spectrum of various frequencies, so all these patterns average out to some baseline intensity of light that the observer can see.

It may seem that the light reaching the observer afterscattering twiceis equally messy as it was after just one scattering event. However, when the incoming lighthits the two particlesfrom theviewing direction, the doubly-scattered waves reaching theobserveralways interfere constructively, regardless of the light’swavelength, or how those particles are positioned!

To understand why this happens, we need to trace the path that the light travels. In the demonstration below, you canscrub through timewith the second slider to look at the path that onepeakandvalleyof an incoming wave takes. For clarity, I’m hiding the wave of the incoming light after it has scattered on the two grains. Similarly, I’m also hiding the waves generated by the first scattering events, leaving only the waves of thesecondscattering:

Thedark pink trailshows the path of light hitting and scattering from the first particle, then hitting and scattering from the second particle, and then eventually arriving at theobserver. Thelight pink trailshows the path of light hitting and scattering from thesecondparticle, then hitting and scattering from the first particle, and then arriving at theobserveras well.

If theincoming light directionmatchestheviewing direction,bothtrailstraverse theexactsame path, just in the opposite order. As thepeaksandvalleyson thetwopathstravel the same distance from the source all the way to theobserver, they always add up constructively forallgrain positions. This positive interference creates consistently brighter light that reaches theobserverwhen theincoming lightandviewingdirections are aligned.

Light waves incoming fromsome other directiontraverse different paths of different lengths, so they interact with each other more or less randomly, with various degrees of constructive or destructive interference. Across all the grain positions and light wavelengths, this results in some average, base intensity of this second scatter.

This entire effect is known ascoherent backscattering. The same interactions happen for any two, three, or more consequent scattering events between the same collection of grains. As long as the scattered incoming light has a path to eventually leave the surface, it also means it can travel the same path, but in the other direction.

Coherent backscattering is currently believed to be the primary contributor to the opposition surge, with a smaller influence from shadow hiding, but both of these effects make the full moon a bright presence in the night skies.

Our journey around the Moon ends here, and so does this article. As we leave the darkness of space, let’s take a final look at the Earth and Moon so beautifully captured in aphotographtaken from space:

# Further Reading

For a short and approachable read,Moon Owners' Workshop Manualdiscusses many of the general facts and discoveries about the Moon, all presented with great photographs and illustrations. The same publisher also has guides on theApollo 11andlater Apollo missions– they very accessibly cover the technical aspects of that wondrous era of lunar exploration.

Lunar Sourcebookis a book on many aspects of lunar history and geology. Although the title is three decades old and many of its data-dense sections are only useful as a reference, itsfree availabilitymakes it unbeatable for deeper dives into lunar sciences.

Finally,Luna Cognitacan only be described as a labor of love. Over the course ofthreethick volumes, Robert A. Garfinkle presents a wealth of information on the Moon, including thorough description ofeverycrater, ridge, and mountain one can observe on each day of the entire synodic month.

# Final Words

The Moon may be just an unassuming neighbor in the sky, but its presence affects our lives in many subtle ways. When it reflects sunlight off its scarred surface to guide the way in the darkness of night, or as it breathes life into oceans by rhythmically raising tides, or when it cloaks the Sun in a rare and awe-inspiring total solar eclipse, the Moon reminds us of the celestial world right outside of the safe confines of our planet.

Traveling through the cold and empty space by Earth’s side, the Moon is always just there. It may be barren and dull, but, undeterred by its own lifelessness, it never leaves us completely alone.

Perhaps the next time you catch a glimpse of the Moon’s shiny surface beaming in the night sky, you’ll see it a little differently – not as a mundane fixture of the heavens, but as a fellow companion that gently affects our own existence.