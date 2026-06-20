# The Kubernetes Svg Assets Refactors Loop

**Loop ID**: #1002 | **Category**: Evaluation | **Author**: @donald_k | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that refactors SVG assets in Kubernetes and stops when documentation is fully aligned with implementation.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify SVG assets in Kubernetes systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Kubernetes repository. Focus specifically on SVG assets. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: documentation is fully aligned with implementation.
```

## 🏁 Implementation Steps
1. Scan the Kubernetes codebase for active SVG assets.
2. Identify any deviations from the target standard: documentation is fully aligned with implementation.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Svg assets meets target standards.
- *Detail*: Checked and confirmed that: documentation is fully aligned with implementation.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on SVG assets to minimize run costs.

## 🏷️ Keywords
kubernetes, evaluation, refactors

## 💬 Reviews & Feedback
- **@alan_turing** (★★★★☆ 4/5): *Successfully implemented this for Kubernetes. The verification step is extremely reliable.* (2026-03-20)