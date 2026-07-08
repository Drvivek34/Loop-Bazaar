# The viral product margin audit loop

**Loop ID**: #083 | **Category**: Operations | **Author**: Subramanyam Badhika | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A commerce research workflow that finds fresh product demand, verifies supplier costs, calculates margin, filters IP and MOQ risks, and stops with a validated candidate or no-go.

## 🎯 Use Case (When to Use)
> Use this when evaluating commerce product ideas and the decision depends on current demand, supplier economics, and risk filtering rather than intuition.

## ⚡ System Prompt / Instructions
```
Identify high-margin product opportunities within the specified niche or market. If the niche is missing, ask and stop. Use only fresh demand signals from approved feeds, ad libraries, or social sources, then shortlist products with clear velocity. For each candidate, record the value proposition, retail price, supplier URLs, unit cost, minimum order quantity, shipping estimate, and IP or trademark risk. Calculate gross margin using the agreed acquisition buffer and reject candidates below the margin floor, above the investment cap, with unverifiable costs, or with immediate legal risk. Repeat up to the research-round cap and stop with a validated candidate, no-go result, blocked access, or approval need.
```

## 🏁 Implementation Steps
1. Ask for the target niche or market if it is not already specified.
2. Find fresh demand signals from approved discovery sources and shortlist distinct candidate products.
3. Verify supplier costs, shipping, minimum order quantity, retail price, and IP or trademark risk from primary sources.
4. Calculate margins with the agreed buffer and reject candidates that fail margin, investment, evidence, or legal gates.
5. Stop with a validated candidate, no-go result, blocked access, approval need, or exhausted research cap.

## 🛑 Stopping Condition (Verification)
**Verification Check**: The winning product has fresh demand evidence, supplier proof, margin math, and risk gates.
- *Detail*: The final payload includes demand sources, supplier URLs, unit economics, margin calculation, rejected candidates with reasons, IP or trademark notes, validation plan, and the stopping reason.

## 💡 Why it works
Trending-product research is easy to fake with stale social proof or guessed supplier numbers; this loop forces fresh demand, primary cost evidence, and explicit risk gates.

## ⚠️ Implementation Note
* Do not place orders, scrape against terms, contact suppliers, launch ads, use trademarks, or make financial commitments without explicit approval.

## 🏷️ Keywords
product validation, margin audit, supplier research, social demand, commerce research

## 💬 Reviews & Feedback
- *No reviews yet.*