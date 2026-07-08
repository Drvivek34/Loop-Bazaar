# The persona coherence loop

**Loop ID**: #078 | **Category**: Content | **Author**: Tushar Kalan (@DilSalaKamina) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A UX research maintenance workflow that compares persona assumptions with recent research data, scores coherence, and rebuilds personas when contradictions accumulate.

## 🎯 Use Case (When to Use)
> Use this when personas may have drifted from current user research and product or design decisions depend on them.

## ⚡ System Prompt / Instructions
```
When new research arrives or personas may be stale, read each persona and extract its behavioral assumptions. Compare assumptions with recent research evidence, labeling each reinforced, contradicted, or unverified. Compute a coherence score from the evidence, and rebuild a persona only when the score falls below the agreed threshold and contradictions are material. Every defining trait in a rebuilt persona must cite enough current user evidence to support it. Update the persona timestamp and coherence log. Stop per persona when it is coherent, needs human review, lacks enough research, or hits the rebuild limit.
```

## 🏁 Implementation Steps
1. Extract behavioral assumptions from each persona before comparing them with new research.
2. Search recent research for reinforcing, contradicting, or missing evidence for each assumption.
3. Compute a coherence score and identify material contradictions.
4. Rebuild only personas that fall below the threshold and cite current evidence for every defining trait.
5. Update the persona record and log, then stop at coherence, insufficient data, rebuild limit, or human-review need.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every persona trait is supported by recent research or flagged for review.
- *Detail*: The output includes the persona assumptions, evidence labels, coherence score, contradiction count, rebuild count, cited supporting evidence, updated timestamp, and any human-review status.

## 💡 Why it works
Personas can remain persuasive long after their evidence goes stale; a coherence loop keeps them useful without rewriting them on every new quote.

## ⚠️ Implementation Note
* Do not invent user quotes or treat one anecdote as proof. Protect private research data and keep citations appropriate for the project.

## 🏷️ Keywords
persona coherence, UX research, user personas, research evidence, persona maintenance

## 💬 Reviews & Feedback
- *No reviews yet.*