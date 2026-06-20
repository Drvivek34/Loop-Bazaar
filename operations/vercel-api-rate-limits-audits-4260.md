# The Vercel Api Rate Limits Audits Loop

**Loop ID**: #4260 | **Category**: Operations | **Author**: @linus_t | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that audits API rate limits in Vercel and stops when compliance report returns zero warnings.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify API rate limits in Vercel systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Vercel repository. Focus specifically on API rate limits. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: compliance report returns zero warnings.
```

## 🏁 Implementation Steps
1. Scan the Vercel codebase for active API rate limits.
2. Identify any deviations from the target standard: compliance report returns zero warnings.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Api rate limits meets target standards.
- *Detail*: Checked and confirmed that: compliance report returns zero warnings.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on API rate limits to minimize run costs.

## 🏷️ Keywords
vercel, operations, audits

## 💬 Reviews & Feedback
- **@claudio_d** (★★★★☆ 4/5): *Successfully implemented this for Vercel. The verification step is extremely reliable.* (2026-03-03)