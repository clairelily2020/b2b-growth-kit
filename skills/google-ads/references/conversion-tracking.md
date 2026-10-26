# Conversion tracking

No bid strategy, keyword decision or CPA target is meaningful until this is healthy.

## Read the goal and action statuses correctly

| What the UI shows | What it means | What to do |
|---|---|---|
| Recording conversions | The action is counting | Confirm it counts the right event once |
| No recent conversions | The tag fired in the past but not recently | Check traffic volume first; then check whether the tag or form changed |
| Inactive / unverified | Nothing has been received | Install or fix the tag or import |
| Goal category "Misconfigured" or "needs attention" | The goal exists but has no working primary action, or the actions conflict | Assign one healthy primary action, or remove the empty goal |

"No recent conversions" and "never worked" are different problems. Check the action's history over the full date range before concluding.

## Where does the tag fire?

Open the conversion action's page-level view (for site tags, the list of webpages where the tag was detected). Check:

- The tag fires on the success state (thank-you page or submit event), not on the form page view.
- Every landing page used by ads appears in the list.
- Pages with historical conversions but none recently point to a page or form change.

## One event, one primary action

It is common to find the same business event tracked several ways: a site tag, an analytics import and an offline upload, all marked primary. That double-counts or splits the signal.

- Pick one source of truth per event as primary.
- Set the others to secondary, or remove them.
- Keep the funnel stages distinct: lead, qualified lead, opportunity, customer. Empty goal categories for later stages mean bidding only ever sees the top of the funnel.

## Moving beyond form fills

Lead forms are an early, noisy signal in B2B. When possible, import later stages:

- Qualified lead or opportunity from the CRM (offline conversion import keyed on click ID, or enhanced conversions for leads).
- Customer or subscription events from the product or billing system.

These let automated bidding optimize for buyers instead of form fillers. They also need consent and data-handling review; see the outreach and evidence policies.

## Tag and analytics setup pattern

1. Define the event in your tag manager, triggered on the success state (form submit success, thank-you page, confirmed booking).
2. Send it to analytics and mark it as a key event or conversion there, or use a native ads conversion tag.
3. Import into Google Ads or link the native tag; set it as primary for the goal.
4. Allow time for data to flow (often a day or two) before judging.

## Troubleshooting

- **Event not firing:** use the tag manager preview; check trigger conditions and whether the tag is paused.
- **In the tag manager but not in analytics:** check the measurement ID and the analytics debug view.
- **In analytics but not in Ads:** the event must be marked as a conversion first, then imported; allow for delay.
- **Double counting:** duplicate tags, several analytics configuration tags, or the same event imported and tagged natively.
- **Conversions on the wrong page:** the trigger is page view instead of success.

## Before changing bids

- [ ] One healthy primary action per goal
- [ ] It fires on success, once per conversion
- [ ] All ad landing pages covered
- [ ] Recent conversion volume is enough for the bid strategy you plan
- [ ] Later-stage imports planned or explicitly out of scope
