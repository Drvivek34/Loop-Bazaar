# The paid-API preflight loop

**Loop ID**: #074 | **Category**: Operations | **Author**: AKT (@akt199009) | **Rating**: ⭐ 5.0/5.0

[← Back to Category Index](README.md) | [← Back to Root Index](../README.md)

---

## 📝 Description
A spend-control workflow where an agent verifies fresh signed uptime, latency, and price attestations before using a paid API or x402 service.

## 🎯 Use Case (When to Use)
> Use this when an agent may spend money on paid APIs and should not trust listings or burn budget re-probing services before every call.

## ⚡ System Prompt / Instructions
```
Before paying for any pay-per-call or x402 service, fetch the latest reliability attestation from an index that continuously probes matching services. Verify the attestation signature against the index public key, check freshness, then compare measured uptime, latency, and price against the task budget and deadline. Proceed only with a service whose verified numbers fit. Record the attestation that justified each spend. Treat unverifiable, stale, or missing attestations as missing data. Stop when no listed service fits, budget approval is needed, or the task can be completed without paid calls.
```

## 🏁 Implementation Steps
1. Find candidate services for the needed capability in a reliability index or approved source.
2. Fetch the latest attestation for each candidate and verify its signature against the index public key.
3. Reject stale, unverifiable, or missing attestations as missing data rather than service failures.
4. Choose only a service whose measured uptime, latency, and price fit the task budget and deadline.
5. Record the attestation behind each spend and stop when no verified option fits or approval is required.

## 🛑 Stopping Condition (Verification)
**Verification Check**: Every paid API decision cites a fresh signature-verified attestation.
- *Detail*: The run record names the service, attestation timestamp, measured uptime, latency, price, signature verification result, budget fit, and reason for use or rejection.

## 💡 Why it works
Paid API listings can show that a service exists without proving it is currently reliable, and repeated self-probing wastes money; signed attestations make verified probes reusable.

## ⚠️ Implementation Note
* An attestation is a spend gate, not a guarantee of task quality. Any actual purchase, budget increase, credential use, or external account change still needs the authority normally required for that environment.

## 🏷️ Keywords
paid API verification, x402 preflight, signed attestation, agent spend control, API reliability

## 💬 Reviews & Feedback
- *No reviews yet.*