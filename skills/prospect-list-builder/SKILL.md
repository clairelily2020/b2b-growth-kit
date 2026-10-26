---
name: prospect-list-builder
description: Build and qualify B2B account and contact lists from exhibitor and event lists, directories, search operators, CRM exports or sales databases - normalize, deduplicate, verify identity, score ICP fit and contactability separately, tier A/B/C/reject with evidence, and keep uncertain rows visible. Use for prospect lists, target account lists, ABM lists, exhibitor or attendee list qualification, LinkedIn search formulas, or cleaning a messy lead list.
---

# Prospect list builder

A short, verified list beats a long, padded one. This skill turns messy sources into accounts and contacts you can defend: who they are, why they fit, how sure you are, and what to do next.

## When to use

- Turning an event exhibitor list, directory or database export into a target list.
- Building an ABM account list or a contact list for outbound.
- Cleaning or re-qualifying an existing lead list.
- Research only: this skill does not send, upload to a CRM, buy data or enrich private data.

## Inputs

- Profile: `icp` (segments, roles, regions, triggers, exclusions), `positioning`, `outreach.suppression_source`.
- Sources: official exhibitor tables, directory exports, CRM or database exports, search results, floor plan or logo images (OCR), existing lists.
- Target size and what the list is for (outbound, ads audience, event meetings).

## Process

1. **Separate sources by confidence.** Official tables and first-party data are high; databases and directories medium; OCR, logo walls and scraped pages are candidates only. Keep the original row and its source on every record.
2. **Normalize and deduplicate.** Normalize domain and company name; match on domain first, then name. Review aliases, subsidiaries and shared domains before merging. A booth number is not a company identifier.
3. **Verify identity.** Each company needs at least one stable signal: official listing, working site, active company page, recent credible mention. A login wall, unavailable page or stale profile means **unverified**, not reject. Reject only with a specific, evidenced reason (does not exist, duplicate, clearly out of ICP).
4. **Score three things separately:** identity confidence, ICP fit (0-5 against the profile, with a one-line reason), and contactability. A strong fit with no contact path is still a strong fit; record the gap.
5. **Find people only when needed.** Roles from the profile; public professional sources only; search operators in [references/search-patterns.md](references/search-patterns.md). Never invent or guess email addresses; mark email status as unknown, found or verified.
6. **Tier:** A = verified, strong fit, clear research angle; B = plausible, one check missing; C = weak fit or poor contactability; Reject = evidenced reason. Uncertain rows stay in the list with their status.
7. **Add the research angle** per A and B account: the specific, checkable reason to reach out now (trigger, event, hiring, launch).
8. **Check suppression** before anything leaves research: customers in active deals, do-not-contact, competitors.

Column schema and summary format: [references/list-schema.md](references/list-schema.md).

## Output

A CSV with the schema columns, plus:

```markdown
Input rows / verified A / B / C / unverified / rejected
Top rejection reasons (with counts)
Shortfall vs target, and which sources would close it
Recommended next step
```

## Gates

- No padding to hit a number; report the shortfall. OCR- or logo-only matches never reach tier A without a second source.
- Unknown and unverified stay labelled as such ([evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md)). A company exhibiting does not prove a given person attends.
- Lawful basis, public data only and suppression follow [outreach-compliance](../b2b-growth-kit/policies/outreach-compliance.md). CRM uploads and paid enrichment need approval ([approval-gates](../b2b-growth-kit/policies/approval-gates.md)).

## References

- [references/list-schema.md](references/list-schema.md) · [references/search-patterns.md](references/search-patterns.md)
- Next: [cold-email](../cold-email/SKILL.md), [linkedin-outbound](../linkedin-outbound/SKILL.md), [linkedin-ads](../linkedin-ads/SKILL.md)
