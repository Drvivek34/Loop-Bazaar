# The devil's-advocate loop

**Loop ID**: #024 | **Category**: Evaluation | **Author**: Anonymous contributor | **Rating**: ⭐ 4.2/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A critic-and-builder workflow that attacks a design, tracks every objection, and requires evidence before an objection can be closed.

## 🎯 Use Case (When to Use)
> Use this before committing to an architecture, interface, rollout plan, or other consequential design that benefits from structured adversarial review.

## ⚡ System Prompt / Instructions
```
Before committing to an architecture, interface, or rollout plan, have a critic argue that it is wrong. Record each objection, impact, and status in a repository-local log at .agent-reviews/redteam.md. The builder must fix and verify each high-impact weakness or document why it is accepted; the critic may reopen unsupported answers. Stop when no high-impact objection remains or the same issues repeat for two rounds without new evidence. Finish with the decision, resolved and accepted objections, evidence, and any stalemate.
```

## 🏁 Implementation Steps
1. Write the design goals and acceptance criteria, then initialize .agent-reviews/redteam.md inside the repository and keep it out of commits.
2. Have the critic present the strongest evidence-backed case against the current design and rank each objection by impact.
3. Have the builder repair the weakness or document an explicit acceptance rationale, then verify the result against the stated criteria.
4. Let the critic reopen weak answers and repeat until the objections are closed with evidence or the loop reports a stalemate honestly.

## 🛑 Stopping Condition (Verification)
**Verification Check**: No high-impact objection remains open.
- *Detail*: Every logged objection is verified as resolved or explicitly accepted with evidence, or the final report truthfully records a two-round stalemate.

## 💡 Why it works
Separating critic and builder roles makes disagreement explicit. A persistent objection log prevents circular debate, while evidence-based closure stops the builder from declaring success by explanation alone.

## ⚠️ Implementation Note
* Keep the critic independent where possible. Do not change the acceptance criteria mid-run simply to close a difficult objection.

## 🏷️ Keywords
devil's advocate loop, adversarial design review, critic builder workflow, architecture objection log, red team design process

## 💬 Reviews & Feedback
- **@james_g** (★★★★☆ 4/5): *Highly recommended workflow, saves considerable manual sweep time.* (2026-06-19)