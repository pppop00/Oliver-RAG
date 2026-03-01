---
title: "Perceptual Reasoning Notes: From Constancy Benchmarks to Large-Scale Video Reasoning"
type: "reflection"
timeline:
  start: "2026-03"
  end: "2026-03"
  period: "grad_and_career"
tags: ["reflection", "research", "vlm", "video-reasoning", "benchmarking"]
domains: ["ai-research", "computer-vision"]
status: "completed"
importance: 5
created: 2026-03-01
updated: 2026-03-01
related:
  - "../projects/probing-perceptual-constancy-in-vlms.md"
  - "../projects/vbvr-a-very-big-video-reasoning-suite.md"
reflection_type: "project"
---

## Summary
The two research papers form a coherent progression: first diagnose perceptual stability in VLMs,
then scale toward structured video reasoning tasks with reproducible evaluation.
Together they suggest that model quality cannot be measured by visual realism alone.

## What the Constancy Work Clarifies
- Perceptual robustness is not uniform across color, size, and shape.
- Shape constancy appears easier for current models than color and size.
- Model scaling helps, but gains differ by perceptual domain.

## What the VBVR Work Adds
- A larger and more systematic task space for video reasoning.
- Verifiable scoring rather than opaque model-as-judge dependency.
- Initial evidence of generalization with scale, but persistent human-performance gap.

## Practical Takeaway
For future model evaluation workflows, use both:
1. Controlled micro-benchmarks for specific cognitive abilities.
2. Large-scale task suites to test transfer and generalization under broader variation.

## Related Projects
- [Probing Perceptual Constancy in VLMs](../projects/probing-perceptual-constancy-in-vlms.md)
- [A Very Big Video Reasoning Suite](../projects/vbvr-a-very-big-video-reasoning-suite.md)
