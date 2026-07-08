# The spec dev-review loop

**Loop ID**: #082 | **Category**: Engineering | **Author**: Ximanta (@kharamdau) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A specification-quality workflow that writes ticket-scoped planning artifacts, applies critical gates, logs review rounds, and stops only at approval or a clear blocker.

## 🎯 Use Case (When to Use)
> Use this when a ticket is too risky or ambiguous to implement until its requirements, edge cases, task plan, and review rubric agree.

## ⚡ System Prompt / Instructions
```
For one ticket or story, write a scoped spec packet: findings, progress, task plan, and a rubric with critical gates and edge cases derived from that ticket. Verify factual claims against the repo before relying on them. After each edit round, run an independent adversarial review against the rubric and require it to check that prior findings remain resolved. If the review finds material issues, fix every affected spec file consistently, append the finding and fix to the review log, and review again. Stop only when the reviewer returns ready with no material findings, or when the round cap is reached and the remaining blocker is logged for human decision.
```

## 🏁 Implementation Steps
1. Derive the spec packet and critical rubric gates from the current ticket, not from a generic template.
2. Verify repo-fact claims before adding them to findings or the task plan.
3. Run an independent adversarial review against the rubric and prior review log.
4. Fix all affected spec files consistently and append each finding and fix to the review log.
5. Stop at a clean ready verdict or a logged blocker after the round cap.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The spec packet is approved against its own rubric with a complete review log.
- *Detail*: The final output includes the spec files, ticket-derived rubric, review rounds, prior-finding regression checks, fixes applied, final ready/not-ready verdict, and any blocker requiring human decision.

## 💡 Why it works
A spec can look complete while its files contradict each other; repeated adversarial review against ticket-specific gates catches drift before implementation.

## ⚠️ Implementation Note
* Do not start implementation inside this loop. Keep review tooling, file names, and round caps adapted to the project rather than hard-coding one platform.

## 🏷️ Keywords
spec review, ticket planning, adversarial review, rubric gates, implementation spec

## 💬 Reviews & Feedback
- *No reviews yet.*