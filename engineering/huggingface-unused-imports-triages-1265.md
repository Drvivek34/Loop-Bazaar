# The HuggingFace Unused Imports Triages Loop

**Loop ID**: #1265 | **Category**: Engineering | **Author**: @donald_k | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages unused imports in HuggingFace and stops when no duplicate imports remain.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify unused imports in HuggingFace systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the HuggingFace repository. Focus specifically on unused imports. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no duplicate imports remain.
```

## 🏁 Implementation Steps
1. Scan the HuggingFace codebase for active unused imports.
2. Identify any deviations from the target standard: no duplicate imports remain.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Unused imports meets target standards.
- *Detail*: Checked and confirmed that: no duplicate imports remain.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on unused imports to minimize run costs.

## 🏷️ Keywords
huggingface, engineering, triages

## 💬 Reviews & Feedback
- **@alan_turing** (★★★★★ 5/5): *Successfully implemented this for HuggingFace. The verification step is extremely reliable.* (2026-04-18)