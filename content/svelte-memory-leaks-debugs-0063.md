# The Svelte Memory Leaks Debugs Loop

**Loop ID**: #0063 | **Category**: Content | **Author**: @tim_berners | **Rating**: ⭐ 4.1/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that debugs memory leaks in Svelte and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify memory leaks in Svelte systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the Svelte repository. Focus specifically on memory leaks. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the Svelte codebase for active memory leaks.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Memory leaks meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on memory leaks to minimize run costs.

## 🏷️ Keywords
svelte, content, debugs

## 💬 Reviews & Feedback
- **@ranvier2d2** (★★★★☆ 4/5): *Successfully implemented this for Svelte. The verification step is extremely reliable.* (2026-06-05)