---
title: How my images are dithered | dead.garden
url: https://dead.garden/blog/how-my-images-are-dithered.html
site_name: hnrss
content_file: hnrss-how-my-images-are-dithered-deadgarden
fetched_at: '2026-07-25T19:28:43.584976'
original_url: https://dead.garden/blog/how-my-images-are-dithered.html
date: '2026-07-22'
description: Hello there! This is my personal website and it is allergic to SEO.
tags:
- hackernews
- hnrss
---

# Jo's Blog

## How my images are dithered

July 06, 2026 (20:57)Jo❤️Read as plaintext

I don't know much about dithering. But when I visit other people's sites and they dither their images in cool ways I always wonder how they do it. So in case anyone is wondering, here's my current method for dithering thesepinkimages.

Edit:Almost like I know myself too well — the pictures now look like this instead:

Which is covered in the post.

Welcome to all the hacker news readers who clicked on this post. I am thankful and glad that this post has come to entertain some of you. Here are some things I feel the need to add to the post since it has left my regular audience:

* There seems to be discussion about whether this counts as dithering. As evidenced by the very first sentence of the post, I am not an authority on the subject. But here is what Wikipedia seems to think:Dithering is analogous to the halftone technique used in printing. For this reason, the term dithering is sometimes used interchangeably with the term halftoning particularly in association with digital printing.(link)In any case — I am/was only aware of this technique being used for AM grid printing, as briefly layed out in the post. So I thought it might be fun to play pretend a little.this is a very inefficient method of reducing the size of an image file — I'd even say this little experiment has nothing at all to do with decreasing file size (in some unlucky cases it will even increase the size of your image). I mention this a few times in the post. It's just a bit of playing around with a certain aestheticplease don't feed images of me and my friends to an LLM?? The code for achieving each effect is all over this page. Just make your own image and feedthatto an LLM.
* this is a very inefficient method of reducing the size of an image file — I'd even say this little experiment has nothing at all to do with decreasing file size (in some unlucky cases it will even increase the size of your image). I mention this a few times in the post. It's just a bit of playing around with a certain aestheticplease don't feed images of me and my friends to an LLM?? The code for achieving each effect is all over this page. Just make your own image and feedthatto an LLM.
* please don't feed images of me and my friends to an LLM?? The code for achieving each effect is all over this page. Just make your own image and feedthatto an LLM.

Dithering, beside making a picture look (to put it professionally) cool as fuck, can also reduce file size (by using less colors while maintaining details) and thus needed storage (if using only the reduced images) and the weight of your website for the client. That's why sites likeLow Tech Magazineuse it, for example.

The idea of pink images came from a post a while back, when I tried this before. The postDesigning without colorintroduces the idea of the current design, where I try to get a sort of black and white "printed" vibe, using color only for emphasis. (This makes sense only when you are a light mode user like me).

The image back then, with the old method, looked like this:

The key difference here being that I limited the picture's palette to true monochrome: black and this pink. Also, the weird "dithered" dots are much bigger.

### So what's this

My goal was to immitate a printed image. While individual pixels on a screen may have the luxury of setting variable values of red, green and blue — making the grid of repeating RGB lights on your screen light up with different intensity — things work a little differently on paper (and other print substrates).

Getting the limited palette of colors your printer is working with to give the illusion of more colors requires using a grid/matrix of dots. You can go about this in three different ways: AM, FM and hybrid grids. The amplitude here being the size of the dot and the frequency, well … the frequency. Making a dark spot with AM grids means big dots, in FM grids it's lotsa dots.

The top shows anFMprint: the dots look chaotic.The bottom showsAM: all dots show up in a predictable pattern and light spots have smaller dots

The problem with amplitude modulated dots is that if you approach this naively you will end up getting unwanted patterns in your images: a so-calledMoiré.

For this reason, there is a rule (DIN 16547) about how exactly the colors are to be offset in an AM print to try and avoid them getting in each others way. Since FM grids are random they do not suffer from this problem.

### Simulating AM pattern on your digital image

I access my server via the command line — so I use a command line tool to quickly edit images. The tool is called imagemagick and is called using the "convert" command.

I found the method to create this illusion online (can't find the link) and adapted it a little. So I can't claim to be the expert on what each individual argument does, but I will try to explain it.

convert "oldfile" -resize 800 -set option:distort:viewport '%wx%h+0+0' \
 -colorspace CMYK -separate null: \
 \( -size 2x2 xc: \( +clone -negate \) \
 +append \( +clone -negate \) -append \) \
 -virtual-pixel tile -filter gaussian \
 \( +clone -distort SRT 2,0 \) +swap \
 \( +clone -distort SRT 2,15 \) +swap \
 \( +clone -distort SRT 2,45 \) +swap \
 \( +clone -distort SRT 2,75 \) +swap +delete \
 -compose Overlay -layers composite -set colorspace CMYK -combine \
 "newfile"

Here's what it does generally: resizes the image to 800px in width (who needs more?), sets the color to CMYK, applies a background to fill the empty space left by rotating (and sets a gaussian blur to filter noise), splits up into the colors, scales them up a bit (for bigger dots) and distorts them (in this case: rotates them) and at the end it combines the 4 images into one again.

The image we generate by running this on the original file looks like this:

Before combining them, these are the individual colors dot grids:

This sets C at 0°, M at 15° etc. But whatever. Zooming in and out doesn't make any weird artifacts apparent so it's good enough.

If we increase the size of the dots to a ridiculous degree (8x8), you can get a better look at what is happening.

#### Edit: The perfect route to CMYK

After sleeping on it and reading the post back, the solution for a pic limited to truly CMYK colors in an AM grid is apparent. For reasons I get into later this is NOT a good way of reducing file size (apart from the fact that limiting colors and resizing the image to 800 in width always reduces the size, everything else is pretty much stacked against that goal). It does, however, look cool.

With the above method, the dots donotvary in size. Why should they? As we already discussed, a digital image (unless I have a GIF or PNG-8 situation somewhere) can give varying intensity of light for R, G and B per pixel. So when we look at the big image above we can cleary see some of the squares are just darker than others. For a true immitation this will not do!

All we need to do is to limit each channel's colors to 2 before combining them again. This is very obvious in hindsight. Idk why the person I got the original command from didn't do this.

convert "oldfile" -resize 800 -set option:distort:viewport '%wx%h+0+0' \
 -colorspace CMYK -separate null: \
 \( -size 2x2 xc: \( +clone -negate \) \
 +append \( +clone -negate \) -append \) \
 -virtual-pixel tile -filter gaussian \
 \( +clone -distort SRT 2,0 \) +swap \
 \( +clone -distort SRT 2,15 \) +swap \
 \( +clone -distort SRT 2,45 \) +swap \
 \( +clone -distort SRT 2,75 \) +swap +delete \
 -compose Overlay -layers composite 
-colors 2
 -set colorspace CMYK -combine \
 "newfile"

This will produce an image that looks like this:

In retrospect I wonder if I might try out images like this instead of pink. If all I want is the general vibe of the grid then pink is fine. Though it does have more colors (shades of pink) for less colors (actually useful distinct ones). Who said blogging about your stupid idea isn't useful?

#### Pink — old method

The script for the old way of doing it had the values of -distort SRT set to "2 (rotation)", meaning it scaled the colors up to 2, making bigger dots.

After running the script above, the colorspace was once again converted, to Gray this time, after which the colors were leveled to monochrome: black andthis pink. The whole command for those who want to try:

convert "oldfile" -resize 800 -set option:distort:viewport '%wx%h+0+0' \
 -colorspace CMYK -separate null: \
 \( -size 2x2 xc: \( +clone -negate \) \
 +append \( +clone -negate \) -append \) \
 -virtual-pixel tile -filter gaussian \
 \( +clone -distort SRT 2,0 \) +swap \
 \( +clone -distort SRT 2,15 \) +swap \
 \( +clone -distort SRT 2,45 \) +swap \
 \( +clone -distort SRT 2,75 \) +swap +delete \
 -compose Overlay -layers composite -set colorspace CMYK -combine \
 -colorspace Gray -colors 2 +level-colors black,#A2719B \ 
 "newfile"

If we zoom in on the image before and after leveling the colors, we can see the dots do seem more like they vary in size. I omitted the -resize flag to give you a better view of the details.

While not entirely accurate, I think this method gets the most printy feel out of an image. Sadly it can swallow a lot of detail, even if the dotsaren'tscaled up. So I abandoned this after a while (also I got sick of looking at it).

Edit:now compare to thereal deal:

### Pink – new method

Monochrome is a cool idea but just has limited use for the blog (and other pics on the website). I need some more depth. What I need is more values of pink. I get these by utilizing the -remap flag.

convert "oldfile" -resize 800 -set option:distort:viewport '%wx%h+0+0' \
 -colorspace CMYK -separate null: \
 \( -size 2x2 xc: \( +clone -negate \) \
 +append \( +clone -negate \) -append \) \
 -virtual-pixel tile -filter gaussian \
 \( +clone -distort SRT 1,0 \) +swap \
 \( +clone -distort SRT 1,15 \) +swap \
 \( +clone -distort SRT 1,45 \) +swap \
 \( +clone -distort SRT 1,75 \) +swap +delete \
 -compose Overlay -layers composite -set colorspace CMYK -combine \
 -remap "$palette" -colors 32 "newfile"

#### Problematic images

For images like the one I've been using everything works beautifully. But with images that are very overwhelmingly light, there can be issues.

Here's an example:

Original image
After running script
After manual edit

The edit in question: increasing brightness to 300%, Saturation to 200%, inverting colors and remaping them to pink

convert "oldfile" -modulate 300,200,100 -negate -remap $palette "newfile" 

This is possibly because my color palette is kinda bad.

### Is this even dithering?

If all you care about is the result then you could say the image has been dithered, especially in the old method. Using only two colors we created the illusion ofsemitones (is this appropriate usage in English?)*. The same is basically true for the new method as well.

But if you care about the method this is not dithering. Or at least it's the most unnecessarily computationally expensive form of dithering I've come across. Let's walk through the steps one more time:

1. Convert RBG to CYMK, adding one channel
2. Split the image into four images and transform each one (starting with scaling them up and inverting them)
3. limit colors to 2 on each and then overlay four images on top of eachother
4. set colorspace to CMYK again
5. limit the colors to 32/64/not sure yet where I want this (overlaying the 4 grids will create new colors)

This whole thing, on my laptop with an 11 year old CPU, can take 10 seconds if the image is big. The file size is not exactly "small" (though still smaller than unscaled pics with more than 32 colors). I can imagine the pattern isn't doing compression algorithms a huge favour. If you value your time or care aboutactuallyreducing an image's sizedo not do this.

### Script

#!/bin/bash
temp="/tmp/images"
palette="/path/to/palette.png"
rm $temp
if [[ $1 = "" ]]; then
if [ -d smol ]; then 
echo must run with argument
else 
mkdir smol big
ls -r *.webp > $temp
ls -r *.png >> $temp
ls -r *.jpg >> $temp
ls -r *.jpeg >> $temp
ls -r *.gif >> $temp
fi
else 
ls -r *$1 > $temp
cp *$1 big
cat $temp
cp $(cat $temp) big/.
fi
i=$(cat "$temp" | wc -l)
echo $i
 while [[ $i -gt 0 ]]
 do
name="$(head -n $i $temp | tail -n +$i)"
echo "doing $name"
convert "$name" -set option:distort:viewport '%wx%h+0+0' \
 -colorspace CMYK -separate null: \
 \( -size 2x2 xc: \( +clone -negate \) \
 +append \( +clone -negate \) -append \) \
 -virtual-pixel tile -filter gaussian \
 \( +clone -distort SRT 2,0 \) +swap \
 \( +clone -distort SRT 2,15 \) +swap \
 \( +clone -distort SRT 2,45 \) +swap \
 \( +clone -distort SRT 2,75 \) +swap +delete \
 -compose Overlay -layers composite -colors 2 \
 -set colorspace CMYK -combine \
 -colors 64 "smol/$name"
(( i-- ))

echo $i
done

To end with, here is the original image withactualdithering (FloydSteinberg)

This file issmallerthan the new (pink) method (but bigger than the old one).

Edit:the true method will produce a smaller file for this image :^} (though this isnota rule!)

### (Edit:) RGB

You can ofc do the same thing with RGB instead of CMYK. That wouldn't really be as accurate for a "print vibe"!! but here's the RGB AM grid version:

📍 Posted from Erfurt, DE

Tags:meta,code

Category: tech

Thoughts? Suggestions? Hate mail?Let me know!