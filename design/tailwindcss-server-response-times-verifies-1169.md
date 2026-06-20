# The TailwindCSS Server Response Times Verifies Loop

**Loop ID**: #1169 | **Category**: Design | **Author**: @inferencegod | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that verifies server response times in TailwindCSS and stops when error rate drops below 0.1%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify server response times in TailwindCSS systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the TailwindCSS repository. Focus specifically on server response times. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: error rate drops below 0.1%.
```

## 🏁 Implementation Steps
1. Scan the TailwindCSS codebase for active server response times.
2. Identify any deviations from the target standard: error rate drops below 0.1%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Server response times meets target standards.
- *Detail*: Checked and confirmed that: error rate drops below 0.1%.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on server response times to minimize run costs.

## 🏷️ Keywords
tailwindcss, design, verifies

## 💬 Reviews & Feedback
- **@grace_hopper** (★★★★☆ 4/5): *Successfully implemented this for TailwindCSS. The verification step is extremely reliable.* (2026-03-26)