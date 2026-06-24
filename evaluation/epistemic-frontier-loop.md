# The epistemic frontier loop

**Loop ID**: #063 | **Category**: Evaluation | **Author**: Indrajeet Yadav (@indrajeet877) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded reasoning loop that separates facts from assumptions, tests falsifiable hypotheses, updates confidence, and selects the next highest-information experiment.

## 🎯 Use Case (When to Use)
> Use this for a hard question, strategy, system, or unresolved decision where several explanations remain plausible and another evidence-gathering step could materially improve the conclusion.

## ⚡ System Prompt / Instructions
```
Investigate [question, decision, or unresolved problem] using [available evidence]. Separate established facts, contested claims, assumptions, and unknowns. Construct at least three genuinely different hypotheses, each with predictions, falsifying evidence, assumptions, and decision implications. Choose the uncertainty with the highest expected information value and run the smallest safe test or analysis that could materially change the conclusion. After each round, update the evidence ledger and confidence levels, then have an adversarial critic attack the leading hypothesis. Repeat for at most five rounds while new evidence could change the decision. Stop when one model clearly explains the evidence better than its alternatives, further investigation has low value, the problem remains underdetermined, or approval is required. Never fabricate evidence or hide uncertainty. Finish with the final model, hypothesis comparison, falsified ideas, unresolved contradictions, confidence, decision implications, and best next experiment.
```

## 🏁 Implementation Steps
1. Separate known facts, contested claims, assumptions, and unknowns.
2. Construct at least three hypotheses with predictions and falsifiers.
3. Select and run the smallest safe high-information test.
4. Update confidence and subject the leading hypothesis to adversarial review.
5. Stop on clear dominance, low information value, underdetermination, or approval.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The conclusion survives comparison with falsifiable alternatives.
- *Detail*: The evidence ledger shows how each hypothesis gained or lost support, what was falsified, why the leading model is preferred, and which uncertainty remains most decision-relevant.

## 💡 Why it works
Competing falsifiable models make uncertainty visible and direct limited research effort toward evidence that can actually change a decision.

## ⚠️ Implementation Note
* Define what meaningful evidence and model dominance mean for the specific question before interpreting confidence changes as a breakthrough.

## 🏷️ Keywords
hypothesis testing, information value, evidence ledger, decision uncertainty, adversarial reasoning

## 💬 Reviews & Feedback
- *No reviews yet.*