---
title: 3.4M Solar Panels
url: https://tech.marksblogg.com/american-solar-farms-v2.html
site_name: hackernews_api
content_file: hackernews_api-34m-solar-panels
fetched_at: '2026-04-23T09:44:25.540809'
original_url: https://tech.marksblogg.com/american-solar-farms-v2.html
author: Mark Litwintschik
date: '2026-04-22'
description: Benchmarks & Tips for Big Data, Hadoop, AWS, Google Cloud, PostgreSQL, Spark, Python & More...
tags:
- hackernews
- trending
---

### 3.4M Solar Panels

In October, Ireviewedthe Ground-Mounted Solar Energy in the United States (GM-SEUS) dataset. This dataset attempted to outline the majority of solar farm arrays and panels across the US. Version 1 of this dataset contained 2.9M panels.

On Monday, version 2 of this dataset was released and now contains more than 3.4M panels. In addition to the panels and arrays being refreshed, there is a new rooftop array dataset.

In this post, I'll review v2 of the GM-SEUS dataset.

## My Workstation

I'm using a 5.7 GHz AMD Ryzen 9 9950X CPU. It has 16 cores and 32 threads and 1.2 MB of L1, 16 MB of L2 and 64 MB of L3 cache. It has a liquid cooler attached and is housed in a spacious, full-sized Cooler Master HAF 700 computer case.

The system has 96 GB of DDR5 RAM clocked at 4,800 MT/s and a 5th-generation, Crucial T700 4 TB NVMe M.2 SSD which can read at speeds up to 12,400 MB/s. There is a heatsink on the SSD to help keep its temperature down. This is my system's C drive.

The system is powered by a 1,200-watt, fully modular Corsair Power Supply and is sat on an ASRock X870E Nova 90 Motherboard.

I'm running Ubuntu 24 LTS via Microsoft's Ubuntu for Windows on Windows 11 Pro. In case you're wondering why I don't run a Linux-based desktop as my primary work environment, I'm still using an Nvidia GTX 1080 GPU which has better driver support on Windows and ArcGIS Pro only supports Windows natively.

## Installing Prerequisites

I'll use GDAL 3.9.3 to help analyse the data in this post.

$
 
sudo
 
add-apt-repository
 
ppa:ubuntugis/ubuntugis-unstable
$
 
sudo
 
apt
 
update
$
 
sudo
 
apt
 
install
 
\

 
gdal-bin

I'll use DuckDB, along with itsH3,JSON,Lindel,ParquetandSpatialextensions in this post.

$
 
cd
 
~
$
 
wget
 
-c
 
https://github.com/duckdb/duckdb/releases/download/v1.5.1/duckdb_cli-linux-amd64.zip
$
 
unzip
 
-j
 
duckdb_cli-linux-amd64.zip
$
 
chmod
 
+x
 
duckdb
$
 
~/duckdb

INSTALL
 
h3
 
FROM
 
community
;

INSTALL
 
lindel
 
FROM
 
community
;

INSTALL
 
json
;

INSTALL
 
parquet
;

INSTALL
 
spatial
;

I'll set up DuckDB to load every installed extension each time it launches.

$
 
vi
 
~/.duckdbrc

.timer on
.width 180
LOAD h3;
LOAD lindel;
LOAD json;
LOAD parquet;
LOAD spatial;

The maps in this post were rendered withQGISversion 4.0.1. QGIS is a desktop application that runs on Windows, macOS and Linux. The application has grown in popularity in recent years and has ~15M application launches from users all around the world each month.

I used QGIS'HCMGISplugin to add basemaps from Esri to this post.

## Analysis-Ready Datasets

The following will download a 3.4 GB ZIP file. I'll extract any GeoPackage (GPKG) file from it.

$
 
wget
 
-O
 
GMSEUS_v2.zip
 
\

 
'https://zenodo.org/records/19581821/files/GMSEUS.zip?download=1'

$
 
unzip
 
-j
 
GMSEUS_v2.zip
 
"*.gpkg"

The following is the projection used by the GPKG files in this dataset.

$
 
gdalsrsinfo
 
\

 
-o
 
proj4
 
\

 
GMSEUS_RooftopArrays_2025_v2_0.gpkg

+proj=aea +lat_0=23 +lon_0=-96 +lat_1=29.5 +lat_2=45.5 +x_0=0 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs

The following will convert the rooftop arrays into Parquet. I needed to use DuckDB v1.4.4 for the following as v1.5.1 was raising exceptions.

$
 
~/duckdb

COPY
 
(

 
WITH
 
a
 
AS
 
(

 
SELECT
 
Source
,

 
grndCvr
,

 
modType
,

 
mount
,

 
nativeID
,

 
roofArrID
,

 
area
:
 
IF
(
area
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
area
::
DOUBLE
),

 
azimuth
:
 
IF
(
azimuth
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
azimuth
::
DOUBLE
),

 
capMWAC
:
 
IF
(
capMWAC
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
capMWAC
::
DOUBLE
),

 
capMWDC
:
 
IF
(
capMWDC
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
capMWDC
::
DOUBLE
),

 
tilt
:
 
IF
(
tilt
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
tilt
::
DOUBLE
),

 
instYr
:
 
CASE
 
WHEN
 
instYr
::
INT
 
=
 
-
9999
 
THEN
 
NULL
 
ELSE
 
instYr
 
END
,

 
ST_FLIPCOORDINATES
(

 
ST_TRANSFORM
(

 
geom
,

 
'+proj=aea +lat_0=23 +lon_0=-96 +lat_1=29.5 +lat_2=45.5 +x_0=0 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
,

 
'EPSG:4326'
))
 
geometry

 
FROM
 
ST_READ
(
'GMSEUS_RooftopArrays_2025_v2_0.gpkg'
)

 
)

 
SELECT
 
*
 
EXCLUDE
 
(
geometry
),

 
{
'xmin'
:
 
ST_XMIN
(
ST_EXTENT
(
geometry
)),

 
'ymin'
:
 
ST_YMIN
(
ST_EXTENT
(
geometry
)),

 
'xmax'
:
 
ST_XMAX
(
ST_EXTENT
(
geometry
)),

 
'ymax'
:
 
ST_YMAX
(
ST_EXTENT
(
geometry
))
}
 
AS
 
bbox
,

 
ST_ASWKB
(
geometry
)
 
geometry

 
FROM
 
a

 
ORDER
 
BY
 
HILBERT_ENCODE
([
ST_Y
(
ST_CENTROID
(
geometry
)),

 
ST_X
(
ST_CENTROID
(
geometry
))]::
double
[
2
])

)
 
TO
 
'GMSEUS_RooftopArrays_2025_v2_0.parquet'
 
(

 
FORMAT
 
'PARQUET'
,

 
CODEC
 
'ZSTD'
,

 
COMPRESSION_LEVEL
 
22
,

 
ROW_GROUP_SIZE
 
15000
);

There are 5,822 records in this dataset.

SELECT
 
COUNT
(
*
)

FROM
 
'GMSEUS_RooftopArrays_2025_v2_0.parquet'
;

5,822

Below is a breakdown of unique values and NULL coverage across each column.

SELECT
 
column_name
,

 
column_type
,

 
null_percentage
,

 
approx_unique
,

 
min
,

 
max

FROM
 
(
SUMMARIZE

 
FROM
 
READ_PARQUET
(
'GMSEUS_RooftopArrays_2025_v2_0.parquet'
))

WHERE
 
column_name
 
!=
 
'geometry'

AND
 
column_name
 
!=
 
'bbox'

ORDER
 
BY
 
LOWER
(
column_name
);

┌─────────────┬─────────────┬─────────────────┬───────────────┬────────────┬────────────────────┐
│ column_name │ column_type │ null_percentage │ approx_unique │ min │ max │
│ varchar │ varchar │ decimal(9,2) │ int64 │ varchar │ varchar │
├─────────────┼─────────────┼─────────────────┼───────────────┼────────────┼────────────────────┤
│ area │ DOUBLE │ 2.77 │ 5180 │ 15.0 │ 487111.0 │
│ azimuth │ DOUBLE │ 89.63 │ 156 │ 0.0 │ 530.02323408881 │
│ capMWAC │ DOUBLE │ 89.52 │ 60 │ 0.2 │ 74.9 │
│ capMWDC │ DOUBLE │ 87.12 │ 166 │ 0.00448 │ 99.7 │
│ grndCvr │ VARCHAR │ 97.61 │ 2 │ impervious │ vegetation │
│ instYr │ BIGINT │ 72.43 │ 23 │ 2003 │ 2025 │
│ modType │ VARCHAR │ 0.00 │ 2 │ c-si │ thin-film │
│ mount │ VARCHAR │ 87.53 │ 5 │ dual_axis │ unknown │
│ nativeID │ VARCHAR │ 0.00 │ 4540 │ 1 │ Xebec 1 solar farm │
│ roofArrID │ BIGINT │ 0.00 │ 5830 │ 1 │ 5822 │
│ Source │ VARCHAR │ 0.00 │ 15 │ CCVPV │ gspt │
│ tilt │ DOUBLE │ 90.64 │ 31 │ 0.0 │ 52.0 │
├─────────────┴─────────────┴─────────────────┴───────────────┴────────────┴────────────────────┤
│ 12 rows 6 columns │
└───────────────────────────────────────────────────────────────────────────────────────────────┘

The following will convert the panels into Parquet.

COPY
 
(

 
WITH
 
a
 
AS
 
(

 
SELECT
 
Source
,

 
arrayID
:
 
arrayID
::
INT
,

 
panelID
:
 
panelID
::
INT
,

 
pnlSource
,

 
rowArea
,

 
rowAzimuth
,

 
rowLength
,

 
rowMount
,

 
rowSpace
:
 
IF
(
rowSpace
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
rowSpace
::
DOUBLE
),

 
rowWidth
,

 
ST_FLIPCOORDINATES
(

 
ST_TRANSFORM
(

 
geom
,

 
'+proj=aea +lat_0=23 +lon_0=-96 +lat_1=29.5 +lat_2=45.5 +x_0=0 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
,

 
'EPSG:4326'
))
 
geometry

 
FROM
 
ST_READ
(
'GMSEUS_Panels_Final_2025_v2_0.gpkg'
)

 
)

 
SELECT
 
*
 
EXCLUDE
 
(
geometry
),

 
{
'xmin'
:
 
ST_XMIN
(
ST_EXTENT
(
geometry
)),

 
'ymin'
:
 
ST_YMIN
(
ST_EXTENT
(
geometry
)),

 
'xmax'
:
 
ST_XMAX
(
ST_EXTENT
(
geometry
)),

 
'ymax'
:
 
ST_YMAX
(
ST_EXTENT
(
geometry
))
}
 
AS
 
bbox
,

 
ST_ASWKB
(
geometry
)
 
geometry

 
FROM
 
a

 
ORDER
 
BY
 
HILBERT_ENCODE
([
ST_Y
(
ST_CENTROID
(
geometry
)),

 
ST_X
(
ST_CENTROID
(
geometry
))]::
double
[
2
])

)
 
TO
 
'GMSEUS_Panels_Final_2025_v2_0.parquet'
 
(

 
FORMAT
 
'PARQUET'
,

 
CODEC
 
'ZSTD'
,

 
COMPRESSION_LEVEL
 
22
,

 
ROW_GROUP_SIZE
 
15000
);

There are 3,429,157 records in this dataset.

SELECT
 
COUNT
(
*
)

FROM
 
'GMSEUS_Panels_Final_2025_v2_0.parquet'
;

3,429,157

Below is a breakdown of unique values and NULL coverage across each column.

SELECT
 
column_name
,

 
column_type
,

 
null_percentage
,

 
approx_unique
,

 
min
,

 
max

FROM
 
(
SUMMARIZE

 
FROM
 
READ_PARQUET
(
'GMSEUS_Panels_Final_2025_v2_0.parquet'
))

WHERE
 
column_name
 
!=
 
'geometry'

AND
 
column_name
 
!=
 
'bbox'

ORDER
 
BY
 
LOWER
(
column_name
);

┌─────────────┬─────────────┬─────────────────┬───────────────┬───────────┬─────────────┐
│ column_name │ column_type │ null_percentage │ approx_unique │ min │ max │
│ varchar │ varchar │ decimal(9,2) │ int64 │ varchar │ varchar │
├─────────────┼─────────────┼─────────────────┼───────────────┼───────────┼─────────────┤
│ arrayID │ INTEGER │ 0.03 │ 12653 │ 1 │ 18980 │
│ panelID │ INTEGER │ 0.00 │ 3323765 │ 1 │ 3429157 │
│ pnlSource │ VARCHAR │ 0.00 │ 5 │ CCVPV │ OSM │
│ rowArea │ DOUBLE │ 0.00 │ 100105 │ 15.01 │ 9982.68 │
│ rowAzimuth │ DOUBLE │ 0.00 │ 22029 │ 90.0 │ 540.0 │
│ rowLength │ DOUBLE │ 0.00 │ 25531 │ 3.96 │ 737.38 │
│ rowMount │ VARCHAR │ 0.00 │ 3 │ dual_axis │ single_axis │
│ rowSpace │ DOUBLE │ 1.27 │ 1836 │ 0.01 │ 20.0 │
│ rowWidth │ DOUBLE │ 0.00 │ 2258 │ 0.45 │ 135.33 │
│ Source │ VARCHAR │ 0.00 │ 12 │ CCVPV │ USPVDB │
├─────────────┴─────────────┴─────────────────┴───────────────┴───────────┴─────────────┤
│ 10 rows 6 columns │
└───────────────────────────────────────────────────────────────────────────────────────┘

The following will convert the arrays and panels datasets into Parquet.

COPY
 
(

 
WITH
 
a
 
AS
 
(

 
SELECT
 
COUNTYFP
,

 
GCR1
,

 
GCR2
,

 
STATEFP
,

 
Source
,

 
arrayID
,

 
avgAzimuth
:
 
IF
(
avgAzimuth
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
avgAzimuth
::
DOUBLE
),

 
avgLength
:
 
IF
(
avgLength
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
avgLength
::
DOUBLE
),

 
avgSpace
:
 
IF
(
avgSpace
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
avgSpace
::
DOUBLE
),

 
avgWidth
:
 
IF
(
avgWidth
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
avgWidth
::
DOUBLE
),

 
capMWAC
,

 
capMWACest
,

 
capMWDC
,

 
capMWDCest
,

 
effInit
:
 
IF
(
effInit
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
effInit
::
DOUBLE
),

 
grndCvr
,

 
instYr
:
 
CASE
 
WHEN
 
instYr
::
INT
 
=
 
-
9999
 
THEN
 
NULL
 
ELSE
 
instYr
 
END
,

 
instYrEst
:
 
CASE
 
WHEN
 
instYrEst
::
INT
 
=
 
-
9999
 
THEN
 
NULL
 
ELSE
 
instYrEst
 
END
,

 
modType
,

 
mount
,

 
nativeID
:
 
IF
(
nativeID
::
TEXT
=
'unknown'
,
 
NULL
,
 
nativeID
),

 
newBound
,

 
numRow
,

 
tilt
:
 
IF
(
tilt
::
TEXT
=
'-9999.0'
,
 
NULL
,
 
tilt
::
DOUBLE
),

 
tiltEst
:
 
CASE
 
WHEN
 
tiltEst
::
INT
 
=
 
-
9999
 
THEN
 
NULL
 
ELSE
 
tiltEst
 
END
,

 
totArea
,

 
totRowArea
,

 
ST_FLIPCOORDINATES
(

 
ST_TRANSFORM
(

 
geom
,

 
'+proj=aea +lat_0=23 +lon_0=-96 +lat_1=29.5 +lat_2=45.5 +x_0=0 +y_0=0 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs'
,

 
'EPSG:4326'
))
 
geometry

 
FROM
 
ST_READ
(
'GMSEUS_Arrays_Final_2025_v2_0.gpkg'
)

 
)

 
SELECT
 
*
 
EXCLUDE
 
(
geometry
),

 
{
'xmin'
:
 
ST_XMIN
(
ST_EXTENT
(
geometry
)),

 
'ymin'
:
 
ST_YMIN
(
ST_EXTENT
(
geometry
)),

 
'xmax'
:
 
ST_XMAX
(
ST_EXTENT
(
geometry
)),

 
'ymax'
:
 
ST_YMAX
(
ST_EXTENT
(
geometry
))
}
 
AS
 
bbox
,

 
ST_ASWKB
(
geometry
)
 
geometry

 
FROM
 
a

 
ORDER
 
BY
 
HILBERT_ENCODE
([
ST_Y
(
ST_CENTROID
(
geometry
)),

 
ST_X
(
ST_CENTROID
(
geometry
))]::
double
[
2
])

)
 
TO
 
'GMSEUS_Arrays_Final_2025_v2_0.parquet'
 
(

 
FORMAT
 
'PARQUET'
,

 
CODEC
 
'ZSTD'
,

 
COMPRESSION_LEVEL
 
22
,

 
ROW_GROUP_SIZE
 
15000
);

There are 18,980 records in this dataset.

SELECT
 
COUNT
(
*
)

FROM
 
'GMSEUS_Arrays_Final_2025_v2_0.parquet'
;

18,980

Below is a breakdown of unique values and NULL coverage across each column.

SELECT
 
column_name
,

 
column_type
,

 
null_percentage
,

 
approx_unique
,

 
min
,

 
max

FROM
 
(
SUMMARIZE

 
FROM
 
READ_PARQUET
(
'GMSEUS_Arrays_Final_2025_v2_0.parquet'
))

WHERE
 
column_name
 
!=
 
'geometry'

AND
 
column_name
 
!=
 
'bbox'

ORDER
 
BY
 
LOWER
(
column_name
);

┌─────────────┬─────────────┬─────────────────┬───────────────┬────────────┬────────────┐
│ column_name │ column_type │ null_percentage │ approx_unique │ min │ max │
│ varchar │ varchar │ decimal(9,2) │ int64 │ varchar │ varchar │
├─────────────┼─────────────┼─────────────────┼───────────────┼────────────┼────────────┤
│ arrayID │ BIGINT │ 0.00 │ 16914 │ 1 │ 18980 │
│ avgAzimuth │ DOUBLE │ 32.88 │ 5865 │ 90.22 │ 540.0 │
│ avgLength │ DOUBLE │ 32.88 │ 12674 │ 4.02 │ 360.128 │
│ avgSpace │ DOUBLE │ 32.88 │ 7965 │ 0.024 │ 20.0 │
│ avgWidth │ DOUBLE │ 32.88 │ 6528 │ 0.863 │ 83.13 │
│ capMWAC │ DOUBLE │ 0.00 │ 4182 │ 0.003 │ 1128.931 │
│ capMWACest │ DOUBLE │ 0.00 │ 6620 │ 0.003 │ 1352.693 │
│ capMWDC │ DOUBLE │ 0.00 │ 7203 │ 0.003 │ 1467.61 │
│ capMWDCest │ DOUBLE │ 0.00 │ 8883 │ 0.004 │ 1758.501 │
│ COUNTYFP │ VARCHAR │ 0.00 │ 237 │ 001 │ 840 │
│ effInit │ DOUBLE │ 0.07 │ 12 │ 0.09 │ 0.21 │
│ GCR1 │ DOUBLE │ 0.00 │ 5096 │ 0.1 │ 1.0 │
│ GCR2 │ DOUBLE │ 0.00 │ 5913 │ 0.0943 │ 0.9883 │
│ grndCvr │ VARCHAR │ 0.00 │ 3 │ impervious │ vegetation │
│ instYr │ BIGINT │ 0.00 │ 26 │ 1985 │ 2025 │
│ instYrEst │ BIGINT │ 0.32 │ 23 │ 2003 │ 2025 │
│ modType │ VARCHAR │ 0.00 │ 3 │ c-si │ thin-film │
│ mount │ VARCHAR │ 0.00 │ 9 │ dual_axis │ unknown │
│ nativeID │ VARCHAR │ 0.23 │ 14342 │ 1 │ York Solar │
│ newBound │ BIGINT │ 0.00 │ 2 │ 0 │ 1 │
│ numRow │ INTEGER │ 0.00 │ 1177 │ 0 │ 90145 │
│ Source │ VARCHAR │ 0.00 │ 10 │ CCVPV │ USPVDB │
│ STATEFP │ VARCHAR │ 0.00 │ 49 │ 01 │ 56 │
│ tilt │ DOUBLE │ 46.39 │ 63 │ 0.0 │ 90.0 │
│ tiltEst │ BIGINT │ 46.39 │ 30 │ 10 │ 43 │
│ totArea │ INTEGER │ 0.00 │ 14669 │ 30 │ 19603313 │
│ totRowArea │ INTEGER │ 0.00 │ 13415 │ 30 │ 8537538 │
├─────────────┴─────────────┴─────────────────┴───────────────┴────────────┴────────────┤
│ 27 rows 6 columns │
└───────────────────────────────────────────────────────────────────────────────────────┘

## Rooftop Solar Arrays

Below is a heatmap of the rooftop solar arrays dataset.

CREATE
 
OR
 
REPLACE
 
TABLE
 
h3_4_stats
 
AS

 
SELECT
 
h3_4
:
 
H3_LATLNG_TO_CELL
(

 
bbox
.
ymin
,

 
bbox
.
xmin
,

 
4
),

 
COUNT
(
*
)
 
num_recs

 
FROM
 
'GMSEUS_RooftopArrays_2025_v2_0.parquet'

 
GROUP
 
BY
 
1
;

COPY
 
(

 
SELECT
 
geometry
:
 
ST_ASWKB
(
H3_CELL_TO_BOUNDARY_WKT
(
h3_4
)::
geometry
),

 
num_recs

 
FROM
 
h3_4_stats

)
 
TO
 
'GMSEUS_RooftopArrays_2025_v2_0.h3_4.parquet'
 
(

 
FORMAT
 
'PARQUET'
,

 
CODEC
 
'ZSTD'
,

 
COMPRESSION_LEVEL
 
22
,

 
ROW_GROUP_SIZE
 
15000
);

These are the source counts for this dataset.

SELECT
 
COUNT
(
*
),

 
Source

FROM
 
'GMSEUS_RooftopArrays_2025_v2_0.parquet'

GROUP
 
BY
 
2

ORDER
 
BY
 
1
 
DESC
;

┌──────────────┬────────────────────────────┐
│ count_star() │ Source │
│ int64 │ varchar │
├──────────────┼────────────────────────────┤
│ 2175 │ OSM │
│ 1835 │ CECSFC │
│ 1024 │ TZSAM │
│ 485 │ USPVDB │
│ 93 │ GRW │
│ 54 │ GMSEUSdigArraysPanels_v2_0 │
│ 46 │ gspt │
│ 43 │ SAM │
│ 24 │ GMSEUSgeoref_v2_0 │
│ 16 │ CCVPV │
│ 15 │ GPPDB │
│ 10 │ CWSD │
│ 2 │ InSPIRE │
├──────────────┴────────────────────────────┤
│ 13 rows 2 columns │
└───────────────────────────────────────────┘

Below are the most-represented source per hexagon.

CREATE
 
OR
 
REPLACE
 
TABLE
 
h3_3s
 
AS

 
WITH
 
b
 
AS
 
(

 
WITH
 
a
 
AS
 
(

 
SELECT
 
h3_3
:
 
H3_LATLNG_TO_CELL
(

 
bbox
.
ymin
,

 
bbox
.
xmin
,

 
3
)
 
,

 
Source
,

 
num_recs
:
 
COUNT
(
*
)

 
FROM
 
'GMSEUS_RooftopArrays_2025_v2_0.parquet'

 
GROUP
 
BY
 
1
,
 
2

 
)

 
SELECT
 
*
,

 
ROW_NUMBER
()
 
OVER
 
(
PARTITION
 
BY
 
h3_3

 
ORDER
 
BY
 
num_recs
 
DESC
)
 
AS
 
rn

 
FROM
 
a

 
)

 
FROM
 
b

 
WHERE
 
rn
 
=
 
1

 
ORDER
 
BY
 
num_recs
 
DESC
;

COPY
 
(

 
SELECT
 
geom
:
 
H3_CELL_TO_BOUNDARY_WKT
(
h3_3
)::
GEOMETRY
,

 
Source

 
FROM
 
h3_3s

)
 
TO
 
'GMSEUS_RooftopArrays_2025_v2_0.Source.h3_3.parquet'
 
(

 
FORMAT
 
'PARQUET'
,

 
CODEC
 
'ZSTD'
,

 
COMPRESSION_LEVEL
 
22
,

 
ROW_GROUP_SIZE
 
15000
);

This is the breakdown of mount and mod types.

WITH
 
a
 
AS
 
(

 
SELECT
 
modType
,

 
mount
,

 
cnt
:
 
COUNT
(
*
)

 
FROM
 
'GMSEUS_RooftopArrays_2025_v2_0.parquet'

 
GROUP
 
BY
 
1
,
 
2

)

PIVOT
 
a

ON
 
modType

USING
 
SUM
(
cnt
)

GROUP
 
BY
 
mount

ORDER
 
BY
 
mount
;

┌─────────────┬────────┬───────────┐
│ mount │ c-si │ thin-film │
│ varchar │ int128 │ int128 │
├─────────────┼────────┼───────────┤
│ dual_axis │ 33 │ NULL │
│ fixed_axis │ 381 │ 2 │
│ mixed │ 2 │ NULL │
│ single_axis │ 210 │ NULL │
│ unknown │ 98 │ NULL │
│ NULL │ 5096 │ NULL │
└─────────────┴────────┴───────────┘

These are the area stats broken down by year of installation.

SELECT
 
instYr
,

 
count
:
 
COUNT
(
*
),

 
avg
:
 
AVG
(
area
)::
INT
,

 
mean
:
 
MEAN
(
area
)::
INT
,

 
max
:
 
MAX
(
area
)::
INT

FROM
 
'GMSEUS_RooftopArrays_2025_v2_0.parquet'

WHERE
 
instYr
 
IS
 
NOT
 
NULL

GROUP
 
BY
 
1

ORDER
 
BY
 
1
;

┌────────┬───────┬───────┬───────┬────────┐
│ instYr │ count │ avg │ mean │ max │
│ int64 │ int64 │ int32 │ int32 │ int32 │
├────────┼───────┼───────┼───────┼────────┤
│ 2003 │ 23 │ 2630 │ 2630 │ 18124 │
│ 2005 │ 1 │ 20342 │ 20342 │ 20342 │
│ 2006 │ 1 │ 37587 │ 37587 │ 37587 │
│ 2007 │ 6 │ 16848 │ 16848 │ 27067 │
│ 2008 │ 4 │ 24989 │ 24989 │ 30107 │
│ 2009 │ 11 │ 7877 │ 7877 │ 30229 │
│ 2010 │ 24 │ 15834 │ 15834 │ 43854 │
│ 2011 │ 46 │ 41511 │ 41511 │ 487111 │
│ 2012 │ 54 │ 13371 │ 13371 │ 38923 │
│ 2013 │ 47 │ 14476 │ 14476 │ 151620 │
│ 2014 │ 24 │ 29289 │ 29289 │ 65995 │
│ 2015 │ 37 │ 34130 │ 34130 │ 218080 │
│ 2016 │ 47 │ 21094 │ 21094 │ 46138 │
│ 2017 │ 105 │ 20882 │ 20882 │ 315564 │
│ 2018 │ 225 │ 13584 │ 13584 │ 152636 │
│ 2019 │ 102 │ 21613 │ 21613 │ 111497 │
│ 2020 │ 143 │ 16052 │ 16052 │ 70018 │
│ 2021 │ 120 │ 16169 │ 16169 │ 101955 │
│ 2022 │ 141 │ 17343 │ 17343 │ 185698 │
│ 2023 │ 164 │ 18865 │ 18865 │ 137787 │
│ 2024 │ 132 │ 14743 │ 14743 │ 63190 │
│ 2025 │ 148 │ 12363 │ 12363 │ 135270 │
├────────┴───────┴───────┴───────┴────────┤
│ 22 rows 5 columns │
└─────────────────────────────────────────┘

## Rooftop Arrays Footprints

The map below shows Los Angeles to Long Beach. The detections are coloured by their source.

Some sources conservatively outline the building footprint.

Other sources have more organic shapes.

The "gspt" source uses vague circles for its detections. Below, there are four warehouses with roof panels but only two large circles are shown for their detections.

There are plenty of rooftop arrays that weren't detected all over LA. Given that this dataset only contains ~5K records, its coverage leaves a fair amount of room for improvement.

## Arrays & Panels

Below is a heatmap of the arrays dataset.

CREATE
 
OR
 
REPLACE
 
TABLE
 
h3_4_stats
 
AS

 
SELECT
 
h3_4
:
 
H3_LATLNG_TO_CELL
(

 
bbox
.
ymin
,

 
bbox
.
xmin
,

 
4
),

 
COUNT
(
*
)
 
num_recs

 
FROM
 
'GMSEUS_Arrays_Final_2025_v2_0.parquet'

 
GROUP
 
BY
 
1
;

COPY
 
(

 
SELECT
 
geometry
:
 
ST_ASWKB
(
H3_CELL_TO_BOUNDARY_WKT
(
h3_4
)::
geometry
),

 
num_recs

 
FROM
 
h3_4_stats

)
 
TO
 
'GMSEUS_Arrays_Final_2025_v2_0.h3_4.parquet'
 
(

 
FORMAT
 
'PARQUET'
,

 
CODEC
 
'ZSTD'
,

 
COMPRESSION_LEVEL
 
22
,

 
ROW_GROUP_SIZE
 
15000
);

These are the record counts for each source.

SELECT
 
COUNT
(
*
),

 
Source

FROM
 
'GMSEUS_Arrays_Final_2025_v2_0.parquet'

GROUP
 
BY
 
2

ORDER
 
BY
 
1
 
DESC
;

┌──────────────┬────────────────────────────┐
│ count_star() │ Source │
│ int64 │ varchar │
├──────────────┼────────────────────────────┤
│ 5222 │ OSM │
│ 4024 │ USPVDB │
│ 3278 │ TZSAM │
│ 2288 │ CECSFC │
│ 1697 │ GMSEUSgeoref_v2_0 │
│ 1291 │ GMSEUSdigArraysPanels_v2_0 │
│ 957 │ GRW │
│ 155 │ CCVPV │
│ 68 │ CWSD │
└──────────────┴────────────────────────────┘

Below are the most-represented source per hexagon.

CREATE
 
OR
 
REPLACE
 
TABLE
 
h3_3s
 
AS

 
WITH
 
b
 
AS
 
(

 
WITH
 
a
 
AS
 
(

 
SELECT
 
h3_3
:
 
H3_LATLNG_TO_CELL
(

 
bbox
.
ymin
,

 
bbox
.
xmin
,

 
3
)
 
,

 
Source
,

 
num_recs
:
 
COUNT
(
*
)

 
FROM
 
'GMSEUS_Arrays_Final_2025_v2_0.parquet'

 
GROUP
 
BY
 
1
,
 
2

 
)

 
SELECT
 
*
,

 
ROW_NUMBER
()
 
OVER
 
(
PARTITION
 
BY
 
h3_3

 
ORDER
 
BY
 
num_recs
 
DESC
)
 
AS
 
rn

 
FROM
 
a

 
)

 
FROM
 
b

 
WHERE
 
rn
 
=
 
1

 
ORDER
 
BY
 
num_recs
 
DESC
;

COPY
 
(

 
SELECT
 
geom
:
 
H3_CELL_TO_BOUNDARY_WKT
(
h3_3
)::
GEOMETRY
,

 
Source

 
FROM
 
h3_3s

)
 
TO
 
'GMSEUS_Arrays_Final_2025_v2_0.Source.h3_3.parquet'
 
(

 
FORMAT
 
'PARQUET'
,

 
CODEC
 
'ZSTD'
,

 
COMPRESSION_LEVEL
 
22
,

 
ROW_GROUP_SIZE
 
15000
);

Solar Farms in close proximity can have different sources attributed to their detection.

Not all solar farms are picked up within the arrays dataset. There are also array datasets that haven't marked out the panels themselves. The following is an example from -118.355, 34.837. The panels are coloured purple.

These are the array capacity stats broken down by year of installation.

SELECT
 
instYr
,

 
count
:
 
COUNT
(
*
),

 
ACavg
:
 
AVG
(
capMWAC
)::
INT
,

 
DCavg
:
 
AVG
(
capMWDC
)::
INT
,

 
ACmean
:
 
MEAN
(
capMWAC
)::
INT
,

 
DCmean
:
 
MEAN
(
capMWDC
)::
INT
,

 
ACmax
:
 
MAX
(
capMWAC
)::
INT
,

 
DCmax
:
 
MAX
(
capMWDC
)::
INT

FROM
 
'GMSEUS_Arrays_Final_2025_v2_0.parquet'

WHERE
 
instYr
 
IS
 
NOT
 
NULL

GROUP
 
BY
 
1

ORDER
 
BY
 
1
;

┌────────┬───────┬───────┬───────┬────────┬────────┬───────┬───────┐
│ instYr │ count │ ACavg │ DCavg │ ACmean │ DCmean │ ACmax │ DCmax │
│ int64 │ int64 │ int32 │ int32 │ int32 │ int32 │ int32 │ int32 │
├────────┼───────┼───────┼───────┼────────┼────────┼───────┼───────┤
│ 1985 │ 1 │ 14 │ 17 │ 14 │ 17 │ 14 │ 17 │
│ 1990 │ 2 │ 88 │ 90 │ 88 │ 90 │ 92 │ 92 │
│ 2002 │ 1 │ 3 │ 3 │ 3 │ 3 │ 3 │ 3 │
│ 2003 │ 7 │ 2 │ 2 │ 2 │ 2 │ 2 │ 3 │
│ 2005 │ 4 │ 0 │ 0 │ 0 │ 0 │ 0 │ 1 │
│ 2006 │ 64 │ 3 │ 4 │ 3 │ 4 │ 100 │ 125 │
│ 2007 │ 101 │ 2 │ 3 │ 2 │ 3 │ 68 │ 68 │
│ 2008 │ 195 │ 2 │ 3 │ 2 │ 3 │ 226 │ 294 │
│ 2009 │ 268 │ 2 │ 2 │ 2 │ 2 │ 150 │ 195 │
│ 2010 │ 401 │ 2 │ 2 │ 2 │ 2 │ 150 │ 195 │
│ 2011 │ 544 │ 3 │ 3 │ 3 │ 3 │ 175 │ 225 │
│ 2012 │ 777 │ 3 │ 3 │ 3 │ 3 │ 331 │ 430 │
│ 2013 │ 793 │ 4 │ 5 │ 4 │ 5 │ 280 │ 313 │
│ 2014 │ 913 │ 6 │ 7 │ 6 │ 7 │ 586 │ 752 │
│ 2015 │ 910 │ 5 │ 7 │ 5 │ 7 │ 314 │ 398 │
│ 2016 │ 1096 │ 9 │ 12 │ 9 │ 12 │ 300 │ 350 │
│ 2017 │ 1765 │ 5 │ 6 │ 5 │ 6 │ 350 │ 455 │
│ 2018 │ 1941 │ 5 │ 6 │ 5 │ 6 │ 352 │ 458 │
│ 2019 │ 1531 │ 6 │ 8 │ 6 │ 8 │ 300 │ 390 │
│ 2020 │ 1673 │ 11 │ 15 │ 11 │ 15 │ 638 │ 829 │
│ 2021 │ 1705 │ 19 │ 24 │ 19 │ 24 │ 504 │ 656 │
│ 2022 │ 1389 │ 16 │ 21 │ 16 │ 21 │ 868 │ 1128 │
│ 2023 │ 2017 │ 34 │ 44 │ 34 │ 44 │ 1095 │ 1423 │
│ 2024 │ 730 │ 37 │ 44 │ 37 │ 44 │ 868 │ 1128 │
│ 2025 │ 152 │ 18 │ 23 │ 18 │ 23 │ 1129 │ 1468 │
├────────┴───────┴───────┴───────┴────────┴────────┴───────┴───────┤
│ 25 rows 8 columns │
└──────────────────────────────────────────────────────────────────┘

Below is a gradient of the azimuth field in a solar farm in California (-115.47, 35.57). Though these detections are in the panels dataset, someone on Hacker News was kind enough topoint outthat these are mirrors and are a part of theIvanpahSolar Power Facility.

Here is the same visualisation at another park.

The desert is full of these microchip-looking patterns.

 Thank you for taking the time to read this post. I offer both consulting and hands-on development services to clients in North America and Europe. If you'd like to discuss how my offerings can help your business please contact me via 
LinkedIn
.
 

Copyright © 2014 - 2026 Mark Litwintschik. This site's template is based off atemplateby Giulio Fidente.