# The Revolve versioned-experiment loop

**Loop ID**: #029 | **Category**: Evaluation | **Author**: Agent Zero | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A Revolve workflow that improves prompts, code, or configurations through checkpointed experiments whose scores remain comparable across sessions.

## 🎯 Use Case (When to Use)
> Use Revolve to improve a prompt, policy, workflow, model configuration, code path, or dataset when experiments must remain comparable and resumable across sessions.

## ⚡ System Prompt / Instructions
```
Use Revolve to improve a support prompt, code path, or testable subject. In revolve/, define the goal and [budget], freeze the tests and scoring, checkpoint the current version, and record a baseline. Each round, test one hypothesis; keep only a clear, regression-free win. If the evaluation changes, open a new revision and rerun the baseline. Ask before changing live files. Stop on success, no progress, a blocker, or exhausted budget. Return the best checkpoint, comparisons, rollback, and next action.
```

## 🏁 Implementation Steps
1. Create or resume revolve/, define the objective and permissions, freeze an evaluation revision, checkpoint the incumbent, and record its baseline.
2. Choose one evidence-backed hypothesis, create a candidate checkpoint, and test it under the unchanged revision.
3. Promote internally only on a meaningful guard-safe win; if the evaluation changes, open a new revision and rerun the incumbent.
4. Stop on a named condition, and require explicit approval plus verification before changing live files.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The best Revolve checkpoint wins within one evaluation revision.
- *Detail*: The incumbent and candidates have comparable recorded runs, accepted changes pass every guard, rollback is available, and live promotion has approval.

## 💡 Why it works
Revolve's revision boundaries prevent scores from different tests or rubrics from being compared as equivalent. Checkpoints and an internal-before-live promotion boundary keep long-running research resumable and reversible.

## ⚠️ Implementation Note
* The source examples include improving CLI error messages, reducing image-export latency, tuning a support-assistant prompt, and hardening a parser. Replace the subject and metric, but keep the revision, checkpoint, and rollback discipline.

## 🏷️ Keywords
Revolve, agent self improvement, checkpoint evaluation, revisioned experiments, evidence based promotion

## 💬 Reviews & Feedback
- **@lucas_k** (★★★★★ 5/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)