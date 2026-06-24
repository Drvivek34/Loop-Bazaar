# The stable-frame-rate loop

**Loop ID**: #054 | **Category**: Engineering | **Author**: Aviv Sheriff (@Avivsh) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable game-performance workflow that measures frame time, CPU, GPU, and memory under fixed conditions and keeps only regression-free optimizations.

## 🎯 Use Case (When to Use)
> Use this when a game or interactive build has unstable frame rate and performance can be measured under one representative, repeatable scenario.

## ⚡ System Prompt / Instructions
```
Improve the frame-rate stability of [game or interactive build]. Before editing, define one repeatable benchmark with the same scene, inputs, hardware, build, resolution, and settings. If no scenario or targets are supplied, propose representative values and state them before proceeding. Record frame-time distribution, average FPS, minimum FPS, CPU use, GPU use, and memory behavior. Identify the largest measured bottleneck and make one focused optimization. Rerun the complete benchmark under the same conditions. Keep the change only if it improves the target without regressing another metric or changing expected behavior. Repeat until [FPS target] holds for [stability period] with no dip below [FPS floor], memory remains below [memory target] without an upward trend, and CPU stays below [CPU target] across two consecutive runs. Stop on success, two rounds without measurable progress, a blocker, or [iteration budget]. Finish with the benchmark setup, before-and-after measurements, retained changes, reverted attempts, and remaining bottlenecks.
```

## 🏁 Implementation Steps
1. Freeze a representative benchmark scenario and record the frame-time, FPS, CPU, GPU, and memory baseline.
2. Identify the largest measured bottleneck and make one focused optimization.
3. Rerun the full benchmark and keep the change only when it improves the target without another regression.
4. Repeat until every threshold holds twice, progress stalls, the budget ends, or a blocker appears.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The frame-rate targets hold under the fixed benchmark without another metric regressing.
- *Detail*: Two consecutive runs meet the FPS, frame-time, CPU, GPU, and memory criteria under the original scene, inputs, hardware, build, resolution, and settings.

## 💡 Why it works
Average FPS can hide stutter, resource growth, and tradeoffs between CPU and GPU work. Fixed conditions and full-metric retesting prevent a local improvement from becoming a broader regression.

## ⚠️ Implementation Note
* Record the exact hardware, build, scene, inputs, resolution, and settings. Do not compare runs made under different conditions as if they were equivalent.

## 🏷️ Keywords
stable frame rate, game performance optimization, frame time benchmark, FPS stability, CPU GPU profiling

## 💬 Reviews & Feedback
- *No reviews yet.*