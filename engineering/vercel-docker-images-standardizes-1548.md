# The Vercel Docker Images Standardizes Loop

**Loop ID**: #1548 | **Category**: Engineering | **Author**: @richard_s | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that standardizes Docker images in Vercel and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in Vercel systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Vercel repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the Vercel codebase for active Docker images.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
vercel, engineering, standardizes

## 💬 Reviews & Feedback
- **@richard_s** (★★★★★ 5/5): *Successfully implemented this for Vercel. The verification step is extremely reliable.* (2026-03-06)