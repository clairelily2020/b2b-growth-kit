# Account audit

## Principles

- Real campaign, keyword and search term data comes before recommendations.
- Low-risk cleanup comes before budget, bidding or expansion.
- Search terms beat keyword-tool guesses.
- The optimization score measures how many Google suggestions you accepted, not performance.
- Dirty terms that converted are isolated for observation, not deleted.
- Test terms with no signal do not stay live "in case".

## Order of work

1. Pull 30 days of campaign, keyword and search term data.
2. Classify keep, watch, pause.
3. Pause high-spend zero-conversion keywords.
4. Pause enabled keywords with zero impressions, clicks and conversions in 30 days (structural noise).
5. Add exact negatives for clear wrong-intent traffic.
6. Move dirty-but-possibly-valuable intent into an observation ad group or campaign.
7. Remove empty ad groups, conflicting negatives and redundant keywords.
8. Only then discuss budgets, bids, landing pages and scaling.

## Keep, watch, pause

**Keep**
- Keywords or search terms with real conversions (on a healthy conversion action).
- Terms that match the current offer and show clear demand.
- Time-bound terms for the current priority period (for example, upcoming events you target).

**Watch**
- Clicks or a few conversions, but mixed intent.
- Might produce leads, not ready to scale.
- Kept in a separate observation group so they do not distort the main intent's numbers.

**Pause**
- High spend, zero conversions, no strong reason to keep.
- Enabled with zero impressions, clicks and conversions in 30 days.
- Long-tail terms for periods or segments that are not a current priority.
- Redundant terms with the same intent in the same ad group.

"High spend" is relative: a common rule of thumb is spend above one to two times your target cost per conversion with zero conversions. State the threshold you used.

## Common negative patterns in B2B

- Jobs and careers (job, career, hiring, salary, internship).
- Free and DIY (free template, free download, how to build) when the offer is paid.
- Navigation to other software (competitor login, competitor support).
- Adjacent but wrong jobs (tracking or analytics tooling, ticketing, venue or floor plan, agenda) unless relevant.
- The wrong side of a marketplace (for example buyer-side terms when the offer is seller-side).

## Recommendation triage

Usually fine:
- Empty ad group cleanup, conflicting negatives, redundant keywords.
- Adding missing RSA headlines, descriptions, sitelinks and approved assets.

Usually not because of the score:
- Switching to maximize conversions without a healthy conversion signal.
- Search partners.
- Broad match expansion.
- Adding keywords just to raise the score.

## Suggested structure

1. **Winner campaign:** the smallest set of terms that clearly expresses the winning intent.
2. **Observation campaign or ad group:** dirty but valuable signals, kept apart.
3. **Time-bound campaign:** only the current priority events or seasons.
4. **Brand and competitor:** separate budgets; competitor terms exact or phrase match only.

## When someone asks "why is this ad not working"

Answer in business terms first, in this order:

1. Is there real volume?
2. Are there real conversions, and is tracking healthy?
3. Is traffic going to the wrong intent?
4. Or is it only a low score?

Before touching the account, state the scope of the change: low-risk cleanup only, no budget or bid changes, no live page changes. That makes rollback and review easy.

## Reusable outputs

- Keep/watch/pause table.
- Top zero-conversion waste list.
- Negative keyword candidates from search terms.
- Change log of what was applied.
- Winning-intent seed list for testing the same intent on other channels.
