---
title: "A Very Big Video Reasoning Suite (VBVR)"
type: "project"
timeline:
  start: "2026-02"
  end: "2026-02"
  period: "grad_and_career"
tags: ["Video-Reasoning", "Benchmark", "Dataset", "Cognitive-Architecture", "VLM-Evaluation", "Research"]
domains: ["research", "ai", "computer-vision"]
status: "completed"
importance: 5
created: 2026-03-01
updated: 2026-03-01
related:
  - "../skills/machine-learning-and-statistical-modeling.md"
  - "../reflections/perceptual-reasoning-research-notes-2026.md"
paper: "https://arxiv.org/abs/2602.20159"
website: "https://video-reason.com"
---

## Summary
VBVR is a large-scale video reasoning suite designed for training and evaluating reasoning in video models.
It introduces a taxonomy-based dataset and a rule-verifiable benchmark pipeline to support reproducible
scaling studies beyond pure visual quality evaluation.

## Project Overview
- Project type: Multi-institution research project
- Role: Co-author (Zelong Hong listed in author list)
- Timepoint: Preprint released in February 2026
- Public resources: paper + benchmark website

## Problem Context
Video generation quality improved rapidly, but video reasoning ability remained under-measured and difficult
to scale due to limited training data and inconsistent evaluation practice.

## Core Contributions Reported in the Paper
1. Dataset scale and coverage:
- 200 curated reasoning tasks organized by five cognitive faculties: abstraction, knowledge, spatiality, perception, transformation.
- 2,015,000 images and 1,007,500 videos.
- 1,000,000 training samples and 7,500 test samples.

2. Evaluation framework:
- VBVR-Bench with rule-based, verifiable scorers.
- Reported human alignment above rho > 0.9 with automated scores.

3. Scaling observations:
- In-domain and out-of-domain performance improved with training scale.
- Persistent gap remained vs human-level performance, indicating architecture limitations beyond data scale.

## Research Value for Personal RAG
- Strong evidence of benchmark design and large-scale data curation involvement.
- Supports queries around research direction: video reasoning, cognitive-task design, and robust model evaluation.

## Related Skills and Notes
- [Machine Learning and Statistical Modeling](../skills/machine-learning-and-statistical-modeling.md)
- [Perceptual Reasoning Research Notes](../reflections/perceptual-reasoning-research-notes-2026.md)
- [projects-index.yaml](../structured-data/projects-index.yaml)
- [VBVR Raw Fulltext Extract](./sources/vbvr-2026-fulltext.md)
