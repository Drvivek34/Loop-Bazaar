# The Vue Bundle Sizes Profiles Loop

**Loop ID**: #2546 | **Category**: Operations | **Author**: @grace_hopper | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that profiles bundle sizes in Vue and stops when target threshold is reached.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in Vue systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Vue repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: target threshold is reached.
```

## 🏁 Implementation Steps
1. Scan the Vue codebase for active bundle sizes.
2. Identify any deviations from the target standard: target threshold is reached.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: target threshold is reached.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
vue, operations, profiles

## 💬 Reviews & Feedback
- **@linus_t** (★★★★☆ 4/5): *Successfully implemented this for Vue. The verification step is extremely reliable.* (2026-03-27)