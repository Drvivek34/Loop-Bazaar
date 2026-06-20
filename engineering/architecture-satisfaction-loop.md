# The architecture satisfaction loop

**Loop ID**: #002 | **Category**: Engineering | **Author**: Peter Steinberger | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded refactoring workflow that live-tests the system, runs an independent review, commits checkpoints, and records progress.

## 🎯 Use Case (When to Use)
> Use this for a deliberate architectural refactor where the destination can be stated in concrete terms and the current system can be tested after each meaningful change.

## ⚡ System Prompt / Instructions
```
Refactor until you are happy with the architecture. After each significant step, live-test the system, run autoreview, and commit. Track progress in /tmp/refactor-{projectname}.md.
```

## 🏁 Implementation Steps
1. Write down the architectural target, constraints, and current risks before editing code.
2. Make one significant, reviewable change at a time.
3. Live-test the affected behavior and run an independent review after each significant step.
4. Commit each verified checkpoint and update the temporary progress file with decisions, blockers, and the next action.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The architecture is satisfactory and checks pass.
- *Detail*: Live-test, autoreview, and commit each significant step.

## 💡 Why it works
Small verified checkpoints reduce refactor risk and preserve rollback points. The progress file keeps the goal and decisions available across long sessions or handoffs.

## ⚠️ Implementation Note
* Define what satisfactory means before starting, such as module boundaries, dependency direction, passing tests, and acceptable performance. A subjective stop condition can otherwise run indefinitely.

## 🏷️ Keywords
AI coding agent, architecture refactor, autoreview, incremental refactoring, coding agent workflow

## 💬 Reviews & Feedback
- **@agent0ai** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)