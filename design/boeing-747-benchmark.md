# The Boeing 747 benchmark

**Loop ID**: #021 | **Category**: Design | **Author**: @victormustar | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A vision benchmark in which an agent builds a Boeing 747 from Three.js primitives, renders nine repeatable angles, and fixes what each view reveals.

## 🎯 Use Case (When to Use)
> Use this as a concrete Three.js vision benchmark, or adapt the same capture-and-critic pattern to another rendered subject.

## ⚡ System Prompt / Instructions
```
Before building, choose reference images, a scoring rubric, [visual threshold], and [budget]. Build the most realistic Boeing 747 you can from Three.js primitives, then create a rig that screenshots nine repeatable angles. After each change, render and score the same views, have a critic identify the weakest feature, and fix it without regressing stronger views. Keep the best version. Stop at the threshold, stalled progress, or budget. Finish with the model, nine renders, scores, remaining gaps, and run summary.
```

## 🏁 Implementation Steps
1. Choose reference images, a scoring rubric, a visual threshold, and a budget; then build the first Boeing 747 from Three.js primitives.
2. Create a repeatable rig that renders the same nine angles after every meaningful change.
3. Score each view against the references, have a critic identify the weakest feature, and fix it without losing stronger work.
4. Keep the best version and repeat until all nine views clear the visual bar or another named stop is reached.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The Boeing 747 meets the visual bar from all nine angles.
- *Detail*: The same camera rig and rubric show every required view meeting the preset threshold, or the run reports stagnation, budget exhaustion, and remaining gaps.

## 💡 Why it works
The nine-angle rig turns a subjective 3D build into a repeatable visual test. Critiquing the same views after each change exposes problems that one hero render can hide.

## ⚠️ Implementation Note
* The source run used a Boeing 747, Three.js primitives, nine camera angles, and repeated critics. To adapt it, replace the subject and renderer but keep fixed views, a visible quality bar, and preserved comparison renders.

## 🏷️ Keywords
Boeing 747 benchmark, Three.js agent workflow, vision self-verification, 3D reconstruction loop, camera inspection system

## 💬 Reviews & Feedback
- **@marcus_a** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)