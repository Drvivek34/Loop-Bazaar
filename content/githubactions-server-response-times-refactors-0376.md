# The GitHub Actions Server Response Times Refactors Loop

**Loop ID**: #0376 | **Category**: Content | **Author**: @steipete | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that refactors server response times in GitHub Actions and stops when all checks pass successfully.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify server response times in GitHub Actions systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the GitHub Actions repository. Focus specifically on server response times. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all checks pass successfully.
```

## 🏁 Implementation Steps
1. Scan the GitHub Actions codebase for active server response times.
2. Identify any deviations from the target standard: all checks pass successfully.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Server response times meets target standards.
- *Detail*: Checked and confirmed that: all checks pass successfully.

## 💡 Why it works
This loop works because it reduces regression risk by integrating tests directly into the loop.

## ⚠️ Implementation Note
* Keep the scope focused on server response times to minimize run costs.

## 🏷️ Keywords
github actions, content, refactors

## 💬 Reviews & Feedback
- **@ken_t** (★★★★☆ 4/5): *Successfully implemented this for GitHub Actions. The verification step is extremely reliable.* (2026-05-21)