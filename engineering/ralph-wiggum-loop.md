# The Ralph (Wiggum) loop

**Loop ID**: #5051 | **Category**: Engineering | **Author**: Geoffrey Huntley (@geoffreyhuntley) | **Rating**: ⭐ 4.9/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A brute-force `while true` bash loop that repeatedly feeds an agent the same prompt file with a fresh context each iteration until the task is complete.

## 🎯 Use Case (When to Use)
> When you want an agent to grind autonomously on a well-specified task overnight.

## ⚡ System Prompt / Instructions
```
Run this prompt file every iteration on a fresh context; read the spec, make the smallest correct change toward completion, verify, and stop only when every item is done.
```

## 🏁 Implementation Steps
1. Put the task/spec in a single prompt file
2. Run the agent in a while-true loop with a fresh context each pass
3. Let it read errors/output and self-correct
4. Add a guard to stop on completion or max iterations

## 🛑 Stopping Condition (Verification)
**Verification Check**: Completion check
- *Detail*: All spec items satisfied and the build/tests pass.

## 💡 Why it works
Fresh context every iteration avoids the quality drop LLMs suffer past ~100k–150k tokens.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
ralph, autonomous, bash loop, fresh context

## 💬 Reviews & Feedback
- *No reviews yet.*