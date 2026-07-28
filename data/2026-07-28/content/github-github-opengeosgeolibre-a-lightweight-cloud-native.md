---
title: 'GitHub - opengeos/GeoLibre: A lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data. It runs in the web browser, on the desktop, on mobile, and inside Jupyter notebooks. · GitHub'
url: https://github.com/opengeos/GeoLibre
site_name: github
content_file: github-github-opengeosgeolibre-a-lightweight-cloud-native
fetched_at: '2026-07-28T11:43:09.916793'
original_url: https://github.com/opengeos/GeoLibre
author: opengeos
description: A lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data. It runs in the web browser, on the desktop, on mobile, and inside Jupyter notebooks. - opengeos/GeoLibre
---

### Uh oh!

There was an error while loading.Please reload this page.

 

 

 opengeos

 

/

GeoLibre

Public

* ### Uh oh!There was an error while loading.Please reload this page.
* NotificationsYou must be signed in to change notification settings
* Fork370
* Star3k

 
 
 
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

888 Commits
888 Commits
.github
.github
 
 
apps/
geolibre-desktop
apps/
geolibre-desktop
 
 
backend/
geolibre_server
backend/
geolibre_server
 
 
docker
docker
 
 
docs
docs
 
 
e2e
e2e
 
 
packages
packages
 
 
packaging
packaging
 
 
python
python
 
 
scripts
scripts
 
 
tests
tests
 
 
workers
workers
 
 
.dockerignore
.dockerignore
 
 
.gitattributes
.gitattributes
 
 
.gitignore
.gitignore
 
 
.oxfmtrc.json
.oxfmtrc.json
 
 
.pre-commit-config.yaml
.pre-commit-config.yaml
 
 
CITATION.cff
CITATION.cff
 
 
CLAUDE.md
CLAUDE.md
 
 
CONTRIBUTING.md
CONTRIBUTING.md
 
 
Dockerfile
Dockerfile
 
 
LICENSE
LICENSE
 
 
README.md
README.md
 
 
eslint.config.mjs
eslint.config.mjs
 
 
mkdocs.yml
mkdocs.yml
 
 
package-lock.json
package-lock.json
 
 
package.json
package.json
 
 
playwright.config.ts
playwright.config.ts
 
 
requirements-docs.txt
requirements-docs.txt
 
 
ruff.toml
ruff.toml
 
 
tsconfig.base.json
tsconfig.base.json
 
 
View all files

## Repository files navigation

# GeoLibre

A free and open-source, lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data. It runs everywhere you do, in the web browser, on the desktop, on mobile, and inside Jupyter notebooks, all while keeping your data local and private.

GeoLibre is built withTauri v2,React,TypeScript,MapLibre GL JS,DuckDB-WASM Spatial, anddeck.gl. The same workspace runs as a native desktop app, a native Android app, in any modern web browser, and adapts responsively to mobile and small screens.

* Launch GeoLibre Web— the full app in your browser, nothing to install
* Download the desktop app— Windows, macOS, and Linux installers
* Get started— install, run from source, and configure
* Features— the complete feature list

## Demos

Click any screenshot to open it at full resolution, or any animation to play the full-quality video.

### 3D Tiles

Open the live project

### NYC buildings and subways

Manhattan building footprints extruded in 3D and colored by construction era, with the MTA subway lines and stations on top and a legend generated automatically from the layers' symbology.

The animation below runs the Time Slider along the buildings' construction year, from 1850 to 2025, so Manhattan fills in era by era. Click it to play the full-quality video.

Open the live project

### Planetary basemaps

GeoLibre is not limited to Earth. Planetary basemaps from OpenPlanetaryMap and USGS Astrogeology cover the Moon, Mars, Mercury, Venus, the Galilean moons (Io, Europa, Ganymede, Callisto), Titan, Pluto, and Charon, with a per-project ellipsoid so distance, area, and scale measurements match the body you are mapping. The deep-space starfield behind each globe comes from the Atmosphere Effects plugin.

Earth

Moon

Mars

Mercury

Pluto

Venus

Switch bodies from the planet switcher in the Layers panel. SeeDemosfor more.

### Video tutorials

* GeoLibre 1.0: A Free, Open-Source Cloud-Native GIS That Runs Anywhere (Browser, Desktop & Jupyter)
* Geoprocessing in the Browser: 700+ Free GIS Tools in GeoLibre, Zero Install

## Documentation

Full documentation, including the User Guide and Tutorials, is published atgeolibre.app.

* Getting Started- use GeoLibre on the web, desktop, Android, or in Jupyter; run it from source; run it with Docker; and configure optional credentials.
* Features- the complete, feature-by-feature list of what GeoLibre can do today.
* Demos- a visual tour: 3D Tiles, 3D city data, planetary basemaps, the SQL Workspace, and embeds.
* Downloads- installers and package managers for Windows, macOS, and Linux.
* User Guide- a feature-by-feature reference for the interface, adding data, layers, styling, the attribute table, map controls, processing, the SQL Workspace, data integrations, plugins, settings, and embedding.
* Tutorials- hands-on, end-to-end workflows: your first map, cloud-native data, vector analysis, terrain analysis, spatial SQL, and sharing and embedding.
* ReferenceArchitectureAndroidiOSProject formatPlugin APIUI ProfilesInternationalizationPython package (Jupyter)Notebook PanelRoadmapContributingHow to Cite
* Architecture
* Android
* iOS
* Project format
* Plugin API
* UI Profiles
* Internationalization
* Python package (Jupyter)
* Notebook Panel
* Roadmap
* Contributing
* How to Cite

Contributions are welcome. See theContributingguide
for the development setup, repository layout, and quality gate.

## Acknowledgements

GeoLibre is built on the free and open-source geospatial and web communities — including MapLibre GL JS, deck.gl, DuckDB-WASM Spatial, Turf.js, Tauri, React, and many more. See the fullAcknowledgementspage for the complete list of projects and community contributors.

* TheAtmosphere Effectsplugin (deep-space backdrop, parallax starfield, comets, and the globe atmosphere halo) adapts the technique and visual design fromLeonel Dias's articleGlobe atmosphere, halo, and comets— the layered Canvas 2D approach, the halo gradient and "screen" blend, the limb-sampling that keeps the halo aligned under pitch, and the starfield/comet parameters.
* Community contributors— thanks toRyanphoenixfor many valued contributions, including issue reports, feedback, and improvements.
* Beta testers— thanks toRené van der Velde(Netherlands) for early testing, detailed bug reports, and feature requests.

## Citation

If you use GeoLibre in your work, please cite it. GeoLibre is archived onZenodo, which mints a DOI for every release. The concept DOI below always resolves to the latest version.

Wu, Q. (2026). GeoLibre: A lightweight, cloud-native GIS platform for visualizing, exploring, and analyzing geospatial data. Zenodo.https://doi.org/10.5281/zenodo.20785400

You can also use GitHub's"Cite this repository"button (which readsCITATION.cff) to copy a ready-made APA or BibTeX entry. See theHow to Citepage for more formats.

## License

MIT