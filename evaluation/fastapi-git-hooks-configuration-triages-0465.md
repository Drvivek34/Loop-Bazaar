# The FastAPI Git Hooks Configuration Triages Loop

**Loop ID**: #0465 | **Category**: Evaluation | **Author**: @victormustar | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that triages Git hooks configuration in FastAPI and stops when no regressions are detected.

## 🎯 Use Case (When to Use)
> Use this whenever you need to check or modify Git hooks configuration in FastAPI systems and need a strict exit criteria.

## ⚡ System Prompt / Instructions
```
Analyze the FastAPI repository. Focus specifically on Git hooks configuration. Run the local inspection checks, locate any anomalies, drift, or inefficiencies. Modify the relevant code paths, verify the modifications against the local checks, and repeat the cycle until the stopping condition is fully met: no regressions are detected.
```

## 🏁 Implementation Steps
1. Scan the FastAPI codebase for active Git hooks configuration.
2. Identify any deviations from the target standard: no regressions are detected.
3. Implement corrections, optimization scripts, or code repairs.
4. Rerun the verification command to check the updated state.
5. Log output details and repeat until no deviations remain.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Git hooks configuration meets target standards.
- *Detail*: Checked and confirmed that: no regressions are detected.

## 💡 Why it works
This loop works because it prevents manual checklist drift and guarantees repeatable quality.

## ⚠️ Implementation Note
* Keep the scope focused on Git hooks configuration to minimize run costs.

## 🏷️ Keywords
fastapi, evaluation, triages

## 💬 Reviews & Feedback
- **@claudio_d** (★★★★☆ 4/5): *Successfully implemented this for FastAPI. The verification step is extremely reliable.* (2026-04-29)