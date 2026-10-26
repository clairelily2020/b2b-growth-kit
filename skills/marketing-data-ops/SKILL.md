---
name: marketing-data-ops
description: Turn messy B2B marketing data (ad platforms, web and product analytics, CRM, partner channels) into one decision-ready working view - inventory sources and their reliability, unify definitions and source buckets across channel, product-event, CRM and decision layers, clean the working set first, audit tracking and identity stitching, and output keep/watch/cut and work-now/enrich/archive decisions. Use for CRM cleanup, attribution audits, tracking plans, channel keep-or-cut decisions, lead routing, or "the numbers don't match".
---

# Marketing data ops

The goal is not a pretty dashboard. It is a working view that answers: which channels to keep, which leads to work today, which fields can be trusted, and which cannot.

## When to use

- Several tools disagree and nobody can tell what a channel produced.
- The CRM is cluttered and the team does not know whom to follow up.
- Checking whether tracking is actually complete before trusting a funnel.
- Deciding budget or channel changes that need joined-up data.
- For a recurring report, use [marketing-reporting](../marketing-reporting/SKILL.md) once the definitions here are settled.

## Inputs

- Profile: `measurement` (tools, conversion events, timezone, currency), `icp`, `approvals.crm_write`.
- Live API access or exports from ad platforms, analytics, product events and the CRM; partner fees and reports.
- The decision someone needs to make.

## Process

1. **Turn the request into one business question.** "Which paid channels should we keep next month?" is workable; "look at the data" is not.
2. **Inventory sources** and label each: verified, partly usable, not trustworthy, missing. Evidence priority: live API or raw export, then current exports and CRM state, then dashboard screenshots, then old documents, then memory. When they conflict, the newer and rawer source wins and the old document gets updated.
3. **Keep four layers apart:** channel (where traffic came from), product events (what people did), CRM (who the record is, its status, lifecycle, owner), and decisions (budget, routing, reporting). Do not collapse them.
4. **Unify definitions before computing anything.** Source buckets, campaign buckets, landing page, signup, activation, paid intent, paid success, lifecycle stage, route. Write them down: [references/data-model.md](references/data-model.md).
5. **Audit tracking, not just presence of events.** An event existing does not mean tracking is complete: check identity stitching (anonymous to known), UTM persistence through signup, required properties on the signup event, and the CRM sync. If a funnel step shows zero, suspect tracking (cross-domain identity, event timing, lost UTMs, failed merges) before concluding nobody converts.
6. **Clean the working set first,** not the whole database: records that are active or valuable get lifecycle, source and next action filled; records with value but missing data go to enrich; invalid records (personal emails where the ICP is business, wrong companies, test data) go to archive.
7. **Decide.** Channels: keep, watch or cut, with the evidence. Records: work now, enrich before use, archive. Leads: raw, qualified sample, sales-ready. Actions: what I can do, what engineering must do, what the founder must decide.
8. **Leave a reusable asset:** a mapping table, view rules, a routing rule, an ownership table, a tracking fix list for engineering, or a month-end template.

## Output

```markdown
## Conclusion (one sentence: the business judgment now)
## State of the data (key counts, which sources are trustworthy, what is missing)
## Decisions (keep/watch/cut; work now/enrich/archive) with evidence
## Actions today (3-5, executable, with owner role)
## Reusable asset produced
```

## Gates

- Never present missing fields as a trend, event presence as complete tracking, or product events as CRM lifecycle ([evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md), [metrics-definitions](../b2b-growth-kit/policies/metrics-definitions.md)).
- Paid and partner channels are tests until they show clean UTMs, signups or activation, and records that reach the CRM working set. Impressions and clicks are not outcomes.
- CRM writes, merges, deletions and imports follow [approval-gates](../b2b-growth-kit/policies/approval-gates.md); start with the working set and a dry run.

## References

- [references/data-model.md](references/data-model.md)
