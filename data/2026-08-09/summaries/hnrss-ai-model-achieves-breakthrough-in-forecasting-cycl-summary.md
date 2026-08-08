---
title: AI model achieves breakthrough in forecasting cyclones — Google DeepMind
url: https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones/
date: 2026-08-08
site: hnrss
model: gpt-oss:120b-cloud
summarized_at: 2026-08-09T00:36:48.805933
---

# AI model achieves breakthrough in forecasting cyclones — Google DeepMind

# WeatherNext: AI model achieves breakthrough in forecasting cyclones

## Overview
- WeatherNext AI model delivers state‑of‑the‑art cyclone forecasts, extending accurate predictions by roughly one extra day.
- The improvement is comparable to a decade of meteorological progress.
- The model and its weights are now open‑sourced to enable broader research and operational use.

## Key Achievements
- Predicts cyclone track, intensity, and wind structure with higher accuracy than previous models.
- Three‑day forecasts match the quality of older two‑day forecasts from competing systems.
- Generates 1,000‑member ensembles in under a minute on a TPU, providing detailed probability maps.
- Demonstrated real‑world impact during the 2025 season, notably improving forecasts for Hurricane Melissa.

## Technical Approach
- Single AI model bridges global atmospheric dynamics and fine‑scale cyclone processes.
- Trained end‑to‑end on ~20 TB of global atmospheric data and the IBTrACS database (~5,000 storms).
- Uses Functional Generative Networks (FGNs) to produce efficient ensembles and capture uncertainty.
- Operates with coarse input resolution (28 km × 28 km), far finer than traditional models, and still achieves high intensity forecast skill.
- A mini version (WeatherNext 2‑mini) runs at 111 km × 111 km resolution on a single TPU, suitable for Colab notebooks.

## Real‑World Impact
- Assisted the National Hurricane Center in issuing an early warning for Hurricane Melissa, allowing critical preparation time in Jamaica.
- Supports forecasters with 1,000 possible scenario forecasts per cyclone to aid decision‑making.
- Enables rapid assessment of rare, high‑impact events such as rapid intensification.

## Open‑Source Release
- Code, model weights, and two model families (WeatherNext Cyclones and WeatherNext 2, plus WeatherNext 2‑mini) are publicly available.
- Intended for academic research, operational forecasting, and development of specialized local models.
- Forecast visualizations are accessible via Weather Lab, integrated into Google Earth AI, showing temperature, precipitation, wind, and cyclone tracks.

## Future Directions
- Invite collaboration from researchers, meteorological agencies, and NGOs to extend and refine the models.
- Aim to build a collaborative ecosystem that combines AI advances with human expertise to improve safety and climate resilience.