---
title: 'GitHub - calcom/cal.diy: Scheduling infrastructure for absolutely everyone. · GitHub'
url: https://github.com/calcom/cal.diy
site_name: github
content_file: github-github-calcomcaldiy-scheduling-infrastructure-for
fetched_at: '2026-05-17T11:28:26.129101'
original_url: https://github.com/calcom/cal.diy
author: calcom
description: Scheduling infrastructure for absolutely everyone. - calcom/cal.diy
---

calcom

 

/

cal.diy

Public

* NotificationsYou must be signed in to change notification settings
* Fork13.4k
* Star43k

 
 
 
 
main
Branches
Tags
Go to file
Code
Open more actions menu

## Folders and files

Name
Name
Last commit message
Last commit date

## Latest commit

 

## History

16,438 Commits
16,438 Commits
.changeset
.changeset
 
 
.claude
.claude
 
 
.cursor
.cursor
 
 
.github
.github
 
 
.husky
.husky
 
 
.opencode/
skill
.opencode/
skill
 
 
.snaplet
.snaplet
 
 
.vscode
.vscode
 
 
.well-known
.well-known
 
 
.yarn
.yarn
 
 
__checks__
__checks__
 
 
agents
agents
 
 
apps
apps
 
 
deploy
deploy
 
 
docs/
api-reference/
v2
docs/
api-reference/
v2
 
 
example-apps/
credential-sync
example-apps/
credential-sync
 
 
packages
packages
 
 
scripts
scripts
 
 
specs
specs
 
 
vitest-mocks
vitest-mocks
 
 
.dockerignore
.dockerignore
 
 
.editorconfig
.editorconfig
 
 
.env.appStore.example
.env.appStore.example
 
 
.env.example
.env.example
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.gitpod.yml
.gitpod.yml
 
 
.kodiak.toml
.kodiak.toml
 
 
.npmrc
.npmrc
 
 
.yarnrc.yml
.yarnrc.yml
 
 
AGENTS.md
AGENTS.md
 
 
CLAUDE.md
CLAUDE.md
 
 
CODE_OF_CONDUCT.md
CODE_OF_CONDUCT.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
PERMISSIONS.md
PERMISSIONS.md
 
 
Procfile
Procfile
 
 
README.md
README.md
 
 
SECURITY.md
SECURITY.md
 
 
SPEC-WORKFLOW.md
SPEC-WORKFLOW.md
 
 
app.json
app.json
 
 
biome-staged.json
biome-staged.json
 
 
biome.json
biome.json
 
 
checkly.config.ts
checkly.config.ts
 
 
docker-compose.yml
docker-compose.yml
 
 
gh.env
gh.env
 
 
headless-routing-to-booking-flow.md
headless-routing-to-booking-flow.md
 
 
i18n-unused.config.js
i18n-unused.config.js
 
 
i18n.json
i18n.json
 
 
i18n.lock
i18n.lock
 
 
lint-staged.config.mjs
lint-staged.config.mjs
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
setupVitest.ts
setupVitest.ts
 
 
turbo.json
turbo.json
 
 
vitest.config.mts
vitest.config.mts
 
 
vitest.workspace.ts
vitest.workspace.ts
 
 
yarn.lock
yarn.lock
 
 
View all files

## Repository files navigation

Warning

Use at your own risk. Cal.diy is the open source community edition of Cal.com and it is intended for users who want to self-host their own Cal.diy instance. It is strictly recommended for personal, non-production use. Please review all installation and configuration steps carefully. Self-hosting requires advanced knowledge of server administration, database management, and securing sensitive data. Proceed only if you are comfortable with these responsibilities.

Tip

For any commercial and enterprise-ready scheduling infrastructure, use Cal.com, not Cal.diy; hosted by us or get invited to on-prem enterprise access here:https://cal.com/sales

### Cal.diy

The community-driven, open-source scheduling platform.GitHubDiscussions·Issues·Contributing

## About Cal.diy

Cal.diyis the community-driven, fully open-source scheduling platform — a fork ofCal.comwith all enterprise/commercial code removed.

Cal.diy is100% MIT-licensedwith no proprietary "Enterprise Edition" features. It's designed for individuals and self-hosters who want full control over their scheduling infrastructure without any commercial dependencies.

### What's different from Cal.com?

* No enterprise features— Teams, Organizations, Insights, Workflows, SSO/SAML, and other EE-only features have been removed
* No license key required— Everything works out of the box, no Cal.com account or license needed
* 100% open source— The entire codebase is licensed under MIT, no "Open Core" split
* Community-maintained— Contributions are welcome and go directly into this project (seeCONTRIBUTING.md)

Note:Cal.diy is a self-hosted project. There is no hosted/managed version. You run it on your own infrastructure.

### Built With

* Next.js
* tRPC
* React.js
* Tailwind CSS
* Prisma.io
* Daily.co

## Getting Started

To get a local copy up and running, please follow these simple steps.

### Prerequisites

Here’s what you need to run Cal.diy.

* Node.js (Version: >=18.x)
* PostgreSQL (Version: >=13.x)
* Yarn(recommended)

If you want to enable any of the available integrations, you may want to obtain additional credentials for each one. More details on this can be found below under theintegrations section.

## Development

### Setup

1. Clone the repo (or forkhttps://github.com/calcom/cal.diy/fork)git clone https://github.com/calcom/cal.diy.gitIf you are on Windows, run the following command in Git Bash with admin privileges:git clone -c core.symlinks=true https://github.com/calcom/cal.diy.git
2. Go to the project foldercdcal.diy
3. Install packages with yarnyarn
4. Set up your.envfile* Duplicate.env.exampleto.env
* Useopenssl rand -base64 32to generate a key and add it underNEXTAUTH_SECRETin the.envfile.
* Useopenssl rand -base64 24to generate a key and add it underCALENDSO_ENCRYPTION_KEYin the.envfile.

Windows users:Replace thepackages/prisma/.envsymlink with a real copy to avoid a Prisma error (unexpected character / in variable name):

#
 Git Bash / WSL

rm packages/prisma/.env 
&&
 cp .env packages/prisma/.env

1. Set up Node
If your Node version does not meet the project's requirements as instructed by the docs, "nvm" (Node Version Manager) allows using Node at the version required by the project:nvm useYou first might need to install the specific version and then use it:nvm install&&nvm useYou can install nvm fromhere.

#### Quick start withyarn dx

* Requires Docker and Docker Compose to be installed
* Will start a local Postgres instance with a few test users - the credentials will be logged in the console

yarn dx

Default credentials created:

Email

Password

Role

free@example.com

free

Free user

pro@example.com

pro

Pro user

trial@example.com

trial

Trial user

admin@example.com

ADMINadmin2022!

Admin user

onboarding@example.com

onboarding

Onboarding incomplete

You can use any of these credentials to sign in athttp://localhost:3000

Tip: To view the full list of seeded users and their details, runyarn db-studioand visithttp://localhost:5555

#### Development tip

1. Addexport NODE_OPTIONS="--max-old-space-size=16384"to your shell script to increase the memory limit for the node process. Alternatively, you can run this in your terminal before running the app. Replace 16384 with the amount of RAM you want to allocate to the node process.
2. AddNEXT_PUBLIC_LOGGER_LEVEL={level}to your .env file to control the logging verbosity for all tRPC queries and mutations.Where {level} can be one of the following:0for silly1for trace2for debug3for info4for warn5for error6for fatalWhen you setNEXT_PUBLIC_LOGGER_LEVEL={level}in your .env file, it enables logging at that level and higher. Here's how it works:The logger will include all logs that are at the specified level or higher. For example: \* If you setNEXT_PUBLIC_LOGGER_LEVEL=2, it will log from level 2 (debug) upwards, meaning levels 2 (debug), 3 (info), 4 (warn), 5 (error), and 6 (fatal) will be logged. \
* If you setNEXT_PUBLIC_LOGGER_LEVEL=3, it will log from level 3 (info) upwards, meaning levels 3 (info), 4 (warn), 5 (error), and 6 (fatal) will be logged, but level 2 (debug) and level 1 (trace) will be ignored. \

echo
 
'
NEXT_PUBLIC_LOGGER_LEVEL=3
'
 
>>
 .env

for Logger level to be set at info, for example.

#### Gitpod Setup

1. Click the button below to open this project in Gitpod.
2. This will open a fully configured workspace in your browser with all the necessary dependencies already installed.

#### Manual setup

1. Configure environment variables in the.envfile. Replace<user>,<pass>,<db-host>, and<db-port>with their applicable valuesDATABASE_URL='postgresql://<user>:<pass>@<db-host>:<db-port>'If you don't know how to configure the DATABASE_URL, then follow the steps here to create a quick local DBDownloadand install PostgreSQL locally (if you don't have it already).Create your own local db by executingcreateDB <DB name>Now open your psql shell with the DB you created:psql -h localhost -U postgres -d <DB name>Inside the psql shell execute\conninfo. And you will get the following info.Now extract all the info and add it to your DATABASE_URL. The url would look something like thispostgresql://postgres:postgres@localhost:5432/Your-DB-Name. The port is configurable and does not have to be 5432.If you don't want to create a local DB. Then you can also consider using services like railway.app, Northflank or render.* Setup postgres DB with railway.app
* Setup postgres DB with Northflank
* Setup postgres DB with render
2. Downloadand install PostgreSQL locally (if you don't have it already).
3. Create your own local db by executingcreateDB <DB name>
4. Now open your psql shell with the DB you created:psql -h localhost -U postgres -d <DB name>
5. Inside the psql shell execute\conninfo. And you will get the following info.
6. Now extract all the info and add it to your DATABASE_URL. The url would look something like thispostgresql://postgres:postgres@localhost:5432/Your-DB-Name. The port is configurable and does not have to be 5432.
7. Copy and paste yourDATABASE_URLfrom.envto.env.appStore.
8. Set up the database using the Prisma schema (found inpackages/prisma/schema.prisma)In a development environment, run:yarn workspace @calcom/prisma db-migrateIn a production environment, run:yarn workspace @calcom/prisma db-deploy
9. Runmailhogto view emails sent during developmentNOTE:Required whenE2E_TEST_MAILHOG_ENABLEDis "1"docker pull mailhog/mailhog
docker run -d -p 8025:8025 -p 1025:1025 mailhog/mailhog
10. Run (in development mode)yarn dev

#### Setting up your first user

##### Approach 1

1. OpenPrisma Studioto look at or modify the database content:yarn db-studio
2. Click on theUsermodel to add a new user record.
3. Fill out the fieldsemail,username,password, and setmetadatato empty{}(remembering to encrypt your password withBCrypt) and clickSave 1 Recordto create your first user.New users are set on aTRIALplan by default. You might want to adjust this behavior to your needs in thepackages/prisma/schema.prismafile.
4. Open a browser tohttp://localhost:3000and login with your just created, first user.

##### Approach 2

Seed the local db by running

cd
 packages/prisma
yarn db-seed

The above command will populate the local db with dummy users.

### E2E-Testing

Be sure to set the environment variableNEXTAUTH_URLto the correct value. If you are running locally, as the documentation within.env.examplementions, the value should behttp://localhost:3000.

#
 In a terminal just run:

yarn test-e2e

#
 To open the last HTML report run:

yarn playwright show-report test-results/reports/playwright-html-report

#### Resolving issues

##### E2E test browsers not installed

Runnpx playwright installto download test browsers and resolve the error below when runningyarn test-e2e:

Executable doesn't exist at /Users/alice/Library/Caches/ms-playwright/chromium-1048/chrome-mac/Chromium.app/Contents/MacOS/Chromium

### Upgrading from earlier versions

1. Pull the current version:git pull
2. Check if dependencies got added/updated/removedyarn
3. Apply database migrations by runningone ofthe following commands:In a development environment, run:yarn workspace @calcom/prisma db-migrate(This can clear your development database in some cases)In a production environment, run:yarn workspace @calcom/prisma db-deploy
4. Check for.envvariables changesyarn predev
5. Start the server. In a development environment, just do:yarn devFor a production build, run for example:yarn build
yarn start
6. Enjoy the new version.

## Deployment

### Docker

The Docker image can be found on DockerHub athttps://hub.docker.com/r/calcom/cal.diy.

Note for ARM Users: Use the {version}-arm suffix for pulling images. Example:docker pull calcom/cal.diy:v5.6.19-arm.

#### Requirements

Make sure you havedocker&docker composeinstalled on the server / system. Both are installed by most docker utilities, including Docker Desktop and Rancher Desktop.

Note:docker composewithout the hyphen is now the primary method of using docker-compose, per the Docker documentation.

#### Running Cal.diy with Docker Compose

1. Clone the repositorygit clone --recursive https://github.com/calcom/cal.diy.git
2. Change into the directorycdcal.diy
3. Prepare your configuration: Rename.env.exampleto.envand then update.envcp .env.example .envMost configurations can be left as-is, but for configuration options seeImportant Run-time variablesbelow.Required Secret KeysBefore starting, you must generate secure values forNEXTAUTH_SECRETandCALENDSO_ENCRYPTION_KEY. Using the defaultsecretplaceholder in production is a security risk.GenerateNEXTAUTH_SECRET(cookie encryption key):openssl rand -base64 32GenerateCALENDSO_ENCRYPTION_KEY(must be 32 bytes for AES256):openssl rand -base64 24Update your.envfile with these values:NEXTAUTH_SECRET=<your_generated_secret>CALENDSO_ENCRYPTION_KEY=<your_generated_key>Push Notifications (VAPID Keys)If you see an error like:Error: No key set vapidDetails.publicKeyThis means your environment variables for Web Push are missing.
You must generate and setNEXT_PUBLIC_VAPID_PUBLIC_KEYandVAPID_PRIVATE_KEY.Generate them with:npx web-push generate-vapid-keysThen update your.envfile:NEXT_PUBLIC_VAPID_PUBLIC_KEY=your_public_key_hereVAPID_PRIVATE_KEY=your_private_key_hereDonotcommit real keys to.env.example— only placeholders.Update the appropriate values in your .env file, then proceed.
4. (optional) Pre-Pull the images by running the following command:docker compose pull
5. Start Cal.diy via docker composeTo run the complete stack, which includes a local Postgres database, Cal.diy web app, and Prisma Studio:docker compose up -dTo run Cal.diy web app and Prisma Studio against a remote database, ensure that DATABASE_URL is configured for an available database and run:docker compose up -d calcom studioTo run only the Cal.diy web app, ensure that DATABASE_URL is configured for an available database and run:docker compose up -d calcomNote: to run in attached mode for debugging, remove-dfrom your desired run command.
6. Open a browser tohttp://localhost:3000, or your defined NEXT_PUBLIC_WEBAPP_URL. The first time you run Cal.diy, a setup wizard will initialize. Define your first user, and you're ready to go!Note for first-time setup (Calendar integration): During the setup wizard, you may encounter a "Connect your Calendar" step that appears to be required. If you do not wish to connect a calendar at this time, you can skip this step by navigating directly to the dashboard at<NEXT_PUBLIC_WEBAPP_URL>/event-types. Calendar integrations can be added later from the Settings > Integrations page.

#### Updating Cal.diy

1. Stop the Cal.diy stackdocker compose down
2. Pull the latest changesdocker compose pull
3. Update env vars as necessary.
4. Re-start the Cal.diy stackdocker compose up -d

#### Building from source with Docker

1. Clone the repositorygit clone https://github.com/calcom/cal.diy.git
2. Change into the directorycdcal.diy
3. Rename.env.exampleto.envand then update.envFor configuration options seeBuild-time variablesbelow. Update the appropriate values in your .env file, then proceed.
4. Build the Cal.diy docker image:Note: Due to application configuration requirements, an available database is currently required during the build process.a) If hosting elsewhere, configure theDATABASE_URLin the .env file, and skip the next stepb) If a local or temporary database is required, start a local database via docker compose.docker compose up -d database
5. Build Cal.diy via docker compose (DOCKER_BUILDKIT=0 must be provided to allow a network bridge to be used at build time. This requirement will be removed in the future)DOCKER_BUILDKIT=0 docker compose build calcom
6. Start Cal.diy via docker composeTo run the complete stack, which includes a local Postgres database, Cal.diy web app, and Prisma Studio:docker compose up -dTo run Cal.diy web app and Prisma Studio against a remote database, ensure that DATABASE_URL is configured for an available database and run:docker compose up -d calcom studioTo run only the Cal.diy web app, ensure that DATABASE_URL is configured for an available database and run:docker compose up -d calcomNote: to run in attached mode for debugging, remove-dfrom your desired run command.
7. Open a browser tohttp://localhost:3000, or your defined NEXT_PUBLIC_WEBAPP_URL. The first time you run Cal.diy, a setup wizard will initialize. Define your first user, and you're ready to go!

#### Configuration

##### Important Run-time variables

These variables must also be provided at runtime

Variable

Description

Required

Default

DATABASE_URL

database url with credentials - if using a connection pooler, this setting should point there

required

postgresql://unicorn_user:magical_password@database:5432/calendso

NEXT_PUBLIC_WEBAPP_URL

Base URL of the site. NOTE: if this value differs from the value used at build-time, there will be a slight delay during container start (to update the statically built files).

optional

http://localhost:3000

NEXTAUTH_URL

Location of the auth server. By default, this is the Cal.diy docker instance itself.

optional

{NEXT_PUBLIC_WEBAPP_URL}/api/auth

NEXTAUTH_SECRET

Cookie encryption key. Must match build variable. Generate with: 
openssl rand -base64 32

required

secret

CALENDSO_ENCRYPTION_KEY

Authentication encryption key (32 bytes for AES256). Must match build variable. Generate with: 
openssl rand -base64 24

required

secret

##### Build-time variables

If building the image yourself, these variables must be provided at the time of the docker build, and can be provided by updating the .env file. Currently, if you require changes to these variables, you must follow the instructions to build and publish your own image.

Variable

Description

Required

Default

DATABASE_URL

database url with credentials - if using a connection pooler, this setting should point there

required

postgresql://unicorn_user:magical_password@database:5432/calendso

MAX_OLD_SPACE_SIZE

Needed for Nodejs/NPM build options

required

4096

NEXTAUTH_SECRET

Cookie encryption key

required

secret

CALENDSO_ENCRYPTION_KEY

Authentication encryption key

required

secret

NEXT_PUBLIC_WEBAPP_URL

Base URL injected into static files

optional

http://localhost:3000

NEXT_PUBLIC_WEBSITE_TERMS_URL

custom URL for terms and conditions website

optional

NEXT_PUBLIC_WEBSITE_PRIVACY_POLICY_URL

custom URL for privacy policy website

optional

CALCOM_TELEMETRY_DISABLED

Allow Cal.diy to collect anonymous usage data (set to 
1
 to disable)

optional

#### Troubleshooting

##### SSL edge termination

If running behind a load balancer which handles SSL certificates, you will need to add the environmental variableNODE_TLS_REJECT_UNAUTHORIZED=0to prevent requests from being rejected. Only do this if you know what you are doing and trust the services/load-balancers directing traffic to your service.

##### Failed to commit changes: Invalid 'prisma.user.create()'

Certain versions may have trouble creating a user if the fieldmetadatais empty. Using an empty json object{}as the field value should resolve this issue. Also, theidfield will autoincrement, so you may also try leaving the value ofidas empty.

##### CLIENT_FETCH_ERROR

If you experience this error, it may be the way the default Auth callback in the server is using the WEBAPP_URL as a base url. The container does not necessarily have access to the same DNS as your local machine, and therefore needs to be configured to resolve to itself. You may be able to correct this by configuringNEXTAUTH_URL=http://localhost:3000/api/auth, to help the backend loop back to itself.

docker-calcom-1 | @calcom/web:start: [next-auth][error][CLIENT_FETCH_ERROR]
docker-calcom-1 | @calcom/web:start: https://next-auth.js.org/errors#client_fetch_error request to http://testing.localhost:3000/api/auth/session failed, reason: getaddrinfo ENOTFOUND testing.localhost {
docker-calcom-1 | @calcom/web:start: error: {
docker-calcom-1 | @calcom/web:start: message: 'request to http://testing.localhost:3000/api/auth/session failed, reason: getaddrinfo ENOTFOUND testing.localhost',
docker-calcom-1 | @calcom/web:start: stack: 'FetchError: request to http://testing.localhost:3000/api/auth/session failed, reason: getaddrinfo ENOTFOUND testing.localhost\n' +
docker-calcom-1 | @calcom/web:start: ' at ClientRequest.<anonymous> (/calcom/node_modules/next/dist/compiled/node-fetch/index.js:1:65756)\n' +
docker-calcom-1 | @calcom/web:start: ' at ClientRequest.emit (node:events:513:28)\n' +
docker-calcom-1 | @calcom/web:start: ' at ClientRequest.emit (node:domain:489:12)\n' +
docker-calcom-1 | @calcom/web:start: ' at Socket.socketErrorListener (node:_http_client:494:9)\n' +
docker-calcom-1 | @calcom/web:start: ' at Socket.emit (node:events:513:28)\n' +
docker-calcom-1 | @calcom/web:start: ' at Socket.emit (node:domain:489:12)\n' +
docker-calcom-1 | @calcom/web:start: ' at emitErrorNT (node:internal/streams/destroy:157:8)\n' +
docker-calcom-1 | @calcom/web:start: ' at emitErrorCloseNT (node:internal/streams/destroy:122:3)\n' +
docker-calcom-1 | @calcom/web:start: ' at processTicksAndRejections (node:internal/process/task_queues:83:21)',
docker-calcom-1 | @calcom/web:start: name: 'FetchError'
docker-calcom-1 | @calcom/web:start: },
docker-calcom-1 | @calcom/web:start: url: 'http://testing.localhost:3000/api/auth/session',
docker-calcom-1 | @calcom/web:start: message: 'request to http://testing.localhost:3000/api/auth/session failed, reason: getaddrinfo ENOTFOUND testing.localhost'
docker-calcom-1 | @calcom/web:start: }

### Railway

You can deploy Cal.diy onRailway. The team at Railway also have adetailed blog poston deploying on their platform.

### Northflank

You can deploy Cal.diy onNorthflank. The team at Northflank also have adetailed blog poston deploying on their platform.

### Vercel

Currently Vercel Pro Plan is required to be able to Deploy this application with Vercel, due to limitations on the number of serverless functions on the free plan.

### Render

### Elestio

## License

Cal.diy is fully open source, licensed under theMIT License.

Unlike Cal.com's "Open Core" model, Cal.diy hasno commercial/enterprise code. The entire codebase is available under the same open-source license.

## Enabling Content Security Policy

* Set CSP_POLICY="non-strict" env variable, which enablesStrict CSPexcept forunsafe-inlineinstyle-src. If you have custom changes in your instance, you may need to modify your code to make it CSP-compatible. Currently, strict CSP is enabled only on the login page. On other SSR pages, it is enabled in report-only mode to detect potential issues. It is not yet supported on SSG pages.

## Integrations

### Obtaining the Google API Credentials

1. OpenGoogle API Console. If you don't have a project in your Google Cloud subscription, you'll need to create one before proceeding further. Under Dashboard pane, select Enable APIS and Services.
2. In the search box, type calendar and select the Google Calendar API search result.
3. Enable the selected API.
4. Next, go to theOAuth consent screenfrom the side pane. Select the app type (Internal or External) and enter the basic app details on the first page.
5. In the second page on Scopes, select Add or Remove Scopes. Search for Calendar.event and select the scope with scope value.../auth/calendar.events,.../auth/calendar.readonlyand select Update.
6. In the third page (Test Users), add the Google account(s) you'll be using. Make sure the details are correct on the last page of the wizard and your consent screen will be configured.
7. Now selectCredentialsfrom the side pane and then select Create Credentials. Select the OAuth Client ID option.
8. Select Web Application as the Application Type.
9. Under Authorized redirect URI's, select Add URI and then add the URI<Cal.diy URL>/api/integrations/googlecalendar/callbackand<Cal.diy URL>/api/auth/callback/googlereplacing Cal.diy URL with the URI at which your application runs.
10. The key will be created and you will be redirected back to the Credentials page. Select the newly generated client ID under OAuth 2.0 Client IDs.
11. Select Download JSON. Copy the contents of this file and paste the entire JSON string in the.envfile as the value forGOOGLE_API_CREDENTIALSkey.

#### Adding google calendar to Cal.diy App Store

After adding Google credentials, you can now add the Google Calendar app to the App Store.
You can repopulate the App Store by running

cd packages/prisma
yarn seed-app-store

You will need to complete a few more steps to activate Google Calendar App.
Make sure to complete section "Obtaining the Google API Credentials". After that do the
following

1. Add extra redirect URL<Cal.diy URL>/api/auth/callback/google
2. Under 'OAuth consent screen', click "PUBLISH APP"

### Obtaining Microsoft Graph Client ID and Secret

1. OpenAzure App Registrationand select New registration
2. Name your application
3. SetWho can use this application or access this API?toAccounts in any organizational directory (Any Azure AD directory - Multitenant)
4. Set theWebredirect URI to<Cal.diy URL>/api/integrations/office365calendar/callbackreplacing Cal.diy URL with the URI at which your application runs.
5. UseApplication (client) IDas theMS_GRAPH_CLIENT_IDattribute value in .env
6. ClickCertificates & secretscreate a new client secret and use the value as theMS_GRAPH_CLIENT_SECRETattribute

### Obtaining Zoom Client ID and Secret

1. OpenZoom Marketplaceand sign in with your Zoom account.
2. On the upper right, click "Develop" => "Build App".
3. Select "General App" , click "Create".
4. Name your App.
5. Choose "User-managed app" for "Select how the app is managed".
6. De-select the option to publish the app on the Zoom App Marketplace, if asked.
7. Now copy the Client ID and Client Secret to your.envfile into theZOOM_CLIENT_IDandZOOM_CLIENT_SECRETfields.
8. Set the "OAuth Redirect URL" under "OAuth Information" as<Cal.diy URL>/api/integrations/zoomvideo/callbackreplacing Cal.diy URL with the URI at which your application runs.
9. Also add the redirect URL given above as an allow list URL and enable "Subdomain check". Make sure, it says "saved" below the form.
10. You don't need to provide basic information about your app. Instead click on "Scopes" and then on "+ Add Scopes". On the left,click the category "Meeting" and check the scopemeeting:write:meeting.click the category "User" and check the scopeuser:read:settings.
11. click the category "Meeting" and check the scopemeeting:write:meeting.
12. click the category "User" and check the scopeuser:read:settings.
13. Click "Done".
14. You're good to go. Now you can easily add your Zoom integration in the Cal.diy settings.

### Obtaining Daily API Credentials

1. OpenDaily.coand create an account.
2. From within your dashboard, go to thedeveloperstab.
3. Copy your API key.
4. Now paste the API key to your.envfile into theDAILY_API_KEYfield in your.envfile.
5. If you have theDaily Scale Planset theDAILY_SCALE_PLANvariable totruein order to use features like video recording.

### Obtaining Basecamp Client ID and Secret

1. Visit the37 Signals Integrations Dashboardand sign in.
2. Register a new application by clicking the Register one now link.
3. Fill in your company details.
4. Select Basecamp 4 as the product to integrate with.
5. Set the Redirect URL for OAuth<Cal.diy URL>/api/integrations/basecamp3/callbackreplacing Cal.diy URL with the URI at which your application runs.
6. Click on done and copy the Client ID and secret into theBASECAMP3_CLIENT_IDandBASECAMP3_CLIENT_SECRETfields.
7. Set theBASECAMP3_CLIENT_SECRETenv variable to{your_domain} ({support_email}).

### Obtaining HubSpot Client ID and Secret

1. OpenHubSpot Developerand sign into your account, or create a new one.
2. From within the home of the Developer account page, go to "Manage apps".
3. Click "Create legacy app" button top right and select public app.
4. Fill in any information you want in the "App info" tab
5. Go to tab "Auth"
6. Now copy the Client ID and Client Secret to your.envfile into theHUBSPOT_CLIENT_IDandHUBSPOT_CLIENT_SECRETfields.
7. Set the Redirect URL for OAuth<Cal.diy URL>/api/integrations/hubspot/callbackreplacing Cal.diy URL with the URI at which your application runs.
8. In the "Scopes" section at the bottom of the page, make sure you select "Read" and "Write" for scopes calledcrm.objects.contactsandcrm.lists.
9. Click the "Save" button at the bottom footer.
10. You're good to go. Now you can see any booking in Cal.diy created as a meeting in HubSpot for your contacts.

### Obtaining Webex Client ID and Secret

See Webex Readme

### Obtaining ZohoCRM Client ID and Secret

1. OpenZoho API Consoleand sign into your account, or create a new one.
2. From within the API console page, go to "Applications".
3. Click "ADD CLIENT" button top right and select "Server-based Applications".
4. Fill in any information you want in the "Client Details" tab
5. Go to tab "Client Secret" tab.
6. Now copy the Client ID and Client Secret to your.envfile into theZOHOCRM_CLIENT_IDandZOHOCRM_CLIENT_SECRETfields.
7. Set the Redirect URL for OAuth<Cal.diy URL>/api/integrations/zohocrm/callbackreplacing Cal.diy URL with the URI at which your application runs.
8. In the "Settings" section check the "Multi-DC" option if you wish to use the same OAuth credentials for all data centers.
9. Click the "Save"/ "UPDATE" button at the bottom footer.
10. You're good to go. Now you can easily add your ZohoCRM integration in the Cal.diy settings.

### Obtaining Zoho Calendar Client ID and Secret

Follow these steps

### Obtaining Zoho Bigin Client ID and Secret

Follow these steps

### Obtaining Pipedrive Client ID and Secret

Follow these steps

### Rate Limiting with Unkey

Cal.diy usesUnkeyfor rate limiting. This is an optional feature and is not required for self-hosting.

If you want to enable rate limiting:

1. Sign up for an account atunkey.com
2. Create a Root key with permissions forratelimit.create_namespaceandratelimit.limit
3. Copy the root key to your.envfile into theUNKEY_ROOT_KEYfield

Note: If you don't configure Unkey, Cal.diy will work normally without rate limiting enabled.

## Contributing

We welcome contributions! Whether it's fixing a typo, improving documentation, or building new features, your help makes Cal.diy better.

Important:Cal.diy is a community fork. Contributions to this repo donotflow to Cal.com's production platform. SeeCONTRIBUTING.mdfor details.

* Check out ourContributing Guidefor detailed steps.
* Join the discussion onGitHub Discussions.
* Please follow our coding standards and commit message conventions to keep the project consistent.

Even small improvements matter — thank you for helping us grow!

### Good First Issues

We have a list ofhelp wantedthat contain small features and bugs which have a relatively limited scope. This is a great place to get started, gain experience, and get familiar with our contribution process.

### Contributors

### Translations

Don't code but still want to contribute? Join ourDiscussionsand help translate Cal.diy into your language.

## Acknowledgements

Cal.diy is built on the foundation created byCal.comand the many contributors to the original project. Special thanks to:

* Vercel
* Next.js
* Day.js
* Tailwind CSS
* Prisma

## About

Scheduling infrastructure for absolutely everyone.

cal.diy

### Topics

 open-source

 typescript

 nextjs

 postgresql

 prisma

 tailwindcss

 trpc

 next-auth

 zod

 turborepo

 t3-stack

### Resources

 Readme

 

### License

 MIT license
 

### Code of conduct

 Code of conduct
 

### Contributing

 Contributing
 

### Security policy

 Security policy
 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

Custom properties
 

### Stars

43k

 stars
 

### Watchers

183

 watching
 

### Forks

13.4k

 forks
 

 Report repository

 

## Releases611

v6.2.0

 Latest

 

Mar 1, 2026

 

+ 610 releases

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript95.8%
* CSS2.1%
* HTML0.7%
* PLpgSQL0.4%
* JavaScript0.4%
* MDX0.3%
* Other0.3%