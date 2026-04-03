---
title: 'GitHub - BigBodyCobain/Shadowbroker: Open-source intelligence for the global theater. Track everything from the corporate/private jets of the wealthy, and spy satellites, to seismic events in one unified interface. The knowledge is available to all but rarely aggregated in the open, until now. · GitHub'
url: https://github.com/BigBodyCobain/Shadowbroker
site_name: hackernews_api
content_file: hackernews_api-github-bigbodycobainshadowbroker-open-source-intel
fetched_at: '2026-03-09T11:18:10.086975'
original_url: https://github.com/BigBodyCobain/Shadowbroker
author: vancecookcobxin
date: '2026-03-08'
description: Open-source intelligence for the global theater. Track everything from the corporate/private jets of the wealthy, and spy satellites, to seismic events in one unified interface. The knowledge is available to all but rarely aggregated in the open, until now. - BigBodyCobain/Shadowbroker
tags:
- hackernews
- trending
---

BigBodyCobain

 

/

Shadowbroker

Public

* NotificationsYou must be signed in to change notification settings
* Fork70
* Star746

 
 
 
 
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

27 Commits
27 Commits
.git_backup
.git_backup
 
 
.github/
workflows
.github/
workflows
 
 
backend
backend
 
 
frontend
frontend
 
 
.gitignore
.gitignore
 
 
README.md
README.md
 
 
clean_zip.py
clean_zip.py
 
 
docker-compose.yml
docker-compose.yml
 
 
jobs.json
jobs.json
 
 
refactor_cesium.py
refactor_cesium.py
 
 
start-backend.js
start-backend.js
 
 
start.bat
start.bat
 
 
start.sh
start.sh
 
 
zip_repo.py
zip_repo.py
 
 
View all files

## Repository files navigation

# 🛰️ S H A D O W B R O K E R

Global Threat Intercept — Real-Time Geospatial Intelligence Platform

ShadowBrokeris a real-time, full-spectrum geospatial intelligence dashboard that aggregates live data from dozens of open-source intelligence (OSINT) feeds and renders them on a unified dark-ops map interface. It tracks aircraft, ships, satellites, earthquakes, conflict zones, CCTV networks, GPS jamming, and breaking geopolitical events — all updating in real time.

Built withNext.js,MapLibre GL,FastAPI, andPython, it's designed for analysts, researchers, and enthusiasts who want a single-pane-of-glass view of global activity.

## Interesting Use Cases

* Track private jets of billionaires
* Monitor satellites passing overhead
* Watch naval traffic worldwide
* Detect GPS jamming zones
* Follow earthquakes and disasters in real time

## ⚡ Quick Start (Docker)

git clone https://github.com/BigBodyCobain/Shadowbroker.git

cd
 Shadowbroker
docker-compose up -d

Openhttp://localhost:3000to view the dashboard!(Requires Docker)

## ✨ Features

### 🛩️ Aviation Tracking

* Commercial Flights— Real-time positions via OpenSky Network (~5,000+ aircraft)
* Private Aircraft— Light GA, turboprops, bizjets tracked separately
* Private Jets— High-net-worth individual aircraft with owner identification
* Military Flights— Tankers, ISR, fighters, transports via adsb.lol military endpoint
* Flight Trail Accumulation— Persistent breadcrumb trails for all tracked aircraft
* Holding Pattern Detection— Automatically flags aircraft circling (>300° total turn)
* Aircraft Classification— Shape-accurate SVG icons: airliners, turboprops, bizjets, helicopters
* Grounded Detection— Aircraft below 100ft AGL rendered with grey icons

### 🚢 Maritime Tracking

* AIS Vessel Stream— 25,000+ vessels via aisstream.io WebSocket (real-time)
* Ship Classification— Cargo, tanker, passenger, yacht, military vessel types with color-coded icons
* Carrier Strike Group Tracker— All 11 active US Navy aircraft carriers with OSINT-estimated positionsAutomated GDELT news scraping for carrier movement intelligence50+ geographic region-to-coordinate mappingsDisk-cached positions, auto-updates at 00:00 & 12:00 UTC
* Automated GDELT news scraping for carrier movement intelligence
* 50+ geographic region-to-coordinate mappings
* Disk-cached positions, auto-updates at 00:00 & 12:00 UTC
* Cruise & Passenger Ships— Dedicated layer for cruise liners and ferries
* Clustered Display— Ships cluster at low zoom with count labels, decluster on zoom-in

### 🛰️ Space & Satellites

* Orbital Tracking— Real-time satellite positions via CelesTrak TLE data + SGP4 propagation (2,000+ active satellites, no API key required)
* Mission-Type Classification— Color-coded by mission: military recon (red), SAR (cyan), SIGINT (white), navigation (blue), early warning (magenta), commercial imaging (green), space station (gold)

### 🌍 Geopolitics & Conflict

* Global Incidents— GDELT-powered conflict event aggregation (last 8 hours, ~1,000 events)
* Ukraine Frontline— Live warfront GeoJSON from DeepState Map
* SIGINT/RISINT News Feed— Real-time RSS aggregation from multiple intelligence-focused sources
* Region Dossier— Right-click anywhere on the map for:Country profile (population, capital, languages, currencies, area)Head of state & government type (Wikidata SPARQL)Local Wikipedia summary with thumbnail
* Country profile (population, capital, languages, currencies, area)
* Head of state & government type (Wikidata SPARQL)
* Local Wikipedia summary with thumbnail

### 📷 Surveillance

* CCTV Mesh— 2,000+ live traffic cameras from:🇬🇧 Transport for London JamCams🇺🇸 Austin, TX TxDOT🇺🇸 NYC DOT🇸🇬 Singapore LTACustom URL ingestion
* 🇬🇧 Transport for London JamCams
* 🇺🇸 Austin, TX TxDOT
* 🇺🇸 NYC DOT
* 🇸🇬 Singapore LTA
* Custom URL ingestion
* Feed Rendering— Automatic detection & rendering of video, MJPEG, HLS, embed, satellite tile, and image feeds
* Clustered Map Display— Green dots cluster with count labels, decluster on zoom

### 📡 Signal Intelligence

* GPS Jamming Detection— Real-time analysis of aircraft NAC-P (Navigation Accuracy Category) valuesGrid-based aggregation identifies interference zonesRed overlay squares with "GPS JAM XX%" severity labels
* Grid-based aggregation identifies interference zones
* Red overlay squares with "GPS JAM XX%" severity labels
* Radio Intercept Panel— Scanner-style UI for monitoring communications

### 🌐 Additional Layers

* Earthquakes (24h)— USGS real-time earthquake feed with magnitude-scaled markers
* Day/Night Cycle— Solar terminator overlay showing global daylight/darkness
* Global Markets Ticker— Live financial market indices (minimizable)
* Measurement Tool— Point-to-point distance & bearing measurement on the map

## 🏗️ Architecture

┌────────────────────────────────────────────────────────┐
│ FRONTEND (Next.js) │
│ │
│ ┌─────────────┐ ┌──────────┐ ┌───────────────┐ │
│ │ MapLibre GL │ │ NewsFeed │ │ Control Panels│ │
│ │ 2D WebGL │ │ SIGINT │ │ Layers/Filters│ │
│ │ Map Render │ │ Intel │ │ Markets/Radio │ │
│ └──────┬──────┘ └────┬─────┘ └───────┬───────┘ │
│ └────────────────┼──────────────────┘ │
│ │ REST API (60s / 120s) │
├──────────────────────────┼─────────────────────────────┤
│ BACKEND (FastAPI) │
│ │ │
│ ┌───────────────────────┼──────────────────────────┐ │
│ │ Data Fetcher (Scheduler) │ │
│ │ │ │
│ │ ┌──────────┬──────────┬──────────┬───────────┐ │ │
│ │ │ OpenSky │ adsb.lol │CelesTrak │ USGS │ │ │
│ │ │ Flights │ Military │ Sats │ Quakes │ │ │
│ │ ├──────────┼──────────┼──────────┼───────────┤ │ │
│ │ │ AIS WS │ Carrier │ GDELT │ CCTV │ │ │
│ │ │ Ships │ Tracker │ Conflict │ Cameras │ │ │
│ │ ├──────────┼──────────┼──────────┼───────────┤ │ │
│ │ │ DeepState│ RSS │ Region │ GPS │ │ │
│ │ │ Frontline│ Intel │ Dossier │ Jamming │ │ │
│ │ └──────────┴──────────┴──────────┴───────────┘ │ │
│ └──────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────┘

## 📊 Data Sources & APIs

Source

Data

Update Frequency

API Key Required

OpenSky Network

Commercial & private flights

~60s

Optional (anonymous limited)

adsb.lol

Military aircraft

~60s

No

aisstream.io

AIS vessel positions

Real-time WebSocket

Yes

CelesTrak

Satellite orbital positions (TLE + SGP4)

~60s

No

USGS Earthquake

Global seismic events

~60s

No

GDELT Project

Global conflict events

~6h

No

DeepState Map

Ukraine frontline

~30min

No

Transport for London

London CCTV JamCams

~5min

No

TxDOT

Austin TX traffic cameras

~5min

No

NYC DOT

NYC traffic cameras

~5min

No

Singapore LTA

Singapore traffic cameras

~5min

Yes

RestCountries

Country profile data

On-demand (cached 24h)

No

Wikidata SPARQL

Head of state data

On-demand (cached 24h)

No

Wikipedia API

Location summaries & aircraft images

On-demand (cached)

No

CARTO Basemaps

Dark map tiles

Continuous

No

## 🚀 Getting Started

### 🐳 Docker Setup (Recommended for Self-Hosting)

The repo includes adocker-compose.ymlthat builds both images locally.

git clone https://github.com/BigBodyCobain/Shadowbroker.git

cd
 Shadowbroker

#
 Add your API keys (optional — see Environment Variables below)

cp backend/.env.example backend/.env

#
 Build and start

docker-compose up -d --build

Openhttp://localhost:3000to view the dashboard.

Custom ports or LAN access?The frontend auto-detects the backend at<your-hostname>:8000. If you remap the backend to a different port
(e.g."9096:8000"), setNEXT_PUBLIC_API_URLbefore building:

NEXT_PUBLIC_API_URL=http://192.168.1.50:9096 docker-compose up -d --build

This is abuild-timevariable (Next.js limitation) — it gets baked into
the frontend duringnpm run build. Changing it requires a rebuild.

### 📦 Quick Start (No Code Required)

If you just want to run the dashboard without dealing with terminal commands:

1. Go to theReleasestab on the right side of this GitHub page.
2. Download the latest.zipfile from the release.
3. Extract the folder to your computer.
4. Windows:Double-clickstart.bat.Mac/Linux:Open terminal, typechmod +x start.sh, and run./start.sh.
5. It will automatically install everything and launch the dashboard!

### 💻 Developer Setup

If you want to modify the code or run from source:

#### Prerequisites

* Node.js18+ andnpm
* Python3.10+ withpip
* API keys for:aisstream.io(required), and optionallyopensky-network.org(OAuth2),lta.gov.sg

### Installation

#
 Clone the repository

git clone https://github.com/your-username/shadowbroker.git

cd
 shadowbroker/live-risk-dashboard

#
 Backend setup

cd
 backend
python -m venv venv
venv
\S
cripts
\a
ctivate 
#
 Windows

#
 source venv/bin/activate # macOS/Linux

pip install -r requirements.txt

#
 Create .env with your API keys

echo
 
"
AIS_API_KEY=your_aisstream_key
"
 
>>
 .env

echo
 
"
OPENSKY_CLIENT_ID=your_opensky_client_id
"
 
>>
 .env

echo
 
"
OPENSKY_CLIENT_SECRET=your_opensky_secret
"
 
>>
 .env

#
 Frontend setup

cd
 ../frontend
npm install

### Running

#
 From the frontend directory — starts both frontend & backend concurrently

npm run dev

This starts:

* Next.jsfrontend onhttp://localhost:3000
* FastAPIbackend onhttp://localhost:8000

## 🎛️ Data Layers

All layers are independently toggleable from the left panel:

Layer

Default

Description

Commercial Flights

✅ ON

Airlines, cargo, GA aircraft

Private Flights

✅ ON

Non-commercial private aircraft

Private Jets

✅ ON

High-value bizjets with owner data

Military Flights

✅ ON

Military & government aircraft

Tracked Aircraft

✅ ON

Special interest watch list

Satellites

✅ ON

Orbital assets by mission type

Carriers / Mil / Cargo

✅ ON

Navy carriers, cargo ships, tankers

Civilian Vessels

❌ OFF

Yachts, fishing, recreational

Cruise / Passenger

✅ ON

Cruise ships and ferries

Earthquakes (24h)

✅ ON

USGS seismic events

CCTV Mesh

❌ OFF

Surveillance camera network

Ukraine Frontline

✅ ON

Live warfront positions

Global Incidents

✅ ON

GDELT conflict events

GPS Jamming

✅ ON

NAC-P degradation zones

Day / Night Cycle

✅ ON

Solar terminator overlay

## 🔧 Performance

The platform is optimized for handling massive real-time datasets:

* Gzip Compression— API payloads compressed ~92% (11.6 MB → 915 KB)
* ETag Caching—304 Not Modifiedresponses skip redundant JSON parsing
* Viewport Culling— Only features within the visible map bounds (+20% buffer) are rendered
* Clustered Rendering— Ships, CCTV, and earthquakes use MapLibre clustering to reduce feature count
* Debounced Viewport Updates— 300ms debounce prevents GeoJSON rebuild thrash during pan/zoom
* Position Interpolation— Smooth 10s tick animation between data refreshes
* React.memo— Heavy components wrapped to prevent unnecessary re-renders
* Coordinate Precision— Lat/lng rounded to 5 decimals (~1m) to reduce JSON size

## 📁 Project Structure

live-risk-dashboard/
├── backend/
│ ├── main.py # FastAPI app, middleware, API routes
│ ├── carrier_cache.json # Persisted carrier OSINT positions
│ ├── cctv.db # SQLite CCTV camera database
│ └── services/
│ ├── data_fetcher.py # Core scheduler — fetches all data sources
│ ├── ais_stream.py # AIS WebSocket client (25K+ vessels)
│ ├── carrier_tracker.py # OSINT carrier position tracker
│ ├── cctv_pipeline.py # Multi-source CCTV camera ingestion
│ ├── geopolitics.py # GDELT + Ukraine frontline fetcher
│ ├── region_dossier.py # Right-click country/city intelligence
│ ├── radio_intercept.py # Scanner radio feed integration
│ ├── network_utils.py # HTTP client with curl fallback
│ └── api_settings.py # API key management
│
├── frontend/
│ ├── src/
│ │ ├── app/
│ │ │ └── page.tsx # Main dashboard — state, polling, layout
│ │ └── components/
│ │ ├── MaplibreViewer.tsx # Core map — 2,000+ lines, all GeoJSON layers
│ │ ├── NewsFeed.tsx # SIGINT feed + entity detail panels
│ │ ├── WorldviewLeftPanel.tsx # Data layer toggles
│ │ ├── WorldviewRightPanel.tsx # Search + filter sidebar
│ │ ├── FilterPanel.tsx # Basic layer filters
│ │ ├── AdvancedFilterModal.tsx # Airport/country/owner filtering
│ │ ├── MapLegend.tsx # Dynamic legend with all icons
│ │ ├── MarketsPanel.tsx # Global financial markets ticker
│ │ ├── RadioInterceptPanel.tsx # Scanner-style radio panel
│ │ ├── FindLocateBar.tsx # Search/locate bar
│ │ ├── SettingsPanel.tsx # App settings
│ │ ├── ScaleBar.tsx # Map scale indicator
│ │ ├── WikiImage.tsx # Wikipedia image fetcher
│ │ └── ErrorBoundary.tsx # Crash recovery wrapper
│ └── package.json

## 🔑 Environment Variables

Create a.envfile in thebackend/directory:

#
 Required

AIS_API_KEY
=
your_aisstream_key
 
#
 Maritime vessel tracking (aisstream.io)

#
 Optional (enhances data quality)

OPENSKY_CLIENT_ID
=
your_opensky_client_id
 
#
 OAuth2 — higher rate limits for flight data

OPENSKY_CLIENT_SECRET
=
your_opensky_secret
 
#
 OAuth2 — paired with Client ID above

LTA_ACCOUNT_KEY
=
your_lta_key
 
#
 Singapore CCTV cameras

## ⚠️Disclaimer

This is aneducational and research toolbuilt entirely on publicly available, open-source intelligence (OSINT) data. No classified, restricted, or non-public data sources are used. Carrier positions are estimates based on public reporting. The military-themed UI is purely aesthetic.

Do not use this tool for any operational, military, or intelligence purpose.

## 📜 License

This project is for educational and personal research purposes. See individual API provider terms of service for data usage restrictions.

Built with ☕ and too many API calls

## About

Open-source intelligence for the global theater. Track everything from the corporate/private jets of the wealthy, and spy satellites, to seismic events in one unified interface. The knowledge is available to all but rarely aggregated in the open, until now.

### Resources

 Readme

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

Activity
 

### Stars

746

 stars
 

### Watchers

2

 watching
 

### Forks

70

 forks
 

 Report repository

 

## Releases3

ShadowBroker v0.3

 Latest

 

Mar 9, 2026

 

+ 2 releases

## Packages0

 

 

 

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Contributors

### Uh oh!

There was an error while loading.Please reload this page.

 

 

## Languages

* TypeScript48.0%
* HTML28.5%
* Python20.3%
* Shell2.1%
* Perl0.4%
* JavaScript0.3%
* Other0.4%