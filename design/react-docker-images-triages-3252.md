# The React Docker Images Triages Loop

**Loop ID**: #3252 | **Category**: Design | **Author**: @bjarnes | **Rating**: ⭐ 4.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages Docker images in React and stops when compliance report returns zero warnings.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Docker images in React systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the React repository. Focus specifically on Docker images. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: compliance report returns zero warnings.
```

## 🏁 Implementation Steps
1. Scan the React codebase for active Docker images.
2. Identify any deviations from the target standard: compliance report returns zero warnings.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Docker images meets target standards.
- *Detail*: Checked and confirmed that: compliance report returns zero warnings.

## 💡 Why it works
This loop works because it forces systematic optimization instead of relying on developer memory.

## ⚠️ Implementation Note
* Keep the scope focused on Docker images to minimize run costs.

## 🏷️ Keywords
react, design, triages

## 💬 Reviews & Feedback
- **@inferencegod** (★★★★☆ 4/5): *Successfully implemented this for React. The verification step is extremely reliable.* (2026-03-20)