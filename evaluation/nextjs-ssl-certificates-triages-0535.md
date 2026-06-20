# The Next.js Ssl Certificates Triages Loop

**Loop ID**: #0535 | **Category**: Evaluation | **Author**: @claudio_d | **Rating**: ⭐ 4.3/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages SSL certificates in Next.js and stops when stale state is fully cleared.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify SSL certificates in Next.js systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Next.js repository. Focus specifically on SSL certificates. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: stale state is fully cleared.
```

## 🏁 Implementation Steps
1. Scan the Next.js codebase for active SSL certificates.
2. Identify any deviations from the target standard: stale state is fully cleared.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Ssl certificates meets target standards.
- *Detail*: Checked and confirmed that: stale state is fully cleared.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on SSL certificates to minimize run costs.

## 🏷️ Keywords
next.js, evaluation, triages

## 💬 Reviews & Feedback
- **@tim_berners** (★★★★☆ 4/5): *Successfully implemented this for Next.js. The verification step is extremely reliable.* (2026-02-26)