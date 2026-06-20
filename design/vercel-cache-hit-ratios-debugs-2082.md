# The Vercel Cache Hit Ratios Debugs Loop

**Loop ID**: #2082 | **Category**: Design | **Author**: @james_g | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs cache hit ratios in Vercel and stops when stale state is fully cleared.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify cache hit ratios in Vercel systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Vercel repository. Focus specifically on cache hit ratios. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: stale state is fully cleared.
```

## 🏁 Implementation Steps
1. Scan the Vercel codebase for active cache hit ratios.
2. Identify any deviations from the target standard: stale state is fully cleared.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Cache hit ratios meets target standards.
- *Detail*: Checked and confirmed that: stale state is fully cleared.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on cache hit ratios to minimize run costs.

## 🏷️ Keywords
vercel, design, debugs

## 💬 Reviews & Feedback
- **@lucas_k** (★★★★☆ 4/5): *Successfully implemented this for Vercel. The verification step is extremely reliable.* (2026-04-17)