---
title: forbidden secrets of ancient X11 scaling technology revealed
url: https://flak.tedunangst.com/post/forbidden-secrets-of-ancient-X11-scaling-technology-revealed
site_name: lobsters
fetched_at: '2025-06-25T23:07:43.529849'
original_url: https://flak.tedunangst.com/post/forbidden-secrets-of-ancient-X11-scaling-technology-revealed
date: '2025-06-25'
tags: graphics, unix
---

## forbidden secrets of ancient X11 scaling technology revealed

People keep telling me that X11 doesn’t support DPI scaling, or fractional scaling, or multiple monitors, or something. There’s nothing you can do to make it work. I find this surprising. Why doesn’t it work? I figure the best way to find out is try the impossible and see how far we get.I’m just going to draw a two inch circle on the screen. This screen, that screen, any screen, the circle should always be two inches. Perhaps not the most exciting task, but I figure it’s isomorphic to any other scaling challenge. Just imagine it’s the letter o or a button we wish to draw at a certain size.I have gathered around me a few screens of different sizes and resolutions. My laptop screen, and then a bit to the right a desktop monitor, and then somewhere over that way a nice big TV. Specifically:$ xrandr | grep \ connected
eDP connected primary 2880x1800+0+0 (normal left inverted right x axis y axis) 302mm x 189mm
DisplayPort-0 connected 2560x1440+2880+0 (normal left inverted right x axis y axis) 590mm x 334mm
DisplayPort-1 connected 3840x2160+5440+0 (normal left inverted right x axis y axis) 1600mm x 900mmI think I just spoiled the ending, but here we go anyway.I’m going to draw the circle with OpenGL, using a simple shader and OBT. There’s a bunch of not very exciting code to create a window and a GLX context, but eventually we’re going to be looking at the shader. This may not be the best way to draw a circle, but it’s my way. For reference, the full code is incircle.c.voidmain(){float thick=radius/10;if(abs(center.y-gl_FragCoord.y)<thick/2)thick=2;
 float pi=3.14159;
 float d=distance(gl_FragCoord.xy,center);
 float angle=atan(gl_FragCoord.y-center.y,gl_FragCoord.x-center.x);
 angle/=2*pi;
 angle+=0.5;
 angle+=0.25;if(angle>1.0)angle-=1.0;
 float amt=(thick-abs(d-radius))/thick;if(d<radius+thick && d>radius-thick)fragment=vec4(rgb(angle)*amt,1.0);elsediscard;}I got a little carried away and made a pretty color wheel instead of a flat circle.The key variable isradiuswhich tells us how many pixels from the center the circle should be. But where does the shader get this from?glUniform1f(0, radius);Okay, but seriously. We listen for configure events. This is the X server telling us our window has been moved or resized. Something has changed, so we should figure out where we are and adjust accordingly.caseConfigureNotify:{XConfigureEvent*xev=(void*)&ev;intx=xev->x;for(inti=0; i<16; i++){if(x>=screen_x[i]&& x-screen_x[i]<screen_w[i]){float r=screen_w[i]/screen_mm[i]*25.4;if(r!=radius){radius=r;}break;}}width=xev->width;
 height=xev->height;}Getting closer. The numbers we need come from the X server.XRRScreenResources*res=XRRGetScreenResourcesCurrent(disp,root);
 float screen_mm[16]={0};
 float screen_w[16]={0};
 float screen_x[16]={0};intj=0;for(inti=0; i<res->noutput; i++){XRROutputInfo*info=XRRGetOutputInfo(disp,res,res->outputs[i]);
 screen_mm[j++]=info->mm_width;}j=0;for(inti=0; i<res->ncrtc; i++){XRRCrtcInfo*info=XRRGetCrtcInfo(disp,res,res->crtcs[i]);
 screen_w[j]=info->width;
 screen_x[j++]=info->x;}It’s somewhat annoying that physical width and virtual width are in different structures, and we have to put the puzzle back together, but there it is.Some more code to handle expose events, the draw loop, etc., and that’s it. A beautiful circle sized just right. Drag it over onto the next monitor, and it changes size. Or rather, it maintains its size. Send it over to the next monitor, and same as before.Time for the visual proof. A nice pretty circle on my laptop. Another circle on my monitor. And despite the 4K resolution, a somewhat pixely circle on my TV. Turns out the hardest part of this adventure was trying to hold an uncooperative tape measure in place with one hand while trying to get a decent, or not, photo with the other.We were so close to perfection. Somebody at the factory screwed up, and my TV is actually 66.5” wide, not the claimed 63 inches. So if we learn anything today, it’s that you shouldn’t use a consumer LG TV for accurately measuring the scale of structural engineering diagrams, at least not without further calibration.The good news is we’ve done the impossible. Even better, I didn’t mention that I wasn’t actually running this program on my laptop. It was running on my router in another room, but everything worked as if byMIT-MAGIC-COOKIE-1. Alas, we are still no closer to understanding why people say this is impossible.Anyway, I think the point is we should probably ignore the people who can’t do something when they tell us we can’t do it either. I woke up this morning not knowing precisely how to draw a scaled circle, having never done so before, but armed with a vague sense that surely it must be possible, because come on of course it is, I got it working. And now look at me, driven insane by the relentless stare of three unblinking eyes.With my new knowledge, I also wrote an onscreenrulerusing the shape extension. Somewhat tautological for measuring the two inch circle, but in the event anyone asks, I can now tell them my terminal line height is 1/8”, and yes, I measured.

Posted 24 Jun 2025 17:59 by tedu Updated: 24 Jun 2025 17:59

Tagged:
programming

x11
