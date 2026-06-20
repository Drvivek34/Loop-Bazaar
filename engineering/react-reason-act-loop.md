# The ReAct (reason + act) loop

**Loop ID**: #5052 | **Category**: Engineering | **Author**: Yao et al. (Princeton/Google) | **Rating**: ⭐ 4.8/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Interleave reasoning traces and tool actions: think, act, observe, repeat — terminating on a final answer.

## 🎯 Use Case (When to Use)
> When a task needs tool use interleaved with reasoning (search, code, lookups).

## ⚡ System Prompt / Instructions
```
Think step by step. Emit a Thought, then an Action (a tool call), read the Observation, and repeat until you can give a Final Answer.
```

## 🏁 Implementation Steps
1. Produce a Thought about the next step
2. Choose and call a tool (Action)
3. Read the tool Observation
4. Repeat until a Final Answer is reached

## 🛑 Stopping Condition (Verification)
**Verification Check**: Termination
- *Detail*: Model emits a Final Answer grounded in observations.

## 💡 Why it works
Grounding reasoning in real tool observations reduces hallucination and enables recovery.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
react, reasoning, tool use, agents

## 💬 Reviews & Feedback
- *No reviews yet.*