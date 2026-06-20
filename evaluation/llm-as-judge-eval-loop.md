# LLM-as-judge evaluation loop

**Loop ID**: #5062 | **Category**: Evaluation | **Author**: Zheng et al. (MT-Bench) | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Use a strong model as a judge to score outputs against a rubric, iterating prompts/models until scores plateau.

## 🎯 Use Case (When to Use)
> When you need scalable, repeatable quality scoring of generations.

## ⚡ System Prompt / Instructions
```
Score each candidate against a fixed rubric with a judge model; compare variants; iterate the system until the judge scores plateau.
```

## 🏁 Implementation Steps
1. Define a scoring rubric
2. Generate candidates
3. Judge-score each against the rubric
4. Iterate the system until scores plateau

## 🛑 Stopping Condition (Verification)
**Verification Check**: Score plateau
- *Detail*: Judge scores stop improving across iterations.

## 💡 Why it works
A consistent judge turns vague quality into a repeatable optimization signal.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
llm as judge, evaluation, rubric, mt-bench

## 💬 Reviews & Feedback
- *No reviews yet.*