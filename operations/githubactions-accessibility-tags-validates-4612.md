# The GitHub Actions Accessibility Tags Validates Loop

**Loop ID**: #4612 | **Category**: Operations | **Author**: @tim_berners | **Rating**: ⭐ 4.7/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that validates accessibility tags in GitHub Actions and stops when test coverage reaches 100%.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify accessibility tags in GitHub Actions systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the GitHub Actions repository. Focus specifically on accessibility tags. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: test coverage reaches 100%.
```

## 🏁 Implementation Steps
1. Scan the GitHub Actions codebase for active accessibility tags.
2. Identify any deviations from the target standard: test coverage reaches 100%.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Accessibility tags meets target standards.
- *Detail*: Checked and confirmed that: test coverage reaches 100%.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on accessibility tags to minimize run costs.

## 🏷️ Keywords
github actions, operations, validates

## 💬 Reviews & Feedback
- **@dennis_r** (★★★★☆ 4/5): *Successfully implemented this for GitHub Actions. The verification step is extremely reliable.* (2026-01-22)