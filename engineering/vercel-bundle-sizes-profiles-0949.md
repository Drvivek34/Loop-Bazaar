# The Vercel Bundle Sizes Profiles Loop

**Loop ID**: #0949 | **Category**: Engineering | **Author**: @james_g | **Rating**: ⭐ 4.1/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that profiles bundle sizes in Vercel and stops when test coverage reaches 100%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in Vercel systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Vercel repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: test coverage reaches 100%.
```

## 🏁 Implementation Steps
1. Scan the Vercel codebase for active bundle sizes.
2. Identify any deviations from the target standard: test coverage reaches 100%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: test coverage reaches 100%.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
vercel, engineering, profiles

## 💬 Reviews & Feedback
- **@donald_k** (★★★★☆ 4/5): *Successfully implemented this for Vercel. The verification step is extremely reliable.* (2026-01-16)