# The five-minute repository maintainer loop

**Loop ID**: #030 | **Category**: Engineering | **Author**: Peter Steinberger | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A five-minute Codex workflow that triages repositories, directs bounded maintenance to dedicated threads, and requires proof and permission before work lands.

## 🎯 Use Case (When to Use)
> Use this when Codex may coordinate maintenance across several active repositories and you want parallel work to stay steerable without duplicating or micromanaging threads.

## ⚡ System Prompt / Instructions
```
While repository maintenance is active, wake every five minutes. Triage [repositories] and read each repository thread's latest state. Reuse one thread per repository; assign its highest-value bounded task only within granted permissions, and do not interrupt coherent active work. Require tests, live proof, autoreview, and green CI before work can land. Escalate product, access, security, or irreversible decisions. Record meaningful changes and stop when every item is landed, decision-ready, blocked, or has no work.
```

## 🏁 Implementation Steps
1. Define the repository scope, exclusions, and separate permissions for triage, delegation, implementation, push, CI repair, merge, and release.
2. Every five minutes, refresh each repository queue and read the latest state of its existing thread before choosing the highest-value eligible item.
3. Reuse one thread per repository, assign one bounded task, and let coherent active work continue unless it is blocked, stalled, unsafe, or off course.
4. Require tests, live proof, autoreview, and green CI; record the evidence, then route the next item or present the owner with one exact decision.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every repository item reaches a proven handoff or terminal state.
- *Detail*: Authorized autonomous work lands with evidence; other items are decision-ready, blocked with one exact ask, or recorded as a clean no-op.

## 💡 Why it works
A five-minute heartbeat keeps the control plane current without turning polling into micromanagement. One thread per repository preserves context, while proof and authorization gates make autonomous landing auditable.

## ⚠️ Implementation Note
* The source pairs Maintainer Orchestrator with github-project-triage, autoreview, and computer use for live proof. A heartbeat automates observation, not authority: triage, delegation, implementation, push, merge, and release remain separate permissions. Read current thread state before steering, and never duplicate or interrupt active work.

## 🏷️ Keywords
Codex repository maintenance, multi-repository orchestration, five minute agent loop, GitHub project triage, thread delegation

## 💬 Reviews & Feedback
- **@agent0ai** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)