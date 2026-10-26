# Metrics definitions

Shared definitions so that reports, ads analysis and planning use the same numbers. A skill that reports a metric uses the definition here or states its own explicitly.

## Every reported number carries

- period (start and end date), timezone and currency from the profile
- source system and the time the data was pulled
- whether the period is complete

Comparisons (week over week, month over month) need matching window lengths and the same definitions on both sides. Mark any instrumentation change that happened inside the window.

## Funnel stages stay distinct

`impression → click → visit → lead → signup/trial → qualified (MQL/SQL) → opportunity → customer → retained`

Never merge two stages because the data is easier to get. A signup is not a qualified lead; a booked meeting is not an opportunity.

## Definitions

| Metric | Formula | Notes |
|---|---|---|
| CTR | clicks / impressions | Null if impressions = 0 |
| CPC | spend / clicks | Null if clicks = 0 |
| Conversion rate | conversions / clicks (state which conversion) | Name the conversion action |
| Cost per conversion | spend / conversions | Null if conversions = 0, never "infinite" |
| Paid-media CAC | paid spend / new customers attributed to that paid channel | Requires verified attribution (below) |
| Blended CAC | total sales and marketing cost / all new customers | Different metric; do not mix with paid-media CAC |
| ROAS | attributed revenue / ad spend | Revenue, not profit. Requires verified attribution |
| Payback (months) | CAC / monthly gross margin per customer | State the margin assumption |
| GRR | (starting MRR - churn - contraction) / starting MRR | Excludes expansion |
| NRR | (starting MRR - churn - contraction + expansion) / starting MRR | |

## Attribution gate

Paid-media CAC and ROAS are calculated **only** when:

1. The ad platform's clicks and the CRM's customers are joined on a verified identity (click ID, email or account), recorded as reviewed evidence with `claim_key = attribution.identity_join`.
2. Both sides cover the same cohort and the same window.
3. No conflicting evidence exists for that join.

Otherwise report CAC and ROAS as `unknown (attribution not verified)` and say what would verify it. Do not compute them from two disconnected tables. The harness enforces this in its `ads` workflow.

## Platform-specific terms

- **Quality Score (Google Ads)**: a 1-10 diagnostic per keyword built from expected CTR, ad relevance and landing page experience. A dash means not enough data, not a low score.
- **Conversion action status**: "No recent conversions" means the tag fired before but not recently. "Inactive" or "Misconfigured" means nothing is being counted. Check this before judging any campaign.
- **Learning phase**: automated bidding needs time and conversion volume after a change. Do not judge or re-edit a campaign inside it unless spend is clearly wasted.
