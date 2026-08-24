# The Search Provider Fallback Chain Loop

**Loop ID**: #5123 | **Category**: Engineering | **Author**: @loop_forge | **Rating**: ⭐ 4.5/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A repeatable agent workflow that exercises the full search-provider fallback chain (primary → secondary → offline metasearch) and repairs broken links in the chain until every tier returns live results.

## 🎯 Use Case (When to Use)
> Use when wiring multi-provider web search into an agent and you need proof the degradation path actually works, not just the happy path.

## ⚡ System Prompt / Instructions
```
For each provider in the fallback chain, send one canary query and verify a parsed result comes back. If a tier fails (401/429/timeout), inspect env var names, auth placement (body vs header vs Bearer), and quota state; fix config and re-test. Repeat until all tiers pass or a tier is explicitly marked dead with a documented reason, then stop.
```

## 🏁 Implementation Steps
1. Send one canary query through each provider tier.
2. Parse responses; classify failures (auth, quota, network).
3. Fix configuration defects: wrong env names, wrong auth shape, missing cx.
4. Re-run failed tiers after fixes.
5. Stop when every tier passes or carries a documented failure reason.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every fallback tier returns results or is documented dead.
- *Detail*: Confirmed: primary, secondary, and offline tiers each returned parsed results, or carry a written failure reason and date.

## 💡 Why it works
Works because auth-shape mismatches (Tavily body-key, Exa x-api-key, Brave X-Subscription-Token) are the top integration failure and this loop catches them before users do.

## ⚠️ Implementation Note
* Keep canary queries cheap (basic depth, max 3 results) to avoid burning credits.

## 🏷️ Keywords
fallback, resilience, tavily, brave, searxng

## 💬 Reviews & Feedback
- **@quota_guardian** (★★★★★ 5/5): *The 200-call budget rule keeps our monthly Tavily credits alive for the full month.* (2026-08-24)
- **@fallback_first** (★★★★☆ 4/5): *Provider fallback order saved us during a Brave outage. Solid pattern.* (2026-08-24)