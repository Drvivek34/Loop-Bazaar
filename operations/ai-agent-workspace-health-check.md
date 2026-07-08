# The AI-agent workspace health check

**Loop ID**: #081 | **Category**: Operations | **Author**: Shinichi Nagata (@DecisionOS) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A read-only restartability audit that inspects source of truth, accepted state, handoff freshness, instruction health, stale artifacts, and the next safe action.

## 🎯 Use Case (When to Use)
> Use this before continuing a long-running AI-agent workspace when state, handoff, source of truth, or next safe action may be unclear.

## ⚡ System Prompt / Instructions
```
Read the repo, workspace, or supplied AI-agent session trace as a restartability audit. Do not edit files. Check the living source of truth, accepted state or SHA, branch safety, handoff freshness, stale artifacts, preview versus public versus test mismatch, always-loaded agent instructions, unresolved items, and the next safe action. Classify the workspace green, yellow, or red with evidence only from the repo, workspace, or trace. If green, say whether it is disciplined or merely low-complexity. Stop after the read-only audit and return the verdict, evidence, unclear state, stale items, instruction risks, and one safe next action.
```

## 🏁 Implementation Steps
1. Read current workspace, repo, or trace evidence without editing files.
2. Identify the living source of truth, accepted state, handoff freshness, branch safety, stale artifacts, and instruction risks.
3. Classify unresolved or unclosed items that make continuation unsafe.
4. Assign a green, yellow, or red verdict backed only by found evidence.
5. Return one safe next action and stop without making changes.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The workspace health verdict is backed by concrete restartability evidence.
- *Detail*: The output includes a green/yellow/red signal, source of truth, accepted state, handoff freshness, instruction health findings, unresolved items, stale artifacts, evidence citations, and one safe next action.

## 💡 Why it works
Long AI-agent work can look busy while becoming unrestartable; a read-only health check reveals whether another agent can safely continue.

## ⚠️ Implementation Note
* This is not a safety badge and does not authorize cleanup, deployment, deletion, or continuation. It only reports current restartability.

## 🏷️ Keywords
AI workspace health, restartability, handoff freshness, agent instructions, source of truth

## 💬 Reviews & Feedback
- *No reviews yet.*