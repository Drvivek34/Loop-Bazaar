# The Web Search Quota Budget Loop

**Loop ID**: #5122 | **Category**: Operations | **Author**: @loop_forge | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that monitors and enforces a per-provider web-search API budget (Tavily / Exa / Firecrawl / Brave), stopping when every wired provider is inside its free-tier quota.

## 🎯 Use Case (When to Use)
> Use whenever an agent makes recurring web searches on free tiers — keeps the monthly 1,000-credit Tavily or Firecrawl allowance from silently running dry.

## ⚡ System Prompt / Instructions
```
Check the quota state file for every configured web-search provider. For each provider above 80% of its monthly allowance, switch new queries to the next provider in the fallback chain. Cache identical queries by normalized URL so repeats never hit the API. Log every call with provider, mode, status, and remaining credits. Repeat until all providers are inside budget, then stop.
```

## 🏁 Implementation Steps
1. Read the quota state file and current usage per provider.
2. Flag any provider above 80% of its monthly free-tier allowance.
3. Re-route scheduled queries to fallback providers as needed.
4. Deduplicate queued queries by normalized URL before any API call.
5. Write updated state and stop when no provider exceeds budget.

## 🛑 Stopping Condition (Verification)
**Verification Check**: All providers inside free-tier budget.
- *Detail*: Verified: every tracked provider is at or below 80% of its verified 2026-08 free-tier allowance (Tavily 1,000/mo; Exa $10/mo; Firecrawl 1,000/mo; Brave $5/mo).

## 💡 Why it works
Works because it turns silent credit exhaustion into an explicit, checkable stopping condition before it breaks production search.

## ⚠️ Implementation Note
* Track only HTTP 200 responses against quota; log 429/5xx separately without incrementing counters.

## 🏷️ Keywords
tavily, exa, firecrawl, brave, quota, budget

## 💬 Reviews & Feedback
- **@quota_guardian** (★★★★★ 5/5): *The 200-call budget rule keeps our monthly Tavily credits alive for the full month.* (2026-08-24)
- **@fallback_first** (★★★★☆ 4/5): *Provider fallback order saved us during a Brave outage. Solid pattern.* (2026-08-24)