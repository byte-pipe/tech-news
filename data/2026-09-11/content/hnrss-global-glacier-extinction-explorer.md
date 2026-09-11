---
title: Global Glacier Extinction Explorer
url: https://glacierextinction.com
site_name: hnrss
content_file: hnrss-global-glacier-extinction-explorer
fetched_at: '2026-09-11T21:35:50.395724'
original_url: https://glacierextinction.com
date: '2026-09-11'
description: Global Glacier Extinction Explorer
tags:
- hackernews
- hnrss
---

☰
Controls

Loading glacier data…

✕

⬚

3D

## About this map

✕

Glacier changes are traditionally quantified in terms of total (regional) mass and area loss, but such
 metrics do not fully capture the disappearance of individual glaciers. Yet every glacier, no matter how
 small, can matter. Beyond their contribution to sea-level rise or regional water resources, glaciers hold
 important cultural, ecological, and societal value, often deeply rooted in local landscapes and
 communities. In the context of the UN International Year of Glacier Preservation (2025), this study
 therefore shifts the focus towards the fate of individual glaciers worldwide.

To assess glacier extinction, two complementary criteria are used. A glacier is considered disappeared
 (extinct) when its area drops below 0.01 km², consistent with commonly used inventory
 thresholds, or when its remaining volume falls below 1% of its initial value, indicating that only a
 negligible ice body persists. To derive volume and area trajectories for each glacier, three global
 glacier models (GloGEM, OGGM, PyGEM) are used, combined with multiple General Circulation Models and
 emission scenarios corresponding to projected temperature increases of +1.5°C, +2.0°C,
 +2.7°C, and +4.0°C. All trajectories are then combined to determine median extinction years, as
 well as Q25 and Q75 ranges (i.e. the 25% and 75% probability intervals). These results are shown on
 the map.

Extinction is defined relative to the initial glacier outlines from the Randolph Glacier Inventory
 (RGI v6.0). Glacier fragmentation during retreat is not accounted for; all remaining ice within
 the original glacier extent is treated as part of the same glacier.

### Data sources

* Extinction projections:Van Tricht, L., Zekollari, H., Huss, M. et al. Peak glacier extinction in the mid-twenty-first
 century.Nature Climate Change16, 143–147 (2026).doi:10.1038/s41558-025-02513-9
* Regional and glacier-specific results(including those shown here) are publicly
 available on Zenodo:doi:10.5281/zenodo.17371641
* Glacier outlines:RGI Consortium (2017). Randolph Glacier Inventory — A Dataset of
 Global Glacier Outlines, Version 6. Boulder, Colorado USA. NSIDC: National Snow and Ice Data Center.doi:10.7265/4m1f-gd79
* Ice volume:Farinotti, D., Huss, M., Fürst, J. J., Landmann, J.,
 Machguth, H., Maussion, F., and Pandit, A.: A consensus estimate for the ice thickness distribution
 of all glaciers on Earth.Nat. Geosci., 12, 168–173,doi:10.1038/s41561-019-0300-3, 2019.

### Acknowledgements

This application is built on open-source software:MapLibre GL JS(map rendering),PMTiles(vector
 tile streaming),GeoPandasandNumPy(data processing),GDAL / ogr2ogr(tile generation),
 andgo-pmtiles(tile packaging).
 The web application was designed and built byK. Van
 Tricht,
 with the assistance of Claude Sonnet 4.6 and GPT-6 Astra for the frontend code and data
 pipeline structure.

### Feedback

If you notice incorrect data or have suggestions for improved naming, please send them tolander.van.tricht@vub.be.