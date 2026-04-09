---
title: Notizen aus der Maschinenhalle » Blog Archive » Download responsibly!
url: https://blog.geofabrik.de/index.php/2025/09/10/download-responsibly/
site_name: hackernews
fetched_at: '2025-09-22T13:21:30.533053'
original_url: https://blog.geofabrik.de/index.php/2025/09/10/download-responsibly/
author: marklit
date: '2025-09-22'
---

# Download responsibly!10.09.2025 | Frederik RammThis month we’ve ramped up the infrastructure behind the download server, and downloads should now be available earlierand faster. There’s also a small technical change in that requests for a “…latest” file will now be answered with aHTTP redirect to the specific latest version (see previous blog post).I would like to use this opportunity to appeal to users of the download server to “download responsibly”. We wantto continue offering this service as powerful and as convenient as possible within our means. We want everyoneto have easy access to the latest OSM data in a form that is useful to them.Every now and then, people break things for others. There have been individual clients downloading the exact same20-GB file 100s of times per day, for several days in a row. (Just the other day, one user has managed to download almost 10,000 copies of the italy-latest.osm.pbf file in 24 hours!) Others download every single file we have on theserver, every day. There’s a limit to the outgoing network bandwidth, and behaviour like this means thatthings are slowing down for everyone. Also, when we block an IP range for abuse, innocent third parties can be affected.Here’s three concrete appeals to users of the download server:1. If you want data for the whole planet, don’t download it piecemeal from us – simply get the planet file from planet.openstreetmap.org and you’re done!2. If you want a large region (like Europe or North America) updated daily, use the excellent pyosmium-up-to-date program which will automatically determine the age of your local file and update it by downloading the latest changes; this saves something like 98% of network traffic compared to a fresh download, and is faster.3. If you automate anything with regard to our download server, monitor what your script is doing or build in appropriate catches so that you don’t end up downloading the same file 1000 times just because your disk is full or something like that.Happy downloading!download.geofabrik.de to use HTTP redirects for "latest" files

#### Service

#### External Links

* German OSM project page
* International OSM project page
* Best of OSM

#### Suche // Archiv

Archiv

 September 2025

 July 2025

 June 2025

 April 2025

 March 2025

 November 2024

 February 2024

 October 2023

 September 2023

 March 2023

 September 2022

 July 2022

 September 2021

 April 2020

 June 2019

 October 2018

 May 2018

 March 2018

 October 2017

 September 2017

 June 2017

 March 2017

 January 2017

 September 2016

 August 2016

 April 2016

 February 2016

 January 2016

 September 2015

 July 2015

 April 2014

 February 2014

 January 2014

 November 2013

 October 2013

 June 2013

 April 2013

 February 2013

 November 2012

 September 2012

 June 2012

 March 2012

 January 2012

 October 2011

 September 2011

 November 2010

 October 2010

 September 2010

 July 2010

 March 2010

 January 2010

 December 2009

 July 2009

 May 2009

 March 2009

 February 2009

 December 2008

 November 2008

 October 2008

 August 2008

 June 2008

 May 2008

#### Rubriken

* Allgemein
* Services
* Uncategorized
* Veröffentlichungen

#### Sitemap

* GEOFABRIKAbout GeofabrikAbout OpenStreetMapAbout Open DataContactPressPublicationsStudents
* About Geofabrik
* About OpenStreetMap
* About Open Data
* Contact
* Press
* Publications
* Students
* Maps & DataDownloadsShape FilesRoutingGeocodingMap StylesTile ServerTile PackagesPrinted MapsWMS ServerOverpass API
* Downloads
* Shape Files
* Routing
* Geocoding
* Map Styles
* Tile Server
* Tile Packages
* Printed Maps
* WMS Server
* Overpass API
* ServicesConsultingTrainingSoftwareServer
* Consulting
* Training
* Software
* Server
* Portfolio
* Contact
* Blog

* © 2020 Geofabrik GmbH Karlsruhe
* Geofabrik is a proud member of theOpenStreetMap Foundation.
* Map data fromOpenStreetMap, OdbL 1.0
* Imprint
