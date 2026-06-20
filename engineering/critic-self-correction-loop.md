# The CRITIC tool-verified loop

**Loop ID**: #5055 | **Category**: Engineering | **Author**: Gou et al. (2024) | **Rating**: ⭐ 4.6/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
Self-correct by verifying outputs with external tools (search, code execution) and revising on the evidence.

## 🎯 Use Case (When to Use)
> When claims/code can be checked by tools before finalizing.

## ⚡ System Prompt / Instructions
```
Produce an answer, then verify it with appropriate tools. If verification fails, revise using the tool evidence and re-verify.
```

## 🏁 Implementation Steps
1. Generate a candidate answer
2. Verify with external tools
3. Collect concrete discrepancies
4. Revise and re-verify until clean

## 🛑 Stopping Condition (Verification)
**Verification Check**: Tool verification
- *Detail*: External tools confirm the output.

## 💡 Why it works
Tool-interactive critique grounds self-correction in reality instead of self-belief.

## ⚠️ Implementation Note
* Curated real-world loop with original source attribution.

## 🏷️ Keywords
critic, self-correction, tool verification

## 💬 Reviews & Feedback
- *No reviews yet.*