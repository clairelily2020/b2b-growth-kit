# Data model

A minimal shared model for small B2B teams. Rename values to match your tools, but keep the separations.

## Source buckets (channel layer)

```text
paid_search, paid_social_linkedin, paid_social_reddit, paid_social_meta,
partner_or_affiliate, owned_web (organic search, direct to content),
email_outbound, social_organic, community, event, referral, direct_or_unknown
```

Rules: every record gets exactly one first-touch bucket. `direct_or_unknown` is honest; do not guess a bucket to make it smaller. Keep raw source values alongside the bucket so mapping mistakes can be fixed.

## Product events (product layer)

| Event | Means | Common trap |
|---|---|---|
| `signup` | Account created | Fires before identity is stitched, losing the source |
| `activation` | First core action that delivers value | Defined vaguely; write the exact action |
| `paid_intent` | Visited pricing, started checkout, asked for a quote | A "demo clicked" button event is a UI check, not a booked demo |
| `paid_success` | Payment or signed order | Refunds and failed payments not subtracted |

Every event needs: the identity it is attached to, the timestamp, the source properties (UTMs persisted from the first visit), and a stable name. When an event was renamed, record both names and the switch date.

## CRM layers (keep three separate fields)

| Field | Answers | Example values |
|---|---|---|
| Record origin | How did this record enter the CRM? | product_signup, form_lead, event_import, outbound_list, manual |
| Record status | Can we use it? | working_now, enrich_before_use, archive_or_ignore |
| Lifecycle stage | Where is it in the buying journey? | subscriber, lead, MQL, SQL, opportunity, customer |

Rules:
- A product signup is not automatically a sales lead; check fit and activation first.
- An imported event or exhibitor list is a research pool, not leads.
- Lifecycle moves only with evidence (see the metrics policy).
- One owner per record in active outreach.

## Working views

Teams work from a few saved views, not the whole database:
- Records to work today (status working_now, has owner and next action).
- Records to review (new signups or replies awaiting qualification).
- Records needing enrichment.

## Tracking completeness checklist

- [ ] Identity stitching from anonymous visit to known user works across the marketing site and the app.
- [ ] UTMs saved on first visit and still present at signup.
- [ ] Signup event carries the required properties.
- [ ] CRM receives signups with source and owner fields.
- [ ] Ad platforms receive the conversion they optimize for, once per conversion.
- [ ] Renamed or duplicate events documented.

## Partner and affiliate channels

Track more than clicks: source bucket, landing page, signups, CRM records created, and records that reached the working set. Fixed fees count as spend for the period they cover.
