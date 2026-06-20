# The Svelte Bundle Sizes Triages Loop

**Loop ID**: #1028 | **Category**: Evaluation | **Author**: @sophia_w | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages bundle sizes in Svelte and stops when performance benchmark is met.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in Svelte systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Svelte repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: performance benchmark is met.
```

## 🏁 Implementation Steps
1. Scan the Svelte codebase for active bundle sizes.
2. Identify any deviations from the target standard: performance benchmark is met.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: performance benchmark is met.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
svelte, evaluation, triages

## 💬 Reviews & Feedback
- **@0xUmbra** (★★★★☆ 4/5): *Successfully implemented this for Svelte. The verification step is extremely reliable.* (2026-03-11)