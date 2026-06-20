# The Flask Cache Hit Ratios Sweeps Loop

**Loop ID**: #1127 | **Category**: Design | **Author**: @steipete | **Rating**: ⭐ 4.7/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that sweeps cache hit ratios in Flask and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify cache hit ratios in Flask systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Flask repository. Focus specifically on cache hit ratios. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the Flask codebase for active cache hit ratios.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Cache hit ratios meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on cache hit ratios to minimize run costs.

## 🏷️ Keywords
flask, design, sweeps

## 💬 Reviews & Feedback
- **@agent0ai** (★★★★☆ 4/5): *Successfully implemented this for Flask. The verification step is extremely reliable.* (2026-06-10)