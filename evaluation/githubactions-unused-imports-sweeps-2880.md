# The GitHub Actions Unused Imports Sweeps Loop

**Loop ID**: #2880 | **Category**: Evaluation | **Author**: @hiten | **Rating**: ⭐ 4.7/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that sweeps unused imports in GitHub Actions and stops when performance benchmark is met.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in GitHub Actions systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the GitHub Actions repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: performance benchmark is met.
```

## 🏁 Implementation Steps
1. Scan the GitHub Actions codebase for active unused imports.
2. Identify any deviations from the target standard: performance benchmark is met.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: performance benchmark is met.

## 💡 Why it works
This loop works because it creates a clear evidence trail of system changes and performance checks.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
github actions, evaluation, sweeps

## 💬 Reviews & Feedback
- **@lSAAGl** (★★★★☆ 4/5): *Successfully implemented this for GitHub Actions. The verification step is extremely reliable.* (2026-05-10)