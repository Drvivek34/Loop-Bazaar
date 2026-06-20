# The GitHub Actions Docker Images Cleans up Loop

**Loop ID**: #2539 | **Category**: Design | **Author**: @swayam | **Rating**: ⭐ 4.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that cleans up Docker images in GitHub Actions and stops when no duplicate imports remain.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in GitHub Actions systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the GitHub Actions repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no duplicate imports remain.
```

## 🏁 Implementation Steps
1. Scan the GitHub Actions codebase for active Docker images.
2. Identify any deviations from the target standard: no duplicate imports remain.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: no duplicate imports remain.

## 💡 Why it works
This loop works because it ensures security policies are consistently enforced without gaps.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
github actions, design, cleans up

## 💬 Reviews & Feedback
- **@elena_r** (★★★★☆ 4/5): *Successfully implemented this for GitHub Actions. The verification step is extremely reliable.* (2026-05-17)