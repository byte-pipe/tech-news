---
title: 'Frontend to Backend: From Vite to Express❗ - DEV Community'
url: https://dev.to/cristea_theodora_6200140b/frontend-to-backend-from-vite-to-express-2c83
site_name: devto
fetched_at: '2025-11-04T19:08:21.366422'
original_url: https://dev.to/cristea_theodora_6200140b/frontend-to-backend-from-vite-to-express-2c83
author: Theodora Cristea
date: '2025-10-28'
description: Intro Hey everyone!🤗 If you're a beginner who's just started learning the backend, or... Tagged with node, backend, beginners, express.
tags: '#node, #backend, #beginners, #express'
---

# Intro

Hey everyone!🤗 If you're a beginner who'sjust startedlearning the backend, or maybe youalready knowthe basics but want a deeper understanding of the logicbehind servers, routing requests and all those fundamentals concepts, I truly hope this articlehelps youout.🥰

It'stotally normalto feel confused at first or not tograspeverything immediatly, you'll figure it out eventually at the right time! Perhaps this article willclarify things, or maybe it will just confirm what you already know!

We will discuss the following concepts:

1. Routing:Frontend vs Backend
2. FromSourcetoServer
3. Development vs Production: More Than Just a Command
4. Order Matters: HandlingCritical Pathsin Express

# Routing: Frontent vs Backend

Routing means deciding whichpiece of codeorwhich pageto return when a user accesses a specificURL(a path, or "route"). Here lies the firstmajor differencebetween the two worlds.

### Frontend Routing (Vite, React Router)

When we work with a modern frontend framework (like React with Vite or Create React App), we don't handle the routing of static files:

→The Dev Server is Smart: Vite's development server is designed to do one thing: help us code fast. It knows how to read our source files (those insrc/) and serve them automatically under the corresponding URLs.

→Automatic Routing: If our HTML or React code refers to/styles/main.css, the Vite serverknowsimmediatelywhereto find the physical file (in its memory or the file system) andsendsit instantly to thebrowser. We don't write special code for this❗

→Focus on Application Logic: Using libraries like React Router, we only focus on the application logic (e.g., "If the URL is/profile, display the Profile component"). This routing happens in the browser, after the JavaScript files have been loaded.

### Manual Routing in the Backend (Express.js)

Express.js is just a minimal framework. It makes no assumptions and has no built-in "magic."

→Routing is Manual: Once we put Express.js in charge as the main server, we must explicitly tell it what to do for every request that reaches it.

Do we want thePOST/api/loginrequest to verify the password in the database❓ We must writeapp.post('/api/login',...).

Do we want theGET/api/usersrequest to return a list of users❓ We must writeapp.get('/api/users', ...).

→Ignorance of Static Files: Without instructions, if it receives a request for/main.css, Expressdoesn't know this is a static file. It will look for an API route or rendering logic. Since itdoesn't find one, it implicitly returns404 Not Found.

When starting out, the Vite Development Server performssilent magic,it's automatically handling all the routingand serving of our static files (like CSS and images) directlyfrom memory.

However, when we introduce Express.js,the magic stops. Express is ignorant and requiresexplicit instructions. We mustmanuallydefine our API routes (app.get('/api/data')) and, most importantly, wemust useexpress.static()to manually tell Express: "This is where you can findall the static files you needfor the web page." Without this manual step, our CSS and JavaScript files will beinvisible to the server, resulting in broken pages❗

# From Source to Server

### Static Files in Development:

During development, when we runnpm run devin our React project:

→No Physical Folder: The Vite server reads our files (.jsx,.css) directly from thesrc/directory andkeeps themin RAM (memory). It does not create a physical folder with compiled files.

→Speed: Any change we save is instantly transmitted to thebrowser via HMR(Hot Module Reloading), making the coding experience fluid.

→Not Production Ready: Although fast, this mode is notstable,secure, oroptimizedto be accessed by thousands of real users on the internet.

### From src to dist:

When and Why Do We Compile❓ Before publishing the application (moving to Production), we must compile the code:

→The Command:npm run build.→Optimization: This command takes all our source files (React,CSS, etc.),minifiesthem (makes them much smaller),concatenatesthem (puts them into fewer bundles), andoptimizesthem for maximum loading speed.

→The Resultdist: All these optimized files are put into a new, physical folder, usually calleddistorbuild. This folder contains the final,static version of the frontend, ready to be served.

### Enterexpress.static():

→How Do We Serve the dist Folder❓ Now that we have theoptimized dist folder, we must tell Express (the backend) thatthis is the folderit needs to serve publicly:

→The Solution isexpress.static(): This line of code is the instruction we give the Express server:

// in production, Express serves the frontend's 'dist' folder

app
.
use
(
express
.
static
(
path
.
join
(
__dirname
,

'
client/dist
'
)));

Enter fullscreen mode

Exit fullscreen mode

→What It Does: Whenever an HTTP requestreaches the serverand doesnot match an API routewe defined (e.g. doesn't start with/api), Express looks in thedist folder! If it finds a file matching the requested URL (e.g.,/style.css), it sends it immediately to theclientand stops the routing process❗

# Development vs Production:

→ If we have seen the commandnpm run devused in both ourfrontend(React) and ourbackend(Express) project directories, we might think they do the same thing.They don't❗ This is acritical distinction, especially when thinking aboutsecurityandperformance.

→The Dualnpm run dev: Two Servers, Two Purposes

When we talk aboutDevelopment Mode(Dev) andProduction Mode(Prod), we are describing thestateandpurposeof our running code.

## Development Mode (our workbench):

Development Mode is ourworkbench, it's optimized for speed and debugging.

→Purpose: the sole goal is to facilitaterapid coding,testing, anddebugging.→Frontend Setup: the server runs theVite Dev Serveron one port (e.g.,5173).→Backend Tooling: we use tools likenodemonto automaticallyrestartthe server the moment we save a change.→Errors: errors are loud and detailed (stack traces) and are printed directly to your console, helping youfix issuesinstantly.→Optimization: files are served as-is, withminimal optimization, as file size and speed aren't the primary concerns.

## Production Mode (the live public server)

Production Mode is the final, optimized version delivered to the public, it's built forstabilityandsecurity.

→Purpose: the goal is to deliver a stable,fast, andsecureexperience to the public.→Frontend Setup: the frontend code is firstbuilt(compiled and minified) and then served by the singleExpress serveron its designated port (e.g.,3000).→Backend Tooling: we usehighlyoptimized process managers (like PM2) to keep the server running continuously and robustly.→Errors: errors are loggedinternallybut are never shown to thepublic user, preventing security leaks❗→Optimization: files are heavily minified and aggressively cached formaximum performanceandfaster loadingtimes for all users.

## Security Risks:

Why we don't run development mode in production❓Running your Express server in Development Mode on a live, public server is amajor security flawand isstrongly discouraged.

→Security Leaks: Development errors often includesensitive data, such as file paths on your server,environment variables, or evenglimpsesinto your database structure. Revealing this information to an attacker is asevere vulnerability❗

→Performance: Dev mode is built forconvenience, not speed. You will experience slowresponse times, poorresourcemanagement, and limitedscalabilityunder real user load.

→Stability: Tools likenodemonare meant torestartyour code whenever you save a change. This behavior is unpredictable andhighly unstablefor a public-facing application that needs to run 24/7❗

# Order Matters: Handling Critical Paths in Express

Now, let's look at the crucial process ofsetting upour routes andmiddlewarein the correct order to ensure Express handles all requests correctly.

### The Role of Middleware: app.use()

In Express, a Middleware is simply a function that executes during therequest-responsecycle. It has access to therequestobjectreq, theresponseobjectres, and thenextfunctionnextin the cycle.

→app.use(middleware): This method is primarily used to register middleware. It executes the provided function for ALLHTTPmethods (GET,POST, etc.) and for ALLpaths(unless we specify a path prefix).

→The Golden Rule: Middleware executes in theexact orderthey are defined in our code. Once a middleware sends aresponse(e.g.,res.send('Hello')), the cycle stops, and no subsequentmiddlewareorroutehandlers are executed❗

Example Order of Flow:

1. app.use(cors)
2. app.use(express.json)
3. app.use('/api', apiRouter)
4. app.use(express.static(dist_path))<- This is the critical separation point❗
5. ... other routes ...

### The React Router Trap:

Why We Needapp.get('*')❓This is the finalpieceof the puzzle that links ourbackendlogic to ourfrontendapplication.

→The Purpose: theapp.get('*')route is theCatch-AllHandler. It uses the wildcard*to matchanyGETrequestthathasn'tbeen handled by any middleware or route defined before it.

→The Scenario: when a user types a direct link likemysite.com/profileinto their browser, the server sees a request for/profile.

1. ExpresscheckstheAPIroutes (e.g.,/api). No match❗
2. Expresschecksexpress.static()for a file named profile. No match.❗
3. The requestfallstoapp.get('*').

→The Solution: we tell Express to simply serve the main application file (index.html) forany unmatchedpath.

app
.
get
(
'
*
'
,

(
req
,

res
)

=>

{


// we tell Express: "Send the HTML file and let React Router handle the URL."


res
.
sendFile
(
path
.
resolve
(
FRONTEND_BUILD_PATH
,

'
index.html
'
));

});

Enter fullscreen mode

Exit fullscreen mode

→Result: The browser loadsindex.html, React takes over, and React Router reads the/profileURL anddisplays the correct component, making the single-page application experience seamless❗

# Conclusion❤️

If you’re a beginner in backend development and these things didn’t make sense right away, don’t be disappointed, they can definitely beconfusing at first. I think we’ve all had these questions when we werejust startingout... I know I sure did❗ 🙃

The main challenge is that we need toshift our mindsetand thewaywe think, from theautomatic, in-memory serving of a frontend tool like Vite, to themore manualandstructured routingapproach of Express.

I hope this articlehelps you out, or maybe reminds you of the struggles you faced at thebeginningof your backend journey.🤗I’m really curious how many of us have gone through the sameconfusion at first, leave me a comment if backend development gave you ahard time too! I’d love to know I wasn’t the only one.🤗🥰

Happy reading, and if this articlehelped youor you found ituseful, give it a reaction!🤗

More articles:Node.js-Steps for building your first server❗My First Node.js: Mastering the Fundamentals❗

 Create template


Templates let you quickly answer FAQs or store snippets for re-use.

Submit

Preview

Dismiss

 View full discussion (45 comments)


Some comments may only be visible to logged-in visitors.Sign into view all comments.

For further actions, you may consider blocking this person and/orreporting abuse
