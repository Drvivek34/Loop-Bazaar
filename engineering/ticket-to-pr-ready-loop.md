# The ticket-to-PR-ready loop

**Loop ID**: #016 | **Category**: Engineering | **Author**: Hiten Shah | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded engineering workflow that turns a ticket, failing behavior, or customer complaint into a proven root cause, minimal patch, and reviewer-ready handoff.

## 🎯 Use Case (When to Use)
> Use this when a real but loosely written ticket, bug report, or customer complaint needs to become a bounded engineering change with enough proof for a fast review.

## ⚡ System Prompt / Instructions
```
Take a ticket, bug report, failing behavior, or customer complaint and turn it into a review-ready patch. Reproduce the failure in the smallest representative environment, prove the root cause, make the smallest credible fix, and rerun the original reproduction plus relevant regression tests. If the issue cannot be reproduced after two serious attempts, say so. Do not fold unrelated refactors into the patch. Finish with the cause, changed files, before-and-after proof, risks, and pull-request summary.
```

## 🏁 Implementation Steps
1. State the expected and actual behavior, then reproduce the failure in the smallest representative environment.
2. Trace the behavior to a root cause and confirm the causal link with evidence.
3. Implement the smallest credible fix, avoiding unrelated cleanup or hidden refactors.
4. Repeat the original reproduction, run relevant regression checks, and package the result for review.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The failure is fixed, verified, and ready for review.
- *Detail*: The issue reproduces before the fix, no longer reproduces afterward, and relevant regression checks pass.

## 💡 Why it works
The loop closes the gap between something being wrong and a reviewer being able to trust the patch. Reproduction, evidence, bounded scope, and a structured handoff remove the detective work from review.

## ⚠️ Implementation Note
* Match the proof to the failure: screenshots or recordings for UI issues, tests or logs for backend behavior, benchmark deltas for performance, and sanitized traces for integrations.

## 🏷️ Keywords
AI coding agent, ticket to pull request, bug reproduction, root cause analysis, review-ready patch

## 💬 Reviews & Feedback
- **@lucas_k** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)