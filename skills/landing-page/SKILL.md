---
name: landing-page
description: Plan, write and QA an isolated B2B campaign landing page that matches the ad or search intent, carries one offer and one primary CTA, has working tracking, and does not touch the rest of the site. Use for campaign or ad landing pages, offer pages, show or event pages, landing page copy, A/B test variants, or landing page audits.
---

# Landing page

A campaign page has one job: turn a specific visitor intent into one action. Everything on it either supports that action or goes.

## When to use

- A new campaign, ad group, offer or event needs a destination.
- An existing landing page converts poorly.
- Setting up an A/B test on a page.
- Not for changing the main site navigation, homepage or design system.

## Inputs

- Profile: `positioning`, `offer` (CTA, UTM), `claims`, `measurement.conversion_events`, `voice`.
- Traffic source and intent (ad group keywords, ad copy, email, social post).
- Proof available: reviewed evidence, customer quotes with permission, product screenshots.

## Process

1. **Match intent.** Write the visitor's exact question or keyword and make the headline answer it. The ad's promise and the page's first screen must say the same thing.
2. **One offer, one primary CTA**, chosen with [offer-design](../offer-design/SKILL.md). A secondary CTA is allowed only for a lower-commitment step of the same offer.
3. **Structure that earns the action:**
   - Hero: headline (who it is for and the outcome), one line on how, primary CTA.
   - Proof: one strong item (named customer with permission, a sourced metric, or a real screenshot).
   - Three benefits written as outcomes, each with a real product visual.
   - How it works in three steps.
   - Objections answered (FAQ from real sales and support questions).
   - Second CTA.
4. **Copy rules:** customer words beat invented ones; specific numbers with sources or none; competitor comparisons are factual and neutral.
5. **Isolation:** put the page in the campaign pages area (or the platform equivalent), scope its styles and scripts, record it in a page inventory (URL, page ID, owner, campaign, status). Do not change shared components or established URLs without wider approval.
6. **Tracking:** UTMs preserved, primary conversion event from the profile fires once per conversion, form or button tested end to end, no test click IDs in published links.
7. **Testing:** change one variable per test (headline, offer, proof, CTA). Decide sample size and duration before starting; low-traffic B2B pages often need weeks.
8. **QA** on desktop and mobile with [prepublish-qa](../prepublish-qa/SKILL.md).

## Output

```markdown
Intent / source / offer / primary CTA and URL / success event
## Page copy by section
## Proof used (with source for each)
## Tracking plan (events, UTMs, test performed)
## Inventory entry
## QA results (each check: pass, fail or not run)
## Test plan (if any): variable, hypothesis, metric, sample or duration, stop rule
```

## Gates

- Product claims map to proof points; see [evidence-and-claims](../b2b-growth-kit/policies/evidence-and-claims.md). No promised leads, meetings or revenue.
- Publishing requires approval for this page and version, and a check of the live URL afterwards; see [approval-gates](../b2b-growth-kit/policies/approval-gates.md).
- Checks not run are reported as unverified, never as passed.

## References

- Ad copy that sends traffic here: [google-ads](../google-ads/SKILL.md), [ad-creative](../ad-creative/SKILL.md)
- The harness checks a landing draft deterministically: `python3 -m b2b_harness landing` in the repo's `harness/` folder.
