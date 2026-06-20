# The TailwindCSS Docker Images Sweeps Loop

**Loop ID**: #3447 | **Category**: Operations | **Author**: @swayam | **Rating**: ⭐ 4.4/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that sweeps Docker images in TailwindCSS and stops when test coverage reaches 100%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in TailwindCSS systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the TailwindCSS repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: test coverage reaches 100%.
```

## 🏁 Implementation Steps
1. Scan the TailwindCSS codebase for active Docker images.
2. Identify any deviations from the target standard: test coverage reaches 100%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: test coverage reaches 100%.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
tailwindcss, operations, sweeps

## 💬 Reviews & Feedback
- **@linus_t** (★★★★☆ 4/5): *Successfully implemented this for TailwindCSS. The verification step is extremely reliable.* (2026-02-01)