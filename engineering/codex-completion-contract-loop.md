# The Codex completion-contract loop

**Loop ID**: #028 | **Category**: Engineering | **Author**: 3goblack (@Dis_Trackted) | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A goal-planner-codex workflow that defines completion up front, tracks proof for every requirement, and prevents partial Codex work from being reported as done.

## 🎯 Use Case (When to Use)
> Use this for long-running Codex work, pull requests, runtime checks, or user-visible artifacts where a plausible partial result could be mistaken for completion.

## ⚡ System Prompt / Instructions
```
Run $goal-planner-codex [task] for long-running Codex work where partial work could be mistaken for done. Landing a PR and verifying production is one example. Before acting, define every required outcome and its evidence. After each bounded action, mark requirements proved, weak, missing, or contradicted. Complete the Goal only when all are proved; otherwise stop as blocked, stalled, or exhausted. Ask before creating Goal state. Finish with the requirement-to-evidence table, status, owner, and next action.
```

## 🏁 Implementation Steps
1. Recover a measurable definition of done for every ambiguous requirement.
2. Record the requirements, scope, non-goals, evidence plan, and current status without expanding the requested work.
3. Execute one bounded action at a time and attach current evidence to each affected requirement.
4. Audit every requirement before closure and preserve honest blocked, exhausted, stalled, or contradicted states.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every Codex Goal requirement has current, adequate proof.
- *Detail*: The final audit contains no weak, missing, or contradicted required item; otherwise the work remains open, blocked, or exhausted.

## 💡 Why it works
A durable completion contract keeps the definition of done visible across long sessions. Mapping every requirement to evidence makes false completion easy to detect.

## ⚠️ Implementation Note
* Use $goal-planner-codex only when the user explicitly asks for a Codex Goal or completion audit. Create native Goal state only with approval; ordinary task planning does not need it, and budget exhaustion never counts as success.

## 🏷️ Keywords
Codex Goal, completion contract, evidence audit, definition of done, false completion prevention

## 💬 Reviews & Feedback
- **@ada_lovelace** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)