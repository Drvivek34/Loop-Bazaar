# The world-state accountability loop

**Loop ID**: #084 | **Category**: Evaluation | **Author**: Nishant Dodiya (@NishantDodiya4) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A general agent-control workflow that turns each meaningful action into a bounded prediction, verification, and continue-or-stop decision.

## 🎯 Use Case (When to Use)
> Use this when an agent is about to change code, files, tools, APIs, research, product decisions, infrastructure, or any system state where assumptions could cause drift.

## ⚡ System Prompt / Instructions
```
Before a meaningful action, build a compact current-state model: known facts, uncertainties, missing evidence, relevant systems, constraints, user goals, and granted authority. Identify the risky assumption the agent is tempted to make, then propose the smallest useful next action. Before acting, predict what should change, what should remain unchanged, what evidence will confirm success, and what would count as surprise or failure. Act only if the action is in scope and verifiable. Afterward, compare predicted and actual state, record the trace, and continue only if the model still holds, risk has not increased, and another bounded pass is justified. Stop at target state, material prediction failure, blocker, approval boundary, or no justified next action.
```

## 🏁 Implementation Steps
1. Build a compact model of current facts, uncertainties, constraints, authority, and relevant systems.
2. Name the risky missing state or assumption before choosing an action.
3. Predict the intended state change, unchanged boundaries, success evidence, and failure signals.
4. Take only one bounded in-scope action with a clear verification method.
5. Compare predicted and actual state, record surprises, and stop or continue based on evidence.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every action has a before-state model, prediction, after-state evidence, and continue-or-stop decision.
- *Detail*: The accountability trace includes current state, uncertainty, proposed action, predicted result, action taken, evidence checked, predicted-versus-actual comparison, surprises, risk changes, and the final decision.

## 💡 Why it works
Agents often continue from stale assumptions; requiring a prediction before action makes drift and unintended consequences visible.

## ⚠️ Implementation Note
* Any production, money, security, privacy, external communication, irreversible state, or public-claim boundary still requires normal human approval.

## 🏷️ Keywords
world state, agent accountability, prediction check, state model, bounded action

## 💬 Reviews & Feedback
- *No reviews yet.*