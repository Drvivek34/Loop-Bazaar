# The restartable handoff loop

**Loop ID**: #066 | **Category**: Operations | **Author**: Shinichi Nagata (@DecisionOS) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded AI-agent handoff workflow that records current state, evidence, risks, untouched scope, and exactly one safe next action before the session ends.

## 🎯 Use Case (When to Use)
> Use this when a session is ending, context is becoming unwieldy, or another human or agent may need to continue the work later.

## ⚡ System Prompt / Instructions
```
Before ending [session or work period], create a restartable handoff. Record the current goal, changes, verification evidence, untouched scope, uncertainties, open risks, off-limits areas, and last decision or gate. Check that a new human or agent could continue without guessing, then name exactly one safe next action and what they must not assume. Stop after the handoff; do not begin that action.
```

## 🏁 Implementation Steps
1. State the current goal, the work completed, and the evidence that was actually verified.
2. Record untouched and off-limits scope, uncertainty, open risks, and the last decision or gate.
3. Test whether a new actor could restart from the handoff without relying on hidden context or assumptions.
4. Name exactly one safe next action, state what must not be assumed, and stop without starting it.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The next person or agent can resume without guessing.
- *Detail*: The handoff accounts for current state, evidence, untouched and off-limits scope, uncertainty, risks, the last decision, one safe next action, and assumptions the next actor must not make.

## 💡 Why it works
A compact end-of-session artifact prevents context loss from turning into duplicated work, unsafe assumptions, or accidental scope expansion. The mandatory stop keeps a handoff from silently becoming authorization for more work.

## ⚠️ Implementation Note
* Describe only verified state. Do not turn guesses into completed work, omit blockers, or use the handoff itself as permission to begin the next action.

## 🏷️ Keywords
AI agent handoff, session continuity, context transfer, restartable work, operational handoff

## 💬 Reviews & Feedback
- *No reviews yet.*