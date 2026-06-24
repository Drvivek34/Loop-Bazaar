# The Loop Hiring Manager

**Loop ID**: #057 | **Category**: Operations | **Author**: Eric Lott | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A portfolio review that finds unowned recurring outcomes, reuses published loops when possible, and recommends one bounded manual trial before adoption.

## 🎯 Use Case (When to Use)
> Use this when a project has recurring agent work or automation ideas but needs to decide which loops are actually worth adopting.

## ⚡ System Prompt / Instructions
```
Decide whether [project or current workspace] needs new recurring agent loops. If the project cannot be identified, ask for it before continuing. Review its goals, repeated failures, recurring chores, existing automation, and adopted loops. Read the current published Loop Library from https://signals.forwardfuture.ai/loop-library/api/loops. Find recurring outcomes that lack reliable ownership, a repeatable process, or proof of completion. For the strongest gap, prefer an exact published loop. If none fits, propose the smallest grounded adaptation. Design a new loop only when neither option works. Keep no more than three evidence-backed candidates and recommend at most one manual trial. For each candidate, define its trigger, inputs, authority, success check, budget, terminal states, trial, and retirement rule. Remove speculative, generic, duplicate, stale, or lower-value candidates. Do not install, schedule, or run anything without approval. Finish with the shortlist, evidence, rejected candidates, and trial recommendation, or explain why no hire is justified.
```

## 🏁 Implementation Steps
1. Review project goals, repeated failures, recurring chores, existing automation, adopted loops, and the live Loop Library.
2. Find important recurring outcomes that lack reliable ownership, a repeatable process, or proof of completion.
3. Prefer an exact published loop, then a small adaptation, and design a new loop only when neither fits.
4. Keep a short evidence-backed slate, define one manual trial and retirement rule, and stop before installation or scheduling.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every recommended loop fills a proven recurring gap and has a safe trial and retirement rule.
- *Detail*: The final slate contains at most three non-duplicate candidates, one recommended manual trial, evidence of recurrence, and explicit authority, success, budget, terminal, and retirement rules.

## 💡 Why it works
Teams can accumulate automation faster than they accumulate proof that it helps. This loop treats each proposed workflow like a role that must earn its place through recurrence, evidence, and a bounded trial.

## ⚠️ Implementation Note
* A recommendation is not permission to install, schedule, or run a loop. Remove candidates that are speculative, duplicate, stale, or weaker than existing manual ownership.

## 🏷️ Keywords
Loop Hiring Manager, agent workflow portfolio, automation selection, loop adoption, manual trial

## 💬 Reviews & Feedback
- *No reviews yet.*