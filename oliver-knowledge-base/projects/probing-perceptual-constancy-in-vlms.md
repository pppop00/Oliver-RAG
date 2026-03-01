---
title: "Probing Perceptual Constancy in Large Vision-Language Models"
type: "project"
timeline:
  start: "2025-02"
  end: "2025-02"
  period: "grad_and_career"
tags: ["VLM", "Perceptual-Constancy", "Benchmark", "Statistical-Analysis", "Research"]
domains: ["research", "ai", "computer-vision"]
status: "completed"
importance: 4
created: 2026-03-01
updated: 2026-03-01
related:
  - "../projects/vbvr-a-very-big-video-reasoning-suite.md"
  - "../reflections/perceptual-reasoning-research-notes-2026.md"
paper: "https://arxiv.org/abs/2502.20173"
---

## Summary
This work studies perceptual constancy behavior in large vision-language models through controlled cognitive tasks.
The benchmark reveals non-uniform performance across color, size, and shape constancy and shows clear scaling
effects with model size.

## Project Overview
- Project type: Research benchmark and analysis
- Role: Co-author (Zelong Hong listed in author list)
- Timepoint: Preprint released in February 2025
- Experimental scope: 155 models and 236 experiments

## Key Findings Reported
1. Domain performance split:
- Shape constancy mean accuracy: 0.723
- Color constancy mean accuracy: 0.588
- Size constancy mean accuracy: 0.584

2. Statistical evidence:
- Significant domain differences via ANOVA.
- Shape constancy significantly higher than color and size.

3. Scaling behavior:
- Positive correlation between model size and perceptual constancy performance.
- Strongest scaling effect reported for size constancy among the three domains.

## Why This Matters in the Knowledge Base
- Adds research evidence for evaluating model robustness under distribution and perspective variation.
- Complements VBVR by connecting perceptual invariance to broader video reasoning and world-modeling goals.

## Related Skills and Links
- [Machine Learning and Statistical Modeling](../skills/machine-learning-and-statistical-modeling.md)
- [Perceptual Reasoning Research Notes](../reflections/perceptual-reasoning-research-notes-2026.md)
- [projects-index.yaml](../structured-data/projects-index.yaml)
- [Perceptual Constancy Raw Fulltext Extract](./sources/perceptual-constancy-vlms-2025-fulltext.md)
