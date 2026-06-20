# The GitHub Actions Bundle Sizes Verifies Loop

**Loop ID**: #2487 | **Category**: Evaluation | **Author**: @elena_r | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that verifies bundle sizes in GitHub Actions and stops when all vulnerabilities are resolved.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify bundle sizes in GitHub Actions systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the GitHub Actions repository. Focus specifically on bundle sizes. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all vulnerabilities are resolved.
```

## 🏁 Implementation Steps
1. Scan the GitHub Actions codebase for active bundle sizes.
2. Identify any deviations from the target standard: all vulnerabilities are resolved.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Bundle sizes meets target standards.
- *Detail*: Checked and confirmed that: all vulnerabilities are resolved.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on bundle sizes to minimize run costs.

## 🏷️ Keywords
github actions, evaluation, verifies

## 💬 Reviews & Feedback
- **@tim_berners** (★★★★☆ 4/5): *Successfully implemented this for GitHub Actions. The verification step is extremely reliable.* (2026-05-25)