# The research-to-artifact loop

**Loop ID**: #052 | **Category**: Content | **Author**: Hiten Shah (@hnshah) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A bounded research workflow that follows the most important evidence gaps until a memo, brief, specification, recommendation, or page is ready to use.

## 🎯 Use Case (When to Use)
> Use this when research should end in a specific decision, brief, recommendation, specification, page, or other artifact rather than a pile of notes.

## ⚡ System Prompt / Instructions
```
Research [question or topic] and produce a decision-ready [memo, brief, specification, recommendation, page, or other artifact] for [audience or decision]. If the question, audience, or intended artifact is missing, ask one focused question before starting. State the decision the artifact should support, its acceptance criteria, the allowed source scope, and the research budget. If no budget is supplied, use no more than ten strong sources or ninety minutes. Prefer current primary sources where available. After each research pass, update the artifact and identify the largest remaining evidence gap, contradiction, or uncertainty. Continue only if resolving it could materially change the decision and the budget allows another pass. Never invent evidence or hide uncertainty. Stop when the artifact meets its acceptance criteria, important claims trace to sources, and remaining uncertainty is explicit. Otherwise stop as blocked or exhausted. Finish with the completed artifact, sources, findings, tensions, confidence level, open questions, and recommended next step.
```

## 🏁 Implementation Steps
1. Define the decision, audience, artifact format, acceptance criteria, source scope, and research budget.
2. Gather the strongest relevant evidence and separate findings, tensions, implications, and open questions.
3. Update the artifact, identify the largest remaining evidence gap, and research again only when it could change the decision.
4. Stop with a sourced decision-ready artifact or an honest blocked or exhausted result.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The artifact is ready to support its stated decision.
- *Detail*: The deliverable meets its acceptance criteria, traces important claims to sources, and states material uncertainty instead of hiding it.

## 💡 Why it works
Research can expand indefinitely when the output and decision are vague. Tying each research pass to a concrete artifact keeps effort proportional to what the decision actually needs.

## ⚠️ Implementation Note
* This loop creates an artifact from research. Use the artifact-to-skill loop later if the proven method behind that artifact should become reusable.

## 🏷️ Keywords
research synthesis, decision ready artifact, evidence based memo, research workflow, source grounded writing

## 💬 Reviews & Feedback
- *No reviews yet.*