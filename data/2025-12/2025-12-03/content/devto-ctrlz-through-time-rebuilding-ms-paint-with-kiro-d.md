---
title: 'Ctrl+Z Through Time: Rebuilding MS Paint (With Kiro Doing the Heavy Lifting) - DEV Community'
url: https://dev.to/annu12340/building-a-windows-95-ms-paint-clone-with-ai-superpowers-and-a-little-help-from-kiro-4pn3
site_name: devto
fetched_at: '2025-12-03T19:08:13.129862'
original_url: https://dev.to/annu12340/building-a-windows-95-ms-paint-clone-with-ai-superpowers-and-a-little-help-from-kiro-4pn3
author: Annu
date: '2025-11-29'
description: Remember MS Paint? That glorious relic of Windows 95 where you'd spend hours drawing stick figures... Tagged with kiroween, kiro, hackathon, vibecoding.
tags: '#kiroween, #kiro, #hackathon, #vibecoding'
---

Remember MS Paint? That glorious relic of Windows 95 where you'd spend hours drawing stick figures and filling random shapes with the bucket tool? Well, I just built a pixel-perfect recreation of it... except this one has AI superpowers. And honestly? Kiro made the whole thing way more fun than it had any right to be.

## The Idea: Nostalgia Meets AI

Picture this: It's 2024, and I'm staring at my modern, sleek design tools thinking "you know what's missing? Beveled buttons and that classic gray background." So naturally, I decided to build a full-blown MS Paint clone with React and TypeScript. But here's the twist - I gave it AI capabilities. Because why not let an AI analyze your stick figure drawings and politely suggest you "consider adding more depth to the composition"?

The result? A web app that looks like it time-traveled from 1995 but can generate images from text and critique your artwork like a pretentious art school professor.

## Enter Kiro: My AI Pair Programming Buddy

Now, I could've spent weeks wrestling with Canvas APIs, debugging flood fill algorithms, and trying to remember how those 3D button effects worked. Instead, I had Kiro as my coding companion, and honestly, it felt like having a really smart friend who never gets tired of your questions.

### The Spec-Driven Approach

Here's where it got interesting. Instead of just diving into code (my usual chaotic approach), Kiro helped me build this thing properly with specs. We created:

* requirements.md- All the "what should this thing do?" stuff
* design.md- The "how are we gonna build this?" blueprint
* tasks.md- The actual work breakdown
* api-documentation.md- Because future me deserves documentation

It felt like having a project manager who actually knows how to code. Kiro would read through my requirements and be like "okay, so you want 16 tools, a color palette, AND AI features? Let's break this down."

### The Fun Parts

Building the Windows 95 UI:

Me: "I want those classic beveled buttons with the 3D effect"

Kiro:Generates perfect CSS with inset shadows and multi-color borders

Me: "Holy crap, that's exactly it"

The best part? Kiro understood the aesthetic I was going for. I'd say "make it look like Windows 95" and it would nail the gray backgrounds, the beveled edges, even the font choices. It's like it had a nostalgic childhood too.

The Canvas Drawing Logic:

Drawing on HTML5 Canvas can be... finicky. You've got mouse events, coordinate tracking, different tools with different behaviors. I was dreading the flood fill algorithm especially (anyone who's implemented one knows the pain).

Me: "I need a flood fill that won't crash the browser"

Kiro:Provides an optimized algorithm with stack-based approach instead of recursion

Me: "You just saved me from stack overflow hell"

AI Integration:

This is where things got wild. I wanted three AI features:

1. Text-to-image generation ("draw a cat")
2. Artwork analysis ("what do you think of my drawing?")
3. A helpful chatbot

Kiro helped me set up the entire backend proxy, integrate NVIDIA's APIs, and handle streaming responses. We went from "I have an API key" to "I have a working AI chatbot" in like an hour.

The coolest part? Kiro helped me implement natural language command detection. So users can say "draw me a sunset" or "generate a robot" or "create abstract art" and it just works. No rigid command syntax needed.

## The Development Flow

Here's what a typical session looked like:

Me:"I need to add the airbrush tool"

Kiro:"Alright, let's add it to the tool config, implement the drawing logic with random spray particles, and add tests"

Five minutes later, airbrush is working

Me:"The chatbot should detect when someone wants to generate an image"

Kiro:"Here's a regex pattern matcher that handles 'draw', 'generate', 'create', and 'make' commands with various formats"

Boom, done

It was like having a coding buddy who's really good at the boring parts (looking at you, TypeScript types) but also gets excited about the fun stuff (AI-generated images appearing on your canvas!).

## The Property-Based Testing Revelation

Kiro introduced me to property-based testing with fast-check, and I'm kind of obsessed now. Instead of writing:

test
(
'
pencil draws a line
'
,

()

=>

{


// Test one specific case

});

Enter fullscreen mode

Exit fullscreen mode

We wrote:

test
(
'
pencil draws correctly for ANY coordinates
'
,

()

=>

{


// Test 100+ random cases automatically

});

Enter fullscreen mode

Exit fullscreen mode

It's like having a QA team that tries to break your code in creative ways. And Kiro set it all up with explanations of why each property test mattered.

## The Moments That Made Me Laugh

### The Clippy Situation

Okay, let's talk about Clippy. You remember Clippy, right? That overly enthusiastic paperclip from Microsoft Office who'd pop up like "It looks like you're writing a letter!" when you absolutely were not writing a letter?

Well, I couldn't build a Windows 95-era app without including everyone's favorite (or most annoying) office assistant. But here's where it got fun.

Me:"Should I add Clippy to the chatbot?"

Kiro:"Absolutely. But why stop at one Clippy?"

Me:"...go on"

Kiro:"Give Clippy different personalities based on context"

And that's how we ended up with FIVE different Clippy variants, each with their own vibe:

🎃 Halloween Clippy- Shows up around spooky season, probably gives you tips on drawing jack-o'-lanterns and ghosts. Has that "I'm fun at parties" energy but in paperclip form.

🔬 Scientist Clippy- Wears tiny glasses (yes, a paperclip with glasses). Appears when you're doing technical stuff. Probably explains the flood fill algorithm in excruciating detail. "Actually, it's a breadth-first search traversal of adjacent pixels with matching color values..."

🎓 Teacher Clippy- The patient one. Shows up during the onboarding tour. Doesn't judge when you click the wrong tool for the fifth time. "That's okay! Let's try again!" Energy: kindergarten teacher who's had three coffees.

🧙 Wizard Clippy- The mystical one. Appears when AI features are active. Probably knows magic (or at least, machine learning). Has that "I've seen things you wouldn't believe" vibe. Definitely the coolest Clippy.

📎 Classic Clippy- The OG. Just vibing. Gives general help. The baseline Clippy energy we all know and... tolerate?

### The Clippy Personality System

Here's the thing - Kiro helped me implement a system where Clippy's personality actually changes based on what you're doing:

* Drawing tools? Classic Clippy shows up with basic tips
* AI image generation? Wizard Clippy appears with mystical wisdom
* Learning the interface? Teacher Clippy guides you patiently
* October? Halloween Clippy is just... there, being spooky
* Asking technical questions? Scientist Clippy adjusts their tiny glasses

The best part? Each personality has slightly different dialogue patterns. Wizard Clippy says things like "Behold! The AI has conjured your image!" while Scientist Clippy is more like "Image generation complete. The neural network has successfully processed your prompt."

Testing the Personalities:

The funniest part of development was testing all the Clippy variants. I'd generate an image and Wizard Clippy would pop up like "Your artistic vision has been manifested!" and I'd be like "Kiro, this is perfect."

Then I'd switch to asking a technical question and Scientist Clippy would appear with "Let me explain the Canvas API's coordinate system" and I'd think "okay, this paperclip is more knowledgeable than me."

Halloween Clippy just shows up in October and makes everything slightly spooky. "Boo! Want to draw a pumpkin?" Yes, Halloween Clippy. Yes, I do.

### Why Multiple Clippys?

Me:"Is five Clippys too many?"

Kiro:"Is there such a thing as too many Clippys?"

Me:"...fair point"

Look, if you're going to embrace the retro aesthetic, you might as well go all in. And having Clippy change personalities based on context makes the whole experience more fun. It's like having a chatbot that's also a method actor.

Plus, it gave us an excuse to create different Clippy assets. Each one has its own little costume or accessory. Wizard Clippy has a tiny hat. Scientist Clippy has glasses. Halloween Clippy has... spooky vibes? It's a paperclip, we worked with what we had.

### The Clippy Easter Eggs

We also added some fun interactions:

* Click Clippy multiple times and he gets annoyed: "I'm helping! Stop poking me!"
* Ask Clippy about himself: "I'm a paperclip with dreams and aspirations"
* Tell Clippy to go away: He minimizes but leaves a tiny corner visible, like "I'm still here if you need me"
* Generate a really weird image: Wizard Clippy: "Even I didn't see that coming"

The personality system made Clippy feel less like an annoying popup and more like a quirky companion. Which is exactly what you want in a retro paint app with AI features.

The Status Bar:

Me: "I want real-time mouse coordinates in the status bar"

Kiro: "Easy. Also, want to show canvas dimensions and tool info?"

Me: "...yes please"

Now the status bar shows everything, just like the original. It's the little details that matter.

The AI Art Critique:

Testing the vision analysis was hilarious. I'd draw terrible stick figures and the AI would politely say things like "The composition shows promise" and "Consider adding more detail to enhance visual interest." It's like having Bob Ross as an AI, but more diplomatic.

## What I Learned

### 1. Specs Actually Help

I used to think specs were boring corporate stuff. But having everything documented meant I could jump back into the project after a break and know exactly where I was. Kiro made writing specs feel less like homework and more like planning a cool project with a friend.

### 2. AI Pair Programming Is Different

Kiro isn't just autocomplete on steroids. It's more like... a really patient senior developer who:

* Remembers the entire codebase
* Suggests better approaches
* Writes tests without complaining
* Explains WHY things work, not just HOW

### 3. The Right Tools Matter

Using Vite, React 19, TypeScript, and modern testing tools made everything smoother. And Kiro knew all the best practices for each one. No more googling "how to configure Vitest" at 2 AM.

## The Final Product

So what did we end up with?

* 16 drawing tools(pencil, brush, airbrush, shapes, fill bucket, etc.)
* 28-color palette(the classic MS Paint colors)
* Pixel-perfect Windows 95 UI(beveled buttons and all)
* AI text-to-image generation(type "draw a cat", get a cat)
* AI artwork analysis(get feedback on your masterpieces)
* Smart chatbot(answers questions about tools and techniques)
* Property-based tests(because we're fancy like that)

The whole thing runs in the browser, looks like 1995, but has 2024 AI capabilities. It's beautiful chaos.

## Try It Yourself

The code is all there. You can:

1. Clone the repo
2. Get a free NVIDIA API key
3. Runnpm run dev
4. Draw terrible stick figures and have AI politely critique them

## The Kiro Difference

Look, I've used AI coding tools before. But Kiro felt different because:

* It understood context- Not just the current file, but the whole project structure
* It suggested better approaches- "Hey, you could use a ref here instead"
* It wrote actual documentation- Not just code comments, but real docs
* It helped with architecture- Not just implementation details
* It made testing fun- Property-based tests are actually cool!

Building this project solo would've taken weeks. With Kiro? A few days of actually enjoyable coding sessions.

## The Takeaway

I'm just happy I built something that makes me smile.If you're building something and thinking "this is gonna take forever," maybe give Kiro a shot. It's like pair programming, but your partner:

* Never needs coffee breaks
* Doesn't judge your code (much)
* Actually enjoys writing tests
* Makes the boring parts less boring

Plus, you might end up with a retro paint app that can generate images of cats wearing wizard hats. And isn't that what we're all really after?

Built with:React, TypeScript, Vite, NVIDIA AI, nostalgia, and KiroTime saved:Probably weeksBeveled buttons created:Too many to countStick figures drawn:Countless

# MS Paint Clone - Architecture Diagram

┌─────────────────────────────────────────────────────────────────────────────────┐
│ FRONTEND │
│ React 19.2 + TypeScript + Vite │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ USER INTERFACE LAYER │
├─────────────────────────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │
│ │ TitleBar │ │ MenuBar │ │ ThemeToggle │ │ StatusBar │ │
│ │ Component │ │ Component │ │ Component │ │ Component │ │
│ └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘ │
│ │
│ ┌────────────────────────────────────────────────────────────────────┐ │
│ │ App.tsx (Root) │ │
│ │ ┌──────────────────────────────────────────────────────────────┐ │ │
│ │ │ State Management: │ │ │
│ │ │ • selectedTool, selectedColor, theme │ │ │
│ │ │ • isChatbotOpen, isGeneratingImage │ │ │
│ │ │ • mousePos, canvasSize, showTour │ │ │
│ │ └──────────────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ DRAWING COMPONENTS │
├─────────────────────────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────────────┐ ┌─────────────────────────────────────┐ │
│ │ Toolbar │ │ Canvas.tsx │ │
│ │ Component │ │ ┌───────────────────────────────┐ │ │
│ │ │ │ │ HTML5 Canvas API │ │ │
│ │ 16 Tools: │────────▶│ │ • Drawing Context │ │ │
│ │ • Pencil │ │ │ • Mouse Event Handlers │ │ │
│ │ • Brush │ │ │ • Tool Implementations │ │ │
│ │ • Airbrush │ │ └───────────────────────────────┘ │ │
│ │ • Eraser │ │ │ │
│ │ • Fill Bucket │ │ Exposed Methods (via ref): │ │
│ │ • Line │ │ • clear() │ │
│ │ • Rectangle │ │ • getCanvasImage() │ │
│ │ • Ellipse │ │ • drawImageOnCanvas() │ │
│ │ • etc... │ │ │ │
│ └──────────────────┘ └─────────────────────────────────────┘ │
│ │
│ ┌──────────────────┐ │
│ │ ColorPalette │ │
│ │ Component │ │
│ │ │ │
│ │ 28 Colors: │ │
│ │ 14×2 Grid │ │
│ └──────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ AI COMPONENTS │
├─────────────────────────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────────────┐ ┌─────────────────────────────────────┐ │
│ │ ChatbotWidget │ │ ChatbotPopup.tsx │ │
│ │ Component │────────▶│ ┌───────────────────────────────┐ │ │
│ │ │ │ │ Command Detection: │ │ │
│ │ 💬 Button │ │ │ • isDrawCommand() │ │ │
│ │ (Bottom-right) │ │ │ • isDrawingRelatedQuestion() │ │ │
│ └──────────────────┘ │ └───────────────────────────────┘ │ │
│ │ │ │
│ │ Message History: │ │
│ │ • User messages │ │
│ │ • Bot responses (streaming) │ │
│ │ • System notifications │ │
│ └─────────────────────────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────────────────────────┘

 │
 │ HTTP Requests
 ▼

┌─────────────────────────────────────────────────────────────────────────────────┐
│ BACKEND │
│ Express.js 5.1 + Node.js │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ API ENDPOINTS │
├─────────────────────────────────────────────────────────────────────────────────┤
│ │
│ ┌────────────────────────────────────────────────────────────────┐ │
│ │ POST /api/chat │ │
│ │ ┌──────────────────────────────────────────────────────────┐ │ │
│ │ │ Input: │ │ │
│ │ │ • messages: Array<{role, content}> │ │ │
│ │ │ • image?: base64 PNG (optional) │ │ │
│ │ │ │ │ │
│ │ │ Logic: │ │ │
│ │ │ • Detect if image present │ │ │
│ │ │ • Select model (vision vs text) │ │ │
│ │ │ • Format multi-modal message if needed │ │ │
│ │ │ • Stream response via SSE │ │ │
│ │ │ │ │ │
│ │ │ Output: Server-Sent Events (streaming text) │ │ │
│ │ └──────────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────────────┘ │
│ │
│ ┌────────────────────────────────────────────────────────────────┐ │
│ │ POST /api/generate-image │ │
│ │ ┌──────────────────────────────────────────────────────────┐ │ │
│ │ │ Input: │ │ │
│ │ │ • prompt: string │ │ │
│ │ │ │ │ │
│ │ │ Logic: │ │ │
│ │ │ • Validate prompt │ │ │
│ │ │ • Call NVIDIA SDXL API │ │ │
│ │ │ • Extract base64 image │ │ │
│ │ │ • Return to frontend │ │ │
│ │ │ │ │ │
│ │ │ Output: { image: base64_png } │ │ │
│ │ └──────────────────────────────────────────────────────────┘ │ │
│ └────────────────────────────────────────────────────────────────┘ │
│ │
│ ┌────────────────────────────────────────────────────────────────┐ │
│ │ Middleware: │ │
│ │ • CORS (allow frontend origin) │ │
│ │ • express.json() (parse JSON bodies) │ │
│ │ • Error handling │ │
│ └────────────────────────────────────────────────────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────────────────────────┘

 │
 │ HTTPS + Bearer Token
 ▼

┌─────────────────────────────────────────────────────────────────────────────────┐
│ NVIDIA API PLATFORM │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ AI MODELS │
├─────────────────────────────────────────────────────────────────────────────────┤
│ │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ meta/llama-3.2-11b-vision-instruct │ │
│ │ ┌────────────────────────────────────────────────────────┐ │ │
│ │ │ Purpose: Artwork analysis & vision tasks │ │ │
│ │ │ Input: Text + Image (multi-modal) │ │ │
│ │ │ Output: Streaming text response │ │ │
│ │ │ Speed: 2-5 seconds │ │ │
│ │ └────────────────────────────────────────────────────────┘ │ │
│ └──────────────────────────────────────────────────────────────┘ │
│ │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ openai/gpt-oss-120b │ │
│ │ ┌────────────────────────────────────────────────────────┐ │ │
│ │ │ Purpose: Text chat & general assistance │ │ │
│ │ │ Input: Text messages only │ │ │
│ │ │ Output: Streaming text response │ │ │
│ │ │ Speed: 1-3 seconds │ │ │
│ │ └────────────────────────────────────────────────────────┘ │ │
│ └──────────────────────────────────────────────────────────────┘ │
│ │
│ ┌──────────────────────────────────────────────────────────────┐ │
│ │ stabilityai/stable-diffusion-xl │ │
│ │ ┌────────────────────────────────────────────────────────┐ │ │
│ │ │ Purpose: Text-to-image generation │ │ │
│ │ │ Input: Text prompt + parameters │ │ │
│ │ │ Output: 1024×1024 PNG (base64) │ │ │
│ │ │ Speed: 10-30 seconds │ │ │
│ │ │ Parameters: │ │ │
│ │ │ • cfg_scale: 7 │ │ │
│ │ │ • steps: 30 │ │ │
│ │ │ • seed: 0 (random) │ │ │
│ │ └────────────────────────────────────────────────────────┘ │ │
│ └──────────────────────────────────────────────────────────────┘ │
│ │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ DATA FLOW EXAMPLES │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ TEXT-TO-IMAGE GENERATION FLOW │
├─────────────────────────────────────────────────────────────────────────────────┤
│ │
│ User types "draw a cat" │
│ │ │
│ ▼ │
│ ChatbotPopup.isDrawCommand() → { isDraw: true, prompt: "a cat" } │
│ │ │
│ ▼ │
│ App.handleGenerateImage("a cat") │
│ │ │
│ ▼ │
│ POST /api/generate-image { prompt: "a cat" } │
│ │ │
│ ▼ │
│ Server → NVIDIA SDXL API │
│ │ │
│ ▼ │
│ NVIDIA generates 1024×1024 PNG (10-30s) │
│ │ │
│ ▼ │
│ Server returns { image: "base64..." } │
│ │ │
│ ▼ │
│ Canvas.drawImageOnCanvas(base64) │
│ │ │
│ ▼ │
│ Image scaled to 80% canvas width, centered, drawn as pixels │
│ │ │
│ ▼ │
│ User can now edit with any tool │
│ │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ VISION ANALYSIS FLOW │
├─────────────────────────────────────────────────────────────────────────────────┤
│ │
│ User draws something │
│ │ │
│ ▼ │
│ User types "what do you think?" │
│ │ │
│ ▼ │
│ ChatbotPopup.isDrawingRelatedQuestion() → true │
│ │ │
│ ▼ │
│ Canvas.getCanvasImage() → base64 PNG │
│ │ │
│ ▼ │
│ POST /api/chat { messages: [...], image: "base64..." } │
│ │ │
│ ▼ │
│ Server formats multi-modal message: │
│ { role: "user", content: [ │
│ { type: "text", text: "what do you think?" }, │
│ { type: "image_url", image_url: { url: "data:image/png;base64,..." } } │
│ ]} │
│ │ │
│ ▼ │
│ Server → NVIDIA Vision API (Llama 3.2 Vision) │
│ │ │
│ ▼ │
│ NVIDIA analyzes image (2-5s) │
│ │ │
│ ▼ │
│ Server streams SSE chunks │
│ │ │
│ ▼ │
│ Frontend parses chunks, updates UI in real-time │
│ │ │
│ ▼ │
│ User sees critique: "I can see you've drawn..." │
│ │
└─────────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────────┐
│ TECHNOLOGY STACK SUMMARY │
└─────────────────────────────────────────────────────────────────────────────────┘

Frontend: Backend: AI/ML:
• React 19.2 • Express.js 5.1 • NVIDIA API Platform
• TypeScript 5.9 • Node.js • Llama 3.2 Vision (11B)
• Vite 7.2 • CORS • GPT-OSS (120B)
• HTML5 Canvas API • dotenv • Stable Diffusion XL
• Pure CSS (no frameworks)

Testing: Code Quality: Dev Tools:
• Vitest 4.0 • ESLint 9.39 • concurrently
• React Testing Library • TypeScript ESLint • Vite dev server
• fast-check 4.3 • React Hooks rules • Hot reload
• jsdom 27.2

Enter fullscreen mode

Exit fullscreen mode

Now if you'll excuse me, I'm going to ask my AI to analyze a drawing of a stick figure riding a dinosaur.

🎨✨

P.S. - The AI genuinely told me my stick figure "showed good use of negative space." I'm framing that feedback.

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

For further actions, you may consider blocking this person and/orreporting abuse
