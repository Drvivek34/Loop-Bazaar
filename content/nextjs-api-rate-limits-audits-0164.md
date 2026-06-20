# The Next.js Api Rate Limits Audits Loop

**Loop ID**: #0164 | **Category**: Content | **Author**: @dennis_r | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits API rate limits in Next.js and stops when no duplicate imports remain.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify API rate limits in Next.js systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Next.js repository. Focus specifically on API rate limits. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no duplicate imports remain.
```

## 🏁 Implementation Steps
1. Scan the Next.js codebase for active API rate limits.
2. Identify any deviations from the target standard: no duplicate imports remain.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Api rate limits meets target standards.
- *Detail*: Checked and confirmed that: no duplicate imports remain.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on API rate limits to minimize run costs.

## 🏷️ Keywords
next.js, content, audits

## 💬 Reviews & Feedback
- **@0xUmbra** (★★★★☆ 4/5): *Successfully implemented this for Next.js. The verification step is extremely reliable.* (2026-05-21)