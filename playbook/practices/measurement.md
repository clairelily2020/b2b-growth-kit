# Measurement: know what happened before deciding who caused it

Keep business facts, platform records and marketing attribution apart. The payment system proves a payment; an ad platform proves it recorded a conversion by its own rules. Neither stands in for the other.

## Minimum event contract

| Event | Counts when | Deduplicate on | Not the same as |
|---|---|---|---|
| Signup | Account created successfully | Registration or user ID | Clicking the signup button |
| Booking | The booking system confirms | Booking ID | Opening the booking page |
| Meeting held | The meeting actually happened | Meeting ID and completed status | A confirmed booking |
| Value action | The defined task is completed | Task ID | Logging in or viewing pages |
| Payment | Payment succeeded | Order ID | Checkout page, created subscription or quote |
| Refund | Refund issued | Refund ID linked to the order | A complaint |

Signups and bookings overlap; when counting acquired people, deduplicate on a reliable identity. If identity cannot be linked, keep it unknown rather than guess. Companies, people and orders are never added together.

The same definitions as a CSV: [measurement-plan.csv](../templates/measurement-plan.csv).

## Storing the source

Record the raw source, medium, campaign and content values; the first entry page; the latest identifiable entry; and the self-reported source. Keep raw values and use a mapping table to unify names for the same partnership in reports. Do not let internal tags or empty sources stand in for organic traffic.

A customer might read a newsletter, later search the brand, then sign up. Reports can show several attribution views; never add revenue across views. Short-link clicks, platform clicks and site visitors are defined differently and do not map one to one.

## Weekly reconciliation

Pick real business records you can check and trace them through source, identity, business success, CRM and the platform's receipt. Use the same window, timezone and deduplication rule; exclude internal and test traffic. When systems cannot be aligned, label the numbers as trend-only.

In Google Ads, whether a primary conversion action is used for bidding also depends on the goals the campaign actually uses, and custom goals are an exception where secondary actions can bid too. Verify configuration, deployment, receipt and attribution separately; a switch in the interface proves nothing on its own. See Google's [conversion goals documentation](https://support.google.com/google-ads/answer/11461796?hl=en).

## Reading experiments

Each round answers only the question written down beforehand. Keep audience tests, copy tests and whole-path tests apart. Count cost, qualified accounts, opportunities and payments on the same definitions, and keep cohorts whose sales cycle has not finished.

Zero deals does not make CAC zero; no detected payment event does not confirm there was no offline deal. Success stories without a denominator cannot produce a conversion rate.

Brand and education content get longer observation windows plus supporting evidence. Measuring incrementality needs a comparable group or a time-based design; with only last-click reports, say so.

Templates: [measurement plan](../templates/measurement-plan.csv), [experiment card](../templates/experiment.md), [experiment log](../templates/experiments.csv). Shared definitions for agents: [metrics-definitions](../../skills/b2b-growth-kit/policies/metrics-definitions.md).
