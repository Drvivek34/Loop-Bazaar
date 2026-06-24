# The next-action confidence check

**Loop ID**: #051 | **Category**: Evaluation | **Author**: Shinichi Nagata (@DecisionOS) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded AI-agent exit gate that verifies the current task, evaluates the next action, and returns control to the user before more work begins.

## 🎯 Use Case (When to Use)
> Use this after an agent finishes a task and another visible action could tempt it to continue beyond the user's original request.

## ⚡ System Prompt / Instructions
```
Run an exit check on the task most recently completed in this conversation or workspace. This check does not authorize additional work. If you cannot identify the task, its intended outcome, or its completion evidence, return BLOCK and list what is missing. Report what changed, what you verified, what you did not touch, and what remains uncertain. Classify the current task as PASS, DELAY, or BLOCK. Separately classify the next visible action as GO, HOLD, CAP, or BLOCK. Explain the decision briefly. If you choose CAP, define its exact scope and limit. Name exactly one allowed next action and anything that remains off limits. Do not begin the action, even if the result is GO. Stop and wait for the user. The check succeeds only when task completion and permission to continue are treated as separate decisions.
```

## 🏁 Implementation Steps
1. Identify the completed task, its intended outcome, and the evidence available for judging completion.
2. Report changed, verified, untouched, and uncertain areas, then classify the current task as PASS, DELAY, or BLOCK.
3. Evaluate the next visible action separately as GO, HOLD, CAP, or BLOCK and define any exact cap.
4. Name one allowed next action, state what remains off limits, and stop without beginning more work.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Completion and permission to continue are evaluated separately.
- *Detail*: The report gives one evidence-backed task status, one next-action gate, and one bounded next action without starting it.

## 💡 Why it works
Agents often treat finishing one task as permission to start the next visible idea. This gate makes completion and continued authority separate decisions, which keeps work bounded and restartable.

## ⚠️ Implementation Note
* GO identifies a sensible next action but still does not authorize the agent to begin it. If the completed task or its evidence cannot be identified, return BLOCK.

## 🏷️ Keywords
next action gate, AI agent stop condition, task completion check, scope control, human approval

## 💬 Reviews & Feedback
- *No reviews yet.*