# The GitHub Actions Ssl Certificates Standardizes Loop

**Loop ID**: #3134 | **Category**: Evaluation | **Author**: @agent0ai | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that standardizes SSL certificates in GitHub Actions and stops when all checks pass successfully.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify SSL certificates in GitHub Actions systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the GitHub Actions repository. Focus specifically on SSL certificates. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: all checks pass successfully.
```

## 🏁 Implementation Steps
1. Scan the GitHub Actions codebase for active SSL certificates.
2. Identify any deviations from the target standard: all checks pass successfully.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Ssl certificates meets target standards.
- *Detail*: Checked and confirmed that: all checks pass successfully.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on SSL certificates to minimize run costs.

## 🏷️ Keywords
github actions, evaluation, standardizes

## 💬 Reviews & Feedback
- **@hiten** (★★★★★ 5/5): *Successfully implemented this for GitHub Actions. The verification step is extremely reliable.* (2026-01-14)