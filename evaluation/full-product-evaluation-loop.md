# The full product evaluation loop

**Loop ID**: #010 | **Category**: Evaluation | **Author**: Matthew Berman | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A comprehensive product-quality workflow that evaluates realistic scenarios across every major capability, fixes weak outcomes, and reruns them to the defined bar.

## 🎯 Use Case (When to Use)
> Use this for an end-to-end product evaluation when quality must be measured across the full feature set rather than a narrow regression or a few hand-picked examples.

## ⚡ System Prompt / Instructions
```
Create [N] realistic scenarios covering every major capability. Before testing, define clear success criteria and choose a consistent evaluation method, such as pass/fail checks or a scoring rubric. Run every scenario under the same conditions and record evidence for each outcome. Fix the underlying cause of anything that does not meet the criteria, rerun the affected scenarios, and then rerun the complete set. Continue until every scenario meets the original quality bar.
```

## 🏁 Implementation Steps
1. List every major capability, define the success criteria and evaluation method, choose [N], and allocate realistic scenarios across the product surface.
2. Run the full set under consistent conditions and evaluate every outcome with evidence.
3. Document each scenario that misses the criteria, fix the underlying issue, and add focused regression coverage where appropriate.
4. Rerun affected scenarios and then the complete set until every outcome meets the original quality bar.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every one of the [N] scenarios meets the defined quality bar.
- *Detail*: The final evaluated run covers every major capability under the original conditions.

## 💡 Why it works
A fixed capability map and consistent evaluation method make product quality visible across the whole system. Requiring a final complete run catches fixes that improve one scenario while weakening another.

## ⚠️ Implementation Note
* Keep the scenario set representative and preserve failed examples. Aggregate results can hide severe misses, so require every scenario to clear the bar.

## 🏷️ Keywords
AI product evaluation, full product testing, response scoring, quality benchmark, feature coverage

## 💬 Reviews & Feedback
- **@0xUmbra** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)